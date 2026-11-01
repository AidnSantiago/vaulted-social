#!/usr/bin/env python3
"""Graphic for FOMC Oct 28 2026 hold and prime-linked loans. Run from repo root: python3 tools/weeks/2026-11-02-fomc-oct-2026.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LOAN, PRIME, MARGIN = 520000, 7.00, 1.50   # illustrative loan, interest-only


def gfx():
    rate = PRIME + MARGIN
    m0 = LOAN * rate / 100 / 12
    m1 = LOAN * (rate + 0.25) / 100 / 12
    assert f"{m0:,.2f}" == "3,683.33" and f"{m1:,.2f}" == "3,791.67" and f"{m1 - m0:,.2f}" == "108.33"
    b = '<div class="abs lbl" style="left:68px;top:268px">What the Fed did, and where prime stands</div>'
    b += stat_card(68, 300, 460, 150, "3-3/4 to 4%", "target range, held", "FOMC statement, October 28, 2026 (10 to 2 vote)", 44)
    b += stat_card(552, 300, 460, 150, "7.00%", "bank prime loan rate", "Fed H.15, October 29, 2026. Set by banks, not the Fed.", 44)
    b += '<div class="abs lbl" style="left:68px;top:480px">Illustrative prime-linked loan: $520,000 interest-only</div>'
    b += stat_card(68, 512, 460, 170, "$3,683.33", "a month at prime + 1.5", "7.00% + 1.50 = 8.50%. Prime unchanged after the meeting.", 44)
    b += stat_card(552, 512, 460, 170, "+$108.33", "per quarter point of change", "8.75% would be $3,791.67 a month", 44)
    b += panel(712, 92, "A HOLD = NO NEW MOVE",
               "Check the note for the index and adjustment date.", 400, 24)
    return shell("The Fed held at 3-3/4 to 4%.", "What that means for prime loans", "Rate decision of October 28, 2026, in plain numbers", b,
                 "Sources: Federal Reserve FOMC statement, Oct 28, 2026; Federal Reserve H.15 release, Oct 30, 2026 (prime 7.00 on Oct 29); Federal Reserve FAQ on the prime rate (updated 2013). "
                 "Arithmetic: $520,000 x 8.50% / 12 = $3,683.33; x 8.75% / 12 = $3,791.67; difference $108.33. Loan terms illustrative.", 842)

PAGES = {"fomc-oct-2026": ("images/2026-11-02/0842-fb-fomc-oct-2026.png", gfx)}
if __name__ == "__main__":
    render([PAGES[k] for k in (sys.argv[1:] or list(PAGES))], ROOT)
