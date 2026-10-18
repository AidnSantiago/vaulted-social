#!/usr/bin/env python3
"""Graphic for construction-employment (Facebook, Thu Oct 22, 2026 8:25 am ET). Run from repo root: python3 tools/weeks/2026-10-19-construction-employment.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BARS = [("August 2025", 213, "2.5%", "seg-steel"),
        ("July 2026", 299, "3.5%", "seg-blue2"),
        ("August 2026 (preliminary)", 251, "2.9%", "seg-gold")]
MAXV = 300.0
BARW = 430

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">Construction job openings, thousands (rate)</div>'
    for i, (name, v, rate, cls) in enumerate(BARS):
        y = 306 + i * 62
        w = round(BARW * v / MAXV)
        b += (f'<div class="abs" style="left:68px;top:{y}px;width:290px;height:48px;display:flex;align-items:center;font-size:18px;line-height:22px;font-weight:700;color:#F0EDE4">{name}</div>'
              f'<div class="abs {cls}" style="left:370px;top:{y+6}px;width:{w}px;height:36px;border-radius:6px"></div>'
              f'<div class="abs mono gold" style="left:{370+w+12}px;top:{y+8}px;font-size:22px;line-height:32px">{v}K ({rate})</div>')
    b += stat_card(68, 520, 460, 150, "+11,000", "construction jobs, September 2026", "BLS Employment Situation")
    b += stat_card(552, 520, 460, 150, "+10,000", "average per month, prior 12 months", "BLS Employment Situation")
    b += panel(698, 120, "ASK FIRST", "Lenders can ask when a crew can actually start and how many jobs the contractor is running now.", 600, 30)
    foot = ("Sources: BLS, The Employment Situation - September 2026 (released Oct 2, 2026). BLS, Job Openings and Labor Turnover Survey, August 2026 "
            "(Table 1, last modified Sept 29, 2026; August figures preliminary). National figures; local markets vary.")
    return shell("Construction job growth is small,", "so ask about start dates.", "Construction jobs and openings, latest BLS data",
                 b, foot, 860)

PAGES = {"construction-employment": ("images/2026-10-22/0825-fb-construction-employment.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
