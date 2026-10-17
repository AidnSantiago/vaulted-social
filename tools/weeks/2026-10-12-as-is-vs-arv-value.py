#!/usr/bin/env python3
"""Graphic for the as-is-vs-arv-value post (Facebook, Sun Oct 18, 2026 1:47 pm ET). Illustrative example.
Run from repo root:  python3 tools/weeks/2026-10-12-as-is-vs-arv-value.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ASIS, ARV, REHAB, LTARV, LTC = 240000, 410000, 60000, 0.70, 0.85   # illustrative


def gfx():
    cost = ASIS + REHAB
    a = ASIS * LTARV
    b_ = ARV * LTARV
    c = cost * LTC
    loan = min(b_, c)
    pct = loan / ASIS * 100
    assert (cost, round(a), round(b_), round(c), round(loan), pct) == (300000, 168000, 287000, 255000, 255000, 106.25)

    b = stat_card(68, 276, 290, 150, "$168,000", "70% of as-is value", "70% x $240,000")
    b += stat_card(395, 276, 290, 150, "$287,000", "70% of ARV", "70% x $410,000")
    b += stat_card(722, 276, 290, 150, "$255,000", "85% of total cost", "85% x ($240,000 + $60,000)")

    b += '<div class="abs lbl" style="left:68px;top:464px">The $255,000 loan against each value</div>'
    X0, W = 232, 700
    S = W / ARV
    H = 56

    def lab(y, big, small):
        return (f'<div class="abs" style="left:68px;top:{y}px;width:156px;height:{H}px;display:flex;flex-direction:column;justify-content:center">'
                f'<div style="font-size:19px;line-height:24px;font-weight:700">{big}</div>'
                f'<div style="font-size:14.5px;line-height:18px;color:#8A9BB0">{small}</div></div>')

    def seg(y, w, cls, text):
        return (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{w:.1f}px;height:{H}px;border-radius:8px;'
                f'display:flex;align-items:center;padding-left:14px;font-size:19px;white-space:nowrap">{text}</div>')

    y1, y2 = 502, 580
    b += lab(y1, "As-is value", "today, as it stands") + lab(y2, "ARV", "after planned repairs")
    b += seg(y1, ASIS * S, "seg-steel", "$240,000")
    b += seg(y2, ARV * S, "seg-gold", "$410,000")
    lx = X0 + loan * S
    b += (f'<div class="abs" style="left:{lx:.1f}px;top:{y1 - 8}px;width:0;height:{y2 - y1 + H + 16}px;border-left:2.5px dashed #F0EDE4"></div>')
    b += (f'<div class="abs mono" style="left:{lx + 12:.1f}px;top:{y1 + 4}px;font-size:16px;line-height:20px;color:#F0EDE4">loan $255,000</div>')
    b += (f'<div class="abs mono" style="left:{lx + 12:.1f}px;top:{y1 + 28}px;font-size:15px;line-height:20px;color:#E2C265">about 106% of as-is</div>')
    b += '<div class="abs" style="left:68px;top:664px;width:944px;font-size:16.5px;line-height:23px;color:#A5B2C3">The lesser cap applies: $255,000, not $287,000. Rehab is $60,000. The loan reaches past today\'s value only if the repairs get done. Caps and how each lender sets them vary by lender.</div>'
    b += panel(742, 100, "ARV WIDENS THE LOAN", "The extra is backed by the finished rehab. Compare both values.", 400, 24)
    foot = ("Sources: Crestmont Capital, What Is After-Repair Value in Fix-and-Flip Loans (Jun 17, 2026): the maximum loan is ARV x maximum LTARV, and when two limits apply \"the lender will offer the lesser of the two calculations\". "
            "FCTD, Fix and Flip Loans: AS-IS Value Versus After Repair Value (Feb 3, 2024): definitions. "
            "Illustrative inputs: bought at as-is value, 70% LTARV, 85% loan-to-cost. "
            "0.70 x 240,000 = 168,000; 0.70 x 410,000 = 287,000; cost 240,000 + 60,000 = 300,000; x 0.85 = 255,000; 255,000 / 240,000 = 106.25%, about 106%.")
    return shell("Worth $240,000 as-is, $410,000 ARV.", "Which value sets the loan?",
                 "Illustrative worked example &middot; same property, two values, two caps", b, foot, 866,
                 eyebrow="PRIVATE LENDING, EXPLAINED")


PAGES = {"as-is-vs-arv-value": ("images/2026-10-18/1347-fb-as-is-vs-arv-value.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
