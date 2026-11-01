#!/usr/bin/env python3
"""Graphic for sale waterfall math (Facebook, Sun Nov 8, 2026 1:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-sale-waterfall-math.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SALE, COSTS, FIRST, SECOND = 410000, 12000, 330000, 60000  # illustrative


def gfx():
    after_costs = SALE - COSTS
    after_first = after_costs - FIRST
    owner = after_first - SECOND
    assert (after_costs, after_first, owner) == (398000, 68000, 8000)
    W = 944
    sc = W / SALE
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative foreclosure sale: $410,000</div>'
    rows = [
        ("1  Sale costs", COSTS, 0, "seg-steel", "$12,000", "$398,000 left"),
        ("2  First lien (foreclosing)", FIRST, COSTS, "seg-blue", "$330,000", "$68,000 left"),
        ("3  Second lien", SECOND, COSTS + FIRST, "seg-blue2", "$60,000", "$8,000 left"),
        ("4  Owner, if anything remains", owner, COSTS + FIRST + SECOND, "seg-gold", "$8,000", "$0 left"),
    ]
    y = 310
    for lab, amt, start, cls, amt_s, left in rows:
        x = 68 + start * sc
        w = amt * sc
        b += f'<div class="abs" style="left:68px;top:{y}px;font-size:19px;font-weight:700;color:#F0EDE4;white-space:nowrap">{lab}</div>'
        b += f'<div class="abs mono gold" style="right:68px;top:{y}px;font-size:18px;white-space:nowrap">{amt_s} paid, {left}</div>'
        b += f'<div class="abs" style="left:68px;top:{y + 32}px;width:{W}px;height:38px;border-radius:6px;background:rgba(138,155,176,.12)"></div>'
        b += f'<div class="abs {cls}" style="left:{x:.1f}px;top:{y + 32}px;width:{max(w, 8):.1f}px;height:38px;border-radius:6px"></div>'
        y += 98
    b += panel(y + 6, 76, "Pay in order", "Each step is paid in full before the next. Varies by state.", 430, 26)
    foot = ("Sources: UWorld Legal, Real Property Quick Tip: How to Distribute Foreclosure Sale Proceeds (published Jan 18, 2021; modified Jan 3, 2025); "
            "Nolo, How to Claim Foreclosure Surplus Funds (page undated, accessed Nov 1, 2026). Illustrative inputs. "
            "Arithmetic: 410,000 - 12,000 = 398,000; 398,000 - 330,000 = 68,000; 68,000 - 60,000 = 8,000.")
    return shell("Who is paid from a foreclosure", "sale, and in what order.",
                 "Costs, first lien, second lien, then the owner &middot; illustrative", b, foot, 900)


PAGES = {"sale-waterfall-math": ("images/2026-11-08/1347-fb-sale-waterfall-math.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
