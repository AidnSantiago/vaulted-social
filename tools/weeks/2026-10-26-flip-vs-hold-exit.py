#!/usr/bin/env python3
"""Graphic for flip-vs-hold-exit (Facebook, Sun Nov 1, 2026 1:47 pm ET). Illustrative numbers.
Run from repo root: python3 tools/weeks/2026-10-26-flip-vs-hold-exit.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ARV, LOAN, COST, RENT, PAY_A, PAY_B = 300000, 210000, 0.06, 2400, 2050, 2600  # illustrative


def row(x, y, w, label, val, color="#F0EDE4", bold=False):
    fw = "700" if bold else "400"
    return (f'<div class="abs" style="left:{x}px;top:{y}px;font-size:19px;color:#A5B2C3;white-space:nowrap">{label}</div>'
            f'<div class="abs mono" style="left:{x + w - 190}px;top:{y - 2}px;width:190px;text-align:right;font-size:22px;color:{color};font-weight:{fw};white-space:nowrap">{val}</div>')


def line(x, y, w):
    return f'<div class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:1px;background:rgba(138,155,176,.35)"></div>'


def gfx():
    costs = ARV * COST
    net = ARV - costs
    left = net - LOAN
    cov_a, cov_b = RENT / PAY_A, RENT / PAY_B
    assert costs == 18000 and net == 282000 and left == 72000
    assert f"{cov_a:.2f}" == "1.17" and f"{cov_b:.2f}" == "0.92"
    b = ""
    # left card: flip
    b += '<div class="card" style="left:68px;top:268px;width:458px;height:420px"></div>'
    b += '<div class="abs lbl" style="left:92px;top:290px">Exit 1: flip</div>'
    b += '<div class="abs" style="left:92px;top:316px;font-size:24px;font-weight:700;color:#F0EDE4">A sale repays the loan</div>'
    x, w = 92, 410
    b += row(x, 372, w, "Sale at ARV", "$300,000")
    b += row(x, 412, w, "Selling costs, 6%", "-$18,000", "#A5B2C3")
    b += line(x, 448, w)
    b += row(x, 462, w, "Net proceeds", "$282,000", "#F0EDE4", True)
    b += row(x, 502, w, "Loan repaid", "-$210,000", "#A5B2C3")
    b += line(x, 538, w)
    b += row(x, 552, w, "Left over", "$72,000", "#E2C265", True)
    b += '<div class="abs" style="left:92px;top:604px;width:410px;font-size:16px;line-height:22px;color:#8A9BB0">Before interest and other costs. The repayment source is the sale price.</div>'
    # right card: hold
    b += '<div class="card" style="left:554px;top:268px;width:458px;height:420px"></div>'
    b += '<div class="abs lbl" style="left:578px;top:290px">Exit 2: hold</div>'
    b += '<div class="abs" style="left:578px;top:316px;font-size:24px;font-weight:700;color:#F0EDE4">A refinance repays the loan</div>'
    x = 578
    b += row(x, 372, w, "Monthly rent", "$2,400")
    b += line(x, 408, w)
    b += '<div class="abs" style="left:578px;top:420px;font-size:15px;font-weight:700;letter-spacing:.12em;color:#8A9BB0">RENT / PAYMENT = COVERAGE</div>'
    b += row(x, 456, w, "$2,400 / $2,050", "1.17", "#E2C265", True)
    b += row(x, 496, w, "$2,400 / $2,600", "0.92", "#C98A7A", True)
    b += '<div class="abs" style="left:578px;top:540px;width:410px;font-size:16px;line-height:22px;color:#A5B2C3">One lender says rent must at least equal the payment, a 1.0 floor. Floors vary by lender.</div>'
    b += '<div class="abs" style="left:578px;top:604px;width:410px;font-size:16px;line-height:22px;color:#8A9BB0">The repayment source is a new lender, sized off value and rent.</div>'
    b += panel(716, 96, "SAME LOAN", "Test the exit the borrower plans: price for a flip, rent and value for a hold.", 560, 28)
    foot = ("Sources: Lendmire, Hard Money Loan Exit Strategy for Real Estate Investors (last reviewed Oct 15, 2026); North Coast Financial, 5 Hard Money Loan Exit Strategies "
            "(modified Sep 23, 2026); Ridge Street Capital, Fix to Rent Loans (updated Oct 9, 2026). Illustrative: $300,000 ARV, $210,000 loan, 6% selling costs, $2,400 rent, "
            "$2,050 and $2,600 payments. 300,000 x 6% = 18,000; 300,000 - 18,000 = 282,000; 282,000 - 210,000 = 72,000; 2,400 / 2,050 = 1.17; 2,400 / 2,600 = 0.92.")
    return shell("One $210,000 loan, two exits.",
                 "Two ways to get repaid.",
                 "A flip depends on a sale price. A hold depends on a refinance.", b, foot, 836)


PAGES = {"flip-vs-hold-exit": ("images/2026-11-01/1347-fb-flip-vs-hold-exit.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
