#!/usr/bin/env python3
"""Graphic for NAR Pending Home Sales, September 2026 (Facebook, Wed Nov 4, 2026 8:56 am ET).
Run from repo root: python3 tools/weeks/2026-11-02-pending-home-sales-sep-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    m = 265000 * 0.12 / 12
    assert f"{m:,.0f}" == "2,650"
    b = stat_card(68, 262, 460, 140, "-7.3%", "vs August 2026", "National pending home sales, month over month", 44)
    b += stat_card(552, 262, 460, 140, "-11.3%", "vs September 2025", "National pending home sales, year over year", 44)
    b += '<div class="abs lbl" style="left:68px;top:430px">Change from August, by region</div>'
    regions = [("Northeast", 4.2), ("Midwest", 6.5), ("South", 8.2), ("West", 9.2)]
    y = 466
    for name, v in regions:
        w = int(v / 9.2 * 560)
        b += f'<div class="abs" style="left:68px;top:{y+7}px;font-size:19px;font-weight:700;color:#F0EDE4">{name}</div>'
        b += (f'<div class="abs seg-blue2" style="left:210px;top:{y}px;width:{w}px;height:38px;border-radius:6px"></div>')
        b += f'<div class="abs mono gold" style="left:{210+w+14}px;top:{y+5}px;font-size:21px">-{v}%</div>'
        y += 50
    b += '<div class="abs lbl" style="left:68px;top:682px">Why it matters for exits</div>'
    b += ('<div class="abs seg-gold" style="left:68px;top:712px;width:300px;height:46px;border-radius:8px 0 0 8px;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:700">Contract signed</div>'
          '<div class="abs seg-steel" style="left:368px;top:712px;width:644px;height:46px;border-radius:0 8px 8px 0;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:700">Sale usually finalized within one or two months</div>')
    b += panel(782, 78, "$265,000 x 12% / 12 = $2,650", "Illustrative interest-only cost of each month a sale slips.", 380, 22)
    foot = ("Source: NAR, Pending Home Sales Decreased 7.3% in September (Oct 20, 2026). National and regional figures; local markets vary. "
            "Arithmetic: $265,000 x 12% / 12 = $2,650 a month (illustrative loan, interest-only).")
    return shell("Pending sales fell 7.3%.", "Closings may follow",
                 "NAR Pending Home Sales, September 2026 data", b, foot, 884, eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"pending-home-sales-sep-2026": ("images/2026-11-04/0856-fb-pending-home-sales-sep-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
