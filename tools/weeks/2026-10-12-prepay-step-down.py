#!/usr/bin/env python3
"""Graphic for the step-down prepayment fee post (Facebook, Sat Oct 17, 2026 1:47 pm ET). Illustrative numbers.
Run from repo root: python3 tools/weeks/2026-10-12-prepay-step-down.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BAL = 360000
STEPS = [(1, 3), (2, 2), (3, 1), (4, 0)]   # illustrative 3/2/1 schedule


def gfx():
    fees = [BAL * p / 100 for _, p in STEPS]
    assert [f"{f:,.0f}" for f in fees] == ["10,800", "7,200", "3,600", "0"]
    b = '<div class="abs lbl" style="left:68px;top:268px">Fee if paid off in each year, balance $360,000</div>'
    base, maxh, bw, gap = 640, 270, 190, 61
    for i, ((yr, p), f) in enumerate(zip(STEPS, fees)):
        x = 68 + i * (bw + gap)
        h = maxh * f / fees[0]
        if f > 0:
            b += (f'<div class="abs seg-gold mono" style="left:{x}px;top:{base - h:.0f}px;width:{bw}px;height:{h:.0f}px;border-radius:10px 10px 0 0;'
                  f'display:flex;align-items:flex-start;justify-content:center;padding-top:12px;font-size:28px">${f:,.0f}</div>')
        else:
            b += (f'<div class="abs mono steel" style="left:{x}px;top:{base - 52}px;width:{bw}px;text-align:center;font-size:28px">$0</div>')
        b += f'<div class="abs" style="left:{x}px;top:{base}px;width:{bw}px;height:3px;background:#46556A"></div>'
        b += (f'<div class="abs" style="left:{x}px;top:{base + 12}px;width:{bw}px;text-align:center;font-size:20px;font-weight:700;color:#F0EDE4">Year {yr}</div>')
        b += (f'<div class="abs mono gold" style="left:{x}px;top:{base + 40}px;width:{bw}px;text-align:center;font-size:20px">{"no fee" if p == 0 else f"{p}%"}</div>')
    b += panel(740, 90, "FEE = % x BALANCE",
               "Schedules and the balance they apply to vary by lender. Some states limit prepayment fees.", 460, 26)
    foot = ("Sources: OfferMarket, Prepayment Penalty guide (last edited Jul 25, 2025): 3-2-1 charges 3% on the outstanding principal loan balance in year 1, 2% in year 2, 1% in year 3. "
            "Home Abroad Inc., DSCR Loan Prepayment Penalty (updated Jun 4, 2026): step-down fees are typically a percentage of the outstanding balance at payoff. "
            "Illustrative: $360,000 balance held constant. Arithmetic: $360,000 x 3% = $10,800; x 2% = $7,200; x 1% = $3,600.")
    return shell("A step-down fee shrinks each year", "3% on $360,000 is $10,800",
                 "Illustrative 3/2/1 prepayment schedule", b, foot, 860)


PAGES = {"prepay-step-down": ("images/2026-10-17/1347-fb-prepay-step-down.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
