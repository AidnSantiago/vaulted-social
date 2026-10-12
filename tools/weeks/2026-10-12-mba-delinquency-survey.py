#!/usr/bin/env python3
"""Graphic for MBA National Delinquency Survey Q2 2026 (LinkedIn, Tue Oct 13, 2026 10:21 am ET). Built Oct 12, 2026.
Run from repo root: python3 tools/weeks/2026-10-12-mba-delinquency-survey.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# (label, sub, year-ago, now)  year-ago = now minus the reported basis-point change
ROWS = [("Delinquency rate", "all loans, seasonally adjusted", 3.93, 4.37),
        ("90+ days late or in foreclosure", "serious delinquency", 1.57, 2.06),
        ("Foreclosure inventory", "loans in the foreclosure process", 0.48, 0.67)]

def gfx():
    assert round(4.37 - 0.44, 2) == 3.93 and round(2.06 - 0.49, 2) == 1.57 and round(0.67 - 0.19, 2) == 0.48
    b = stat_card(68, 268, 290, 150, "4.37%", "delinquency rate, Q2 2026", "down 7 bps from Q1")
    b += stat_card(395, 268, 290, 150, "+44 bps", "versus a year earlier", "headline rate, 3.93% to 4.37%")
    b += stat_card(722, 268, 290, 150, "2.06%", "90+ days or in foreclosure", "up 49 bps in a year")
    b += '<div class="abs lbl" style="left:68px;top:446px">A year ago versus Q2 2026, percent of loans</div>'
    X0, S, H = 330, 105, 30          # px per percentage point
    y = 482
    for lab, sub, old, new in ROWS:
        b += (f'<div class="abs" style="left:68px;top:{y}px;width:250px;height:{2*H+8}px;display:flex;flex-direction:column;justify-content:center">'
              f'<div style="font-size:18px;line-height:22px;font-weight:700">{lab}</div>'
              f'<div style="font-size:14px;line-height:18px;color:#8A9BB0">{sub}</div></div>')
        b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:{y}px;width:{old*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:10px;font-size:15px;min-width:70px">{old:.2f}</div>')
        b += (f'<div class="abs seg-gold mono" style="left:{X0}px;top:{y+H+8}px;width:{new*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:10px;font-size:15px;min-width:70px">{new:.2f}</div>')
        y += 2*H + 8 + 22
    b += ('<div class="abs" style="left:330px;top:790px;font-size:14.5px;color:#A5B2C3">'
          '<span style="display:inline-block;width:14px;height:14px;background:#3F5E8E;border-radius:3px;margin-right:8px;vertical-align:-2px"></span>Q2 2025 '
          '<span style="display:inline-block;width:14px;height:14px;background:#D2B058;border-radius:3px;margin:0 8px 0 24px;vertical-align:-2px"></span>Q2 2026</div>')
    b += panel(822, 70, "WATCH THE LATE STAGES", "Late-stage loans are rising even as the headline eases.", 430, 22)
    foot = ("Source: Mortgage Bankers Association, National Delinquency Survey, Q2 2026 (released Aug 13, 2026); NMP, Aug 18, 2026. One-to-four-unit residential mortgages, not private loans. "
            "Year-ago bars are arithmetic: 4.37 - 0.44 = 3.93; 2.06 - 0.49 = 1.57; 0.67 - 0.19 = 0.48. bps = basis points.")
    return shell("Delinquencies eased 7 bps in Q2.", "Late-stage loans kept rising.",
                 "MBA National Delinquency Survey, second quarter 2026", b, foot, 906,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"mba-delinquency-survey": ("images/2026-10-13/1021-li-mba-delinquency-survey.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
