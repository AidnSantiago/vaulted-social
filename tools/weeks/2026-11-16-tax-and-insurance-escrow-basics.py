#!/usr/bin/env python3
"""Graphic for tax and insurance escrow basics. Run from repo root: python3 tools/weeks/2026-11-16-tax-and-insurance-escrow-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

TAX, INS = 4800, 1800
tot = TAX + INS; mo = tot / 12; mt = TAX / 12; mi = INS / 12

def gfx():
    assert tot == 6600 and mo == 550 and mt == 400 and mi == 150
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative: $4,800 tax and $1,800 insurance a year</div>'
    # row 1: escrow, 12 equal blocks
    body += '<div class="card" style="left:68px;top:326px;width:944px;height:150px"><div class="abs" style="left:24px;top:14px;font-size:20px;font-weight:700">With escrow</div>'
    body += '<div class="abs steel" style="left:200px;top:17px;font-size:16px">one twelfth of each bill, with every payment</div>'
    for i in range(12):
        body += f'<div class="abs mono" style="left:{24+i*76}px;top:60px;width:68px;height:62px;border-radius:8px;background:#C9A84C;color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:19px">$550</div>'
    body += '</div>'
    # row 2: no escrow, two lumps, illustrative timing
    body += '<div class="card" style="left:68px;top:496px;width:944px;height:150px"><div class="abs" style="left:24px;top:14px;font-size:20px;font-weight:700">Without escrow</div>'
    body += '<div class="abs steel" style="left:222px;top:17px;font-size:16px">the borrower pays each bill directly (timing illustrative)</div>'
    for i in range(12):
        if i in (2, 8):
            continue
        body += f'<div class="abs" style="left:{24+i*76}px;top:60px;width:68px;height:62px;border-radius:8px;background:rgba(11,31,58,.08)"></div>'
    body += '<div class="abs mono" style="left:176px;top:60px;width:68px;height:62px;border-radius:8px;background:#5B7DAE;color:#fff;display:flex;align-items:center;justify-content:center;font-size:17px">$4,800</div>'
    body += '<div class="abs mono" style="left:632px;top:60px;width:68px;height:62px;border-radius:8px;background:#5B7DAE;color:#fff;display:flex;align-items:center;justify-content:center;font-size:17px">$1,800</div>'
    body += '</div>'
    body += ('<div class="card" style="left:68px;top:666px;width:944px;height:92px">'
             '<div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:25px">($4,800 + $1,800) &divide; 12 = $550</div>'
             '<div class="abs steel" style="right:26px;top:0;height:100%;width:330px;display:flex;align-items:center;font-size:17px;line-height:24px">$400 tax plus $150 insurance a month</div></div>')
    body += ('<div class="panel" style="top:780px;height:96px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:19px;line-height:27px;color:#3F5470">'
             'Unpaid property taxes can become a lien, and a lapsed policy may lead a lender to buy its own. Lenders can track both due dates either way. Terms vary by lender and state.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Taxes and insurance:", "escrow or no escrow?",
                "What each means for a lender, with the monthly math", body,
                "Sources: CFPB, What is escrow (last reviewed Sep 11, 2024); Nolo, What Is a Mortgage Escrow Account (updated Aug 4, 2025). Sources describe home mortgages; private loan terms vary. "
                "Arithmetic: 4,800 + 1,800 = 6,600; 6,600 / 12 = 550; 4,800 / 12 = 400; 1,800 / 12 = 150. Amounts and timing illustrative.", 905)

PAGES = {"tax-and-insurance-escrow-basics": ("images/2026-11-22/1727-fb-tax-and-insurance-escrow-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
