#!/usr/bin/env python3
"""Graphic for receiver-appointment (LinkedIn, Thu Nov 12, 2026 3:40 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-receiver-appointment.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def col(x, w, title, items, tcls):
    h = (f'<div class="card" style="left:{x}px;top:262px;width:{w}px;height:318px">'
         f'<div class="abs lbl" style="left:22px;top:20px">{title}</div>')
    y = 62
    for it in items:
        h += (f'<div class="abs" style="left:22px;top:{y+2}px;width:20px;height:20px;border-radius:50%;background:rgba(201,168,76,.18);border:1.5px solid #C9A84C"></div>'
              f'<div class="abs" style="left:56px;top:{y}px;width:{w-80}px;font-size:19px;line-height:25px;color:#F0EDE4">{it}</div>')
        y += 62
    return h + '</div>'

def gfx():
    b = col(68, 460, "A receiver may", ["Collect rents from tenants", "Operate and manage the property", "Arrange repairs and maintenance", "Report to the court on funds"], "")
    b += col(552, 460, "Courts may weigh", ["Rents not turned over by the borrower", "Property not properly maintained", "Danger of waste, loss or impairment", "Collateral otherwise at risk"], "")
    b += '<div class="abs" style="left:68px;top:604px;width:944px;font-size:18px;line-height:26px;color:#A5B2C3">The receiver is an unbiased third party and does not take title to the property.</div>'
    b += panel(664, 120, "ask early, ask counsel", "Timing, grounds and powers vary by state and by the loan documents.", 430, 24)
    foot = ("Sources: von Briesen &amp; Roper, The Critical Role of the Foreclosure Receiver (Dec 18, 2013, Wisconsin); Neubert, Pepe &amp; Monteith, Connecticut Receivership Law (May 27, 2026); "
            "Nolo via AllLaw, Commercial Real Estate Foreclosure (updated Jul 21, 2023). Not legal advice.")
    return shell("The tenants keep paying. Who", "collects while foreclosure runs?", "When a lender can ask a court for a receiver", b, foot, 810, eyebrow="FORECLOSURE BASICS FOR LENDERS")

PAGES = {"receiver-appointment": ("images/2026-11-12/1540-li-receiver-appointment.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
