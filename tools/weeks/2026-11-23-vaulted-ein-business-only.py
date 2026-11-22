#!/usr/bin/env python3
"""Graphic for vaulted-ein-business-only. Run from repo root: python3 tools/weeks/2026-11-23-vaulted-ein-business-only.py"""
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
.pill{display:inline-block;padding:6px 10px;border-radius:999px;border:1px solid rgba(154,123,34,.6);color:#9C7F2B;font-size:15px;font-weight:700;font-family:'DejaVu Sans Mono',monospace;margin:0 4px 0 0;white-space:nowrap}
.node{position:absolute;width:150px;height:150px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.panel{position:absolute;left:68px;width:944px;border-radius:12px;background:rgba(11,31,58,.05);border:1.5px dashed rgba(154,123,34,.6)}
.foot{position:absolute;left:68px;width:944px;font-size:15px;line-height:22px;color:#5A6B82}
.logo{position:absolute;left:68px;bottom:46px;display:flex;align-items:center;gap:12px;font-family:Georgia,serif;font-weight:700;font-size:27px;color:#C9A84C}
.url{position:absolute;right:68px;bottom:52px;font-size:19px;font-weight:700;color:#3F5470;letter-spacing:.04em}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'

def gfx():
    b = ('<div class="card" style="left:68px;top:290px;width:458px;height:200px"><div class="abs lbl" style="left:24px;top:22px">Accepted</div>'
         '<div class="abs" style="left:24px;top:60px;width:410px;font-family:Georgia,serif;font-size:36px;font-weight:700;line-height:42px">EIN plus entity type</div>'
         '<div class="abs" style="left:24px;top:146px;width:410px;font-size:18px;color:#3F5470">Accepted only with an entity type</div></div>')
    b += ('<div class="card" style="left:554px;top:290px;width:458px;height:200px"><div class="abs lbl" style="left:24px;top:22px">Refused</div>'
          '<div class="abs" style="left:24px;top:60px;width:410px;font-family:Georgia,serif;font-size:36px;font-weight:700;line-height:42px">SSN-shaped numbers</div>'
          '<div class="abs" style="left:24px;top:146px;width:410px;font-size:18px;color:#3F5470">Not accepted</div></div>')
    b += ('<div class="card" style="left:68px;top:520px;width:458px;height:200px"><div class="abs lbl" style="left:24px;top:22px">What is shown</div>'
          '<div class="abs" style="left:24px;top:60px;width:410px;font-family:Georgia,serif;font-size:36px;font-weight:700;line-height:42px">Only the last 4</div>'
          '<div class="abs" style="left:24px;top:146px;width:410px;font-size:18px;color:#3F5470">Visible to the owner only</div></div>')
    b += ('<div class="card" style="left:554px;top:520px;width:458px;height:200px"><div class="abs lbl" style="left:24px;top:22px">Refuse every tax ID</div>'
          '<div class="abs" style="left:24px;top:62px;width:410px"><span class="pill">Document fields</span><span class="pill" style="margin-top:8px">Term sheet reader</span><span class="pill" style="margin-top:8px">Apply page</span></div></div>')
    b += ('<div class="panel" style="top:752px;height:110px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Plan around it</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:600px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Lenders can ask where a full tax ID really needs to live, and keep it out of general loan fields.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, year-end tax figures, PR 68, Nov 12 2026, source dated 2026-11-15."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">TAX ID HANDLING</div></div>'
            f'<h1>EINs for businesses only,<br><em>with the last 4 shown</em></h1>'
            f'<div class="sub">How tax IDs are handled</div>{b}'
            f'<div class="foot" style="top:900px;width:700px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"vaulted-ein-business-only": ("images/2026-11-27/1400-li-vaulted-ein-business-only.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
