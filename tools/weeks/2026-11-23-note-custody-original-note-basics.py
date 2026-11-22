#!/usr/bin/env python3
"""Graphic for original note custody basics. Run from repo root: python3 tools/weeks/2026-11-23-note-custody-original-note-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    body = '<div class="abs lbl" style="left:68px;top:290px">UCC 3-309: what a lender without the note must show</div>'
    cells = [("1", "Was entitled", "The lender was entitled to enforce the note when possession was lost, or acquired it from someone who was."),
             ("2", "Not given away", "The loss was not a transfer by the lender or a lawful seizure."),
             ("3", "Cannot get it back", "The note was destroyed, cannot be located, or is held by someone who cannot be found.")]
    for i, (n, h, d) in enumerate(cells):
        x = 68 + i * 321
        body += (f'<div class="card" style="left:{x}px;top:326px;width:302px;height:250px">'
                 f'<div class="abs mono gold" style="left:20px;top:16px;font-size:32px">{n}</div>'
                 f'<div class="abs" style="left:20px;top:66px;width:262px;font-size:22px;font-weight:700">{h}</div>'
                 f'<div class="abs" style="left:20px;top:102px;width:262px;font-size:18px;line-height:26px">{d}</div></div>')
    body += ('<div class="card" style="left:68px;top:604px;width:458px;height:150px"><div class="abs lbl" style="left:22px;top:18px">Then it must prove</div>'
             '<div class="abs" style="left:22px;top:48px;width:414px;font-size:19px;line-height:27px">The terms of the note and its right to enforce it.</div></div>')
    body += ('<div class="card" style="left:554px;top:604px;width:458px;height:150px"><div class="abs lbl" style="left:22px;top:18px">And the court must find</div>'
             '<div class="abs" style="left:22px;top:48px;width:414px;font-size:19px;line-height:27px">The borrower is adequately protected against a claim by someone else.</div></div>')
    body += ('<div class="panel" style="top:780px;height:84px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">Know where it sits</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:560px;display:flex;align-items:center;font-size:18px;line-height:25px;color:var(--s)">Rules vary by state. Lenders can log where each original is held.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Where is the original note?", "Losing it adds a hurdle",
                "A lost note can still be enforced, with proof", body,
                "Sources: Cornell Law School LII, UCC 3-309 (page undated, accessed 2026-11-22); UNC School of Government, Dude, Where is My Note? (updated 2018-10-02).", 900)

PAGES = {"note-custody-original-note-basics": ("images/2026-11-27/0800-fb-note-custody-original-note-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
