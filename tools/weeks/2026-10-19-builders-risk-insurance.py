#!/usr/bin/env python3
"""Graphic for builder's risk vs standard policy on rehab/vacant property (Facebook, Sat Oct 24, 2026 5:27 pm ET).
Run from repo root: python3 tools/weeks/2026-10-19-builders-risk-insurance.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, title, tag, lines, cls):
    h = (f'<div class="card" style="left:{x}px;top:300px;width:290px;height:410px">'
         f'<div class="abs {cls}" style="left:0;top:0;width:290px;height:8px;border-radius:14px 14px 0 0"></div>'
         f'<div class="abs lbl" style="left:20px;top:30px">{tag}</div>'
         f'<div class="abs" style="left:20px;top:56px;width:250px;font-size:23px;line-height:28px;font-weight:700;color:#F0EDE4">{title}</div>')
    y = 112
    for ln in lines:
        h += f'<div class="abs" style="left:20px;top:{y}px;width:250px;font-size:17px;line-height:24px;color:#A5B2C3">{ln}</div>'
        y += 98
    return h + '</div>'

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">Three policy types a lender may see on a rehab file</div>'
    b += col(68, "Standard homeowners", "Occupied homes",
             ["Designed for homes occupied on a regular basis", "Vacancy limits typically start after 30 or 60 consecutive days", "Under renovation may not count as vacant"], "seg-steel")
    b += col(395, "Vacant or unoccupied", "Add-on or separate",
             ["May be needed if the owner moves out during work", "Can sometimes be added to the existing policy", "Terms vary by insurer"], "seg-blue2")
    b += col(722, "Builder&#39;s risk", "Project policy",
             ["Written for the timeline of a construction or renovation project", "Covers direct physical loss from covered perils", "Perils and limits vary by policy"], "seg-gold")
    b += panel(740, 100, "ASK", "Lenders can request the actual policy form and confirm with the insurer which coverage applies during the work.", 640, 30)
    foot = ("Sources: NerdWallet, unoccupied and vacant home insurance (updated Apr. 17, 2026); This Old House (updated Jun. 5, 2026); "
            "HUB International, builders risk FAQ (page undated, accessed Oct. 18, 2026); Eshoo, Property Insurance Coverage Law (Oct. 8, 2018).")
    return shell("Rehab or empty? The standard", "policy may not fit.",
                 "Check which coverage applies while the property is under work", b, foot, 876,
                 eyebrow="INSURANCE, EXPLAINED")

PAGES = {"builders-risk-insurance": ("images/2026-10-24/1727-fb-builders-risk-insurance.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
