#!/usr/bin/env python3
"""Graphic for rehab overrun and loan-to-cost (Facebook, Fri Nov 6, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-overrun-ltc-math.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

P, R, O = 241000, 57500, 14500  # illustrative
LOAN = round(0.85 * P + R)
COST = P + R
COST2 = COST + O
assert (LOAN, COST, COST2) == (262350, 298500, 313000)
L_A = LOAN + O
assert L_A == 276850 and COST - LOAN == 36150 and COST2 - LOAN == 50650 and COST2 - L_A == 36150
assert round(LOAN / COST * 100, 1) == 87.9 and round(L_A / COST2 * 100, 1) == 88.5 and round(LOAN / COST2 * 100, 1) == 83.8


def col(x, w, tag, tagcls, rows, ltc, note):
    b = f'<div class="card" style="left:{x}px;top:296px;width:{w}px;height:392px"></div>'
    b += f'<div class="abs {tagcls} mono" style="left:{x+18}px;top:314px;padding:7px 12px;border-radius:8px;font-size:15px;white-space:nowrap">{tag}</div>'
    y = 366
    for lab, val in rows:
        b += f'<div class="abs" style="left:{x+18}px;top:{y}px;font-size:15.5px;color:#A5B2C3;white-space:nowrap">{lab}</div>'
        b += f'<div class="abs mono" style="left:{x+18}px;top:{y+22}px;font-size:23px;line-height:30px;white-space:nowrap">{val}</div>'
        y += 66
    b += f'<div class="abs" style="left:{x+18}px;top:{y+2}px;font-size:15.5px;color:#A5B2C3;white-space:nowrap">Loan to cost</div>'
    b += f'<div class="abs mono gold" style="left:{x+18}px;top:{y+24}px;font-size:40px;line-height:46px;white-space:nowrap">{ltc}</div>'
    return b


def gfx():
    w, g = 296, 28
    b = '<div class="abs lbl" style="left:68px;top:262px">Illustrative: $241,000 purchase, $57,500 rehab budget</div>'
    b += col(68, w, "START", "seg-steel", [("Loan", "$262,350"), ("Total cost", "$298,500"), ("Borrower cash in", "$36,150")], "87.9%", "")
    b += col(68 + w + g, w, "LENDER FUNDS", "seg-blue", [("Loan", "$276,850"), ("Total cost", "$313,000"), ("Borrower cash in", "$36,150")], "88.5%", "")
    b += col(68 + 2 * (w + g), w, "BORROWER PAYS", "seg-gold", [("Loan", "$262,350"), ("Total cost", "$313,000"), ("Borrower cash in", "$50,650")], "83.8%", "")
    b += '<div class="abs steel" style="left:68px;top:712px;font-size:17px;white-space:nowrap">Rehab runs $14,500 over: total cost rises from $298,500 to $313,000.</div>'
    b += panel(758, 100, "LTC = loan / total cost", "Who covers the overrun changes the ratio.", 390, 25)
    foot = ("Sources: FCTD, Fix and Flip Loans: LTV vs LTC, Feb 3, 2024; Backflip, LTC, LTV and LtPP, Mar 21, 2025. Illustrative inputs. "
            "Arithmetic: 0.85 x 241,000 + 57,500 = 262,350; 241,000 + 57,500 = 298,500; +14,500 = 313,000; 262,350 / 298,500 = 87.9%; "
            "276,850 / 313,000 = 88.5%; 262,350 / 313,000 = 83.8%; cash in = total cost - loan: 36,150 and 50,650.")
    return shell("A rehab overrun moves", "the loan to cost ratio.",
                 "Same budget, two ways to cover $14,500 &middot; illustrative", b, foot, 884)


PAGES = {"overrun-ltc-math": ("images/2026-11-06/1247-fb-overrun-ltc-math.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
