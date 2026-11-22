#!/usr/bin/env python3
"""Graphic for servicing transfer notice basics. Run from repo root: python3 tools/weeks/2026-11-23-servicing-transfer-notice-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    x0, x1 = 150, 930  # day -15 .. day +30 mapped across the line
    def X(d): return x0 + (d + 15) / 45 * (x1 - x0)
    body = '<div class="abs lbl" style="left:68px;top:290px">Notice timeline, days from the transfer date</div>'
    body += f'<div class="abs" style="left:{x0}px;top:392px;width:{x1-x0}px;height:6px;border-radius:3px;background:#3F5470"></div>'
    marks = [(-15, "DAY -15", "Outgoing servicer notice due by this date", "#C9A84C"),
             (0, "DAY 0", "Servicing transfer date", "#0B1F3A"),
             (15, "DAY +15", "New servicer notice due by this date", "#C9A84C"),
             (30, "DAY +30", "New owner notice after a sale", "#9C7F2B")]
    for d, lab, cap, col in marks:
        x = X(d)
        body += f'<div class="abs" style="left:{x-14:.0f}px;top:381px;width:28px;height:28px;border-radius:14px;background:{col}"></div>'
        body += f'<div class="abs mono" style="left:{x-70:.0f}px;top:336px;width:140px;text-align:center;font-size:21px;color:#0B1F3A">{lab}</div>'
        body += f'<div class="abs steel" style="left:{x-80:.0f}px;top:424px;width:160px;text-align:center;font-size:16px;line-height:22px">{cap}</div>'
    cards = [("Covered mortgage loans", "Regulation X: outgoing servicer notice at least 15 days before, new servicer notice within 15 days after. Truth in Lending: new owner notice within 30 days of a sale."),
             ("Business purpose loans", "Regulation X exempts a loan made primarily for a business, commercial, or agricultural purpose. State rules vary, and the note may set its own terms.")]
    for i, (h, d) in enumerate(cards):
        x = 68 + i * 482
        body += (f'<div class="card" style="left:{x}px;top:548px;width:462px;height:200px"><div class="abs lbl" style="left:22px;top:18px">{h}</div>'
                 f'<div class="abs" style="left:22px;top:52px;width:418px;font-size:19px;line-height:27px">{d}</div></div>')
    body += ('<div class="panel" style="top:778px;height:84px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'Lenders can confirm loan purpose first, then check state law and the note.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Loan sold or servicing moved?", "who tells the borrower, and when",
                "Servicing transfer notices, and where business loans differ", body,
                "Sources: CFPB, 12 CFR 1024.33 (page undated, accessed 2026-11-22); Cornell LII, 12 CFR 1024.33 and 15 U.S.C. 1641 (accessed 2026-11-22); "
                "eCFR, 12 CFR 1024.5 (current as of 2026-10-23). Educational only; not legal advice.", 890)

PAGES = {"servicing-transfer-notice-basics": ("images/2026-11-26/1540-li-servicing-transfer-notice-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
