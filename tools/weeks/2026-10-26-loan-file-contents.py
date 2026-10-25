#!/usr/bin/env python3
"""Graphic for loan file contents (Facebook, Sun Nov 1, 2026, 10:15 am ET). Run from repo root: python3 tools/weeks/2026-10-26-loan-file-contents.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render, CHK
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

COLS = [
    ("At closing", ["Signed note", "Deed of trust or mortgage", "Guaranty", "Business purpose certification", "Entity certificate"]),
    ("During the loan", ["Title insurance policy", "Insurance declarations page", "Most recent tax bill", "Borrower payment history"]),
    ("At payoff", ["Recordable lien release", "Original note returned", "Release may be delayed"]),
]

def gfx():
    b = ""
    w, step, top, h = 290, 327, 272, 430
    for i, (title, rows) in enumerate(COLS):
        x = 68 + i * step
        b += (f'<div class="card" style="left:{x}px;top:{top}px;width:{w}px;height:{h}px">'
              f'<div class="abs lbl" style="left:22px;top:22px">{title}</div>')
        for j, r in enumerate(rows):
            y = 70 + j * 68
            b += (f'<div class="abs" style="left:22px;top:{y}px">{CHK}</div>'
                  f'<div class="abs" style="left:60px;top:{y - 2}px;width:{w - 80}px;font-size:18px;line-height:23px;color:#F0EDE4">{r}</div>')
        b += '</div>'
    b += panel(734, 92, "ONE FILE", "Lenders can check each stage against their own list. Requirements vary by lender and state.", 560, 28)
    foot = ("Sources: Fortra Law, The Essential Loan Documents Checklist for Lenders (Feb 16, 2024); Superior Loan Servicing, Servicing File Content "
            "Requirements (page undated, accessed 2026-10-25); FDIC, Obtaining a Lien Release (page undated, accessed 2026-10-25); "
            "CFPB, lien release FAQ (Sep 13, 2024). General education, not legal advice.")
    return shell("What belongs in the file,", "closing through payoff?",
                 "A checklist drawn from lender and servicer guides.", b, foot, 852)

PAGES = {"loan-file-contents": ("images/2026-11-01/1015-fb-loan-file-contents.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
