#!/usr/bin/env python3
"""Graphic for transactional-funding. Run from repo root: python3 tools/weeks/2026-11-16-transactional-funding.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import css, V
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

PURCHASE, RESALE = 140000, 175000
SPREAD = RESALE - PURCHASE
assert SPREAD == 35000

def gfx():
    steps = [("1", "Lender funds", "Pays for the first purchase.", f"${PURCHASE:,}"),
             ("2", "Investor resells", "Sells to the end buyer.", f"${RESALE:,}"),
             ("3", "Lender repaid", "From the sale proceeds, plus its fees.", f"${PURCHASE:,}"),
             ("4", "Investor keeps", "What remains, before fees and costs.", f"${SPREAD:,}")]
    b = ""
    for i, (n, h, d, amt) in enumerate(steps):
        x = 68 + i * 242
        b += (f'<div class="card" style="left:{x}px;top:290px;width:218px;height:270px">'
              f'<div class="abs mono" style="left:20px;top:20px;width:36px;height:36px;border-radius:50%;background:#C9A84C;color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:19px">{n}</div>'
              f'<div class="abs" style="left:20px;top:72px;width:180px;font-size:21px;font-weight:700">{h}</div>'
              f'<div class="abs steel" style="left:20px;top:106px;width:180px;font-size:16.5px;line-height:23px">{d}</div>'
              f'<div class="abs mono gold" style="left:20px;top:200px;font-size:27px;white-space:nowrap">{amt}</div></div>')
        if i < 3:
            b += (f'<svg class="abs" style="left:{x+221}px;top:415px" width="20" height="20" viewBox="0 0 29 20">'
                  '<path d="M2 10 H24 M17 3 L25 10 L17 17" fill="none" stroke="#9C7F2B" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    track = 944
    w1 = track * PURCHASE / RESALE
    b += '<div class="abs lbl" style="left:68px;top:596px">Where the $175,000 resale goes (illustrative)</div>'
    b += f'<div class="abs" style="left:68px;top:630px;width:{w1:.0f}px;height:52px;border-radius:8px 0 0 8px;background:#3F5470"></div>'
    b += f'<div class="abs" style="left:{68+w1:.0f}px;top:630px;width:{track-w1:.0f}px;height:52px;border-radius:0 8px 8px 0;background:#C9A84C"></div>'
    b += '<div class="abs mono" style="left:88px;top:644px;font-size:21px;color:#F0EDE4">$140,000 repays lender</div>'
    b += f'<div class="abs mono" style="left:{68+w1+14:.0f}px;top:644px;font-size:21px;color:#0B1F3A">$35,000</div>'
    b += '<div class="panel" style="top:728px;height:100px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:21px">The resale repays the loan</div><div class="abs" style="right:26px;top:0;height:100%;width:430px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Repayment can come the same day. Fees, rates and terms vary by lender.</div></div>'
    foot = ("Sources: NewSilver, Transactional Funding Explained (Apr 30, 2024); DKC Lending, Transactional Funding (modified Nov 2, 2022). "
            "Illustrative figures. Arithmetic: 175,000 - 140,000 = 35,000, before lender fees and closing costs.")
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css("light")}</style></head><body>'
            '<div class="hdr"><div class="tag">LENDER BASICS</div><div class="eyebrow">PRIVATE LENDING, EXPLAINED</div></div>'
            '<h1>A same-day loan,<br><em>repaid by the resale</em></h1>'
            '<div class="sub">How a transactional loan works, step by step</div>'
            f'{b}<div class="foot" style="top:872px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div></body></html>')

PAGES = {"transactional-funding": ("images/2026-11-17/1727-fb-transactional-funding.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
