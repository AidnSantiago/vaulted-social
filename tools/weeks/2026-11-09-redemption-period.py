#!/usr/bin/env python3
"""Graphic for redemption-period (Facebook, Mon Nov 9, 2026 8:42 am ET). Run from repo root: python3 tools/weeks/2026-11-09-redemption-period.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

TWO_YEARS_DAYS = 2 * 365
assert TWO_YEARS_DAYS == 730

def gfx():
    b = stat_card(68, 262, 460, 152, "About half", "of states", "Have a law giving a right to redeem after the sale", 44)
    b += stat_card(552, 262, 460, 152, "30 days-2 years", "range of periods", "Varies by state", 34)
    b += '<div class="abs lbl" style="left:68px;top:442px">Redemption windows, bar length = days</div>'
    rows = [("Low end of range", "30 days", 30, "seg-steel"),
            ("Maine", "90 days from judgment", 90, "seg-blue2"),
            ("Tennessee", "two years", 730, "seg-gold")]
    y = 482
    for name, label, d, cls in rows:
        w = max(int(d / 730 * 560), 8)
        b += f'<div class="abs" style="left:68px;top:{y+9}px;font-size:19px;font-weight:700;color:#F0EDE4;white-space:nowrap">{name}</div>'
        b += f'<div class="abs {cls}" style="left:250px;top:{y}px;width:{w}px;height:42px;border-radius:6px"></div>'
        b += f'<div class="abs mono gold" style="left:{250+w+14}px;top:{y+9}px;font-size:19px;white-space:nowrap">{label}</div>'
        y += 60
    b += ('<div class="abs" style="left:68px;top:668px;width:944px;font-size:17px;line-height:24px;color:#A5B2C3">'
          'Tennessee: right of redemption may be waived in the mortgage or deed of trust.</div>')
    b += panel(708, 120, "bid price + interest + fees", "To redeem after a sale, the borrower must typically pay the bid price plus interest and other allowable fees.", 420, 24)
    foot = ("Sources: FindLaw, Statutory Redemption (updated Sep 24, 2026); Nolo, The Right of Redemption (updated Feb 20, 2024). "
            "Arithmetic: two years = 2 x 365 = 730 days. Periods, waiver and payment rules vary by state.")
    return shell("After the sale, the clock", "may still be running", "Statutory right of redemption, in plain terms", b, foot, 856, eyebrow="FORECLOSURE BASICS FOR LENDERS")

PAGES = {"redemption-period": ("images/2026-11-09/0842-fb-redemption-period.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
