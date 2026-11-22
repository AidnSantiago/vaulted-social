#!/usr/bin/env python3
"""Graphic for default notice and cure period basics. Run from repo root: python3 tools/weeks/2026-11-23-default-notice-cure-period-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    steps = [("1", "Payment missed", "The borrower fails to pay as the note requires."),
             ("2", "Notice of default", "A formal written statement that the borrower has not met an obligation."),
             ("3", "15 day cure window", "Illustrative. Time to pay the missed amount."),
             ("4", "Cured or not", "Cured: loan continues. Not cured: remedies may follow.")]
    body = '<div class="abs lbl" style="left:68px;top:290px">Illustrative timeline, 15 day cure period</div>'
    for i, (n, h, d) in enumerate(steps):
        x = 68 + i * 238
        hot = i == 2
        bg = "background:#0B1F3A;" if hot else ""
        ink = "#F0EDE4" if hot else "#0B1F3A"
        sub = "#C9D2DE" if hot else "#3F5470"
        body += (f'<div class="card" style="left:{x}px;top:326px;width:222px;height:290px;{bg}">'
                 f'<div class="abs mono" style="left:20px;top:20px;width:36px;height:36px;border-radius:50%;background:#C9A84C;color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:19px">{n}</div>'
                 f'<div class="abs" style="left:20px;top:72px;width:184px;font-size:21px;font-weight:700;line-height:26px;color:{ink}">{h}</div>'
                 f'<div class="abs" style="left:20px;top:132px;width:184px;font-size:16.5px;line-height:24px;color:{sub}">{d}</div></div>')
    body += ('<div class="card" style="left:68px;top:644px;width:944px;height:120px"><div class="abs lbl" style="left:24px;top:18px">Who sets the length</div>'
             '<div class="abs" style="left:24px;top:48px;width:896px;font-size:19px;line-height:27px">Cure periods vary by state and by loan documents. Additional notice requirements may apply before remedies become available.</div></div>')
    body += ('<div class="panel" style="top:790px;height:84px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">Check both</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:660px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Lenders can read the loan documents and state law before sending a notice.</div></div>')
    return page("light", "LENDER BASICS", "PRIVATE LENDING, EXPLAINED", "Missed a payment?", "Notice, then cure period",
                "What a notice of default and a cure period are", body,
                "Sources: Cornell Legal Information Institute, Notice of default (last reviewed 2025-09); Reed Smith, What just happened: a default or an event of default? (2026-03-06). "
                "Cure window of 15 days is illustrative. Not legal advice.", 900)

PAGES = {"default-notice-cure-period-basics": ("images/2026-11-29/1015-fb-default-notice-cure-period-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
