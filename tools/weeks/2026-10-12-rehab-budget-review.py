#!/usr/bin/env python3
"""Graphic for rehab budget review checklist. Run from repo root: python3 tools/weeks/2026-10-12-rehab-budget-review.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render, CHK
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BUDGET = 52000                 # illustrative
LOW = BUDGET * 5 // 100        # 2600
HIGH = BUDGET * 10 // 100      # 5200

ROWS = [
    ("Line-item detail", "Quantities and materials named, labor and materials separated where possible"),
    ("Contractor quotes", "Costs built from current contractor bids and actual contractor input"),
    ("Contingency line", "One lender guide: 5% commonly required, up to a 10% ceiling"),
    ("Timeline", "Compared with the scope of work and the local sales market"),
]


def gfx():
    b = ""
    for i, (t, d) in enumerate(ROWS):
        y = 272 + i * 84
        b += (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:72px">'
              f'<div class="abs" style="left:20px;top:23px">{CHK}</div>'
              f'<div class="abs" style="left:64px;top:0;height:72px;width:250px;display:flex;align-items:center;font-size:21px;font-weight:700;color:#F0EDE4">{t}</div>'
              f'<div class="abs" style="left:320px;top:0;height:72px;width:600px;display:flex;align-items:center;font-size:17px;line-height:23px;color:#A5B2C3">{d}</div></div>')
    b += stat_card(68, 622, 462, 150, f"${LOW:,}", "contingency at 5%", f"of an illustrative ${BUDGET:,} rehab budget")
    b += stat_card(550, 622, 462, 150, f"${HIGH:,}", "contingency at the 10% ceiling", f"10% &times; ${BUDGET:,}")
    b += panel(796, 84, "WATCH VAGUE LINES", "Vague line items can signal weak planning or hidden costs.", 440)
    foot = ("Sources: Kiavi, How to Write a Fix and Flip Scope of Work (Jun 1, 2026); Merchants Mortgage, How Fix and Flip Lenders Determine Project Risk (May 4, 2026). "
            f"Budget is illustrative. Arithmetic: 5% &times; ${BUDGET:,} = ${LOW:,}; 10% &times; ${BUDGET:,} = ${HIGH:,}. Requirements vary by lender.")
    return shell("Four checks on a rehab budget", "before the first draw.", "What a lender can review in the scope of work",
                 b, foot, 900)


PAGES = {"rehab-budget-review": ("images/2026-10-14/1727-fb-rehab-budget-review.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
