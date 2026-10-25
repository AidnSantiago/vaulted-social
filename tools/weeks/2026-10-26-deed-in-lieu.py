#!/usr/bin/env python3
"""Graphic for deed in lieu of foreclosure (FB Sun Nov 1, 2026, 5:27 pm). Run from repo root: python3 tools/weeks/2026-10-26-deed-in-lieu.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def gfx():
    b = '<div class="abs lbl" style="left:68px;top:270px">What can stay on the property</div>'
    rows = [("Junior liens", "seg-blue"), ("Judgments", "seg-blue2"), ("Other claims", "seg-steel")]
    y = 308
    for t, cls in rows:
        b += (f'<div class="abs {cls}" style="left:68px;top:{y}px;width:420px;height:58px;border-radius:10px;'
              f'display:flex;align-items:center;padding-left:22px;font-size:21px;font-weight:700">{t}</div>')
        y += 70
    b += ('<div class="abs seg-gold" style="left:68px;top:518px;width:420px;height:62px;border-radius:10px;'
          'display:flex;align-items:center;padding-left:22px;font-size:21px;font-weight:700">Lender takes the deed</div>')
    b += ('<div class="abs" style="left:518px;top:308px;width:494px;font-size:19px;line-height:27px;color:#A5B2C3">'
          'These can stay after a deed in lieu, per the sources.</div>')
    def card(top, label, text, h=130):
        return (f'<div class="card" style="left:518px;top:{top}px;width:494px;height:{h}px">'
                f'<div class="abs lbl" style="left:22px;top:16px">{label}</div>'
                f'<div class="abs" style="left:22px;top:46px;width:450px;font-size:18px;line-height:26px;color:#F0EDE4">{text}</div></div>')
    b += card(384, "Deed in lieu", "The lender takes title subject to existing liens and claims.")
    b += card(534, "Foreclosure", "A lender may choose it to obtain clean title.", 120)
    b += panel(700, 100, "JUNIOR LIENS MATTER", "One source says a lender should hesitate where junior liens or judgments are outstanding. Varies by state.", 470, 24)
    nb = lambda t: t.replace(" ", "&nbsp;")
    foot = ("Sources: " + nb("Pillsbury") + ", Deeds in Lieu of Foreclosure (Aug 12, 2020); "
            + nb("Attorneys' Title Guaranty Fund") + ", Deeds in Lieu of Foreclosure (Feb 10, 2012; modified Mar 29, 2012); "
            + nb("LoneStarLandLaw.com") + ", Deeds in Lieu of Foreclosure (published Sep 4, 2025; modified Oct 12, 2026). "
            "Rules vary by state. Not legal advice.")
    return shell("Deed in lieu of foreclosure?", "Look at what stays on title.",
                 "The borrower hands over the property. The liens may not go away.", b, foot, 836)


PAGES = {"deed-in-lieu": ("images/2026-11-01/1727-fb-deed-in-lieu.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
