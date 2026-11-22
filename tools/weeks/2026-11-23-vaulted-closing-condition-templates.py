#!/usr/bin/env python3
"""Graphic for Vaulted closing condition templates. Run from repo root: python3 tools/weeks/2026-11-23-vaulted-closing-condition-templates.py"""
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
.sub{position:absolute;left:68px;top:226px;font-size:20.5px;color:#3F5470}
.card{position:absolute;border-radius:14px;background:#fff;border:1px solid rgba(11,31,58,.16)}
.lbl{font-size:14.5px;font-weight:700;letter-spacing:.16em;color:#9C7F2B;text-transform:uppercase}
.panel{position:absolute;left:68px;width:944px;border-radius:12px;background:rgba(11,31,58,.05);border:1.5px dashed rgba(154,123,34,.6)}
.foot{position:absolute;left:68px;width:944px;font-size:15px;line-height:22px;color:#5A6B82}
.logo{position:absolute;left:68px;bottom:46px;display:flex;align-items:center;gap:12px;font-family:Georgia,serif;font-weight:700;font-size:27px;color:#C9A84C}
.url{position:absolute;right:68px;bottom:52px;font-size:19px;font-weight:700;color:#3F5470;letter-spacing:.04em}
.row{position:absolute;left:0;width:944px;height:58px;border-top:1px solid rgba(11,31,58,.12)}
.c{position:absolute;top:0;height:100%;display:flex;align-items:center;font-size:20px}
.st{padding:5px 14px;border-radius:999px;font-size:15px;font-weight:700;border:1px solid rgba(11,31,58,.25);color:#3F5470}
.open{background:#C9A84C;border-color:#C9A84C;color:#0B1F3A}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'

def gfx():
    rows = [("Appraisal report", "Appraiser"), ("Entity documents", "Borrower"),
            ("Insurance binder", "Insurance agent"), ("Title commitment", "Title company")]
    b = '<div class="abs lbl" style="left:68px;top:290px">Illustrative template, written once</div>'
    b += '<div class="card" style="left:68px;top:326px;width:560px;height:330px">'
    b += ('<div class="abs lbl" style="left:26px;top:20px">Condition</div><div class="abs lbl" style="left:330px;top:20px">Owner</div>'
          '<div class="abs" style="left:0;top:52px;width:560px">')
    for i, (c, o) in enumerate(rows):
        b += (f'<div class="row" style="top:{i*68}px;width:560px;height:68px"><div class="c" style="left:26px">{c}</div>'
              f'<div class="c" style="left:330px;color:#3F5470">{o}</div></div>')
    b += '</div></div>'
    b += ('<div class="card" style="left:656px;top:326px;width:356px;height:156px"><div class="abs lbl" style="left:22px;top:18px">Per loan</div>'
          '<div class="abs" style="left:22px;top:48px;width:314px;font-size:19px;line-height:27px">A checklist with an owner<br>for each item.</div></div>')
    b += ('<div class="card" style="left:656px;top:500px;width:356px;height:156px"><div class="abs lbl" style="left:22px;top:18px">Template</div>'
          '<div class="abs" style="left:22px;top:48px;width:314px;font-size:19px;line-height:27px">A template can be saved<br>for all loans.</div></div>')
    b += ('<div class="panel" style="top:700px;height:110px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Blocking stop</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:610px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">'
          'Moving a loan&rsquo;s stage past an open blocking condition is stopped with a list of what&rsquo;s open, and the lender can choose &ldquo;Move anyway&rdquo;.</div></div>')
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            '<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">CLOSING CONDITION TEMPLATES</div></div>'
            '<h1>Write the checklist once.<br><em>Save it for all loans.</em></h1>'
            '<div class="sub">A standard closing list with an owner on every item</div>'
            f'{b}<div class="foot" style="top:850px">Illustrative conditions and owners only. Product text: Vaulted (vaultedonline.com), live feature, accessed 2026-11-15. Requirements vary by lender.</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"vaulted-closing-condition-templates": ("images/2026-11-27/1247-fb-vaulted-closing-condition-templates.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
