#!/usr/bin/env python3
"""Graphic for default interest vs note rate (Facebook, Thu Oct 15, 2026 12:47 pm ET). Built Oct 13, 2026.
Run from repo root: python3 tools/weeks/2026-10-12-default-interest.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BAL, R_NOTE, R_DEF = 380000, 10, 18   # all illustrative


def gfx():
    m_note = BAL * R_NOTE / 100 / 12
    m_def = BAL * R_DEF / 100 / 12
    diff = m_def - m_note
    assert f"{m_note:,.2f}" == "3,166.67" and f"{m_def:,.2f}" == "5,700.00" and f"{diff:,.2f}" == "2,533.33"
    X0, S = 68, 944 / m_def
    b = '<div class="abs lbl" style="left:68px;top:268px">One month of interest on $380,000, interest-only</div>'
    b += stat_card(68, 304, 290, 150, "10%", "note rate", "illustrative")
    b += stat_card(395, 304, 290, 150, "18%", "default rate", "illustrative")
    b += stat_card(722, 304, 290, 150, "+$2,533", "more in one month", "$5,700.00 - $3,166.67")
    b += '<div class="abs lbl" style="left:68px;top:488px">Monthly interest if the default rate applies to the whole balance</div>'
    H = 64
    b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:530px;width:{m_note * S:.1f}px;height:{H}px;border-radius:8px;'
          f'display:flex;align-items:center;padding-left:18px;font-size:22px">$3,166.67 at 10%</div>')
    b += (f'<div class="abs seg-gold mono" style="left:{X0}px;top:614px;width:{m_def * S:.1f}px;height:{H}px;border-radius:8px;'
          f'display:flex;align-items:center;padding-left:18px;font-size:22px">$5,700.00 at 18%</div>')
    b += ('<div class="abs steel" style="left:68px;top:696px;width:944px;font-size:17px;line-height:24px">'
          'A note can instead apply the default rate only to the amount in default. Limits vary by state.</div>')
    b += panel(752, 92, "CHECK THE NOTE WORDING",
               "Which balance, which defaults, and what the state allows all vary.", 430, 24)
    foot = ("Sources: UpCounsel, Understanding Default Interest Rate Clauses in Contracts, updated Nov 10, 2025; "
            "Aaron Hall, Default Interest Rates: Legal Implications and Best Practices, updated Oct 1, 2024; "
            "GoDocs, Default Interest Rate (page undated, accessed 2026-10-13). Not legal advice. "
            "Illustrative: $380,000, 10% and 18%. Monthly interest = balance x rate / 12: "
            "$3,166.67 and $5,700.00; difference $2,533.33.")
    return shell("A 10% note rate can become", "18% after a default.",
                 "What one month of default interest adds &middot; illustrative", b, foot, 876,
                 eyebrow="PRIVATE LENDING, EXPLAINED")


PAGES = {"default-interest": ("images/2026-10-15/1247-fb-default-interest.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
