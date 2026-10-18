#!/usr/bin/env python3
"""Graphic for contractor vetting. Run from repo root: python3 tools/weeks/2026-10-19-contractor-vetting.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render, CHK
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ROWS = [
    ("License", "Look up status on the state board site", "A number on a bid is not proof"),
    ("Insurance", "Certificate is information only", "Ask for the endorsement too"),
    ("W-9", "Payee's correct name and taxpayer ID", "IRS form for payee records"),
    ("References", "Call past clients", "Ask about scope, timing, payments"),
    ("Lien waivers", "Can release the right to file a lien", "Rules vary by state"),
]


def gfx():
    b = ""
    top, h, gap = 262, 94, 10
    for i, (t, d, s) in enumerate(ROWS):
        y = top + i * (h + gap)
        b += (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:{h}px">'
              f'<div class="abs" style="left:24px;top:34px">{CHK}</div>'
              f'<div class="abs" style="left:70px;top:0;height:{h}px;width:200px;display:flex;align-items:center;'
              f'font-family:Georgia,serif;font-weight:700;font-size:28px;color:#E2C265">{t}</div>'
              f'<div class="abs" style="left:290px;top:19px;width:630px;font-size:22px;line-height:28px;font-weight:700;color:#F0EDE4">{d}</div>'
              f'<div class="abs" style="left:290px;top:53px;width:630px;font-size:18px;line-height:24px;color:#8A9BB0">{s}</div></div>')
    b += panel(top + 5 * (h + gap) + 4, 60, "VERIFY FIRST", "Check before the first draw, not after.", 520, 24)
    foot = ("Sources: California CSLB, Finding the right contractor (page undated, accessed 2026-10-18); Miller Nash, certificate of insurance (2015-04-06); "
            "IRS, Instructions for the Requester of Form W-9 (updated 2026-04-30); Corpay, lien waivers (2026-06-11). Example board: CSLB. Practice varies by state and lender.")
    return shell("Vetting a contractor,", "five things to verify.", "A checklist of what a lender can ask for", b, foot, 880)


PAGES = {"contractor-vetting": ("images/2026-10-23/1727-fb-contractor-vetting.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
