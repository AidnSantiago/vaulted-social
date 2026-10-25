#!/usr/bin/env python3
"""Graphic for draw-fraud-red-flags (Facebook, Tue Oct 27, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-10-26-draw-fraud-red-flags.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render, CHK
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def row(y, n, title, desc):
    return (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:112px"></div>'
            f'<div class="abs" style="left:92px;top:{y+43}px">{CHK}</div>'
            f'<div class="abs lbl" style="left:140px;top:{y+16}px;font-size:13px">FLAG {n}</div>'
            f'<div class="abs" style="left:140px;top:{y+38}px;width:850px;font-size:23px;line-height:28px;font-weight:700;color:#F0EDE4">{title}</div>'
            f'<div class="abs steel" style="left:140px;top:{y+72}px;width:850px;font-size:17px;line-height:22px">{desc}</div>')

def gfx():
    b = row(272, 1, "The same invoice in more than one draw", "Described as one invoice submitted across multiple draws or projects")
    b += row(414, 2, "An invoice altered to show more", "Higher quantities or prices than the supplier invoice")
    b += row(556, 3, "Billing ahead of the work in place", "Described on progress payments, where a sub bills ahead of the work")
    b += panel(718, 130, "INVOICES vs INSPECTION", "One way to test: compare invoices with inspection findings. Is the work billed the work seen?", 470, 22)
    foot = ("Sources: Trinity Real Estate Solutions, Construction Lending Fraud (May 8, 2026). Corpay, Construction Payment Fraud (updated Jul 1, 2026). "
            "None of these flags alone proves intent.")
    return shell("Draw fraud", "red flags", "Three things to check before a draw is paid", b, foot, 886)

PAGES = {"draw-fraud-red-flags": ("images/2026-10-27/1727-fb-draw-fraud-red-flags.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
