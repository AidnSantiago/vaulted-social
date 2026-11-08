#!/usr/bin/env python3
"""Graphic for bls-residential-construction-jobs-oct-2026 (Facebook, Wed Nov 11, 2026 8:56 am ET). Run from repo root: python3 tools/weeks/2026-11-09-bls-residential-construction-jobs-oct-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SPEC, BLDG = 15200, 1200
assert SPEC + BLDG == 16400

def gfx():
    b = stat_card(68, 262, 300, 152, "-16,400", "residential jobs, Oct", "Largest monthly drop since Mar 2021", 40)
    b += stat_card(390, 262, 300, 152, "-40,200", "net, last 12 months", "Residential construction", 40)
    b += stat_card(712, 262, 300, 152, "-3,000", "all construction, Oct", "Overall sector, per BLS", 40)
    b += '<div class="abs lbl" style="left:68px;top:450px">Where the October loss came from (jobs)</div>'
    rows = [("Residential specialty", "trade contractors", SPEC, "seg-gold", "-15,200"),
            ("Residential building", "builders and remodelers", BLDG, "seg-blue2", "-1,200")]
    y = 492
    for n1, n2, v, cls, lab in rows:
        w = max(int(v / 16400 * 520), 8)
        b += (f'<div class="abs" style="left:68px;top:{y}px;font-size:19px;font-weight:700;color:#F0EDE4;white-space:nowrap">{n1}</div>'
              f'<div class="abs" style="left:68px;top:{y+24}px;font-size:15px;color:#8A9BB0;white-space:nowrap">{n2}</div>')
        b += f'<div class="abs {cls}" style="left:330px;top:{y+2}px;width:{w}px;height:44px;border-radius:6px"></div>'
        b += f'<div class="abs mono gold" style="left:{330+w+14}px;top:{y+11}px;font-size:21px;white-space:nowrap">{lab}</div>'
        y += 76
    b += ('<div class="abs" style="left:68px;top:652px;width:944px;font-size:17px;line-height:24px;color:#A5B2C3">'
          'Residential construction employs about 3.3 million people. One month is not a trend.</div>')
    b += panel(704, 118, "crews = schedule", "Trade labor can affect how fast rehab work and draws move. Lenders can ask each contractor about crew availability.", 470, 26)
    foot = ("Sources: NAHB Eye On Housing, Jing Fu (Nov 6, 2026), analysis of BLS data; ENR (Nov 6, 2026); "
            "BLS Employment Situation, Oct 2026 (released Nov 6, 2026). Arithmetic: 15,200 + 1,200 = 16,400.")
    return shell("Residential construction", "shed 16,400 jobs in October", "Monthly change in employment, October 2026", b, foot, 856, eyebrow="LABOR SUPPLY FOR REHAB LENDERS")

PAGES = {"bls-residential-construction-jobs-oct-2026": ("images/2026-11-11/0856-fb-bls-residential-construction-jobs-oct-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
