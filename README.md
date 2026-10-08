# vaulted-social

Graphics and tooling for Vaulted's Facebook and LinkedIn posts. Images live here so scheduled posts can point at stable public links.

Cadence: Facebook 3 posts a day (morning, afternoon, evening), LinkedIn 1 post each weekday. The slot times are the SLOTS table in `tools/slots.py` (Eastern time). Buffer's own posting schedule is not used and cannot be edited through its API, so every post is created with mode `customScheduled` and an exact `dueAt`. Buffer's free plan holds 10 scheduled posts per channel, so the Sunday build queues up to the cap and holds the rest in the plan; the daily top-up (Monday to Saturday) queues held posts as slots free up.

- `images/<post date>/<HHMM>-<fb|li>-<topic>.png` - one 2160x2160 graphic per post. Buffer links to these URLs until the post is published, so do not rename or delete a graphic after its post is queued.
- `plans/<Monday date>.json` - the week's posts (text, alt text, sources, status queued/held/missed).
- `ledger.json` - every topic already used, with figures and sources.
- `topic_bank.json` - unused topic ideas (ideas only, not facts; every claim is researched at build time).
- `tools/` - graphics library (`gfx_lib.py`), slot calculator (`slots.py`), plan checker (`check_plan.py`), the brief each post-building subagent follows (`post_brief.md`), and per-post graphic builders under `tools/weeks/`.
