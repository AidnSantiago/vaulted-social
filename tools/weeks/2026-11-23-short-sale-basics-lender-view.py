#!/usr/bin/env python3
"""Graphic for short sale basics (lender view). Run from repo root: python3 tools/weeks/2026-11-23-short-sale-basics-lender-view.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

PAYOFF, SALE = 255000, 215000
GAP = PAYOFF - SALE

def gfx():
    assert GAP == 40000
    track = 944
    wsale = track * SALE / PAYOFF
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative short sale: payoff vs offer</div>'
    body += '<div class="abs steel" style="left:68px;top:322px;font-size:18px">Loan payoff</div>'
    body += f'<div class="abs" style="left:68px;top:350px;width:{track}px;height:46px;border-radius:8px;background:#3F5470"></div>'
    body += f'<div class="abs mono" style="left:88px;top:361px;font-size:22px;color:#fff">${PAYOFF:,}</div>'
    body += '<div class="abs steel" style="left:68px;top:412px;font-size:18px">Buyer offer the lender agrees to accept</div>'
    body += f'<div class="abs" style="left:68px;top:440px;width:{wsale:.0f}px;height:46px;border-radius:8px;background:#5B7DAE"></div>'
    body += f'<div class="abs" style="left:{68+wsale:.0f}px;top:440px;width:{track-wsale:.0f}px;height:46px;border-radius:0 8px 8px 0;border:1.5px dashed #9A7B22;background:rgba(201,168,76,.28)"></div>'
    body += f'<div class="abs mono" style="left:88px;top:451px;font-size:22px;color:#fff">${SALE:,}</div>'
    body += f'<div class="abs mono" style="left:{68+wsale+14:.0f}px;top:451px;font-size:22px;color:#0B1F3A">${GAP:,}</div>'
    body += '<div class="abs steel" style="left:68px;top:496px;font-size:17px">Shortfall: whether the borrower still owes it varies by state and by the lender agreement.</div>'
    body += ('<div class="card" style="left:68px;top:540px;width:458px;height:200px"><div class="abs lbl" style="left:22px;top:18px">Short sale</div>'
             '<div class="abs" style="left:22px;top:50px;width:414px;font-size:19px;line-height:27px">The sale happens only with the approval of the mortgage lender, at a price below what is owed.</div></div>')
    body += ('<div class="card" style="left:554px;top:540px;width:458px;height:200px"><div class="abs lbl" style="left:22px;top:18px">Foreclosure</div>'
             '<div class="abs" style="left:22px;top:50px;width:414px;font-size:19px;line-height:27px">Longer timelines may add missed property taxes, hazard insurance and HOA payments. Fed study: short sales sold for 9.2 to 10.5 percent more on average.</div></div>')
    body += ('<div class="panel" style="top:764px;height:84px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'Lenders can weigh the offer against the full cost and time of foreclosing, not just the payoff.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Short sale or", "foreclosure?",
                "The lender agrees to take less than the payoff", body,
                "Sources: CFPB, What is a short sale (reviewed Feb 2, 2024); Freddie Mac, What Is a Short Sale (reviewed Oct 13, 2025); Federal Reserve Bank of Philadelphia WP 19-13 (Feb 2019, home sales). "
                "Arithmetic: 255,000 - 215,000 = 40,000. Figures illustrative.", 880)

PAGES = {"short-sale-basics-lender-view": ("images/2026-11-27/1727-fb-short-sale-basics-lender-view.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
