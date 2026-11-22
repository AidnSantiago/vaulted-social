#!/usr/bin/env python3
"""Graphic for vaulted-apply-page-questions. Run from repo root: python3 tools/weeks/2026-11-23-vaulted-apply-page-questions.py"""
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
.q{position:absolute;font-size:19px;line-height:25px;font-weight:700}
.qs{position:absolute;font-size:15.5px;line-height:21px;color:#3F5470}
.panel{position:absolute;left:68px;width:944px;border-radius:12px;background:rgba(11,31,58,.05);border:1.5px dashed rgba(154,123,34,.6)}
.foot{position:absolute;left:68px;width:944px;font-size:15px;line-height:22px;color:#5A6B82}
.logo{position:absolute;left:68px;bottom:46px;display:flex;align-items:center;gap:12px;font-family:Georgia,serif;font-weight:700;font-size:27px;color:#C9A84C}
.url{position:absolute;right:68px;bottom:52px;font-size:19px;font-weight:700;color:#3F5470;letter-spacing:.04em}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'
QS = [("Who is applying", "Name, person or entity, guarantor"),
      ("The property", "Property type and purpose"),
      ("The numbers", "Purchase price, value today, value after repairs, repair budget"),
      ("The timeline", "Close-by date and exit plan"),
      ("The experience", "Deals in the last 3 years")]

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:276px">Apply page: all optional</div><div class="abs lbl" style="left:690px;top:276px">Where answers show</div>'
    left = '<div class="card" style="left:68px;top:306px;width:580px;height:420px">'
    for i, (q, s) in enumerate(QS):
        y = 20 + i * 78
        left += f'<div class="q" style="left:24px;top:{y}px">{q}</div><div class="qs" style="left:24px;top:{y+27}px;width:530px">{s}</div>'
        if i < 4:
            left += f'<div class="abs" style="left:24px;top:{y+66}px;width:532px;height:1px;background:rgba(11,31,58,.12)"></div>'
    left += '</div>'
    def out(y, t, s):
        return (f'<div class="card" style="left:690px;top:{y}px;width:322px;height:194px"><div class="abs mono" style="left:22px;top:30px;font-size:24px;color:#9C7F2B">{t}</div>'
                f'<div class="abs" style="left:22px;top:76px;width:278px;font-size:18px;line-height:26px;color:#0B1F3A">{s}</div></div>')
    right = out(306, "Inquiry card", "The answers appear on the card.") + out(532, "Lender email", "The answers appear in the email.")
    arrow = '<div class="abs mono" style="left:652px;top:476px;width:36px;text-align:center;font-size:34px;color:#C9A84C">&rarr;</div>'
    pan = ('<div class="panel" style="top:756px;height:100px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Basics up front</div>'
           '<div class="abs" style="right:26px;top:0;height:100%;width:560px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">A deal can be easier to judge when the basics arrive with the inquiry.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, live feature, accessed 2026-11-15."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">THE APPLY PAGE</div></div>'
            f'<h1>The questions a lender<br><em>decides on</em></h1>'
            f'<div class="sub">Optional answers land on the inquiry card and in the lender email</div>{b}{left}{arrow}{right}{pan}'
            f'<div class="foot" style="top:884px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"apply-page-questions": ("images/2026-11-23/1247-fb-vaulted-apply-page-questions.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
