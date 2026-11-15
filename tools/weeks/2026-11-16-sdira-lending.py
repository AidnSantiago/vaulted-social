#!/usr/bin/env python3
"""Graphic for IRA lending and prohibited transactions. Run from repo root: python3 tools/weeks/2026-11-16-sdira-lending.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    body = '<div class="abs lbl" style="left:68px;top:290px">Who counts as a disqualified person (IRS)</div>'
    body += ('<div class="card" style="left:68px;top:330px;width:300px;height:250px">'
             '<div class="abs lbl" style="left:22px;top:20px">A plan</div>'
             '<div class="abs" style="left:22px;top:56px;width:256px;font-size:30px;font-weight:700;font-family:Georgia,serif">An IRA</div>'
             '<div class="abs steel" style="left:22px;top:112px;width:256px;font-size:18px;line-height:26px">The Department of Labor says the term plan includes an IRA.</div></div>')
    body += ('<div class="abs mono gold" style="left:378px;top:372px;width:150px;text-align:center;font-size:20px;line-height:26px">LOAN<br>or credit</div>'
             '<div class="abs mono gold" style="left:378px;top:430px;width:150px;text-align:center;font-size:50px;line-height:60px">&harr;</div>'
             '<div class="abs mono gold" style="left:378px;top:500px;width:150px;text-align:center;font-size:17px">prohibited</div>')
    body += ('<div class="card" style="left:538px;top:330px;width:474px;height:250px">'
             '<div class="abs lbl" style="left:22px;top:20px">A disqualified person includes</div>')
    items = ["The IRA owner's fiduciary", "Spouse", "Ancestor", "Lineal descendant", "Spouse of a lineal descendant"]
    y = 62
    for it in items:
        body += f'<div class="abs" style="left:22px;top:{y}px;font-size:21px;font-weight:700"><span class="gold">&#9632;</span>&nbsp; {it}</div>'
        y += 36
    body += '</div>'
    body += ('<div class="card" style="left:68px;top:610px;width:944px;height:96px"><div class="abs lbl" style="left:24px;top:16px">The consequence</div>'
             '<div class="abs" style="left:24px;top:44px;width:896px;font-size:19px;line-height:27px">The IRS says a disqualified person who takes part in a prohibited transaction must pay a tax.</div></div>')
    body += ('<div class="panel" style="top:736px;height:104px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">GENERAL EDUCATION</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:600px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Not tax or legal advice. Rules and exceptions vary. Consult a qualified tax or legal professional first.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Can an IRA lend to family?", "Not without a hard look",
                "Prohibited transactions, in plain terms", body,
                "Sources: 26 U.S.C. 4975(c)(1)(B), (e)(1), (e)(6) (Cornell LII; page undated, accessed 2026-11-15); IRS, Retirement topics - Prohibited transactions (updated 2026-06-27); "
                "IRS, Retirement plan investments FAQs (updated 2026-04-08); DOL EBSA Advisory Opinion 2011-04A (2011-02-03).", 880)

PAGES = {"sdira-lending": ("images/2026-11-19/1727-fb-sdira-lending.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
