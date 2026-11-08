#!/usr/bin/env python3
"""Graphic for asset-based lending. Run from repo root: python3 tools/weeks/2026-11-09-asset-based-lending.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def card(x, y, w, h, tag, head, items, gold=False):
    c = "#E2C265" if gold else "#F0EDE4"
    s = (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
         f'<div class="abs lbl" style="left:24px;top:22px;font-size:13px">{tag}</div>'
         f'<div class="abs mono" style="left:24px;top:50px;width:{w-48}px;font-size:24px;line-height:30px;color:{c}">{head}</div>')
    yy = 100
    for it in items:
        s += f'<div class="abs" style="left:24px;top:{yy}px;width:{w-48}px;font-size:21px;line-height:26px;font-weight:700;color:#F0EDE4">{it}</div>'
        yy += 40
    return s + '</div>'

def gfx():
    b = card(68, 272, 450, 230, "Looks mainly at", "ASSET-BASED", ["The collateral", "Not primarily the borrower"], True)
    b += card(562, 272, 450, 230, "Is more concerned with", "CONVENTIONAL", ["Credit record", "Income", "Balance sheet and cash flow"])
    b += ('<div class="card" style="left:68px;top:528px;width:944px;height:130px">'
          '<div class="abs lbl" style="left:24px;top:20px;font-size:13px">Consumer loans secured by a dwelling</div>'
          '<div class="abs" style="left:24px;top:52px;width:896px;font-size:19px;line-height:27px;color:#F0EDE4">Federal rules require a good faith ability-to-repay determination that considers income or assets other than the home. Business purpose loans are outside that rule.</div></div>')
    b += panel(684, 92, "THE PROPERTY CARRIES THE FILE", "Rules vary by state<br>and by loan purpose.", 300, 24)
    foot = ("Sources: Hammerle Morris Law Firm, What is Asset-Based Lending in Real Estate? (2020-04-02); U.S. Small Business Administration, Asset-Based Lending "
            "(2017-12-31): a loan secured by collateral; CFPB, Regulation Z 1026.43 (page undated, accessed 2026-11-08). Not legal advice.")
    return shell("Asset-based lending:", "the collateral leads.", "Underwriting focus: the property first, the borrower second.", b, foot, 808)

PAGES = {"asset-based-lending": ("images/2026-11-14/0932-fb-asset-based-lending.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
