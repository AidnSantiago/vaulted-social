#!/usr/bin/env python3
"""Graphic for days on market, Realtor.com Sept 2026 (Facebook, Sat Oct 17, 2026 9:32 am ET).
Run from repo root: python3 tools/weeks/2026-10-12-days-on-market.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    m = 325000 * 0.11 / 12
    assert f"{m:,.2f}" == "2,979.17" and f"{2*m:,.2f}" == "5,958.33"
    b = '<div class="abs lbl" style="left:68px;top:270px">Median days on market, U.S. listings</div>'
    X0, S, H = 250, 10.5, 44
    rows = [("Sept 2025", 62, "seg-blue"), ("Aug 2026", 60, "seg-blue"), ("Sept 2026", 61, "seg-gold")]
    y = 308
    for lab, v, cls in rows:
        b += f'<div class="abs" style="left:68px;top:{y}px;height:{H}px;display:flex;align-items:center;font-size:19px;font-weight:700">{lab}</div>'
        b += (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{v*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:19px">{v}</div>')
        y += H + 14
    b += '<div class="abs lbl" style="left:68px;top:482px">What the days cost in interest</div>'
    b += stat_card(68, 520, 290, 150, "$2,979.17", "one month of interest", "$325,000 at 11% interest-only", 36)
    b += stat_card(395, 520, 290, 150, "$5,958.33", "two months of interest", "about the 61-day median", 36)
    b += stat_card(722, 520, 290, 150, "+$2,979.17", "if a sale runs 30 days late", "added carry", 36)
    b += panel(708, 92, "HALF TAKE LONGER", "A median is the midpoint. Lenders can also check local days on market.", 470, 24)
    foot = ("Source: Realtor.com, September 2026 Monthly Housing Trends Report (published Sep 30, 2026). "
            "Sept 2025 = 61 + 1; Aug 2026 = 61 - 1. Interest: $325,000 x 11% / 12 = $2,979.17 (illustrative loan). National figures; local markets vary.")
    return shell("The median home sat 61 days.", "Each month is another interest bill.",
                 "Realtor.com, September 2026 data", b, foot, 842, eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"days-on-market": ("images/2026-10-17/0932-fb-days-on-market.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
