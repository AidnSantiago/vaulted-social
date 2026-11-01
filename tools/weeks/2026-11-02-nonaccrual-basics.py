#!/usr/bin/env python3
"""Graphic for nonaccrual-basics (LinkedIn, Fri Nov 6, 2026 2:00 pm ET). Illustrative loan.
Run from repo root: python3 tools/weeks/2026-11-02-nonaccrual-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, RATE = 192000, 0.0925  # illustrative


def gfx():
    m = LOAN * RATE / 12
    assert m == 1480 and m * 3 == 4440
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative $192,000 loan, 9.25 percent, interest only</div>'
    xs = [68, 375, 682]
    for i, x in enumerate(xs):
        b += stat_card(x, 306, 290 if i < 2 else 330, 160, "$1,480", f"Month {i + 1} unpaid", "interest accrued, no cash received", 42)
    # 90 day bar
    y = 508
    w = 944
    b += f'<div class="abs seg-blue" style="left:68px;top:{y}px;width:{w}px;height:56px;border-radius:8px"></div>'
    b += f'<div class="abs mono" style="left:68px;top:{y}px;width:{w}px;height:56px;display:flex;align-items:center;justify-content:center;font-size:21px">3 unpaid months = $4,440 of interest</div>'
    b += ('<div class="card" style="left:68px;top:590px;width:462px;height:124px">'
          '<div class="abs lbl" style="left:20px;top:16px">Call report test</div>'
          '<div class="abs" style="left:20px;top:44px;width:424px;font-size:17px;line-height:24px;color:#A5B2C3">Nonaccrual when principal or interest is in default 90 days or more, unless well secured and in collection.</div></div>')
    b += ('<div class="card" style="left:550px;top:590px;width:462px;height:124px">'
          '<div class="abs lbl" style="left:20px;top:16px">Accounting guidance</div>'
          '<div class="abs" style="left:20px;top:44px;width:424px;font-size:17px;line-height:24px;color:#A5B2C3">Accrual is generally suspended when collection of interest is less than probable.</div></div>')
    b += panel(740, 92, "income is not cash", "Private lenders can check how their own investor reports label it.", 430, 26)
    foot = ("Sources: FFIEC 051 Schedule RC-N instructions, rev. 6-21 (via FDIC); PwC Viewpoint, Loans and investment securities 6.10, Mar 12, 2025. Bank rules, shown as a reference point. Example illustrative. "
            "Arithmetic: 192,000 x 0.0925 / 12 = 1,480; 1,480 x 3 = 4,440.")
    return shell("When does interest stop", "counting as income?", "Nonaccrual basics, with one illustrative loan", b, foot, 856)


PAGES = {"nonaccrual-basics": ("images/2026-11-06/1400-li-nonaccrual-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
