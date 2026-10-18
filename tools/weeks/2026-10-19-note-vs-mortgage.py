#!/usr/bin/env python3
"""Graphic for note vs mortgage / deed of trust (Facebook, Tue Oct 20, 2026 5:27 pm ET).
Run from repo root: python3 tools/weeks/2026-10-19-note-vs-mortgage.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def comp(x, y, w, h, tag, name, sub, rows):
    s = f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
    s += f'<div class="abs lbl" style="left:24px;top:22px">{tag}</div>'
    s += f'<div class="abs mono gold" style="left:24px;top:48px;font-size:25px;line-height:38px;white-space:nowrap">{name}</div>'
    s += f'<div class="abs" style="left:24px;top:94px;width:{w - 48}px;font-size:18px;line-height:24px;color:#A5B2C3;white-space:nowrap">{sub}</div>'
    for i, (k, v) in enumerate(rows):
        yy = 144 + i * 50
        s += (f'<div class="abs" style="left:24px;top:{yy}px;width:110px;height:44px;display:flex;align-items:center;'
              f'font-size:13.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#8A9BB0">{k}</div>')
        s += (f'<div class="abs" style="left:140px;top:{yy}px;width:{w - 140 - 16}px;height:44px;display:flex;align-items:center;'
              f'font-size:18px;line-height:22px;color:#F0EDE4">{v}</div>')
    return s + '</div>'


def gfx():
    b = comp(68, 272, 462, 372, "The debt", "Promissory note", "the borrower's written promise to repay", [
        ("What", "states the repayment obligation"),
        ("Answers", "how much is owed, and on what terms"),
        ("Creates", "the personal obligation to repay"),
        ("Alone", "no collateral is pledged"),
    ])
    b += comp(550, 272, 462, 372, "The security", "Mortgage / deed of trust", "pledges the property as collateral", [
        ("What", "a lien on the real estate"),
        ("Answers", "what the lender can enforce against"),
        ("Gives", "the right to foreclose on default"),
        ("Varies", "by state; a deed of trust adds a trustee"),
    ])
    b += panel(676, 104, "NOTE + SECURITY",
               "The note says what is owed. The security instrument ties that debt to the property.", 470, 26)
    foot = ("Sources: Pierce Law, Deed of Trust vs. Promissory Note, NC (Jan 24, 2026); LBC Capital, What Is a Promissory Note in Private Real Estate Lending "
            "(Oct 15, 2026); Nolo, Mortgage vs. Promissory Note and Mortgage vs. Deed of Trust (pages undated, accessed Oct 18, 2026); "
            "OnlineEd, Promissory Note (Feb 6, 2026). Terms and instruments vary by state and lender. Not legal advice.")
    return shell("The note is the debt.", "The mortgage is the security.",
                 "Two documents, two different jobs",
                 b, foot, 818)


PAGES = {"note-vs-mortgage": ("images/2026-10-20/1727-fb-note-vs-mortgage.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
