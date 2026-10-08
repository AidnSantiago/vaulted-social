#!/usr/bin/env python3
"""Graphic for cross-collateralization (FB Sat Oct 10, 2026, 9:32 am). Run from repo root: python3 tools/weeks/2026-10-05-cross-collateralization.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Illustrative inputs (also listed under "derived" in the plan entry)
LOAN, PROP_A, PROP_B = 310000, 225000, 175000
COMBINED = PROP_A + PROP_B                      # 400,000
LTV_BOTH = LOAN / COMBINED * 100                # 77.5
LTV_A = LOAN / PROP_A * 100                     # 137.8
assert COMBINED == 400000 and f"{LTV_BOTH:.1f}" == "77.5" and f"{LTV_A:.1f}" == "137.8"

LEFT = 68
S = 640 / COMBINED                              # px per dollar: the $400,000 combined value is 640 px wide
BAR_H = 38


def bar(left, top, width, text, cls, radius="8px", extra="", size=16):
    return (f'<div class="abs {cls} mono" style="left:{left:.1f}px;top:{top}px;width:{width:.1f}px;height:{BAR_H}px;'
            f'border-radius:{radius};display:flex;align-items:center;padding-left:12px;font-size:{size}px;white-space:nowrap;{extra}">{text}</div>')


def row_title(top, text):
    return f'<div class="abs" style="left:{LEFT}px;top:{top}px;font-size:18px;line-height:24px;font-weight:700;color:#F0EDE4;white-space:nowrap">{text}</div>'


def stat(top, big, caption, formula):
    return (f'<div class="abs mono gold" style="left:736px;top:{top}px;font-size:46px;line-height:50px;white-space:nowrap">{big}</div>'
            f'<div class="abs" style="left:736px;top:{top + 54}px;font-size:17px;line-height:22px;font-weight:700;color:#F0EDE4;white-space:nowrap">{caption}</div>'
            f'<div class="abs mono" style="left:736px;top:{top + 80}px;font-size:15px;line-height:20px;color:#8A9BB0;white-space:nowrap">{formula}</div>')


def info_card(x, w, label, text, top=628, h=124):
    return (f'<div class="card" style="left:{x}px;top:{top}px;width:{w}px;height:{h}px">'
            f'<div class="abs lbl" style="left:20px;top:16px">{label}</div>'
            f'<div class="abs" style="left:20px;top:44px;width:{w - 40}px;font-size:16px;line-height:22px;color:#F0EDE4">{text}</div></div>')


def gfx():
    wl, wa, wb = LOAN * S, PROP_A * S, PROP_B * S          # 496, 360, 280 px
    b = '<div class="abs lbl" style="left:68px;top:262px">The loan vs. the value behind it, bar length = dollars</div>'

    # Row 1: both properties pledged
    y = 296
    b += row_title(y, "Both properties pledged")
    b += bar(LEFT, y + 30, wl, "Loan $310,000", "seg-steel")
    b += bar(LEFT, y + 76, wa, "Property A $225,000", "seg-gold", "8px 0 0 8px")
    b += bar(LEFT + wa, y + 76, wb, "Property B $175,000", "seg-blue2", "0 8px 8px 0", "border-left:2px solid #0B1F3A;")
    bw = wa + wb
    b += (f'<svg class="abs" style="left:{LEFT}px;top:{y + 120}px" width="{bw:.0f}" height="10" viewBox="0 0 {bw:.0f} 10">'
          f'<path d="M1 1 V8 H{bw - 1:.0f} V1" fill="none" stroke="#E2C265" stroke-width="2"/></svg>')
    b += (f'<div class="abs gold" style="left:{LEFT}px;top:{y + 134}px;width:{bw:.0f}px;text-align:center;'
          f'font-size:17px;line-height:22px;font-weight:700">Combined value $400,000</div>')
    b += stat(y + 28, "77.5%", "LTV on combined value", "$310,000 &divide; $400,000")

    # Row 2: Property B released, nothing paid down
    y = 478
    b += row_title(y, "Property B sells and is released, nothing paid down")
    b += bar(LEFT, y + 30, wa, "Loan $310,000", "seg-steel", "8px 0 0 8px")
    b += (f'<div class="abs mono" style="left:{LEFT + wa:.1f}px;top:{y + 30}px;width:{wl - wa:.1f}px;height:{BAR_H}px;'
          f'border:1.5px dashed rgba(226,194,101,.9);border-radius:0 8px 8px 0;display:flex;align-items:center;justify-content:center;'
          f'font-size:14px;color:#E2C265;white-space:nowrap">not covered</div>')
    b += bar(LEFT, y + 76, wa, "Property A $225,000", "seg-gold", "8px 0 0 8px")
    b += (f'<div class="abs" style="left:{LEFT + wa:.1f}px;top:{y + 76}px;width:{wb:.1f}px;height:{BAR_H}px;'
          f'border:1.5px dashed rgba(138,155,176,.75);border-radius:0 8px 8px 0;display:flex;align-items:center;justify-content:center;'
          f'font-size:15px;color:#A5B2C3;white-space:nowrap">Property B released</div>')
    b += stat(y + 28, "137.8%", "LTV on Property A alone", "$310,000 &divide; $225,000")

    # What to check
    cw = 298
    b += info_card(68, cw, "Release", "How a property leaves the loan when it is sold. Varies by lender and loan documents.")
    b += info_card(391, cw, "Default", "What a default puts at risk. A lender could take possession of part or all of the properties.")
    b += info_card(714, cw, "Valuation", "How each property is valued,<br>such as an appraisal of each.<br>If a value falls, LTV rises.")

    b += panel(774, 84, "READ THE RELEASE TERMS", "More collateral helps only while enough<br>stays behind the loan.", 430)

    nb = lambda t: t.replace(" ", "&nbsp;")
    foot = ("Sources: " + nb("Barnes Walker") + " legal glossary (undated, accessed " + nb("Oct 7, 2026") + "); "
            + nb("Multifamily Loans") + ", cross collateralization guide (" + nb("Nov 3, 2022") + "); " + nb("Lendz Financial") + ", cross-collateral loan guide (" + nb("Feb 26, 2026") + "); "
            "UpCounsel, Partial Release Clause Explained (" + nb("Sep 29, 2025") + "). Illustrative example. "
            + nb("$225,000 + $175,000 = $400,000") + "; " + nb("$310,000 &divide; $400,000 = 77.5%") + "; " + nb("$310,000 &divide; $225,000 = 137.8%") + ". "
            "The term can also mean one property securing several loans. Terms vary by lender, loan documents and state. Not legal advice.")
    return shell("What is cross-collateralization?", "One loan, more than one property.",
                 "Illustrative example: one $310,000 loan secured by two properties", b, foot, 880)


PAGES = {"cross-collateralization": ("images/2026-10-10/0932-fb-cross-collateralization.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
