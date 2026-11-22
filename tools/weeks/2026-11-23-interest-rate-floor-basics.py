#!/usr/bin/env python3
"""Graphic for interest rate floor basics. Run from repo root: python3 tools/weeks/2026-11-23-interest-rate-floor-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, MARGIN, FLOOR = 540000, 4.0, 11.5
PRIMES = [7.75, 6.75, 5.75]

def mo(rate):
    return LOAN * rate / 100 / 12

def gfx():
    assert round(mo(11.5), 2) == 5175.00 and round(mo(9.75), 2) == 4387.50 and round(mo(11.5) - mo(9.75), 2) == 787.50
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative: $540,000 interest-only, prime plus 4 percent, 11.5 percent floor</div>'
    for x, t in ((90, "Prime (illustrative)"), (360, "Formula: prime + 4"), (680, "Rate charged")):
        body += f'<div class="abs steel" style="left:{x}px;top:332px;font-size:16px;font-weight:700">{t}</div>'
    y = 362
    for p in PRIMES:
        f = p + MARGIN
        hit = f < FLOOR
        r = max(f, FLOOR)
        bg = "background:#0B1F3A;" if hit else ""
        ink = "#F0EDE4" if hit else "#0B1F3A"
        gold = "#E2C265" if hit else "#9C7F2B"
        note = "floor applies" if hit else "formula applies"
        body += (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:84px;{bg}">'
                 f'<div class="abs mono" style="left:22px;top:0;height:100%;width:250px;display:flex;align-items:center;font-size:28px;color:{ink}">{p:.2f}%</div>'
                 f'<div class="abs mono" style="left:292px;top:0;height:100%;width:260px;display:flex;align-items:center;font-size:28px;color:{ink}">{f:.2f}%</div>'
                 f'<div class="abs mono" style="left:612px;top:0;height:100%;width:170px;display:flex;align-items:center;font-size:28px;color:{gold}">{r:.2f}%</div>'
                 f'<div class="abs" style="left:780px;top:0;height:100%;width:140px;display:flex;align-items:center;font-size:16px;font-weight:700;color:{gold}">{note}</div></div>')
        y += 98
    body += ('<div class="card" style="left:68px;top:664px;width:458px;height:110px"><div class="abs lbl" style="left:22px;top:16px">At 11.5% floor rate</div>'
             '<div class="abs mono gold" style="left:22px;top:44px;font-size:34px">$5,175.00</div><div class="abs steel" style="left:22px;top:84px;font-size:15px">monthly interest</div></div>')
    body += ('<div class="card" style="left:554px;top:664px;width:458px;height:110px"><div class="abs lbl" style="left:22px;top:16px">At 9.75% formula rate</div>'
             '<div class="abs mono gold" style="left:22px;top:44px;font-size:34px">$4,387.50</div><div class="abs steel" style="left:22px;top:84px;font-size:15px">monthly interest</div></div>')
    body += ('<div class="panel" style="top:798px;height:66px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:24px">Floor holds $787.50 a month</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:400px;display:flex;align-items:center;font-size:17px;line-height:23px;color:#3F5470">Terms vary by lender. Confirm the floor in the note.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "What happens when prime falls?", "A rate floor, worked out",
                "The rate cannot drop below the floor", body,
                "Sources: Rocket Mortgage, Interest rate floor: Definition and how it works (updated 2026-05-01); LendingTree glossary, Interest rate floor (page undated, accessed 2026-11-22). "
                "Arithmetic: 540,000 x 0.115 / 12 = 5,175.00; 540,000 x 0.0975 / 12 = 4,387.50; difference 787.50. Loan, margin, floor and prime values illustrative.", 890)

PAGES = {"interest-rate-floor-basics": ("images/2026-11-26/1727-fb-interest-rate-floor-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
