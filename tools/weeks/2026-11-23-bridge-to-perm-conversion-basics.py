#!/usr/bin/env python3
"""Graphic for bridge-to-perm takeout checks. Run from repo root: python3 tools/weeks/2026-11-23-bridge-to-perm-conversion-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

APPR, CAP, PAYOFF = 430000, 0.75, 335000
RENT, PITIA = 2650, 2850
CEIL = round(APPR * CAP)
GAP = PAYOFF - CEIL
DSCR = round(RENT / PITIA, 2)

def gfx():
    assert (CEIL, GAP, DSCR) == (322500, 12500, 0.93)
    b = '<div class="abs lbl" style="left:68px;top:290px">Illustrative: $335,000 bridge payoff, 12 months</div>'
    def card(x, n, title, f1, f2, f3, result, bad):
        c = (f'<div class="card" style="left:{x}px;top:330px;width:458px;height:330px">'
             f'<div class="abs mono" style="left:22px;top:20px;width:44px;height:44px;border-radius:50%;background:#C9A84C;color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:21px">{n}</div>'
             f'<div class="abs" style="left:82px;top:20px;height:44px;display:flex;align-items:center;font-size:26px;font-weight:700;color:#0B1F3A">{title}</div>'
             f'<div class="abs steel" style="left:22px;top:84px;width:414px;font-size:18px;line-height:25px;color:#3F5470">{f1}</div>'
             f'<div class="abs mono" style="left:22px;top:148px;width:414px;font-size:21px;line-height:30px;color:#0B1F3A">{f2}</div>'
             f'<div class="abs steel" style="left:22px;top:206px;width:414px;font-size:18px;line-height:25px;color:#3F5470">{f3}</div>'
             f'<div class="abs" style="left:22px;top:262px;width:414px;height:48px;border-radius:10px;background:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700;color:#E2C265">{result}</div></div>')
        return c
    b += card(68, 1, "Value test", "Takeout ceiling = appraised value x LTV cap (one source: 75 percent)",
              "$430,000 x 75%<br>= $322,500", "Payoff $335,000 minus ceiling $322,500", "$12,500 gap to cover", True)
    b += card(554, 2, "Coverage test", "DSCR = gross monthly rent / monthly PITIA",
              "$2,650 / $2,850<br>= 0.93", "One source: most require 1.00 or more", "0.93 is below 1.00", True)
    b += ('<div class="card" style="left:68px;top:690px;width:944px;height:80px">'
          '<div class="abs mono" style="left:22px;top:18px;width:44px;height:44px;border-radius:50%;background:#C9A84C;color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:21px">3</div>'
          '<div class="abs" style="left:82px;top:0;height:100%;width:160px;display:flex;align-items:center;font-size:24px;font-weight:700;color:#0B1F3A">Lease</div>'
          '<div class="abs" style="left:250px;top:0;height:100%;width:670px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">One source: month to month leases do not satisfy most DSCR lenders</div></div>')
    b += ('<div class="panel" style="top:800px;height:62px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:19px;color:#3F5470">'
          'Test the takeout before funding the bridge. Cutoffs vary by lender.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Bridge to permanent loan:", "test the takeout first",
                "Three checks on who repays the bridge", b,
                "Sources: Peersense, Bridge to DSCR Refinance Playbook (updated 2026-05-16); Ascension Private, DSCR Refinance Readiness (page undated, accessed 2026-11-22); HardMoneyHome, DSCR Loans Explained (2026-08-21). "
                "Arithmetic: 430,000 x 0.75 = 322,500; 335,000 - 322,500 = 12,500; 2,650 / 2,850 = 0.93. Loan, value and rent illustrative.", 905)

PAGES = {"bridge-to-perm-conversion-basics": ("images/2026-11-26/0825-fb-bridge-to-perm-conversion-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
