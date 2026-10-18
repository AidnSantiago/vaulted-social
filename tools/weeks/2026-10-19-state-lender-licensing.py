#!/usr/bin/env python3
"""Graphic for state-lender-licensing (LinkedIn, Fri Oct 23, 2026, 2:00 pm ET). Run from repo root: python3 tools/weeks/2026-10-19-state-lender-licensing.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def col(x, state, regulator, rows, cls):
    w, top, h = 458, 262, 430
    b = f'<div class="card" style="left:{x}px;top:{top}px;width:{w}px;height:{h}px"></div>'
    b += (f'<div class="abs {cls} mono" style="left:{x+20}px;top:{top+20}px;width:{w-40}px;height:44px;border-radius:8px;'
          f'display:flex;align-items:center;padding-left:14px;font-size:21px">{state}</div>')
    b += f'<div class="abs lbl" style="left:{x+22}px;top:{top+82}px;font-size:13px">Regulator page</div>'
    b += f'<div class="abs" style="left:{x+22}px;top:{top+104}px;width:{w-44}px;font-size:19px;line-height:25px;color:#E2C265;font-weight:700">{regulator}</div>'
    y = top + 170
    for lab, txt in rows:
        b += f'<div class="abs lbl" style="left:{x+22}px;top:{y}px;font-size:13px">{lab}</div>'
        b += f'<div class="abs" style="left:{x+22}px;top:{y+22}px;width:{w-44}px;font-size:18px;line-height:24px;color:#F0EDE4">{txt}</div>'
        y += 128 if len(rows) == 2 else 90
    return b


def gfx():
    b = col(68, "CALIFORNIA", "Dept. of Financial Protection and Innovation",
            [("License required for", "Any person engaging in the business of a finance lender"),
             ("Law says finance lender includes", "Making commercial loans. Some exemptions apply.")], "seg-gold")
    b += col(554, "FLORIDA", "Office of Financial Regulation",
             [("License required for", "An entity making a mortgage loan for compensation or gain"),
              ("Also covers", "Selling or offering to sell a mortgage loan to a noninstitutional investor")], "seg-steel")
    b += panel(716, 100, "VARIES BY STATE", "Read the regulator page. Ask counsel if a specific loan is covered.", 470, 24)
    foot = ("Sources: California DFPI, About California Financing Law (page undated, accessed Oct 18, 2026). "
            "Paul Hastings, The California Financing Law (Aug 5, 2025). "
            "Florida Office of Financial Regulation, Mortgage Lender and Branches (page undated, accessed Oct 18, 2026). Not legal advice.")
    return shell("Do you need a state", "lender license?", "Two states, two different licensing triggers", b, foot, 842)


PAGES = {"state-lender-licensing": ("images/2026-10-23/1400-li-state-lender-licensing.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
