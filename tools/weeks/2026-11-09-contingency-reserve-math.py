#!/usr/bin/env python3
"""Graphic for contingency reserve math (Facebook, Tue Nov 10, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-contingency-reserve-math.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

P, H = 188000, 66000  # illustrative
def calc(c):
    cont = round(H * c); bud = H + cont; loan = round(0.9 * P + bud); cost = P + bud
    return cont, bud, loan, round(loan / cost * 100, 1)
A, B = calc(0.08), calc(0.12)
assert A == (5280, 71280, 240480, 92.7) and B == (7920, 73920, 243120, 92.8) and B[2] - A[2] == 2640


def col(x, w, tag, tagcls, v, pct):
    cont, bud, loan, ltc = v
    b = f'<div class="card" style="left:{x}px;top:296px;width:{w}px;height:392px"></div>'
    b += f'<div class="abs {tagcls} mono" style="left:{x+22}px;top:314px;padding:7px 14px;border-radius:8px;font-size:16px;white-space:nowrap">{tag}</div>'
    # stacked bar: hard costs + contingency
    bw = w - 44
    cw = max(6, round(bw * cont / bud))
    b += f'<div class="abs seg-blue" style="left:{x+22}px;top:370px;width:{bw-cw}px;height:26px;border-radius:6px 0 0 6px"></div>'
    b += f'<div class="abs seg-gold" style="left:{x+22+bw-cw}px;top:370px;width:{cw}px;height:26px;border-radius:0 6px 6px 0"></div>'
    y = 414
    for lab, val, cls in [("Contingency", f"${cont:,}", "gold"), ("Rehab budget", f"${bud:,}", ""), ("Loan", f"${loan:,}", ""), ("Loan to cost", f"{ltc}%", "")]:
        b += f'<div class="abs" style="left:{x+22}px;top:{y}px;font-size:15.5px;color:#A5B2C3;white-space:nowrap">{lab}</div>'
        b += f'<div class="abs mono {cls}" style="left:{x+22}px;top:{y+22}px;font-size:26px;line-height:32px;white-space:nowrap">{val}</div>'
        y += 66
    return b


def gfx():
    w, g = 458, 28
    b = '<div class="abs lbl" style="left:68px;top:262px">Illustrative: $188,000 purchase, $66,000 hard costs</div>'
    b += col(68, w, "8% CONTINGENCY", "seg-steel", A, 8)
    b += col(68 + w + g, w, "12% CONTINGENCY", "seg-gold", B, 12)
    b += '<div class="abs steel" style="left:68px;top:708px;font-size:17px;white-space:nowrap">Loan = 90% of purchase + full rehab budget. Sources: contingency can run 3% to 10% (MCAP); 10-15% (Kiavi).</div>'
    b += panel(758, 100, "+$2,640 on the loan", "Loan to cost barely moves: 92.7% to 92.8%. Size the line on purpose.", 430, 25)
    foot = ("Sources: MCAP, How to budget for your construction project, Nov 12, 2024 (3% to 10% of construction costs); "
            "Kiavi, Rehab over budget contingency options, Aug 10, 2026 (at least 10-15% of the renovation budget). Illustrative inputs; lender rules vary by lender. "
            "Arithmetic: 66,000 x 8% = 5,280; 66,000 x 12% = 7,920; 0.9 x 188,000 + 71,280 = 240,480; + 73,920 = 243,120; "
            "240,480 / 259,280 = 92.7%; 243,120 / 261,920 = 92.8%.")
    return shell("Sizing a rehab contingency", "changes the loan budget.",
                 "Same deal at 8% and 12% of hard costs &middot; illustrative", b, foot, 884)


PAGES = {"contingency-reserve-math": ("images/2026-11-10/1247-fb-contingency-reserve-math.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
