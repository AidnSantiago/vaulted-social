#!/usr/bin/env python3
"""Graphic for lis pendens (FB Thu Oct 15, 2026, 5:27 pm). Run from repo root: python3 tools/weeks/2026-10-12-lis-pendens.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def info_card(x, w, label, text, top=530, h=160):
    return (f'<div class="card" style="left:{x}px;top:{top}px;width:{w}px;height:{h}px">'
            f'<div class="abs lbl" style="left:22px;top:18px">{label}</div>'
            f'<div class="abs" style="left:22px;top:48px;width:{w - 44}px;font-size:18px;line-height:26px;color:#F0EDE4">{text}</div></div>')


def gfx():
    b = step_cards([
        ("1", "Lawsuit filed", "A suit affects title, ownership or use of a property.", "suit pending"),
        ("2", "Notice recorded", "A notice goes in the property records, in the chain of title.", "lis pendens"),
        ("3", "Later buyer or lender", "A title search can turn up the notice. Illustrative $210,000 loan.", "can see it"),
    ], h=222)
    b += info_card(68, 464, "What the sources say",
                   "Interests acquired during the suit are subject to its outcome. It can cloud title and prevent a sale or refinancing.")
    b += info_card(548, 464, "Varies by state",
                   "Some states require the filer to show probable cause or a good chance of winning if the notice is challenged.")
    b += panel(716, 96, "ASK ABOUT THE SUIT", "What does it claim, and how does the title company treat the notice?", 470)
    nb = lambda t: t.replace(" ", "&nbsp;")
    foot = ("Sources: " + nb("Cornell Legal Information Institute") + ", lis pendens (last reviewed June 2023); "
            + nb("Barnes Walker") + ", Notice of Lis Pendens (page undated, accessed " + nb("Oct 13, 2026") + "); "
            + nb("Corinthian Title") + ", Lis Pendens (page undated, accessed " + nb("Oct 13, 2026") + "). "
            "The $210,000 loan is illustrative. Rules vary by state. Not legal advice.")
    return shell("What is a lis pendens?", "A notice that says suit pending.",
                 "Latin for suit pending: a recorded notice about a lawsuit", b, foot, 846)


PAGES = {"lis-pendens": ("images/2026-10-15/1727-fb-lis-pendens.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
