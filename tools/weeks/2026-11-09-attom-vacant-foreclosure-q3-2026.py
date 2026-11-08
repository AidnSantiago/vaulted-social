#!/usr/bin/env python3
"""Graphic for ATTOM Q3 2026 vacant property and zombie foreclosure report.
Run from repo root: python3 tools/weeks/2026-11-09-attom-vacant-foreclosure-q3-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert round(8482 / 259666 * 100, 1) == 3.3
    b = stat_card(68, 262, 460, 150, "259,666", "Residential properties in foreclosure", "ATTOM Q3 2026 report", 46)
    b += stat_card(552, 262, 460, 150, "8,482", "Were zombies, about 3.3%", "Owner abandoned before foreclosure ended", 46)
    b += '<div class="abs lbl" style="left:68px;top:432px">Share of residential properties vacant, ATTOM Q3 2026 report</div>'
    scale = 944 - 330  # px for 3.0 percent
    rows = [("New Hampshire", 0.3, "seg-steel"), ("U.S. overall", 1.3, "seg-gold"), ("Oklahoma, Kansas", 2.4, "seg-blue2")]
    for i, (name, v, cls) in enumerate(rows):
        y = 470 + i * 70
        w = int(v / 3.0 * scale)
        b += f'<div class="abs" style="left:68px;top:{y}px;width:200px;height:50px;display:flex;align-items:center;font-size:20px;font-weight:700">{name}</div>'
        b += f'<div class="abs {cls}" style="left:280px;top:{y}px;width:{w}px;height:50px;border-radius:8px"></div>'
        b += f'<div class="abs mono gold" style="left:{280 + w + 14}px;top:{y}px;height:50px;display:flex;align-items:center;font-size:22px">{v}%</div>'
    b += panel(702, 110, "Check the asset", "Lenders can ask who maintains an empty property and what its insurance requires.", 430, 26)
    foot = ("Source: ATTOM, Vacant Property and Zombie Foreclosure Report, National Vacancy Rate Doesn't Budge in Third Quarter (published Aug 27, 2026; "
            "dateline Aug 28, 2026). National and state figures; local markets vary. Arithmetic: 8,482 / 259,666 = 3.3%.")
    return shell("1.3% of homes were vacant,", "3.3% of foreclosures were zombies",
                 "ATTOM Q3 2026 Vacant Property and Zombie Foreclosure Report", b, foot, 850, eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"attom-vacant-foreclosure-q3-2026": ("images/2026-11-13/0800-fb-attom-vacant-foreclosure-q3-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
