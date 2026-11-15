#!/usr/bin/env python3
"""Graphic for catastrophe exposure. Run from repo root: python3 tools/weeks/2026-11-16-catastrophe-exposure.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

N, EXP, BAL = 20, 8, 300000

def gfx():
    tot, ex = N * BAL, EXP * BAL
    assert tot == 6000000 and ex == 2400000 and round(100 * ex / tot) == 40
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative book: 20 loans of $300,000</div>'
    x0, y0, s, g = 68, 326, 66, 12
    for i in range(N):
        r, c = divmod(i, 5)
        hot = i < EXP
        col = "#C9A84C" if hot else "#5B7DAE"
        tc = "#0B1F3A" if hot else "#FFFFFF"
        body += (f'<div class="abs mono" style="left:{x0 + c * (s + g)}px;top:{y0 + r * (s + g)}px;width:{s}px;height:{s}px;border-radius:10px;background:{col};color:{tc};'
                 f'display:flex;align-items:center;justify-content:center;font-size:20px">{i + 1}</div>')
    body += ('<div class="abs steel" style="left:68px;top:644px;font-size:17px;width:390px;line-height:24px">Gold: 8 loans in one county. Blue: 12 elsewhere.</div>')
    body += ('<div class="card" style="left:500px;top:326px;width:512px;height:130px"><div class="abs mono gold" style="left:22px;top:18px;font-size:40px">$2,400,000</div>'
             '<div class="abs" style="left:22px;top:78px;width:468px;font-size:19px;line-height:25px;font-weight:700">of $6,000,000, or 40 percent of the book</div></div>')
    body += ('<div class="card" style="left:500px;top:476px;width:512px;height:150px"><div class="abs lbl" style="left:22px;top:18px">Check 1: the map</div>'
             '<div class="abs" style="left:22px;top:48px;width:468px;font-size:18px;line-height:25px">High-risk flood areas begin with the letters A or V on FEMA flood maps and are called special flood hazard areas.</div></div>')
    body += ('<div class="card" style="left:500px;top:646px;width:512px;height:150px"><div class="abs lbl" style="left:22px;top:18px">Check 2: the coverage</div>'
             '<div class="abs" style="left:22px;top:48px;width:468px;font-size:18px;line-height:25px">Homeowners policies typically do not cover flood. NFIP policies generally have a 30-day wait.</div></div>')
    body += ('<div class="panel" style="top:704px;height:92px;width:400px"><div class="abs" style="left:22px;top:0;height:100%;width:360px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">'
             'Rules for private loans vary by lender. Confirm before closing.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "One storm, many loans:", "know your flood exposure",
                "Map every loan, then confirm flood coverage", body,
                "Sources: FEMA FloodSmart, What Is My Flood Risk (page undated, accessed 2026-11-15); FEMA FloodSmart agents, Flood Insurance 101 (page undated, accessed 2026-11-15); FDIC Consumer Compliance Manual V-6, last updated November 2023. "
                "Arithmetic: 20 x $300,000 = $6,000,000; 8 x $300,000 = $2,400,000; 2,400,000 / 6,000,000 = 40 percent. Book illustrative.", 850)

PAGES = {"catastrophe-exposure": ("images/2026-11-17/1021-li-catastrophe-exposure.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
