#!/usr/bin/env python3
"""Graphic for borrower credit score use in private lending. Run from repo root: python3 tools/weeks/2026-11-23-borrower-credit-score-use-private-lending.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def box(x, y, w, h, lbl, big, line, src):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs lbl" style="left:22px;top:18px">{lbl}</div>'
            f'<div class="abs" style="left:22px;top:46px;width:{w-44}px;font-family:Georgia,serif;font-weight:700;font-size:27px;line-height:32px">{big}</div>'
            f'<div class="abs steel" style="left:22px;top:84px;width:{w-44}px;font-size:17px;line-height:24px">{line}</div>'
            f'<div class="abs gold" style="left:22px;top:{h-32}px;font-size:14px;font-weight:700">{src}</div></div>')

def gfx():
    body = '<div class="abs lbl" style="left:68px;top:290px">What the two guides say lenders look at</div>'
    body += box(68, 326, 458, 168, "1. Collateral", "Largely about the property", "Requirements are largely based on the value of the collateral.", "NerdWallet")
    body += box(554, 326, 458, 168, "2. Skin in the game", "Not credit score alone", "Called the biggest factor in qualifying for a hard money loan.", "Point")
    body += box(68, 514, 458, 168, "3. Experience", "Matters on rehab loans", "Lenders often require a certain level of experience for rehabs.", "Point")
    body += box(554, 514, 458, 168, "4. Credit score", "Checked, weighed less", "A FICO of 550 or higher is preferred by some lenders.", "NerdWallet, Point")
    body += ('<div class="panel" style="top:712px;height:84px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">Weights vary by lender</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:430px;display:flex;align-items:center;font-size:17px;line-height:24px;color:#3F5470">A lender can decide how much each piece counts.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Credit score is one input",
                "not the whole decision", "What hard money guides say lenders weigh", body,
                "Sources: NerdWallet, Hard Money Business Loans (updated 2026-03-10); Point, Hard Money Loan Requirements (published 2025-09-22). "
                "Both are general guides; requirements vary by lender.", 830)

PAGES = {"borrower-credit-score-use-private-lending": ("images/2026-11-28/0932-fb-borrower-credit-score-use-private-lending.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
