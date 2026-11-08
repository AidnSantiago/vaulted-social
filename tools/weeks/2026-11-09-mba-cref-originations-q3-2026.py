#!/usr/bin/env python3
"""Graphic for MBA commercial/multifamily originations, Q2 2026 (latest release; Q3 2026 not yet published).
Run from repo root: python3 tools/weeks/2026-11-09-mba-cref-originations-q3-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ROWS = [("CMBS", 68), ("Depositories", 61), ("Investor-driven lenders", 18), ("GSEs", -17), ("Life insurance companies", -27)]

def gfx():
    b = stat_card(68, 262, 460, 152, "+16%", "Versus a year earlier", "Second quarter 2026 vs second quarter 2025", 46)
    b += stat_card(552, 262, 460, 152, "+12%", "Versus the prior quarter", "Second quarter 2026 vs first quarter 2026", 46)
    b += '<div class="abs lbl" style="left:68px;top:442px">Change in loans by lender type, year over year</div>'
    zero = 560; scale = 3.3
    top = 480
    for i, (n, v) in enumerate(ROWS):
        y = top + i * 56
        w = abs(v) * scale
        cls = "seg-gold" if v > 0 else "seg-steel"
        left = zero if v > 0 else zero - w
        b += f'<div class="abs" style="left:68px;top:{y+9}px;width:{zero-68-8-(0 if v>0 else 0)}px;font-size:17px;color:#A5B2C3;white-space:nowrap">{n}</div>' if v > 0 else \
             f'<div class="abs" style="left:68px;top:{y+9}px;font-size:17px;color:#A5B2C3;white-space:nowrap">{n}</div>'
        b += f'<div class="abs {cls}" style="left:{left}px;top:{y}px;width:{w}px;height:40px;border-radius:6px"></div>'
        lab = f"{'+' if v>0 else '-'}{abs(v)}%"
        lx = zero + w + 12 if v > 0 else zero + 12
        b += f'<div class="abs mono gold" style="left:{lx}px;top:{y+8}px;font-size:19px">{lab}</div>'
    b += f'<div class="abs" style="left:{zero}px;top:{top-4}px;width:2px;height:{5*56-8}px;background:#8A9BB0"></div>'
    b += panel(778, 84, "Latest MBA release", "A market read for pricing context, not a forecast.", 430, 24)
    foot = ("Source: Mortgage Bankers Association, Quarterly Survey of Commercial/Multifamily Mortgage Bankers Originations, second quarter 2026 (Aug 6, 2026); "
            "PDF undated, accessed Nov 8, 2026. Q3 2026 not yet published.")
    return shell("Commercial lending is up 16%", "from a year earlier",
                 "MBA originations, second quarter 2026, the latest release", b, foot, 886, eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"mba-cref-originations-q3-2026": ("images/2026-11-10/1021-li-mba-cref-originations-q3-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
