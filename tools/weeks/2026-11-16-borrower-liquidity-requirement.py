#!/usr/bin/env python3
"""Graphic for borrower liquidity proof of funds. Run from repo root: python3 tools/weeks/2026-11-16-borrower-liquidity-requirement.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

INC, DEP = 7000, 45000

def gfx():
    line = INC * 0.5
    assert line == 3500
    base, maxh = 640, 270
    hl = maxh * line / DEP
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative statement review</div>'
    body += f'<div class="abs" style="left:68px;top:{base}px;width:520px;height:3px;background:#0B1F3A"></div>'
    body += (f'<div class="abs" style="left:110px;top:{base - maxh}px;width:150px;height:{maxh}px;border-radius:10px 10px 0 0;background:#C9A84C"></div>'
             f'<div class="abs mono gold" style="left:70px;top:{base - maxh - 44}px;width:230px;text-align:center;font-size:34px">$45,000</div>'
             f'<div class="abs steel" style="left:70px;top:{base + 12}px;width:230px;text-align:center;font-size:18px">Single large deposit</div>')
    body += (f'<div class="abs" style="left:330px;top:{base - hl:.0f}px;width:150px;height:{hl:.0f}px;border-radius:6px 6px 0 0;background:#5B7DAE"></div>'
             f'<div class="abs mono" style="left:300px;top:{base - hl - 44:.0f}px;width:210px;text-align:center;font-size:34px">$3,500</div>'
             f'<div class="abs steel" style="left:300px;top:{base + 12}px;width:210px;text-align:center;font-size:18px">50% of $7,000 a month</div>')
    body += (f'<div class="abs" style="left:68px;top:{base - hl:.0f}px;width:520px;border-top:3px dashed #9A7B22"></div>')
    cells = [("Fannie Mae", "A large deposit is a single deposit that exceeds 50% of the total monthly qualifying income for the loan."),
             ("Purchase loans", "If the funds are needed to complete the purchase, the lender must document an acceptable source."),
             ("Freddie Mac", "Defines a large deposit differently. Its own test applies, so check the current Freddie Mac text.")]
    for i, (h, d) in enumerate(cells):
        y = 320 + i * 132
        body += (f'<div class="card" style="left:630px;top:{y}px;width:382px;height:120px"><div class="abs lbl" style="left:20px;top:12px">{h}</div>'
                 f'<div class="abs" style="left:20px;top:38px;width:344px;font-size:16.5px;line-height:23px">{d}</div></div>')
    body += ('<div class="panel" style="top:736px;height:96px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:27px;color:#0B1F3A">'
             'Private lender policies may differ. Lenders may ask for documents showing the source.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "A balance is not proof", "of where the money came from",
                "How conventional lenders treat a large deposit", body,
                "Sources: Fannie Mae Selling Guide B3-4.2-02 (12/14/2022); Freddie Mac Guide section 5501.1 as reproduced at homebuyer.com (published 2026-02-24). "
                "Arithmetic: 50% x $7,000 = $3,500. Income and deposit are illustrative. Conventional purchase rules shown for context only.", 862)

PAGES = {"borrower-liquidity-requirement": ("images/2026-11-22/1015-fb-borrower-liquidity-requirement.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
