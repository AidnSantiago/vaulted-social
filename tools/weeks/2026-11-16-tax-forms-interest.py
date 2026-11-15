#!/usr/bin/env python3
"""Graphic for IRS forms and interest. Run from repo root: python3 tools/weeks/2026-11-16-tax-forms-interest.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    assert 12000 > 1500 and 12000 > 600
    body = ('<div class="card" style="left:68px;top:290px;width:944px;height:96px">'
            '<div class="abs lbl" style="left:24px;top:16px">Illustrative</div>'
            '<div class="abs mono gold" style="left:24px;top:42px;font-size:36px">$12,000</div>'
            '<div class="abs" style="left:250px;top:0;height:100%;width:660px;display:flex;align-items:center;font-size:20px;line-height:27px">of interest received in a year. Which IRS forms may be involved?</div></div>')
    cols = [("FORM 1099-INT", "$600 or more", "Other interest paid to you by a business is reported to you on this form at $600 or more."),
            ("FORM 1098", "$600 or more", "Filed by someone in a trade or business who receives $600 or more of mortgage interest from an individual."),
            ("SCHEDULE B", "Over $1,500", "Part I is required if you had over $1,500 of taxable interest or ordinary dividends, among other cases.")]
    for i, (h, big, d) in enumerate(cols):
        x = 68 + i * 321
        body += (f'<div class="card" style="left:{x}px;top:416px;width:302px;height:290px"><div class="abs lbl" style="left:20px;top:20px">{h}</div>'
                 f'<div class="abs mono gold" style="left:20px;top:56px;font-size:30px">{big}</div>'
                 f'<div class="abs" style="left:20px;top:112px;width:262px;font-size:18px;line-height:26px">{d}</div></div>')
    body += ('<div class="panel" style="top:732px;height:130px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;line-height:30px">REPORT IT<br>EITHER WAY</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:640px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">The IRS says you must report all interest even without a Form 1099-INT. Which forms apply varies by situation. Ask your accountant.</div></div>')
    return page("light", "TAX BASICS", "PRIVATE LENDING, EXPLAINED", "Interest received?", "Three IRS forms to know",
                "General education, not tax advice", body,
                "Sources: IRS Instructions for Forms 1099-INT and 1099-OID (rev. 01/2024, updated 2026-04-30); IRS Instructions for Form 1098 (updated 2026-04-30); IRS Topic no. 403 (updated 2026-10-07); IRS Publication 550 (for 2025 returns; page undated, accessed 2026-11-15). $12,000 is illustrative.", 890)

PAGES = {"tax-forms-interest": ("images/2026-11-18/1727-fb-tax-forms-interest.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
