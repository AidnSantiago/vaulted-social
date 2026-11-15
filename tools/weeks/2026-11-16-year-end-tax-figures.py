#!/usr/bin/env python3
"""Graphic for vaulted-year-end-tax-figures. Run from repo root: python3 tools/weeks/2026-11-16-year-end-tax-figures.py"""
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
.num{position:absolute;left:20px;top:20px;width:36px;height:36px;border-radius:50%;background:#C9A84C;color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:19px}
.ct{position:absolute;left:20px;top:72px;width:190px;font-size:20px;font-weight:700}
.cd{position:absolute;left:20px;top:106px;width:184px;font-size:16.5px;line-height:24px;color:#3F5470}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:268px">Two sets of figures, one page</div>'
    cards = [("Per loan", "Interest received", "The 1098 figures"),
             ("Per investor", "Distributions", "For each investor")]
    for i, (k, h, d) in enumerate(cards):
        x = 68 + i * 480
        b += (f'<div class="card" style="left:{x}px;top:304px;width:464px;height:190px">'
              f'<div class="abs lbl" style="left:26px;top:22px">{k}</div>'
              f'<div class="abs" style="left:26px;top:60px;font-family:Georgia,serif;font-size:36px;font-weight:700">{h}</div>'
              f'<div class="abs" style="left:26px;top:116px;font-size:20px;color:#3F5470">{d}</div></div>')
    b += ('<div class="abs mono" style="left:0;width:1080px;top:500px;text-align:center;font-size:26px;color:#9C7F2B">&#9660;</div>')
    b += ('<div class="card" style="left:68px;top:540px;width:944px;height:112px"><div class="abs lbl" style="left:26px;top:20px">Year-end tax page, under Tools</div>'
          '<div class="abs" style="left:26px;top:52px;width:892px;font-size:21px;line-height:30px">Owner-only. CSV downloads for the accountant.</div></div>')
    b += ('<div class="panel" style="top:690px;height:120px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;width:330px;line-height:30px;color:#9C7F2B">It does not decide which forms are required</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:520px;display:flex;align-items:center;font-size:19px;line-height:27px;color:#3F5470">That call stays with you and your accountant.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, live feature, accessed 2026-11-15."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">YEAR-END TAX</div></div>'
            f'<h1>Year-end figures,<br><em>ready for the accountant</em></h1>'
            f'<div class="sub">Interest received per loan, distributions per investor</div>{b}'
            f'<div class="foot" style="top:900px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"year-end-tax-figures": ("images/2026-11-19/1247-fb-vaulted-year-end-tax-figures.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
