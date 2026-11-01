#!/usr/bin/env python3
"""Graphic for debt yield (FB Sat Nov 7, 2026, 1:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-debt-yield.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

A_NOI, A_LOAN, B_NOI, B_LOAN = 96000, 1200000, 84000, 1000000
assert A_NOI / A_LOAN == 0.08 and round(B_NOI / B_LOAN * 100, 1) == 8.4

def col(x, title, rows, cls):
    w = 456
    b = f'<div class="card" style="left:{x}px;top:262px;width:{w}px;height:312px"></div>'
    b += f'<div class="abs {cls} mono" style="left:{x+20}px;top:280px;padding:8px 14px;border-radius:8px;font-size:18px;white-space:nowrap">{title}</div>'
    y = 336
    for lab, val, big in rows:
        b += f'<div class="abs" style="left:{x+20}px;top:{y}px;font-size:17px;color:#A5B2C3;white-space:nowrap">{lab}</div>'
        b += f'<div class="abs mono {"gold" if big else ""}" style="left:{x+20}px;top:{y+22}px;font-size:{44 if big else 28}px;line-height:46px;white-space:nowrap">{val}</div>'
        y += 70 if not big else 80
    return b

def use(x, title, desc, cls):
    return (f'<div class="card" style="left:{x}px;top:608px;width:290px;height:120px"></div>'
            f'<div class="abs {cls} mono" style="left:{x+16}px;top:622px;padding:4px 10px;border-radius:6px;font-size:16px;white-space:nowrap">{title}</div>'
            f'<div class="abs" style="left:{x+16}px;top:662px;width:258px;font-size:16px;line-height:23px;color:#A5B2C3">{desc}</div>')

def gfx():
    b = col(68, "Property A", [("NOI", "$96,000", False), ("Loan", "$1,200,000", False), ("Debt yield", "8%", True)], "seg-steel")
    b += col(556, "Property B", [("NOI", "$84,000", False), ("Loan", "$1,000,000", False), ("Debt yield", "8.4%", True)], "seg-gold")
    b += use(68, "DSCR", "Depends on the interest rate and amortization schedule", "seg-blue")
    b += use(395, "LTV", "Depends on the appraised value", "seg-blue")
    b += use(722, "Debt yield", "Depends only on NOI and loan amount", "seg-gold")
    b += panel(758, 92, "NOI / loan = debt yield", "Less NOI, yet the higher debt yield: B has less loan per dollar of income.", 430, 24)
    foot = ("Sources: Lev, What is Debt Yield (2026-05-11); Wall Street Prep, Debt Yield (updated 2024-02-27). "
            "Arithmetic: 96,000 / 1,200,000 = 8%; 84,000 / 1,000,000 = 8.4%. Example is illustrative.")
    return shell("Less income, higher debt yield?", "Compare two loan requests", "Debt yield is NOI divided by the loan amount", b, foot, 874,
                 eyebrow="UNDERWRITING FOR PRIVATE LENDERS")

PAGES = {"debt-yield": ("images/2026-11-07/1347-fb-debt-yield.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
