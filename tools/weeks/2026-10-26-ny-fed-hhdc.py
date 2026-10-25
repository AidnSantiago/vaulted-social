#!/usr/bin/env python3
"""Graphic for NY Fed Household Debt and Credit Q2 2026 (Facebook, Sat Oct 31, 2026 9:32 am ET). Built Oct 25, 2026.
Run from repo root: python3 tools/weeks/2026-10-26-ny-fed-hhdc.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def card(x, y, w, h, label, big, cap, cls):
    return (f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:14px">'
            f'<div class="abs" style="left:26px;top:22px;font-size:16px;font-weight:700;letter-spacing:.14em">{label}</div>'
            f'<div class="abs mono" style="left:26px;top:60px;font-size:78px;line-height:90px">{big}</div>'
            f'<div class="abs" style="left:26px;top:166px;width:{w-52}px;font-size:18px;line-height:24px;font-weight:700">{cap}</div></div>')

def gfx():
    assert round(1.52 - 1.29, 2) == 0.23 and round((1.52 / 1.29 - 1) * 100) == 18
    b = card(68, 270, 400, 230, "Q2 2025", "1.29%", "mortgage balances newly 90+ days late", "seg-blue")
    b += '<div class="abs mono gold" style="left:486px;top:360px;font-size:34px">&rarr;</div>'
    b += card(540, 270, 472, 230, "Q2 2026", "1.52%", "mortgage balances newly 90+ days late", "seg-gold")
    b += stat_card(68, 530, 290, 150, "+0.23", "percentage points", "1.52 minus 1.29")
    b += stat_card(395, 530, 290, 150, "~18%", "higher than a year ago", "1.52 / 1.29, rounded")
    b += stat_card(722, 530, 290, 150, "$505B", "originated in Q2", "new mortgage debt")
    b += ('<div class="abs" style="left:68px;top:706px;width:944px;font-size:18px;line-height:26px;color:#A5B2C3">'
          'Annualized share of balances that newly became 90 or more days late, as a share of balances that were current or under 90 days late the quarter before. All household mortgages, not private loans.</div>')
    b += panel(800, 80, "A BACKDROP, NOT YOUR BOOK", "Check your own loans one by one.", 400, 24)
    foot = ("Source: Federal Reserve Bank of New York, Quarterly Report on Household Debt and Credit, Q2 2026 (press release Aug 11, 2026). "
            "Arithmetic: 1.52 - 1.29 = 0.23; 1.52 / 1.29 - 1 = 17.8%, about 18%. National figures.")
    return shell("Mortgage flow into 90+ days late", "rose to 1.52% in Q2 2026.",
                 "NY Fed Household Debt and Credit report, second quarter 2026", b, foot, 912,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"ny-fed-hhdc": ("images/2026-10-31/0932-fb-ny-fed-hhdc.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
