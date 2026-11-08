#!/usr/bin/env python3
"""Graphic for environmental-basics (LinkedIn, Fri Nov 13, 2026 2:00 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-environmental-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    body = '<div class="abs lbl" style="left:68px;top:258px">What a Phase I includes</div>'
    body += step_cards([
        (1, "Records", "Review site records and government records", None),
        (2, "Site visit", "Visual inspection of the site and adjoining properties", None),
        (3, "Interviews", "Owners, operators and others with site knowledge", None),
    ], top=290, h=170)
    body += ('<div class="card" style="left:68px;top:482px;width:460px;height:152px">'
             '<div class="abs mono gold" style="left:22px;top:20px;font-size:22px;line-height:28px">WHAT IT LOOKS FOR</div>'
             '<div class="abs" style="left:22px;top:58px;width:416px;font-size:18px;line-height:26px;color:#F0EDE4">A recognized environmental condition: hazardous substances or petroleum products present or likely present</div></div>')
    body += ('<div class="card" style="left:552px;top:482px;width:460px;height:152px">'
             '<div class="abs mono gold" style="left:22px;top:20px;font-size:22px;line-height:28px">WHAT IT DOES NOT DO</div>'
             '<div class="abs" style="left:22px;top:58px;width:416px;font-size:18px;line-height:26px;color:#F0EDE4">Collect and lab test environmental samples</div></div>')
    body += stat_card(68, 654, 460, 150, "1 year", "outer limit before acquisition", "Inquiry done or updated within it", 40)
    body += stat_card(552, 654, 460, 150, "180 days", "for key elements", "Interviews, records, site visit", 40)
    body += panel(822, 74, "ASK EARLY", "Which standard and timing does the lender want?", 480, 26)
    foot = ("Sources: EPA, Brownfields All Appropriate Inquiries (updated May 7, 2026); EPA, AAI fact sheet (March 2026); West Virginia DEP, A User's Guide to Phase I Environmental Site Assessments (page undated, accessed 2026-11-08). "
            "AAI standards apply to buyers seeking liability protection. Lender requirements vary by lender.")
    return shell("What a Phase I environmental", "report covers.", "Records, a site visit and interviews. No lab testing.", body, foot, 914, eyebrow="ENVIRONMENTAL DUE DILIGENCE")

PAGES = {"environmental-basics": ("images/2026-11-13/1400-li-environmental-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
