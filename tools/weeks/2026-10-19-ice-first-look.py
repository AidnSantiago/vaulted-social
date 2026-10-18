#!/usr/bin/env python3
"""Graphic for ICE First Look (August 2026 data), LinkedIn, Mon Oct 19, 2026 11:34 am ET.
Run from repo root: python3 tools/weeks/2026-10-19-ice-first-look.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def col(x, w, title, tag, rows):
    s = (f'<div class="card" style="left:{x}px;top:410px;width:{w}px;height:310px">'
         f'<div class="abs lbl" style="left:24px;top:22px">{tag}</div>'
         f'<div class="abs" style="left:24px;top:50px;font-family:Georgia,serif;font-weight:700;font-size:28px">{title}</div>')
    y = 108
    for big, cap, cls in rows:
        s += (f'<div class="abs mono {cls}" style="left:24px;top:{y}px;font-size:44px;line-height:52px;white-space:nowrap">{big}</div>'
              f'<div class="abs" style="left:24px;top:{y + 54}px;width:{w - 48}px;font-size:18px;line-height:24px;color:#A5B2C3">{cap}</div>')
        y += 102
    return s + '</div>'


def gfx():
    b = ('<div class="abs seg-gold" style="left:68px;top:268px;width:944px;height:124px;border-radius:14px">'
         '<div class="abs mono" style="left:26px;top:24px;font-size:62px;line-height:76px">3.53%</div>'
         '<div class="abs" style="left:290px;top:30px;width:630px;font-size:22px;line-height:30px;font-weight:700">'
         'National delinquency rate, August 2026. Up 14 basis points, effectively flat after calendar effects.</div></div>')
    b += col(68, 462, "Foreclosure starts", "New activity (flow)",
             [("-6%", "change from July", "gold"), ("+29%", "change from a year earlier", "gold")])
    b += col(550, 462, "Active inventory", "Loans already in process (stock)",
             [("+2,000", "loans added in August", "gold"), ("+41%", "change from a year earlier", "gold")])
    b += panel(750, 96, "SAME MONTH, LAST YEAR", "Compare to the prior year, and read new starts apart from inventory.", 480, 22)
    foot = ("Source: ICE Mortgage Technology, First Look at August 2026 Mortgage Data (Sept. 28, 2026). "
            "Residential mortgage data, not private loans. As of August 2026.")
    return shell("Delinquencies look steady.", "Foreclosure starts do not.",
                 "ICE First Look, August 2026 data", b, foot, 868)


PAGES = {"ice-first-look": ("images/2026-10-19/1134-li-ice-first-look.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
