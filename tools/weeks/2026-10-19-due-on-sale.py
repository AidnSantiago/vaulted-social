#!/usr/bin/env python3
"""Graphic for due-on-sale clause (Facebook, Wed Oct 21, 2026 5:27 pm ET).
Run from repo root: python3 tools/weeks/2026-10-19-due-on-sale.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, step_cards, ARROW_R, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def box(x, y, w, h, tag, title, desc):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs lbl" style="left:22px;top:20px">{tag}</div>'
            f'<div class="abs" style="left:22px;top:52px;width:{w - 44}px;font-size:23px;line-height:29px;font-weight:700;color:#F0EDE4">{title}</div>'
            f'<div class="abs" style="left:22px;top:96px;width:{w - 44}px;font-size:17px;line-height:24px;color:#A5B2C3">{desc}</div></div>')


def gfx():
    b = box(68, 262, 430, 170, "The trigger", "Property is sold or transferred",
            "without the lender's prior written consent")
    b += ARROW_R.format(x=510, y=337)
    b += box(552, 262, 460, 170, "The lender's option", "Declare the loan due and payable",
             "a right the lender holds at its option")
    b += '<div class="abs lbl" style="left:68px;top:470px">Federal exceptions, residential property with fewer than five units</div>'
    ex = [("Lease", "Lease of three years or less with no purchase option"),
          ("Family", "Transfer where the borrower's spouse or children become an owner"),
          ("Trust", "Transfer into a trust where the borrower is and remains a beneficiary")]
    for i, (t, d) in enumerate(ex):
        x = 68 + i * 327
        b += (f'<div class="card" style="left:{x}px;top:520px;width:290px;height:170px">'
              f'<div class="abs mono gold" style="left:20px;top:16px;font-size:26px;line-height:34px">{t}</div>'
              f'<div class="abs" style="left:20px;top:62px;width:250px;font-size:17px;line-height:23px;color:#F0EDE4">{d}</div></div>')
    b += panel(722, 100, "VARIES", "Details depend on the loan documents, the state and the facts of the transfer.", 560, 26)
    foot = ("Sources: 12 U.S.C. 1701j-3(a) and (d), U.S. Code 2024 Edition, GPO (accessed Oct 18, 2026; page undated beyond the 2024 edition label); "
            "Fitzpatrick Lentz and Bubba, Limitations on Enforcing Due on Sale Clauses (Mar 18, 2021). Selected exceptions shown, not a full list. Not legal advice.")
    return shell("A due-on-sale clause", "gives the lender an option.",
                 "What it says, and what federal law carves out", b, foot, 860)


PAGES = {"due-on-sale": ("images/2026-10-21/1727-fb-due-on-sale.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
