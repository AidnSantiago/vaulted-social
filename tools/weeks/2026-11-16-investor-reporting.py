#!/usr/bin/env python3
"""Graphic for investor reporting. Run from repo root: python3 tools/weeks/2026-11-16-investor-reporting.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def rows(items, x, y0, w):
    out = ""
    for i, (a, b) in enumerate(items):
        y = y0 + i * 62
        out += (f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:50px;border-radius:8px;background:rgba(11,31,58,.05)"></div>'
                f'<div class="abs" style="left:{x}px;top:{y}px;width:6px;height:50px;border-radius:8px 0 0 8px;background:#C9A84C"></div>'
                f'<div class="abs" style="left:{x+22}px;top:{y}px;height:50px;display:flex;align-items:center;font-size:19px;font-weight:700">{a}</div>'
                f'<div class="abs mono gold" style="right:{1080-x-w+16}px;top:{y}px;height:50px;display:flex;align-items:center;font-size:17px">{b}</div>')
    return out

def gfx():
    body = ('<div class="card" style="left:68px;top:290px;width:458px;height:440px"><div class="abs lbl" style="left:24px;top:20px">ILPA template</div>'
            '<div class="abs steel" style="left:24px;top:46px;font-size:17px">Built for private equity funds</div></div>')
    body += rows([("Fee and expense detail", ""), ("Cash flows with dates", ""), ("Net IRR and TVPI", ""), ("Partnership expenses", "22, was 9")], 90, 392, 414)
    body += ('<div class="card" style="left:554px;top:290px;width:458px;height:440px"><div class="abs lbl" style="left:24px;top:20px">Community loan fund</div>'
             '<div class="abs steel" style="left:24px;top:46px;font-size:17px">Loan quality report, as of 6/30/2026</div></div>')
    body += rows([("Current", ""), ("31-60 days past due", ""), ("61-90 days past due", ""), (">90 days past due", ""), ("Non-Accrual, Impaired", "% of portfolio")], 576, 392 - 0, 414)
    body += ('<div class="panel" style="top:752px;height:96px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:21px">TAKEAWAY</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:700px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">A lender fund can build a monthly view from the same pieces: cash flows, fees, aging and non-accrual. Format varies by fund.</div></div>')
    return page("light", "INVESTORS", "PRIVATE LENDING, EXPLAINED", "Two public reports show", "what investors can see",
                "A private equity template and a community loan fund report", body,
                "Sources: Preqin, ILPA updates reporting guidelines to improve transparency, Jan 23, 2025 (22 expenses, up from nine; net IRR and TVPI); ACA Global, ILPA revised reporting template, Jan 31, 2025 (cash flows, fees); "
                "Community Loan Fund Loan Quality Report, as of 6/30/2026. Row labels as printed in the reports.", 872)

PAGES = {"investor-reporting": ("images/2026-11-16/1134-li-investor-reporting.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
