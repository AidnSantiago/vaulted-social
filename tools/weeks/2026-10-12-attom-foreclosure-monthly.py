#!/usr/bin/env python3
"""Graphic for ATTOM August 2026 foreclosure report (Facebook, Wed Oct 14, 2026 8:56 am ET).
Run from repo root: python3 tools/weeks/2026-10-12-attom-foreclosure-monthly.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ROWS = [("Properties with filings", "40,277", 13, "seg-blue"),
        ("Foreclosure starts", "25,894", 7, "seg-blue2"),
        ("Bank repossessions (REO)", "5,794", 42, "seg-gold")]

def gfx():
    b = ""
    b += '<div class="abs lbl" style="left:68px;top:268px">Change from August 2025, by stage</div>'
    X0, S, H = 360, 13.2, 62   # px per percent
    y = 312
    for lab, n, pct, cls in ROWS:
        b += (f'<div class="abs" style="left:68px;top:{y}px;width:280px;height:{H}px;display:flex;flex-direction:column;justify-content:center">'
              f'<div style="font-size:19px;line-height:23px;font-weight:700">{lab}</div>'
              f'<div class="mono gold" style="font-size:17px;line-height:22px">{n} in Aug 2026</div></div>')
        b += (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{pct*S:.1f}px;height:{H}px;border-radius:0 8px 8px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:14px;font-size:22px">+{pct}%</div>')
        y += H + 26
    b += '<div class="abs" style="left:68px;top:%dpx;font-size:16px;color:#8A9BB0">Bar length is proportional to the year-over-year percent change.</div>' % (y + 2)
    b += stat_card(68, 640, 290, 150, "+22%", "REOs vs July 2026", "starts were down 3% vs July")
    b += stat_card(395, 640, 290, 150, "+1%", "filings vs July 2026", "up 13% vs a year ago")
    b += stat_card(722, 640, 290, 150, "1 in 3,569", "housing units with a filing", "ATTOM: well below historical norms", 38)
    b += panel(822, 70, "READ THE STAGES", "A total hides the mix of starts and REOs.", 430, 24)
    foot = ("Source: ATTOM, August 2026 U.S. Foreclosure Market Report (Sept 17, 2026). Percent changes are ATTOM-reported. "
            "Filings, starts and REOs are counts of properties; stages are not additive.")
    return shell("Filings up 13% in August.", "REOs up 42%, starts up 7%.",
                 "ATTOM U.S. foreclosure activity, August 2026 vs a year earlier", b, foot, 912,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"attom-foreclosure-monthly": ("images/2026-10-14/0856-fb-attom-foreclosure-monthly.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
