#!/usr/bin/env python3
"""Graphic for in-house vs third-party servicing (LinkedIn, Thu Oct 29, 2026 3:40 pm ET).
Run from repo root: python3 tools/weeks/2026-10-26-servicing-in-house-or-third-party.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def comp(x, y, w, h, name, sub, rows):
    s = f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
    s += f'<div class="abs lbl" style="left:22px;top:20px">{name}</div>'
    s += f'<div class="abs" style="left:22px;top:48px;width:{w-44}px;font-size:19px;line-height:24px;color:#A5B2C3">{sub}</div>'
    for i, (k, v) in enumerate(rows):
        yy = 110 + i * 62
        s += (f'<div class="abs" style="left:22px;top:{yy}px;width:{w-44}px;font-size:13.5px;font-weight:700;letter-spacing:.12em;'
              f'text-transform:uppercase;color:#8A9BB0">{k}</div>')
        s += f'<div class="abs" style="left:22px;top:{yy+20}px;width:{w-44}px;font-size:18px;line-height:22px;color:#F0EDE4">{v}</div>'
    return s + '</div>'


def gfx():
    b = comp(68, 262, 462, 366, "In-house servicing", "The lender does the servicing work itself", [
        ("Payments", "Lender staff collect and record them"),
        ("Escrow", "Lender staff manage it, if there is one"),
        ("Borrower contact", "Lender staff answer the borrower"),
        ("Responsibility", "The lender"),
    ])
    b += comp(550, 262, 462, 366, "Third-party servicer", "A separate company does the servicing work", [
        ("Payments", "Collects them, passes them to the lender"),
        ("Escrow", "Funds it and pays tax and insurance bills"),
        ("Borrower contact", "Main point of contact for the borrower"),
        ("Responsibility", "Not outsourced under bank guidance"),
    ])
    b += panel(654, 120, "OUTSOURCE THE TASK", "Bank regulators: using third parties does not diminish responsibility. Rules for private lenders vary by state.", 470, 23)
    b += panel(790, 84, "ASK BEFORE YOU PICK", "What will they do, and what stays with us?", 400, 23)
    return shell("Outsource the task,", "keep the accountability", "In-house versus third-party loan servicing", b,
                 "Sources: Freddie Mac, Mortgage Servicers: Who Are They and How They Can Help (last reviewed Oct 27, 2025). Federal Reserve, FDIC and OCC, Interagency Guidance on Third-Party Relationships (Jun 6, 2023); applies to banking organizations.", 900)


PAGES = {"servicing-in-house-or-third-party": ("images/2026-10-29/1540-li-servicing-in-house-or-third-party.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
