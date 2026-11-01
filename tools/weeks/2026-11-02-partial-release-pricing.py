#!/usr/bin/env python3
"""Graphic for partial release pricing (FB Thu Nov 5, 2026, 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-partial-release-pricing.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, LOTS, VAL, PCT = 900000, 4, 300000, 1.20
ALLOC = LOAN // LOTS
REL = round(ALLOC * PCT)
REM_A, REM_B = LOAN - ALLOC, LOAN - REL
COLL = VAL * (LOTS - 1)
assert (ALLOC, REL, REM_A, REM_B, COLL) == (225000, 270000, 675000, 630000, 900000)
assert round(REM_A / COLL * 100) == 75 and round(REM_B / COLL * 100) == 70

def col(x, title, pill, rows, cls):
    w = 456
    b = f'<div class="card" style="left:{x}px;top:300px;width:{w}px;height:400px"></div>'
    b += f'<div class="abs {cls} mono" style="left:{x+20}px;top:320px;padding:8px 14px;border-radius:8px;font-size:18px;white-space:nowrap">{title}</div>'
    y = 380
    for lab, val, big in rows:
        b += f'<div class="abs" style="left:{x+20}px;top:{y}px;font-size:17px;color:#A5B2C3;white-space:nowrap">{lab}</div>'
        b += f'<div class="abs mono {"gold" if big else ""}" style="left:{x+20}px;top:{y+24}px;font-size:{40 if big else 30}px;line-height:46px;white-space:nowrap">{val}</div>'
        y += 80 if big else 76
    return b

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:240px">Illustrative: $900,000 loan, 4 lots at $300,000 each</div>'
    b = b.replace("top:240px", "top:268px")
    b += col(68, "Pro rata release", "", [("Paid down to release lot 1", "$225,000", False), ("Remaining loan", "$675,000", False),
        ("Remaining value, 3 lots", "$900,000", False), ("Remaining loan to value", "75%", True)], "seg-steel")
    b += col(556, "120% release", "", [("Paid down to release lot 1", "$270,000", False), ("Remaining loan", "$630,000", False),
        ("Remaining value, 3 lots", "$900,000", False), ("Remaining loan to value", "70%", True)], "seg-gold")
    b += panel(728, 96, "$225,000 x 120% = $270,000", "A higher release price can lower the remaining loan to value after a lot sells.", 430, 24)
    foot = ("Sources: Lendmire, DSCR Blanket Loan Release Prices (published 2026-10-11), citing a legal glossary range of about 110% to 125% of the pro rata allocation; "
            "C-Loans, Partial Release Clauses on Commercial Loans (2009-12-17). Terms vary by lender. "
            "Arithmetic: 900,000 / 4 = 225,000; x 1.20 = 270,000; 900,000 - 270,000 = 630,000; 630,000 / 900,000 = 70%; 675,000 / 900,000 = 75%. Example is illustrative.")
    return shell("One lot sells. Pro rata price", "or 120 percent?", "Pro rata share versus a 120 percent release price", b, foot, 844,
                 eyebrow="LOAN STRUCTURING FOR PRIVATE LENDERS")

PAGES = {"partial-release-pricing": ("images/2026-11-05/1247-fb-partial-release-pricing.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
