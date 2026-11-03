#!/usr/bin/env python3
"""Graphic for intercreditor basics (LinkedIn, Wed Nov 4, 2026, 5:09 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-intercreditor-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

NET, SENIOR, JUNIOR = 1150000, 780000, 245000  # illustrative


def gfx():
    owner = NET - SENIOR - JUNIOR
    assert owner == 125000
    W = 944
    sc = W / NET
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative sale, net of costs: $1,150,000</div>'
    # stacked bar
    x = 68
    segs = [("Senior", SENIOR, "seg-blue", "$780,000"), ("Junior", JUNIOR, "seg-blue2", "$245,000"), ("Owner", owner, "seg-gold", "$125,000")]
    for name, amt, cls, s in segs:
        w = amt * sc
        b += (f'<div class="abs {cls}" style="left:{x:.1f}px;top:312px;width:{w:.1f}px;height:84px;border-radius:8px;border:2px solid #0B1F3A;'
              f'display:flex;flex-direction:column;align-items:center;justify-content:center">'
              f'<div style="font-size:19px;font-weight:700">{name}</div><div class="mono" style="font-size:17px">{s}</div></div>')
        x += w
    b += '<div class="abs steel" style="left:68px;top:408px;font-size:17px">Paid left to right: each step is paid in full before the next.</div>'
    cards = [("Payment order", "Sets who is paid first from proceeds"),
             ("Standstill", "Can hold back junior enforcement for a period"),
             ("Cure and consent", "Junior may cure defaults; consent can apply to changes")]
    cw = 300
    for i, (t, d) in enumerate(cards):
        cx = 68 + i * (cw + 22)
        b += (f'<div class="card" style="left:{cx}px;top:466px;width:{cw}px;height:150px">'
              f'<div class="abs gold" style="left:20px;top:18px;font-size:22px;font-weight:700">{t}</div>'
              f'<div class="abs" style="left:20px;top:58px;width:{cw - 40}px;font-size:18px;line-height:26px;color:#A5B2C3">{d}</div></div>')
    b += panel(650, 100, "Read first", "Lenders can read the payment order before funding a junior loan. Terms vary by agreement.", 480, 26)
    foot = ("Sources: HelloData, What is an Intercreditor Agreement in Real Estate (page undated, accessed Nov 3, 2026); Blaney, A Standstill with a Time Limit "
            "is Not a True Standstill (Mar 1, 2017); White and Williams, Key Provisions to Focus on when Negotiating Intercreditor Agreements (Oct 5, 2017). "
            "Illustrative inputs. Arithmetic: 1,150,000 - 780,000 - 245,000 = 125,000. General education, not legal advice.")
    return shell("Two lenders, one property.", "Who is paid first?",
                 "What an intercreditor agreement can set between senior and junior", b, foot, 790)


PAGES = {"intercreditor-basics": ("images/2026-11-04/1709-li-intercreditor-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
