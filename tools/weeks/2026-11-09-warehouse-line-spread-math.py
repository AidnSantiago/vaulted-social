#!/usr/bin/env python3
"""Graphic for warehouse line spread math (Facebook, Thu Nov 12, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-warehouse-line-spread-math.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, RATE, SHARE, LINE_RATE = 750000, 0.1075, 0.65, 0.0775  # illustrative
LINE = LOAN * SHARE
EQ = LOAN - LINE
INC = LOAN * RATE
COST = LINE * LINE_RATE
NET = INC - COST
ROE = NET / EQ * 100
assert LINE == 487500 and EQ == 262500 and INC == 80625 and COST == 37781.25 and NET == 42843.75 and round(ROE, 2) == 16.32


def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">Illustrative $750,000 loan, funding split</div>'
    wl = round(944 * SHARE)
    b += f'<div class="abs seg-steel" style="left:68px;top:296px;width:{wl}px;height:84px;border-radius:10px 0 0 10px"></div>'
    b += f'<div class="abs seg-gold" style="left:{68+wl}px;top:296px;width:{944-wl}px;height:84px;border-radius:0 10px 10px 0"></div>'
    b += f'<div class="abs mono" style="left:92px;top:312px;font-size:26px;line-height:30px;white-space:nowrap">$487,500</div>'
    b += f'<div class="abs" style="left:92px;top:344px;font-size:15px;color:#D5DDE8;white-space:nowrap">Credit line, 65%, at 7.75%</div>'
    b += f'<div class="abs mono" style="left:{68+wl+20}px;top:312px;font-size:26px;line-height:30px;white-space:nowrap">$262,500</div>'
    b += f'<div class="abs" style="left:{68+wl+20}px;top:344px;font-size:15px;white-space:nowrap">Lender equity, 35%</div>'
    b += stat_card(68, 416, 290, 150, "$80,625", "Interest earned", "$750,000 x 10.75%", 40)
    b += stat_card(395, 416, 290, 150, "$37,781", "Line interest paid", "$487,500 x 7.75% = $37,781.25", 40)
    b += stat_card(722, 416, 290, 150, "$42,844", "Net spread", "$80,625 - $37,781.25", 40)
    b += panel(596, 100, "$42,843.75 / $262,500", "= 16.32% a year on the lender's own money, before fees and losses.", 400, 24)
    b += panel(722, 100, "Spread only pays", "if the borrower pays. Losses and idle time come out of this number.", 430, 25)
    foot = ("Sources: Axos Bank, What is warehouse lending?, Dec 11, 2025 (definition of warehouse lending); Customers Bank, How Warehouse Lending Works "
            "for Mortgage Originators, page undated, accessed 2026-11-08. Illustrative inputs; terms vary by lender. "
            "Arithmetic: 750,000 x 65% = 487,500; 80,625 - 37,781.25 = 42,843.75; 42,843.75 / 262,500 = 16.32%.")
    return shell("A credit line funds the loan.", "The spread pays the equity.",
                 "Loan yield minus borrowing cost &middot; illustrative", b, foot, 850)


PAGES = {"warehouse-line-spread-math": ("images/2026-11-12/1247-fb-warehouse-line-spread-math.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
