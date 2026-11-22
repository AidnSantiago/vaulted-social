#!/usr/bin/env python3
"""Graphic for lien search vs title search basics. Run from repo root: python3 tools/weeks/2026-11-23-lien-search-vs-title-search-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    cols = [("LIEN SEARCH", "Claims against it", "Looks for liens, which are legal claims against a property to secure a debt."),
            ("TITLE SEARCH", "Who owns it", "Reviews public records to confirm the legal owner and identify issues."),
            ("TITLE COMMITMENT", "The promise", "A promise that the title insurance policy will be issued at closing.")]
    body = ""
    for i, (name, sub, desc) in enumerate(cols):
        x = 68 + i * 321
        body += (f'<div class="card" style="left:{x}px;top:296px;width:302px;height:236px">'
                 '<div class="abs" style="left:0;top:0;width:100%;height:10px;border-radius:14px 14px 0 0;background:#C9A84C"></div>'
                 f'<div class="abs lbl" style="left:22px;top:34px;font-size:15px">{name}</div>'
                 f'<div class="abs mono gold" style="left:22px;top:66px;font-size:22px;white-space:nowrap">{sub}</div>'
                 f'<div class="abs" style="left:22px;top:118px;width:258px;font-size:19px;line-height:27px">{desc}</div></div>')
    body += ('<div class="card" style="left:68px;top:560px;width:944px;height:150px">'
             '<div class="abs lbl" style="left:24px;top:18px">The gap to know about</div>'
             '<div class="abs" style="left:24px;top:50px;width:896px;font-size:19px;line-height:27px">A traditional title search only locates recorded liens. A municipal lien search can find unrecorded items such as code violations and special assessments.</div></div>')
    body += ('<div class="panel" style="top:736px;height:76px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'Lenders can ask the title company what was searched. Scope varies by state and lender.</div></div>')
    return page("light", "BASICS", "PRIVATE LENDING, EXPLAINED", "Lien search, title search", "and title commitment",
                "Three similar terms, three different jobs", body,
                "Sources: Commercial Partners (CTIC), lien searches (Mar 11, 2026); Rocket Mortgage, title search (Jul 17, 2026); Ownerly, title commitment (Jun 17, 2021); "
                "PropLogix (Aug 17, 2025; modified Jan 20, 2026); Wolters Kluwer (May 17, 2024). Educational only; not legal advice.", 836)

PAGES = {"lien-search-vs-title-search-basics": ("images/2026-11-29/1347-fb-lien-search-vs-title-search-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
