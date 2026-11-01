#!/usr/bin/env python3
"""Graphic for bridge loan definition (Facebook, Mon Nov 2, 2026, 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-bridge-loan-definition.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def box(x, w, label, title, lines, style):
    s = (f'<div class="abs {style}" style="left:{x}px;top:330px;width:{w}px;height:190px;border-radius:14px">'
         f'<div class="abs" style="left:20px;top:18px;font-size:14.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;opacity:.85">{label}</div>'
         f'<div class="abs" style="left:20px;top:48px;font-size:25px;font-weight:700;white-space:nowrap">{title}</div>')
    for i, l in enumerate(lines):
        s += f'<div class="abs" style="left:20px;top:{92 + i*28}px;font-size:18px;white-space:nowrap;opacity:.92">{l}</div>'
    return s + '</div>'

def gfx():
    b = box(68, 270, "The gap", "Not yet eligible", ["Needs improvements", "or stabilization first"], "seg-steel")
    b += box(405, 270, "The bridge", "Short-term loan", ["Covers the temporary", "gap in funding"], "seg-gold")
    b += box(742, 270, "The exit", "Permanent loan", ["Refinance into longer-", "term financing"], "seg-blue")
    for x in (339, 676):
        b += ('<svg class="abs" style="left:%dpx;top:415px" width="29" height="20" viewBox="0 0 29 20"><path d="M2 10 H24 M17 3 L25 10 L17 17" fill="none" stroke="#C9A84C" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>' % x)
    b += ('<div class="card" style="left:68px;top:556px;width:944px;height:170px">'
          '<div class="abs lbl" style="left:24px;top:20px">How long can a bridge loan run?</div>'
          '<div class="abs" style="left:24px;top:52px;width:896px;font-size:20px;line-height:30px;color:#F0EDE4">'
          'PNC: <span class="gold">a few months to one year</span> is the typical range.</div>'
          '<div class="abs" style="left:24px;top:90px;width:896px;font-size:20px;line-height:30px;color:#F0EDE4">'
          'Adventures in CRE: <span class="gold">a few months to several years</span>.</div>'
          '<div class="abs" style="left:24px;top:128px;font-size:15px;color:#8A9BB0">Terms vary by lender.</div></div>')
    b += panel(758, 84, "THE EXIT", "Lenders can ask how the loan gets paid off before they fund.", 470, 28)
    foot = ("Sources: Adventures in CRE, Bridge Loan glossary (updated Jul 2, 2025); PNC, What Is a Bridge Loan? (Apr 7, 2025). "
            "Terms and practice vary by lender. General education, not legal or investment advice.")
    return shell("A short loan for a gap.", "Then a permanent loan.",
                 "What a bridge loan bridges, and where it ends.", b, foot, 876)

PAGES = {"bridge-loan-definition": ("images/2026-11-02/1727-fb-bridge-loan-definition.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
