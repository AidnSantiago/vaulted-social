#!/usr/bin/env python3
"""Graphic for origination points split with a broker (Facebook, Sat Nov 14, 2026 1:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-origination-points-split.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, PTS, BROKER_PTS, RATE = 355000, 2.5, 1.0, 10.3  # illustrative
TOTAL = round(LOAN * PTS / 100)
BROKER = round(LOAN * BROKER_PTS / 100)
LENDER = TOTAL - BROKER
INT = round(LOAN * RATE / 100)
INC_SPLIT = INT + LENDER
INC_ALL = INT + TOTAL
Y_SPLIT = round(INC_SPLIT / LOAN * 100, 2)
Y_ALL = round(INC_ALL / LOAN * 100, 2)
assert (TOTAL, BROKER, LENDER, INT, INC_SPLIT, INC_ALL, Y_SPLIT, Y_ALL) == (8875, 3550, 5325, 36565, 41890, 45440, 11.8, 12.8)


def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">Illustrative $355,000 loan, 2.5 points = $8,875</div>'
    W = 944
    wb = round(W * BROKER / TOTAL)
    b += f'<div class="abs seg-steel mono" style="left:68px;top:298px;width:{wb}px;height:64px;border-radius:8px 0 0 8px;display:flex;align-items:center;justify-content:center;font-size:24px">1 pt &middot; $3,550</div>'
    b += f'<div class="abs seg-gold mono" style="left:{68+wb}px;top:298px;width:{W-wb}px;height:64px;border-radius:0 8px 8px 0;display:flex;align-items:center;justify-content:center;font-size:24px">1.5 pts &middot; $5,325</div>'
    b += f'<div class="abs steel" style="left:68px;top:372px;font-size:17px;white-space:nowrap">Broker share (example)</div>'
    b += f'<div class="abs steel" style="left:{68+wb}px;top:372px;font-size:17px;white-space:nowrap">Lender keeps</div>'
    b += '<div class="abs lbl" style="left:68px;top:428px">Lender income over 12 months, interest-only at 10.3%</div>'
    b += stat_card(68, 462, 458, 190, "11.8%", "Lender yield, 1 point to broker", "$36,565 interest + $5,325 points = $41,890", 54)
    b += stat_card(554, 462, 458, 190, "12.8%", "Lender yield, keeps all 2.5 points", "$36,565 interest + $8,875 points = $45,440", 54)
    b += panel(684, 120, "(interest + points kept) / loan",
               "Same loan, same rate: a 1 point broker share cuts the lender yield by 1.0 point.", 380, 22)
    foot = ("Sources: Private Lender Link, Origination Fees / Points for Private Mortgages, updated Jul 7, 2023 (a percentage of the loan amount charged for originating the loan); "
            "Capital Funding, Hard Money Lender Fee Structures: A Broker's Guide, Jul 5, 2026 (broker fees can be embedded within origination points). "
            "Illustrative inputs: $355,000 loan, 2.5 points, 1 point to broker, 10.3 percent interest-only, 12 months. "
            "Arithmetic: 355,000 x 2.5% = 8,875; x 1% = 3,550; 8,875 - 3,550 = 5,325; 355,000 x 10.3% = 36,565; 41,890 / 355,000 = 11.8%; 45,440 / 355,000 = 12.8%.")
    return shell("One loan, 2.5 points.", "Who keeps them?",
                 "A broker's share of points changes the lender's yield &middot; illustrative", b, foot, 826)


PAGES = {"origination-points-split": ("images/2026-11-14/1347-fb-origination-points-split.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
