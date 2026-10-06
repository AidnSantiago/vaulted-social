#!/usr/bin/env python3
"""Work out which Buffer posting slots still need a post.

The model must not do day-of-week, daylight-saving or UTC arithmetic in its head. Use this instead.

    python3 tools/slots.py --queue /tmp/queue.json [--now 2026-10-11T18:30:00-04:00] [--cap 10]
                           [--schedule fb=/tmp/fb_schedule.json] [--schedule li=/tmp/li_schedule.json]

--queue      JSON list of already scheduled posts: [{"channel": "fb" | "li", "dueAt": "2026-10-12T21:27:00.000Z"}, ...]
             (copy channelService + dueAt out of Buffer's list_posts result; "facebook"/"linkedin" also work)
--now        Defaults to the real current time. Everything is computed in America/New_York.
--cap        Scheduled posts a channel may hold at once (Buffer free plan: 10 per channel).
--extend-days N  Rehearsals only: move the end of the window N days later.
--schedule   Optional override of a channel's weekly slots, in the shape Buffer's get_channel returns as
             postingSchedule: [{"day": "mon", "times": ["17:27"], "paused": false}, ...].
             Buffer is the source of truth. If get_channel shows different times than SLOTS below, pass them here.

Window: from now until the end of the coming Sunday (if today is Sunday: the Sunday a week away), so a Sunday-evening run
covers Monday-Sunday and a Thursday run covers through that Sunday.

Output: a readable table, then a JSON block (between ---JSON--- markers) with every open slot:
{"channel", "slot_local", "slot_utc", "day", "action": "queue_now" | "hold"}.
queue_now = within the channel's remaining capacity (earliest open slots first); hold = open, but the cap is reached.
"""
import argparse, json, sys
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")
DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

SLOTS = {  # default weekly slots (ET); keep in sync with Buffer
    "fb": {"mon": ["17:27"], "tue": ["09:15", "17:27"], "wed": ["08:56", "17:27"], "thu": ["08:25", "17:27"],
           "fri": ["08:00", "17:27"], "sat": ["17:27"], "sun": ["10:15", "17:27"]},
    "li": {"wed": ["17:09"], "thu": ["15:40"], "fri": ["14:00"]},
}
CHANNEL_ALIASES = {"facebook": "fb", "fb": "fb", "linkedin": "li", "li": "li"}


def parse_dt(s):
    s = s.strip().replace("Z", "+00:00")
    d = datetime.fromisoformat(s)
    return d if d.tzinfo else d.replace(tzinfo=ET)


def load_schedule(path):
    data = json.load(open(path))
    out = {}
    for row in data:
        if row.get("paused"):
            continue
        out[row["day"][:3].lower()] = list(row.get("times") or [])
    return out


def window_end(now):
    """Last moment of the coming Sunday (a week out if today is Sunday)."""
    days_ahead = (6 - now.weekday()) % 7  # Sunday weekday() == 6
    if days_ahead == 0:
        days_ahead = 7
    end_day = (now + timedelta(days=days_ahead)).date()
    return datetime.combine(end_day, time(23, 59, 59), ET)


def slots_between(sched, start, end):
    d = start.date()
    out = []
    while d <= end.date():
        for hhmm in sched.get(DAYS[d.weekday()], []):
            h, m = (int(x) for x in hhmm.split(":"))
            t = datetime.combine(d, time(h, m), ET)
            if start < t <= end:
                out.append(t)
        d += timedelta(days=1)
    return sorted(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue", required=True)
    ap.add_argument("--now")
    ap.add_argument("--cap", type=int, default=10)
    ap.add_argument("--extend-days", type=int, default=0, help="push the end of the window out by N days (rehearsals only)")
    ap.add_argument("--schedule", action="append", default=[])
    a = ap.parse_args()

    now = parse_dt(a.now).astimezone(ET) if a.now else datetime.now(ET)
    end = window_end(now) + timedelta(days=a.extend_days)
    sched = {k: dict(v) for k, v in SLOTS.items()}
    for item in a.schedule:
        ch, path = item.split("=", 1)
        sched[CHANNEL_ALIASES[ch]] = load_schedule(path)

    queue = json.load(open(a.queue))
    taken = {"fb": [], "li": []}
    for q in queue:
        ch = CHANNEL_ALIASES.get(str(q.get("channel", q.get("channelService", ""))).lower())
        if ch:
            taken[ch].append(parse_dt(q["dueAt"]).astimezone(ET))

    print(f"now {now:%a %Y-%m-%d %H:%M %Z}   window ends {end:%a %Y-%m-%d %H:%M %Z}   cap {a.cap} scheduled per channel")
    result = []
    for ch, label in (("fb", "FACEBOOK"), ("li", "LINKEDIN")):
        used = len(taken[ch])
        capacity = max(0, a.cap - used)
        slots = slots_between(sched[ch], now, end)
        open_slots = [s for s in slots if not any(abs((s - t).total_seconds()) < 90 for t in taken[ch])]
        print(f"\n{label}: {used} scheduled now, capacity {capacity}, {len(slots)} slots in window, {len(open_slots)} open")
        for i, s in enumerate(open_slots):
            action = "queue_now" if i < capacity else "hold"
            print(f"  {s:%a %Y-%m-%d %H:%M %Z}  {s.isoformat()}  utc {s.astimezone(UTC):%Y-%m-%dT%H:%MZ}  {action}")
            result.append({"channel": ch, "slot_local": s.isoformat(), "slot_utc": s.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
                           "day": s.strftime("%a"), "action": action})
    print("\n---JSON---")
    print(json.dumps(result, indent=1))
    print("---JSON---")


if __name__ == "__main__":
    sys.exit(main())
