#!/usr/bin/env python3
"""Graphic for force-placed insurance after a hazard policy lapse (FB Thu Nov 5, 2026, 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-hazard-insurance-lapse.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def info_card(x, y, w, h, title, desc):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs lbl" style="left:20px;top:18px">{title}</div>'
            f'<div class="abs" style="left:20px;top:50px;width:{w-40}px;font-size:19px;line-height:26px;color:#F0EDE4">{desc}</div></div>')

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">Sequence for covered home mortgages</div>'
    b += step_cards([
        (1, "Coverage lapses", "The borrower policy ends or is not renewed.", None),
        (2, "Written notice", "Required before the borrower is charged.", "45 days or more"),
        (3, "Proof of coverage", "Servicer cancels the force-placed policy.", "within 15 days"),
    ], top=294, h=224)
    b += '<div class="abs lbl" style="left:68px;top:550px">What a force-placed policy is</div>'
    b += info_card(68, 582, 296, 140, "Protects", "May protect the lender more than the borrower")
    b += info_card(392, 582, 296, 140, "Coverage", "May omit personal property and liability")
    b += info_card(716, 582, 296, 140, "Cost", "Can be much more than a regular policy")
    b += panel(750, 70, "Takeaway", "Track expiration dates. Request renewal proof before a lapse.", 560, 24)
    foot = ("Sources: Progressive, Force-Placed and Lender Placed Insurance (updated 2023-08-15); CFPB, 12 CFR 1024.37 Force-placed insurance "
            "(current regulation, page undated, accessed 2026-11-01); Cornell LII, 12 CFR 1024.37 (page undated, accessed 2026-11-01). "
            "Federal servicing rules apply to covered home mortgages; loan terms vary by lender and state.")
    return shell("Borrower insurance lapses.", "What can the lender do?",
                 "Force-placed insurance, also called lender-placed", b, foot, 850,
                 eyebrow="PROTECTING THE COLLATERAL")

PAGES = {"hazard-insurance-lapse": ("images/2026-11-05/1727-fb-hazard-insurance-lapse.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
