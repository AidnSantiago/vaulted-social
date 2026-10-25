#!/usr/bin/env python3
"""Graphic for Realtor.com September 2026 price cuts. Run from repo root: python3 tools/weeks/2026-10-26-realtor-inventory-price-cuts.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert round(285000 * 0.96) == 273600 and round(285000 * 0.04) == 11400
    b = stat_card(68, 268, 290, 150, "20.8%", "listings with a cut", "up 0.9 points from a year earlier")
    b += stat_card(395, 268, 290, 150, "+5.4%", "active inventory", "year over year", 46)
    b += stat_card(722, 268, 290, 150, "1.16M+", "active listings", "over 1,161,000 homes", 46)
    b += '<div class="abs lbl" style="left:68px;top:452px">Share of active listings with a price reduction, September 2026</div>'
    W = 944; w = round(W * 0.208)
    b += (f'<div class="abs seg-gold mono" style="left:68px;top:488px;width:{w}px;height:50px;border-radius:8px 0 0 8px;display:flex;align-items:center;justify-content:center;font-size:22px">20.8%</div>'
          f'<div class="abs seg-steel" style="left:{68+w}px;top:488px;width:{W-w}px;height:50px;border-radius:0 8px 8px 0;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:700">79.2% no price cut</div>')
    b += '<div class="abs lbl" style="left:68px;top:572px">Illustrative: asking price vs sale price</div>'
    cards = [("$285,000", "Listed at", "illustrative list price", "seg-blue"),
             ("-4%", "Price cut", "illustrative cut", "seg-blue2"),
             ("$273,600", "Sale price", "$11,400 below asking", "seg-gold")]
    x = 68
    for big, t, n, cls in cards:
        b += (f'<div class="abs {cls}" style="left:{x}px;top:608px;width:305px;height:120px;border-radius:14px">'
              f'<div class="abs mono" style="left:22px;top:14px;font-size:36px;line-height:44px;white-space:nowrap">{big}</div>'
              f'<div class="abs" style="left:22px;top:62px;font-size:20px;font-weight:700">{t}</div>'
              f'<div class="abs" style="left:22px;top:90px;font-size:15px">{n}</div></div>')
        x += 320
    b += panel(758, 96, "LIST PRICE = ASK", "A lender can ask what payoff looks like at a lower sale price.", 520, 26)
    foot = ("Source: Realtor.com Monthly Housing Report, September 2026 data (PR Newswire, Sept 30, 2026; RISMedia, Oct 7, 2026). "
            "Arithmetic: 100 - 20.8 = 79.2; $285,000 x 0.96 = $273,600; $285,000 x 0.04 = $11,400. The $285,000 and 4% are illustrative. National figures.")
    return shell("1 in 5 listings took a price cut", "Asking is not the sale price.",
                 "Realtor.com, September 2026 data", b, foot, 884,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"realtor-inventory-price-cuts": ("images/2026-10-26/0842-fb-realtor-inventory-price-cuts.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
