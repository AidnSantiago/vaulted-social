#!/usr/bin/env python3
"""Graphic for wraparound loans (FB Sun Nov 8, 2026, 5:27 pm ET). Flow boxes + lien stack + risk cards, no numbers.
Run from repo root: python3 tools/weeks/2026-11-02-wraparound-loans.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render, ARROW_R
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def box(x, y, w, h, title, desc, accent="#F0EDE4"):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs" style="left:20px;top:22px;width:{w-40}px;font-size:24px;font-weight:700;color:{accent}">{title}</div>'
            f'<div class="abs" style="left:20px;top:58px;width:{w-40}px;font-size:16.5px;line-height:23px;color:#A5B2C3">{desc}</div></div>')

def risk(x, y, w, h, label, title, desc):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs lbl" style="left:24px;top:20px">{label}</div>'
            f'<div class="abs" style="left:24px;top:48px;width:{w-48}px;font-size:23px;line-height:28px;font-weight:700;color:#F0EDE4">{title}</div>'
            f'<div class="abs" style="left:24px;top:112px;width:{w-48}px;font-size:17px;line-height:24px;color:#A5B2C3">{desc}</div></div>')

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px;color:#8A9BB0">Monthly payments flow</div>'
    b += box(68, 296, 270, 128, "Buyer", "Pays the seller each month.")
    b += ARROW_R.format(x=346, y=350)
    b += box(405, 296, 270, 128, "Seller", "Keeps the original loan and pays it.")
    b += ARROW_R.format(x=683, y=350)
    b += box(742, 296, 270, 128, "Original lender", "Holds the first lien.", "#E2C265")
    b += '<div class="abs lbl" style="left:68px;top:452px;color:#8A9BB0">Lien position</div>'
    b += ('<div class="abs seg-gold" style="left:68px;top:484px;width:944px;height:52px;border-radius:10px;display:flex;align-items:center;padding-left:22px;font-size:19px;font-weight:700">1st: original mortgage (seller as borrower)</div>')
    b += ('<div class="abs seg-blue" style="left:68px;top:546px;width:944px;height:52px;border-radius:10px;display:flex;align-items:center;padding-left:22px;font-size:19px;font-weight:700">2nd (junior): wraparound loan (buyer as borrower)</div>')
    b += risk(68, 624, 452, 186, "Risk 1", "Seller stops paying", "The original lender can foreclose even if the buyer pays the seller on time.")
    b += risk(560, 624, 452, 186, "Risk 2", "Due-on-sale clause", "The original lender may be able to demand full repayment after the sale.")
    b += panel(828, 74, "Verify", "Confirm who pays the underlying loan.", 430, 26)
    foot = ("Sources: Rocket Mortgage, What Is A Wraparound Mortgage? (published 2024-01-11); AmeriSave, Wraparound Mortgage glossary (updated 2026-10-11). "
            "Terms and enforcement vary by state and by lender. Educational only, not legal advice.")
    return shell("Wraparound loans:", "a second lien on top of a first",
                 "The seller keeps the original mortgage in place", b, foot, 922,
                 eyebrow="LOAN STRUCTURES FOR PRIVATE LENDERS")

PAGES = {"wraparound-loans": ("images/2026-11-08/1727-fb-wraparound-loans.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
