#!/usr/bin/env python3
"""Graphic for title commitment reading basics. Run from repo root: python3 tools/weeks/2026-11-16-title-commitment-reading-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    cols = [("A", "Schedule A", "The basic facts", ["Effective date", "Who is insured", "Amount of insurance", "Current owner", "Legal description"], "#5B7DAE"),
            ("B-I", "Schedule B, Part I", "Requirements", ["Must be met before the policy is issued", "Examples: payments or documents to complete"], "#C9A84C"),
            ("B-II", "Schedule B, Part II", "Exceptions", ["Matters the policy will not cover", "An exception can cover items first showing in the public records after the commitment date"], "#3F5470")]
    body = ""
    x = 68
    for tag, t, sub, items, col in cols:
        body += (f'<div class="card" style="left:{x}px;top:290px;width:296px;height:400px">'
                 f'<div class="abs" style="left:0;top:0;width:296px;height:10px;border-radius:14px 14px 0 0;background:{col}"></div>'
                 f'<div class="abs mono gold" style="left:22px;top:32px;font-size:34px">{tag}</div>'
                 f'<div class="abs" style="left:22px;top:84px;width:252px;font-size:22px;font-weight:700">{t}</div>'
                 f'<div class="abs lbl" style="left:22px;top:118px;width:252px">{sub}</div>')
        y = 164
        for it in items:
            lines = 1 + len(it) // 24
            body += (f'<div class="abs" style="left:22px;top:{y}px;width:252px;font-size:18px;line-height:24px;color:#0B1F3A">{it}</div>')
            y += 24 * lines + 14
        body += '</div>'
        x += 324
    body += ('<div class="panel" style="top:722px;height:104px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:24px">READ ALL OF B</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:640px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Lenders can check the insured and amount in Schedule A, then read every exception. Questions can go to the title company.</div></div>')
    return page("light", "BASICS", "PRIVATE LENDING, EXPLAINED", "How to read a title commitment", "Schedule A, then both B parts",
                "Three sections, and what each one tells a lender", body,
                "Sources: First American Title, Understanding Your Title Commitment (page undated, accessed 2026-11-15); ALTA Commitment for Title Insurance form, 7-1-21 (form dated 08/10/2021, accessed 2026-11-15, via Stewart). "
                "Forms and wording vary by state and title company. Educational only; not legal advice.", 862)

PAGES = {"title-commitment-reading-basics": ("images/2026-11-22/1347-fb-title-commitment-reading-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
