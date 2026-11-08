#!/usr/bin/env python3
"""Graphic for entity borrowers. Run from repo root: python3 tools/weeks/2026-11-09-entity-borrowers.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LX, MX, RX = 68, 296, 662   # row label column, individual column, LLC column
CW = 350

def head(x, w, t, gold=False):
    col = "#E2C265" if gold else "#F0EDE4"
    return (f'<div class="abs mono" style="left:{x}px;top:272px;width:{w}px;font-size:24px;line-height:30px;color:{col}">{t}</div>')

def row(y, h, label, a, b):
    s = (f'<div class="abs lbl" style="left:{LX}px;top:{y+22}px;width:230px;line-height:22px">{label}</div>')
    s += (f'<div class="card" style="left:{MX}px;top:{y}px;width:{CW}px;height:{h}px">'
          f'<div class="abs" style="left:20px;top:16px;width:{CW-40}px;font-size:18px;line-height:25px;color:#A5B2C3">{a}</div></div>')
    s += (f'<div class="card" style="left:{RX}px;top:{y}px;width:{CW}px;height:{h}px">'
          f'<div class="abs" style="left:20px;top:16px;width:{CW-40}px;font-size:18px;line-height:25px;color:#F0EDE4">{b}</div></div>')
    return s

def gfx():
    b = head(MX, CW, "INDIVIDUAL") + head(RX, CW, "LLC", True)
    b += row(318, 98, "Who signs", "The borrower signs for themselves.", "A person signs for the entity, so authority to sign is a question.")
    b += row(430, 98, "Existence", "The person is the borrower.", "Articles of organization and a good standing certificate.")
    b += row(542, 98, "Authority", "The person is the one who agrees to the loan.", "Operating agreement and a resolution naming the loan and signer.")
    b += row(654, 98, "Recourse", "The person is the debtor.", "A personal guaranty can add the owner as a second obligor.")
    b += panel(776, 92, "SIGNED &#8800; AUTHORIZED", "A signature is evidence someone signed, not proof they had authority.", 500, 24)
    foot = ("Sources: Geraci Law Firm, Private Lending Authority Disputes (2026-06-22); Spilman Thomas &amp; Battle, Another Limited Liability Company Wants a Loan (page dated 2023-08-11); "
            "Nolo, Personal Liability for LLC Mortgages (updated 2024-09-26). Varies by state and by lender. Not legal advice.")
    return shell("Lending to an LLC is not", "lending to a person.", "Same property, different paperwork and a different question.", b, foot, 888)

PAGES = {"entity-borrowers": ("images/2026-11-10/1727-fb-entity-borrowers.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
