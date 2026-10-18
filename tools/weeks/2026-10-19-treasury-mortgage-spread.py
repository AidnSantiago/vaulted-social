#!/usr/bin/env python3
"""Graphic for 10-year Treasury vs 30-year mortgage rate spread (Facebook, Tue Oct 20, 2026 9:15 am ET). Built Oct 18, 2026.
Run from repo root: python3 tools/weeks/2026-10-19-treasury-mortgage-spread.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert round(7.40 - 5.10, 2) == 2.30
    b = '<div class="abs lbl" style="left:68px;top:268px">Percent, as of October 15, 2026</div>'
    X0, S, H = 300, 85, 52   # px per percentage point
    rows = [("10-year Treasury", 5.10, "seg-blue"), ("30-year mortgage", 7.40, "seg-gold")]
    y = 312
    for lab, v, cls in rows:
        b += f'<div class="abs" style="left:68px;top:{y}px;height:{H}px;display:flex;align-items:center;font-size:19px;font-weight:700">{lab}</div>'
        b += (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{v*S:.1f}px;height:{H}px;border-radius:0 6px 6px 0;'
              f'display:flex;align-items:center;justify-content:flex-end;padding-right:12px;font-size:21px">{v:.2f}</div>')
        y += H + 22
    b += '<div class="abs lbl" style="left:68px;top:476px">The spread</div>'
    b += stat_card(68, 510, 290, 150, "2.30 pts", "mortgage minus Treasury", "7.40 - 5.10 = 230 basis points", 40)
    b += stat_card(395, 510, 290, 150, "100-300", "basis points, since 2000", "Boston Fed, May 19, 2026", 40)
    b += stat_card(722, 510, 290, 150, "$51", "less per month", "illustrative, $300,000 loan", 46)
    b += panel(700, 96, "7.40 to 7.15", "Illustrative: gap held at 2.30, 10-year down 0.25. Payment $2,077 to $2,026, 30-year amortization.", 560, 26)
    foot = ("Sources: Freddie Mac PMMS, 30-year fixed average as of Oct 15, 2026 (page undated, accessed Oct 18, 2026); FRED series DGS10, Oct 15, 2026 "
            "(updated Oct 16, 2026); Federal Reserve Bank of Boston, May 19, 2026. Payments computed on $300,000 over 30 years; the 0.25 move is illustrative.")
    return shell("The mortgage rate sits 2.30 points", "above the 10-year Treasury.",
                 "What the gap means for refinance exits", b, foot, 826,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"treasury-mortgage-spread": ("images/2026-10-20/0915-fb-treasury-mortgage-spread.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
