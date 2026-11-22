#!/usr/bin/env python3
"""Graphic for borrower reporting covenants basics. Run from repo root: python3 tools/weeks/2026-11-23-borrower-reporting-covenants-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    rows = [("QUARTERLY", "Financial statements", "Due 25 days after quarter end"),
            ("ANNUAL", "Tax returns", "Copy of each year's return"),
            ("BEFORE EXPIRY", "Insurance renewal", "Proof the policy was renewed")]
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative reporting schedule</div>'
    y = 326
    for when, what, detail in rows:
        body += (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:132px">'
                 f'<div class="abs" style="left:26px;top:0;height:100%;width:250px;display:flex;align-items:center"><span class="pill">{when}</span></div>'
                 f'<div class="abs" style="left:290px;top:30px;font-family:Georgia,serif;font-size:32px;font-weight:700;color:#0B1F3A">{what}</div>'
                 f'<div class="abs" style="left:290px;top:76px;font-size:21px;color:#3F5470">{detail}</div></div>')
        y += 150
    body += ('<div class="panel" style="top:790px;height:84px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:27px;color:#3F5470">'
             'A named document and a date make a request checkable. Terms vary by lender.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Reporting covenants:", "what a borrower sends",
                "Affirmative covenants can require financials, taxes and insurance", body,
                "Sources: Olshan, Negotiating Loan Documents for Borrowers Part V (2020-06-16); Truist, Understanding loan covenants (modified 2026-07-31); "
                "American Bar Association, Negotiating the Loan Agreement (page undated, accessed 2026-11-22). Schedule illustrative.", 905)

PAGES = {"borrower-reporting-covenants-basics": ("images/2026-11-26/1247-fb-borrower-reporting-covenants-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
