#!/usr/bin/env python3
"""Graphic for capitalized interest and LTV (Facebook, Mon Nov 9, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-capitalized-interest-ltv.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, VAL, RATE = 280000, 400000, 0.11  # illustrative


def gfx():
    bals = [LOAN * (1 + RATE / 12) ** n for n in range(7)]
    assert round(bals[1]) == 282567 and round(bals[6]) == 295757
    assert round(bals[6] / VAL * 100, 1) == 73.9 and round(VAL - bals[6]) == 104243
    H, base, colw, gap = 230, 570, 112, 26  # bar area height for $400,000
    b = '<div class="abs lbl" style="left:68px;top:268px">Balance when each month of interest is capitalized</div>'
    b += f'<div class="abs mono steel" style="left:68px;top:{base - H - 26}px;font-size:14px;white-space:nowrap">Value $400,000</div>'
    b += f'<div class="abs" style="left:68px;top:{base - H}px;width:944px;border-top:1.5px dashed rgba(165,178,195,.5)"></div>'
    for n, bal in enumerate(bals):
        x = 68 + n * (colw + gap) + 8
        bh = bal / VAL * H
        cls = "seg-gold" if n == 6 else "seg-blue"
        b += (f'<div class="abs {cls}" style="left:{x}px;top:{base - bh:.1f}px;width:{colw - 16}px;height:{bh:.1f}px;border-radius:6px 6px 0 0"></div>')
        b += (f'<div class="abs mono" style="left:{x - 10}px;top:{base - bh + 12:.1f}px;width:{colw - 16 + 20}px;text-align:center;font-size:15px;color:{"#0B1F3A" if n == 6 else "#F0EDE4"}">${bal:,.0f}</div>')
        b += (f'<div class="abs mono {"gold" if n == 6 else "steel"}" style="left:{x - 10}px;top:{base + 8}px;width:{colw - 16 + 20}px;text-align:center;font-size:16px">{bal / VAL * 100:.1f}%</div>')
        b += (f'<div class="abs steel" style="left:{x - 10}px;top:{base + 32}px;width:{colw - 16 + 20}px;text-align:center;font-size:14px">{"Start" if n == 0 else "Month " + str(n)}</div>')
    b += stat_card(68, 654, 462, 150, "70.0% to 73.9%", "LTV after six months", "$280,000 to $295,757 on a $400,000 value", 38)
    b += stat_card(550, 654, 462, 150, "$15,757", "less equity cushion", "$120,000 to $104,243, no new money advanced", 46)
    b += panel(822, 70, "Balance / value", "Check LTV on the current balance.", 330, 25)
    foot = ("Sources: Consumer Financial Protection Bureau, Ask CFPB, page last modified May 28, 2024; Federal Student Aid, Financial Aid Dictionary, page undated, accessed 2026-11-08. "
            "Illustrative: $280,000 loan, $400,000 value held flat, 11% rate, interest capitalized monthly. "
            "Arithmetic: 280,000 x (1 + 0.11/12)^6 = 295,757; 295,757 / 400,000 = 73.9%; 400,000 - 295,757 = 104,243.")
    return shell("Unpaid interest does not vanish.", "It raises the balance.",
                 "Capitalized interest and LTV over six months &middot; illustrative", b, foot, 906)


PAGES = {"capitalized-interest-ltv": ("images/2026-11-09/1247-fb-capitalized-interest-ltv.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
