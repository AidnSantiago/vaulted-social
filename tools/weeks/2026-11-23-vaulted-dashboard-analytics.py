#!/usr/bin/env python3
"""Graphic for vaulted-dashboard-analytics. Run from repo root: python3 tools/weeks/2026-11-23-vaulted-dashboard-analytics.py"""
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
.panel{position:absolute;left:68px;width:944px;border-radius:12px;background:rgba(11,31,58,.05);border:1.5px dashed rgba(154,123,34,.6)}
.foot{position:absolute;left:68px;width:944px;font-size:15px;line-height:22px;color:#5A6B82}
.logo{position:absolute;left:68px;bottom:46px;display:flex;align-items:center;gap:12px;font-family:Georgia,serif;font-weight:700;font-size:27px;color:#C9A84C}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'

def gfx():
    def col(i, q, title, line):
        x = 68 + i * 327
        return (f'<div class="card" style="left:{x}px;top:292px;width:290px;height:250px">'
                f'<div class="abs lbl" style="left:22px;top:30px;width:246px;line-height:21px">{q}</div>'
                f'<div class="abs" style="left:22px;top:88px;width:246px;font-family:Georgia,serif;font-size:34px;line-height:40px;font-weight:700">{title}</div>'
                f'<div class="abs" style="left:22px;top:186px;width:246px;font-size:18px;line-height:25px;color:#3F5470">{line}</div></div>')
    b = col(0, "What came in", "Interest collected", "Shown as a chart")
    b += col(1, "What it earns", "Rate", "Shown as analytics")
    b += col(2, "How much is lent", "LTV", "Shown as analytics")
    b += ('<div class="card" style="left:68px;top:576px;width:944px;height:96px">'
          '<div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Chart total = Collected This Year tile</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:250px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">The chart and the headline number agree.</div></div>')
    pan = ('<div class="panel" style="top:712px;height:100px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Cash, yield, leverage</div>'
           '<div class="abs" style="right:26px;top:0;height:100%;width:500px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Each one answers a different question about the loans.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, Dashboard analytics, PR 57, Nov 7 2026, source dated 2026-11-15."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">DASHBOARD ANALYTICS</div></div>'
            f'<h1>Cash collected is one number.<br><em>Rate and LTV add two more</em></h1>'
            f'<div class="sub">What the Vaulted dashboard analytics includes</div>{b}{pan}'
            f'<div class="foot" style="top:850px;width:700px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div></body></html>')

PAGES = {"dashboard-analytics": ("images/2026-11-24/1021-li-vaulted-dashboard-analytics.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
