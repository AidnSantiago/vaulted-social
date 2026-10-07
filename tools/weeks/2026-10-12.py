#!/usr/bin/env python3
"""Graphics for the rehearsal posts of the week of 2026-10-12 (built Oct 7, 2026).
Run from repo root:  python3 tools/weeks/2026-10-12.py [key ...]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def gfx_wltv():
    b = '<div class="abs lbl" style="left:68px;top:268px">Three loans, bar length = loan balance</div>'
    S = 690 / 600000
    for i, (bal, ltv, name) in enumerate(((600000, 75, "Loan A"), (100000, 55, "Loan B"), (150000, 60, "Loan C"))):
        y = 306 + i * 66
        b += f'<div class="abs" style="left:68px;top:{y}px;width:90px;height:50px;display:flex;align-items:center;font-size:19px;font-weight:700">{name}</div>'
        cls = "seg-gold" if i == 0 else "seg-blue"
        b += (f'<div class="abs {cls} mono" style="left:160px;top:{y}px;width:{bal * S:.1f}px;height:50px;border-radius:8px;'
              f'display:flex;align-items:center;padding-left:10px;font-size:16px;white-space:nowrap">${bal:,}</div>')
        b += f'<div class="abs mono gold" style="left:{160 + bal * S + 18:.1f}px;top:{y}px;height:50px;display:flex;align-items:center;font-size:22px;white-space:nowrap">{ltv}% LTV</div>'
    b += stat_card(68, 520, 450, 150, "63.3%", "Simple average LTV", "(75 + 55 + 60) &divide; 3")
    b += stat_card(562, 520, 450, 150, "70.0%", "Weighted average LTV", "$595,000 &divide; $850,000")
    b += panel(704, 100, "WEIGHT BY BALANCE", "Loan A is about 71% of the balance, so it pulls the average up. Track the weighted figure.", 470)
    foot = ("Definition: weighted average LTV weights each loan's LTV by its outstanding principal balance (Law Insider, Weighted Average LTV definition, accessed Oct 7, 2026). "
            "Example loans are illustrative. Weighted: (0.75 x $600,000 + 0.55 x $100,000 + 0.60 x $150,000) &divide; $850,000 = 70.0%. Loan A: $600,000 &divide; $850,000 = 70.6%.")
    return shell("Average LTV can hide your risk.", "Weight it by loan balance.",
                 "Simple average vs. weighted average, three illustrative loans", b, foot, 840)


def gfx_losspayee():
    b = step_cards([
        ("1", "A loss occurs", "A fire causes $90,000 of damage on a property with a $240,000 loan.", "$90,000 loss"),
        ("2", "Lender is named", "The lender is the named mortgagee on the policy.", "mortgagee clause"),
        ("3", "Insurer pays", "The insurer pays the lender for the loss.", "lender is paid"),
    ], top=268, h=222)

    def d(x, label, text):
        return (f'<div class="card" style="left:{x}px;top:528px;width:462px;height:150px">'
                f'<div class="abs lbl" style="left:22px;top:18px">{label}</div>'
                f'<div class="abs" style="left:22px;top:48px;width:418px;font-size:19px;line-height:26px;color:#F0EDE4">{text}</div></div>')
    b += d(68, "Loss payee", "The party entitled to the insurance payout if a claim is made.")
    b += d(550, "Mortgagee clause", "Entitles a named mortgagee to be paid for damage or loss to the property.")
    b += panel(712, 92, "37.5% OF THE BALANCE", "$90,000 &divide; $240,000. Payout amounts depend on the policy.", 430)
    foot = ("Source: Citizens Bank, What is a mortgagee clause? (accessed Oct 7, 2026; page undated). "
            "Loan and loss amounts are illustrative. $90,000 &divide; $240,000 = 37.5%.")
    return shell("What is a loss payee?", "The lender named on the policy.",
                 "Insurance terms every private lender should know", b, foot, 850,
                 eyebrow="PRIVATE LENDING, EXPLAINED")


def gfx_flipprofit():
    b = '<div class="abs lbl" style="left:68px;top:268px">Typical gross profit per flip</div>'
    S = 560 / 71000
    rows = (("Q2 2025", 71000, "27.6%"), ("Q1 2026", 66932, "25.7%"), ("Q2 2026", 60526, "21.5%"))
    for i, (q, v, m) in enumerate(rows):
        y = 304 + i * 62
        b += f'<div class="abs" style="left:68px;top:{y}px;width:100px;height:48px;display:flex;align-items:center;font-size:19px;font-weight:700">{q}</div>'
        cls = "seg-gold" if i == 2 else "seg-blue"
        b += (f'<div class="abs {cls} mono" style="left:176px;top:{y}px;width:{v * S:.1f}px;height:48px;border-radius:8px;'
              f'display:flex;align-items:center;padding-left:14px;font-size:19px;white-space:nowrap">${v:,}</div>')
        b += f'<div class="abs mono gold" style="left:{176 + v * S + 20:.1f}px;top:{y}px;height:48px;display:flex;align-items:center;font-size:20px;white-space:nowrap">{m} margin</div>'
    b += stat_card(68, 510, 450, 150, "21.5%", "profit margin, Q2 2026", "down from 27.6% a year earlier")
    b += stat_card(562, 510, 450, 150, "20-33%", "rehab and other costs", "of after repair value, not in gross profit", big_size=44)
    b += panel(694, 100, "LESS ROOM FOR ERROR", "Stress test the rehab budget and the exit plan before you fund.", 440)
    foot = ("Source: ATTOM, Home Flipping Profits Continue Gradual Two-Year Decline, Q2 2026 Home Flipping Report (Oct 1, 2026). "
            "Gross profit is the difference between purchase and resale price, and excludes rehab costs and other expenses, "
            "which flipping veterans estimate typically run between 20 and 33 percent of after-repair value (per ATTOM).")
    return shell("Flip profits keep shrinking.", "What it means for lenders.",
                 "ATTOM, Q2 2026 &middot; typical U.S. home flip", b, foot, 830,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")


PAGES = {
    "wltv": ("images/2026-10-12/1727-fb-weighted-ltv.png", gfx_wltv),
    "losspayee": ("images/2026-10-13/0915-fb-loss-payee.png", gfx_losspayee),
    "flipprofit": ("images/2026-10-14/1709-li-flip-profit.png", gfx_flipprofit),
}

if __name__ == "__main__":
    keys = sys.argv[1:] or list(PAGES)
    render([PAGES[k] for k in keys], ROOT)
