#!/usr/bin/env python3
"""Graphic for default carry cost (Facebook, Mon Nov 2, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-default-carry-cost.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, RATE, TAX, INS, MONTHS = 420000, 0.11, 5400, 3000, 8  # illustrative


def gfx():
    interest = LOAN * RATE / 12
    tax, ins = TAX / 12, INS / 12
    month = interest + tax + ins
    assert round(interest, 2) == 3850 and tax == 450 and ins == 250 and month == 4550 and month * MONTHS == 36400
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative monthly carry</div>'
    b += stat_card(68, 304, 290, 150, "$3,850", "lost interest", "$420,000 x 11% / 12", 46)
    b += stat_card(395, 304, 290, 150, "$450", "property taxes", "$5,400 / 12", 46)
    b += stat_card(722, 304, 290, 150, "$250", "insurance", "$3,000 / 12", 46)
    b += '<div class="abs lbl" style="left:68px;top:488px">Carry that builds up over 8 months</div>'
    W = 944
    for k in range(MONTHS):
        pass
    cum = [month * (k + 1) for k in range(MONTHS)]
    mx = cum[-1]
    for k, v in enumerate(cum):
        top = 528 + k * 31
        w = v / mx * W
        cls = "seg-gold" if k == MONTHS - 1 else "seg-blue"
        lab = f"Month {k + 1}: ${v:,.0f}"
        b += f'<div class="abs {cls}" style="left:68px;top:{top}px;width:{w:.1f}px;height:26px;border-radius:6px"></div>'
        if w < 330:
            b += (f'<div class="abs mono steel" style="left:{68 + w + 12:.1f}px;top:{top}px;height:26px;display:flex;'
                  f'align-items:center;font-size:15px">{lab}</div>')
        else:
            col = "#0B1F3A" if k == MONTHS - 1 else "#F0EDE4"
            b += (f'<div class="abs mono" style="left:80px;top:{top}px;width:{w - 24:.1f}px;height:26px;display:flex;'
                  f'align-items:center;justify-content:flex-end;font-size:15px;color:{col}">{lab}</div>')
    b += panel(790, 80, "$4,550 x 8 = $36,400", "Per month: $3,850 + $450 + $250.", 330, 26)
    foot = ("Sources: Congressional Research Service, The Process, Data, and Costs of Mortgage Foreclosure, 2008-10-20; "
            "Note Servicing Center, Carry Costs in Private Lending (page undated, accessed 2026-11-01). "
            "Illustrative: $420,000 loan, 11%, taxes $5,400 a year, insurance $3,000 a year, 8 months. "
            "Arithmetic: 3,850 + 450 + 250 = 4,550; 4,550 x 8 = 36,400.")
    return shell("Default does not stop the clock.", "Carry costs keep running.",
                 "Monthly carry while foreclosure runs &middot; illustrative", b, foot, 888)


PAGES = {"default-carry-cost": ("images/2026-11-02/1247-fb-default-carry-cost.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
