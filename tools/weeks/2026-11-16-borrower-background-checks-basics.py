#!/usr/bin/env python3
"""Graphic for borrower-background-checks-basics. Run from repo root: python3 tools/weeks/2026-11-16-borrower-background-checks-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import css, V
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

CHK = ('<svg class="abs" style="left:22px;top:20px" width="34" height="34" viewBox="0 0 26 26"><rect x="1.5" y="1.5" width="23" height="23" rx="5" fill="none" stroke="#9C7F2B" stroke-width="2"/>'
       '<path d="M7 13.4 L11.2 17.4 L19 8.8" fill="none" stroke="#9C7F2B" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def gfx():
    cards = [("Identity", "Who is signing?", "Government ID checked against public records. Confirm the signer is who they claim to be."),
             ("Litigation", "Any lawsuits or filings?", "Court records can show lawsuits, judgments, bankruptcies and prior foreclosures."),
             ("Liens", "What is already attached?", "A lien review can look for IRS tax liens, mechanics' liens or HOA super-liens."),
             ("Experience", "What have they finished?", "A project history list: addresses, purchase prices, sale prices and timelines.")]
    b = ""
    for i, (h, q, d) in enumerate(cards):
        x = 68 + (i % 2) * 478
        y = 290 + (i // 2) * 232
        b += (f'<div class="card" style="left:{x}px;top:{y}px;width:466px;height:216px">{CHK}'
              f'<div class="abs lbl" style="left:70px;top:19px">{h}</div>'
              f'<div class="abs" style="left:70px;top:42px;font-size:24px;font-weight:700;font-family:Georgia,serif">{q}</div>'
              f'<div class="abs steel" style="left:24px;top:98px;width:418px;font-size:19px;line-height:28px">{d}</div></div>')
    b += ('<div class="panel" style="top:770px;height:92px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:20px">Before funding, not after</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:500px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">What a lender checks varies by lender and by state.</div></div>')
    foot = ("Sources: LBC Capital, Know Your Borrower (Nov 12, 2026); Note Servicing Center, Hard Money Due Diligence Checklist (page undated, accessed 2026-11-15).")
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css("light")}</style></head><body>'
            '<div class="hdr"><div class="tag">LENDER CHECKLIST</div><div class="eyebrow">PRIVATE LENDING, EXPLAINED</div></div>'
            '<h1>Four borrower checks<br><em>before closing</em></h1>'
            '<div class="sub">What a lender can look at, and why each one matters</div>'
            f'{b}<div class="foot" style="top:884px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div></body></html>')

PAGES = {"borrower-background-checks-basics": ("images/2026-11-20/1727-fb-borrower-background-checks-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
