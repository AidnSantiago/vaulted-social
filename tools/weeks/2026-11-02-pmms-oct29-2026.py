#!/usr/bin/env python3
"""Graphic for Freddie Mac PMMS as of Oct 29 2026 and refinance exits. Run from repo root: python3 tools/weeks/2026-11-02-pmms-oct29-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

P, R0, R1 = 370000, 6.17, 7.24

def pm(p, r, n=360):
    i = r / 1200
    return p * i / (1 - (1 + i) ** -n)

def gfx():
    a, b = pm(P, R0), pm(P, R1)
    assert f"{a:,.2f}" == "2,258.94" and f"{b:,.2f}" == "2,521.54" and round(b - a) == 263
    # bars: heights proportional to rate
    base, maxh = 560, 190
    h0, h1 = maxh * R0 / R1, maxh
    body = '<div class="abs lbl" style="left:68px;top:268px">Freddie Mac 30-year fixed average</div>'
    def bar(x, h, cls, val, cap):
        return (f'<div class="abs seg-{cls}" style="left:{x}px;top:{base - h:.0f}px;width:230px;height:{h:.0f}px;border-radius:10px 10px 0 0"></div>'
                f'<div class="abs mono gold" style="left:{x}px;top:{base - h - 46:.0f}px;width:230px;text-align:center;font-size:36px">{val}</div>'
                f'<div class="abs" style="left:{x}px;top:{base + 10}px;width:230px;text-align:center;font-size:17px;color:#A5B2C3">{cap}</div>')
    body += bar(88, h0, "steel", "6.17%", "A year earlier")
    body += bar(348, h1, "gold", "7.24%", "As of Oct 29, 2026")
    body += '<div class="abs mono gold" style="left:68px;top:620px;font-size:20px">+1.07 points year over year</div>'
    body += stat_card(628, 300, 384, 150, "$2,258.94", "a month at 6.17%", "Illustrative: $370,000, 30 years, P&amp;I", 40)
    body += stat_card(628, 470, 384, 150, "$2,521.54", "a month at 7.24%", "About $263 more a month", 40)
    body += panel(690, 110, "SAME LOAN, NEW RATE", "Lenders can ask if a refinance exit still works at today's rate. Rates vary by lender.", 450, 22)
    return shell("Rates are 1.07 points higher", "than a year ago", "Freddie Mac 30-year average, as of October 29, 2026", body,
                 "Source: Freddie Mac Primary Mortgage Market Survey, as of Oct 29, 2026 (7.24 and 6.17 a year earlier; page undated, accessed 2026-11-01); FRED MORTGAGE30US, updated Oct 29, 2026; InvestingLive, Oct 30, 2025 (6.17). "
                 "Arithmetic: 7.24 - 6.17 = 1.07; payment on $370,000 over 360 months: $2,258.94 vs $2,521.54, difference about $263. Loan illustrative.", 842)

PAGES = {"pmms-oct29-2026": ("images/2026-11-05/0825-fb-pmms-oct29-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
