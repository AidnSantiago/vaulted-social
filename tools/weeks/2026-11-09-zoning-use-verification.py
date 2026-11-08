#!/usr/bin/env python3
"""Graphic for zoning-use-verification (Facebook, Sat Nov 14, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-zoning-use-verification.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render, CHK
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def item(y, title, desc):
    return (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:100px"></div>'
            f'<div class="abs" style="left:92px;top:{y+37}px">{CHK}</div>'
            f'<div class="abs" style="left:140px;top:{y+16}px;font-size:23px;font-weight:700;color:#F0EDE4;white-space:nowrap">{title}</div>'
            f'<div class="abs" style="left:140px;top:{y+52}px;font-size:17px;color:#A5B2C3;white-space:nowrap">{desc}</div>')

def gfx():
    b = item(262, "Zoning district, in writing", "Cities can issue a zoning verification letter")
    b += item(374, "Is the planned use permitted?", "The district alone does not answer it")
    b += item(486, "Is the current use nonconforming?", "Status can be lost after abandonment or destruction")
    b += item(598, "Code violations, asked separately", "Some cities handle Fire Code requests apart from the letter")
    b += panel(722, 96, "ASK IN WRITING", "A letter may not say whether existing<br>development meets current code.", 440, 26)
    foot = ("Sources: City of Orlando, Request a Zoning Verification Letter (page undated, accessed 2026-11-08); City of Sioux Falls, Zoning Verification Requests "
            "(page undated, accessed 2026-11-08); Gary D. Taylor, Iowa State University, Nonconforming Uses aka Grandfathered Uses in Zoning (page undated, accessed 2026-11-08); "
            "IRMI, Nonconforming Use (page undated, accessed 2026-11-08). Varies by city. Not legal advice.")
    return shell("Check zoning before you fund", "a conversion or multi-unit.", "A short checklist for verifying permitted use", b, foot, 836, eyebrow="ZONING DILIGENCE FOR LENDERS")

PAGES = {"zoning-use-verification": ("images/2026-11-14/1727-fb-zoning-use-verification.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
