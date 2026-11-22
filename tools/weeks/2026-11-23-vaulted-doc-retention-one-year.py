#!/usr/bin/env python3
"""Graphic for vaulted-doc-retention-one-year. Run from repo root: python3 tools/weeks/2026-11-23-vaulted-doc-retention-one-year.py"""
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
    b = '<div class="card" style="left:68px;top:290px;width:944px;height:250px">'
    b += '<div class="abs lbl" style="left:28px;top:22px">The retention clock</div>'
    # line
    b += '<div class="abs" style="left:200px;top:140px;width:544px;height:0;border-top:4px solid #C9A84C"></div>'
    b += '<div class="abs mono" style="left:200px;top:100px;width:544px;text-align:center;font-size:19px;color:#3F5470">one year</div>'
    b += ('<div class="node" style="left:46px;top:66px;background:#0B1F3A;color:#F0EDE4">'
          '<div class="mono" style="font-size:26px;color:#E2C265">Upload</div><div style="font-size:16px;margin-top:6px">borrower sends<br>the file</div></div>')
    b += ('<div class="node" style="left:748px;top:66px;background:#C9A84C;color:#0B1F3A">'
          '<div class="mono" style="font-size:26px">Deleted</div><div style="font-size:16px;margin-top:6px">by the daily<br>scheduled job</div></div>')
    b += '</div>'
    # file types card
    b += '<div class="card" style="left:68px;top:570px;width:458px;height:190px"><div class="abs lbl" style="left:22px;top:20px">Accepted file types</div>'
    b += ('<div class="abs" style="left:22px;top:58px;width:414px">'
          '<span class="pill">PDF</span><span class="pill">JPEG</span><span class="pill">PNG</span><span class="pill">HEIC</span><span class="pill">DOCX</span><span class="pill">XLSX</span></div>'
          '<div class="abs" style="left:22px;top:136px;width:414px;font-size:19px;line-height:26px;font-weight:700">Up to 20 MB, checked by their contents</div></div>')
    # account closed card
    b += ('<div class="card" style="left:554px;top:570px;width:458px;height:190px"><div class="abs lbl" style="left:22px;top:20px">If an account closes</div>'
          '<div class="abs" style="left:22px;top:58px;width:414px;font-family:Georgia,serif;font-size:34px;font-weight:700;line-height:40px">All uploaded files<br>are deleted</div>'
          '<div class="abs" style="left:22px;top:140px;width:414px;font-size:19px;line-height:26px;color:#3F5470">No need to wait for the year to end</div></div>')
    b += ('<div class="panel" style="top:792px;height:96px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Plan around it</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:600px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Lenders can save anything needed past one year elsewhere first. Record rules vary by state and by lender.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, document requests, PR 72, Nov 13 2026, source dated 2026-11-15."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">DOCUMENT REQUESTS</div></div>'
            f'<h1>Uploaded today,<br><em>deleted one year later</em></h1>'
            f'<div class="sub">What happens to files borrowers upload</div>{b}'
            f'<div class="foot" style="top:918px;width:700px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"vaulted-doc-retention-one-year": ("images/2026-11-25/1247-fb-vaulted-doc-retention-one-year.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
