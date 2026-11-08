#!/usr/bin/env python3
"""Graphic for deficiency judgment. Run from repo root: python3 tools/weeks/2026-11-09-deficiency-judgment.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def box(x, y, w, h, title, sub, gold=False):
    c = "gold" if gold else ""
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs mono {c}" style="left:20px;top:26px;width:{w-40}px;font-size:25px;line-height:32px;color:{"#E2C265" if gold else "#F0EDE4"}">{title}</div>'
            f'<div class="abs" style="left:20px;top:96px;width:{w-40}px;font-size:17px;line-height:24px;color:#A5B2C3">{sub}</div></div>')

def op(x, y, s):
    return f'<div class="abs mono gold" style="left:{x}px;top:{y}px;font-size:44px;line-height:48px">{s}</div>'

def case(x, y, w, h, head, l1):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs mono gold" style="left:20px;top:20px;width:{w-40}px;font-size:22px;line-height:28px">{head}</div>'
            f'<div class="abs" style="left:20px;top:90px;width:{w-40}px;font-size:18px;line-height:26px;color:#F0EDE4">{l1}</div></div>')

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:272px">The shortfall</div>'
    b += box(68, 306, 270, 170, "Debt owed", "The total mortgage debt.")
    b += op(356, 366, "&minus;")
    b += box(412, 306, 270, 170, "Sale price", "What the foreclosure sale brings.")
    b += op(700, 366, "=")
    b += box(756, 306, 256, 170, "Deficiency", "The gap a lender may try to recover.", True)
    b += '<div class="abs lbl" style="left:68px;top:508px">Whether and how it is pursued varies by state</div>'
    b += case(68, 542, 290, 180, "JUDICIAL", "The bank can usually request it in the foreclosure lawsuit.")
    b += case(395, 542, 290, 180, "NONJUDICIAL", "The bank must sue the borrower after the foreclosure.")
    b += case(722, 542, 290, 180, "SOME STATES", "Prohibit it, or limit the amount a bank can recover.")
    b += panel(752, 100, "CHECK FIRST", "Check state rules before pricing a loan,<br>not after a sale falls short.", 500, 26)
    foot = ("Sources: Nolo, Deficiency Judgments (updated 2024-02-20); LegalMatch, Deficiency Judgments (updated 2023-03-08). "
            "Rules and exceptions vary by state. Not legal advice.")
    return shell("When a foreclosure sale", "falls short of the debt.", "A deficiency judgment is a money judgment for the shortfall.", b, foot, 884)

PAGES = {"deficiency-judgment": ("images/2026-11-09/1727-fb-deficiency-judgment.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
