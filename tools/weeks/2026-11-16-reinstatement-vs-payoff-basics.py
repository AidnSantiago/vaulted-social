#!/usr/bin/env python3
"""Graphic for reinstatement vs payoff. Run from repo root: python3 tools/weeks/2026-11-16-reinstatement-vs-payoff-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, tag, head, big, bigcap, rows, color):
    b = (f'<div class="card" style="left:{x}px;top:296px;width:458px;height:420px">'
         f'<div class="abs" style="left:0;top:0;width:458px;height:8px;border-radius:14px 14px 0 0;background:{color}"></div>'
         f'<div class="abs lbl" style="left:24px;top:30px">{tag}</div>'
         f'<div class="abs" style="left:24px;top:60px;width:410px;font-size:24px;line-height:30px;font-weight:700">{head}</div>'
         f'<div class="abs mono gold" style="left:24px;top:132px;font-size:46px;white-space:nowrap">{big}</div>'
         f'<div class="abs steel" style="left:24px;top:192px;width:410px;font-size:16.5px;line-height:22px">{bigcap}</div>')
    y = 244
    for r in rows:
        b += (f'<div class="abs" style="left:24px;top:{y+9}px;width:8px;height:8px;border-radius:50%;background:{color}"></div>'
              f'<div class="abs" style="left:46px;top:{y}px;width:388px;font-size:18px;line-height:25px">{r}</div>')
        y += 38
    return b + '</div>'

def gfx():
    body = col(68, "Route one", "Reinstatement", "$9,000", "Illustrative quote, paid in one lump sum",
               ["Missed payments", "Late fees", "Foreclosure costs, such as attorney fees"], "#5B7DAE")
    body += col(554, "Route two", "Payoff", "$260,000+", "Illustrative balance, plus similar fees and costs",
                ["Whole unpaid principal", "Interest", "Fees and costs"], "#C9A84C")
    body += ('<div class="panel" style="top:746px;height:100px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:20px">Varies by state</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:640px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">A right to reinstate can come from state law or the loan documents. Lenders can put each figure in a written quote.</div></div>')
    foot = ("Sources: Nolo, Reinstatement vs Payoff in Foreclosure (updated Apr 1, 2025); Justia, Reinstatement and Payoff to Prevent Foreclosure (page undated, accessed 2026-11-15). "
            "Loan balance and quote are illustrative. General education, not legal advice.")
    return page("light", "BASICS", "PRIVATE LENDING, EXPLAINED", "Reinstate or pay off?", "Two ways to answer a default notice",
                "The same loan, two very different numbers", body, foot, 880)

PAGES = {"reinstatement-vs-payoff-basics": ("images/2026-11-21/1347-fb-reinstatement-vs-payoff-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
