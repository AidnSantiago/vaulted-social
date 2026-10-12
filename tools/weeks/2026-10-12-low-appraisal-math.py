#!/usr/bin/env python3
"""Graphic for the low-appraisal-math post (Facebook, Tue Oct 13, 2026 12:47 pm ET). Illustrative example.
Run from repo root:  python3 tools/weeks/2026-10-12-low-appraisal-math.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PRICE, APPR, LTV = 420000, 385000, 0.70   # illustrative


def gfx():
    loan_c, loan_a = PRICE * LTV, APPR * LTV
    gap = loan_c - loan_a
    cash_c, cash_a = PRICE - loan_c, PRICE - loan_a
    assert (round(loan_c), round(loan_a), round(gap), round(cash_c), round(cash_a)) == (294000, 269500, 24500, 126000, 150500)

    b = stat_card(68, 276, 290, 150, "$294,000", "70% of $420,000 price", "if sized on the contract")
    b += stat_card(395, 276, 290, 150, "$269,500", "70% of $385,000 value", "sized on the lower value")
    b += stat_card(722, 276, 290, 150, "$24,500", "less loan", "the gap someone must cover")

    b += '<div class="abs lbl" style="left:68px;top:464px">Who funds the $420,000 purchase</div>'
    X0, W = 232, 700
    S = W / PRICE
    H = 56

    def lab(y, big, small):
        return (f'<div class="abs" style="left:68px;top:{y}px;width:156px;height:{H}px;display:flex;flex-direction:column;justify-content:center">'
                f'<div style="font-size:19px;line-height:24px;font-weight:700">{big}</div>'
                f'<div style="font-size:14.5px;line-height:18px;color:#8A9BB0">{small}</div></div>')

    def seg(y, x, w, cls, text, rad, pad=14):
        return (f'<div class="abs {cls} mono" style="left:{x:.1f}px;top:{y}px;width:{w:.1f}px;height:{H}px;border-radius:{rad};'
                f'display:flex;align-items:center;padding-left:{pad:.0f}px;font-size:19px;white-space:nowrap">{text}</div>')

    y1, y2 = 502, 580
    b += lab(y1, "Contract price", "$420,000") + lab(y2, "Appraisal", "$385,000")
    b += seg(y1, X0, loan_c * S, "seg-gold", "Loan $294,000", "8px 0 0 8px")
    b += seg(y1, X0 + loan_c * S, cash_c * S, "seg-steel", "Cash $126,000", "0 8px 8px 0")
    b += seg(y2, X0, loan_a * S, "seg-gold", "Loan $269,500", "8px 0 0 8px")
    b += seg(y2, X0 + loan_a * S, cash_a * S, "seg-steel", "Cash $150,500", "0 8px 8px 0", 14 + gap * S)
    gx = X0 + loan_a * S
    b += (f'<div class="abs" style="left:{gx:.1f}px;top:{y2}px;width:{gap * S:.1f}px;height:{H}px;'
          f'border:1.5px dashed rgba(226,194,101,.9);border-radius:0;'
          f'background:repeating-linear-gradient(135deg,rgba(226,194,101,.30) 0 6px,rgba(226,194,101,0) 6px 12px)"></div>')
    b += (f'<div class="abs" style="left:{gx - 60:.1f}px;top:{y2 + H + 8}px;width:260px;font-size:15px;line-height:20px;color:#E2C265">'
          f'hatched: the $24,500 gap</div>')
    b += '<div class="abs" style="left:68px;top:700px;width:944px;font-size:16.5px;line-height:23px;color:#A5B2C3">The gap can be covered by more borrower cash, a lower price, or a reworked deal. Whether max LTV applies to the lower value or the contract price varies by lender.</div>'
    b += panel(762, 84, "LOAN = LTV x VALUE USED", "The value a lender uses sets the loan.", 360, 24)
    foot = ("Sources: Lendmire, Hard Money Loan Based Upon Appraised Value (updated Oct 11, 2026): the loan amount is calculated as a percentage of the lower of appraised value or purchase price. "
            "Montegra, How Hard Money Lenders Determine Loan-To-Value Ratios (Jul 16, 2015): lender practice differs. The Mortgage Reports (updated Dec 10, 2024). "
            "Illustrative: price $420,000, appraisal $385,000, 70% max LTV. 0.70 x 420,000 = 294,000; 0.70 x 385,000 = 269,500; gap 24,500; "
            "cash = 420,000 - loan = 126,000 and 150,500.")
    return shell("Price $420,000, appraised $385,000.", "The 70% LTV loan shrinks $24,500.",
                 "Illustrative worked example &middot; loan = max LTV x the value the lender uses", b, foot, 868,
                 eyebrow="PRIVATE LENDING, EXPLAINED")


PAGES = {"low-appraisal-math": ("images/2026-10-13/1247-fb-low-appraisal-math.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
