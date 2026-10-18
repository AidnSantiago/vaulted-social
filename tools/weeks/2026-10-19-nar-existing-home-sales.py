#!/usr/bin/env python3
"""Graphic for NAR existing-home sales, September 2026 data (Facebook, Wed Oct 21, 2026 8:56 am ET). Built Oct 18, 2026.
Run from repo root: python3 tools/weeks/2026-10-19-nar-existing-home-sales.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert 60 - 33 == 27 and 27 * 70 == 1890
    b = stat_card(68, 268, 290, 150, "3.99M", "annual sales pace", "seasonally adjusted rate")
    b += stat_card(395, 268, 290, 150, "4.8 mo", "months of supply", "up from 4.5 a year earlier", 40)
    b += stat_card(722, 268, 290, 150, "$417,500", "median price", "up 1.3% from a year ago", 38)
    b += '<div class="abs lbl" style="left:68px;top:452px">Days on market: median vs an illustrative slow sale</div>'
    X0, S, H = 250, 11, 44   # px per day
    y = 492
    b += f'<div class="abs" style="left:68px;top:{y}px;height:{H}px;display:flex;align-items:center;font-size:19px;font-weight:700">Median</div>'
    b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:{y}px;width:{33*S}px;height:{H}px;border-radius:0 6px 6px 0;'
          f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:19px">33 days</div>')
    y += H + 20
    b += f'<div class="abs" style="left:68px;top:{y}px;height:{H}px;display:flex;align-items:center;font-size:19px;font-weight:700">Slow sale</div>'
    b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:{y}px;width:{33*S}px;height:{H}px;border-radius:0;'
          f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:19px">33</div>')
    b += (f'<div class="abs seg-gold mono" style="left:{X0+33*S}px;top:{y}px;width:{27*S}px;height:{H}px;border-radius:0 6px 6px 0;'
          f'display:flex;align-items:center;justify-content:center;font-size:19px">+27 = 60 days</div>')
    b += ('<div class="abs" style="left:68px;top:630px;width:944px;font-size:18px;line-height:26px;color:#A5B2C3">'
          'NAR reports 1.60 million unsold homes. The 60-day sale is an illustrative example, not a market figure.</div>')
    b += '<div class="abs lbl" style="left:68px;top:704px">Why it matters at exit</div>'
    b += panel(738, 84, "27 DAYS = $1,890", "Illustrative: at $70 a day in interest, taxes and insurance, 27 extra days costs $1,890.", 470, 24)
    foot = ("Source: National Association of REALTORS, Existing-Home Sales, September 2026 data (released Oct 13, 2026). "
            "Arithmetic: 60 - 33 = 27 days; 27 x $70 = $1,890. The $70 a day and 60 days are illustrative. National figures; local markets vary.")
    return shell("Median sale took 33 days in September", "Plan your exit around it.",
                 "NAR existing-home sales, September 2026 data", b, foot, 856,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"nar-existing-home-sales": ("images/2026-10-21/0856-fb-nar-existing-home-sales.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
