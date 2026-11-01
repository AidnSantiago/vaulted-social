#!/usr/bin/env python3
"""Graphic for mortgage vs deed of trust (FB Fri Nov 6, 2026, 8:00 am ET). Comparison cards, no numbers beyond two/three parties.
Run from repo root: python3 tools/weeks/2026-11-02-mortgage-vs-deed-of-trust.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, title, big, parties, rows, accent):
    w = 452
    h = f'<div class="card" style="left:{x}px;top:272px;width:{w}px;height:350px">'
    h += f'<div class="abs lbl" style="left:24px;top:22px;color:{accent}">{title}</div>'
    h += f'<div class="abs mono gold" style="left:24px;top:52px;font-size:40px;line-height:48px;white-space:nowrap;color:{accent}">{big}</div>'
    h += f'<div class="abs" style="left:24px;top:108px;width:{w-48}px;font-size:18px;line-height:24px;color:#A5B2C3">{parties}</div>'
    y = 176
    for lab, txt in rows:
        h += f'<div class="abs lbl" style="left:24px;top:{y}px;font-size:13px;color:#8A9BB0">{lab}</div>'
        h += f'<div class="abs" style="left:24px;top:{y+22}px;width:{w-48}px;font-size:19px;line-height:25px;font-weight:700;color:#F0EDE4">{txt}</div>'
        y += 86
    return h + '</div>'

def gfx():
    b = col(68, "Mortgage", "Two parties", "Borrower and lender.",
            [("Foreclosure path", "Most often judicial: filed in a court"),
             ("Who acts", "The lender, through the court")], "#E2C265")
    b += col(560, "Deed of trust", "Three parties", "Borrower, lender and a trustee.",
             [("Foreclosure path", "Often nonjudicial: no court needed"),
              ("Who acts", "The trustee, under a power-of-sale clause")], "#8FB0E0")
    b += panel(662, 96, "Varies by state", "The state where the property sits decides which instrument is used and how it is enforced.", 520, 26)
    foot = ("Sources: Geraci LLP, Deed of Trust vs. Mortgage (published 2024-06-04); Chase, Deed of Trust vs Mortgage (published 2025-10-30); "
            "Nolo, What Is a Power of Sale Foreclosure? (page undated, accessed 2026-11-01). Educational only, not legal advice.")
    return shell("Same default.", "Different foreclosure path.",
                 "What the lender holds can change how the lender enforces it", b, foot, 790,
                 eyebrow="LOAN DOCUMENTS FOR PRIVATE LENDERS")

PAGES = {"mortgage-vs-deed-of-trust": ("images/2026-11-06/0800-fb-mortgage-vs-deed-of-trust.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
