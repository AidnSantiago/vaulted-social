#!/usr/bin/env python3
"""Graphic for payoff statement and per diem (Facebook, Sat Oct 17, 2026 5:27 pm ET).
Run from repo root: python3 tools/weeks/2026-10-12-payoff-statement-per-diem.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BAL, RATE, DAYS = 275000, 9, 10   # all illustrative


def gfx():
    per_diem = BAL * RATE / 100 / 365
    ten = per_diem * DAYS
    assert f"{per_diem:.2f}" == "67.81" and f"{ten:.2f}" == "678.08"
    X0, S = 68, 944 / ten
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative loan, actual/365 day count</div>'
    b += stat_card(68, 304, 290, 150, "$275,000", "balance", "illustrative", 40)
    b += stat_card(395, 304, 290, 150, "9%", "note rate", "illustrative")
    b += stat_card(722, 304, 290, 150, "$67.81", "per diem", "$275,000 x 9% / 365")
    b += '<div class="abs lbl" style="left:68px;top:488px">Interest added if the payoff date slips</div>'
    H = 64
    b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:530px;width:{per_diem * S:.1f}px;height:{H}px;border-radius:8px;'
          f'"></div><div class="abs mono gold" style="left:{X0 + per_diem * S + 16:.1f}px;top:530px;height:{H}px;display:flex;align-items:center;font-size:22px">1 day: $67.81</div>')
    b += (f'<div class="abs seg-gold mono" style="left:{X0}px;top:614px;width:{ten * S:.1f}px;height:{H}px;border-radius:8px;'
          f'display:flex;align-items:center;padding-left:18px;font-size:22px">10 days: about $678</div>')
    b += ('<div class="abs steel" style="left:68px;top:696px;width:944px;font-size:17px;line-height:24px">'
          'A payoff statement is for a specific day. Past that day, interest keeps accruing.</div>')
    b += panel(752, 92, "ASK FOR THE PER DIEM",
               "Day count and fees vary by note. Check the note.", 430, 24)
    foot = ("Sources: CFPB, What is a payoff amount, last reviewed Aug 28, 2026; Rhode Island General Laws 19-9-9 "
            "(page undated, accessed 2026-10-17); Federal Title and Escrow, Mar 20, 2013. "
            "Illustrative: $275,000, 9%, actual/365. Per diem = 275,000 x 0.09 / 365 = $67.81; x 10 days = $678.08.")
    return shell("A payoff is good for one day.", "Per diem covers the rest.",
                 "What a payoff statement shows &middot; illustrative", b, foot, 876)


PAGES = {"payoff-statement-per-diem": ("images/2026-10-17/1727-fb-payoff-statement-per-diem.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
