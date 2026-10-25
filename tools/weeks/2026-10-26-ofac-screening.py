#!/usr/bin/env python3
"""Graphic for OFAC screening (LinkedIn, Wed Oct 28, 2026, 5:09 pm ET). Run from repo root: python3 tools/weeks/2026-10-26-ofac-screening.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ARW = ('<svg class="abs" style="left:{x}px;top:{y}px" width="29" height="20" viewBox="0 0 29 20"><path d="M2 10 H24 M17 3 L25 10 L17 17" '
       'fill="none" stroke="#C9A84C" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def box(x, y, w, h, style, big, title, sub):
    return (f'<div class="abs {style}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:12px">'
            f'<div class="abs mono" style="left:20px;top:0;height:{h}px;display:flex;align-items:center;font-size:36px">{big}</div>'
            f'<div class="abs" style="left:112px;top:{h//2-34}px;font-size:21px;font-weight:700;white-space:nowrap">{title}</div>'
            f'<div class="abs" style="left:112px;top:{h//2+4}px;font-size:16px;white-space:nowrap;opacity:.9">{sub}</div></div>')


def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">OFAC example: owners add up</div>'
    b += box(68, 306, 440, 100, "seg-steel", "25%", "Blocked Person X", "owns 25 percent of Entity A")
    b += box(68, 426, 440, 100, "seg-steel", "25%", "Blocked Person Y", "owns another 25 percent")
    b += ARW.format(x=520, y=346) + ARW.format(x=520, y=466)
    b += ('<div class="abs seg-gold" style="left:566px;top:306px;width:446px;height:220px;border-radius:12px">'
          '<div class="abs mono" style="left:24px;top:22px;font-size:52px">50%</div>'
          '<div class="abs" style="left:24px;top:96px;font-size:25px;font-weight:700">Entity A is blocked</div>'
          '<div class="abs" style="left:24px;top:134px;width:400px;font-size:17px;line-height:24px">'
          'Considered blocked even if its own name is not on the SDN List</div></div>')
    b += ('<div class="card" style="left:68px;top:556px;width:944px;height:122px">'
          '<div class="abs lbl" style="left:24px;top:20px">Why it matters</div>'
          '<div class="abs" style="left:24px;top:52px;width:896px;font-size:21px;line-height:30px;color:#F0EDE4">'
          'U.S. persons are generally prohibited from dealing with SDNs. Civil liability may apply '
          '<span class="gold">even without knowing</span>.</div></div>')
    b += panel(702, 92, "BEFORE CLOSING", "Lenders can screen borrowers and their owners.", 470)
    foot = ("Sources: U.S. Treasury OFAC, FAQ 18 (released Sept 10, 2002) and FAQ 399, 50 Percent Rule (released Aug 13, 2014); "
            "OFAC FAQ 91 (updated Aug 21, 2024); OFAC Ransomware Advisory (Sept 21, 2021). "
            "General education, not legal advice.")
    return shell("Not on the list?", "Check the owners too.", "What an OFAC sanctions check covers", b, foot, 824)


PAGES = {"ofac-screening": ("images/2026-10-28/1709-li-ofac-screening.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
