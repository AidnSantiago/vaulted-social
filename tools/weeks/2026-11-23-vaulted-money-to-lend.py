#!/usr/bin/env python3
"""Graphic for vaulted-money-to-lend. Run from repo root: python3 tools/weeks/2026-11-23-vaulted-money-to-lend.py"""
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

def gfx():
    def box(top, n, title, line):
        return (f'<div class="card" style="left:68px;top:{top}px;width:944px;height:210px">'
                f'<div class="abs mono" style="left:30px;top:0;height:100%;display:flex;align-items:center;font-size:76px;color:#C9A84C">{n}</div>'
                f'<div class="abs lbl" style="left:150px;top:62px">{"Shown first" if n == "1" else "Shown below it"}</div>'
                f'<div class="abs" style="left:150px;top:92px;font-family:Georgia,serif;font-size:42px;font-weight:700">{title}</div>'
                f'<div class="abs" style="left:150px;top:150px;font-size:20px;color:#3F5470">{line}</div></div>')
    b = box(290, "1", "Money to Lend", "The capital question")
    b += '<div class="abs mono" style="left:68px;top:508px;width:944px;text-align:center;font-size:40px;line-height:40px;color:#C9A84C">&darr;</div>'
    b += box(552, "2", "Portfolio Health", "The condition of the loans already out")
    pan = ('<div class="panel" style="top:786px;height:92px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Capital, then health</div>'
           '<div class="abs" style="right:26px;top:0;height:100%;width:520px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Both are in view before the next loan is considered.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, Money to Lend shown above Portfolio Health, PR 59, Nov 7 2026, source dated 2026-11-15."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">MONEY TO LEND</div></div>'
            f'<h1>Capital first,<br><em>then portfolio health</em></h1>'
            f'<div class="sub">The order in which Vaulted shows them</div>{b}{pan}'
            f'<div class="foot" style="top:910px;width:700px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"money-to-lend": ("images/2026-11-24/1247-fb-vaulted-money-to-lend.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
