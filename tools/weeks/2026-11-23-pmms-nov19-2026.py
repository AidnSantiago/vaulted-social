#!/usr/bin/env python3
"""Graphic for Freddie Mac PMMS as of Nov 19 2026. Run from repo root: python3 tools/weeks/2026-11-23-pmms-nov19-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

P = 445000

def pm(p, r, n=360):
    i = r / 1200
    return p * i / (1 - (1 + i) ** -n)

def gfx():
    a, b = pm(P, 6.26), pm(P, 7.28)
    assert f"{a:,.0f}" == "2,743" and f"{b:,.0f}" == "3,045" and round(b - a) == 302
    body = '<div class="abs lbl" style="left:68px;top:290px">Freddie Mac weekly averages, as of Nov 19, 2026</div>'
    def card(x, name, now, wk, yr):
        return (f'<div class="card" style="left:{x}px;top:326px;width:458px;height:206px">'
                f'<div class="abs lbl" style="left:24px;top:18px">{name}</div>'
                f'<div class="abs mono gold" style="left:24px;top:46px;font-size:64px">{now}</div>'
                f'<div class="abs steel" style="left:24px;top:128px;width:410px;font-size:19px;line-height:26px">Last week {wk}<br>A year ago {yr}</div></div>')
    body += card(68, "30-year fixed", "7.28%", "7.11%", "6.26%") + card(554, "15-year fixed", "6.66%", "6.45%", "5.54%")
    body += ('<div class="abs lbl" style="left:68px;top:566px">Illustrative $445,000, 30 years, principal and interest</div>')
    body += ('<div class="card" style="left:68px;top:600px;width:300px;height:118px"><div class="abs steel" style="left:22px;top:16px;font-size:17px">At 6.26%</div>'
             '<div class="abs mono" style="left:22px;top:46px;font-size:34px">$2,743</div><div class="abs steel" style="left:22px;top:90px;font-size:15px">a month</div></div>')
    body += ('<div class="card" style="left:394px;top:600px;width:300px;height:118px"><div class="abs steel" style="left:22px;top:16px;font-size:17px">At 7.28%</div>'
             '<div class="abs mono" style="left:22px;top:46px;font-size:34px">$3,045</div><div class="abs steel" style="left:22px;top:90px;font-size:15px">a month</div></div>')
    body += ('<div class="card" style="left:720px;top:600px;width:292px;height:118px"><div class="abs steel" style="left:22px;top:16px;font-size:17px">Difference</div>'
             '<div class="abs mono gold" style="left:22px;top:46px;font-size:34px">+$302</div><div class="abs steel" style="left:22px;top:90px;font-size:15px">a month</div></div>')
    body += ('<div class="panel" style="top:752px;height:104px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">NOT A FORECAST</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:610px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Lenders can re-run a refinance exit payment at a current rate. The survey covers owner-occupied purchase loans.</div></div>')
    return page("light", "THIS WEEK", "PRIVATE LENDING, EXPLAINED", "The 30-year rate is 7.28%,", "up from 7.11% last week",
                "Freddie Mac weekly average, as of November 19, 2026", body,
                "Source: Freddie Mac Primary Mortgage Market Survey, as of Nov 19, 2026 (page undated, accessed 2026-11-22). Last week and a year ago as printed on the page. "
                "Arithmetic: payment on $445,000 over 360 months: $2,742.84 at 6.26% vs $3,044.74 at 7.28%, difference $301.91 (about $302). Loan illustrative.", 888)

PAGES = {"pmms-nov19-2026": ("images/2026-11-25/0856-fb-pmms-nov19-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
