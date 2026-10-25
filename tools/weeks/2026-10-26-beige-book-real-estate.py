#!/usr/bin/env python3
"""Graphic for Beige Book Oct 2026 real estate commentary (Facebook, Thu Oct 29, 2026 8:25 am ET). Built Oct 25, 2026.
Run from repo root: python3 tools/weeks/2026-10-26-beige-book-real-estate.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, name, num, res, com, extra):
    w = 460
    s = f'<div class="card" style="left:{x}px;top:262px;width:{w}px;height:430px">'
    s += f'<div class="abs mono gold" style="left:22px;top:20px;font-size:30px;line-height:36px">{name}</div>'
    s += f'<div class="abs steel" style="left:22px;top:60px;font-size:15px">{num}</div>'
    s += '<div class="abs lbl" style="left:22px;top:104px">Residential</div>'
    s += f'<div class="abs" style="left:22px;top:130px;width:{w-44}px;font-size:19px;line-height:26px;font-weight:700;color:#F0EDE4">{res}</div>'
    s += '<div class="abs lbl" style="left:22px;top:250px">Commercial</div>'
    s += f'<div class="abs" style="left:22px;top:276px;width:{w-44}px;font-size:19px;line-height:26px;font-weight:700;color:#F0EDE4">{com}</div>'
    s += f'<div class="abs" style="left:22px;top:338px;width:{w-44}px;font-size:15.5px;line-height:22px;color:#A5B2C3">{extra}</div>'
    return s + '</div>'

def gfx():
    b = col(68, "Boston", "First District", "Closed home sales decreased moderately in August, year over year",
            "Roughly stable on balance",
            "Contacts cited downside risks tied to political uncertainty and rising longer-term interest rates.")
    b += col(552, "Atlanta", "Sixth District", "Home sales improved moderately; many buyers had difficulty qualifying for a mortgage",
             "Expanded modestly on balance",
             "Sellers offered discounts and incentives.")
    b += panel(722, 82, "Local check", "Lenders can check recent local sales before relying on a resale assumption.", 560, 24)
    foot = ("Source: Federal Reserve Board, Beige Book October 2026, Boston and Atlanta district reports, last updated Oct 14, 2026 "
            "(information collected on or before Oct 5, 2026). Quotes paraphrased from the district Real Estate sections.")
    return shell("Same Beige Book,", "different home sales", "Fed district commentary on real estate, October 14, 2026", b, foot, 826,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"beige-book-real-estate": ("images/2026-10-29/0825-fb-beige-book-real-estate.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
