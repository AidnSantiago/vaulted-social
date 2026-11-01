#!/usr/bin/env python3
"""Graphic for post-closing liquidity (Facebook, Wed Nov 4, 2026, 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-post-closing-liquidity.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    b = step_cards([
        (1, "Liquid assets", "What the borrower holds before the deal funds.", None),
        (2, "Close the loan", "Down payment and all transaction costs are paid.", None),
        (3, "Cash left", "Post-closing liquidity: what lenders can look at.", None),
    ], top=272, h=176)
    b += ('<div class="card" style="left:68px;top:480px;width:462px;height:190px">'
          '<div class="abs lbl" style="left:22px;top:20px">What it can protect against</div>'
          '<div class="abs" style="left:22px;top:56px;width:420px;font-size:20px;line-height:30px;color:#F0EDE4">'
          '<span class="gold">Rent can dip.</span> A tenant can leave. Reserves show a borrower can keep paying while the property recovers.</div></div>')
    b += ('<div class="card" style="left:550px;top:480px;width:462px;height:190px">'
          '<div class="abs lbl" style="left:22px;top:20px">Generally does not count</div>'
          '<div class="abs" style="left:22px;top:56px;width:420px;font-size:20px;line-height:30px;color:#F0EDE4">'
          '<span class="gold">Gifts.</span><br><span class="gold">Unsecured borrowed funds.</span><br><span class="gold">Home equity.</span></div></div>')
    b += panel(704, 96, "THE CHECK", "Lenders can ask what cash is left after closing, not just what is needed to close.", 520, 28)
    foot = ("Sources: GoSBA Loans, Post-Close Liquidity (modified Jun 10, 2026); Lendmire, DSCR Reserve Requirements (Nov 1, 2026); "
            "Fannie Mae Selling Guide B3-4.1-01 (Aug 7, 2024). What counts varies by lender. General education, not legal or investment advice.")
    return shell("Cash to close is one test.", "Cash left is another.",
                 "What post-closing liquidity means for a lender.", b, foot, 836)

PAGES = {"post-closing-liquidity": ("images/2026-11-04/1727-fb-post-closing-liquidity.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
