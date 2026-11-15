#!/usr/bin/env python3
"""Graphic for vaulted-lending-guidelines. Run from repo root: python3 tools/weeks/2026-11-16-vaulted-lending-guidelines.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px}
body{position:relative;overflow:hidden;font-family:'Liberation Sans',Arial,sans-serif;color:#0B1F3A;background:linear-gradient(180deg,#F6F3EA 0%,#F0EDE4 100%)}
.abs{position:absolute}.mono{font-family:'DejaVu Sans Mono',Menlo,monospace;font-weight:700}
.hdr{position:absolute;left:68px;top:54px;display:flex;align-items:center;gap:16px}
.tag{padding:7px 16px;border-radius:999px;background:#C9A84C;color:#0B1F3A;font-weight:700;font-size:15px;letter-spacing:.18em}
.eyebrow{font-size:15px;font-weight:700;letter-spacing:.2em;color:#3F5470}
h1{position:absolute;left:68px;top:104px;font-family:Georgia,'Liberation Serif',serif;font-size:45px;line-height:54px;white-space:nowrap}
h1 em{font-style:normal;color:#9C7F2B}
.sub{position:absolute;left:68px;top:226px;font-size:20.5px;color:#3F5470}
.card{position:absolute;border-radius:14px;background:#fff;border:1px solid rgba(11,31,58,.16)}
.lbl{font-size:14.5px;font-weight:700;letter-spacing:.16em;color:#9C7F2B;text-transform:uppercase}
.row{position:absolute;left:22px;width:calc(100% - 44px);height:50px;border-bottom:1px solid rgba(11,31,58,.12);display:flex;align-items:center;justify-content:space-between;font-size:19px;font-weight:700}
.row span.r{font-size:15px;letter-spacing:.12em;color:#9C7F2B}
.panel{position:absolute;left:68px;width:944px;border-radius:12px;background:rgba(11,31,58,.05);border:1.5px dashed rgba(154,123,34,.6)}
.foot{position:absolute;left:68px;width:944px;font-size:15px;line-height:22px;color:#5A6B82}
.logo{position:absolute;left:68px;bottom:46px;display:flex;align-items:center;gap:12px;font-family:Georgia,serif;font-weight:700;font-size:27px;color:#C9A84C}
.url{position:absolute;right:68px;bottom:52px;font-size:19px;font-weight:700;color:#3F5470;letter-spacing:.04em}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'
CRIT = ["States", "Loan types", "Amount range", "Max LTV or LTC", "Minimum experience"]

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:276px">Set once</div><div class="abs lbl" style="left:604px;top:276px">Checked on every inquiry</div>'
    left = '<div class="card" style="left:68px;top:306px;width:400px;height:346px"><div class="abs mono" style="left:22px;top:18px;font-size:20px;color:#0B1F3A">Settings</div>'
    for i, c in enumerate(CRIT):
        left += f'<div class="row" style="top:{60 + i*52}px">{c}</div>'
    left += '</div>'
    right = '<div class="card" style="left:604px;top:306px;width:408px;height:346px"><div class="abs mono" style="left:22px;top:18px;font-size:20px;color:#0B1F3A">Inquiry card</div>'
    for i, c in enumerate(CRIT):
        right += f'<div class="row" style="top:{60 + i*52}px">{c}<span class="r mono">PASS / FAIL</span></div>'
    right += '</div>'
    arrow = '<div class="abs mono" style="left:480px;top:446px;width:112px;text-align:center;font-size:44px;color:#C9A84C">&rarr;</div><div class="abs" style="left:480px;top:500px;width:112px;text-align:center;font-size:15px;line-height:20px;color:#3F5470">same lines every time</div>'
    mail = ('<div class="card" style="left:68px;top:668px;width:944px;height:100px"><div class="abs lbl" style="left:24px;top:16px">Inquiry email</div>'
            '<div class="abs" style="left:24px;top:46px;width:896px;font-size:20px;line-height:28px">Includes a one line verdict.</div></div>')
    pan = ('<div class="panel" style="top:796px;height:84px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Write it down once</div>'
           '<div class="abs" style="right:26px;top:0;height:100%;width:520px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Each inquiry is measured against the same criteria.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, live feature, accessed 2026-11-15."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">LENDING GUIDELINES</div></div>'
            f'<h1>Same criteria,<br><em>every inquiry</em></h1>'
            f'<div class="sub">Settings on one side, a pass or fail screen on the other</div>{b}{left}{arrow}{right}{mail}{pan}'
            f'<div class="foot" style="top:918px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"lending-guidelines": ("images/2026-11-18/1709-li-vaulted-lending-guidelines.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
