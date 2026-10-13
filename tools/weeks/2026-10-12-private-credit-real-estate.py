#!/usr/bin/env python3
"""Graphic for banks vs commercial/multifamily mortgage debt (LinkedIn, Thu Oct 15, 2026 3:40 pm ET). Built Oct 13, 2026.
Run from repo root: python3 tools/weeks/2026-10-12-private-credit-real-estate.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert 100 - 38 == 62
    b = stat_card(68, 268, 290, 150, "$1.9T", "held by banks and thrifts", "of $5.1T total, end of Q2 2026")
    b += stat_card(395, 268, 290, 150, "+$13.3B", "bank holdings in Q2 2026", "a 0.7% increase on Q1")
    b += stat_card(722, 268, 290, 150, "+61%", "loans for depositories", "Q2 2026 vs a year earlier")
    b += '<div class="abs lbl" style="left:68px;top:462px">Who holds commercial and multifamily mortgage debt</div>'
    W = 944
    wb = W * 0.38
    b += (f'<div class="abs seg-gold mono" style="left:68px;top:504px;width:{wb:.1f}px;height:64px;border-radius:8px 0 0 8px;'
          f'display:flex;align-items:center;justify-content:center;font-size:26px">38%</div>')
    b += (f'<div class="abs seg-steel mono" style="left:{68+wb:.1f}px;top:504px;width:{W-wb:.1f}px;height:64px;border-radius:0 8px 8px 0;'
          f'display:flex;align-items:center;justify-content:center;font-size:26px">62%</div>')
    b += ('<div class="abs" style="left:68px;top:580px;font-size:17px;line-height:22px;font-weight:700;color:#F0EDE4;width:340px">Banks and thrifts</div>'
          f'<div class="abs" style="left:{68+wb+16:.1f}px;top:580px;font-size:17px;line-height:22px;font-weight:700;color:#F0EDE4;width:500px">All other holders</div>')
    b += ('<div class="abs" style="left:68px;top:640px;width:944px;font-size:19px;line-height:28px;color:#A5B2C3">'
          'Scope: commercial and multifamily loans, not one-to-four unit investor loans.<br>'
          'The origination figure comes from MBA\'s survey of mortgage bankers, a separate data set.</div>')
    b += panel(762, 100, "BANKS ARE STILL HERE", "Private lenders can treat banks as active competitors.", 400, 24)
    foot = ("Sources: Mortgage Bankers Association, Commercial/Multifamily Mortgage Debt Outstanding, Q2 2026 (released Sep 29, 2026); "
            "MBA Quarterly Survey of Commercial/Multifamily Mortgage Bankers Originations, Q2 2026 (Aug 6, 2026). "
            "Arithmetic: 100 - 38 = 62 percent. T = trillion, B = billion.")
    return shell("Banks are not leaving commercial", "real estate lending.",
                 "MBA data, second quarter 2026", b, foot, 896,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"private-credit-real-estate": ("images/2026-10-15/1540-li-private-credit-real-estate.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
