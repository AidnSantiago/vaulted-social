#!/usr/bin/env python3
"""Graphic for NY Fed Q3 2026 flow into serious delinquency (mortgages). Run from repo root: python3 tools/weeks/2026-11-16-mba-delinquency-q3-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

A, B, BOOK = 1.28, 1.60, 20_000_000

def gfx():
    da, db = BOOK * A / 100, BOOK * B / 100
    assert round(da) == 256000 and round(db) == 320000 and round(B - A, 2) == 0.32 and round((B / A - 1) * 100) == 25
    track = 760
    body = '<div class="abs lbl" style="left:68px;top:290px">Flow into serious delinquency (90+ days), mortgage debt, annualized</div>'
    def row(y, name, v, col, dol):
        w = track * v / 2.0
        return (f'<div class="abs steel" style="left:68px;top:{y}px;font-size:18px">{name}</div>'
                f'<div class="abs" style="left:68px;top:{y+28}px;width:{w:.0f}px;height:52px;border-radius:8px;background:{col}"></div>'
                f'<div class="abs mono" style="left:84px;top:{y+39}px;font-size:28px;color:{"#FFFFFF" if col != "#C9A84C" else "#0B1F3A"}">{v:.2f}%</div>'
                f'<div class="abs mono gold" style="left:{68+w+16:.0f}px;top:{y+42}px;font-size:21px">${dol:,.0f} a year</div>')
    body += row(326, "Q3 2025", A, "#5B7DAE", da)
    body += row(426, "Q3 2026", B, "#C9A84C", db)
    body += '<div class="abs steel" style="left:68px;top:520px;font-size:16px">Dollar figures: illustrative $20,000,000 of balances</div>'
    def card(x, w, lab, big, txt):
        return (f'<div class="card" style="left:{x}px;top:570px;width:{w}px;height:150px"><div class="abs lbl" style="left:20px;top:16px">{lab}</div>'
                f'<div class="abs mono gold" style="left:20px;top:44px;font-size:36px">{big}</div>'
                f'<div class="abs" style="left:20px;top:94px;width:{w-40}px;font-size:17px;line-height:23px">{txt}</div></div>')
    body += card(68, 296, "Change", "+0.32 pts", "from 1.28% to 1.60%")
    body += card(392, 296, "Relative", "+25%", "1.60 divided by 1.28")
    body += card(716, 296, "Measure", "Newly 90+", "Share of balances newly 90 days late")
    body += ('<div class="panel" style="top:750px;height:96px"><div class="abs" style="left:26px;top:0;height:100%;width:892px;display:flex;align-items:center;font-size:20px;line-height:28px;color:#3F5470">'
             'This is all consumer mortgage debt, not private loans. Lenders can use it as a backdrop and watch their own aging buckets.</div></div>')
    return page("light", "NEW DATA", "PRIVATE LENDING, EXPLAINED", "Mortgage flow into 90+ late", "rose from 1.28% to 1.60%",
                "New York Fed household debt report, Q3 2026, released November 10, 2026", body,
                "Source: Federal Reserve Bank of New York, Household Debt and Credit Report, Q3 2026 (Nov 10, 2026): flow into serious delinquency, mortgage debt, Q3 2025 1.28%, Q3 2026 1.60%; rates are annualized shares of balances. "
                "Arithmetic: 1.60 - 1.28 = 0.32 points; 1.60 / 1.28 = 1.25; $20,000,000 x 1.28% = $256,000; x 1.60% = $320,000 (illustrative).", 872)

PAGES = {"mba-delinquency-q3-2026": ("images/2026-11-19/0825-fb-mba-delinquency-q3-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
