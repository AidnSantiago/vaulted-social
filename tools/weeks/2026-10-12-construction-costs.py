#!/usr/bin/env python3
"""Graphic for construction cost inputs. Run from repo root: python3 tools/weeks/2026-10-12-construction-costs.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BID = 68000                      # illustrative
IDX = 10.5
UP = round(BID * IDX / 100)      # 7140
NEW = BID + UP                   # 75140

BARS = [("Residential maintenance and repair inputs", 10.5, "seg-gold"),
        ("Lumber and plywood", 9.6, "seg-blue2"),
        ("Concrete products", 4.2, "seg-blue"),
        ("Steel mill products", 27.6, "seg-steel")]
MAXV = 30.0
BARW = 520

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">Producer price index, change Sept 2025 to Sept 2026</div>'
    for i, (name, v, cls) in enumerate(BARS):
        y = 306 + i * 62
        w = round(BARW * v / MAXV)
        b += (f'<div class="abs" style="left:68px;top:{y}px;width:300px;height:48px;display:flex;align-items:center;font-size:18px;line-height:22px;font-weight:700;color:#F0EDE4">{name}</div>'
              f'<div class="abs {cls}" style="left:380px;top:{y+6}px;width:{w}px;height:36px;border-radius:6px"></div>'
              f'<div class="abs mono gold" style="left:{380+w+12}px;top:{y+8}px;font-size:22px;line-height:32px">+{v}%</div>')
    b += stat_card(68, 568, 300, 150, f"${BID:,}", "illustrative bid", "priced a year ago")
    b += stat_card(390, 568, 300, 150, f"+${UP:,}", "if every dollar rose 10.5%", f"${BID:,} &times; 10.5%")
    b += stat_card(712, 568, 300, 150, f"${NEW:,}", "ceiling, not a forecast", "not every dollar is materials", big_size=42)
    b += panel(742, 100, "CHECK THE BID DATE", "Lenders can ask when each contractor bid was priced and whether those prices are still held.", 470, 24)
    foot = ("Source: AGC, PPI Tables (BLS data compiled by Ken Simonson), updated Oct 15, 2026; figures are national, local costs vary. "
            f"Bid is illustrative. Arithmetic: ${BID:,} &times; 10.5% = ${UP:,}; ${BID:,} + ${UP:,} = ${NEW:,}.")
    return shell("Rehab bids from last year", "may be out of date.", "Construction input prices as of September 2026",
                 b, foot, 870)

PAGES = {"construction-costs": ("images/2026-10-18/1015-fb-construction-costs.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
