#!/usr/bin/env python3
"""Graphic for Fed SLOOS July 2026, CRE standards and demand (LinkedIn, Mon Oct 26, 2026 11:34 am ET). Built Oct 25, 2026.
Run from repo root: python3 tools/weeks/2026-10-26-sloos-cre-standards-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# (title, sub, [(label, value, css class)])
CARDS = [("Nonfarm nonresidential", "change in standards, Q2 2026", [("Eased", 13.2, "seg-gold"), ("Tightened", 1.9, "seg-blue")]),
         ("Multifamily", "change in standards, Q2 2026", [("Eased", 15.1, "seg-gold"), ("Tightened", 9.4, "seg-blue")]),
         ("Construction and land", "development, change in demand", [("Weaker", 25.9, "seg-blue"), None])]
SCALE = 8.0   # px per percentage point

def gfx():
    top, h = 268, 470
    base = top + h - 70
    b = ""
    for i, (t, sub, bars) in enumerate(CARDS):
        x = 68 + i * 327
        b += (f'<div class="card" style="left:{x}px;top:{top}px;width:290px;height:{h}px"></div>'
              f'<div class="abs" style="left:{x+20}px;top:{top+18}px;width:250px;font-size:21px;line-height:26px;font-weight:700">{t}</div>'
              f'<div class="abs" style="left:{x+20}px;top:{top+48}px;width:250px;font-size:15px;line-height:20px;color:#8A9BB0">{sub}</div>')
        for j, bar in enumerate(bars):
            bx = x + 40 + j * 118
            if bar is None:
                b += (f'<div class="abs" style="left:{bx}px;top:{base-70}px;width:100px;font-size:15px;line-height:20px;color:#A5B2C3;text-align:center">14 of 54 responding banks</div>')
                continue
            lab, v, cls = bar
            hh = v * SCALE
            b += (f'<div class="abs {cls}" style="left:{bx+5}px;top:{base-hh:.1f}px;width:90px;height:{hh:.1f}px;border-radius:6px 6px 0 0"></div>'
                  f'<div class="abs mono gold" style="left:{bx}px;top:{base-hh-30:.1f}px;width:100px;text-align:center;font-size:19px;line-height:24px">{v}%</div>'
                  f'<div class="abs" style="left:{bx}px;top:{base+10}px;width:100px;text-align:center;font-size:16px;color:#A5B2C3">{lab}</div>')
        b += f'<div class="abs" style="left:{x+20}px;top:{base}px;width:250px;height:1px;background:rgba(138,155,176,.45)"></div>'
    b += panel(766, 70, "BY LOAN TYPE", "Bank appetite varies by loan type, not one headline.", 430, 24)
    foot = ("Source: Federal Reserve Board, July 2026 Senior Loan Officer Opinion Survey, Table 1 (last updated Aug 3, 2026); survey covers the second quarter of 2026. "
            "Bars are percent of responding banks. Standards: Q8 nonfarm nonresidential, Q9 multifamily; demand: Q10 construction and land development, 14 of 54 banks.")
    return shell("Banks eased on some CRE loans.", "Construction demand weakened.",
                 "Fed loan officer survey, second quarter 2026", b, foot, 864,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"sloos-cre-standards-2026": ("images/2026-10-26/1134-li-sloos-cre-standards-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
