#!/usr/bin/env python3
"""Graphic for first-payment stub interest (Facebook, Sun Nov 15, 2026 1:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-first-payment-stub-interest.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, RATE = 325000, 0.10  # illustrative
DAYS = 30 - 19 + 1
PD = LOAN * RATE / 360
STUB = LOAN * RATE / 360 * DAYS
A31 = LOAN * RATE / 360 * 31
T30 = LOAN * RATE / 12
assert DAYS == 12 and f"{PD:.2f}" == "90.28" and f"{STUB:.2f}" == "1083.33"
assert f"{A31:.2f}" == "2798.61" and f"{T30:.2f}" == "2708.33"


def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">Illustrative loan closes Nov 19 &middot; 30-day month</div>'
    w = 944 / 30
    for d in range(1, 31):
        on = d >= 19
        cls = "seg-gold" if on else "seg-steel"
        b += (f'<div class="abs {cls}" style="left:{68 + (d - 1) * w + 1.5:.1f}px;top:298px;width:{w - 3:.1f}px;height:46px;border-radius:5px;'
              f'opacity:{1 if on else .45}"></div>')
    b += '<div class="abs steel" style="left:68px;top:352px;font-size:16px">Nov 1</div>'
    b += f'<div class="abs gold mono" style="left:{68 + 18 * w:.1f}px;top:352px;font-size:16px;white-space:nowrap">Nov 19 to Nov 30 = 12 days</div>'
    b += stat_card(68, 396, 290, 150, "12 days", "stub period", "19th through 30th", 40)
    b += stat_card(395, 396, 290, 150, "$90.28", "interest per day", "$325,000 x 10% / 360", 40)
    b += stat_card(722, 396, 290, 150, "$1,083.33", "stub interest", "12 x $325,000 x 10% / 360", 40)
    b += '<div class="abs lbl" style="left:68px;top:576px">A 31-day month, one month of interest</div>'
    S = 700 / A31
    b += (f'<div class="abs seg-gold mono" style="left:68px;top:610px;width:{A31 * S:.1f}px;height:54px;border-radius:8px;display:flex;align-items:center;padding-left:16px;font-size:21px">'
          f'$2,798.61</div><div class="abs steel" style="left:{68 + A31 * S + 14:.1f}px;top:610px;height:54px;display:flex;align-items:center;font-size:17px;white-space:nowrap">Actual/360, 31 days</div>')
    b += (f'<div class="abs seg-blue mono" style="left:68px;top:676px;width:{T30 * S:.1f}px;height:54px;border-radius:8px;display:flex;align-items:center;padding-left:16px;font-size:21px">'
          f'$2,708.33</div><div class="abs steel" style="left:{68 + T30 * S + 14:.1f}px;top:676px;height:54px;display:flex;align-items:center;font-size:17px;white-space:nowrap">30/360, every month 30 days</div>')
    b += panel(758, 92, "CHECK THE NOTE", "Day count and start date vary by lender.", 400, 26)
    foot = ("Sources: Chase, What is prepaid interest, Jul 17, 2026 (stub period from closing through month end); Corporate Finance Institute, "
            "Day Count Convention, Aug 19, 2020 (Actual/360 and 30/360); Commercial Loan Direct, Actual/360 (page undated, accessed 2026-11-08). "
            "Illustrative inputs. Arithmetic: 325,000 x 0.10 / 360 = 90.2778 a day; x 12 = 1,083.33; x 31 = 2,798.61; 325,000 x 0.10 / 12 = 2,708.33.")
    return shell("Closing mid-month leaves odd days.", "Day count prices them.",
                 "Stub interest, actual/360 vs 30/360 &middot; illustrative", b, foot, 868)


PAGES = {"first-payment-stub-interest": ("images/2026-11-15/1347-fb-first-payment-stub-interest.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
