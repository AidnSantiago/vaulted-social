#!/usr/bin/env python3
"""Graphic for lien-position-explained (Facebook, Mon Oct 19, 2026 12:47 pm ET). Illustrative waterfall.
Run from repo root:  python3 tools/weeks/2026-10-19-lien-position-explained.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

L1, L2, L3, COST = 200000, 60000, 25000, 0.06   # illustrative
X0, S = 220, 330 / 200000
ROWH = 32


def scenario(price):
    net = price - round(price * COST)
    rem, rows = net, []
    for name, owed in (("1st lien", L1), ("2nd lien", L2), ("3rd lien", L3)):
        paid = min(rem, owed)
        rem -= paid
        rows.append((name, owed, paid))
    return net, rows, rem


def fmt(n):
    return "${:,.0f}".format(n)


def block(top, title, price):
    net, rows, left = scenario(price)
    b = f'<div class="abs lbl" style="left:68px;top:{top}px">{title}</div>'
    y = top + 30

    def row(y, label, owed, paid, cls, status, scol):
        r = (f'<div class="abs" style="left:68px;top:{y}px;width:146px;height:26px;display:flex;align-items:center;font-size:18px;font-weight:700">{label}</div>')
        if owed > paid:   # dashed outline for the unpaid part of the claim
            r += (f'<div class="abs" style="left:{X0}px;top:{y}px;width:{owed * S:.1f}px;height:26px;border:1.5px dashed rgba(226,194,101,.8);border-radius:5px"></div>')
        if paid > 0:
            r += (f'<div class="abs {cls}" style="left:{X0}px;top:{y}px;width:{paid * S:.1f}px;height:26px;border-radius:5px"></div>')
        tx = X0 + max(paid, owed) * S + 10
        r += (f'<div class="abs mono" style="left:{tx:.1f}px;top:{y}px;height:26px;display:flex;align-items:center;font-size:16px;color:#F0EDE4;white-space:nowrap">{fmt(paid)}</div>')
        r += (f'<div class="abs" style="left:868px;top:{y}px;height:26px;display:flex;align-items:center;font-size:16px;font-weight:700;color:{scol};white-space:nowrap">{status}</div>')
        return r

    b += row(y, "Net sale", net, net, "seg-steel", "after 6% costs", "#8A9BB0"); y += ROWH
    for name, owed, paid in rows:
        if paid == owed:
            st, col, cls = "paid in full", "#E2C265", "seg-gold"
        else:
            st, col, cls = f"short {fmt(owed - paid)}", "#F0A090", "seg-gold"
        b += row(y, name, owed, paid, cls, st, col); y += ROWH
    b += row(y, "Owner", left, left, "seg-blue", "left over" if left else "nothing left", "#8A9BB0")
    return b


def gfx():
    n1, r1, left1 = scenario(310000)
    n2, r2, left2 = scenario(270000)
    assert (n1, left1) == (291400, 6400) and [p for _, _, p in r1] == [200000, 60000, 25000]
    assert (n2, left2) == (253800, 0) and [p for _, _, p in r2] == [200000, 53800, 0]
    b = block(262, "Sells for $310,000", 310000)
    b += block(496, "Sells for $270,000", 270000)
    b += panel(740, 84, "PAID IN ORDER", "A lower sale price hits the junior liens first.", 380, 26)
    foot = ("Sources: Rocket Mortgage, First lien vs. second lien (updated Sep 26, 2026): the first lienholder is paid in full and the second is paid from what is left over. "
            "Nolo, What Is Lien Priority (page undated, accessed 2026-10-18): a lien with low priority might get nothing from a foreclosure sale. Some liens can rank out of order under state law. "
            "Illustrative: liens $200,000 / $60,000 / $25,000; 6% selling costs. 310,000 - 18,600 = 291,400; 270,000 - 16,200 = 253,800.")
    return shell("First lien gets paid first.", "Junior liens take the shortfall.",
                 "Illustrative sale proceeds, paid in lien order &middot; priority rules vary by state", b, foot, 856)


PAGES = {"lien-position-explained": ("images/2026-10-19/1247-fb-lien-position-explained.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
