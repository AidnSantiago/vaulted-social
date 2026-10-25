#!/usr/bin/env python3
"""Graphic for final-draw-conditions (Facebook, Fri Oct 30, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-10-26-final-draw-conditions.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render, CHK
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, title, who, items):
    w, y0 = 462, 262
    s = f'<div class="card" style="left:{x}px;top:{y0}px;width:{w}px;height:430px"></div>'
    s += f'<div class="abs lbl" style="left:{x+24}px;top:{y0+22}px">{title}</div>'
    s += f'<div class="abs steel" style="left:{x+24}px;top:{y0+48}px;font-size:16px;white-space:nowrap">{who}</div>'
    for i, (txt, both) in enumerate(items):
        y = y0 + 100 + i * 100
        bg = 'background:rgba(201,168,76,.10);border:1px solid rgba(201,168,76,.45);' if both else 'border:1px solid rgba(138,155,176,.25);'
        col_ = '#E2C265' if both else '#F0EDE4'
        s += f'<div class="abs" style="left:{x+18}px;top:{y}px;width:{w-36}px;height:84px;border-radius:10px;{bg}"></div>'
        s += f'<div class="abs" style="left:{x+32}px;top:{y+29}px">{CHK}</div>'
        s += f'<div class="abs" style="left:{x+72}px;top:{y+12}px;width:{w-110}px;height:60px;display:flex;align-items:center;font-size:19px;line-height:24px;font-weight:700;color:{col_}">{txt}</div>'
    return s

def gfx():
    b = col(68, "Hard money guide", "Lendmire, last draw", [
        ("Final inspection", False),
        ("Certificate of occupancy", True),
        ("A final lien waiver", True)])
    b += col(550, "Commercial guide", "Terrapin, final funds", [
        ("Certificate of occupancy", True),
        ("Final unconditional lien waivers from all tiers", True),
        ("Final title endorsement, no open liens", False)])
    b += panel(716, 110, "GOLD = IN BOTH", "Lenders can share the final draw list with the borrower early. Requirements vary by lender, loan and state.", 470, 26)
    foot = ("Sources: Lendmire, How ADU Builders Draw Funds on a Hard Money Construction Loan (Oct 23, 2026): the last draw \"usually requires\" these items. "
            "Terrapin Capital Group, Commercial Construction Loan Draw Schedule 2026 (Apr 24, 2026): items a lender verifies before final funds release.")
    return shell("What a final draw", "can wait on", "Two lender guides, side by side", b, foot, 850)

PAGES = {"final-draw-conditions": ("images/2026-10-30/1727-fb-final-draw-conditions.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
