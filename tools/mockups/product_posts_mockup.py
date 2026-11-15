#!/usr/bin/env python3
"""Mockups for product-led Vaulted social posts. Run: python3 tools/mockups/product_posts_mockup.py <outdir>"""
import sys, os
from playwright.sync_api import sync_playwright

def css(t):
    d = t == "dark"
    P = dict(
        bg="linear-gradient(165deg,#0B1F3A 0%,#091A32 40%,#060D18 100%)" if d else "linear-gradient(180deg,#F6F3EA 0%,#F0EDE4 100%)",
        ink="#F0EDE4" if d else "#0B1F3A", sub="#A5B2C3" if d else "#3F5470", gold="#D2B058" if d else "#9A7B22",
        card="linear-gradient(180deg,#172740,#111d31)" if d else "#FFFFFF", cardb="rgba(138,155,176,.30)" if d else "rgba(11,31,58,.16)",
        dash="rgba(201,168,76,.55)" if d else "rgba(154,123,34,.6)", panel="rgba(22,30,42,.88)" if d else "rgba(11,31,58,.05)",
        foot="#7F90A6" if d else "#5A6B82", track="rgba(90,107,130,.30)" if d else "rgba(11,31,58,.10)",
        tag_bg="#C9A84C", tag_ink="#0B1F3A")
    return f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1080px}}
body{{position:relative;overflow:hidden;font-family:'Liberation Sans',Arial,sans-serif;color:{P['ink']};background:{P['bg']}}}
.abs{{position:absolute}} .mono{{font-family:'DejaVu Sans Mono',Menlo,monospace;font-weight:700}}
.hdr{{position:absolute;left:68px;top:54px;display:flex;align-items:center;gap:16px}}
.tag{{padding:7px 16px;border-radius:999px;background:{P['tag_bg']};color:{P['tag_ink']};font-weight:700;font-size:15px;letter-spacing:.18em}}
.eyebrow{{font-size:15px;font-weight:700;letter-spacing:.2em;color:{P['sub']}}}
h1{{position:absolute;left:68px;top:104px;font-family:Georgia,'Liberation Serif',serif;font-size:45px;line-height:54px;white-space:nowrap}}
h1 em{{font-style:normal;color:{P['gold']}}}
.sub{{position:absolute;left:68px;top:226px;font-size:20.5px;color:{P['sub']}}}
.card{{position:absolute;border-radius:14px;background:{P['card']};border:1px solid {P['cardb']}}}
.lbl{{font-size:14.5px;font-weight:700;letter-spacing:.16em;color:{P['gold']};text-transform:uppercase}}
.panel{{position:absolute;left:68px;width:944px;border-radius:12px;background:{P['panel']};border:1.5px dashed {P['dash']}}}
.foot{{position:absolute;left:68px;width:944px;font-size:15px;line-height:22px;color:{P['foot']}}}
.logo{{position:absolute;left:68px;bottom:46px;display:flex;align-items:center;gap:12px;font-family:Georgia,serif;font-weight:700;font-size:27px;color:#C9A84C}}
.url{{position:absolute;right:68px;bottom:52px;font-size:19px;font-weight:700;color:{P['sub']};letter-spacing:.04em}}
.gold{{color:{P['gold']}}} .steel{{color:{P['sub']}}}
.pill{{display:inline-block;padding:5px 12px;border-radius:999px;border:1px solid {P['dash']};color:{P['gold']};font-size:15px;font-weight:700}}
"""
V = '<svg width="22" height="27.5" viewBox="0 0 24 30"><polygon points="0,0 12,30 24,0 18.2,0 12,17.4 5.8,0" fill="#C9A84C"/></svg>'
def page(t, tag, eyebrow, h1a, h1b, sub, body, foot, foot_top):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css(t)}</style></head><body>'
            f'<div class="hdr"><div class="tag">{tag}</div><div class="eyebrow">{eyebrow}</div></div><h1>{h1a}<br><em>{h1b}</em></h1><div class="sub">{sub}</div>'
            f'{body}<div class="foot" style="top:{foot_top}px">{foot}</div><div class="logo">{V}<span>Vaulted</span></div><div class="url">vaultedonline.com</div></body></html>')

def draws(t):
    # illustrative: budget 120000, 45% verified = 54000, requested 70000
    track = 944
    b = ('<div class="abs lbl" style="left:68px;top:290px">Illustrative draw request, rehab budget $120,000</div>')
    rows = [("Requested", 70000, "#5B7DAE"), ("Verified work in place", 54000, "#C9A84C"), ("Most a lender can approve", 54000, "#C9A84C")]
    y = 326
    for name, v, col in rows:
        w = track * v / 120000
        b += f'<div class="abs steel" style="left:68px;top:{y}px;font-size:18px">{name}</div>'
        b += f'<div class="abs" style="left:68px;top:{y+28}px;width:{track}px;height:40px;border-radius:8px;background:var(--x,rgba(128,140,160,.18))"></div>'
        b += f'<div class="abs" style="left:68px;top:{y+28}px;width:{w:.0f}px;height:40px;border-radius:8px;background:{col}"></div>'
        b += f'<div class="abs mono" style="left:{68+w+14:.0f}px;top:{y+36}px;font-size:21px;color:#0B1F3A;display:none"></div>'
        b += f'<div class="abs mono" style="left:84px;top:{y+37}px;font-size:21px;color:#0B1F3A">${v:,}</div>'
        y += 92
    b += ('<div class="card" style="left:68px;top:610px;width:458px;height:150px"><div class="abs lbl" style="left:22px;top:18px">Why it matters</div>'
          '<div class="abs" style="left:22px;top:48px;width:414px;font-size:19px;line-height:27px">Paying ahead of the work leaves cash in a property that has not earned it yet. Policies vary by lender.</div></div>')
    b += ('<div class="card" style="left:554px;top:610px;width:458px;height:150px"><div class="abs lbl" style="left:22px;top:18px">In Vaulted</div>'
          '<div class="abs" style="left:22px;top:48px;width:414px;font-size:19px;line-height:27px">Draw approval stops at verified work in place and shows the most the lender can approve.</div></div>')
    b += '<div class="panel" style="top:790px;height:84px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">New: Nov 15</div><div class="abs" style="right:26px;top:0;height:100%;width:640px;display:flex;align-items:center;font-size:18px;line-height:25px;color:var(--s)">Every draw also keeps an inspection record and a lien waiver status.</div></div>'
    return b

def reserve(t):
    b = '<div class="abs lbl" style="left:68px;top:290px">Worked example (illustrative)</div>'
    b += ('<div class="card" style="left:68px;top:326px;width:944px;height:150px">'
          '<div class="abs mono gold" style="left:30px;top:30px;font-size:44px;white-space:nowrap">$18,000 &divide; $2,400</div>'
          '<div class="abs mono gold" style="right:30px;top:30px;font-size:44px">= 7.5 months</div>'
          '<div class="abs steel" style="left:30px;top:100px;font-size:19px">interest reserve  &divide;  monthly interest  =  months of payments covered</div></div>')
    cells = [("Define it", "An interest reserve is money set aside to pay a loan’s interest while the project earns nothing yet."),
             ("Size it", "Divide the reserve by the monthly interest to see how many payments it covers."),
             ("Watch it", "A reserve that runs out before the exit leaves the lender with a gap to cover.")]
    for i, (h, d) in enumerate(cells):
        x = 68 + i * 321
        b += (f'<div class="card" style="left:{x}px;top:506px;width:302px;height:210px"><div class="abs lbl" style="left:20px;top:18px">{h}</div>'
              f'<div class="abs" style="left:20px;top:52px;width:262px;font-size:18px;line-height:26px">{d}</div></div>')
    b += '<div class="panel" style="top:750px;height:110px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">In Vaulted</div><div class="abs" style="right:26px;top:0;height:100%;width:640px;display:flex;align-items:center;font-size:18px;line-height:25px;color:var(--s)">Set a reserve on each loan, mark payments paid from it, and see what is left and how many months it covers.</div></div>'
    return b

def clear(t):
    steps = [("1", "Checklist", "Add conditions to a loan, each with an owner."), ("2", "Borrower uploads", "Requested files arrive through the borrower portal."),
             ("3", "Accept or return", "Accept a file, or send it back with a note."), ("4", "Clear to close", "Blocking items stop the move to closing unless overridden.")]
    b = ""
    for i, (n, h, d) in enumerate(steps):
        x = 68 + i * 238
        b += (f'<div class="card" style="left:{x}px;top:300px;width:222px;height:250px">'
              f'<div class="abs mono" style="left:20px;top:20px;width:36px;height:36px;border-radius:50%;background:#C9A84C;color:#0B1F3A;display:flex;align-items:center;justify-content:center;font-size:19px">{n}</div>'
              f'<div class="abs" style="left:20px;top:72px;width:184px;font-size:21px;font-weight:700">{h}</div>'
              f'<div class="abs steel" style="left:20px;top:108px;width:184px;font-size:16.5px;line-height:24px">{d}</div></div>')
    b += ('<div class="card" style="left:68px;top:580px;width:944px;height:120px"><div class="abs lbl" style="left:24px;top:18px">Why lenders do it</div>'
          '<div class="abs" style="left:24px;top:48px;width:896px;font-size:19px;line-height:27px">A closing checklist can show what is still open before money moves. What a lender requires varies by lender and by state.</div></div>')
    b += ('<div class="abs" style="left:68px;top:735px"><span class="pill">All plans: closing conditions</span> &nbsp;<span class="pill">Operator and Fund: borrower document requests</span></div>')
    b += '<div class="panel" style="top:790px;height:84px"><div class="abs mono gold" style="left:26px;top:0;height:100%;display:flex;align-items:center;font-size:22px">30-day trial</div><div class="abs" style="right:26px;top:0;height:100%;width:620px;display:flex;align-items:center;font-size:18px;line-height:25px;color:var(--s)">Full access, no card required. Plans start at $99 a month.</div></div>'
    return b

M = {
 "A-draws-dark": ("dark", draws, "NEW IN VAULTED", "DRAWS, EXPLAINED", "Fund only the work", "that is in place", "A request is not a verified percentage complete", 
    "Illustrative figures only: $120,000 budget, 45% verified = $54,000. Feature live Nov 15, 2026.", 905),
 "A-draws-light": ("light", draws, "NEW IN VAULTED", "DRAWS, EXPLAINED", "Fund only the work", "that is in place", "A request is not a verified percentage complete",
    "Illustrative figures only: $120,000 budget, 45% verified = $54,000. Feature live Nov 15, 2026.", 905),
 "B-reserve-light": ("light", reserve, "LENDER BASICS + VAULTED", "INTEREST RESERVES", "How many months", "does the reserve cover?", "A worked example, then where it lives in Vaulted",
    "Illustrative figures only. Arithmetic: 18,000 / 2,400 = 7.5. Definitions vary by loan agreement.", 905),
 "B-reserve-dark": ("dark", reserve, "LENDER BASICS + VAULTED", "INTEREST RESERVES", "How many months", "does the reserve cover?", "A worked example, then where it lives in Vaulted",
    "Illustrative figures only. Arithmetic: 18,000 / 2,400 = 7.5. Definitions vary by loan agreement.", 905),
 "C-clear-dark": ("dark", clear, "INSIDE VAULTED", "CLOSING CONDITIONS", "Clear to close,", "tracked in one place", "From checklist to closing, with borrower documents in the loan",
    "Source: vaultedonline.com feature and pricing pages. Plans and prices as shown on the site; confirm before publishing.", 905),
}
if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch()
        for k, (t, fn, tag, eb, a, b2, sub, foot, ft) in M.items():
            body = fn(t)
            s = "#A5B2C3" if t == "dark" else "#3F5470"
            html = page(t, tag, eb, a, b2, sub, body, foot, ft).replace("var(--s)", s).replace("var(--x,rgba(128,140,160,.18))", "rgba(90,107,130,.30)" if t == "dark" else "rgba(11,31,58,.10)")
            pg = br.new_page(viewport={"width": 1080, "height": 1080}, device_scale_factor=2)
            pg.set_content(html); pg.screenshot(path=f"{out}/{k}.png"); pg.close()
        br.close()
    print("ok")
