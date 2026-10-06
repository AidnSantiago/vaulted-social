#!/usr/bin/env python3
"""Check a weekly plan file against the house rules before anything is pushed or queued.

    python3 tools/check_plan.py plans/2026-10-12.json [--skip-images] [--schedule fb=/tmp/fb.json] [--schedule li=/tmp/li.json]

Prints FAIL (must fix) and WARN (look at it) lines, then OK or NOT OK. Exit code 1 when NOT OK.

Plan file shape (one file per week, named for the Monday of the week):
{
  "week_start": "2026-10-12",
  "posts": [
    {
      "channel": "fb" | "li",
      "slot_local": "2026-10-12T17:27:00-04:00",          # exact Buffer slot, from tools/slots.py
      "topic": "cross-collateralization",                 # kebab-case key, also written to ledger.json
      "kind": "evergreen" | "data",
      "text": "full post text exactly as it will be posted",
      "alt": "alt text for the graphic (40-420 characters)",
      "image": "images/2026-10-12/1727-fb-cross-collateralization.png",
      "sources": [{"title": "", "publisher": "", "url": "https://...", "date": "2026-09-30", "quote": "verbatim sentence with the figure"}],
      "derived": [{"figure": "$2,057", "calc": "payment on $200,000 at 12% over 30 years, computed in Python"}],
      "status": "planned" | "queued" | "held" | "missed",
      "buffer_id": null
    }
  ]
}
Every number in the text should appear in a source quote or be listed under "derived" with the calculation.
"""
import argparse, json, os, re, struct, sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import slots as slotmod  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, ".."))
ET = ZoneInfo("America/New_York")
LI_RESERVED = set("()[]{}<>@#*_~|\\")
APOSTROPHES = "'’‘`"
BANNED = ["$155 billion", "155 billion", "guaranteed return", "risk-free", "risk free", "can't lose", "cannot lose"]
PRODUCT_CLAIMS = re.compile(r"\b(vaulted (will|can|lets|helps|automat|tracks|manages|sends)|with vaulted|our (software|platform|app|product|tool)|vaulted'?s? (software|platform|app|feature))", re.I)
STATUSES = {"planned", "queued", "held", "missed"}


def words(text):
    body = re.sub(r"(?im)^\s*vaultedonline\.com\s*$", "", text)
    return len(body.split())


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    w, h = struct.unpack(">II", head[16:24])
    return w, h


def norm_num(tok):
    t = tok.replace("$", "").replace(",", "").replace("%", "")
    if "." in t:
        t = t.rstrip("0").rstrip(".")
    return t


def numbers_in(text):
    out = []
    for m in re.finditer(r"\$?\d[\d,]*(?:\.\d+)?%?", text):
        tok = m.group(0).rstrip(",.")
        n = norm_num(tok)
        small_plain = ("$" not in tok and "%" not in tok and "." not in tok and len(n) <= 2)
        is_year = bool(re.fullmatch(r"(19|20)\d\d", n)) and "$" not in tok and "%" not in tok
        if small_plain or is_year:
            continue
        out.append((tok, n))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--schedule", action="append", default=[])
    ap.add_argument("--ledger", default=os.path.join(ROOT, "ledger.json"))
    ap.add_argument("--skip-images", action="store_true", help="text stage: do not require the PNG files to exist yet")
    a = ap.parse_args()

    fails, warns = [], []
    F = lambda i, m: fails.append(f"FAIL post {i}: {m}")
    W = lambda i, m: warns.append(f"WARN post {i}: {m}")

    plan = json.load(open(a.plan))
    posts = plan.get("posts", [])
    if not posts:
        fails.append("FAIL: plan has no posts")
    sched = {k: dict(v) for k, v in slotmod.SLOTS.items()}
    for item in a.schedule:
        ch, path = item.split("=", 1)
        sched[slotmod.CHANNEL_ALIASES[ch]] = slotmod.load_schedule(path)

    ledger = []
    if os.path.exists(a.ledger):
        ledger = json.load(open(a.ledger)).get("entries", [])
    cutoff = datetime.now(ET) - timedelta(weeks=12)

    seen_slots, seen_topics = set(), {}
    for i, p in enumerate(posts, 1):
        ch = p.get("channel")
        text = p.get("text", "")
        if ch not in ("fb", "li"):
            F(i, "channel must be fb or li")
            continue
        # slot
        try:
            slot = datetime.fromisoformat(p["slot_local"]).astimezone(ET)
        except Exception:
            F(i, "slot_local missing or not ISO 8601")
            continue
        hhmm = f"{slot:%H:%M}"
        day = slotmod.DAYS[slot.weekday()]
        if hhmm not in sched[ch].get(day, []):
            F(i, f"{slot:%a %H:%M} is not a {ch} posting slot")
        key = (ch, slot.isoformat())
        if key in seen_slots:
            F(i, "two posts for the same channel and slot")
        seen_slots.add(key)
        # topic
        topic = p.get("topic", "")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", topic):
            F(i, "topic must be a kebab-case key")
        seen_topics.setdefault(topic, set()).add(ch)
        if len(seen_topics[topic]) > 1:
            F(i, f"topic '{topic}' is used on both channels in this plan")
        for e in ledger:
            if e.get("key") != topic:
                continue
            d = e.get("date")
            try:
                recent = (d is None) or datetime.fromisoformat(d).replace(tzinfo=ET) > cutoff
            except Exception:
                recent = True
            if recent:
                F(i, f"topic '{topic}' is already in ledger.json ({d}); pick a new topic or a clearly new angle with a new key")
        # text rules
        n = words(text)
        low = text.lower()
        for b in BANNED:
            if b in low:
                F(i, f"banned phrase: {b}")
        if PRODUCT_CLAIMS.search(text):
            F(i, "reads like a Vaulted product claim; remove it")
        if "—" in text or "–" in text:
            W(i, "contains a dash character (em/en); prefer commas or periods")
        if "#" in text:
            F(i, "hashtags are not used")
        if re.search(r"[\U0001F000-\U0001FFFF☀-➿]", text):
            F(i, "no emoji")
        if ch == "fb":
            if not (75 <= n <= 100):
                F(i, f"Facebook posts are 75-100 words; this has {n}")
            lines = [l for l in text.rstrip().split("\n")]
            if lines[-1].strip() != "vaultedonline.com":
                F(i, "last line must be exactly: vaultedonline.com")
            if re.search(r"https?://", text):
                F(i, "no full URLs in the body")
            if "\n\n" not in text:
                W(i, "use short paragraphs separated by blank lines")
        else:
            if not (60 <= n <= 140):
                F(i, f"LinkedIn posts are 60-140 words; this has {n}")
            bad = sorted({c for c in text if c in LI_RESERVED or c in APOSTROPHES})
            if bad:
                F(i, f"LinkedIn text contains characters to avoid: {bad}")
            if "vaultedonline" in low or re.search(r"https?://", text):
                F(i, "no link in LinkedIn posts")
            if "%" in text:
                W(i, "spell out percent on LinkedIn")
        if re.search(r"\bVaulted\b", text):
            W(i, "mentions Vaulted by name; make sure it is not a product claim")
        # alt + image
        alt = p.get("alt", "")
        if not (40 <= len(alt) <= 420):
            F(i, "alt text must be 40-420 characters")
        img = p.get("image", "")
        m = re.fullmatch(r"images/(\d{4}-\d{2}-\d{2})/(\d{4})-(fb|li)-[a-z0-9]+(-[a-z0-9]+)*\.png", img)
        if not m:
            F(i, "image path must look like images/YYYY-MM-DD/HHMM-fb-slug.png")
        else:
            if m.group(1) != f"{slot:%Y-%m-%d}" or m.group(2) != f"{slot:%H%M}" or m.group(3) != ch:
                F(i, "image path date, time and channel must match the slot")
            full = os.path.join(ROOT, img)
            if a.skip_images:
                pass
            elif not os.path.exists(full):
                F(i, "image file not found: " + img)
            elif png_size(full) != (2160, 2160):
                F(i, f"image must be 2160x2160, got {png_size(full)}")
        # sources and numbers
        srcs = p.get("sources", [])
        if not srcs:
            F(i, "at least one source is required")
        quotes = ""
        for s in srcs:
            if not str(s.get("url", "")).startswith("https://"):
                F(i, "each source needs an https url")
            if not s.get("quote") or not s.get("date") or not s.get("publisher"):
                F(i, "each source needs publisher, date and a verbatim quote")
            quotes += " " + str(s.get("quote", ""))
        known = {norm_num(t) for t, _ in numbers_in(quotes)} | {norm_num(t) for t, _ in numbers_in(" ".join(d.get("figure", "") for d in p.get("derived", [])))}
        for tok, nn in numbers_in(text):
            if nn not in known:
                W(i, f"figure {tok} is not in any source quote or in 'derived'")
        st = p.get("status")
        if st not in STATUSES:
            F(i, f"status must be one of {sorted(STATUSES)}")

    for line in fails + warns:
        print(line)
    ok = not fails
    print("OK" if ok else "NOT OK", f"({len(posts)} posts, {len(fails)} fail, {len(warns)} warn)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
