#!/usr/bin/env python3
"""Graphic for in-balance requirement. Run from repo root: python3 tools/weeks/2026-10-19-in-balance-requirement.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

COST = 104000      # illustrative remaining cost to complete
UNDISB = 90000     # illustrative undisbursed loan funds
GAP = COST - UNDISB  # 14000
BAR_X, BAR_W = 68, 944


def gfx():
    wu = round(BAR_W * UNDISB / COST)
    wg = BAR_W - wu
    b = ""
    b += '<div class="abs lbl" style="left:68px;top:268px">Remaining cost to complete</div>'
    b += (f'<div class="abs seg-steel" style="left:{BAR_X}px;top:300px;width:{BAR_W}px;height:64px;border-radius:10px;'
          f'display:flex;align-items:center;justify-content:center;font-size:30px" ><span class="mono">${COST:,}</span></div>')
    b += '<div class="abs lbl" style="left:68px;top:392px">Undisbursed loan funds</div>'
    b += (f'<div class="abs seg-blue2" style="left:{BAR_X}px;top:424px;width:{wu}px;height:64px;border-radius:10px 0 0 10px;'
          f'display:flex;align-items:center;justify-content:center;font-size:30px"><span class="mono">${UNDISB:,}</span></div>')
    b += (f'<div class="abs" style="left:{BAR_X+wu}px;top:424px;width:{wg}px;height:64px;border-radius:0 10px 10px 0;'
          f'border:2px dashed #D2B058;border-left:none;display:flex;align-items:center;justify-content:center;font-size:20px;color:#E2C265">'
          f'<span class="mono">${GAP:,}</span></div>')
    b += '<div class="abs" style="left:68px;top:500px;font-size:18px;color:#A5B2C3">Gap of <span class="mono gold">$14,000</span> = $104,000 minus $90,000. The loan is out of balance.</div>'
    b += stat_card(68, 556, 462, 150, "IN BALANCE", "Undisbursed funds can finish the job", "Unfunded loan covers the remaining cost", big_size=38)
    b += stat_card(550, 556, 462, 150, "OUT OF BALANCE", "The lender may act", "Sample: deposit the gap or pay costs", big_size=38)
    b += panel(730, 100, "$104,000 - $90,000 = $14,000", "Lenders can compare remaining cost with undisbursed funds.", 400, 24)
    foot = ("Sources: Scotsman Guide, Construction Lending 101 (Oct 30, 2019); Construction Loan Agreement, Summit Hotel Properties and Compass Bank, SEC filing (Sep 17, 2008). "
            "Dollar figures are illustrative. Arithmetic: $104,000 - $90,000 = $14,000. Terms vary by lender.")
    return shell("When a rehab loan", "falls out of balance.", "Undisbursed loan funds versus cost to complete", b, foot, 870)


PAGES = {"in-balance-requirement": ("images/2026-10-21/1247-fb-in-balance-requirement.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
