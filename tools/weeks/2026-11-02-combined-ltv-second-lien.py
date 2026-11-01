#!/usr/bin/env python3
"""Graphic for combined LTV with a second lien. Run from repo root: python3 tools/weeks/2026-11-02-combined-ltv-second-lien.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def seg(x, w, cls, big, small):
    return (f'<div class="abs {cls}" style="left:{x}px;top:318px;width:{w}px;height:96px;border-radius:10px">'
            f'<div class="abs mono" style="left:0;top:16px;width:{w}px;text-align:center;font-size:24px">{big}</div>'
            f'<div class="abs" style="left:0;top:56px;width:{w}px;text-align:center;font-size:15px;font-weight:700">{small}</div></div>')

def gfx():
    W = 944
    w1, w2 = 566, 132           # 60% and 14% of 944, rounded
    w3 = W - w1 - w2 - 8        # remaining equity, two 4px gaps
    b = '<div class="abs lbl" style="left:68px;top:276px">Property value $450,000</div>'
    b += seg(68, w1, "seg-blue", "$270,000", "First lien")
    b += seg(68 + w1 + 4, w2, "seg-gold", "$63,000", "Second")
    b += seg(68 + w1 + w2 + 8, w3, "seg-steel", "$117,000", "Left over")
    b += '<div class="abs steel" style="left:68px;top:424px;font-size:16px">Left over = $450,000 - $270,000 - $63,000, before any costs.</div>'
    y, h, w = 472, 168, 296
    b += stat_card(68, y, w, h, "60%", "First lien alone", "$270,000 / $450,000")
    b += stat_card(68 + 324, y, w, h, "74%", "Combined LTV", "($270,000 + $63,000) / $450,000")
    b += stat_card(68 + 648, y, w, h, "82.2%", "If value drops 10%", "$333,000 / $405,000")
    b += panel(664, 96, "ADD EVERY LIEN", "Lenders can compute combined LTV before funding and again if value changes.", 470)
    foot = ("Sources: Experian, What Is Combined Loan-to-Value Ratio? (Jan 15, 2024); Bankrate, Combined loan-to-value ratio "
            "(Jul 31, 2026). Illustrative: $450,000 value, $270,000 first, $63,000 second. Arithmetic: 270,000 / 450,000 = 60%; "
            "333,000 / 450,000 = 74%; 450,000 x 0.90 = 405,000; 333,000 / 405,000 = 82.2%. Not legal advice.")
    return shell("Add every lien,", "then divide by value.", "How a $63,000 second lien changes a 60% LTV loan.", b, foot, 784)

PAGES = {"combined-ltv-second-lien": ("images/2026-11-03/1247-fb-combined-ltv-second-lien.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
