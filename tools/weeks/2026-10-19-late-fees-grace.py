#!/usr/bin/env python3
"""Graphic for late fees and grace periods. Run from repo root: python3 tools/weeks/2026-10-19-late-fees-grace.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def case(x, state, court, rows, verdict):
    w = 462
    b = (f'<div class="card" style="left:{x}px;top:292px;width:{w}px;height:430px">'
         f'<div class="abs mono gold" style="left:22px;top:20px;font-size:38px;line-height:46px">{state}</div>'
         f'<div class="abs steel" style="left:22px;top:70px;font-size:16px;line-height:22px;width:{w-44}px">{court}</div>')
    y = 118
    for k, v in rows:
        b += (f'<div class="abs lbl" style="left:22px;top:{y}px;font-size:13px">{k}</div>'
              f'<div class="abs" style="left:22px;top:{y+22}px;width:{w-44}px;font-size:19px;line-height:25px;font-weight:700;color:#F0EDE4">{v}</div>')
        y += 74
    b += (f'<div class="abs" style="left:22px;top:{y+4}px;width:{w-44}px;height:52px;border-radius:8px;background:rgba(201,168,76,.14);'
          f'border:1px solid rgba(201,168,76,.55);display:flex;align-items:center;padding:0 16px;color:#E2C265;font-size:17px;font-weight:700">{verdict}</div></div>')
    return b

def gfx():
    b = (f'<div class="card" style="left:68px;top:292px;width:462px;height:430px">'
         f'<div class="abs mono gold" style="left:22px;top:20px;font-size:34px;line-height:42px">The test</div>'
         f'<div class="abs steel" style="left:22px;top:70px;font-size:16px;line-height:22px;width:418px">What the court asked</div>'
         f'<div class="abs" style="left:22px;top:130px;width:418px;font-size:22px;line-height:30px;font-weight:700;color:#F0EDE4">Was the fee reasonable in light of the anticipated or actual loss caused by the late payment?</div>'
         f'<div class="abs steel" style="left:22px;top:300px;width:418px;font-size:17px;line-height:24px">A late fee written into the note can still be tested in court. Results vary by state and by the facts.</div></div>')
    b += case(550, "Arizona", "State supreme court, April 25, 2017",
              [("LATE FEE", "5% of the unpaid amount"), ("APPLIED TO", "Final balloon payment, commercial loan"),
               ("FEE AT ISSUE", "Nearly $1.4 million")], "Held unenforceable")
    b += panel(752, 92, "TAKEAWAY", "Read your own late fee clause with that test in mind.", 470, 28)
    foot = ("Sources: "
            "Dobson Bay Club II DD v. La Sonrisa de Siena, Arizona Supreme Court (decided Apr 25, 2017, via FindLaw). "
            "Court outcomes depend on the facts and state. Not legal advice.")
    return shell("A 5% late fee on a balloon,", "held a penalty.", "How one court tested a late fee against actual harm", b, foot, 870)

PAGES = {"late-fees-grace": ("images/2026-10-25/1727-fb-late-fees-grace.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
