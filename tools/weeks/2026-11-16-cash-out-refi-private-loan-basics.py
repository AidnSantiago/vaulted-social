#!/usr/bin/env python3
"""Graphic for cash-out vs rate-term refinance leverage. Run from repo root: python3 tools/weeks/2026-11-16-cash-out-refi-private-loan-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

V, PAY, CASH = 400000, 210000, 90000

def gfx():
    n1, n2 = PAY, PAY + CASH
    l1, l2 = n1 / V * 100, n2 / V * 100
    assert (n2, round(l1, 1), round(l2, 1), V - n1, V - n2) == (300000, 52.5, 75.0, 190000, 100000)
    top, H = 340, 300
    def card(x, title, loan, ltv, eq, hl):
        lh, eh = H * loan / V, H * (V - loan) / V
        s = (f'<div class="card" style="left:{x}px;top:{top-40}px;width:458px;height:{H+90}px">'
             f'<div class="abs lbl" style="left:24px;top:20px">{title}</div>'
             f'<div class="abs mono gold" style="left:24px;top:56px;font-size:52px">{ltv}</div>'
             f'<div class="abs steel" style="left:24px;top:122px;font-size:18px">of value is the new loan</div>'
             f'<div class="abs" style="left:262px;top:60px;width:172px;height:{H}px;border-radius:10px;background:#5B7DAE;opacity:.35"></div>'
             f'<div class="abs" style="left:262px;top:{60+H-lh:.0f}px;width:172px;height:{lh:.0f}px;border-radius:{10 if loan==V else 0}px 0 10px 10px;background:{hl}"></div>'
             f'<div class="abs mono" style="left:262px;top:{60+H-lh+8:.0f}px;width:172px;text-align:center;font-size:20px;color:#0B1F3A">${loan:,}</div>'
             f'<div class="abs mono" style="left:262px;top:{60+(H-lh)/2-12:.0f}px;width:172px;text-align:center;font-size:16px;color:#0B1F3A">equity ${V-loan:,}</div>'
             f'<div class="abs" style="left:24px;top:190px;width:220px;font-size:18px;line-height:25px">{eq}</div></div>')
        return s
    body = '<div class="abs lbl" style="left:68px;top:268px">Illustrative: value $400,000, payoff $210,000</div>'
    body += card(68, "Rate-term refi", n1, "52.5%", "New loan replaces the $210,000 payoff. No cash out.", "#5B7DAE")
    body += card(554, "Cash-out refi", n2, "75%", "Same payoff plus $90,000 to the borrower.", "#C9A84C")
    body += ('<div class="panel" style="top:730px;height:96px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">+$90,000</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:640px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Lenders can size leverage on the new loan, not the old payoff. Terms vary by lender.</div></div>')
    return page("light", "BASICS", "PRIVATE LENDING, EXPLAINED", "Cash out lifts the loan",
                "from 52.5% to 75% of value", "Same property, same payoff, different leverage (before costs)", body,
                "Sources: Fannie Mae Selling Guide B2-1.3-02 (10/08/2025): limited cash-out cash back not above the greater of 1% of the new loan or $2,000; CFPB Office of Research blog (Dec 18, 2023): cash-out refinance means borrowing an amount substantially greater than owed. "
                "Arithmetic: 210,000 / 400,000 = 52.5%; (210,000 + 90,000) / 400,000 = 75%; equity 190,000 vs 100,000. Values illustrative.", 842)

PAGES = {"cash-out-refi-private-loan-basics": ("images/2026-11-21/0932-fb-cash-out-refi-private-loan-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
