#!/usr/bin/env python3
"""Graphic for portfolio-loan-meaning (Facebook, Sun Nov 15, 2026 10:15 am ET). Run from repo root: python3 tools/weeks/2026-11-09-portfolio-loan-meaning.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, title, tag, lines, accent):
    b = f'<div class="card" style="left:{x}px;top:272px;width:458px;height:400px"></div>'
    b += f'<div class="abs lbl" style="left:{x+26}px;top:296px">{tag}</div>'
    b += f'<div class="abs" style="left:{x+26}px;top:328px;font-family:Georgia,serif;font-weight:700;font-size:32px;color:{accent};white-space:nowrap">{title}</div>'
    y = 392
    for head, desc in lines:
        b += f'<div class="abs" style="left:{x+26}px;top:{y}px;font-size:21px;font-weight:700;color:#F0EDE4;white-space:nowrap">{head}</div>'
        b += f'<div class="abs" style="left:{x+26}px;top:{y+32}px;width:406px;font-size:18px;line-height:26px;color:#A5B2C3">{desc}</div>'
        y += 104
    return b

def gfx():
    b = col(68, "Sold loan", "SOLD IN THE SECONDARY MARKET", [
        ("Who holds it", "The buyer, not the original lender."),
        ("What the lender gets", "Sale proceeds, which can fund additional mortgages."),
    ], "#A5B2C3")
    b += col(554, "Portfolio loan", "KEPT ON THE LENDER'S BOOKS", [
        ("Who holds it", "The lender, as an investment asset."),
        ("What the lender gets", "Free to set terms and documentation. Takes on more risk."),
    ], "#E2C265")
    b += panel(704, 130, "Hold vs sell", "Holding lets the lender set its own terms. Selling brings proceeds that can fund additional mortgages.", 430, 26)
    foot = ("Sources: Rocket Mortgage (Quicken Loans), Portfolio Loans: Defined And Explained (published Sep 20, 2024); "
            "Experian, What Is a Portfolio Mortgage? (Apr 10, 2025). Terms vary by lender.")
    return shell("A portfolio loan stays", "on the lender's books", "Held by the lender instead of sold", b, foot, 868, eyebrow="LOAN BASICS FOR LENDERS")

PAGES = {"portfolio-loan-meaning": ("images/2026-11-15/1015-fb-portfolio-loan-meaning.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
