#!/usr/bin/env python3
"""Graphic for year-end portfolio review checklist. Run from repo root: python3 tools/weeks/2026-11-23-year-end-portfolio-review-checklist.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOANS, MATURING = 24, 6

def gfx():
    assert LOANS - MATURING == 18
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative: 24 loans, 6 mature in the next 90 days</div>'
    # dot grid: 3 rows of 8
    for i in range(LOANS):
        r, c = divmod(i, 8)
        hot = i < MATURING
        bg = "#C9A84C" if hot else "rgba(11,31,58,.10)"
        col = "#0B1F3A" if hot else "#3F5470"
        body += (f'<div class="abs mono" style="left:{68 + c*60}px;top:{330 + r*60}px;width:50px;height:50px;border-radius:10px;background:{bg};color:{col};'
                 f'display:flex;align-items:center;justify-content:center;font-size:17px">{i+1}</div>')
    body += ('<div class="abs steel" style="left:68px;top:520px;width:470px;font-size:18px;line-height:26px">'
             'Gold: loans maturing in the next 90 days. A lender can contact each borrower before the date.</div>')
    items = [("Maturities", "Next 90 days"), ("Insurance", "Expiration dates"), ("Property taxes", "Payment status"),
             ("Late payers", "Who is behind"), ("Extensions", "Open requests")]
    y = 330
    for i, (t, d) in enumerate(items, 1):
        body += (f'<div class="card" style="left:580px;top:{y}px;width:432px;height:62px">'
                 f'<div class="abs mono" style="left:14px;top:12px;width:38px;height:38px;border-radius:50%;background:#C9A84C;color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:18px">{i}</div>'
                 f'<div class="abs" style="left:68px;top:0;height:100%;display:flex;align-items:center;font-size:21px;font-weight:700">{t}</div>'
                 f'<div class="abs steel" style="right:18px;top:0;height:100%;display:flex;align-items:center;font-size:16.5px">{d}</div></div>')
        y += 72
    body += ('<div class="card" style="left:68px;top:696px;width:944px;height:116px"><div class="abs lbl" style="left:24px;top:16px">Why it matters</div>'
             '<div class="abs" style="left:24px;top:46px;width:896px;font-size:19px;line-height:27px">NCUA examiner guidance says systems should identify and report maturing loans. Starting in December leaves time to call borrowers first.</div></div>')
    body += ('<div class="panel" style="top:832px;height:52px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:19px;color:#3F5470">'
             'Five lists, one pass. Process varies by lender.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "A year-end portfolio review:", "five lists to run",
                "Catch Q1 maturities before they catch you", body,
                "Sources: NCUA, Commercial Loan Administration, Examiner's Guide (updated 2021-10-14); Abrigo, After the Closing: A Recipe for Sound Loan Administration (2013-06-27, modified 2019-07-03). "
                "Loan counts illustrative. Arithmetic: 24 - 6 = 18.", 905)

PAGES = {"year-end-portfolio-review-checklist": ("images/2026-11-29/1727-fb-year-end-portfolio-review-checklist.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
