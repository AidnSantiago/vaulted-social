#!/usr/bin/env python3
"""Graphic for homeowners insurance cost trend and DSCR (Facebook, Fri Oct 23, 2026 8:00 am ET). Built Oct 18, 2026.
Run from repo root: python3 tools/weeks/2026-10-19-insurance-cost-trend.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    rent, pit, ins = 2400, 1850, 300
    ins2 = round(ins * 1.3)
    a, b2 = pit + ins, pit + ins2
    d1, d2 = rent / a, rent / b2
    assert (a, b2, ins2) == (2150, 2240, 390) and round(d1, 2) == 1.12 and round(d2, 2) == 1.07
    b = '<div class="abs lbl" style="left:68px;top:268px">NAIC, average homeowners premium per policy, 2018 to 2024</div>'
    b += stat_card(68, 304, 290, 150, "18.3-43.3%", "inflation-adjusted rise", "range across four NAIC regions", 38)
    b += stat_card(395, 304, 290, 150, "2.4-5.3%", "average rise per year", "range across regions", 40)
    b += stat_card(722, 304, 290, 150, "4 of 4", "regions saw increases", "average premium per policy", 44)
    b += '<div class="abs lbl" style="left:68px;top:486px">Illustrative DSCR: rent $2,400 a month</div>'
    for x, lab, ins_s, pay, ds, cls in [(68, "Before", "$300", "$2,150", "1.12", "seg-blue"), (545, "Insurance up 30%", "$390", "$2,240", "1.07", "seg-gold")]:
        b += (f'<div class="card" style="left:{x}px;top:522px;width:467px;height:150px">'
              f'<div class="abs lbl" style="left:20px;top:16px">{lab}</div>'
              f'<div class="abs mono gold" style="left:20px;top:46px;font-size:46px;line-height:54px">{ds}</div>'
              f'<div class="abs steel" style="left:170px;top:50px;width:280px;font-size:17px;line-height:25px">DSCR = $2,400 / {pay}<br>insurance {ins_s} a month</div>'
              f'<div class="abs" style="left:20px;top:112px;font-size:15px;color:#8A9BB0">payment = $1,850 + {ins_s} = {pay}</div></div>')
    b += panel(708, 96, "1.12 to 1.07", "Same rent, same loan. Minimum DSCR varies by lender, and landlord policies can differ from homeowners.", 560, 28)
    foot = ("Source: NAIC, news release, Aug. 5, 2026 (MCAS data, 2018 to 2024). Example is illustrative: DSCR = rent / (principal, interest, taxes + insurance); "
            "2,400 / 2,150 = 1.12; 2,400 / 2,240 = 1.07; 300 x 1.3 = 390.")
    return shell("Premiums rose in every NAIC region.", "Your DSCR can feel it.",
                 "Premium trend, and what it does to the ratio", b, foot, 826,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"insurance-cost-trend": ("images/2026-10-23/0800-fb-insurance-cost-trend.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
