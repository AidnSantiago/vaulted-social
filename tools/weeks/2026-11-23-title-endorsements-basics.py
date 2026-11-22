#!/usr/bin/env python3
"""Graphic for title endorsements basics. Run from repo root: python3 tools/weeks/2026-11-23-title-endorsements-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    body = ('<div class="card" style="left:68px;top:290px;width:944px;height:84px"><div class="abs lbl" style="left:24px;top:16px">Base policy</div>'
            '<div class="abs" style="left:24px;top:42px;width:896px;font-size:19px;color:#3F5470">An endorsement is attached to the policy. It adds to or limits coverage.</div></div>')
    rows = [("SURVEY", "ALTA 25", "Same as survey", "Covers a difference between the insured land and a survey. Generally needs an ALTA survey."),
            ("ACCESS", "ALTA 17", "Access and entry", "Without it, a policy does not insure a particular means of access."),
            ("COMPREHENSIVE", "ALTA 9 series", "Restrictions and encroachments", "Can cover violations of restrictions and encroachments.")]
    y = 396
    for name, code, sub, desc in rows:
        body += (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:122px">'
                 '<div class="abs" style="left:0;top:0;width:10px;height:100%;border-radius:14px 0 0 14px;background:#C9A84C"></div>'
                 f'<div class="abs lbl" style="left:34px;top:18px;font-size:16px">{name}</div>'
                 f'<div class="abs mono gold" style="left:34px;top:48px;font-size:26px;white-space:nowrap">{code}</div>'
                 f'<div class="abs steel" style="left:34px;top:88px;font-size:16px;white-space:nowrap">{sub}</div>'
                 f'<div class="abs" style="left:350px;top:0;height:100%;width:560px;display:flex;align-items:center;font-size:20px;line-height:28px">{desc}</div></div>')
        y += 134
    body += ('<div class="panel" style="top:822px;height:76px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'Lenders can ask the title company which endorsements fit the property. Availability varies by state.</div></div>')
    return page("light", "BASICS", "PRIVATE LENDING, EXPLAINED", "Title endorsements", "add-ons to the base policy",
                "Three a lender can ask about, in plain English", body,
                "Sources: Williams Mullen, Title Endorsement Basics (Nov 18, 2024); American Association of Private Lenders, Title Policy Endorsements 101 (Nov 6, 2020); "
                "Old Republic Title, ALTA Endorsements Guide (Mar 2026). Educational only; not legal advice.", 924)

PAGES = {"title-endorsements-basics": ("images/2026-11-28/1347-fb-title-endorsements-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
