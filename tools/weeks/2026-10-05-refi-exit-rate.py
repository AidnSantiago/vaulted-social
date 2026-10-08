#!/usr/bin/env python3
"""Graphic for the refinance-exit post (Freddie Mac PMMS, rates as of Oct 1, 2026; Facebook, Thu Oct 8, 2026 12:47 pm ET). Built Oct 7, 2026.
Run from repo root:  python3 tools/weeks/2026-10-05-refi-exit-rate.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, R_OLD, R_NEW = 325000, 6.34, 7.28   # illustrative payoff; Freddie Mac PMMS 30-year rates (a year ago, Oct 1, 2026)


def pmt(principal, annual_pct, years=30):
    """Monthly principal-and-interest payment on a fixed-rate loan."""
    r = annual_pct / 100 / 12
    n = years * 12
    return principal * r / (1 - (1 + r) ** -n)


def gfx():
    pay_old, pay_new = pmt(LOAN, R_OLD), pmt(LOAN, R_NEW)
    supported = pay_old / pmt(1, R_NEW)          # loan the old payment supports at the new rate
    gap = LOAN - supported
    more = pay_new - pay_old
    pct = (pay_new / pay_old - 1) * 100
    # the numbers printed below must match the post and the footnote
    assert f"${round(pay_old):,}" == "$2,020" and f"${round(pay_new):,}" == "$2,224" and f"${round(more):,}" == "$204"
    assert f"{pct:.1f}" == "10.1" and f"${round(supported, -3):,.0f}" == "$295,000" and f"${round(gap, -3):,.0f}" == "$30,000"
    assert f"${supported:,.0f}" == "$295,251" and f"${gap:,.0f}" == "$29,749"

    X0, S = 232, 560 / LOAN
    y1, y2, H = 538, 610, 56
    b = '<div class="abs lbl" style="left:68px;top:268px">Monthly payment on a $325,000, 30-year loan</div>'
    b += stat_card(68, 300, 290, 150, "$2,020", "a month at 6.34%", "$325,000 loan, a year ago")
    b += stat_card(395, 300, 290, 150, "$2,224", "a month at 7.28%", "$325,000 loan, Oct 1, 2026")
    b += stat_card(722, 300, 290, 150, "+$204", "more each month", "10.1% higher, same loan")

    b += '<div class="abs lbl" style="left:68px;top:498px">What the same $2,020 payment can refinance</div>'

    def lab(y, big, small):
        return (f'<div class="abs" style="left:68px;top:{y}px;width:156px;height:{H}px;display:flex;flex-direction:column;justify-content:center">'
                f'<div style="font-size:19px;line-height:24px;font-weight:700">{big}</div>'
                f'<div style="font-size:14.5px;line-height:18px;color:#8A9BB0">{small}</div></div>')
    b += lab(y1, "At 6.34%", "a year ago") + lab(y2, "At 7.28%", "Oct 1, 2026")
    b += (f'<div class="abs seg-blue mono" style="left:{X0}px;top:{y1}px;width:{LOAN * S:.1f}px;height:{H}px;border-radius:8px;'
          f'display:flex;align-items:center;padding-left:16px;font-size:21px">$325,000</div>')
    b += (f'<div class="abs seg-gold mono" style="left:{X0}px;top:{y2}px;width:{supported * S:.1f}px;height:{H}px;border-radius:8px 0 0 8px;'
          f'display:flex;align-items:center;padding-left:16px;font-size:21px">$295,000</div>')
    gx = X0 + supported * S
    b += (f'<div class="abs" style="left:{gx:.1f}px;top:{y2}px;width:{gap * S:.1f}px;height:{H}px;border-radius:0 8px 8px 0;'
          f'border:1.5px dashed rgba(226,194,101,.85);border-left:none;'
          f'background:repeating-linear-gradient(135deg,rgba(226,194,101,.22) 0 6px,rgba(226,194,101,0) 6px 12px)"></div>')
    end = X0 + LOAN * S
    b += (f'<div class="abs" style="left:{end - 1:.1f}px;top:{y1 - 12}px;height:{y2 + H - y1 + 24}px;'
          f'border-left:2px dashed rgba(226,194,101,.9)"></div>')
    b += (f'<div class="abs" style="left:{end + 16:.1f}px;top:{y2}px;width:190px;height:{H}px;display:flex;flex-direction:column;justify-content:center">'
          f'<div class="mono gold" style="font-size:22px;line-height:26px">$30,000</div>'
          f'<div style="font-size:14.5px;line-height:18px;color:#A5B2C3">short of the payoff</div></div>')
    b += panel(726, 96, "SAME PAYMENT, SMALLER LOAN",
               "When rates rise, a refinance sized by the payment can fall short of the payoff.", 440, 24)
    foot = ("Source: Freddie Mac, Primary Mortgage Market Survey, as of Oct 1, 2026: 30-year fixed-rate mortgage averaged 7.28%, up from 6.34% a&nbsp;year&nbsp;ago (Oct 2, 2025). "
            "The survey covers owner-occupied purchase loans, so investor rates differ. "
            "Illustrative: $325,000, 30-year fixed, principal and interest. Payment = L x r / (1 - (1 + r)^-n), r = rate / 12, n = 360: "
            "$2,020.14 at 6.34%, $2,223.69 at 7.28% (+$203.55, +10.1%). "
            "$2,020.14 supports $295,251 at 7.28%; $325,000 - $295,251 = $29,749. Rounded: $204, $295,000, $30,000.")
    return shell("30-year rate up from 6.34% to 7.28%.", "The same payment refinances less.",
                 "Freddie Mac survey, Oct 1, 2026 &middot; illustrative $325,000 refinance", b, foot, 856,
                 eyebrow="MARKET DATA FOR PRIVATE LENDERS")


PAGES = {"refi-exit-rate": ("images/2026-10-08/1247-fb-refi-exit-rate.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
