#!/usr/bin/env python3
"""Graphic for Fed SLOOS April 2026 (Q1), construction and land development standards and demand (LinkedIn, Mon Nov 2, 2026 11:34 am ET).
October 2026 survey not yet out on Nov 1, so the latest differing survey (April 2026) is used. Run from repo root: python3 tools/weeks/2026-11-02-sloos-oct-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

W = 944  # bar width px for 100 percent
def bar(y, title, sub, segs):
    # segs: (label, count, pct, css, text color)
    b = (f'<div class="abs" style="left:68px;top:{y}px;font-size:23px;font-weight:700">{title}</div>'
         f'<div class="abs" style="left:68px;top:{y+31}px;font-size:16px;color:#8A9BB0">{sub}</div>')
    x = 68.0
    by = y + 64
    for lab, cnt, pct, cls in segs:
        w = W * pct / 100.0
        inner = f'{pct}%' if w > 100 else ''
        b += (f'<div class="abs {cls} mono" style="left:{x:.1f}px;top:{by}px;width:{w-3:.1f}px;height:64px;border-radius:6px;'
              f'display:flex;align-items:center;justify-content:center;font-size:20px">{inner}</div>')
        x += w
    return b

def legend(y, items):
    b = ""; x = 68
    for lab, cls, w in items:
        b += (f'<div class="abs {cls}" style="left:{x}px;top:{y+4}px;width:16px;height:16px;border-radius:3px"></div>'
              f'<div class="abs" style="left:{x+24}px;top:{y}px;font-size:16px;color:#A5B2C3;white-space:nowrap">{lab}</div>')
        x += w
    return b

def gfx():
    b = bar(262, "Standards for construction and land loans", "61 banks, first quarter 2026, share of banks",
            [("Tightened", 8, 13.1, "seg-blue"), ("Unchanged", 48, 78.7, "seg-steel"), ("Eased", 5, 8.2, "seg-gold")])
    b += legend(396, [("Tightened somewhat 13.1%", "seg-blue", 250), ("Basically unchanged 78.7%", "seg-steel", 270), ("Eased somewhat 8.2%", "seg-gold", 240)])
    b += bar(466, "Demand for construction and land loans", "60 banks, first quarter 2026, share of banks",
             [("Weaker", 13, 21.7, "seg-blue"), ("Same", 41, 68.3, "seg-steel"), ("Stronger", 6, 10.0, "seg-gold")])
    b += legend(600, [("Weaker 21.7%", "seg-blue", 200), ("About the same 68.3%", "seg-steel", 260), ("Stronger, 6 banks", "seg-gold", 240)])
    b += panel(664, 120, "MOSTLY STEADY", "Standards held for most banks. Weaker demand outnumbered stronger demand.", 520, 26)
    foot = ("Source: Federal Reserve Board, April 2026 Senior Loan Officer Opinion Survey, Table 1, released May 4, 2026; first quarter 2026. "
            "Arithmetic: weaker demand = 12 moderately + 1 substantially = 13 of 60 = 21.7%. Stronger = 6 of 60.")
    return shell("Banks held construction", "standards. Demand softened.",
                 "Fed loan officer survey, first quarter 2026", b, foot, 830,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"sloos-oct-2026": ("images/2026-11-02/1134-li-sloos-oct-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
