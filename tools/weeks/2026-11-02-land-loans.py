#!/usr/bin/env python3
"""Graphic for land loan supervisory LTV limits (FB Tue Nov 3, 2026, 9:15 am ET). Fallback topic for attom-foreclosure-monthly-sep-2026 (September report not yet published).
Run from repo root: python3 tools/weeks/2026-11-02-land-loans.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

VALUE = 240000
RAW, DEV = VALUE * 0.65, VALUE * 0.75
assert round(RAW) == 156000 and round(DEV) == 180000 and round(DEV - RAW) == 24000

def gfx():
    S = 700 / VALUE
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative $240,000 parcel, bar length = dollars</div>'
    rows = [("Value", VALUE, "$240,000 appraised value", "seg-steel"),
            ("Raw land, 65 percent", RAW, "$156,000", "seg-gold"),
            ("Land development, 75 percent", DEV, "$180,000", "seg-blue2")]
    y = 310
    for title, v, txt, cls in rows:
        b += f'<div class="abs" style="left:68px;top:{y}px;font-size:18px;line-height:24px;font-weight:700;color:#F0EDE4;white-space:nowrap">{title}</div>'
        b += (f'<div class="abs {cls} mono" style="left:68px;top:{y+30}px;width:{v*S:.0f}px;height:42px;border-radius:8px;display:flex;align-items:center;'
              f'padding-left:14px;font-size:19px;white-space:nowrap">{txt}</div>')
        y += 104
    b += stat_card(790, 414, 222, 150, "$24,000", "gap in loan size", "$180,000 minus $156,000", 36)
    b += panel(650, 100, "Reference point", "Private lender limits vary by lender. Lenders can use these as a benchmark.", 500, 26)
    foot = ("Sources: Interagency Guidelines for Real Estate Lending Policies, 12 CFR Part 208 Appendix C (Cornell LII copy; page undated, accessed 2026-11-01); "
            "Federal Reserve SR 93-33, June 14, 1993. Guidelines address regulated institutions. "
            "Arithmetic: 240,000 x 0.65 = 156,000; 240,000 x 0.75 = 180,000; difference 24,000. The $240,000 value is illustrative.")
    return shell("Raw land: 65 percent.", "Land development: 75 percent.",
                 "Supervisory loan-to-value limits in federal bank guidelines", b, foot, 790,
                 eyebrow="LOAN SIZING FOR PRIVATE LENDERS")

PAGES = {"land-loans": ("images/2026-11-03/0915-fb-land-loans.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
