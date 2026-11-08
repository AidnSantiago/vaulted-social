#!/usr/bin/env python3
"""Graphic for portfolio yield, weighted average (Facebook, Wed Nov 11, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-09-portfolio-yield-weighted-avg.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOANS = [(205000, 9.5), (415000, 11.25), (435000, 12.5)]  # illustrative
INT = [b * r / 100 for b, r in LOANS]
TOT, TINT = sum(b for b, _ in LOANS), sum(INT)
SIMPLE, WEIGHTED = sum(r for _, r in LOANS) / 3, TINT / TOT * 100
assert INT == [19475.0, 46687.5, 54375.0] and TOT == 1055000 and TINT == 120537.5
assert round(SIMPLE, 2) == 11.08 and round(WEIGHTED, 2) == 11.43


def money(v):
    return f"${v:,.2f}" if v != int(v) else f"${int(v):,}"


def gfx():
    b = '<div class="abs lbl" style="left:68px;top:262px">Illustrative three-loan portfolio</div>'
    b += '<div class="card" style="left:68px;top:292px;width:944px;height:262px"></div>'
    for x, t, al in [(92, "Balance", "left"), (300, "Bar length = balance", "left"), (690, "Rate", "left"), (800, "Annual interest", "left")]:
        b += f'<div class="abs steel" style="left:{x}px;top:306px;font-size:14px;white-space:nowrap">{t}</div>'
    y = 336
    for (bal, r), i in zip(LOANS, INT):
        w = round(360 * bal / 435000)
        b += f'<div class="abs mono" style="left:92px;top:{y}px;font-size:22px;line-height:30px;white-space:nowrap">{money(bal)}</div>'
        b += f'<div class="abs seg-blue" style="left:300px;top:{y+2}px;width:{w}px;height:26px;border-radius:6px"></div>'
        b += f'<div class="abs mono gold" style="left:690px;top:{y}px;font-size:22px;line-height:30px;white-space:nowrap">{r:g}%</div>'
        b += f'<div class="abs mono" style="left:800px;top:{y}px;font-size:22px;line-height:30px;white-space:nowrap">{money(i)}</div>'
        y += 46
    b += '<div class="abs" style="left:92px;top:480px;width:896px;height:1px;background:rgba(138,155,176,.35)"></div>'
    b += f'<div class="abs mono" style="left:92px;top:494px;font-size:22px;line-height:30px;white-space:nowrap">{money(TOT)}</div>'
    b += '<div class="abs steel" style="left:300px;top:498px;font-size:16px;white-space:nowrap">Total balance</div>'
    b += f'<div class="abs mono gold" style="left:800px;top:494px;font-size:22px;line-height:30px;white-space:nowrap">{money(TINT)}</div>'
    b += stat_card(68, 584, 458, 150, f"{SIMPLE:.2f}%", "Simple average", "(9.5 + 11.25 + 12.5) / 3")
    b += stat_card(554, 584, 458, 150, f"{WEIGHTED:.2f}%", "Weighted by balance", "$120,537.50 / $1,055,000")
    b += panel(764, 100, "Weight by balance", "The largest balance carries the highest rate, so the simple average understates yield.", 430, 25)
    foot = ("Sources: CFPB, Should I consolidate or refinance my student loans?, last reviewed Dec 3, 2024 (weighted average of loan rates); "
            "FINRA, MBS Data Glossary, page undated, accessed 2026-11-08 (pool WAC). Illustrative inputs. "
            "Arithmetic: 205,000 x 9.5% = 19,475; 415,000 x 11.25% = 46,687.50; 435,000 x 12.5% = 54,375; 120,537.50 / 1,055,000 = 11.43%.")
    return shell("Blended portfolio yield", "is a weighted average.",
                 "Simple vs balance-weighted &middot; illustrative", b, foot, 884)


PAGES = {"portfolio-yield-weighted-avg": ("images/2026-11-11/1247-fb-portfolio-yield-weighted-avg.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
