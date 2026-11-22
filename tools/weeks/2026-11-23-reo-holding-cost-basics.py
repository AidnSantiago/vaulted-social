#!/usr/bin/env python3
"""Graphic for REO holding cost basics. Run from repo root: python3 tools/weeks/2026-11-23-reo-holding-cost-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ITEMS = [("Property taxes", 540), ("Insurance", 310), ("Utilities", 180), ("Upkeep", 150)]
MONTH = sum(v for _, v in ITEMS)
SIX = MONTH * 6

def gfx():
    assert MONTH == 1180 and SIX == 7080
    track = 620
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative monthly holding costs on one property</div>'
    y = 330
    for name, v in ITEMS:
        w = track * v / 540
        body += f'<div class="abs" style="left:68px;top:{y+10}px;width:190px;font-size:20px;font-weight:700">{name}</div>'
        body += f'<div class="abs" style="left:262px;top:{y}px;width:{w:.0f}px;height:50px;border-radius:8px;background:#5B7DAE"></div>'
        body += f'<div class="abs mono" style="left:278px;top:{y+13}px;font-size:21px;color:#fff">${v:,}</div>'
        y += 66
    body += ('<div class="card" style="left:68px;top:610px;width:458px;height:150px"><div class="abs lbl" style="left:22px;top:18px">Per month</div>'
             f'<div class="abs mono gold" style="left:22px;top:50px;font-size:46px">${MONTH:,}</div>'
             '<div class="abs steel" style="left:22px;top:110px;font-size:17px">540 + 310 + 180 + 150</div></div>')
    body += ('<div class="card" style="left:554px;top:610px;width:458px;height:150px"><div class="abs lbl" style="left:22px;top:18px">Over six months</div>'
             f'<div class="abs mono gold" style="left:22px;top:50px;font-size:46px">${SIX:,}</div>'
             '<div class="abs steel" style="left:22px;top:110px;font-size:17px">1,180 x 6 months</div></div>')
    body += ('<div class="panel" style="top:790px;height:84px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'Lenders can add holding costs to the resale timeline and price. Amounts vary by property and lender.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "After foreclosure,", "the bills start",
                "What holding a property can cost, with an example", body,
                "Sources: Federal Reserve, SR-12-10 OREO Q&amp;A (FAQ dated Jun 28, 2012; page undated, accessed 2026-11-22); FDIC, Other Real Estate Owned guidance (updated Mar 24, 2024). "
                "Arithmetic: 540+310+180+150 = 1,180; 1,180 x 6 = 7,080. Cost amounts illustrative.", 900)

PAGES = {"reo-holding-cost-basics": ("images/2026-11-28/1727-fb-reo-holding-cost-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
