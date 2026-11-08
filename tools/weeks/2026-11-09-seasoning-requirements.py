#!/usr/bin/env python3
"""Graphic for seasoning-requirements (Facebook, Thu Nov 12, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-seasoning-requirements.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def cmp_card(x, y, w, h, tag, title, lines, accent):
    b = (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-color:{accent}">'
         f'<div class="abs lbl" style="left:22px;top:20px">{tag}</div>'
         f'<div class="abs" style="left:22px;top:52px;width:{w-44}px;font-size:25px;line-height:30px;font-weight:700;color:#F0EDE4">{title}</div>'
         f'<div class="abs" style="left:22px;top:128px;width:{w-44}px;font-size:17px;line-height:25px;color:#A5B2C3">{lines}</div></div>')
    return b

def gfx():
    b = stat_card(68, 262, 460, 152, "6 months", "Fannie Mae cash-out refinance", "On title before the new loan", 40)
    b += stat_card(552, 262, 460, 152, "3 to 6 months", "Some DSCR lenders", "Before they use current value; varies by lender", 40)
    b += '<div class="abs lbl" style="left:68px;top:446px">What value can the exit lender count?</div>'
    b += cmp_card(68, 482, 460, 228, "Inside the window", "Lower of appraised value or purchase price",
                  "Many lenders size the loan this way, so a rehab gain may not count yet.", "rgba(138,155,176,.55)")
    b += cmp_card(552, 482, 460, 228, "After the window", "Current appraised value",
                  "Once the seasoning period has passed, lenders use the appraisal.", "rgba(201,168,76,.7)")
    b += panel(738, 100, "Ask early", "What seasoning will the exit lender require? Rules vary by lender.", 500, 28)
    foot = ("Sources: Fannie Mae Selling Guide B2-1.3-03 (12/10/2025, accessed Nov 8, 2026); Axiant Partners, DSCR Loans With No Seasoning "
            "(updated Sep 2, 2026); Lendmire, DSCR seasoning (Oct 15, 2026). Seasoning is lender policy and varies by lender.")
    return shell("What is seasoning, and why", "does it shape your exit?", "Time owned can decide the value a lender counts", b, foot, 862, eyebrow="REFINANCE EXITS, EXPLAINED")

PAGES = {"seasoning-requirements": ("images/2026-11-12/1727-fb-seasoning-requirements.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
