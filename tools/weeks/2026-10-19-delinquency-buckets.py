#!/usr/bin/env python3
"""Graphic for delinquency buckets. Run from repo root: python3 tools/weeks/2026-10-19-delinquency-buckets.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">Reported as late buckets</div>'
    cols = [("30 to 59", "days late", "first late bucket", "seg-blue"),
            ("60 to 89", "days late", "second late bucket", "seg-blue2"),
            ("90+", "days late", "oldest late bucket", "seg-gold")]
    x = 68
    for big, unit, note, cls in cols:
        b += (f'<div class="abs {cls}" style="left:{x}px;top:304px;width:305px;height:190px;border-radius:14px">'
              f'<div class="abs mono" style="left:22px;top:26px;font-size:44px;line-height:52px;white-space:nowrap">{big}</div>'
              f'<div class="abs" style="left:22px;top:86px;font-size:22px;font-weight:700">{unit}</div>'
              f'<div class="abs" style="left:22px;top:130px;font-size:18px;line-height:24px">{note}</div></div>')
        x += 320
    b += ('<div class="abs" style="left:68px;top:508px;width:944px;font-size:17px;color:#A5B2C3">'
          'Length of delinquency is set by the number of missed payments (MBA).</div>')
    b += ('<div class="abs" style="left:68px;top:560px;width:944px;height:170px;border-radius:14px;border:1.5px dashed rgba(138,155,176,.7);background:rgba(22,30,42,.6)">'
          '<div class="abs lbl" style="left:26px;top:20px;color:#8A9BB0">Counted separately</div>'
          '<div class="abs" style="left:26px;top:52px;font-size:30px;font-weight:700;font-family:Georgia,serif">Loans in the foreclosure process</div>'
          '<div class="abs" style="left:26px;top:98px;width:890px;font-size:19px;line-height:26px;color:#A5B2C3">'
          'Left out of the 30, 60 and 90+ buckets. Reported on their own as foreclosure starts and foreclosure inventory.</div></div>')
    b += panel(762, 96, "CHECK THE CUT-OFFS", "Write down how your reports bucket loans and whether foreclosure is counted.", 520, 24)
    foot = ("Source: Mortgage Bankers Association, National Delinquency Survey FAQ (page undated, accessed 2026-10-18); "
            "MBA Newslink, Aug 14, 2023. MBA survey covers residential mortgages, not private loans.")
    return shell("Late is not one number.", "Know the bucket and the cut-off.",
                 "How the MBA sorts delinquent loans", b, foot, 886,
                 eyebrow="PRIVATE LENDING, EXPLAINED")

PAGES = {"delinquency-buckets": ("images/2026-10-24/0932-fb-delinquency-buckets.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
