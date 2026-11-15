#!/usr/bin/env python3
"""Graphic for attom-zombie-foreclosure-q4-2026. Run from repo root: python3 tools/weeks/2026-11-16-attom-zombie-q4.py"""
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
.url{position:absolute;right:68px;bottom:52px;font-size:19px;font-weight:700;color:#3F5470;letter-spacing:.04em}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'

def gfx():
    track = 944
    b = '<div class="abs lbl" style="left:68px;top:290px">Share of foreclosures that are zombies, Q4 2026</div>'
    rows = [("United States", 3, "#5B7DAE", "3 percent"), ("Baltimore, MD (highest metro)", 13, "#C9A84C", "13 percent")]
    y = 326
    for name, v, col, lab in rows:
        w = track * v / 15
        b += f'<div class="abs" style="left:68px;top:{y}px;font-size:18px;color:#3F5470">{name}</div>'
        b += f'<div class="abs" style="left:68px;top:{y+28}px;width:{track}px;height:40px;border-radius:8px;background:rgba(11,31,58,.10)"></div>'
        b += f'<div class="abs" style="left:68px;top:{y+28}px;width:{w:.0f}px;height:40px;border-radius:8px;background:{col}"></div>'
        b += f'<div class="abs mono" style="left:84px;top:{y+37}px;font-size:21px;color:#0B1F3A">{lab}</div>'
        y += 92
    cards = [("29 states", "zombie properties rose from Q3", "Quarter over quarter"),
             ("PA +17.2%", "Pennsylvania, to 252", "zombie properties"),
             ("MD +19.2%", "Maryland, to 180", "zombie properties")]
    for i, (big, cap, small) in enumerate(cards):
        x = 68 + i * 321
        b += (f'<div class="card" style="left:{x}px;top:530px;width:302px;height:170px">'
              f'<div class="abs mono" style="left:20px;top:22px;font-size:34px;color:#9C7F2B;white-space:nowrap">{big}</div>'
              f'<div class="abs" style="left:20px;top:80px;width:262px;font-size:20px;line-height:24px;font-weight:700">{cap}</div>'
              f'<div class="abs" style="left:20px;top:134px;font-size:15px;color:#5A6B82">{small}</div></div>')
    b += ('<div class="panel" style="top:735px;height:96px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:21px;color:#9C7F2B">Check the local rate</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:470px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">A 3 percent national average can hide a 13 percent market.</div></div>')
    foot = ("Source: ATTOM, Q4 2026 Vacant Property and Zombie Foreclosure Report, Oct 29, 2026. 269,195 properties in foreclosure; "
            "8,040 zombies (3 percent). Bars scaled to a 15 percent axis.")
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">DATA</div><div class="eyebrow">ATTOM Q4 2026</div></div>'
            f'<h1>Zombie foreclosures:<br><em>3 percent, or 13 percent</em></h1>'
            f'<div class="sub">The national rate and the highest metro rate, side by side</div>{b}'
            f'<div class="foot" style="top:872px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"attom-zombie-q4": ("images/2026-11-16/0842-fb-attom-zombie-q4.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
