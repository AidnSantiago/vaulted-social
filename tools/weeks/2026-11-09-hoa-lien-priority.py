#!/usr/bin/env python3
"""Graphic for hoa-lien-priority (Facebook, Wed Nov 11, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-hoa-lien-priority.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def row(y, label, sub, cls, w, tcol="#0B1F3A"):
    return (f'<div class="abs {cls}" style="left:68px;top:{y}px;width:{w}px;height:64px;border-radius:8px"></div>'
            f'<div class="abs" style="left:88px;top:{y+9}px;font-size:21px;font-weight:700;color:{tcol};white-space:nowrap">{label}</div>'
            f'<div class="abs" style="left:88px;top:{y+36}px;font-size:15px;color:{tcol};white-space:nowrap">{sub}</div>')

def gfx():
    b = stat_card(68, 262, 460, 152, "Colorado", "six months of assessments", "Super-lien status, per Nolo", 40)
    b += stat_card(552, 262, 460, 152, "Nevada", "nine months of assessments", "Super-lien status, per Nolo", 40)
    b += '<div class="abs lbl" style="left:68px;top:446px">Payment order in a super-lien state (simplified)</div>'
    b += row(480, "1. HOA super-lien portion", "Ranks ahead of the first mortgage", "seg-gold", 944)
    b += row(556, "2. First mortgage", "May be eliminated if the super lien is foreclosed", "seg-blue2", 944, "#F0EDE4")
    b += row(632, "3. Rest of the HOA lien", "Ranks behind the first mortgage", "seg-steel", 944, "#F0EDE4")
    b += panel(722, 112, "Ask in diligence", "Is the property in an HOA, are assessments current, and does state law give a super lien? Varies by state.", 520, 26)
    foot = ("Sources: Nolo, Homeowners Association Super Liens (updated Aug 19, 2025); Colo. Rev. Stat. 38-33.3-316 (current through Fall 2025, accessed Nov 8, 2026); "
            "My Compliance Resource, HOA Super Lien (Sep 30, 2014). Amount covered and rules vary by state.")
    return shell("Can an HOA lien jump", "ahead of your first mortgage?", "Super liens, in plain terms", b, foot, 858, eyebrow="LIEN PRIORITY FOR LENDERS")

PAGES = {"hoa-lien-priority": ("images/2026-11-11/1727-fb-hoa-lien-priority.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
