#!/usr/bin/env python3
"""Graphic for FHFA HPI and Case-Shiller July 2026 readings (Facebook, Tue Oct 27, 2026 9:15 am ET). Built Oct 25, 2026.
Run from repo root: python3 tools/weeks/2026-10-26-home-price-index.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    comp = 340000
    a = comp * 0.026 * 0.5
    b_ = comp * 0.06 * 0.5
    assert round(a) == 4420 and round(b_) == 10200 and round(b_ - a) == 5780
    b = '<div class="abs lbl" style="left:68px;top:268px">12-month change to July 2026, percent</div>'
    # number line 0 to 7 percent across x 100..980
    X0, X1, SC = 100, 980, 7.0
    px = lambda v: X0 + (X1 - X0) * v / SC
    b += f'<div class="abs" style="left:{X0}px;top:352px;width:{X1-X0}px;height:6px;border-radius:3px;background:#46556A"></div>'
    b += f'<div class="abs seg-blue2" style="left:{px(0.6):.0f}px;top:349px;width:{px(6.3)-px(0.6):.0f}px;height:12px;border-radius:6px"></div>'
    marks = [(0.6, "0.6", "Mountain", "seg-steel", 0), (1.9, "1.9", "Case-Shiller", "seg-blue", 0), (2.6, "2.6", "FHFA U.S.", "seg-gold", 1), (6.3, "6.3", "Middle Atlantic", "seg-steel", 0)]
    for v, t, lab, cls, up in marks:
        x = px(v)
        b += f'<div class="abs {cls} mono" style="left:{x-34:.0f}px;top:296px;width:68px;height:34px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:19px">{t}</div>'
        b += f'<div class="abs" style="left:{x-1.5:.0f}px;top:332px;width:3px;height:36px;background:#C9A84C"></div>'
    for v, lab, dy in [(0.6, "Mountain", 0), (1.9, "Case-Shiller", 0), (2.6, "FHFA U.S.", 24), (6.3, "Middle Atlantic", 0)]:
        x = px(v)
        b += f'<div class="abs steel" style="left:{x-60:.0f}px;top:{378+dy}px;width:120px;text-align:center;font-size:15px;line-height:19px">{lab}</div>'
    b += '<div class="abs lbl" style="left:68px;top:452px">Illustrative: $340,000 comp, 6-month hold</div>'
    b += stat_card(68, 488, 290, 150, "$4,420", "at the 2.6 percent pace", "340,000 x 2.6% x 6/12", 46)
    b += stat_card(395, 488, 290, 150, "$10,200", "at an assumed 6 percent", "340,000 x 6% x 6/12", 42)
    b += stat_card(722, 488, 290, 150, "$5,780", "gap in assumed value", "10,200 minus 4,420", 46)
    b += panel(670, 92, "Check comps", "Lenders can check ARV against recent comps, not only a growth rate.", 560, 26)
    foot = ("Sources: FHFA, House Price Index monthly release, Sept 29, 2026 (purchase-only, seasonally adjusted, July 2025 to July 2026); "
            "S&P Cotality Case-Shiller U.S. National Index, Sept 29, 2026 (annual gain, July 2026). Data as of July 2026. "
            "Arithmetic: 340,000 x 0.026 x 0.5 = 4,420; 340,000 x 0.06 x 0.5 = 10,200; difference 5,780. The comp, hold and 6 percent are illustrative.")
    return shell("Home prices rose 2.6 percent.", "Does your ARV assume more?",
                 "Latest FHFA and Case-Shiller readings, as of July 2026 data", b, foot, 790,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")

PAGES = {"home-price-index": ("images/2026-10-27/0915-fb-home-price-index.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
