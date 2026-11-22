#!/usr/bin/env python3
"""Graphic for Census rental vacancy Q3 2026 and DSCR. Run from repo root: python3 tools/weeks/2026-11-23-rental-vacancy-q3-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

RENT, PITIA, VAC = 2000, 1500, 0.076

def gfx():
    eff = RENT * (1 - VAC)
    a, b, loss = RENT / PITIA, eff / PITIA, RENT * VAC
    assert f"{a:.2f}" == "1.33" and f"{b:.2f}" == "1.23" and round(loss) == 152 and round(eff) == 1848
    body = '<div class="abs lbl" style="left:68px;top:290px">U.S. rental vacancy rate, Census Bureau</div>'
    rows = [("Q3 2025", 7.1, "#5B7DAE"), ("Q2 2026", 7.3, "#5B7DAE"), ("Q3 2026", 7.6, "#C9A84C")]
    y = 326
    for name, v, col in rows:
        w = 700 * v / 8.0
        body += (f'<div class="abs steel" style="left:68px;top:{y+6}px;font-size:19px;width:110px">{name}</div>'
                 f'<div class="abs" style="left:190px;top:{y}px;width:{w:.0f}px;height:42px;border-radius:8px;background:{col}"></div>'
                 f'<div class="abs mono" style="left:{190+w+14:.0f}px;top:{y+6}px;font-size:24px">{v}%</div>')
        y += 56
    body += '<div class="abs lbl" style="left:68px;top:508px">Illustrative DSCR test, rent divided by PITIA</div>'
    def card(x, t, big, l1, l2, col):
        return (f'<div class="card" style="left:{x}px;top:544px;width:458px;height:184px">'
                f'<div class="abs steel" style="left:24px;top:16px;font-size:18px">{t}</div>'
                f'<div class="abs mono {col}" style="left:24px;top:46px;font-size:58px">{big}</div>'
                f'<div class="abs steel" style="left:24px;top:116px;font-size:17px;line-height:24px;width:410px">{l1}<br>{l2}</div></div>')
    body += card(68, "Full rent", "1.33", "$2,000 rent / $1,500 PITIA", "", "")
    body += card(554, "Rent less 7.6% vacancy", "1.23", "$1,848 rent / $1,500 PITIA", "$152 a month lost", "gold")
    body += ('<div class="panel" style="top:752px;height:104px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">NATIONAL, NOT LOCAL</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:580px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Lenders can test a deal at a market vacancy rate, not only at full rent. Local rates differ.</div></div>')
    return page("light", "DATA", "PRIVATE LENDING, EXPLAINED", "Rental vacancy hit 7.6%", "in Q3 2026",
                "What a higher vacancy rate does to a DSCR test", body,
                "Sources: U.S. Census Bureau, Quarterly Residential Vacancies and Homeownership, Q3 2026 (Oct 28, 2026); LendingTree, DSCR Loan (Nov 4, 2026): DSCR = gross monthly rent / PITIA. "
                "Arithmetic: 2000/1500 = 1.33; 2000 x (1 - 0.076) = 1,848; 1848/1500 = 1.23; 2000 x 0.076 = 152. Rent and payment illustrative.", 888)

PAGES = {"rental-vacancy-q3-2026": ("images/2026-11-25/1709-li-rental-vacancy-q3-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
