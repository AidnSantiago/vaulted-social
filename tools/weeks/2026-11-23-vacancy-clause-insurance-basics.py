#!/usr/bin/env python3
"""Graphic for vacancy clause basics. Run from repo root: python3 tools/weeks/2026-11-23-vacancy-clause-insurance-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, LOSS = 175000, 43750
pct = LOSS / LOAN * 100

def gfx():
    assert pct == 25
    track = 944
    w = track * LOSS / LOAN
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative: $175,000 loan, $43,750 water damage claim</div>'
    body += f'<div class="abs" style="left:68px;top:330px;width:{track}px;height:70px;border-radius:10px;background:#5B7DAE"></div>'
    body += f'<div class="abs" style="left:68px;top:330px;width:{w:.0f}px;height:70px;border-radius:10px 0 0 10px;background:#C9A84C"></div>'
    body += '<div class="abs mono" style="left:88px;top:352px;font-size:24px;color:#0B1F3A">$43,750</div>'
    body += f'<div class="abs mono" style="left:{68+w+24:.0f}px;top:352px;font-size:24px;color:#fff">$175,000 loan balance</div>'
    body += '<div class="abs steel" style="left:68px;top:412px;font-size:18px">If the insurer limits or excludes the loss, that part may go unpaid: 25 percent of the loan.</div>'
    cells = [("The clause", "A hazard policy may limit or exclude some losses once a property has been vacant a stated number of consecutive days."),
             ("The losses", "Sources name vandalism, broken glass and water damage as examples that may be affected."),
             ("The renovation", "Whether a rehab counts as vacant depends on the policy wording.")]
    for i, (h, d) in enumerate(cells):
        x = 68 + i * 321
        body += (f'<div class="card" style="left:{x}px;top:470px;width:302px;height:210px"><div class="abs lbl" style="left:20px;top:18px">{h}</div>'
                 f'<div class="abs" style="left:20px;top:52px;width:262px;font-size:18px;line-height:26px">{d}</div></div>')
    body += ('<div class="panel" style="top:710px;height:110px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'Lenders can ask for the policy vacancy wording and whether an endorsement or other coverage fits the project. Wording varies by policy.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Vacant during the rehab?", "check the clause",
                "What a vacancy clause can do to a claim, with an example", body,
                "Sources: NerdWallet, Unoccupied and Vacant Home Insurance (updated Apr 17, 2026); PropertyCasualty360, Policy Definitions of Vacancy and Occupancy (republished Jun 17, 2021). "
                "Arithmetic: 43,750 / 175,000 = 25%. Loan and claim amounts illustrative.", 880)

PAGES = {"vacancy-clause-insurance-basics": ("images/2026-11-23/1727-fb-vacancy-clause-insurance-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
