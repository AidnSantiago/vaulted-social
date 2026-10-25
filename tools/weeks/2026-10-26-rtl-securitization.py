#!/usr/bin/env python3
"""Graphic for RTL securitization volume (KBRA), LinkedIn, Fri Oct 30, 2026 2:00 pm ET.
Run from repo root: python3 tools/weeks/2026-10-26-rtl-securitization.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SCALE = 100  # px per $1 billion


def gfx():
    b = ('<div class="abs lbl" style="left:68px;top:270px">RTL securitization issuance, billions of dollars</div>')
    rows = [("2024", 6.2, None, "$6.2B"), ("2025", 5.5, None, "$5.5B"), ("2026 projected", 4.8, 3.5, "$4.8B")]
    y = 316
    for yr, tot, rated, lab in rows:
        b += f'<div class="abs" style="left:68px;top:{y + 20}px;width:170px;font-size:21px;font-weight:700;color:#F0EDE4">{yr}</div>'
        x0 = 250
        if rated:
            w1 = round(rated * SCALE); w2 = round((tot - rated) * SCALE)
            b += (f'<div class="abs seg-gold mono" style="left:{x0}px;top:{y}px;width:{w1}px;height:62px;border-radius:8px 0 0 8px;'
                  f'display:flex;align-items:center;justify-content:center;font-size:22px">$3.5B</div>'
                  f'<div class="abs seg-steel mono" style="left:{x0 + w1}px;top:{y}px;width:{w2}px;height:62px;border-radius:0 8px 8px 0;'
                  f'display:flex;align-items:center;justify-content:center;font-size:19px">$1.3B</div>')
            b += f'<div class="abs mono gold" style="left:{x0 + w1 + w2 + 16}px;top:{y + 15}px;font-size:26px;white-space:nowrap">{lab}</div>'
        else:
            w = round(tot * SCALE)
            b += (f'<div class="abs seg-blue2" style="left:{x0}px;top:{y}px;width:{w}px;height:62px;border-radius:8px"></div>'
                  f'<div class="abs mono gold" style="left:{x0 + w + 16}px;top:{y + 15}px;font-size:26px;white-space:nowrap">{lab}</div>')
        y += 88
    b += ('<div class="abs" style="left:250px;top:582px;font-size:17px;color:#A5B2C3;white-space:nowrap">'
          '<span style="display:inline-block;width:14px;height:14px;background:#D2B058;border-radius:3px;margin-right:8px"></span>Rated, about 73% of 2026 projection'
          '<span style="display:inline-block;width:14px;height:14px;background:#5A6B82;border-radius:3px;margin:0 8px 0 28px"></span>Remainder, by subtraction</div>')
    b += stat_card(68, 640, 300, 150, "-12%", "2026 projection vs 2025", "KBRA, full-year 2026")
    b += stat_card(390, 640, 300, 150, "~73%", "rated share of 2026", "about $3.5B of $4.8B")
    b += stat_card(712, 640, 300, 150, "less than 5%", "of private-label issuance", "RTL share, 2026 expected", big_size=34)
    b += panel(812, 62, "A PROJECTION", "Full-year 2026 is a KBRA estimate, not a final count.", 560, 22)
    foot = ("Sources: KBRA, Laying the Foundation: The Evolution of RTL Lending (July 30, 2026); National Mortgage Professional, "
            "Aug. 3, 2026. 2026 is projected. Arithmetic: $4.8B less $3.5B rated = $1.3B remainder.")
    return shell("RTL securitization is projected", "at $4.8B for 2026.", "KBRA volume figures: 2024, 2025 and 2026 projected", b, foot, 898)


PAGES = {"rtl-securitization": ("images/2026-10-30/1400-li-rtl-securitization.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
