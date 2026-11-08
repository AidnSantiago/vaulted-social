#!/usr/bin/env python3
"""Graphic for ICE First Look, September 2026 (MBA Q3 2026 NDS not yet released). Run from repo root: python3 tools/weeks/2026-11-09-ice-first-look-sep-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def bar(y, pct, label):
    x0, w = 68, 944
    fill = w * pct / 100
    s = f'<div class="abs" style="left:{x0}px;top:{y}px;font-size:18px;color:#A5B2C3;white-space:nowrap">{label}</div>'
    s += f'<div class="abs" style="left:{x0}px;top:{y+32}px;width:{w}px;height:44px;border-radius:8px;background:rgba(90,107,130,.30);border:1px solid rgba(138,155,176,.30)"></div>'
    s += f'<div class="abs seg-gold" style="left:{x0}px;top:{y+32}px;width:{fill}px;height:44px;border-radius:8px"></div>'
    s += f'<div class="abs mono" style="left:{x0+16}px;top:{y+43}px;font-size:21px;color:#0B1F3A">{pct}%</div>'
    return s

def gfx():
    b = stat_card(68, 262, 460, 152, "3.66%", "National delinquency rate", "September 2026, up 12 basis points from August", 46)
    b += stat_card(552, 262, 460, 152, "Early 2019", "Active foreclosure inventory", "Highest level since then", 46)
    b += '<div class="abs lbl" style="left:68px;top:444px">Share from loans originated in 2022 or later</div>'
    b += bar(476, 43, "Of September foreclosure starts")
    b += bar(578, 49, "Of completed foreclosure sales")
    b += panel(704, 96, "Newer loans", "All U.S. mortgages, not private loans. Lenders can review delinquencies by origination date.", 520, 26)
    foot = ("Source: ICE First Look at Mortgage Performance, September 2026 data (Oct 27, 2026); HousingWire (Oct 27, 2026); The MortgagePoint (Oct 28, 2026). "
            "Bars drawn to scale on a 0 to 100% track.")
    return shell("Loans from 2022 or later in the", "foreclosure pipeline",
                 "ICE First Look, September 2026 data, released October 27", b, foot, 842, eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"ice-first-look-sep-2026": ("images/2026-11-12/0825-fb-ice-first-look-sep-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
