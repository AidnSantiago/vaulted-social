#!/usr/bin/env python3
"""Graphic for the cost-of-capital spread post (illustrative $5,000,000 fund; Facebook, Thu Oct 29, 2026 12:47 pm ET). Built Oct 25, 2026.
Run from repo root: python3 tools/weeks/2026-10-26-cost-of-capital-spread.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

FUND, YIELD, COST, COST2 = 5_000_000, 11.5, 7.0, 8.0   # illustrative


def gfx():
    earned, owed = FUND * YIELD / 100, FUND * COST / 100
    spread1, spread2 = FUND * (YIELD - COST) / 100, FUND * (YIELD - COST2) / 100
    drop = (1 - spread2 / spread1) * 100
    assert (earned, owed, spread1, spread2) == (575000, 350000, 225000, 175000) and f"{drop:.0f}" == "22"

    b = '<div class="abs lbl" style="left:68px;top:268px">$5,000,000 fund: yield on loans, split into cost and spread</div>'
    b += stat_card(68, 300, 290, 150, "$575,000", "interest earned", "11.5% yield on $5,000,000")
    b += stat_card(395, 300, 290, 150, "$350,000", "interest owed", "7% cost of capital")
    b += stat_card(722, 300, 290, 150, "$225,000", "a year of spread", "4.5 points, before expenses")

    X0, S, H = 68, 944 / 11.5, 62
    def row(y, label, cost, spread, cost_txt, spr_txt):
        r = f'<div class="abs" style="left:68px;top:{y - 30}px;font-size:17px;font-weight:700;color:#F0EDE4">{label}</div>'
        r += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:{y}px;width:{cost * S:.1f}px;height:{H}px;border-radius:8px 0 0 8px;'
              f'display:flex;align-items:center;padding-left:16px;font-size:20px">{cost_txt}</div>')
        r += (f'<div class="abs seg-gold mono" style="left:{X0 + cost * S:.1f}px;top:{y}px;width:{spread * S:.1f}px;height:{H}px;border-radius:0 8px 8px 0;'
              f'display:flex;align-items:center;padding-left:16px;font-size:20px">{spr_txt}</div>')
        return r
    b += '<div class="abs lbl" style="left:68px;top:480px">Same 11.5% yield, one point more cost</div>'
    b += row(552, "Cost at 7%", COST, YIELD - COST, "7% cost", "4.5 spread")
    b += row(660, "Cost at 8%", COST2, YIELD - COST2, "8% cost", "3.5 spread")
    b += panel(750, 96, "-$50,000 A YEAR",
               "One point more on the cost side cut the spread from $225,000 to $175,000, about 22% less.", 480, 28)
    foot = ("Definition: net interest spread is interest yield on earning assets minus interest rates paid on borrowed funds "
            "(Wikipedia, Net interest spread, page undated, accessed 2026-10-25); Interest Spread = Yield on Interest-Earning Assets minus Cost of "
            "Interest-Bearing Liabilities (Umbrex, updated 2026-03-25). Illustrative: $5,000,000 fund, 7% cost, 11.5% yield, all funds lent. "
            "Arithmetic: 5,000,000 x 11.5% = $575,000; x 7% = $350,000; difference $225,000 (4.5 points). At 8%: 3.5 points = $175,000; 50,000 / 225,000 = 22.2%.")
    return shell("A 7% cost and an 11.5% yield", "leave a 4.5 point spread", "Illustrative $5,000,000 fund, before expenses and losses", b, foot, 868,
                 eyebrow="THE MATH OF LENDING")


PAGES = {"cost-of-capital-spread": ("images/2026-10-29/1247-fb-cost-of-capital-spread.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
