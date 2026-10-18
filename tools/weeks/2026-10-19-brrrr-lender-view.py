#!/usr/bin/env python3
"""Graphic for the BRRRR lender-view post (Facebook, Fri Oct 23, 2026 12:47 pm ET). Built Oct 18, 2026.
Run from repo root: python3 tools/weeks/2026-10-19-brrrr-lender-view.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ARV, PAYOFF = 260000, 178000          # illustrative
BASE = ARV * 0.75                      # 195,000
CAP70 = ARV * 0.70                     # 182,000
LOW = ARV * 0.90 * 0.75                # 175,500


def gfx():
    assert (BASE, CAP70, LOW) == (195000, 182000, 175500)
    assert (BASE - PAYOFF, CAP70 - PAYOFF, LOW - PAYOFF) == (17000, 4000, -2500)
    b = '<div class="abs lbl" style="left:68px;top:268px">Illustrative bridge loan and exit</div>'
    b += stat_card(68, 300, 290, 150, "$260,000", "after-repair value", "illustrative")
    b += stat_card(395, 300, 290, 150, "$178,000", "bridge payoff", "illustrative")
    b += stat_card(722, 300, 290, 150, "75%", "refinance LTV", "varies by lender")
    b += '<div class="abs lbl" style="left:68px;top:480px">Refinance proceeds vs. the $178,000 payoff</div>'

    X0, S, H = 250, 560 / 200000, 54
    rows = [("Base case", "75% of $260,000", BASE, "seg-gold", "+$17,000", "cushion"),
            ("70% cap", "70% of $260,000", CAP70, "seg-blue", "+$4,000", "cushion"),
            ("Value 10% lower", "75% of $234,000", LOW, "seg-steel", "-$2,500", "short")]
    top0, gap = 520, 76
    for i, (a, a2, v, cls, d, w) in enumerate(rows):
        y = top0 + i * gap
        b += (f'<div class="abs" style="left:68px;top:{y}px;width:170px;height:{H}px;display:flex;flex-direction:column;justify-content:center">'
              f'<div style="font-size:19px;line-height:24px;font-weight:700">{a}</div>'
              f'<div style="font-size:14px;line-height:18px;color:#8A9BB0">{a2}</div></div>')
        b += (f'<div class="abs {cls} mono" style="left:{X0}px;top:{y}px;width:{v * S:.1f}px;height:{H}px;border-radius:8px;'
              f'display:flex;align-items:center;padding-left:14px;font-size:20px">${v:,.0f}</div>')
        b += (f'<div class="abs" style="left:{X0 + v * S + 14:.1f}px;top:{y}px;width:120px;height:{H}px;display:flex;flex-direction:column;justify-content:center">'
              f'<div class="mono gold" style="font-size:20px;line-height:24px">{d}</div>'
              f'<div style="font-size:14px;line-height:18px;color:#A5B2C3">{w}</div></div>')
    px = X0 + PAYOFF * S
    b += (f'<div class="abs" style="left:{px:.1f}px;top:{top0 - 16}px;height:{2 * gap + H + 32}px;border-left:2px dashed rgba(226,194,101,.9)"></div>')
    b += (f'<div class="abs" style="left:{px - 60:.1f}px;top:{top0 + 2 * gap + H + 18}px;width:120px;text-align:center;font-size:14px;color:#E2C265">payoff $178,000</div>')
    b += panel(790, 100, "DOES THE EXIT COVER IT?",
               "The refinance is the repayment source. Test it against a lower value and a lower LTV.", 440, 24)
    foot = ("Sources: Kiavi, DSCR Loan for BRRRR (May 11, 2026): cash-out is &quot;typically in the 70-75% range&quot; of appraised value; a low appraisal may limit the cash out. "
            "iPropertyManagement, BRRRR guide (updated Sep 4, 2026): some lenders cap investment property cash-out at 70%. "
            "Illustrative: ARV $260,000; payoff $178,000. $260,000 x 0.75 = $195,000; x 0.70 = $182,000; $260,000 x 0.90 x 0.75 = $175,500.")
    return shell("The refinance is the repayment source.", "Does it cover the payoff?",
                 "BRRRR exit test, illustrative numbers", b, foot, 912,
                 eyebrow="PRIVATE LENDING, EXPLAINED")


PAGES = {"brrrr-lender-view": ("images/2026-10-23/1247-fb-brrrr-lender-view.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
