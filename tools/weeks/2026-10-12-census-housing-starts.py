#!/usr/bin/env python3
"""Graphic for Census/HUD New Residential Construction, August 2026 (Facebook, Fri Oct 16, 2026 8:00 am ET). Built Oct 13, 2026.
Run from repo root: python3 tools/weeks/2026-10-12-census-housing-starts.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# (label, sub, revised July, August, change text from the release)
ROWS = [("Housing starts", "all private units", 1309000, 1275000, "-2.6%"),
        ("Building permits", "all private units", 1433000, 1394000, "-2.7%"),
        ("Single-family starts", "one-unit homes", 853000, 918000, "+7.6%")]

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">Seasonally adjusted annual rates, July (revised) vs August 2026</div>'
    X0, W, H = 300, 560, 46
    S = W / 1500000
    y = 308
    for lab, sub, jul, aug, chg in ROWS:
        b += (f'<div class="abs" style="left:68px;top:{y}px;width:225px;height:{2*H+8}px;display:flex;flex-direction:column;justify-content:center">'
              f'<div style="font-size:19px;line-height:23px;font-weight:700">{lab}</div>'
              f'<div style="font-size:14px;line-height:18px;color:#8A9BB0">{sub}</div></div>')
        b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:{y}px;width:{jul*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:10px;font-size:15px">{jul:,}</div>')
        b += (f'<div class="abs seg-gold mono" style="left:{X0}px;top:{y+H+8}px;width:{aug*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:10px;font-size:15px">{aug:,}</div>')
        b += (f'<div class="abs mono gold" style="left:{X0+max(jul,aug)*S+16:.0f}px;top:{y+H-8}px;font-size:22px;white-space:nowrap">{chg}</div>')
        y += 2*H + 8 + 40
    b += ('<div class="abs" style="left:300px;top:{0}px;font-size:14.5px;color:#A5B2C3">'
          '<span style="display:inline-block;width:14px;height:14px;background:#3F5E8E;border-radius:3px;margin-right:8px;vertical-align:-2px"></span>July (revised) '
          '<span style="display:inline-block;width:14px;height:14px;background:#D2B058;border-radius:3px;margin:0 8px 0 24px;vertical-align:-2px"></span>August 2026</div>').format(y - 6)
    b += ('<div class="abs" style="left:68px;top:{0}px;width:944px;font-size:16.5px;line-height:23px;color:#A5B2C3">'
          'The Census change in total starts carries a margin of error of &plusmn;12.0 percent. Next release: October 20, 2026.</div>').format(y + 36)
    b += panel(y + 90, 76, "ONE MONTH IS ONE PRINT", "Annualized rates, not units started in a month.", 400, 22)
    foot = ("Source: U.S. Census Bureau and HUD, New Residential Construction, August 2026 (released Sep 17, 2026). "
            "Bars are seasonally adjusted annual rates; July figures are the revised estimates; percent changes are as reported by Census.")
    return shell("August 2026 housing starts:", "1,275,000, down 2.6%.",
                 "Census and HUD new residential construction, August 2026", b, foot, y + 196,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"census-housing-starts": ("images/2026-10-16/0800-fb-census-housing-starts.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
