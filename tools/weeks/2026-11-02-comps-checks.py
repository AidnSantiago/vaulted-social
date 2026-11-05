#!/usr/bin/env python3
"""Graphic for comps-checks (Facebook, Sat Nov 7, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-comps-checks.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, CHK, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ROWS = [
    ("Recency", "When did each comp close?", "Sales closed within the last 12 months should be used. An older sale needs an explanation."),
    ("Distance", "How many miles away is it?", "The appraiser must be specific about distance in miles, measured in a straight line."),
    ("Similarity", "Are size and condition alike?", "Similar site, room count, finished area, style and condition."),
    ("Adjustments", "What supports each one?", "Adjustments must reflect the market, not a rule of thumb."),
]

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:272px">Four checks on the comps behind a value</div>'
    y = 310
    for name, q, g in ROWS:
        b += (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:112px">'
              f'<div class="abs" style="left:22px;top:43px">{CHK}</div>'
              f'<div class="abs mono gold" style="left:66px;top:19px;font-size:22px">{name}</div>'
              f'<div class="abs" style="left:66px;top:55px;width:300px;font-size:20px;line-height:26px;font-weight:700;color:#F0EDE4">{q}</div>'
              f'<div class="abs" style="left:400px;top:17px;width:512px;height:78px;display:flex;align-items:center;font-size:17px;line-height:24px;color:#A5B2C3">{g}</div></div>')
        y += 124
    b += panel(y + 2, 80, "AT LEAST 3 COMPS", "A comp is a recent sale of a similar property. Standards vary by lender.", 470, 24)
    foot = ("Source: Fannie Mae Selling Guide B4-1.3-08, Comparable Sales, and B4-1.3-09, Adjustments to Comparable Sales (both dated 2025-06-04). "
            "Conventional loan guidance, used here as a reference only. Not legal advice.")
    return shell("What is behind the value?", "Check the comps.", "A checklist for reviewing comparable sales in an appraisal", b, foot, 926)

PAGES = {"comps-checks": ("images/2026-11-07/1727-fb-comps-checks.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
