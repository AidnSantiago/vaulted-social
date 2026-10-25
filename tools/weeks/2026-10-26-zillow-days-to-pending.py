#!/usr/bin/env python3
"""Graphic for Zillow September 2026 market report (Facebook, Fri Oct 30, 2026 8:00 am ET).
Run from repo root: python3 tools/weeks/2026-10-26-zillow-days-to-pending.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    daily = 330000 * 0.10 / 365
    assert f"{daily:.2f}" == "90.41"
    assert f"{daily*29:,.0f}" == "2,622" and f"{daily*2:,.0f}" == "181"
    b = '<div class="abs lbl" style="left:68px;top:268px">Timeline: listing to pending to closing</div>'
    # timeline bar
    b += ('<div class="abs seg-gold mono" style="left:68px;top:312px;width:560px;height:70px;border-radius:8px 0 0 8px;'
          'display:flex;align-items:center;justify-content:center;font-size:24px">29 days to go pending</div>')
    b += ('<div class="abs seg-steel" style="left:628px;top:312px;width:384px;height:70px;border-radius:0 8px 8px 0;'
          'display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700">Closing still ahead</div>')
    b += '<div class="abs" style="left:68px;top:392px;font-size:16px;color:#8A9BB0">Median, Zillow, September 2026. A pending sale is under contract, not closed.</div>'
    b += stat_card(68, 440, 290, 150, "29 days", "median to go pending", "2 days longer than a year ago", 40)
    b += stat_card(395, 440, 290, 150, "-8.5%", "newly pending sales", "vs a year earlier", 40)
    b += stat_card(722, 440, 290, 150, "$2,622", "interest over 29 days", "illustrative: $330,000 at 10%", 40)
    b += '<div class="abs lbl" style="left:68px;top:624px">Illustrative interest, $330,000 at 10% interest-only</div>'
    b += ('<div class="abs" style="left:68px;top:660px;width:944px;font-size:21px;line-height:30px;color:#A5B2C3">'
          '<span class="mono gold">$330,000 x 10% / 365 = $90.41 a day</span><br>'
          '29 days is $2,622. The 2 extra days add $181.</div>')
    b += panel(760, 92, "ASK FOR THE TIMELINE", "Lenders can ask what listing time an exit plan assumes.", 430, 24)
    foot = ("Source: Zillow, September 2026 Market Report (Oct 6, 2026). National medians; local markets vary. "
            "Illustrative: $330,000 x 10% / 365 = $90.41 a day (actual/365); x 29 = $2,621.92; x 2 = $180.82.")
    return shell("Homes took 29 days to go pending.", "Pending is not closed.",
                 "Zillow, September 2026 national data", b, foot, 876, eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"zillow-days-to-pending": ("images/2026-10-30/0800-fb-zillow-days-to-pending.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
