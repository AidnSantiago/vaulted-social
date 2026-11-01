#!/usr/bin/env python3
"""Graphic for loan-loss-reserve (LinkedIn, Tue Nov 3, 2026 10:21 am ET). Illustrative pooled reserve.
Run from repo root:  python3 tools/weeks/2026-11-02-loan-loss-reserve.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

A, RA, B, RB = 2900000, 0.012, 1450000, 0.03  # illustrative
W = 944


def gfx():
    ra, rb = A * RA, B * RB
    tot = ra + rb
    assert round(ra) == 34800 and round(rb) == 43500 and round(tot) == 78300 and A + B == 4350000
    assert round(tot / (A + B) * 100, 1) == 1.8
    wa = W * A / (A + B)
    wb = W - wa
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative $4,350,000 loan book, two pools</div>'
    y = 306
    b += (f'<div class="abs seg-blue" style="left:68px;top:{y}px;width:{wa:.1f}px;height:84px;border-radius:8px 0 0 8px"></div>'
          f'<div class="abs seg-gold" style="left:{68 + wa:.1f}px;top:{y}px;width:{wb:.1f}px;height:84px;border-radius:0 8px 8px 0"></div>'
          f'<div class="abs mono" style="left:68px;top:{y}px;width:{wa:.1f}px;height:84px;display:flex;align-items:center;justify-content:center;font-size:26px">$2,900,000</div>'
          f'<div class="abs mono" style="left:{68 + wa:.1f}px;top:{y}px;width:{wb:.1f}px;height:84px;display:flex;align-items:center;justify-content:center;font-size:26px;color:#0B1F3A">$1,450,000</div>')
    b += (f'<div class="abs steel" style="left:68px;top:{y + 98}px;font-size:17px;font-weight:700">Pool 1: lower risk, 1.2 percent</div>'
          f'<div class="abs gold" style="left:{68 + wa + 20:.0f}px;top:{y + 98}px;font-size:17px;font-weight:700;white-space:nowrap">Pool 2: higher risk, 3.0 percent</div>')
    cy = 470
    b += stat_card(68, cy, 290, 168, "$34,800", "Pool 1 reserve", "$2,900,000 x 1.2%", 40)
    b += stat_card(375, cy, 290, 168, "$43,500", "Pool 2 reserve", "$1,450,000 x 3.0%", 40)
    b += stat_card(682, cy, 330, 168, "$78,300", "total reserve", "1.8% of $4,350,000", 40)
    b += panel(676, 96, "pool x rate = reserve", "A lender can start from its own loss history, then adjust for current conditions.", 440, 24)
    b += ('<div class="abs" style="left:68px;top:796px;width:944px;font-size:17px;line-height:25px;color:#A5B2C3">'
          'The Federal Reserve defines the allowance for credit losses as an estimate of expected credit losses, and says loans with similar risk characteristics can be measured as a pool.</div>')
    return shell("What is a loan loss", "reserve, in plain terms?", "Expected losses, estimated by pool of similar loans", b,
                 "Sources: Federal Reserve, FAQs on the CECL Methodology (page undated, accessed 2026-11-01); FDIC, FIL-39-2016 (June 17, 2016). Bank accounting terms. Example figures illustrative. Arithmetic: 2,900,000 x 0.012 = 34,800; 1,450,000 x 0.03 = 43,500; sum = 78,300; 78,300 / 4,350,000 = 1.8%.", 880)


PAGES = {"loan-loss-reserve": ("images/2026-11-03/1021-li-loan-loss-reserve.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
