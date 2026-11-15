#!/usr/bin/env python3
"""Graphic for survey and boundary risk basics. Run from repo root: python3 tools/weeks/2026-11-16-survey-and-boundary-risk-basics.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mockups"))
from gfx_lib import render
from product_posts_mockup import page
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def gfx():
    rows = [("1", "The policy", "Standard title policies exclude matters that a correct survey would reveal."),
            ("2", "The survey flags it", "An encroachment is a structure that crosses a property line without legal authorization. The title company lists it as a specific exception."),
            ("3", "The lender weighs it", "If a building the lender funds sits partly on a neighbor’s land, the security interest is compromised.")]
    body = ""
    y = 296
    for n, t, d in rows:
        body += (f'<div class="card" style="left:68px;top:{y}px;width:944px;height:118px">'
                 f'<div class="abs mono" style="left:22px;top:30px;width:56px;height:56px;border-radius:50%;background:#C9A84C;color:#0B1F3A;font-size:26px;display:flex;align-items:center;justify-content:center">{n}</div>'
                 f'<div class="abs" style="left:104px;top:16px;font-size:23px;font-weight:700">{t}</div>'
                 f'<div class="abs" style="left:104px;top:50px;width:810px;font-size:19px;line-height:26px;color:#3F5470">{d}</div></div>')
        y += 136
    body += ('<div class="panel" style="top:712px;height:104px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:24px">ASK</div>'
             '<div class="abs" style="right:26px;top:0;height:100%;width:790px;display:flex;align-items:center;font-size:19px;line-height:26px;color:#3F5470">Lenders can read the exceptions on a title commitment and ask whether a survey is needed. Requirements vary by state and by lender.</div></div>')
    return page("light", "BASICS", "PRIVATE LENDING, EXPLAINED", "A survey shows what title", "records can miss",
                "Boundary and encroachment risk, in three steps", body,
                "Sources: Starfield &amp; Smith, The Survey Exception (Oct 24, 2018); ALTA Land Survey, What Happens If an ALTA Survey Reveals an Encroachment (Jun 5, 2026); FindLaw, Title Policy May Not Cover Boundary Disputes (updated Jul 11, 2017). Educational only; not legal advice.", 862)

PAGES = {"survey-and-boundary-risk-basics": ("images/2026-11-21/1727-fb-survey-and-boundary-risk-basics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
