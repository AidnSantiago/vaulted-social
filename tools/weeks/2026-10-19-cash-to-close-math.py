#!/usr/bin/env python3
"""Graphic for the cash-to-close-math post (Facebook, Tue Oct 20, 2026 12:47 pm ET). Illustrative example.
Run from repo root: python3 tools/weeks/2026-10-19-cash-to-close-math.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PRICE, LTV, POINTS, CLOSING = 175000, 0.85, 2, 4200   # illustrative


def gfx():
    loan = PRICE * LTV
    down = PRICE - loan
    pts = loan * POINTS / 100
    total = down + pts + CLOSING
    assert (round(loan), round(down), round(pts), round(total)) == (148750, 26250, 2975, 33425)
    b = stat_card(68, 276, 290, 150, "$148,750", "85% loan", "of the $175,000 price")
    b += stat_card(395, 276, 290, 150, "$26,250", "down payment", "$175,000 - $148,750")
    b += stat_card(722, 276, 290, 150, "$2,975", "two points", "2% of the $148,750 loan")
    b += '<div class="abs lbl" style="left:68px;top:470px">Cash the borrower brings to closing</div>'
    X0, W, H, Y = 68, 944, 70, 508
    S = W / total
    segs = [(down, "seg-gold", "Down $26,250", "8px 0 0 8px"),
            (pts, "seg-blue2", "", "0"),
            (CLOSING, "seg-steel", "", "0 8px 8px 0")]
    x = X0
    for v, cls, t, rad in segs:
        w = v * S
        b += (f'<div class="abs {cls} mono" style="left:{x:.1f}px;top:{Y}px;width:{w:.1f}px;height:{H}px;border-radius:{rad};'
              f'display:flex;align-items:center;padding-left:14px;font-size:19px;white-space:nowrap">{t}</div>')
        x += w
    xp = X0 + down * S
    xc = xp + pts * S
    b += (f'<div class="abs mono" style="left:{xp:.1f}px;top:{Y + H + 10}px;font-size:17px;color:#A5B2C3">Points $2,975</div>')
    b += (f'<div class="abs mono" style="right:68px;top:{Y + H + 38}px;font-size:17px;color:#A5B2C3">Closing costs $4,200</div>')
    b += '<div class="abs" style="left:68px;top:672px;width:944px;font-size:16.5px;line-height:23px;color:#A5B2C3">Rehab funds and an appraisal fee vary by lender and are not in this total.</div>'
    b += panel(730, 90, "$26,250 + $2,975 + $4,200 = $33,425", "The full cash number, not just the down payment.", 330, 24)
    foot = ("Sources: New Silver, What are Points on a Hard Money Loan (Nov 19, 2025): each point is one percent of the loan amount. "
            "BiggerPockets, 10 Important Terms (updated Feb 27, 2024): points are fees charged by the lender at closing. "
            "CFPB, Closing Disclosure explainer (Oct 10, 2023): cash to close is the amount paid at closing. "
            "Illustrative: price $175,000, loan 85%, 2 points, closing costs $4,200. 0.85 x 175,000 = 148,750; 175,000 - 148,750 = 26,250; "
            "0.02 x 148,750 = 2,975; 26,250 + 2,975 + 4,200 = 33,425.")
    return shell("$175,000 rehab purchase, 85% loan.", "The cash to close is $33,425.",
                 "Illustrative worked example &middot; down payment + points + closing costs", b, foot, 868)


PAGES = {"cash-to-close-math": ("images/2026-10-20/1247-fb-cash-to-close-math.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
