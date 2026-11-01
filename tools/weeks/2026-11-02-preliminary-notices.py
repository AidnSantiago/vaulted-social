#!/usr/bin/env python3
"""Graphic for preliminary notices (FB Fri Nov 6, 2026, 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-preliminary-notices.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">Two states, two windows (varies by state)</div>'
    b += stat_card(68, 296, 460, 200, "20 days", "California notice deadline", "After first furnishing work. Recipients include the construction lender, if any", 54)
    b += stat_card(552, 296, 460, 200, "31 days", "Nevada lien right look-back", "Covers work in the 31 days before the notice is given", 54)
    b += '<div class="abs lbl" style="left:68px;top:520px">What a lender can do when one arrives</div>'
    items = [("1", "Log the date", "Record when each notice arrives."),
             ("2", "Match the name", "Compare the sender to draw request names."),
             ("3", "Ask the borrower", "Confirm that party is under contract.")]
    for i, (n, t, d) in enumerate(items):
        x = 68 + i * 324
        b += (f'<div class="card" style="left:{x}px;top:552px;width:296px;height:150px">'
              f'<div class="num">{n}</div><div class="ctitle" style="top:68px">{t}</div>'
              f'<div class="cdesc" style="top:100px;width:256px">{d}</div></div>')
    b += panel(734, 70, "Takeaway", "A notice can signal that a lien claim may follow.", 520, 24)
    foot = ("Sources: Cal. Civil Code 8200 and 8204 via California Public Law and Justia (2010 text; Public Law page verified 2026-10-26); "
            "BayLegal (2026-04-20); NRS 108.245 via Nevada Public Law (2025-05-26) and Justia (2025 NRS). "
            "Rules, deadlines and recipients vary by state. Not legal advice.")
    return shell("A sub sends a preliminary notice.", "What can the lender do?",
                 "Deadlines vary by state", b, foot, 840, eyebrow="PROTECTING THE COLLATERAL")

PAGES = {"preliminary-notices": ("images/2026-11-06/1727-fb-preliminary-notices.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
