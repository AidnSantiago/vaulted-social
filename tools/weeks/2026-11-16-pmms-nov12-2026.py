#!/usr/bin/env python3
"""Graphic for Freddie Mac PMMS as of Nov 12 2026. Run from repo root: python3 tools/weeks/2026-11-16-pmms-nov12-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

P, R0, R1 = 390000, 6.24, 7.11

def pm(p, r, n=360):
    i = r / 1200
    return p * i / (1 - (1 + i) ** -n)

def gfx():
    a, b = pm(P, R0), pm(P, R1)
    assert f"{a:,.0f}" == "2,399" and f"{b:,.0f}" == "2,624" and round(b - a) == 225
    base, maxh = 600, 230
    h0, h1 = maxh * R0 / R1, maxh
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative $390,000, 30 years, principal and interest</div>'
    def bar(x, h, col, val, pay, cap):
        return (f'<div class="abs" style="left:{x}px;top:{base - h:.0f}px;width:210px;height:{h:.0f}px;border-radius:10px 10px 0 0;background:{col}"></div>'
                f'<div class="abs mono gold" style="left:{x}px;top:{base - h - 44:.0f}px;width:210px;text-align:center;font-size:34px">{val}</div>'
                f'<div class="abs mono" style="left:{x}px;top:{base + 10}px;width:210px;text-align:center;font-size:20px">{pay} a month</div>'
                f'<div class="abs steel" style="left:{x}px;top:{base + 38}px;width:210px;text-align:center;font-size:17px">{cap}</div>')
    body += bar(88, h0, "#5B7DAE", "6.24%", "$2,399", "A year ago")
    body += bar(338, h1, "#C9A84C", "7.11%", "$2,624", "As of Nov 12, 2026")
    body += ('<div class="card" style="left:612px;top:330px;width:400px;height:130px"><div class="abs mono gold" style="left:22px;top:20px;font-size:40px">+$225</div>'
             '<div class="abs" style="left:22px;top:78px;width:356px;font-size:19px;line-height:25px;font-weight:700">more a month on the same balance</div></div>')
    body += ('<div class="card" style="left:612px;top:480px;width:400px;height:130px"><div class="abs lbl" style="left:22px;top:18px">The survey</div>'
             '<div class="abs" style="left:22px;top:46px;width:356px;font-size:18px;line-height:25px">Owner-occupied 1-unit home purchase loans. Investor rates differ.</div></div>')
    body += ('<div class="panel" style="top:704px;height:104px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">LAST WEEK: 7.18%</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:600px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Lenders can re-run a refinance exit payment at a current rate, not the closing-day rate. Rates vary by lender.</div></div>')
    return page("light", "THIS WEEK", "PRIVATE LENDING, EXPLAINED", "The 30-year rate is 7.11%,", "up from 6.24% a year ago",
                "Freddie Mac weekly average, as of November 12, 2026", body,
                "Source: Freddie Mac Primary Mortgage Market Survey, as of Nov 12, 2026 (7.11 now, 7.18 prior week, 6.24 a year ago; page undated, accessed 2026-11-15); FRED MORTGAGE30US, updated Nov 12, 2026. "
                "Arithmetic: payment on $390,000 over 360 months: $2,398.76 at 6.24 vs $2,623.55 at 7.11, difference $224.79 (about $225). Loan illustrative.", 842)

PAGES = {"pmms-nov12-2026": ("images/2026-11-17/0915-fb-pmms-nov12-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
