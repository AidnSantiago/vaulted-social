#!/usr/bin/env python3
"""Graphic for loan extension request checklist. Run from repo root: python3 tools/weeks/2026-11-23-loan-extension-request-checklist.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, PCT = 460000, 1
FEE = LOAN * PCT // 100

def gfx():
    assert FEE == 4600
    rows = [("Value", "Current condition and an updated valuation"),
            ("Taxes and insurance", "Evidence that both are current"),
            ("Payment history", "Record of performance, plus any delays explained"),
            ("Exit plan", "A named repayment source, remaining steps, a realistic schedule"),
            ("Fee", "Last: $460,000 x 1 percent = $4,600")]
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative: $460,000 loan, 1 percent extension fee</div>'
    y = 326
    for i, (t, d) in enumerate(rows, 1):
        last = i == 5
        bg = "background:#0B1F3A;" if last else ""
        ink = "#F0EDE4" if last else "#0B1F3A"
        sub = "#E2C265" if last else "#3F5470"
        circ = "#C9A84C"
        body += (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:84px;{bg}">'
                 f'<div class="abs mono" style="left:22px;top:20px;width:44px;height:44px;border-radius:50%;background:{circ};color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:21px">{i}</div>'
                 f'<div class="abs" style="left:90px;top:0;height:100%;width:260px;display:flex;align-items:center;font-size:24px;font-weight:700;color:{ink}">{t}</div>'
                 f'<div class="abs" style="left:350px;top:0;height:100%;width:570px;display:flex;align-items:center;font-size:19px;line-height:26px;color:{sub}">{d}</div></div>')
        y += 98
    body += ('<div class="panel" style="top:830px;height:62px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:19px;color:#3F5470">'
             'The fee comes last: it does not fix weak answers to the first four. Terms vary by lender.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "An extension request:", "review in this order",
                "Five checks before a lender says yes", body,
                "Sources: Dan Handford, BiggerPockets, When Real Estate Loans Need More Time (page undated, accessed 2026-11-22); Federal Reserve SR 23-5, interagency policy statement (June 30, 2023). "
                "Arithmetic: 460,000 x 0.01 = 4,600. Loan and fee illustrative.", 905)

PAGES = {"loan-extension-request-checklist": ("images/2026-11-24/1727-fb-loan-extension-request-checklist.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
