#!/usr/bin/env python3
"""Graphic for payment application order. Run from repo root: python3 tools/weeks/2026-10-19-payment-application-order.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

PAY, FEE, INT = 2500, 150, 1900   # illustrative
# Order A: fee, interest, principal
A_PRIN = PAY - FEE - INT          # 450
# Order B: interest, principal, fee last
B_PRIN = PAY - INT                # 600
H = 320                           # bar height in px for $2,500
BAR_TOP = 330


def seg(x, y, w, h, cls, label, amt, size=21):
    return (f'<div class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;display:flex;flex-direction:column;'
            f'align-items:center;justify-content:center;font-size:{size}px;line-height:26px;border-radius:6px;{"flex-direction:row;gap:14px;" if h < 70 else ""}">'
            f'<span style="font-size:15px;font-weight:700">{label}</span><span class="mono">{amt}</span></div>')


def column(x, title, parts, owed):
    b = f'<div class="abs lbl" style="left:{x}px;top:272px;width:440px">{title}</div>'
    y = BAR_TOP
    for cls, label, amt, val in parts:
        h = max(round(H * val / PAY), 64)
        b += seg(x, y, 300, h - 4, cls, label, amt)
        y += h
    b += (f'<div class="abs" style="left:{x+316}px;top:{BAR_TOP}px;width:130px;font-size:15px;line-height:21px;color:#A5B2C3">{owed}</div>')
    return b


def gfx():
    fmt = lambda v: f"${v:,}"
    b = column(68, "Fees first", [("seg-steel", "Late fee", fmt(FEE), FEE), ("seg-blue", "Interest", fmt(INT), INT),
                                  ("seg-gold", "Principal", fmt(A_PRIN), A_PRIN)],
               f"Late fee fully paid. Principal falls by {fmt(A_PRIN)}.")
    b += column(552, "Interest and principal first", [("seg-blue", "Interest", fmt(INT), INT), ("seg-gold", "Principal", fmt(B_PRIN), B_PRIN)],
                f"Principal falls by {fmt(B_PRIN)}. {fmt(FEE)} late fee still owed.")
    b += ('<div class="abs" style="left:552px;top:%dpx;width:300px;height:56px;border:2px dashed #D2B058;border-radius:6px;display:flex;align-items:center;justify-content:center;gap:14px;color:#E2C265;font-size:15px;font-weight:700">'
          '<span>Late fee, still owed</span><span class="mono" style="font-size:21px">$150</span></div>' % (BAR_TOP + max(round(H*INT/PAY),64) + max(round(H*B_PRIN/PAY),64) + 4))
    b += panel(752, 92, "$2,500 payment", "Same payment, same loan. The order in the note decides where each dollar lands.", 560, 28)
    foot = ("Sources: Law Insider, sample clauses on payment application (page undated, accessed 2026-10-18); LegalClarity, Mortgage Payment Waterfall (May 15, 2026). "
            "Dollar figures are illustrative. Arithmetic: 2,500 - 150 - 1,900 = 450; 2,500 - 1,900 = 600. Order varies by loan documents.")
    return shell("One payment, two", "different outcomes.", "How the order in the note changes a $2,500 payment", b, foot, 870)


PAGES = {"payment-application-order": ("images/2026-10-24/1347-fb-payment-application-order.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
