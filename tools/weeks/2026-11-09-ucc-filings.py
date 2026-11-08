#!/usr/bin/env python3
"""Graphic for UCC filings vs mortgages. Run from repo root: python3 tools/weeks/2026-11-09-ucc-filings.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, y, w, h, head, sub, items, where, gold=False):
    c = "#E2C265" if gold else "#F0EDE4"
    s = (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
         f'<div class="abs mono" style="left:22px;top:20px;width:{w-44}px;font-size:22px;line-height:28px;color:{c}">{head}</div>'
         f'<div class="abs" style="left:22px;top:54px;width:{w-44}px;font-size:16px;line-height:22px;color:#8A9BB0">{sub}</div>')
    yy = 96
    for it in items:
        s += (f'<div class="abs" style="left:22px;top:{yy}px;width:{w-44}px;font-size:19px;line-height:24px;font-weight:700;color:#F0EDE4">{it}</div>')
        yy += 32
    s += (f'<div class="abs lbl" style="left:22px;top:{h-70}px;font-size:13px">Filed in</div>'
          f'<div class="abs" style="left:22px;top:{h-46}px;width:{w-44}px;font-size:17px;line-height:22px;color:#E2C265;font-weight:700">{where}</div></div>')
    return s

def gfx():
    b = col(68, 272, 450, 250, "MORTGAGE", "Real property", ["The land", "The building"], "County land records")
    b += col(562, 272, 450, 250, "UCC FINANCING STATEMENT", "Personal property", ["Equipment", "Membership interests"], "A separate UCC filing office", True)
    b += ('<div class="card" style="left:68px;top:548px;width:944px;height:150px">'
          '<div class="abs mono gold" style="left:22px;top:18px;font-size:22px;line-height:28px">FIXTURES: GOODS ATTACHED TO LAND</div>'
          '<div class="abs" style="left:22px;top:58px;width:900px;font-size:19px;line-height:27px;color:#F0EDE4">A fixture filing is recorded where mortgages are recorded.</div>'
          '<div class="abs" style="left:22px;top:94px;width:900px;font-size:17px;line-height:24px;color:#A5B2C3">It does not perfect an interest in goods that are not fixtures.</div></div>')
    b += panel(722, 100, "SEARCH BOTH", "A mortgage alone may not cover<br>personal property. Rules vary by state.", 480, 28)
    foot = ("Sources: Cornell LII, UCC 9-109, 9-501 and 9-102 (pages undated, accessed 2026-11-08); Violette Law Firm, Florida UCC Financing Statements (2025-12-18); "
            "Equipment Leasing and Finance Assoc., When Goods and Realty Collide (May/June 2022); Henson Efron (2018-09-18), which says membership interests are most commonly treated as general intangibles. Varies by state. Not legal advice.")
    return shell("A mortgage is not the whole", "collateral package.", "Different collateral is perfected in different places.", b, foot, 842)

PAGES = {"ucc-filings": ("images/2026-11-11/1709-li-ucc-filings.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
