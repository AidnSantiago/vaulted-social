#!/usr/bin/env python3
"""Graphic for concentration-risk (Facebook, Thu Oct 22, 2026 12:47 pm ET). Illustrative stacked bar + ratio cards.
Run from repo root:  python3 tools/weeks/2026-10-19-concentration-risk.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

PORT, TOP1, TOP3 = 8000000, 1400000, 3200000   # illustrative
W = 944


def gfx():
    p1, p3 = TOP1 / PORT * 100, TOP3 / PORT * 100
    assert (p1, p3) == (17.5, 40.0)
    w1, w3, wr = W * TOP1 / PORT, W * (TOP3 - TOP1) / PORT, W * (PORT - TOP3) / PORT
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative $8,000,000 portfolio</div>'
    y = 306
    b += (f'<div class="abs seg-gold" style="left:68px;top:{y}px;width:{w1:.1f}px;height:84px;border-radius:8px 0 0 8px"></div>'
          f'<div class="abs seg-blue2" style="left:{68 + w1:.1f}px;top:{y}px;width:{w3:.1f}px;height:84px"></div>'
          f'<div class="abs seg-steel" style="left:{68 + w1 + w3:.1f}px;top:{y}px;width:{wr:.1f}px;height:84px;border-radius:0 8px 8px 0"></div>')
    b += (f'<div class="abs mono" style="left:68px;top:{y}px;width:{w1:.1f}px;height:84px;display:flex;align-items:center;justify-content:center;font-size:24px;color:#0B1F3A">17.5%</div>'
          f'<div class="abs mono" style="left:{68 + w1:.1f}px;top:{y}px;width:{w3:.1f}px;height:84px;display:flex;align-items:center;justify-content:center;font-size:24px">22.5%</div>'
          f'<div class="abs mono" style="left:{68 + w1 + w3:.1f}px;top:{y}px;width:{wr:.1f}px;height:84px;display:flex;align-items:center;justify-content:center;font-size:24px">60%</div>')
    ly = y + 98
    b += (f'<div class="abs" style="left:68px;top:{ly}px;width:{w1 + 20:.0f}px;font-size:17px;line-height:22px;font-weight:700;color:#E2C265">Top borrower<br><span class="mono" style="font-size:15px;font-weight:700">$1,400,000</span></div>'
          f'<div class="abs" style="left:{68 + w1 + 40:.0f}px;top:{ly}px;width:300px;font-size:17px;line-height:22px;font-weight:700;color:#A5B2C3">Next two borrowers<br><span class="mono" style="font-size:15px">$1,800,000</span></div>'
          f'<div class="abs" style="left:{68 + w1 + w3 + 60:.0f}px;top:{ly}px;width:330px;font-size:17px;line-height:22px;font-weight:700;color:#A5B2C3">All other borrowers<br><span class="mono" style="font-size:15px">$4,800,000</span></div>')
    cy = 470
    b += stat_card(68, cy, 458, 168, "17.5%", "in the top borrower", "$1,400,000 / $8,000,000", 56)
    b += stat_card(554, cy, 458, 168, "40%", "in the top three borrowers", "$3,200,000 / $8,000,000", 56)
    b += panel(676, 96, "exposure / portfolio", "Lenders can group related borrowers together before ranking the largest names.", 440, 24)
    b += ('<div class="abs" style="left:68px;top:796px;width:944px;font-size:17px;line-height:25px;color:#A5B2C3">'
          'The OCC bank handbook says methods for identifying concentrations vary from bank to bank, and lists exposure to any one borrower or group of related borrowers.</div>')
    return shell("Is your top borrower", "too much of the book?", "Two ratios show how concentrated a portfolio is", b,
                 "Source: OCC, Comptroller's Handbook, Concentrations of Credit v3.0 (September 2026). Figures illustrative. Arithmetic: 1,400,000 / 8,000,000 = 17.5%; 3,200,000 / 8,000,000 = 40%; (3,200,000 - 1,400,000) / 8,000,000 = 22.5%.", 880)


PAGES = {"concentration-risk": ("images/2026-10-22/1247-fb-concentration-risk.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
