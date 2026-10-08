# Brief: build ONE post (text, sources, graphic) for Vaulted

Used by the Sunday weekly build and the daily top-up. The orchestrator pastes this whole file into a subagent's prompt, followed by an ASSIGNMENT block.

Vaulted (vaultedonline.com) is software for private and hard money real estate lenders. Its Facebook Page and LinkedIn profile publish short educational posts for private and hard money lenders and new investors. You build exactly ONE post, described in your ASSIGNMENT. Be efficient: you are one of several people building posts in parallel.

## ASSIGNMENT (given after this brief)
channel (fb or li); slot_local (ISO time with offset, Eastern); topic key; kind (evergreen or data); format; angle; illustrative example numbers to use; numbers to avoid; a backup topic; the week's Monday date (YYYY-MM-DD); today's date.

## Boundaries
- Work only in /home/claude/vaulted-social (a public git repo, already cloned) and /tmp. Create only the files listed under DELIVERABLES. Do not edit or delete any existing file. Do NOT run any git command. Do NOT call Buffer, Gmail or any other connector tool. Do not print or store secrets.
- Before designing, read: the docstring of tools/check_plan.py (plan entry schema), tools/gfx_lib.py (graphics helpers), and one or two worked builders under tools/weeks/ (tools/weeks/2026-10-05-*.py are single-post builders; tools/weeks/2026-10-06.py has eight). Look at two existing PNGs under images/ (downscale a copy to 1080 px with PIL into /tmp, then Read the copy) to learn the house style.

## Rules (non-negotiable)
1. Never invent a fact, number, date, quote or source. Every figure in the post or graphic must come from a page you opened with WebFetch during this task, or be arithmetic you computed in Python (show the calculation), or be an illustrative input you chose yourself (label it "illustrative" in derived). If you cannot verify a claim, drop it or change the angle. If you cannot build a verified post on your topic after real effort, switch to the backup topic in your assignment and say so.
2. Provide real value: teach a lender something concrete (a mechanic, a worked example with numbers, or a verified data point and what it means for a lender). No filler, no hype, no generic motivation.
3. No claims about what Vaulted's software does or will do. No legal, tax or investment advice. Where law or practice varies, say "varies by state" or "varies by lender". Plain, educational tone.
4. Do not state a "general practice", "typically" or "most lenders" claim unless a source you opened says it. For process suggestions use "can" wording ("Lenders can confirm...") instead of asserting what lenders do. Do not word a claim more strongly than its source does (a source that says "may" gives you "may").
5. Research: WebSearch (standard mode first) for primary or highly credible sources (government, data firms, industry bodies, law firms, trade publications, not marketing fluff). HOW TO REACH A PAGE: in unattended runs WebFetch only accepts an address that came from a WebSearch result or from a page you already fetched. Never type or guess an address from memory and never retry a failed one; if you need a particular site's page, run WebSearch with allowed_domains set to that site's domain and a query naming the page, then fetch the address exactly as listed. Open each page with WebFetch and ask for the exact figures or definitions as verbatim quotes plus the page's publish or update date. Confirm every figure you will print with a second, quote-only fetch (summaries can be lossy). For an insurance, legal, tax or regulatory definition, confirm it against a second independent source. If sources disagree, use a range and name the source, or drop the claim. If a page has no date, record the date as "<today> (accessed; page undated)" and put "page undated, accessed <date>" in the graphic footnote. Prefer dated sources.
6. Not usable: "$155 billion" as 2025 origination volume (untraceable); single-figure draw inspection fees or timing; invented lists of draw milestones.
7. Do not repeat topics already used: read ledger.json and never reuse a key or its headline figures within 12 weeks. Do not reuse the example numbers listed under "numbers to avoid" in your assignment, or any example number in ledger.json's figures from the last 12 weeks. Use the example numbers suggested in your assignment.
8. Weekly-changing data (mortgage rates, weekly indexes) must say "as of <date>" in the post and the graphic.

## Writing spec
- Facebook: 75 to 100 words, not counting the final line. The final line is exactly: vaultedonline.com (on its own line, after a blank line).
- LinkedIn: 75 to 100 words, no link, no hashtags, no apostrophes (write "does not", rephrase possessives) and none of these characters: ( ) [ ] { } < > @ # * _ ~ | \ . Spell out "percent". No final link line.
- Open with a specific hook (a question, a number, or a short real situation). Give the useful mechanic with numbers. Close with a plain takeaway.
- Plain language. Short paragraphs separated by a blank line. Straight quotes. No emojis, no hashtags, no em or en dashes (use commas and periods), no exclamation marks. Do not write "Vaulted can/will/helps ..." and do not mention the product.
- Alt text for the graphic: 40 to 420 characters describing what it shows and its key figures.

## Graphic spec
- One 2160x2160 PNG (1080x1080 CSS pixels at 2x) built with tools/gfx_lib.py (shell, panel, stat_card, step_cards, render and plain HTML/CSS inside the body). House style: navy gradient, gold/steel/cream palette, small-caps eyebrow, a two-line serif headline (first line cream, second line gold, each at most 38 characters), a one-line subtitle, ONE clear visual that shows the post's numbers or mechanism (bar chart, timeline, step cards, stat cards, formula with an example, comparison cards, waterfall), a dashed takeaway panel, a source footnote naming each source with its date, and the Vaulted mark (the shell adds it). Choose a layout that differs from the other posts in the same week.
- Every number on the graphic must be in the post, in a source quote, or be arithmetic noted in the footnote. No product claims. Wording on the graphic must not claim more than the post does.
- Image path: images/<YYYY-MM-DD>/<HHMM>-<fb|li>-<slug>.png, where date and time are the slot's local Eastern date and 24-hour time (for example images/2026-10-12/1727-fb-cross-collateral.png).
- Render with gfx_lib.render. Read every WARN line it prints (overlapping text, text at a box edge, a line over text, outside the frame) and fix each one. Then open the PNG (downscaled copy) with Read and LOOK at it: orphaned words, awkward wraps, a footnote crowding the Vaulted mark, bars that do not match their numbers. Fix and re-render until clean (at most 5 renders).
- Builder script skeleton:
```python
#!/usr/bin/env python3
"""Graphic for <topic>. Run from repo root: python3 tools/weeks/<Monday>-<slug>.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    body = ...
    return shell("Headline line one", "headline line two", "subtitle", body, "Source: ... (date). Arithmetic: ...", 840)

PAGES = {"<slug>": ("images/<YYYY-MM-DD>/<HHMM>-<fb|li>-<slug>.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
```

## DELIVERABLES (create exactly these)
1. Plan entry JSON at /tmp/parts/<topic-key>.json (mkdir -p /tmp/parts), written with Python json.dump, one object with these fields: channel; slot_local (from the assignment); topic (kebab-case key); kind; text (the full post exactly as it will be posted); alt; image (path as above); sources (list of {title, publisher, url, date, quote}; quote = the verbatim sentence containing the figure or definition you rely on; date = the page's publish or update date as YYYY-MM-DD); derived (list of {figure, calc}: every illustrative input and every computed number in the post or graphic, with the Python expression and result); status "planned"; buffer_id null.
2. The builder script tools/weeks/<Monday>-<slug>.py and the rendered PNG at the image path, 2160x2160.
3. Validation: write a one-post plan {"week_start": "<Monday>", "posts": [your entry]} to /tmp/parts/check_<topic-key>.json and run `cd /home/claude/vaulted-social && python3 tools/check_plan.py /tmp/parts/check_<topic-key>.json`. It must print OK. Fix every FAIL; look at every WARN (a figure not found in a source quote or in derived must be added to derived or removed).

## Final answer (under 170 words)
Topic key and slug; the full post text; each figure with its source (publisher, date); anything you are unsure of or any fallback you took; the file paths you created.
