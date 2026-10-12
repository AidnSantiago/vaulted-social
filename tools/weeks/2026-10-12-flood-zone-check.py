#!/usr/bin/env python3
"""Graphic for flood-zone-check (FB Tue Oct 13, 2026, 5:27 pm). Run from repo root: python3 tools/weeks/2026-10-12-flood-zone-check.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def info_card(x, y, w, h, label, text):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs lbl" style="left:22px;top:18px">{label}</div>'
            f'<div class="abs" style="left:22px;top:48px;width:{w - 44}px;font-size:19px;line-height:27px;color:#F0EDE4">{text}</div></div>')


def gfx():
    b = step_cards([
        (1, "Search the address", "FEMA Flood Map Service Center, search by address or location", None),
        (2, "Read the zone", "Special flood hazard area: at least a 1% chance of flooding in any given year", None),
        (3, "Check who is bound", "The rule names regulated lenders. Others can ask counsel", None),
    ], top=262, h=196)
    b += '<div class="abs lbl" style="left:68px;top:492px">If the lender is covered and the loan is in that area</div>'
    b += info_card(68, 526, 460, 150, "Insurance amount", "At least the lesser of the loan balance or the maximum coverage available, for the loan term")
    b += info_card(552, 526, 460, 150, "What it covers", "The building and personal property securing the loan, not the land itself")
    b += panel(716, 108, "FLOOD ZONE", "Lenders can look up the zone before closing and confirm with counsel which rules apply to them.", 560, 24)
    foot = ("Sources: FEMA Flood Map Service Center (page undated, accessed 2026-10-12); FDIC Consumer Compliance Examination Manual, "
            "V-6 (updated Nov 2023); eCFR 12 CFR Part 339, current as of 2026-10-07. Insurance applies where federal flood insurance is available.")
    return shell("Is the property in", "a flood zone?", "A quick check before a loan closes", b, foot, 852)


PAGES = {"flood-zone-check": ("images/2026-10-13/1727-fb-flood-zone-check.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
