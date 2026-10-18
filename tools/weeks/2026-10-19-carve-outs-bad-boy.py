#!/usr/bin/env python3
"""Graphic for carve-outs-bad-boy (LinkedIn, Thu Oct 22, 2026, 3:40 pm ET). Comparison cards.
Run from repo root: python3 tools/weeks/2026-10-19-carve-outs-bad-boy.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def col(x, w, label, title, exposure, bar_w, bar_cls, items, note):
    h = (f'<div class="card" style="left:{x}px;top:272px;width:{w}px;height:448px">'
         f'<div class="abs lbl" style="left:24px;top:22px">{label}</div>'
         f'<div class="abs" style="left:24px;top:52px;width:{w - 48}px;font-size:26px;line-height:32px;font-weight:700;color:#F0EDE4">{title}</div>'
         f'<div class="abs steel" style="left:24px;top:124px;font-size:16px;font-weight:700">Personal exposure</div>'
         f'<div class="abs {bar_cls} mono" style="left:24px;top:152px;width:{bar_w}px;height:40px;border-radius:8px;display:flex;align-items:center;padding-left:14px;font-size:16px;white-space:nowrap">{exposure}</div>'
         f'<div class="abs steel" style="left:24px;top:216px;font-size:16px;font-weight:700">Example triggers named in sources</div>')
    y = 246
    for it in items:
        h += (f'<div class="abs" style="left:24px;top:{y}px;width:{w - 48}px;font-size:18px;line-height:24px;color:#F0EDE4">&bull;&nbsp;{it}</div>')
        y += 34
    h += (f'<div class="abs" style="left:24px;top:376px;width:{w - 48}px;font-size:16px;line-height:22px;color:#8A9BB0">{note}</div></div>')
    return h


def gfx():
    b = col(68, 458, "Above the line", "Tied to the lender loss", "Actual loss from the act", 280, "seg-blue2",
            ["Fraud", "Intentional misrepresentation", "Misapplied casualty or<br>&nbsp;&nbsp;condemnation proceeds"],
            "Liability follows the loss the act causes.")
    b += col(554, 458, "Below the line", "Springing recourse", "Can reach the entire debt", 400, "seg-gold",
             ["Voluntary bankruptcy filing", "Can apply whether or not the<br>&nbsp;&nbsp;lender experiences any loss"],
             "Which acts sit below the line varies by loan documents.")
    b += panel(744, 84, "READ THE TRIGGER LIST", "Ask counsel what each trigger means<br>in your state.", 400)
    foot = ("Sources: Barley Snyder, Bad boy guaranties (Mar 1, 2016): below the line triggers apply whether or not the lender experiences any loss. "
            "Selzer Gurvitch, Bad-Boy Guaranties (page undated, accessed 2026-10-18): above the line exceptions are triggered only by actual lender loss. "
            "Hinckley Allen, Approaches to Carve-Out Guarantees (Nov 30, 2016). Not legal advice.")
    return shell("A non-recourse loan is not", "always non-recourse.",
                 "Carve-outs can make a guarantor personally liable &middot; terms vary by loan", b, foot, 858)


PAGES = {"carve-outs-bad-boy": ("images/2026-10-22/1540-li-carve-outs-bad-boy.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
