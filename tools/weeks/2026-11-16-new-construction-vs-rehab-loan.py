#!/usr/bin/env python3
"""Graphic for new-construction-vs-rehab-loan (Facebook, Mon Nov 16, 2026 5:27 pm ET). Run from repo root: python3 tools/weeks/2026-11-16-new-construction-vs-rehab-loan.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px}
body{position:relative;overflow:hidden;font-family:'Liberation Sans',Arial,sans-serif;color:#0B1F3A;background:linear-gradient(180deg,#F6F3EA 0%,#F0EDE4 100%)}
.abs{position:absolute} .mono{font-family:'DejaVu Sans Mono',Menlo,monospace;font-weight:700}
.hdr{position:absolute;left:68px;top:54px;display:flex;align-items:center;gap:16px}
.tag{padding:7px 16px;border-radius:999px;background:#C9A84C;color:#0B1F3A;font-weight:700;font-size:15px;letter-spacing:.18em}
.eyebrow{font-size:15px;font-weight:700;letter-spacing:.2em;color:#3F5470}
h1{position:absolute;left:68px;top:104px;font-family:Georgia,'Liberation Serif',serif;font-size:45px;line-height:54px;white-space:nowrap}
h1 em{font-style:normal;color:#9C7F2B}
.sub{position:absolute;left:68px;top:226px;font-size:20.5px;color:#3F5470;white-space:nowrap}
.card{position:absolute;border-radius:14px;background:#fff;border:1px solid rgba(11,31,58,.16)}
.lbl{font-size:14.5px;font-weight:700;letter-spacing:.16em;color:#9C7F2B;text-transform:uppercase}
.panel{position:absolute;left:68px;width:944px;border-radius:12px;background:rgba(11,31,58,.05);border:1.5px dashed rgba(156,127,43,.6)}
.foot{position:absolute;left:68px;width:944px;font-size:15px;line-height:22px;color:#5A6B82}
.logo{position:absolute;left:68px;bottom:46px;display:flex;align-items:center;gap:12px;font-family:Georgia,serif;font-weight:700;font-size:27px;color:#C9A84C}
.k{font-size:14.5px;font-weight:700;letter-spacing:.12em;color:#3F5470;text-transform:uppercase}
.v{font-size:21px;line-height:26px;font-weight:700}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'

def col(x, tag, title, rows, accent):
    b = (f'<div class="card" style="left:{x}px;top:278px;width:462px;height:470px;border-color:{accent}">'
         f'<div class="abs lbl" style="left:24px;top:20px">{tag}</div>'
         f'<div class="abs" style="left:24px;top:48px;font-size:28px;font-weight:700;font-family:Georgia,serif">{title}</div>')
    y = 104
    for k, v in rows:
        b += f'<div class="abs k" style="left:24px;top:{y}px">{k}</div><div class="abs v" style="left:24px;top:{y+22}px;width:414px">{v}</div>'
        y += 90
    return b + '</div>'

def gfx():
    b = col(68, "Rehab loan", "$85,000 budget", [
        ("What is financed", "Work on a house that already exists"),
        ("Typical timeline", "3 to 9 months"),
        ("Budget certainty", "Easier to lock than a build"),
        ("A 10% overrun", '<span class="mono" style="color:#9C7F2B;font-size:26px">$8,500</span>')], "rgba(11,31,58,.30)")
    b += col(550, "Ground-up loan", "$320,000 budget", [
        ("What is financed", "A house that does not exist yet"),
        ("Typical timeline", "12 to 24 months"),
        ("Draws", "Tied to building milestones, inspected"),
        ("A 10% overrun", '<span class="mono" style="color:#9C7F2B;font-size:26px">$32,000</span>')], "rgba(156,127,43,.8)")
    b += ('<div class="panel" style="top:778px;height:84px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:24px;color:#9C7F2B">Ask early</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:660px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">How will an overrun be covered? A contingency reserve is one option.</div></div>')
    foot = ("Sources: Park Place Finance (May 14, 2026): timelines, no collateral yet, budgets harder to lock; Flipper Force (page undated, accessed Nov 15, 2026): milestone draws, overruns. "
            "Budgets illustrative. Arithmetic: 85,000 x 0.10 = 8,500; 320,000 x 0.10 = 32,000.")
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">COMPARE</div><div class="eyebrow">PRIVATE LENDING, EXPLAINED</div></div>'
            f'<h1>Ground-up vs. rehab loans:<br><em>where the risk changes</em></h1>'
            f'<div class="sub">Same draws idea, very different exposure</div>{b}'
            f'<div class="foot" style="top:884px">{foot}</div><div class="logo">{V}<span>Vaulted</span></div></body></html>')

PAGES = {"new-construction-vs-rehab-loan": ("images/2026-11-16/1727-fb-new-construction-vs-rehab-loan.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
