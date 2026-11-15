#!/usr/bin/env python3
"""Graphic for balloon maturity refinance risk. Run from repo root: python3 tools/weeks/2026-11-16-balloon-maturity-refi-risk.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BAL, LTV = 340000, 0.75
V1, V2 = 480000, 420000

def gfx():
    n1, n2 = V1 * LTV, V2 * LTV
    assert n1 == 360000 and n2 == 315000 and BAL - n2 == 25000
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative: $340,000 balloon due at month 12, refinance at 75 percent of value</div>'
    def card(x, cap, val, new, ok, col):
        res = ("Covers the balloon" if ok else "Short by $25,000")
        return (f'<div class="card" style="left:{x}px;top:332px;width:458px;height:300px">'
                f'<div class="abs lbl" style="left:24px;top:20px">{cap}</div>'
                f'<div class="abs steel" style="left:24px;top:56px;font-size:18px">Value at maturity</div>'
                f'<div class="abs mono" style="left:24px;top:82px;font-size:36px">{val}</div>'
                f'<div class="abs steel" style="left:24px;top:140px;font-size:18px">New loan at 75 percent</div>'
                f'<div class="abs mono" style="left:24px;top:166px;font-size:36px">{new}</div>'
                f'<div class="abs" style="left:24px;top:232px;width:410px;height:48px;border-radius:10px;background:{col};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:21px;color:{"#0B1F3A" if ok else "#FFFFFF"}">{res}</div></div>')
    body += card(68, "The plan", "$480,000", "$360,000", True, "#C9A84C")
    body += card(554, "Value falls", "$420,000", "$315,000", False, "#B0463C")
    body += ('<div class="abs mono" style="left:68px;top:662px;width:944px;text-align:center;font-size:24px">$340,000 balloon  -  $315,000 new loan  =  <span class="gold">$25,000 gap</span></div>')
    body += ('<div class="panel" style="top:722px;height:104px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">BEFORE MATURITY</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:620px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Lenders can re-check property value and the borrower exit plan well before the due date, not in the final week. Terms vary by lender.</div></div>')
    return page("light", "BALLOON LOANS", "PRIVATE LENDING, EXPLAINED", "A balloon is due in 12 months.", "Will the refinance cover it?",
                "How a falling value turns a planned exit into a payoff gap", body,
                "Source: CFPB, What is a balloon loan? (last reviewed Aug 28, 2026): a balloon payment is \"a large, one-time payment at the end of the loan term.\" "
                "Arithmetic: 480,000 x 0.75 = 360,000; 420,000 x 0.75 = 315,000; 340,000 - 315,000 = 25,000. Loan, values and 75 percent refinance limit are illustrative.", 850)

PAGES = {"balloon-maturity-refi-risk": ("images/2026-11-20/0800-fb-balloon-maturity-refi-risk.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
