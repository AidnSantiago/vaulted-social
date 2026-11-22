#!/usr/bin/env python3
"""Graphic for NAR existing-home sales, October 2026. Run from repo root: python3 tools/weeks/2026-11-23-nar-existing-home-sales-oct-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    track, mx = 944, 6.0
    body = '<div class="abs lbl" style="left:68px;top:290px">Months of supply, existing homes</div>'
    rows = [("October 2025", 4.4, "#5B7DAE"), ("September 2026", 4.7, "#5B7DAE"), ("October 2026", 5.1, "#C9A84C")]
    y = 326
    for name, v, col in rows:
        w = track * v / mx
        body += f'<div class="abs steel" style="left:68px;top:{y}px;font-size:18px">{name}</div>'
        body += f'<div class="abs" style="left:68px;top:{y+28}px;width:{track}px;height:40px;border-radius:8px;background:rgba(11,31,58,.10)"></div>'
        body += f'<div class="abs" style="left:68px;top:{y+28}px;width:{w:.0f}px;height:40px;border-radius:8px;background:{col}"></div>'
        body += f'<div class="abs mono" style="left:84px;top:{y+37}px;font-size:21px;color:#0B1F3A">{v} months</div>'
        y += 88
    cards = [("Sales pace, annual rate", "3.75M", "down 5.5% from September"), ("Median price", "$416,700", "up 0.4% year over year"), ("Median time on market", "35 days", "up from 33 in September")]
    for i, (h, big, d) in enumerate(cards):
        x = 68 + i * 321
        body += (f'<div class="card" style="left:{x}px;top:604px;width:302px;height:150px"><div class="abs lbl" style="left:20px;top:16px;font-size:12.5px;letter-spacing:.1em">{h}</div>'
                 f'<div class="abs mono gold" style="left:20px;top:50px;font-size:36px">{big}</div><div class="abs steel" style="left:20px;top:104px;font-size:18px">{d}</div></div>')
    body += ('<div class="panel" style="top:784px;height:96px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">THE TAKEAWAY</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:640px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">National data is context. Check comps and days on market near the collateral.</div></div>')
    return page("light", "NEW DATA", "PRIVATE LENDING, EXPLAINED", "Home sales slowed to 3.75M", "as supply rose to 5.1 months",
                "NAR existing-home sales, October 2026, released November 12, 2026", body,
                "Source: National Association of Realtors, existing-home sales for October 2026, Nov 12, 2026. Sales are a seasonally adjusted annual rate. Bars drawn from zero on a 6-month axis.", 920)

PAGES = {"nar-existing-home-sales-oct-2026": ("images/2026-11-23/0842-fb-nar-existing-home-sales-oct-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
