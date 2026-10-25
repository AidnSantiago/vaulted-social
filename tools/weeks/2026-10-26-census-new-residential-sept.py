#!/usr/bin/env python3
"""Graphic for Census new residential construction, September 2026 data (Facebook, Wed Oct 28, 2026 8:56 am ET).
Run from repo root: python3 tools/weeks/2026-10-26-census-new-residential-sept.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert round((1 - 859/900) * 100, 1) == 4.6 and round((1 - 845/880) * 100, 1) == 4.0
    b = '<div class="abs lbl" style="left:68px;top:262px">Single-family, seasonally adjusted annual rate</div>'
    rows = [("Starts", 900, 859, "4.6% lower"), ("Permits", 880, 845, "4.0% lower")]
    X0, S, H = 210, 0.78, 38   # px per thousand
    y = 304
    for name, aug, sep, chg in rows:
        b += f'<div class="abs" style="left:68px;top:{y}px;height:{H}px;display:flex;align-items:center;font-size:19px;font-weight:700">{name}</div>'
        b += (f'<div class="abs seg-steel mono" style="left:{X0}px;top:{y}px;width:{aug*S:.0f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:17px">Aug {aug},000</div>')
        y += H + 8
        b += (f'<div class="abs seg-gold mono" style="left:{X0}px;top:{y}px;width:{sep*S:.0f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:17px">Sep {sep},000</div>')
        b += f'<div class="abs mono gold" style="left:{X0+int(aug*S)+14}px;top:{y-24}px;font-size:17px;white-space:nowrap">{chg}</div>' if False else ''
        y += H + 26
    b += stat_card(68, 584, 290, 150, "840,000", "completions", "single-family, September")
    b += stat_card(395, 584, 290, 150, "+/-10.0%", "starts margin", "range on the 4.6% change", 40)
    b += stat_card(722, 584, 290, 150, "4.6%", "starts below Aug", "Aug revised to 900,000", 46)
    b += panel(764, 92, "ONE MONTH", "The starts change could be zero within its range. Watch several releases.", 560, 26)
    foot = ("Source: U.S. Census Bureau and HUD, New Residential Construction, September 2026 (released Oct 20, 2026). "
            "Arithmetic: (1 - 859/900) = 4.6% lower; (1 - 845/880) = 4.0% lower. National figures; local markets vary.")
    return shell("Single-family starts fell to 859,000", "Permits slipped to 845,000.",
                 "Census/HUD new residential construction, September 2026", b, foot, 896,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"census-new-residential-sept": ("images/2026-10-28/0856-fb-census-new-residential-sept.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
