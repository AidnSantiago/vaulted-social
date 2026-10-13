#!/usr/bin/env python3
"""Graphic for NAR existing-home sales, August 2026 data (Facebook, Thu Oct 15, 2026 8:25 am ET). Built Oct 13, 2026.
Run from repo root: python3 tools/weeks/2026-10-12-nar-existing-home-sales.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert round(1.62 / 3.98 * 12, 1) == 4.9
    b = stat_card(68, 268, 290, 150, "3.98M", "annual sales pace", "down 2.0% from July")
    b += stat_card(395, 268, 290, 150, "$429,100", "median price", "up 1.6% from a year ago", 38)
    b += stat_card(722, 268, 290, 150, "31 days", "median time on market", "all existing homes")
    b += '<div class="abs lbl" style="left:68px;top:452px">Months of supply of unsold inventory</div>'
    X0, S, H = 250, 150, 44   # px per month
    rows = [("August 2025", 4.6, "seg-blue"), ("August 2026", 4.9, "seg-gold")]
    y = 492
    for lab, v, cls in rows:
        b += f'<div class="abs" style="left:68px;top:{y}px;height:{H}px;display:flex;align-items:center;font-size:19px;font-weight:700">{lab}</div>'
        b += (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{v*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:19px">{v}</div>')
        y += H + 20
    b += ('<div class="abs" style="left:68px;top:622px;width:944px;font-size:18px;line-height:26px;color:#A5B2C3">'
          '1.62 million unsold homes, up 5.9% from August 2025. NAR calls 4.9 months its highest in over ten years.</div>')
    b += '<div class="abs lbl" style="left:68px;top:698px">Why it matters at exit</div>'
    b += panel(732, 84, "EXTRA MONTH = $1,500", "Illustrative: at $1,500 a month of carry, 2 more months on market adds $3,000.", 470, 24)
    foot = ("Source: National Association of REALTORS, Existing-Home Sales Report, August 2026 data (released Sep 10, 2026). "
            "Months of supply = 1.62M / 3.98M x 12 = 4.9. The $1,500 carry is illustrative. National figures; local markets vary.")
    return shell("Months of supply hit 4.9 in August.", "Check that against your exit.",
                 "NAR existing-home sales, August 2026 data", b, foot, 850,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"nar-existing-home-sales": ("images/2026-10-15/0825-fb-nar-existing-home-sales.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
