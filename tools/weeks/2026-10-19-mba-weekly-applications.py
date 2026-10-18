#!/usr/bin/env python3
"""Graphic for MBA weekly applications survey, week ending Oct 9, 2026 (Facebook, Mon Oct 19, 2026 8:42 am ET). Built Oct 18, 2026.
Run from repo root: python3 tools/weeks/2026-10-19-mba-weekly-applications.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    now = round(100 * (1 - 0.56))
    assert now == 44
    b = stat_card(68, 268, 290, 150, "7.5%", "30-year fixed rate", "highest since November 2023", 46)
    b += stat_card(395, 268, 290, 150, "37.7%", "refinance share of apps", "up from 37.0% the week before", 46)
    b += stat_card(722, 268, 290, 150, "-4%", "Purchase Index", "change from one week earlier", 46)
    b += '<div class="abs lbl" style="left:68px;top:452px">Refinance Index, same week one year ago = 100</div>'
    X0, S, H = 300, 6.6, 58
    rows = [("A year ago", 100, "seg-blue"), ("Week of Oct 9, 2026", now, "seg-gold")]
    y = 496
    for lab, v, cls in rows:
        b += (f'<div class="abs" style="left:68px;top:{y}px;width:220px;height:{H}px;display:flex;align-items:center;font-size:19px;line-height:23px;font-weight:700">{lab}</div>')
        b += (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{v*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:22px">{v}</div>')
        y += H + 24
    b += '<div class="abs" style="left:300px;top:670px;font-size:15px;color:#8A9BB0">56 percent lower than a year earlier leaves the index at 44 on this scale</div>'
    b += panel(730, 96, "STRESS THE EXIT", "Lenders can ask what a refinance payoff looks like at rates near 7.5%.", 600, 24)
    foot = ("Source: Mortgage Bankers Association, Weekly Mortgage Applications Survey, week ending Oct 9, 2026 (released Oct 14, 2026); "
            "HousingWire, Oct 14, 2026. Rates are as of that week. Arithmetic: 100 x (1 - 0.56) = 44. Not private loan data.")
    return shell("Refinance demand is 56 percent", "below a year ago.",
                 "MBA weekly applications, week ending October 9, 2026", b, foot, 862,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"mba-weekly-applications": ("images/2026-10-19/0842-fb-mba-weekly-applications.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
