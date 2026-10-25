#!/usr/bin/env python3
"""Graphic for assignment of rents (Facebook, Thu Oct 29, 2026, 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-10-26-assignment-of-rents.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">How the clause can work, in order</div>'
    b += step_cards([
        ("1", "Rents assigned", "The borrower assigns the rents to the lender and keeps a license to collect them.", None),
        ("2", "Default", "The license is revocable upon default. Enforcement may need added steps.", None),
        ("3", "Notice and tenants", "Steps may include written notice and direction letters to tenants.", None),
    ], top=298, h=214)
    b += ('<div class="card" style="left:68px;top:546px;width:944px;height:164px">'
          '<div class="abs lbl" style="left:24px;top:20px">Varies by state</div>'
          '<div class="abs" style="left:24px;top:52px;width:896px;font-size:21px;line-height:30px;color:#F0EDE4">'
          'The clause is <span class="gold">not self-executing in many states</span>. Receivership is a common enforcement tool.</div></div>')
    b += panel(742, 84, "ASK COUNSEL", "How is it enforced in the property state?", 470)
    foot = ("Sources: Cummings Law, Understanding the Rents, Issues, and Profits Clause (updated Oct 25, 2026); "
            "Jeffrey B. Steiner, DLA Piper, Assignment of Leases and Rents: Absolutely Collateral (Mar 20, 2018). "
            "Rules vary by state and by lender. General education, not legal advice.")
    return shell("Default happens. Tenants still pay.", "Who collects the rent?",
                 "What an assignment of rents is meant to do after default.", b, foot, 862)

PAGES = {"assignment-of-rents": ("images/2026-10-29/1727-fb-assignment-of-rents.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
