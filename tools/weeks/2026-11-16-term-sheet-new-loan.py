#!/usr/bin/env python3
"""Graphic for vaulted-term-sheet-new-loan. Run from repo root: python3 tools/weeks/2026-11-16-term-sheet-new-loan.py"""
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

CSS += """
.box{position:absolute;width:26px;height:26px;border-radius:6px;border:2px solid #3F5470;background:#fff}
.skel{position:absolute;height:12px;border-radius:6px;background:rgba(11,31,58,.14)}
.no{color:#9C7F2B;font-weight:700}
"""

def gfx():
    b = '<div class="abs lbl" style="left:68px;top:266px">Term sheet reader, Documents tab</div>'
    # left: reader mock
    b += '<div class="card" style="left:68px;top:300px;width:470px;height:330px">'
    b += '<div class="box" style="left:24px;top:24px"></div><div class="abs" style="left:64px;top:24px;font-size:21px;font-weight:700;line-height:28px">Select all</div>'
    b += '<div class="abs mono" style="right:24px;top:24px;font-size:20px;line-height:28px;color:#9C7F2B">N of M ticked</div>'
    b += '<div class="abs" style="left:24px;top:70px;width:422px;height:1px;background:rgba(11,31,58,.16)"></div>'
    for i, w in enumerate([260, 200, 300, 230]):
        y = 96 + i * 52
        b += f'<div class="box" style="left:24px;top:{y}px"></div><div class="skel" style="left:64px;top:{y+7}px;width:{w}px"></div>'
    b += '<div class="abs" style="left:24px;top:288px;font-size:15px;color:#5A6B82">Values still arrive unticked.</div></div>'
    # right: never does
    b += '<div class="card" style="left:562px;top:300px;width:450px;height:330px"><div class="abs lbl" style="left:24px;top:24px">What it never does</div>'
    for i, t in enumerate(["Edit a value", 'Turn on "Use this for all my loans"', "Save anything"]):
        y = 74 + i * 82
        b += (f'<div class="abs" style="left:24px;top:{y}px;width:402px;height:64px;border-radius:10px;background:rgba(11,31,58,.05);display:flex;align-items:center;padding:0 18px;font-size:20px;font-weight:700;line-height:25px">'
              f'<span class="no" style="margin-right:14px;font-size:24px">&times;</span>{t}</div>')
    b += '</div>'
    b += ('<div class="card" style="left:68px;top:660px;width:944px;height:100px"><div class="abs lbl" style="left:24px;top:18px">Start a new loan from a term sheet</div>'
          '<div class="abs" style="left:24px;top:48px;width:896px;font-size:19px;line-height:27px">Tick what you want, review it, then save. Nothing is saved for you.</div></div>')
    b += ('<div class="panel" style="top:790px;height:84px"><div class="abs mono" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px;color:#9C7F2B">You tick. You save.</div>'
          '<div class="abs" style="right:26px;top:0;height:100%;width:480px;display:flex;align-items:center;font-size:18px;line-height:25px;color:#3F5470">Saving stays with the lender.</div></div>')
    foot = "Source: Vaulted (vaultedonline.com) product backlog, live feature, accessed 2026-11-15. Checklist rows are schematic."
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="hdr"><div class="tag">INSIDE VAULTED</div><div class="eyebrow">TERM SHEET READER</div></div>'
            f'<h1>Term sheet in,<br><em>you stay in control</em></h1>'
            f'<div class="sub">Values arrive unticked. Nothing saves until you save.</div>{b}'
            f'<div class="foot" style="top:910px">{foot}</div>'
            f'<div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

PAGES = {"term-sheet-new-loan": ("images/2026-11-20/1247-fb-vaulted-term-sheet-new-loan.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
