#!/usr/bin/env python3
"""Graphic for mechanics lien deadlines by state (Facebook, Thu Oct 22, 2026 5:27 pm ET).
Run from repo root: python3 tools/weeks/2026-10-19-mechanics-lien-deadlines.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def state_card(x, y, w, h, st, rule, lines, date_txt):
    s = (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
         f'<div class="abs lbl" style="left:20px;top:18px">{st}</div>'
         f'<div class="abs" style="left:20px;top:46px;width:{w - 40}px;font-size:21px;line-height:27px;font-weight:700;color:#F0EDE4">{rule}</div>')
    top = 126
    for l in lines:
        s += f'<div class="abs" style="left:20px;top:{top}px;width:{w - 40}px;font-size:16px;line-height:22px;color:#A5B2C3">{l}</div>'
        top += 46
    s += (f'<div class="abs" style="left:20px;bottom:16px;width:{w - 40}px;font-size:14px;line-height:20px;color:#8A9BB0">{"Depends on the notice date" if date_txt.startswith("Earlier") else "Illustrative, last work Sep 10"}</div>'
          f'<div class="abs mono gold" style="left:20px;bottom:40px;font-size:{22 if len(date_txt) < 24 else 18}px;white-space:nowrap">{date_txt}</div></div>')
    return s


def gfx():
    b = state_card(68, 270, 290, 360, "Florida", "90 days after final furnishing",
                   ["Claim of lien is recorded in the clerk's office"], "Dec 9")
    b += state_card(395, 270, 290, 360, "Texas", "15th day of the 4th month",
                    ["3rd month for residential construction", "Affidavit filed with the county clerk"], "Jan 15 / Dec 15")
    b += state_card(722, 270, 290, 360, "California", "Direct contractor: 90 days after completion",
                    ["Or 60 days after the owner records a notice of completion"], "Earlier of two")
    b += '<div class="abs lbl" style="left:68px;top:650px">Same last day of work, three different clocks</div>'
    b += panel(690, 110, "VARIES", "Rules differ by state and by claimant type. Lenders can ask title or counsel which clock applies.", 600, 28)
    foot = ("Sources: Fla. Stat. 713.08(5), 2026 Florida Statutes, The Florida Legislature; Tex. Prop. Code 53.052, Justia (2025 edition) and "
            "Public.Law (verified May 26, 2025); Cal. Civ. Code 8412, FindLaw (current as of Jan 1, 2026). Dates are illustrative: "
            "Sep 10, 2026 + 90 days = Dec 9; Texas 4th month after September = Jan 15, 3rd month = Dec 15. Not legal advice.")
    return shell("Mechanics lien deadlines", "run on different clocks.",
                 "Three states, one last day of work: September 10", b, foot, 830)


PAGES = {"mechanics-lien-deadlines": ("images/2026-10-22/1727-fb-mechanics-lien-deadlines.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
