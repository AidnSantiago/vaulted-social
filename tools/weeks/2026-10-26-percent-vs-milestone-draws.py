#!/usr/bin/env python3
"""Graphic for percent-complete vs milestone draws (Facebook, Fri Oct 30, 2026 12:47 pm ET).
Run from repo root: python3 tools/weeks/2026-10-26-percent-vs-milestone-draws.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, render

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Illustrative inputs (chosen for the example, not market figures)
BUDGET = 120000
PCT = 50                      # verified percent complete
N_CHECK = 4                   # hypothetical number of equal checkpoints
# Computed in Python
EARNED = BUDGET * PCT // 100          # 60000
CHECK = BUDGET // N_CHECK             # 30000
MS_RELEASED = CHECK * 1               # only first checkpoint verified: 30000
X0, W = 68, 944
S = W / BUDGET


def m(n):
    return f"${n:,}"


def bar_row(y, label, sub):
    return (f'<div class="abs lbl" style="left:{X0}px;top:{y}px">{label}</div>'
            f'<div class="abs" style="left:{X0}px;top:{y + 24}px;font-size:17px;color:#A5B2C3;white-space:nowrap">{sub}</div>')


def gfx():
    b = ""
    # budget bar
    b += f'<div class="abs lbl" style="left:{X0}px;top:262px">The budget</div>'
    b += (f'<div class="abs seg-steel mono" style="left:{X0}px;top:290px;width:{W}px;height:44px;border-radius:10px;'
          f'display:flex;align-items:center;justify-content:center;font-size:20px">{m(BUDGET)} rehab budget</div>')
    # percent-complete
    y = 360
    b += bar_row(y, "Percent complete", f"Inspector verifies {PCT}% done: {PCT}% &times; {m(BUDGET)}")
    yb = y + 58
    b += (f'<div class="abs seg-gold mono" style="left:{X0}px;top:{yb}px;width:{EARNED * S:.1f}px;height:50px;border-radius:10px 0 0 10px;'
          f'display:flex;align-items:center;justify-content:center;font-size:22px">{m(EARNED)} earned</div>')
    b += (f'<div class="abs" style="left:{X0 + EARNED * S:.1f}px;top:{yb}px;width:{(BUDGET - EARNED) * S:.1f}px;height:50px;border-radius:0 10px 10px 0;'
          f'border:1.5px dashed rgba(138,155,176,.5);border-left:none;display:flex;align-items:center;justify-content:center;'
          f'font-size:16px;color:#8A9BB0">not yet earned</div>')
    # milestone
    y = 540
    b += bar_row(y, "Milestone (hypothetical)", f"{N_CHECK} equal checkpoints of {m(CHECK)}; only the first is verified")
    yb = y + 58
    for i in range(N_CHECK):
        x = X0 + i * CHECK * S
        if i == 0:
            b += (f'<div class="abs seg-gold mono" style="left:{x:.1f}px;top:{yb}px;width:{CHECK * S - 4:.1f}px;height:50px;border-radius:10px 0 0 10px;'
                  f'display:flex;align-items:center;justify-content:center;font-size:20px">{m(CHECK)}</div>')
        else:
            rad = "0 10px 10px 0" if i == N_CHECK - 1 else "0"
            b += (f'<div class="abs" style="left:{x:.1f}px;top:{yb}px;width:{CHECK * S - (4 if i < N_CHECK - 1 else 0):.1f}px;height:50px;border-radius:{rad};'
                  f'border:1.5px dashed rgba(138,155,176,.5);display:flex;align-items:center;justify-content:center;'
                  f'font-size:16px;color:#8A9BB0">waits</div>')
    b += (f'<div class="abs" style="left:{X0}px;top:{yb + 62}px;font-size:17px;color:#A5B2C3;white-space:nowrap">'
          f'Work is {PCT}% done, but only {m(MS_RELEASED)} is released until the next checkpoint is verified.</div>')
    b += panel(752, 96, "Same job, two releases", f"{m(EARNED)} vs {m(MS_RELEASED)} at {PCT}% done. Both follow verified work, not the calendar.", 470, 26)
    foot = ("Sources: Yieldi, Draw Schedules Explained (updated May 21, 2026); Clion Capital, Construction Loan Draw Schedules<br>"
            "Explained (Jun 9, 2026); Yieldstack, Construction Draw Schedules in 2026 (Mar 22, 2026). Methods and treatment of<br>"
            "partial work vary by lender and loan. "
            f"Illustrative: {m(BUDGET)} budget, {PCT}% complete; {PCT}% &times; {m(BUDGET)} = {m(EARNED)};<br>"
            f"{m(BUDGET)} / {N_CHECK} = {m(CHECK)} per hypothetical checkpoint.")
    return shell("Percent complete or milestone?", "Same budget, different release.",
                 f"Illustrative {m(BUDGET)} rehab at {PCT}% complete", b, foot, 876)


PAGES = {"percent-vs-milestone-draws": ("images/2026-10-30/1247-fb-percent-vs-milestone-draws.png", gfx)}

if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
