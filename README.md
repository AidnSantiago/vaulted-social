# vaulted-social

Graphics and tooling for Vaulted's Facebook and LinkedIn posts. Images live here so scheduled posts can point at stable public links.

- `images/<post date>/<HHMM>-<fb|li>-<topic>.png` - one 2160x2160 graphic per post. Buffer links to these URLs until the post is published, so do not rename or delete a graphic after its post is queued.
- `plans/<Monday date>.json` - the week's posts (text, alt text, sources, status).
- `ledger.json` - every topic already used, with sources.
- `tools/` - graphics library, slot calculator and plan checker used by the weekly routine.
