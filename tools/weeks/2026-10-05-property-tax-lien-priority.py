#!/usr/bin/env python3
"""Graphic for the property tax lien priority post (Facebook, Sat Oct 10, 2026, 1:47 pm ET).
Run from repo root: python3 tools/weeks/2026-10-05-property-tax-lien-priority.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, TAX = 360000, 7800   # illustrative inputs
LW = 740.0                 # px width of the loan bar; the tax sliver is drawn to the same scale
TW = LW * TAX / LOAN       # 16.03 px (2.17% of the loan bar)
GAP = 6
BH = 56                    # bar height


def loan_bar(x, y, big, small):
    return (f'<div class="abs seg-blue" style="left:{x:.1f}px;top:{y}px;width:{LW:.1f}px;height:{BH}px;border-radius:10px;'
            f'display:flex;align-items:center;padding-left:18px;white-space:nowrap">'
            f'<span class="mono" style="font-size:20px;margin-right:14px">{big}</span>'
            f'<span style="font-size:19px">{small}</span></div>')


def tax_sliver(x, y):
    return f'<div class="abs seg-gold" style="left:{x:.1f}px;top:{y}px;width:{TW:.1f}px;height:{BH}px;border-radius:4px"></div>'


def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative: a $360,000 loan and an unpaid $7,800 tax bill</div>'

    # lane 1: the order things happen in time
    y1 = 298
    b += loan_bar(68, y1, "$360,000", "first-lien loan, recorded first")
    sx = 68 + LW + GAP
    b += tax_sliver(sx, y1)
    b += (f'<div class="abs" style="left:{sx + TW + 14:.1f}px;top:{y1}px;width:150px;height:{BH}px;display:flex;flex-direction:column;justify-content:center">'
          '<div class="mono gold" style="font-size:21px;line-height:24px">$7,800</div>'
          '<div style="font-size:14.5px;line-height:18px;color:#A5B2C3">tax bill, unpaid</div></div>')

    # the flip
    b += ('<svg class="abs" style="left:68px;top:368px" width="22" height="30" viewBox="0 0 22 30">'
          '<path d="M11 3 V25 M4 18 L11 26 L18 18" fill="none" stroke="#C9A84C" stroke-width="2.4" '
          'stroke-linecap="round" stroke-linejoin="round"/></svg>')
    b += ('<div class="abs gold" style="left:104px;top:368px;height:30px;display:flex;align-items:center;'
          'font-size:18px;font-weight:700">In a number of states, the tax lien jumps the line</div>')

    # lane 2: the order claims are paid if the property is sold
    b += '<div class="abs lbl" style="left:68px;top:414px">If the property is sold, who is paid first</div>'
    y2 = 442
    b += tax_sliver(68, y2)
    b += loan_bar(68 + TW + GAP, y2, "$360,000", "first-lien loan, paid second")
    b += ('<svg class="abs" style="left:68px;top:506px" width="16" height="12" viewBox="0 0 16 12">'
          '<polygon points="8,0 16,12 0,12" fill="#E2C265"/></svg>')
    b += ('<div class="abs mono gold" style="left:94px;top:502px;height:22px;display:flex;align-items:center;'
          'font-size:18px;white-space:nowrap">$7,800 tax lien, paid first</div>')

    # numbers
    b += stat_card(68, 558, 450, 150, "2.2%", "tax bill as a share of the loan", "$7,800 &divide; $360,000")
    b += stat_card(562, 558, 450, 150, "$367,800", "balance if the lender pays the tax", "$360,000 + $7,800, before interest and fees")

    # takeaway
    b += panel(732, 100, "WATCH TAX STATUS",
               "Lenders can confirm taxes are current at closing, then monitor status on a schedule, such as before each draw.", 470)

    nb = lambda s: s.replace(" ", "&nbsp;")   # keep dates and citations from wrapping mid-way
    foot = (f"Sources: Nolo, How Do Property Liens Work? (updated {nb('Feb 21, 2024')}); Nelson Mullins, Tax Sale Investing ({nb('May 13, 2020')}); "
            f"Jimerson Birr ({nb('May 24, 2021')}); American Association of Private Lenders, Cover Your Asset, Part 2 ({nb('Mar 18, 2019')}); "
            f"Illinois Legal Aid Online ({nb('Feb 27, 2026')}); {nb('Fla. Stat. 197.122')} (2026 ed.; {nb('page undated, accessed Oct 7, 2026')}). "
            "Priority rules vary by state. Amounts are illustrative: $7,800 &divide; $360,000 = 2.17%, shown as 2.2%; "
            "$360,000 + $7,800 = $367,800. General education, not legal advice.")
    return shell("Your loan was recorded first.", "A tax bill can still be paid first.",
                 "Recording order is not always payment order, and it varies by state.",
                 b, foot, 856)


PAGES = {"property-tax-lien-priority": ("images/2026-10-10/1347-fb-property-tax-lien-priority.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
