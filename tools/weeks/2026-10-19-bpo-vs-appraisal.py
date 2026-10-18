#!/usr/bin/env python3
"""Graphic for bpo-vs-appraisal (Facebook, Mon Oct 19, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-10-19-bpo-vs-appraisal.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, title, rows, cls):
    w, top, h = 458, 262, 440
    b = f'<div class="card" style="left:{x}px;top:{top}px;width:{w}px;height:{h}px"></div>'
    b += f'<div class="abs {cls} mono" style="left:{x+20}px;top:{top+20}px;width:{w-40}px;height:44px;border-radius:8px;display:flex;align-items:center;padding-left:14px;font-size:21px">{title}</div>'
    y = top + 84
    for lab, txt in rows:
        b += f'<div class="abs lbl" style="left:{x+22}px;top:{y}px;font-size:13px">{lab}</div>'
        b += f'<div class="abs" style="left:{x+22}px;top:{y+22}px;width:{w-44}px;font-size:19px;line-height:25px;color:#F0EDE4">{txt}</div>'
        y += 85
    return b

def gfx():
    b = col(68, "BROKER PRICE OPINION", [
        ("What it is", "An estimate of price"),
        ("Who prepares it", "A licensed broker or sales agent"),
        ("Standards", "Not an opinion of market value"),
        ("Where it shows up", "Not subject to development standards")], "seg-steel")
    b += col(554, "APPRAISAL", [
        ("What it is", "An opinion of value"),
        ("Who prepares it", "Only a licensed or certified appraiser"),
        ("Standards", "Report must follow USPAP"),
        ("Where it shows up", "Used in mortgage finance transactions")], "seg-gold")
    b += panel(728, 100, "TWO OPINIONS", "Different preparers, different standards. Check which one the file calls for.", 480, 24)
    foot = ("Sources: Texas Appraiser Licensing and Certification Board, Appraisal, Evaluation, Broker's Price Opinion: What's the Difference? (Dec 29, 2021). "
            "Quicken Loans, Broker Price Opinion (updated Oct 25, 2023). Texas Real Estate Research Center, For What It's Worth (Jan 9, 2013). Two of the three sources are Texas agencies; rules vary by state.")
    return shell("Broker price opinion", "versus appraisal", "Two different opinions of what a property is worth", b, foot, 856)

PAGES = {"bpo-vs-appraisal": ("images/2026-10-19/1727-fb-bpo-vs-appraisal.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
