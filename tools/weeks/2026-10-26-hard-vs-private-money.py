#!/usr/bin/env python3
"""Graphic for hard-vs-private-money (Facebook, Mon Oct 26, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-10-26-hard-vs-private-money.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def card(y, who, view, quote, cls):
    h = 150
    b = f'<div class="card" style="left:68px;top:{y}px;width:944px;height:{h}px"></div>'
    b += f'<div class="abs {cls} mono" style="left:88px;top:{y+20}px;width:260px;height:110px;border-radius:10px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:19px;line-height:25px;padding:0 10px">{view}</div>'
    b += f'<div class="abs lbl" style="left:372px;top:{y+22}px;font-size:13px">{who}</div>'
    b += f'<div class="abs" style="left:372px;top:{y+48}px;width:620px;font-size:20px;line-height:28px;color:#F0EDE4">{quote}</div>'
    return b

def gfx():
    b = card(262, "Scotsman Guide, 2024", "A SUBSET", "Hard money is a subset of private lending: real estate-backed, short-term loans.", "seg-gold")
    b += card(430, "CRE University, 2009", "DIFFERENT LENDERS", "Hard money lenders are organized and usually licensed.", "seg-blue2")
    b += card(598, "BiggerPockets author", "THE SAME THING", "&ldquo;These are completely interchangeable terms in our industry.&rdquo;", "seg-steel")
    b += panel(776, 96, "ASK, DO NOT ASSUME", "The label alone may not tell you the terms. Ask who funds it and what it costs.", 480, 22)
    foot = ("Sources: Scotsman Guide, Discern all the flavors of private lending (May 1, 2024). CRE University, The Difference Between Hard Money and Private Money (June 30, 2009). "
            "BiggerPockets member blog, Hard Money vs Private Money: Are They Really Different (page undated, accessed Oct 25, 2026).")
    return shell("Hard money or", "private money?", "Sources use the two terms in different ways", b, foot, 892)

PAGES = {"hard-vs-private-money": ("images/2026-10-26/1727-fb-hard-vs-private-money.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
