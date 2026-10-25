#!/usr/bin/env python3
"""Graphic for Census rental vacancy rate, Q2 2026 (LinkedIn, Tue Oct 27, 2026 10:21 am ET). Built Oct 25, 2026.
Run from repo root: python3 tools/weeks/2026-10-26-rental-vacancy-census.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# (label, vacancy percent, bar style)
ROWS = [("3% vacancy", 3.0, "seg-blue"), ("5% vacancy", 5.0, "seg-blue"),
        ("7.3% vacancy", 7.3, "seg-gold"), ("10% vacancy", 10.0, "seg-blue")]

def gfx():
    b = stat_card(68, 268, 300, 150, "7.3%", "rental vacancy, Q2 2026", "Census Bureau, national")
    b += stat_card(392, 268, 300, 150, "7.0%", "rental vacancy, Q2 2025", "Not statistically different")
    b += ('<div class="abs lbl" style="left:68px;top:452px">Rent left per $100 of potential rent (illustrative)</div>')
    X0, W, H = 250, 700, 46
    y = 490
    for lab, v, cls in ROWS:
        kept = 100 - v
        w = W * kept / 100
        vw = W * v / 100
        b += (f'<div class="abs" style="left:68px;top:{y}px;height:{H}px;width:175px;display:flex;align-items:center;font-size:19px;font-weight:700">{lab}</div>')
        b += (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{w:.1f}px;height:{H}px;border-radius:6px 0 0 6px;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:19px">${kept:.2f}</div>')
        b += (f'<div class="abs" style="left:{X0 + w:.1f}px;top:{y}px;width:{vw:.1f}px;height:{H}px;border:1.5px dashed rgba(138,155,176,.55);border-left:none;border-radius:0 6px 6px 0"></div>')
        y += H + 16
    b += ('<div class="abs" style="left:250px;top:{0}px;font-size:14.5px;color:#A5B2C3">'
          'Solid bar: rent left after vacancy. Dashed: vacancy. The 3% to 10% range is one trade source.</div>').format(y - 2)
    b += panel(y + 44, 96, "HIGHER VACANCY, LOWER NOI", "A national rate is not a local one.", 330, 25)
    foot = ("Sources: U.S. Census Bureau, Quarterly Residential Vacancies and Homeownership, Q2 2026 (Jul 28, 2026); "
            "Scotsman Guide, Not An Exact Science (Nov 15, 2019). Arithmetic: 100 minus vacancy percent; 5% shown is illustrative. "
            "Q3 2026 release is scheduled for Oct 28, 2026.")
    return shell("Rental vacancy was 7.3% in Q2.", "What it does to rent.",
                 "Census rental vacancy rate and an income underwriting lens", b, foot, y + 160,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"rental-vacancy-census": ("images/2026-10-27/1021-li-rental-vacancy-census.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
