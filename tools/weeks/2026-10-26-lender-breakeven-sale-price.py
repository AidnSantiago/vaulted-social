#!/usr/bin/env python3
"""Graphic for lender-breakeven-sale-price (Facebook, Wed Oct 28, 2026 12:47 pm ET). Illustrative numbers.
Run from repo root: python3 tools/weeks/2026-10-26-lender-breakeven-sale-price.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, RATE, MONTHS, LEGAL, SELL = 180000, 0.12, 9, 9000, 0.08   # illustrative


def gfx():
    interest = LOAN * RATE * MONTHS / 12
    owed = LOAN + interest + LEGAL
    be = owed / (1 - SELL)
    sell = be * SELL
    short = owed - 200000 * (1 - SELL)
    assert interest == 16200 and owed == 205200 and f"{be:,.0f}" == "223,043" and round(sell) == 17843
    assert round(be / LOAN * 100) == 124 and short == 21200
    BE = 223044
    X0, W = 68, 944
    parts = [("seg-blue", LOAN), ("seg-blue2", interest), ("seg-steel", LEGAL), ("seg-gold", BE - owed)]
    b = '<div class="abs lbl" style="left:68px;top:268px">What a sale must cover (illustrative)</div>'
    x = X0
    for i, (cls, v) in enumerate(parts):
        w = W * v / BE
        rad = "10px 0 0 10px" if i == 0 else ("0 10px 10px 0" if i == 3 else "0")
        txt = "$180,000" if i == 0 else ""
        b += (f'<div class="abs {cls} mono" style="left:{x:.1f}px;top:306px;width:{w:.1f}px;height:70px;border-radius:{rad};'
              f'display:flex;align-items:center;padding-left:18px;font-size:26px">{txt}</div>')
        x += w
    # legend row
    leg = [("#3B5C8E", "Principal $180,000"), ("#5B7DAE", "Interest $16,200"), ("#5A6B82", "Legal and carry $9,000"), ("#D2B058", "Selling costs 8%: $17,844")]
    pos = [(68, 396), (330, 396), (68, 428), (330, 428)]
    for (c, t), (lx, ly) in zip(leg, pos):
        b += (f'<div class="abs" style="left:{lx}px;top:{ly + 4}px;width:16px;height:16px;border-radius:4px;background:{c}"></div>'
              f'<div class="abs" style="left:{lx + 26}px;top:{ly}px;font-size:18px;color:#A5B2C3;white-space:nowrap">{t}</div>')
    b += '<div class="abs mono gold" style="left:640px;top:396px;font-size:26px;white-space:nowrap">= $223,044</div>'
    b += '<div class="abs" style="left:640px;top:432px;font-size:17px;color:#A5B2C3;white-space:nowrap">breakeven sale price</div>'
    b += stat_card(68, 490, 290, 150, "$205,200", "owed before selling", "180,000 + 16,200 + 9,000")
    b += stat_card(395, 490, 290, 150, "$223,044", "breakeven price", "205,200 / 0.92 = 124% of loan")
    b += stat_card(722, 490, 290, 150, "-$21,200", "short at $200,000", "$184,000 net after 8% costs", 44)
    b += panel(690, 100, "PRICE = OWED / (1 - COSTS)",
               "Selling costs come off the top, so the sale price must exceed what is owed.", 330, 24)
    foot = ("Sources: NerdWallet (updated Jul 2, 2026): closing costs for a seller can amount to roughly 6% to 10% of the sale price. "
            "Zillow (published Nov 21, 2024; modified Sep 16, 2025): sellers expect to pay 8% to 10% of the sale price in closing costs. "
            "Illustrative: $180,000 loan, 12%, 9 months, $9,000 legal and carry, 8% selling costs. 180,000 x 12% x 9/12 = $16,200; "
            "owed $205,200; 205,200 / 0.92 = $223,043.48, rounded up to $223,044; 8% = $17,844; 200,000 x 0.92 = $184,000; 205,200 - 184,000 = $21,200.")
    return shell("A $180,000 loan in default needs",
                 "a sale near $223,000 to break even",
                 "Principal, interest, costs and selling expenses all come out of the price", b, foot, 830)


PAGES = {"lender-breakeven-sale-price": ("images/2026-10-28/1247-fb-lender-breakeven-sale-price.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
