#!/usr/bin/env python3
"""Graphic for the effective cost of a short loan (Facebook, Mon Oct 26, 2026 12:47 pm ET). Illustrative numbers.
Run from repo root: python3 tools/weeks/2026-10-26-effective-apr-short-loan.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, RATE, POINTS, MONTHS = 150000, 0.11, 2.5, 6   # illustrative


def gfx():
    month = LOAN * RATE / 12
    interest = month * MONTHS
    fee = LOAN * POINTS / 100
    total = interest + fee
    pts_ann = POINTS * 12 / MONTHS
    eff = total / LOAN * (12 / MONTHS) * 100
    assert f"{month:,.0f}" == "1,375" and f"{interest:,.0f}" == "8,250" and f"{fee:,.0f}" == "3,750"
    assert f"{total:,.0f}" == "12,000" and f"{total / LOAN * 100:.0f}" == "8" and pts_ann == 5 and round(eff) == 16

    X0, W = 68, 944
    wi, wf = W * interest / total, W * fee / total
    b = '<div class="abs lbl" style="left:68px;top:268px">Cost over 6 months on a $150,000 loan</div>'
    b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:306px;width:{wi:.1f}px;height:70px;border-radius:10px 0 0 10px;'
          f'display:flex;align-items:center;padding-left:18px;font-size:26px">$8,250</div>')
    b += (f'<div class="abs seg-gold mono" style="left:{X0 + wi:.1f}px;top:306px;width:{wf:.1f}px;height:70px;border-radius:0 10px 10px 0;'
          f'display:flex;align-items:center;justify-content:center;font-size:26px">$3,750</div>')
    b += '<div class="abs" style="left:68px;top:386px;font-size:17px;color:#A5B2C3">Interest: $1,375 a month x 6 (11% interest-only)</div>'
    b += (f'<div class="abs" style="left:{X0 + wi + 12:.1f}px;top:386px;width:{wf - 12:.1f}px;font-size:17px;line-height:22px;color:#E2C265">2.5 points</div>')
    b += stat_card(68, 450, 290, 150, "11%", "quoted rate", "interest only")
    b += stat_card(395, 450, 290, 150, "+5%", "points, annualized", "2.5 points x 2 (6 months)")
    b += stat_card(722, 450, 290, 150, "16%", "annualized cost", "$12,000 = 8% of the loan in 6 months")
    b += panel(650, 100, "RATE + POINTS",
               "The shorter the loan, the more each point adds to the annual cost. Compare total cost over the expected hold.", 470, 26)
    foot = ("Sources: CFPB, Ask CFPB, interest rate vs APR (last reviewed Aug 28, 2026): the APR is the interest rate plus any additional fees charged by the lender. "
            "Real Estate Skills (Oct 28, 2025): 1 point = 1% of loan amount. Herring Bank (reviewed May 1, 2025): on a 6-month hold, points are annualized and added to the interest rate. "
            "Illustrative: $150,000, 11% interest-only, 2.5 points paid at closing, 6 months. 150,000 x 11% / 12 = $1,375; x 6 = $8,250; 2.5% x 150,000 = $3,750; "
            "total $12,000 = 8%; x 2 = 16% (simple annualization).")
    return shell("A quoted 11% rate on a 6-month loan", "is about 16% a year, simple basis",
                 "Illustrative $150,000 loan with 2.5 points, interest-only", b, foot, 790)


PAGES = {"effective-apr-short-loan": ("images/2026-10-26/1247-fb-effective-apr-short-loan.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
