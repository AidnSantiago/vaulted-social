#!/usr/bin/env python3
"""Graphic for lender's vs owner's title policy (Facebook, Sun Oct 25, 2026 1:47 pm ET).
Run from repo root: python3 tools/weeks/2026-10-19-title-lender-vs-owner-policy.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def lane(y, tag, who, barw, barcls, bartxt, note):
    s = f'<div class="abs lbl" style="left:68px;top:{y}px">{tag}</div>'
    s += f'<div class="abs" style="left:68px;top:{y + 26}px;font-family:Georgia,serif;font-weight:700;font-size:28px;color:#F0EDE4;white-space:nowrap">{who}</div>'
    s += (f'<div class="abs {barcls}" style="left:68px;top:{y + 76}px;width:{barw}px;height:58px;border-radius:10px;'
          f'display:flex;align-items:center;padding-left:20px;font-weight:700;font-size:18px;white-space:nowrap">{bartxt}</div>')
    s += f'<div class="abs" style="left:68px;top:{y + 144}px;width:944px;font-size:18px;line-height:24px;color:#A5B2C3;white-space:nowrap">{note}</div>'
    return s


def gfx():
    b = '<div class="abs mono steel" style="left:68px;top:262px;font-size:15px">CLOSING</div>'
    b += '<div class="abs" style="left:68px;top:286px;width:944px;height:2px;background:rgba(138,155,176,.35)"></div>'
    b += lane(306, "Lender's policy", "Protects only the lender", 560, "seg-gold",
              "Ends when the mortgage is paid off",
              "Source: lender's policy &quot;only protects the lender&quot;")
    b += lane(496, "Owner's policy", "Protects the owner's property rights", 944, "seg-blue2",
              "Lasts as long as the owner owns the property",
              "Source: &quot;protects your property rights for as long as you own the home&quot;")
    b += panel(690, 104, "TWO POLICIES",
               "Each one covers a different party. Lenders can confirm a lender's policy is on the commitment.", 480, 26)
    foot = ("Sources: American Land Title Association (ALTA), FAQs of Title Insurance for Homeowners; Maryland Insurance Administration, "
            "title insurance consumer brochure (form MIA-HE-1). Both pages undated, accessed Oct 18, 2026. "
            "Terms and requirements vary by state and lender. Not legal advice.")
    return shell("Two title policies.", "Two different insureds.",
                 "Who each policy covers, and for how long", b, foot, 826)


PAGES = {"title-lender-vs-owner-policy": ("images/2026-10-25/1347-fb-title-lender-vs-owner-policy.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
