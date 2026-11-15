#!/usr/bin/env python3
"""Graphic for private lending market structure (Forecasa via AAPL, Oct 28 2026). Run from repo root: python3 tools/weeks/2026-11-16-private-lending-market-structure.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

TOTAL, NEW = 15865, 6128
RET = TOTAL - NEW
TOP10 = 24.7

def gfx():
    assert RET == 9737 and round(NEW / TOTAL * 100) == 39 and round(100 - TOP10, 1) == 75.3
    tw = 944
    wn = tw * NEW / TOTAL
    wt = tw * TOP10 / 100
    body = '<div class="abs lbl" style="left:68px;top:292px">Active private lenders in 2025</div>'
    body += (f'<div class="abs" style="left:68px;top:326px;width:{tw - wn:.0f}px;height:74px;border-radius:10px 0 0 10px;background:#5B7DAE"></div>'
             f'<div class="abs" style="left:{68 + tw - wn:.0f}px;top:326px;width:{wn:.0f}px;height:74px;border-radius:0 10px 10px 0;background:#C9A84C"></div>'
             f'<div class="abs mono" style="left:90px;top:343px;font-size:28px;color:#fff">{RET:,} originated in 2024 too</div>'
             f'<div class="abs mono" style="left:{68 + tw - wn + 20:.0f}px;top:343px;font-size:28px;color:#0B1F3A">{NEW:,} new</div>')
    body += (f'<div class="abs steel" style="left:68px;top:412px;font-size:18px">{TOTAL:,} lenders in all, up from 13,860 in 2024</div>'
             '<div class="abs mono gold" style="right:68px;top:410px;font-size:22px">39% of the base</div>')
    body += '<div class="abs lbl" style="left:68px;top:480px">Share of 2025 originations by unit count</div>'
    body += (f'<div class="abs" style="left:68px;top:514px;width:{wt:.0f}px;height:74px;border-radius:10px 0 0 10px;background:#0B1F3A"></div>'
             f'<div class="abs" style="left:{68 + wt:.0f}px;top:514px;width:{tw - wt:.0f}px;height:74px;border-radius:0 10px 10px 0;background:rgba(11,31,58,.14)"></div>'
             f'<div class="abs mono" style="left:84px;top:531px;font-size:28px;color:#E2C265">24.7%</div>'
             f'<div class="abs mono" style="left:{68 + wt + 24:.0f}px;top:531px;font-size:28px;color:#0B1F3A">75.3% went to every other lender</div>')
    body += (f'<div class="abs steel" style="left:68px;top:600px;font-size:18px">Top 10 lenders (23.8% in 2024)</div>')
    body += ('<div class="card" style="left:68px;top:656px;width:458px;height:132px"><div class="abs lbl" style="left:22px;top:18px">Not a few giants</div>'
             '<div class="abs" style="left:22px;top:48px;width:414px;font-size:19px;line-height:27px">The top 10 hold under a quarter of loans, so most volume is spread widely.</div></div>')
    body += ('<div class="card" style="left:554px;top:656px;width:458px;height:132px"><div class="abs lbl" style="left:22px;top:18px">A field that refills</div>'
             '<div class="abs" style="left:22px;top:48px;width:414px;font-size:19px;line-height:27px">Nearly two in five active lenders had not originated in 2024.</div></div>')
    body += ('<div class="panel" style="top:812px;height:70px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:20px">TAKEAWAY</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:700px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Lenders can ask who the new names in their market are before setting terms.</div></div>')
    return page("light", "MARKET DATA", "PRIVATE LENDING, EXPLAINED", "Nearly 2 in 5 private lenders",
                "were new in 2025", "Forecasa lender counts and concentration, reported by AAPL on October 28, 2026", body,
                "Source: Sean Morgan, From New Frontier to Established Markets, American Association of Private Lenders, Oct 28, 2026 (lender counts from Forecasa). "
                "Arithmetic: 15,865 minus 6,128 equals 9,737; 6,128 divided by 15,865 equals 38.6 percent, reported as 39 percent; 100 minus 24.7 equals 75.3.", 900)

PAGES = {"private-lending-market-structure": ("images/2026-11-20/1400-li-private-lending-market-structure.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
