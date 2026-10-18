#!/usr/bin/env python3
"""Graphic for usury and business-purpose loans. Run from repo root: python3 tools/weeks/2026-10-19-usury-business-purpose.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def case(x, state, switch, rows, note):
    w = 462
    b = (f'<div class="card" style="left:{x}px;top:292px;width:{w}px;height:430px">'
         f'<div class="abs mono gold" style="left:22px;top:20px;font-size:38px;line-height:46px">{state}</div>'
         f'<div class="abs lbl" style="left:22px;top:76px;font-size:13px">WHAT CHANGES THE CAP</div>'
         f'<div class="abs" style="left:22px;top:98px;width:{w-44}px;font-size:19px;line-height:25px;font-weight:700;color:#F0EDE4">{switch}</div>')
    y = 150
    for lab, val, desc in rows:
        b += (f'<div class="abs" style="left:22px;top:{y}px;width:{w-44}px;height:78px;border-radius:10px;background:rgba(11,31,58,.7);border:1px solid rgba(138,155,176,.30)">'
              f'<div class="abs mono gold" style="left:16px;top:14px;font-size:30px;line-height:36px">{val}</div>'
              f'<div class="abs steel" style="left:100px;top:15px;width:{w-44-116}px;font-size:16px;line-height:23px">{lab}<br>{desc}</div></div>')
        y += 92
    b += f'<div class="abs steel" style="left:22px;top:{y+2}px;width:{w-44}px;font-size:15px;line-height:20px">{note}</div></div>'
    return b

def gfx():
    b = case(68, "New York", "Who the borrower is",
             [("Civil cap", "16%", "Generally exempt: corporations, LLCs"),
              ("Criminal cap", "25%", "Generally still applies")],
             "Exemption does not apply where the entity owns a one or two family home as its principal asset.")
    b += case(550, "Florida", "How big the loan is",
              [("$500,000 or less", "18%", "Maximum, simple interest"),
               ("Over $500,000", "25%", "Maximum, simple interest")],
              "Above 25% is criminal usury at any loan size.")
    b += panel(752, 92, "NOT A PASS", "A business purpose does not settle it. Each state sets its own test.", 470, 28)
    foot = ("Sources: Adam Leitman Bailey, P.C., Avoiding Usury (page updated Sep 14, 2026); Bond, Schoeneck and King PLLC (Feb 22, 2022); "
            "Jimerson Birr, Mortgage and Note Default: Avoiding Usury Allegations (Sep 25, 2018). "
            "Rules vary by state and change. Not legal advice.")
    return shell("Business loan, same rate cap?", "Not in every state.", "Two states, two different tests for the usury limit", b, foot, 870)

PAGES = {"usury-business-purpose": ("images/2026-10-21/1709-li-usury-business-purpose.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
