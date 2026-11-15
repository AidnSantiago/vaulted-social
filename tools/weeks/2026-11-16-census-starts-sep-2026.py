#!/usr/bin/env python3
"""Graphic for Census housing starts, September 2026. Run from repo root: python3 tools/weeks/2026-11-16-census-starts-sep-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert 1288000 - 1221000 == 67000 and 1400000 - 1221000 == 179000
    track, mx = 944, 1500000
    body = '<div class="abs lbl" style="left:68px;top:290px">Housing starts, seasonally adjusted annual rate</div>'
    rows = [("September 2025", 1319000, "#5B7DAE"), ("August 2026 (revised)", 1288000, "#5B7DAE"), ("September 2026", 1221000, "#C9A84C")]
    y = 326
    for name, v, col in rows:
        w = track * v / mx
        body += f'<div class="abs steel" style="left:68px;top:{y}px;font-size:18px">{name}</div>'
        body += f'<div class="abs" style="left:68px;top:{y+28}px;width:{track}px;height:40px;border-radius:8px;background:rgba(11,31,58,.10)"></div>'
        body += f'<div class="abs" style="left:68px;top:{y+28}px;width:{w:.0f}px;height:40px;border-radius:8px;background:{col}"></div>'
        body += f'<div class="abs mono" style="left:84px;top:{y+37}px;font-size:21px;color:#0B1F3A">{v:,}</div>'
        y += 88
    cards = [("Single-family starts", "859,000", "down 4.6% from August"), ("Permits authorized", "1,400,000", "179,000 above starts"), ("Total starts, month on month", "-5.2%", "67,000 fewer than August")]
    for i, (h, big, d) in enumerate(cards):
        x = 68 + i * 321
        body += (f'<div class="card" style="left:{x}px;top:604px;width:302px;height:150px"><div class="abs lbl" style="left:20px;top:16px;font-size:12.5px;letter-spacing:.1em">{h}</div>'
                 f'<div class="abs mono gold" style="left:20px;top:50px;font-size:36px">{big}</div><div class="abs steel" style="left:20px;top:104px;font-size:18px">{d}</div></div>')
    body += ('<div class="panel" style="top:784px;height:96px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">THE TAKEAWAY</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:640px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Use national starts as context, then underwrite the local exit. Markets vary.</div></div>')
    return page("light", "NEW DATA", "PRIVATE LENDING, EXPLAINED", "Housing starts slipped to", "1,221,000 in September",
                "U.S. Census Bureau, released October 20, 2026", body,
                "Source: U.S. Census Bureau, New Residential Construction, September 2026, released Oct 20, 2026. Arithmetic: 1,288,000 - 1,221,000 = 67,000; 1,400,000 - 1,221,000 = 179,000. Bars drawn from zero.", 920)

PAGES = {"census-starts-sep-2026": ("images/2026-11-18/0856-fb-census-starts-sep-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
