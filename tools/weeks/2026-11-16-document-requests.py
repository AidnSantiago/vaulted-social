#!/usr/bin/env python3
"""Graphic for vaulted-document-requests. Run from repo root: python3 tools/weeks/2026-11-16-document-requests.py"""
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
    steps = [("1", "Lender asks", "One click asks for the standard set for the loan type, or add your own with a note and due date."),
             ("2", "Borrower uploads", "Documents for your lender, in the portal, with an upload button on each request."),
             ("3", "Lender reviews", "Download, Accept, or Ask again with a note. A file can be attached too."),
             ("4", "Borrower reads", "Review notes are shown on the request. Emails are sent both ways.")]
    b = ""
    for i, (n, h, d) in enumerate(steps):
        x = 68 + i * 240
        b += (f'<div class="card" style="left:{x}px;top:300px;width:224px;height:270px"><div class="num mono">{n}</div>'
              f'<div class="ct">{h}</div><div class="cd">{d}</div></div>')
    b += ('<div class="abs lbl" style="left:68px;top:268px">From the loan page to the borrower portal and back</div>')
    b += ('<div class="card" style="left:68px;top:620px;width:944px;height:120px"><div class="abs lbl" style="left:24px;top:18px">On the loan page</div>'
          '<div class="abs" style="left:24px;top:48px;width:896px;font-size:19px;line-height:27px">Lender side: "Documents from the borrower". Borrower side: "Documents for your lender".</div></div>')
    b += ('<div class="panel" style="top:776px;height:84px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">Accept or Ask again</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:520px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Each request carries its own upload, review and note.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, live feature, accessed 2026-11-15."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">BORROWER DOCUMENTS</div></div>'
            f'<h1>Document requests,<br><em>reviewed on the request</em></h1>'
            f'<div class="sub">The request and review loop for lender and borrower</div>{b}'
            f'<div class="foot" style="top:900px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"document-requests": ("images/2026-11-16/1247-fb-vaulted-document-requests.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
