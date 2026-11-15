#!/usr/bin/env python3
"""Graphic for note sale basics. Run from repo root: python3 tools/weeks/2026-11-16-note-sale-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ITEMS = [("Original note", "The original promissory note, not a copy"),
         ("Allonge", "The instrument that endorses the note to the next holder"),
         ("Mortgage details", "Legal description and recording information match the title policy"),
         ("Recorded assignments", "Any assignments of the mortgage have been properly recorded"),
         ("Payment history", "Whether the borrower is current or in default"),
         ("Insurance", "Policies, and whether coverage is adequate")]

def gfx():
    body = '<div class="abs lbl" style="left:68px;top:284px">The file a buyer can review</div>'
    for i, (t, d) in enumerate(ITEMS):
        x = 68 + (i % 2) * 476
        y = 320 + (i // 2) * 150
        body += (f'<div class="card" style="left:{x}px;top:{y}px;width:468px;height:132px">'
                 f'<div class="abs" style="left:0;top:0;width:8px;height:132px;border-radius:14px 0 0 14px;background:#C9A84C"></div>'
                 f'<div class="abs mono gold" style="left:30px;top:20px;font-size:26px">{i+1:02d}</div>'
                 f'<div class="abs" style="left:92px;top:20px;width:350px;font-size:23px;line-height:30px;font-weight:700">{t}</div>'
                 f'<div class="abs steel" style="left:30px;top:66px;width:410px;font-size:17px;line-height:24px">{d}</div></div>')
    body += ('<div class="panel" style="top:788px;height:84px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:21px">TAKEAWAY</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:700px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Sellers can gather these in one package before the first call. Requirements vary by buyer.</div></div>')
    return page("light", "NOTE SALES", "PRIVATE LENDING, EXPLAINED", "What a note buyer", "asks to see in the file",
                "Six items from public loan purchase guidance", body,
                "Sources: Thomson Reuters Practical Law, Loan Purchase Due Diligence Transaction Checklist, hunton.com (page undated, accessed 2026-11-15); "
                "GlobeSt, Note Sales Unwrapped (page undated, accessed 2026-11-15). Item order is editorial.", 900)

PAGES = {"note-sale-basics": ("images/2026-11-19/1540-li-note-sale-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
