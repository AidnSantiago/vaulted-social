#!/usr/bin/env python3
"""Graphic for protective advances and LTV (Facebook, Sat Oct 31, 2026 1:47 pm ET).
Run from repo root: python3 tools/weeks/2026-10-26-protective-advances-ltv.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, VAL, ADV = 250000, 350000, 6500   # illustrative


def gfx():
    new = LOAN + ADV
    l0, l1 = LOAN / VAL * 100, new / VAL * 100
    assert new == 256500 and f"{l0:.1f}" == "71.4" and f"{l1:.1f}" == "73.3"
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative loan and value</div>'
    b += stat_card(68, 304, 290, 150, "$250,000", "loan balance", "illustrative", 40)
    b += stat_card(395, 304, 290, 150, "$6,500", "protective advance", "taxes or insurance paid", 44)
    b += stat_card(722, 304, 290, 150, "$350,000", "property value", "illustrative", 40)
    b += '<div class="abs lbl" style="left:68px;top:488px">Balance as a share of $350,000 value</div>'
    S = 944 / 100  # px per percent, full width = 100% of value
    H = 64
    b += (f'<div class="abs seg-blue mono" style="left:68px;top:530px;width:{l0 * S:.1f}px;height:{H}px;border-radius:8px;'
          f'display:flex;align-items:center;padding-left:18px;font-size:22px">Before: $250,000 = 71.4%</div>')
    b += (f'<div class="abs seg-gold mono" style="left:68px;top:614px;width:{l1 * S:.1f}px;height:{H}px;border-radius:8px;'
          f'display:flex;align-items:center;padding-left:18px;font-size:22px">After: $256,500 = 73.3%</div>')
    b += ('<div class="abs steel" style="left:68px;top:696px;width:944px;font-size:17px;line-height:24px">'
          'One source says an advance is added to the loan balance and accrues interest.</div>')
    b += panel(752, 92, "RECHECK LTV", "Terms vary by lender and state.", 430, 26)
    foot = ("Sources: LegalClarity, Protective Advances, May 13, 2026; Justia Contracts Dictionary, Protective Advances "
            "(page undated, accessed 2026-10-25). Illustrative: $250,000 loan, $350,000 value, $6,500 advance. "
            "Arithmetic: 250,000 / 350,000 = 71.4%; (250,000 + 6,500) / 350,000 = 73.3%.")
    return shell("An advance adds to the balance.", "LTV rises with it.",
                 "Protective advances &middot; illustrative", b, foot, 876)


PAGES = {"protective-advances-ltv": ("images/2026-10-31/1347-fb-protective-advances-ltv.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
