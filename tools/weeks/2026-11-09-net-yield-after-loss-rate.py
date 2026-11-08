#!/usr/bin/env python3
"""Graphic for net yield after a loss (Facebook, Fri Nov 13, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-net-yield-after-loss-rate.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

PORT, GROSS_PCT, LOSS = 2200000, 10.2, 44000  # illustrative
INTEREST = round(PORT * GROSS_PCT / 100)
NET = INTEREST - LOSS
NET_PCT = round(NET / PORT * 100, 2)
LOSS_PCT = round(LOSS / PORT * 100, 2)
assert INTEREST == 224400 and NET == 180400 and NET_PCT == 8.2 and LOSS_PCT == 2.0


def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">Illustrative $2,200,000 portfolio, one year</div>'
    b += '<div class="card" style="left:68px;top:292px;width:944px;height:240px"></div>'
    rows = [("Interest earned", INTEREST, "seg-blue2", "$224,400", "#F0EDE4"),
            ("One loss", LOSS, "seg-steel", "&minus;$44,000", "#E2C265"),
            ("Kept (net)", NET, "seg-gold", "$180,400", "#E2C265")]
    y = 316
    maxw = 520
    left = 330
    for i, (lab, v, cls, txt, col) in enumerate(rows):
        w = round(maxw * v / INTEREST)
        x = left if i != 2 else left
        if i == 1:
            x = left + round(maxw * NET / INTEREST)  # loss sits at the right end of the interest bar
        b += f'<div class="abs" style="left:92px;top:{y+4}px;font-size:19px;font-weight:700;white-space:nowrap">{lab}</div>'
        b += f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:34px;border-radius:6px"></div>'
        tx = left + maxw + 14 if i != 1 else left + maxw + 14
        b += f'<div class="abs mono" style="left:{tx}px;top:{y+2}px;font-size:21px;color:{col};white-space:nowrap">{txt}</div>'
        y += 68
    b += stat_card(68, 562, 458, 150, "10.2%", "Gross yield", "$224,400 / $2,200,000")
    b += stat_card(554, 562, 458, 150, "8.2%", "Net yield after the loss", "$180,400 / $2,200,000")
    b += panel(742, 100, "Net = (interest &minus; losses) / lent", "The one loss equals 2.0 percent of the portfolio, so it lowers yield by 2.0 points.", 400, 21)
    foot = ("Sources: WallStreetMojo, Net Yield, updated Jan 14, 2026 (net yield is the return after deducting costs); Law Insider, Net Yield, page undated, accessed 2026-11-08 (Gross Yield less impairments). "
            "Illustrative inputs: $2,200,000 portfolio, 10.2 percent gross rate, one $44,000 loss, one year. "
            "Arithmetic: 2,200,000 x 10.2% = 224,400; 224,400 - 44,000 = 180,400; 180,400 / 2,200,000 = 8.2%; 44,000 / 2,200,000 = 2.0%.")
    return shell("Gross yield is not", "what you keep.",
                 "Net yield after one loss &middot; illustrative", b, foot, 876)


PAGES = {"net-yield-after-loss-rate": ("images/2026-11-13/1247-fb-net-yield-after-loss-rate.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
