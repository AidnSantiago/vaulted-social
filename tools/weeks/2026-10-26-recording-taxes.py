#!/usr/bin/env python3
"""Graphic for recording-taxes (Facebook, Tue Oct 27, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-10-26-recording-taxes.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN = 400000
SCALE = 0.2  # px per dollar

def seg(x, y, dollars, label, cls):
    w = dollars * SCALE
    return (f'<div class="abs {cls} mono" style="left:{x}px;top:{y}px;width:{w - 4}px;height:62px;border-radius:8px;'
            f'display:flex;align-items:center;justify-content:center;font-size:18px">{label}</div>')

def row(top, title, sub, parts, total):
    b = f'<div class="card" style="left:68px;top:{top}px;width:944px;height:196px"></div>'
    b += f'<div class="abs" style="left:92px;top:{top+18}px;font-size:23px;font-weight:700;color:#F0EDE4">{title}</div>'
    b += f'<div class="abs" style="left:92px;top:{top+50}px;font-size:16px;color:#8A9BB0">{sub}</div>'
    x = 92
    for d, lab, cls in parts:
        b += seg(x, top + 88, d, lab, cls)
        x += d * SCALE
    b += f'<div class="abs mono gold" style="left:92px;top:{top+163}px;font-size:19px;white-space:nowrap">{total}</div>'
    return b

def gfx():
    b = row(262, "Florida", "Per $100: note stamps $0.35, intangible tax 2 mills ($0.20)",
            [(1400, "$1,400", "seg-gold"), (800, "$800", "seg-blue2")], "$1,400 + $800 = $2,200")
    b += row(480, "New York", "Per $100: 50 + 25 + 25 cents, before any city or county tax",
             [(2000, "$2,000", "seg-gold"), (1000, "$1,000", "seg-blue"), (1000, "$1,000", "seg-blue2")], "$2,000 + $1,000 + $1,000 = $4,000")
    b += panel(704, 100, "SAME $400,000", "Some states tax the loan amount at recording. Rates and rules vary by state.", 470, 24)
    foot = ("Sources: Florida Dept. of Revenue, TIP 24B04-01 (May 29, 2024). Florida Statutes s. 199.133 (2025). NY Dept. of Taxation and Finance, mortgage recording tax (updated Dec 30, 2025). "
            "Illustrative $400,000 loan. Arithmetic: $400,000 / $100 x $0.35 = $1,400; x $0.002 = $800; x $1.00 = $4,000.")
    return shell("A tax on the loan amount", "in some states", "Same illustrative $400,000 loan, two states", b, foot, 840)

PAGES = {"recording-taxes": ("images/2026-10-27/1247-fb-recording-taxes.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
