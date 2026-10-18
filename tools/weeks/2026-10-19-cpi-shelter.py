#!/usr/bin/env python3
"""Graphic for BLS CPI shelter reading (LinkedIn, Tue Oct 20, 2026 10:21 am ET). Built Oct 18, 2026.
Run from repo root: python3 tools/weeks/2026-10-19-cpi-shelter.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    hi, lo = 2250 * 1.05, 2250 * 1.028
    assert round(hi, 2) == 2362.50 and round(lo) == 2313 and round(hi - lo, 2) == 49.5 and round((hi - lo) * 12) == 594
    b = '<div class="abs lbl" style="left:68px;top:268px">12-month change, September 2026, percent</div>'
    X0, S, H = 330, 150, 52
    rows = [("Rent of primary residence", 2.8, "seg-blue"), ("Shelter", 3.2, "seg-steel"), ("Owners equivalent rent", 3.3, "seg-gold")]
    y = 310
    for lab, v, cls in rows:
        b += f'<div class="abs" style="left:68px;top:{y}px;width:250px;height:{H}px;display:flex;align-items:center;font-size:19px;font-weight:700">{lab}</div>'
        b += (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{v*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:21px">{v:.1f}</div>')
        y += H + 18
    b += '<div class="abs lbl" style="left:68px;top:534px">Illustrative: rent of $2,250 a month, one year out</div>'
    b += stat_card(68, 570, 290, 150, "$2,362.50", "at 5 percent growth", "2,250 x 1.05", 38)
    b += stat_card(395, 570, 290, 150, "$2,313", "at 2.8 percent growth", "2,250 x 1.028", 42)
    b += stat_card(722, 570, 290, 150, "$594", "less rent per year", "about $50 x 12 months", 46)
    b += panel(748, 92, "Test both", "Lenders can run the numbers at the assumed growth rate and at the published index pace.", 560, 26)
    foot = ("Source: U.S. Bureau of Labor Statistics, CPI news release for September 2026, Oct 14, 2026 (12-month unadjusted changes, CPI-U). "
            "Arithmetic: 2,250 x 1.05 = 2,362.50; 2,250 x 1.028 = 2,313; difference 49.50 a month, 594 a year. The 5 percent rate and the rent are illustrative.")
    return shell("Rent rose 2.8 percent in a year.", "Is your growth assumption close?",
                 "What the latest CPI shelter data means for rent assumptions", b, foot, 866,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"cpi-shelter": ("images/2026-10-20/1021-li-cpi-shelter.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
