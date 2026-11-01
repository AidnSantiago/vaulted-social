#!/usr/bin/env python3
"""Graphic for the bankruptcy automatic stay (FB Sun Nov 8, 2026, 10:15 am ET). Run from repo root: python3 tools/weeks/2026-11-02-automatic-stay.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">What happens after a bankruptcy filing</div>'
    b += step_cards([
        (1, "Borrower files", "The automatic stay usually comes into force automatically.", "NO NOTICE NEEDED"),
        (2, "Foreclosure stops", "Actions such as foreclosures against the debtor are stopped.", "ACTION STOPPED"),
        (3, "Lender can ask", "A party must file a motion for relief from the stay.", "COURT DECIDES"),
    ], top=304, h=230)
    b += ('<div class="card" style="left:68px;top:590px;width:944px;height:106px">'
          '<div class="abs lbl" style="left:24px;top:18px">Common reasons one court lists for relief</div>'
          '<div class="abs" style="left:24px;top:52px;width:896px;font-size:21px;line-height:30px;color:#F0EDE4">'
          'The debtor is behind on payments, or there is no equity in the property.</div></div>')
    b += panel(740, 84, "Takeaway", "Check the filing with counsel before any sale step.", 520, 24)
    foot = ("Sources: U.S. Courts glossary, Automatic stay (page undated, accessed 2026-11-01); "
            "Jimerson Firm, Relief from the automatic stay (page undated, accessed 2026-11-01); "
            "U.S. Bankruptcy Court, Central District of California, Relief from stay: real property (page undated, accessed 2026-11-01). "
            "Rules vary by case and court. Not legal advice.")
    return shell("Borrower files for bankruptcy.", "Foreclosure actions stop.",
                 "The automatic stay, in three steps", b, foot, 870, eyebrow="WHEN A BORROWER FILES")

PAGES = {"automatic-stay": ("images/2026-11-08/1015-fb-automatic-stay.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
