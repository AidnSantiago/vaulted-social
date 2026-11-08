#!/usr/bin/env python3
"""Graphic for Fed Financial Stability Report (May 2026, latest edition) CRE findings (LinkedIn, Mon Nov 9, 2026 11:34 am ET).
Run from repo root: python3 tools/weeks/2026-11-09-fed-financial-stability-nov-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def row(y, tag, text):
    return (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:74px">'
            f'<div class="abs mono gold" style="left:20px;top:0;height:74px;display:flex;align-items:center;font-size:17px;width:190px">{tag}</div>'
            f'<div class="abs" style="left:215px;top:0;height:74px;width:700px;display:flex;align-items:center;font-size:19px;line-height:25px;color:#F0EDE4">{text}</div></div>')

def gfx():
    b = stat_card(68, 262, 300, 150, "$3,368B", "CRE credit outstanding", "end of 2025", 44)
    # growth bars
    b += '<div class="abs" style="left:402px;top:262px;font-size:19px;font-weight:700">Annual growth of CRE credit</div>'
    maxw = 520.0
    for y, lab, v, cls in ((300, "Last 12 months", 2.4, "seg-gold"), (356, "Long-run average", 5.9, "seg-steel")):
        w = maxw * v / 5.9
        b += (f'<div class="abs" style="left:402px;top:{y}px;font-size:15px;color:#A5B2C3">{lab}</div>'
              f'<div class="abs {cls} mono" style="left:402px;top:{y+20}px;width:{w:.0f}px;height:30px;border-radius:5px;display:flex;align-items:center;justify-content:flex-end;padding-right:10px;font-size:18px">{v}%</div>')
    b += row(448, "MATURITIES", "A large volume of CRE debt is scheduled to mature over the coming year.")
    b += row(534, "EXTENSIONS", "Lender willingness to extend or modify maturing loans has helped limit forced-sale risk to date.")
    b += row(620, "CAP RATES", "Recovered from 2022 lows to a level just below their historical average.")
    b += panel(718, 96, "ASK AT CLOSING", "How does this borrower repay at maturity if a refinance is not available?", 560, 24)
    foot = ("Source: Federal Reserve Board, Financial Stability Report, May 2026 (released May 8, 2026; page updated May 28, 2026), Table 2.1 and Section 1; "
            "Orrick InfoBytes, May 22, 2026. CRE credit growth is 2024:Q4 to 2025:Q4. Long-run average is 1997 to 2025:Q4.")
    return shell("Fed on commercial real estate:", "maturities are the watch item",
                 "Latest Financial Stability Report, May 2026", b, foot, 842,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"fed-financial-stability-nov-2026": ("images/2026-11-09/1134-li-fed-financial-stability-nov-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
