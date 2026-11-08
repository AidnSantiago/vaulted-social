#!/usr/bin/env python3
"""Graphic for Redfin four weeks ending Oct 25 2026 (fallback from ATTOM Q3 2026, not yet released).
Run from repo root: python3 tools/weeks/2026-11-09-attom-flip-q3-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    sale = 372000 * 0.983
    gap = 372000 - sale
    assert f"{sale:,.0f}" == "365,676" and f"{gap:,.0f}" == "6,324"
    b = stat_card(68, 262, 460, 140, "$389,601", "Median sale price", "Down 0.1% from a year earlier", 44)
    b += stat_card(552, 262, 460, 140, "-15.9%", "Pending sales, year over year", "Lowest level in Redfin records", 44)
    b += stat_card(68, 422, 460, 140, "50 days", "Median days on market", "Homes that sold", 44)
    b += stat_card(552, 422, 460, 140, "21.5%", "Listings with price drops", "Up from 20.9%", 44)
    b += '<div class="abs lbl" style="left:68px;top:596px">Illustrative list price vs likely sale price</div>'
    w2 = int(944 * 0.983)
    b += ('<div class="abs seg-steel" style="left:68px;top:630px;width:944px;height:44px;border-radius:8px;display:flex;align-items:center;padding-left:18px;font-size:18px;font-weight:700">List price $372,000 (100%)</div>')
    b += (f'<div class="abs seg-gold" style="left:68px;top:688px;width:{w2}px;height:44px;border-radius:8px;display:flex;align-items:center;padding-left:18px;font-size:18px;font-weight:700">Average sale-to-list 98.3% = $365,676</div>')
    b += panel(756, 90, "$372,000 x 98.3% = $365,676", "A lender can test the exit on a lower price and a longer timeline.", 380, 22)
    foot = ("Source: Redfin, U.S. Home-Sale Prices Just Fell for the First Time in 3 Years (Oct 29, 2026), four weeks ending Oct 25, 2026. National figures; local markets vary. "
            "Arithmetic: $372,000 x 98.3% = $365,676 (illustrative list price).")
    return shell("Sale prices dipped, and", "pending sales at a Redfin low",
                 "Redfin, four weeks ending October 25, 2026", b, foot, 868, eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"attom-flip-q3-2026": ("images/2026-11-10/0915-fb-redfin-market-oct-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
