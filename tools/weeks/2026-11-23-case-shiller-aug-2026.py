#!/usr/bin/env python3
"""Graphic for Case-Shiller August 2026. Run from repo root: python3 tools/weeks/2026-11-23-case-shiller-aug-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

V = 500000  # illustrative value a year ago

def gfx():
    chi, nat, sea = 6.7, 2.1, -2.0
    vals = {k: round(V * (1 + r / 100)) for k, r in (("chi", chi), ("nat", nat), ("sea", sea))}
    assert vals == {"chi": 533500, "nat": 510500, "sea": 490000} and round(chi - sea, 1) == 8.7
    ppu = 90; zero = 68 + 2.5 * ppu
    body = '<div class="abs lbl" style="left:68px;top:290px">Annual change in home prices, August 2026</div>'
    rows = [("Chicago, highest of 20 cities", chi, "#C9A84C", "+6.7%"), ("U.S. National index", nat, "#5B7DAE", "+2.1%"), ("Seattle, lowest of 20 cities", sea, "#5A6B82", "-2.0%")]
    y = 326
    for name, v, col, txt in rows:
        body += f'<div class="abs steel" style="left:68px;top:{y}px;font-size:18px">{name}</div>'
        if v >= 0:
            x, w = zero, v * ppu
        else:
            x, w = zero + v * ppu, -v * ppu
        body += f'<div class="abs" style="left:{x:.0f}px;top:{y+28}px;width:{w:.0f}px;height:38px;border-radius:8px;background:{col}"></div>'
        lx = x + w + 14 if v >= 0 else zero + 14
        body += f'<div class="abs mono" style="left:{lx:.0f}px;top:{y+35}px;font-size:22px;color:#0B1F3A">{txt}</div>'
        y += 84
    body += f'<div class="abs" style="left:{zero:.0f}px;top:352px;width:2px;height:236px;background:#0B1F3A;opacity:.5"></div>'
    body += '<div class="abs lbl" style="left:68px;top:600px">Illustrative $500,000 property, one year later</div>'
    for i, (n, k, c) in enumerate((("At the Chicago rate", "chi", "gold"), ("At the national rate", "nat", ""), ("At the Seattle rate", "sea", ""))):
        x = 68 + i * 321
        body += (f'<div class="card" style="left:{x}px;top:634px;width:302px;height:104px"><div class="abs steel" style="left:20px;top:14px;font-size:17px">{n}</div>'
                 f'<div class="abs mono {c}" style="left:20px;top:48px;font-size:32px">${vals[k]:,}</div></div>')
    body += ('<div class="panel" style="top:764px;height:92px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">8.7 POINT SPREAD</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:600px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Lenders can compare local trends with the national figure. A citywide index does not value one property.</div></div>')
    return page("light", "THIS MONTH", "PRIVATE LENDING, EXPLAINED", "One national number,", "very different cities",
                "S&amp;P Cotality Case-Shiller, annual change to August 2026", body,
                "Source: S&amp;P Dow Jones Indices, S&amp;P Cotality Case-Shiller Index Reports Annual Gain in August 2026 (Oct 27, 2026). "
                "Arithmetic: 6.7 - (-2.0) = 8.7 points. $500,000 x 1.067 = $533,500; x 1.021 = $510,500; x 0.98 = $490,000. Property value illustrative.", 884)

PAGES = {"case-shiller-aug-2026": ("images/2026-11-23/1134-li-case-shiller-aug-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
