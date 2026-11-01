#!/usr/bin/env python3
"""Graphic for judgment liens. Run from repo root: python3 tools/weeks/2026-11-02-judgment-liens.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def state_card(x, y, w, h, name, l1, l2):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs mono gold" style="left:24px;top:20px;font-size:32px">{name}</div>'
            f'<div class="abs" style="left:24px;top:76px;width:{w-48}px;font-size:19px;line-height:27px;font-weight:700;color:#F0EDE4">{l1}</div>'
            f'<div class="abs" style="left:24px;top:136px;width:{w-48}px;font-size:17px;line-height:25px;color:#A5B2C3">{l2}</div></div>')

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:272px">How a judgment can reach real property</div>'
    b += step_cards([
        (1, "Judgment", "A court rules against the borrower.", None),
        (2, "Abstract", "Paperwork is recorded or entered in a county record.", None),
        (3, "Lien", "The judgment can attach to the borrower&#39;s real property.", None),
    ], top=306, h=196)
    b += '<div class="abs lbl" style="left:68px;top:530px">Two states, two wordings</div>'
    b += state_card(68, 562, 458, 200, "TEXAS", "Recorded and indexed abstract attaches to real property.", "Includes property acquired after recording.")
    b += state_card(554, 562, 458, 200, "MISSOURI", "No lien until an abstract is entered in a record.", "Liens rank by sequence of entry.")
    b += panel(786, 88, "VARIES BY STATE", "Search county records, then ask a title professional how local law ranks it.", 470, 24)
    foot = ("Sources: Texas Property Code 52.001 (page dated 2025-05-26); Missouri Revised Statutes 511.500 (effective 1997-08-28). "
            "Statutes have exceptions, including exempt property in Texas. Not legal advice.")
    return shell("A judgment is not a lien", "until it reaches the record.", "In Texas and Missouri, recording or entry is the step that matters.", b, foot, 896)

PAGES = {"judgment-liens": ("images/2026-11-07/0932-fb-judgment-liens.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
