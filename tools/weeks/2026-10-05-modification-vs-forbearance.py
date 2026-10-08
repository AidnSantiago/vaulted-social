#!/usr/bin/env python3
"""Graphic for forbearance vs modification (Facebook, Sun Oct 11, 2026, 1:47 pm ET).
Run from repo root: python3 tools/weeks/2026-10-05-modification-vs-forbearance.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render, CHK, ARROW_R

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Illustrative inputs, and the arithmetic behind every number on the graphic.
PRINCIPAL, RATE = 275000, 0.11
MONTHLY = PRINCIPAL * RATE / 12      # 2520.8333...
DEFER3 = MONTHLY * 3                  # 7562.50
EXTRA6 = MONTHLY * 6                  # 15125.00
M = f"${MONTHLY:,.2f}"
D3 = f"${DEFER3:,.2f}"
E6 = f"${EXTRA6:,.0f}"
assert (M, D3, E6) == ("$2,520.83", "$7,562.50", "$15,125")

SUBLBL = "font-size:14px;font-weight:700;letter-spacing:.12em;color:#8A9BB0;white-space:nowrap"
X0 = 322   # left edge of the middle column inside each lane card
RX = 700   # left edge of the result column


def lane(top, label, head, desc, mid, big, cap, small, doc):
    return (f'<div class="card" style="left:68px;top:{top}px;width:944px;height:208px">'
            f'<div class="abs lbl" style="left:24px;top:20px">{label}</div>'
            f'<div class="abs" style="left:24px;top:46px;font-size:26px;line-height:32px;font-weight:700;color:#F0EDE4;white-space:nowrap">{head}</div>'
            f'<div class="abs" style="left:24px;top:88px;width:272px;font-size:16.5px;line-height:22px;color:#A5B2C3">{desc}</div>'
            f'{mid}'
            f'<div class="abs mono gold" style="left:{RX}px;top:24px;font-size:40px;line-height:48px;white-space:nowrap">{big}</div>'
            f'<div class="abs" style="left:{RX}px;top:80px;width:230px;font-size:21px;line-height:26px;font-weight:700;color:#F0EDE4">{cap}</div>'
            f'<div class="abs" style="left:{RX}px;top:112px;width:230px;font-size:15px;line-height:20px;color:#8A9BB0">{small}</div>'
            f'<div class="abs" style="left:24px;top:162px;width:896px;border-top:1px solid rgba(138,155,176,.28)"></div>'
            f'<div class="abs" style="left:24px;top:172px">{CHK}</div>'
            f'<div class="abs" style="left:62px;top:170px;height:30px;display:flex;align-items:center;font-size:17px;color:#F0EDE4;white-space:nowrap">{doc}</div>'
            '</div>')


def mid_forbearance():
    h = f'<div class="abs" style="left:{X0}px;top:22px;{SUBLBL}">3 MONTHS OF INTEREST DEFERRED</div>'
    for i in range(3):
        x = X0 + i * 110
        h += (f'<div class="abs" style="left:{x}px;top:54px;width:100px;height:64px;border-radius:10px;'
              f'border:2px dashed rgba(226,194,101,.85);background:rgba(201,168,76,.10)">'
              f'<div class="abs mono" style="left:0;top:8px;width:96px;text-align:center;font-size:13px;color:#8A9BB0">Month {i + 1}</div>'
              f'<div class="abs mono gold" style="left:0;top:31px;width:96px;text-align:center;font-size:15px">{M}</div></div>')
    h += f'<div class="abs mono" style="left:{X0}px;top:128px;font-size:17px;color:#F0EDE4;white-space:nowrap">3 x {M}</div>'
    h += ARROW_R.format(x=656, y=76)
    return h


def mid_modification():
    stub_w = 100
    line_x = X0 + stub_w + 8
    t0 = line_x + 12
    h = (f'<div class="abs" style="left:{X0 - 20}px;top:22px;width:{line_x - X0 + 12}px;text-align:right;{SUBLBL}">OLD MATURITY</div>'
         f'<div class="abs" style="left:{t0}px;top:22px;{SUBLBL}">+6 MONTHS</div>'
         f'<div class="abs seg-steel" style="left:{X0}px;top:54px;width:{stub_w}px;height:64px;border-radius:10px 0 0 10px;'
         f'display:flex;align-items:center;justify-content:center;text-align:center;font-size:14px;line-height:18px">original<br>term</div>'
         f'<div class="abs" style="left:{line_x}px;top:44px;height:84px;border-left:2px dashed rgba(226,194,101,.85)"></div>')
    for i in range(6):
        x = t0 + i * 34
        rad = "0 10px 10px 0" if i == 5 else "0"
        h += (f'<div class="abs seg-gold mono" style="left:{x}px;top:54px;width:30px;height:64px;border-radius:{rad};'
              f'display:flex;align-items:center;justify-content:center;font-size:16px">{i + 1}</div>')
    h += f'<div class="abs mono" style="left:{t0}px;top:128px;font-size:17px;color:#F0EDE4;white-space:nowrap">6 x {M}</div>'
    h += ARROW_R.format(x=656, y=76)
    return h


def doc(txt):
    return f'<span class="gold" style="font-weight:700">Document:&nbsp;</span>{txt}'


def gfx():
    b = lane(266, "Forbearance", "A temporary pause",
             "Old terms paused, not rewritten.<br>Nothing is forgiven.",
             mid_forbearance(), D3, "still owed later", "Deferred, not forgiven.",
             doc("the amount owed and a reservation of rights."))
    b += lane(490, "Modification", "A permanent change",
              "New terms replace the old ones.",
              mid_modification(), "+" + E6, "more interest", "Paid over the 6 extra months.",
              doc("the new terms. With a known default, it may waive that default."))
    b += panel(716, 96, "PAUSE OR REPLACE",
               "Document each for what it is: a pause, or new terms.<br>Business-purpose loans generally fall outside federal consumer mortgage rules, so loan documents and state law control.", 600)
    foot = ("Sources: CFPB, What is mortgage forbearance? (Aug 31, 2026) and What is a mortgage loan modification? (Mar 12, 2025); "
            "CFPB, Regulation X 1024.5 (page undated, accessed Oct 7, 2026); Fannie Mae, Forbearance (page undated, accessed Oct 7, 2026); ABF Journal, Markovich and Brownstein (May 11, 2020); "
            "Pillsbury (Apr 13, 2020); Amundsen Davis (Oct 23, 2025). CFPB and Fannie Mae forbearance pages describe consumer mortgages; "
            "Regulation X exempts credit primarily for a business purpose. "
            "Illustrative: $275,000 x 11% &divide; 12 = $2,520.83 a month (rounded); x 3 = $7,562.50; x 6 = $15,125.00 (unrounded). "
            "Assumes no interest on the deferred amount (CFPB: it could add up). General education, not legal advice.")
    return shell("Forbearance vs. modification:", "pause the terms or replace them.",
                 "Illustrative: $275,000 interest-only loan at 11% = $2,520.83 interest a month",
                 b, foot, 834)


PAGES = {"modification-vs-forbearance": ("images/2026-10-11/1347-fb-modification-vs-forbearance.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
