#!/usr/bin/env python3
"""Graphic for draw-photo-documentation (Facebook, Fri Nov 13, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-draw-photo-documentation.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ITEMS = [
    ("Dated and geotagged", "A timestamp and location tag make the record traceable."),
    ("Wide first, then close", "Show the area, then the detail up close."),
    ("Same spot, same angle", "Repeat the view so progress is obvious."),
    ("In focus", "Blurry or small photos may bring an inspector back."),
]

def row(y, i, t, d):
    return (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:112px">'
            f'<div class="num" style="top:38px">{i}</div>'
            f'<div class="abs" style="left:82px;top:20px;font-size:26px;font-weight:700;color:#F0EDE4">{t}</div>'
            f'<div class="abs" style="left:82px;top:60px;width:840px;font-size:19px;line-height:26px;color:#A5B2C3">{d}</div></div>')

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">Four checks on a progress photo</div>'
    for k, (t, d) in enumerate(ITEMS):
        b += row(296 + k * 126, k + 1, t, d)
    b += panel(812, 80, "Ask first", "What photos a lender accepts varies by lender.", 480, 28)
    foot = ("Sources: CompanyCam, Construction Photo Documentation (Feb 17, 2026); Projul, Construction Progress Photos Best Practices "
            "(Aug 13, 2025); Trinity, Three Critical Factors of a Draw Inspection (Aug 9, 2021).")
    return shell("What photos can back up", "a draw request?", "A checklist lenders can share with borrowers", b, foot, 912, eyebrow="DRAW DOCUMENTATION, EXPLAINED")

PAGES = {"draw-photo-documentation": ("images/2026-11-13/1727-fb-draw-photo-documentation.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
