#!/usr/bin/env python3
"""Graphic for retainage vs. rehab holdback (Facebook, Fri Oct 9, 2026 12:47 pm ET).
Run from repo root: python3 tools/weeks/2026-10-05-retainage-vs-holdback.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Illustrative inputs (chosen for the example, not market figures)
HOLDBACK = 64000                         # rehab holdback the lender keeps back
CONTRACT = 48000                         # contractor contract
RATE = 10                                # retainage, percent
# Computed in Python
RETAINAGE = CONTRACT * RATE // 100       # 4800
PAID = CONTRACT - RETAINAGE              # 43200
REST = HOLDBACK - CONTRACT               # 16000 (drawn only as an unlabeled remainder)
BAR_W = 944
S = BAR_W / HOLDBACK                     # px per dollar; both bars share one scale
X0 = 68


def money(n):
    return f"${n:,}"


def comp_card(x, y, w, h, name, big, sub, rows):
    """Comparison card: gold caps name, big mono number, one steel line, then a 4-row label/value table."""
    s = f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
    s += f'<div class="abs lbl" style="left:22px;top:20px">{name}</div>'
    s += f'<div class="abs mono gold" style="left:22px;top:44px;font-size:54px;line-height:62px;white-space:nowrap">{big}</div>'
    s += f'<div class="abs" style="left:22px;top:112px;width:{w - 44}px;font-size:17px;line-height:22px;color:#A5B2C3;white-space:nowrap">{sub}</div>'
    for i, (k, v) in enumerate(rows):
        yy = 152 + i * 31
        s += (f'<div class="abs" style="left:22px;top:{yy}px;width:100px;height:28px;display:flex;align-items:center;'
              f'font-size:13.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#8A9BB0">{k}</div>')
        s += (f'<div class="abs" style="left:128px;top:{yy}px;width:{w - 128 - 14}px;height:28px;display:flex;align-items:center;'
              f'font-size:18px;color:#F0EDE4;white-space:nowrap">{v}</div>')
    return s + '</div>'


def gfx():
    b = comp_card(68, 262, 462, 286, "Rehab holdback", money(HOLDBACK), "part of the loan, kept back by the lender", [
        ("Held by", "the lender"),
        ("Purpose", "funds the rehab as work is verified"),
        ("Released", "in draws"),
        ("Set in", "the loan documents"),
    ])
    b += comp_card(550, 262, 462, 286, "Contractor retainage", money(RETAINAGE), f"{RATE}% of a {money(CONTRACT)} contract", [
        ("Held by", "the property owner"),
        ("Purpose", "leverage to finish the job"),
        ("Released", "at completion, per the contract"),
        ("Set in", "the construction contract"),
    ])
    # ---- bars on one scale
    y1, y2, H = 574, 630, 46
    b += (f'<div class="abs seg-steel mono" style="left:{X0}px;top:{y1}px;width:{HOLDBACK * S:.1f}px;height:{H}px;border-radius:10px;'
          f'display:flex;align-items:center;padding-left:16px;font-size:18px;white-space:nowrap">{money(HOLDBACK)} rehab holdback</div>')
    b += (f'<div class="abs seg-blue" style="left:{X0}px;top:{y2}px;width:{PAID * S:.1f}px;height:{H}px;border-radius:10px 0 0 10px;'
          f'display:flex;align-items:center;padding-left:16px;font-size:18px;white-space:nowrap">'
          f'<span class="mono">{money(PAID)}</span>&nbsp;paid as work progresses</div>')
    b += (f'<div class="abs seg-gold mono" style="left:{X0 + PAID * S:.1f}px;top:{y2}px;width:{RETAINAGE * S:.1f}px;height:{H}px;'
          f'display:flex;align-items:center;justify-content:center;font-size:17px">{RATE}%</div>')
    b += (f'<div class="abs" style="left:{X0 + CONTRACT * S:.1f}px;top:{y2}px;width:{REST * S:.1f}px;height:{H}px;border-radius:0 10px 10px 0;'
          f'border:1.5px dashed rgba(138,155,176,.5);border-left:none;display:flex;align-items:center;justify-content:center;'
          f'font-size:15px;color:#8A9BB0">rest of the holdback</div>')
    # bracket under the contract bar
    cw = CONTRACT * S
    b += (f'<svg class="abs" style="left:{X0}px;top:{y2 + H + 6}px" width="{cw:.1f}" height="12" viewBox="0 0 {cw:.1f} 12">'
          f'<path d="M1 0 V10 H{cw - 1:.1f} V0" fill="none" stroke="#8A9BB0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    b += (f'<div class="abs" style="left:{X0}px;top:{y2 + H + 22}px;width:{cw:.1f}px;text-align:center;font-size:17px;font-weight:700;color:#F0EDE4">'
          f'{money(CONTRACT)} contractor contract</div>')
    # ---- takeaway panel
    b += panel(742, 96, f"{RATE}% &times; {money(CONTRACT)} = {money(RETAINAGE)}",
               "Paying the contractor in full from every draw gives that leverage away. The holdback does not replace it.", 440, 26)
    foot = ("Sources: Corpay, Construction Retainage Explained (updated Jun 1, 2026); Snell &amp; Wilmer, Retainage in the Southwest (Jun 12, 2024);<br>"
            "Kiavi, How the Fix-and-Flip Draw Process Works (Jun 15, 2026); AAPL, Understanding Draw Management (Jul 24, 2023);<br>"
            "OnlineEd, Holdback (Feb 4, 2026). Retainage is often 5 to 10 percent; terms vary by state, contract and lender. Not legal advice.<br>"
            f"Illustrative example: {RATE}% &times; {money(CONTRACT)} = {money(RETAINAGE)}; "
            f"{money(CONTRACT)} &minus; {money(RETAINAGE)} = {money(PAID)}.")
    return shell("Rehab holdback is not retainage.", "Two holds, two different jobs.",
                 f"Illustrative rehab, drawn to scale: {money(HOLDBACK)} holdback, {money(CONTRACT)} contract",
                 b, foot, 862)


PAGES = {"retainage-vs-holdback": ("images/2026-10-09/1247-fb-retainage-vs-holdback.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
