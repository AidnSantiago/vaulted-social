#!/usr/bin/env python3
"""Graphic for loss severity math (Facebook, Wed Nov 4, 2026 12:47 pm ET). Run from repo root: python3 tools/weeks/2026-11-02-loss-severity-math.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

BAL, INT, COST, SALE, SELL = 290000, 19000, 13000, 305000, 0.08  # illustrative


def gfx():
    net = SALE * (1 - SELL)
    owed = BAL + INT + COST
    loss = owed - net
    assert net == 280600 and owed == 322000 and loss == 41400
    assert round(loss / BAL * 100, 1) == 14.3 and round((BAL + COST - net) / BAL * 100, 1) == 7.7
    W = 944
    sc = W / owed
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative foreclosure sale</div>'
    # bar 1: owed
    b += '<div class="abs steel" style="left:68px;top:306px;font-size:18px;font-weight:700">What the lender is owed: $322,000</div>'
    x = 68
    for w, cls, lab, col in ((BAL, "seg-blue", "$290,000 balance", "#F0EDE4"), (INT, "seg-steel", "", "#F0EDE4"), (COST, "seg-blue2", "", "#F0EDE4")):
        ww = w * sc
        b += (f'<div class="abs {cls}" style="left:{x:.1f}px;top:340px;width:{ww:.1f}px;height:56px;border-radius:6px"></div>'
              f'<div class="abs mono" style="left:{x:.1f}px;top:340px;width:{ww:.1f}px;height:56px;display:flex;align-items:center;justify-content:center;font-size:15px;color:{col}">{lab}</div>')
        x += ww
    b += '<div class="abs mono steel" style="right:68px;top:402px;font-size:14px;white-space:nowrap;text-align:right">$19,000 interest (steel), $13,000 costs (blue)</div>'
    # bar 2: net proceeds + gap
    b += '<div class="abs steel" style="left:68px;top:462px;font-size:18px;font-weight:700">What the sale nets: $305,000 less 8% = $280,600</div>'
    nw = net * sc
    b += (f'<div class="abs seg-blue" style="left:68px;top:496px;width:{nw:.1f}px;height:56px;border-radius:6px"></div>'
          f'<div class="abs mono" style="left:68px;top:496px;width:{nw:.1f}px;height:56px;display:flex;align-items:center;justify-content:center;font-size:17px;color:#F0EDE4">$280,600 net</div>')
    gw = loss * sc
    b += (f'<div class="abs seg-gold" style="left:{68 + nw:.1f}px;top:496px;width:{gw:.1f}px;height:56px;border-radius:6px"></div>'
          f'<div class="abs mono" style="left:{68 + nw:.1f}px;top:496px;width:{gw:.1f}px;height:56px;display:flex;align-items:center;justify-content:center;font-size:16px;color:#0B1F3A">$41,400</div>')
    b += f'<div class="abs mono gold" style="left:{68 + nw:.1f}px;top:558px;font-size:14px;white-space:nowrap">loss</div>'
    # stat cards
    b += '<div class="abs lbl" style="left:68px;top:604px">Same loss, two definitions</div>'
    b += stat_card(68, 640, 462, 150, "14.3%", "with lost interest", "$41,400 / $290,000 balance", 46)
    b += stat_card(550, 640, 462, 150, "7.7%", "without lost interest", "$22,400 / $290,000 balance", 46)
    b += panel(810, 76, "Loss / unpaid balance", "State which definition you use.", 330, 25)
    foot = ("Sources: Federal Reserve Bank of Philadelphia, Mortgage Loss Severities: What Keeps Them So High?, WP 20-37, Sept 2020; "
            "Urban Institute, Loss Severity on Residential Mortgages, Feb 2015. Illustrative inputs. "
            "Arithmetic: 305,000 x 0.92 = 280,600; 290,000 + 19,000 + 13,000 = 322,000; 322,000 - 280,600 = 41,400; 41,400 / 290,000 = 14.3%; 22,400 / 290,000 = 7.7%.")
    return shell("A sale price is not a recovery.", "Loss severity shows the gap.",
                 "Net loss as a share of the unpaid balance &middot; illustrative", b, foot, 902)


PAGES = {"loss-severity-math": ("images/2026-11-04/1247-fb-loss-severity-math.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
