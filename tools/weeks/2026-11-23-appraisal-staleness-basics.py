#!/usr/bin/env python3
"""Graphic for appraisal staleness basics. Run from repo root: python3 tools/weeks/2026-11-23-appraisal-staleness-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

VALUE, DROP = 425000, 5
NEW = VALUE * (100 - DROP) // 100
GAP = VALUE - NEW

def gfx():
    assert NEW == 403750 and GAP == 21250
    track = 944
    segs = [("0 to 4 months", 4, "#5B7DAE", "#fff"), ("4 to 12 months: update", 8, "#C9A84C", "#0B1F3A"), ("Over 12 months", 3, "#3F5470", "#fff")]
    total = sum(s[1] for s in segs)
    body = '<div class="abs lbl" style="left:68px;top:290px">One public benchmark: age of the appraisal at closing</div>'
    x = 68
    for name, m, col, tc in segs:
        w = track * m / total
        body += (f'<div class="abs" style="left:{x:.0f}px;top:326px;width:{w-4:.0f}px;height:64px;border-radius:8px;background:{col};color:{tc};'
                 f'display:flex;align-items:center;justify-content:center;font-weight:700;font-size:19px">{name}</div>')
        x += w
    body += '<div class="abs steel" style="left:68px;top:402px;font-size:18px">Fannie Mae Selling Guide: an update past four months. A decline found in the update means a new appraisal.</div>'
    body += '<div class="abs lbl" style="left:68px;top:462px">Illustrative: what a 5 percent decline does to the value</div>'
    body += (f'<div class="card" style="left:68px;top:498px;width:300px;height:170px"><div class="abs steel" style="left:22px;top:20px;font-size:18px">Appraised value</div>'
             f'<div class="abs mono gold" style="left:22px;top:62px;font-size:38px">${VALUE:,}</div></div>')
    body += (f'<div class="card" style="left:394px;top:498px;width:300px;height:170px"><div class="abs steel" style="left:22px;top:20px;font-size:18px">After a 5 percent decline</div>'
             f'<div class="abs mono gold" style="left:22px;top:62px;font-size:38px">${NEW:,}</div></div>')
    body += (f'<div class="card" style="left:720px;top:498px;width:292px;height:170px"><div class="abs steel" style="left:22px;top:20px;font-size:18px">Gap</div>'
             f'<div class="abs mono gold" style="left:22px;top:62px;font-size:38px">${GAP:,}</div></div>')
    body += ('<div class="panel" style="top:704px;height:110px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'Age limits vary by lender. Lenders can set their own limit and ask for an update before closing.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "How old is too old", "for an appraisal?",
                "Age limits are not universal, so lenders can set their own", body,
                "Sources: Fannie Mae Selling Guide B4-1.2-04 (06/04/2025); Interagency Appraisal and Evaluation Guidelines, Federal Register (Dec 10, 2010). "
                "Arithmetic: 425,000 x 0.95 = 403,750; 425,000 - 403,750 = 21,250. Value and decline illustrative.", 850)

PAGES = {"appraisal-staleness-basics": ("images/2026-11-25/1727-fb-appraisal-staleness-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
