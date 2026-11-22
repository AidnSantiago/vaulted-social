#!/usr/bin/env python3
"""Graphic for ATTOM H1 2026 REO increases by state. Run from repo root: python3 tools/weeks/2026-11-23-attom-reo-states-h1-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

DATA = [("Colorado", 215, 595, 176.7), ("Florida", 1126, 2070, 83.8), ("Texas", 2207, 3322, 50.5)]

def gfx():
    for _, a, b, p in DATA:
        assert round((b / a - 1) * 100, 1) == p
    track, mx = 560, 3322
    body = '<div class="abs lbl" style="left:68px;top:290px">REO properties, first half 2025 vs first half 2026</div>'
    y = 326
    for name, a, b, p in DATA:
        body += f'<div class="abs" style="left:68px;top:{y}px;font-size:20px;font-weight:700">{name}</div>'
        body += f'<div class="abs mono gold" style="left:{1012-170}px;top:{y-2}px;width:170px;text-align:right;font-size:26px">+{p}%</div>'
        for k, (v, col, lab) in enumerate([(a, "#5B7DAE", "2025"), (b, "#C9A84C", "2026")]):
            w = max(track * v / mx, 6)
            yy = y + 32 + k * 40
            body += f'<div class="abs" style="left:68px;top:{yy}px;width:{w:.0f}px;height:32px;border-radius:6px;background:{col}"></div>'
            body += f'<div class="abs mono" style="left:{68+w+12:.0f}px;top:{yy+5}px;font-size:19px;color:#0B1F3A">{v:,} <span class="steel" style="font-weight:400;font-size:15px">H1 {lab}</span></div>'
        y += 136
    body += ('<div class="panel" style="top:750px;height:96px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'Lenders can compare each state in their portfolio with local data and revisit exit assumptions, such as resale timelines and values.</div></div>')
    return page("light", "NEW DATA", "PRIVATE LENDING, EXPLAINED", "Repossessions rose fastest", "in a few states",
                "ATTOM mid-year 2026: states with at least 500 REOs in the first half", body,
                "Source: ATTOM, Top 10 U.S. States with the Largest Annual Increases in REOs in the First Half of 2026 (Jul 31, 2026). REO = property repossessed by the lender. "
                "Arithmetic: 595 / 215 = 2.767 (+176.7%); 2,070 / 1,126 = 1.838 (+83.8%); 3,322 / 2,207 = 1.505 (+50.5%).", 880)

PAGES = {"attom-reo-states-h1-2026": ("images/2026-11-24/0915-fb-attom-reo-states-h1-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
