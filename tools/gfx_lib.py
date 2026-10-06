#!/usr/bin/env python3
"""Shared look and renderer for Vaulted social graphics.

Every graphic is a 1080x1080 CSS-pixel HTML frame rendered at 2x (2160x2160 PNG).
Look: navy gradient, gold + steel + cream, serif two-line headline (cream + gold),
mono numerals, dashed gold formula panel, source footnote, V-mark + "Vaulted" bottom-left.

Typical use (see tools/weeks/*.py and tools/examples/*.py):

    from gfx_lib import shell, panel, stat_card, render
    def gfx_example():
        body = stat_card(68, 300, 290, 150, "$2,000", "interest per month", "12% interest-only")
        body += panel(520, 92, "A FORMULA", "plain-language takeaway", 430)
        return shell("Headline line one", "headline line two (gold)", "subtitle", body, "Source: ...", 860)
    render([("images/2026-10-12/1727-fb-example.png", gfx_example)], repo_root)

Rules of thumb (learned the hard way):
- Headline lines must fit one line each (about 38 characters at 43px serif).
- Keep every element inside the 1080 frame; render() prints OUT OF FRAME if anything leaves it.
- Always open the PNG and look at it. Check for overlaps, orphaned words, cramped text.
"""
import os
from playwright.sync_api import sync_playwright

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;background:#060D18}
body{position:relative;overflow:hidden;font-family:'Liberation Sans',Arial,Helvetica,sans-serif;color:#F0EDE4;
 background:radial-gradient(900px 560px at 100% 0%,rgba(150,170,190,.17),rgba(150,170,190,0) 65%),
            linear-gradient(165deg,#0B1F3A 0%,#091A32 38%,#060D18 100%)}
.dots{position:absolute;inset:0;background-image:radial-gradient(rgba(138,155,176,.20) 1.1px,transparent 1.7px);background-size:58px 58px;background-position:30px 30px;opacity:.5}
.eyebrow{position:absolute;left:68px;top:58px;font-size:15.5px;font-weight:700;letter-spacing:.2em;color:#8A9BB0;text-transform:uppercase}
h1{position:absolute;left:68px;top:96px;font-family:Georgia,'Liberation Serif','Times New Roman',serif;font-weight:700;font-size:43px;line-height:52px;color:#F0EDE4;letter-spacing:-.2px;white-space:nowrap}
h1 em{font-style:normal;color:#D2B058}
.sub{position:absolute;left:68px;font-size:20.5px;color:#A5B2C3;white-space:nowrap}
.foot{position:absolute;left:68px;width:944px;font-size:15px;line-height:22.5px;color:#7F90A6}
.logo{position:absolute;left:68px;bottom:48px;display:flex;align-items:center;gap:12px;font-family:Georgia,'Liberation Serif','Times New Roman',serif;font-weight:700;font-size:27px;color:#C9A84C}
.mono{font-family:'DejaVu Sans Mono',Menlo,Consolas,monospace;font-weight:700}
.abs{position:absolute}
.gold{color:#E2C265}
.steel{color:#A5B2C3}
.card{position:absolute;border-radius:14px;background:linear-gradient(180deg,#172740 0%,#111d31 100%);border:1px solid rgba(138,155,176,.30)}
.num{position:absolute;left:20px;top:18px;width:36px;height:36px;border-radius:50%;background:linear-gradient(180deg,#E2C264,#B8963F);color:#0B1F3A;font-weight:700;font-size:19px;display:flex;align-items:center;justify-content:center}
.ctitle{position:absolute;left:20px;top:70px;font-size:22px;font-weight:700;color:#F0EDE4}
.cdesc{position:absolute;left:20px;top:102px;width:252px;font-size:16px;line-height:23px;color:#A5B2C3}
.pill{position:absolute;left:20px;bottom:18px;padding:6px 13px;border-radius:999px;background:rgba(201,168,76,.14);border:1px solid rgba(201,168,76,.55);color:#E2C265;font-family:'DejaVu Sans Mono',monospace;font-weight:700;font-size:15px}
.seg-gold{background:linear-gradient(180deg,#E2C264 0%,#B8963F 100%);color:#0B1F3A}
.seg-blue{background:linear-gradient(180deg,#3B5C8E 0%,#2A4670 100%);color:#F0EDE4}
.seg-blue2{background:linear-gradient(180deg,#5B7DAE 0%,#3F5E8E 100%);color:#F0EDE4}
.seg-steel{background:linear-gradient(180deg,#5A6B82 0%,#46556A 100%);color:#F0EDE4}
.panel{position:absolute;left:68px;width:944px;border-radius:12px;background:rgba(22,30,42,.88);border:1.5px dashed rgba(201,168,76,.5)}
.pl{position:absolute;left:26px;top:0;height:100%;display:flex;align-items:center;font-family:'DejaVu Sans Mono',Menlo,Consolas,monospace;font-weight:700;font-size:26px;color:#E2C265;white-space:nowrap}
.pr{position:absolute;right:26px;top:0;height:100%;display:flex;align-items:center;font-size:17px;line-height:24px;color:#A5B2C3}
.lbl{font-size:14.5px;font-weight:700;letter-spacing:.16em;color:#C9A84C;text-transform:uppercase}
"""

V_MARK = ('<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>')

ARROW_R = ('<svg class="abs" style="left:{x}px;top:{y}px" width="29" height="20" viewBox="0 0 29 20">'
           '<path d="M2 10 H24 M17 3 L25 10 L17 17" fill="none" stroke="#C9A84C" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def shell(h1a, h1b, sub, body, foot, foot_top, eyebrow="PRIVATE LENDING, EXPLAINED", sub_top=212):
    """Full page. h1a = cream first line, h1b = gold second line, foot_top = y of the source footnote."""
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="dots"></div><div class="eyebrow">{eyebrow}</div>'
            f'<h1>{h1a}<br><em>{h1b}</em></h1><div class="sub" style="top:{sub_top}px">{sub}</div>'
            f'{body}<div class="foot" style="top:{foot_top}px">{foot}</div>'
            f'<div class="logo">{V_MARK}<span>Vaulted</span></div></body></html>')


def panel(top, height, left_text, right_text, right_width=430, left_size=26):
    """Dashed gold panel: mono gold text on the left, plain steel sentence on the right."""
    return (f'<div class="panel" style="top:{top}px;height:{height}px">'
            f'<div class="pl" style="font-size:{left_size}px">{left_text}</div>'
            f'<div class="pr" style="width:{right_width}px">{right_text}</div></div>')


def stat_card(x, y, w, h, big, caption, small="", big_size=46):
    """Card with a big gold mono number, a bold caption and an optional small steel line."""
    s = (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
         f'<div class="abs mono gold" style="left:20px;top:22px;font-size:{big_size}px;line-height:54px;white-space:nowrap">{big}</div>'
         f'<div class="abs" style="left:20px;top:84px;width:{w - 40}px;font-size:20px;line-height:24px;font-weight:700;color:#F0EDE4">{caption}</div>')
    if small:
        s += f'<div class="abs" style="left:20px;top:116px;width:{w - 40}px;font-size:15px;line-height:20px;color:#8A9BB0">{small}</div>'
    return s + '</div>'


def render(pages, root, scale=2):
    """pages: list of (path relative to root, builder function). Writes PNGs (2160x2160 at scale 2).
    Also writes a .html next to a temp dir (not kept in the repo)."""
    import tempfile
    tmp = tempfile.mkdtemp(prefix="vgfx_")
    out = []
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--no-sandbox"])
        for rel, build in pages:
            html_path = os.path.join(tmp, os.path.basename(rel) + ".html")
            open(html_path, "w").write(build())
            pg = br.new_page(viewport={"width": 1080, "height": 1080}, device_scale_factor=scale)
            pg.goto("file://" + html_path)
            pg.wait_for_timeout(250)
            bad = pg.evaluate("""() => [...document.querySelectorAll('body *')].filter(e => {const r=e.getBoundingClientRect(); return r.width>0 && (r.right>1080.5 || r.bottom>1080.5 || r.left<-0.5)}).map(e => e.className + ' ' + (e.textContent||'').slice(0,30))""")
            if bad:
                print(rel, "OUT OF FRAME:", bad[:5])
            dest = os.path.join(root, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            pg.screenshot(path=dest)
            pg.close()
            out.append(dest)
            print("rendered", rel)
        br.close()
    return out
