#!/usr/bin/env python3
"""Graphic for FEMA disaster declarations (Facebook, Sun Oct 25, 2026 10:15 am ET). Built Oct 18, 2026.
Run from repo root: python3 tools/weeks/2026-10-19-fema-disaster-declarations.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    d2026, avg = 133, 125
    assert d2026 - avg == 8
    scale = 560 / d2026
    b = '<div class="abs lbl" style="left:68px;top:272px">Federal disasters declared, USAFacts</div>'
    rows = [("2026, Jan to Sept", d2026, "seg-gold", 316), ("Yearly average, 2021 to 2025", avg, "seg-blue", 388)]
    for lab, v, cls, y in rows:
        w = round(v * scale)
        b += f'<div class="abs steel" style="left:68px;top:{y}px;width:250px;font-size:18px;line-height:24px;font-weight:700;color:#F0EDE4;padding-top:20px">{lab}</div>'
        b += f'<div class="abs {cls}" style="left:330px;top:{y}px;width:{w}px;height:64px;border-radius:8px"></div>'
        b += f'<div class="abs mono gold" style="left:{330 + w + 16}px;top:{y + 12}px;font-size:34px">{v}</div>'
    b += step_cards([
        (1, "Find the county", "Is it named in a recent declaration?", "county list"),
        (2, "Check the flood zone", "Confirm the map status.", "flood map"),
        (3, "Confirm insurance", "Ask what coverage is in force.", "policy"),
    ], top=500, h=190)
    b += panel(722, 92, "COUNTY, NOT STATE", "A declaration names counties. Being listed is a reason to ask, not proof of damage.", 520, 24)
    foot = ("Sources: USAFacts, updated Oct. 13, 2026 (133 so far in 2026, as of September; 125 average per year). "
            "FEMA OpenFEMA Disaster Declarations Summaries (county field; page undated, accessed Oct. 18, 2026). "
            "FEMA, How do I know if my area is eligible (page undated, accessed Oct. 18, 2026).")
    return shell("Disaster declarations list counties.", "Check the property's.",
                 "133 declared in 2026 through September", b, foot, 850,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"fema-disaster-declarations": ("images/2026-10-25/1015-fb-fema-disaster-declarations.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
