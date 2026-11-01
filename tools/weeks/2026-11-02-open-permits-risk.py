#!/usr/bin/env python3
"""Graphic for open-permits-risk (Facebook, Tue Nov 3, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-open-permits-risk.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def row(y, label, head, text, src):
    s = f'<div class="card" style="left:68px;top:{y}px;width:944px;height:150px"></div>'
    s += f'<div class="abs" style="left:68px;top:{y}px;width:6px;height:150px;border-radius:14px 0 0 14px;background:linear-gradient(180deg,#E2C264,#B8963F)"></div>'
    s += f'<div class="abs lbl" style="left:104px;top:{y+24}px">{label}</div>'
    s += f'<div class="abs mono gold" style="left:104px;top:{y+60}px;font-size:25px;line-height:30px;width:250px">{head}</div>'
    s += f'<div class="abs" style="left:400px;top:{y+22}px;width:580px;height:106px;display:flex;flex-direction:column;justify-content:center;font-size:21px;line-height:29px;font-weight:700;color:#F0EDE4">{text}</div>'
    s += f'<div class="abs steel" style="left:400px;top:{y+112}px;font-size:14px;white-space:nowrap;display:none">{src}</div>'
    return s

def gfx():
    b = row(262, "WHERE IT SHOWS UP", "VALUE", "Unpermitted space may not count as official gross living area, even if the work looks high quality.", "")
    b += row(432, "WHERE IT SHOWS UP", "INSURANCE", "Unpermitted additions may not be covered under a homeowner's policy.", "")
    b += row(602, "WHERE IT SHOWS UP", "CLOSING", "With an open permit on record, a lender may not know if the work was finished properly and may suspend the mortgage.", "")
    b += panel(790, 100, "CHECK EARLY", "Lenders can check permit records and ask for final sign-offs. Varies by state and lender.", 470, 26)
    foot = ("Sources: AAA AMC, Permits and Unpermitted Additions (May 20, 2026); Shovels, What Is Unpermitted Work (May 6, 2026); "
            "Lendworth, Open Permit or Unpermitted Addition Found Before Your Florida Mortgage Closing (Sep 1, 2026). Each source uses \"may\" wording.")
    return shell("Open permits can", "reach your loan file", "Value, insurance and closing", b, foot, 912)

PAGES = {"open-permits-risk": ("images/2026-11-03/1727-fb-open-permits-risk.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
