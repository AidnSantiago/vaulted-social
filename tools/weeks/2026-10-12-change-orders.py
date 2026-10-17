#!/usr/bin/env python3
"""Graphic for change-order checks. Run from repo root: python3 tools/weeks/2026-10-12-change-orders.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BUDGET = 84000   # illustrative
CHANGE = 6300    # illustrative
PCT = CHANGE / BUDGET * 100   # 7.5
BAR_W = 944
CH_W = round(BAR_W * CHANGE / BUDGET)   # 71


def card(x, y, w, h, n, title, desc):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="num" style="top:16px">{n}</div>'
            f'<div class="abs" style="left:68px;top:0;height:68px;width:{w-84}px;display:flex;align-items:center;font-size:21px;font-weight:700;color:#F0EDE4">{title}</div>'
            f'<div class="abs" style="left:20px;top:72px;width:{w-40}px;font-size:16px;line-height:22px;color:#A5B2C3">{desc}</div></div>')


def gfx():
    b = f'<div class="abs lbl" style="left:68px;top:268px">Illustrative rehab budget and one change order</div>'
    b += (f'<div class="abs seg-blue" style="left:68px;top:300px;width:{BAR_W - CH_W}px;height:60px;border-radius:10px 0 0 10px"></div>'
          f'<div class="abs seg-gold" style="left:{68 + BAR_W - CH_W}px;top:300px;width:{CH_W}px;height:60px;border-radius:0 10px 10px 0"></div>')
    b += (f'<div class="abs mono" style="left:88px;top:318px;font-size:24px;color:#F0EDE4">${BUDGET:,} budget</div>')
    b += (f'<div class="abs mono gold" style="left:{68 + BAR_W - 260}px;top:372px;width:260px;text-align:right;font-size:24px">${CHANGE:,} = {PCT:.1f}%</div>')
    b += f'<div class="abs" style="left:68px;top:376px;font-size:17px;color:#A5B2C3">Added bathroom, priced by the contractor</div>'
    cw, ch = 462, 128
    b += card(68, 428, cw, ch, 1, "Written and signed?", "Borrower and contractor sign the change order, then it goes to the lender.")
    b += card(550, 428, cw, ch, 2, "Adds a line item?", "One guide treats a scope change that adds or removes a line as material.")
    b += card(68, 574, cw, ch, 3, "Is the total unchanged?", "Some lenders allow moving funds between lines when the total budget is the same.")
    b += card(550, 574, cw, ch, 4, "Who pays?", "One guide says upgrades can be paid by the borrower, with proof of payment.")
    b += panel(722, 84, "APPROVE FIRST", "One guide: written lender approval before the affected draw funds.", 440)
    foot = ("Sources: Ledger Trade &amp; Capital, Construction Loan Draw Schedule (Oct 9, 2026); LandGorilla, How Lenders Can Navigate Rising Material Costs (page undated, accessed Oct 17, 2026); "
            f"HUD Loans, How Construction Draw Processes Vary by Lender (May 21, 2025). Amounts are illustrative. Arithmetic: ${CHANGE:,} / ${BUDGET:,} = {PCT:.1f}%. Practices vary by lender.")
    return shell("Four checks on a rehab", "change order.", "Before the affected draw funds", b, foot, 830)


PAGES = {"change-orders": ("images/2026-10-18/1727-fb-change-orders.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
