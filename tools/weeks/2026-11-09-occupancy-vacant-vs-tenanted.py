#!/usr/bin/env python3
"""Graphic for occupancy-vacant-vs-tenanted (Facebook, Sun Nov 15, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-occupancy-vacant-vs-tenanted.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, title, rows, accent):
    h = (f'<div class="card" style="left:{x}px;top:262px;width:460px;height:400px"></div>'
         f'<div class="abs" style="left:{x}px;top:262px;width:460px;height:62px;border-radius:14px 14px 0 0" ><div class="{accent}" style="width:460px;height:62px;border-radius:14px 14px 0 0"></div></div>'
         f'<div class="abs" style="left:{x+22}px;top:278px;font-family:Georgia,serif;font-size:27px;font-weight:700;color:#0B1F3A;white-space:nowrap">{title}</div>')
    for i, (k, v) in enumerate(rows):
        y = 342 + i * 77
        h += (f'<div class="abs lbl" style="left:{x+22}px;top:{y}px;font-size:13px">{k}</div>'
              f'<div class="abs" style="left:{x+22}px;top:{y+22}px;width:416px;font-size:17px;line-height:23px;color:#E4E8EE">{v}</div>')
    return h

def gfx():
    b = col(68, "Vacant", [
        ("Lease to honor", "None. There is no tenant lease to work around."),
        ("Lease to review", "Nothing to review. Confirm it is truly vacant."),
        ("Exit timing", "No tenant notice period to run."),
        ("Questions", "Is it secured, insured and maintained?"),
    ], "seg-steel")
    b += col(552, "Tenanted", [
        ("Lease to honor", "Sale may be subject to the remaining lease term."),
        ("Residential notice", "Federal law: 90 days notice to a bona fide tenant."),
        ("Commercial rank", "A lease may rank ahead of the mortgage."),
        ("Lease review", "Term, rent, deposits, subordination, estoppel."),
    ], "seg-gold")
    b += panel(694, 118, "Ask for the lease", "Lenders can review the lease and ask for an estoppel before relying on the rent. Rules vary by state. Not legal advice.", 520, 26)
    foot = ("Sources: Starfield &amp; Smith, Best Practices: SNDA Fundamentals (Feb 22, 2017); Williams Mullen, Residential Foreclosures: Lenders Become Landlords (page undated, accessed Nov 8, 2026); "
            "Protecting Tenants at Foreclosure Act, Sec. 702 (May 20, 2009, as amended); Wealth Management, Machson (May 1, 2003).")
    return shell("Vacant or tenanted?", "What changes at foreclosure", "Two paths for the same collateral", b, foot, 840, eyebrow="OCCUPANCY AND COLLATERAL")

PAGES = {"occupancy-vacant-vs-tenanted": ("images/2026-11-15/1727-fb-occupancy-vacant-vs-tenanted.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
