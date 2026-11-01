#!/usr/bin/env python3
"""Graphic for participation vs assignment (LinkedIn, Thu Nov 5, 2026, 3:40 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-participation-vs-assignment.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def head(x, w, title, style):
    return (f'<div class="abs {style}" style="left:{x}px;top:272px;width:{w}px;height:62px;border-radius:12px;'
            f'display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700">{title}</div>')

def cell(x, y, w, h, label, text):
    return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="abs lbl" style="left:20px;top:16px;font-size:13px">{label}</div>'
            f'<div class="abs" style="left:20px;top:44px;width:{w - 40}px;font-size:20px;line-height:27px;font-weight:700;color:#F0EDE4">{text}</div></div>')

def gfx():
    W, X1, X2 = 462, 68, 550
    b = head(X1, W, "Participation", "seg-blue") + head(X2, W, "Assignment", "seg-gold")
    rows = [
        ("Title to the loan", "Lead lender keeps title", "The entire note changes hands"),
        ("Contact for the borrower", "Lead lender stays the contact", "Buyer replaces the seller as lender"),
        ("Buyer position", "Interest in the loan, not a creditor of the borrower", "Acknowledged replacement of the seller"),
    ]
    y = 350
    for lab, a, c in rows:
        b += cell(X1, y, W, 112, lab, a) + cell(X2, y, W, 112, lab, c)
        y += 124
    b += ('<div class="card" style="left:68px;top:722px;width:944px;height:64px">'
          '<div class="abs" style="left:24px;top:0;height:64px;display:flex;align-items:center;font-size:20px;color:#F0EDE4">'
          'Servicing in a participation: <span class="gold" style="margin-left:8px">the lead lender manages it.</span></div></div>')
    b += panel(802, 76, "BEFORE BUYING", "Lenders can confirm in writing who holds title and services.", 480, 24)
    foot = ("Sources: Mayer Brown, Participations in the Fund Finance Market (May 6, 2025); Geraci LLP, Loan Participation Agreements in Private Lending "
            "(modified June 1, 2026); Dykema, Loan Participations (Summer 2012). Terms vary by agreement and by state. General education, not legal advice.")
    return shell("Same loan, two ways to sell it.", "Who the borrower deals with.",
                 "Participation versus assignment, side by side.", b, foot, 896)

PAGES = {"participation-vs-assignment": ("images/2026-11-05/1540-li-participation-vs-assignment.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
