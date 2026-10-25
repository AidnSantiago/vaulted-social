#!/usr/bin/env python3
"""Graphic for judicial-vs-nonjudicial (FB Sat Oct 31, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-10-26-judicial-vs-nonjudicial.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def col(x, w, head, cls, rows):
    b = f'<div class="card" style="left:{x}px;top:262px;width:{w}px;height:430px"></div>'
    b += (f'<div class="abs {cls} mono" style="left:{x+20}px;top:282px;width:{w-40}px;height:54px;border-radius:10px;'
          f'display:flex;align-items:center;justify-content:center;font-size:22px">{head}</div>')
    y = 356
    for lab, txt in rows:
        b += f'<div class="abs lbl" style="left:{x+22}px;top:{y}px;font-size:13px">{lab}</div>'
        b += f'<div class="abs" style="left:{x+22}px;top:{y+24}px;width:{w-44}px;font-size:19px;line-height:26px;color:#F0EDE4">{txt}</div>'
        y += 112
    return b


def gfx():
    b = col(68, 464, "JUDICIAL", "seg-blue2", [
        ("How it starts", "The lender must file a lawsuit."),
        ("Who oversees", "A court, through in-court hearings."),
        ("Timing, per Nolo", "Can be lengthy: several months or even years in some cases."),
    ])
    b += col(548, 464, "NONJUDICIAL", "seg-gold", [
        ("How it starts", "Power of sale, no court order first."),
        ("Who handles it", "A trustee typically handles it."),
        ("Timing, per Nolo", "Often just a few months or less."),
    ])
    b += panel(716, 96, "VARIES BY STATE", "Ask counsel which process applies to the loan.", 470)
    nb = lambda t: t.replace(" ", "&nbsp;")
    foot = ("Sources: " + nb("Nolo") + ", The Difference Between a Judicial and Nonjudicial Foreclosure (page undated, accessed " + nb("Oct 25, 2026") + "). "
            + nb("Cornell Legal Information Institute") + ", non-judicial foreclosure (last reviewed August 2023). "
            "Procedures differ widely by state. Not legal advice.")
    return shell("Judicial or nonjudicial?", "Who runs the foreclosure.",
                 "Court-run or trustee-run, and what that can mean for timing", b, foot, 846)


PAGES = {"judicial-vs-nonjudicial": ("images/2026-10-31/1727-fb-judicial-vs-nonjudicial.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
