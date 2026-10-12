#!/usr/bin/env python3
"""Graphic for the extension-fee yield post (Facebook, Wed Oct 14, 2026 12:47 pm ET). Illustrative numbers.
Run from repo root: python3 tools/weeks/2026-10-12-extension-fee-yield.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, RATE, POINTS, MONTHS = 450000, 0.105, 1, 3   # illustrative


def gfx():
    month = LOAN * RATE / 12
    interest = month * MONTHS
    fee = LOAN * POINTS / 100
    total = interest + fee
    ann = total / LOAN * (12 / MONTHS) * 100
    assert f"{month:,.2f}" == "3,937.50" and f"{interest:,.2f}" == "11,812.50" and f"{fee:,.0f}" == "4,500"
    assert f"{total:,.2f}" == "16,312.50" and f"{total / LOAN * 100:.3f}" == "3.625" and f"{ann:.1f}" == "14.5"

    X0, W = 68, 944
    wi, wf = W * interest / total, W * fee / total
    b = '<div class="abs lbl" style="left:68px;top:268px">Earned over the 3-month extension on $450,000</div>'
    b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:306px;width:{wi:.1f}px;height:70px;border-radius:10px 0 0 10px;'
          f'display:flex;align-items:center;padding-left:18px;font-size:26px">$11,812.50</div>')
    b += (f'<div class="abs seg-gold mono" style="left:{X0 + wi:.1f}px;top:306px;width:{wf:.1f}px;height:70px;border-radius:0 10px 10px 0;'
          f'display:flex;align-items:center;justify-content:center;font-size:24px">$4,500</div>')
    b += (f'<div class="abs" style="left:{X0}px;top:386px;font-size:17px;color:#A5B2C3">Interest: $3,937.50 a month x 3 (10.5% interest-only)</div>')
    b += (f'<div class="abs" style="left:{X0 + wi + 12:.1f}px;top:386px;width:{wf - 12:.1f}px;font-size:17px;line-height:22px;color:#E2C265">1 point fee</div>')
    b += stat_card(68, 450, 290, 150, "$16,312.50", "interest plus fee", "3.625% of the balance", big_size=36)
    b += stat_card(395, 450, 290, 150, "10.5%", "annualized, no fee", "interest only")
    b += stat_card(722, 450, 290, 150, "14.5%", "annualized, with fee", "$16,312.50 x 4 / $450,000")
    b += panel(650, 100, "FEE + INTEREST",
               "Extension fees are negotiated and vary by lender. The fee adds yield only if the borrower keeps paying.", 470, 26)
    foot = ("Sources: Real Estate Skills, Hard Money Loans: Rates, Terms &amp; Real Costs (updated Aug 2026): a point is one percent of the loan amount; extensions usually cost a fee. "
            "Note Servicing Center (page undated, accessed Oct 12, 2026): extension fees typically structured as additional points. "
            "Illustrative: $450,000, 10.5% interest-only, 1 point, 3 months. $450,000 x 10.5% / 12 = $3,937.50; x 3 = $11,812.50; 1% x $450,000 = $4,500; "
            "total $16,312.50 = 3.625%; x 4 = 14.5% (simple annualization).")
    return shell("A 1 point fee on a 3-month extension", "lifts 10.5% to 14.5% annualized",
                 "Illustrative $450,000 loan, interest-only, 3 more months", b, foot, 790)


PAGES = {"extension-fee-yield": ("images/2026-10-14/1247-fb-extension-fee-yield.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
