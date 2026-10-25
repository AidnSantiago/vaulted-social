#!/usr/bin/env python3
"""Graphic for subordination basics (Facebook, Wed Oct 28, 2026, 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-10-26-subordination-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def row(x, y, w, rank, title, sub, style):
    return (f'<div class="abs {style}" style="left:{x}px;top:{y}px;width:{w}px;height:92px;border-radius:12px">'
            f'<div class="abs mono" style="left:18px;top:0;height:92px;display:flex;align-items:center;font-size:30px">{rank}</div>'
            f'<div class="abs" style="left:64px;top:16px;font-size:22px;font-weight:700;white-space:nowrap">{title}</div>'
            f'<div class="abs" style="left:64px;top:50px;font-size:16px;white-space:nowrap;opacity:.9">{sub}</div></div>')

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:272px">Before</div>'
    b += '<div class="abs lbl" style="left:556px;top:272px">After the subordination agreement</div>'
    W = 456
    b += row(68, 306, W, "1", "Existing first lien", "ranks first", "seg-blue")
    b += row(68, 410, W, "2", "Second lien", "paid after the first lien", "seg-steel")
    b += row(556, 306, W, "1", "New refinance loan", "moves into first position", "seg-gold")
    b += row(556, 410, W, "2", "Second lien, subordinated", "lowered so the new loan moves ahead", "seg-steel")
    b += ('<svg class="abs" style="left:526px;top:392px" width="29" height="20" viewBox="0 0 29 20"><path d="M2 10 H24 M17 3 L25 10 L17 17" fill="none" stroke="#C9A84C" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    b += ('<div class="card" style="left:68px;top:530px;width:944px;height:214px">'
          '<div class="abs lbl" style="left:24px;top:20px">Why the second lender is asked</div>'
          '<div class="abs" style="left:24px;top:52px;width:896px;font-size:21px;line-height:30px;color:#F0EDE4">'
          'If it does not sign, the new lender <span class="gold">might not refinance</span>.</div>'
          '<div class="abs lbl" style="left:24px;top:108px">What the second lender gives up</div>'
          '<div class="abs" style="left:24px;top:140px;width:896px;font-size:21px;line-height:30px;color:#F0EDE4">'
          'Subordinate liens <span class="gold">might not get paid</span> after a foreclosure.</div></div>')
    b += panel(764, 84, "BEFORE SIGNING", "Lenders can check what sits ahead of their lien.", 470)
    foot = ("Sources: Nolo, What a Subordination Agreement Means for Your Mortgage Refinance (updated Nov 9, 2023); "
            "Barnes Walker, Subordination Agreement (page undated, accessed Oct 25, 2026). "
            "Rules and practice vary by state and by lender. General education, not legal advice.")
    return shell("One lien steps back.", "So another can move ahead.",
                 "What a subordination agreement does, and why a lender is asked.", b, foot, 876)

PAGES = {"subordination-basics": ("images/2026-10-28/1727-fb-subordination-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
