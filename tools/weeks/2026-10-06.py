#!/usr/bin/env python3
"""Graphics for the posts queued Oct 8-11, 2026 (built Oct 6, 2026).
Run from repo root:  python3 tools/weeks/2026-10-06.py [key ...]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gfx_lib import shell, panel, stat_card, step_cards, render, ARROW_R, CHK

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# ------------------------------------------------------------ FB Thu 5:27p: flip timeline (ATTOM Q2 2026)
def gfx_flip():
    X0, W = 88, 904
    K = W / 365
    x = lambda d: X0 + d * K
    TOP, H = 362, 56
    b = (f'<div class="abs" style="left:{X0}px;top:{TOP}px;width:{W}px;height:{H}px;border-radius:10px;'
         f'background:rgba(138,155,176,.14);border:1px solid rgba(138,155,176,.32)"></div>')
    b += (f'<div class="abs seg-gold mono" style="left:{X0}px;top:{TOP}px;width:{161 * K:.1f}px;height:{H}px;'
          f'border-radius:10px 0 0 10px;display:flex;align-items:center;justify-content:center;font-size:24px">161 days</div>')
    for d, label, mode in ((182, "6-month term ends", "c"), (365, "12-month term ends", "r")):
        xx = x(d)
        b += f'<div class="abs" style="left:{xx:.1f}px;top:{TOP - 18}px;height:{H + 20}px;border-left:2px dashed rgba(226,194,101,.85)"></div>'
        if mode == "c":
            b += f'<div class="abs" style="left:{xx - 130:.1f}px;top:{TOP - 48}px;width:260px;text-align:center;font-size:16px;font-weight:700;color:#E2C265">{label}</div>'
        else:
            b += f'<div class="abs" style="left:{xx - 260:.1f}px;top:{TOP - 48}px;width:260px;text-align:right;font-size:16px;font-weight:700;color:#E2C265">{label}</div>'
    ticks = ((0, "Purchase", "l"), (91, "3 mo", "c"), (182, "6 mo", "c"), (274, "9 mo", "c"), (365, "12 mo", "r"))
    for d, lab, al in ticks:
        xx = x(d)
        b += f'<div class="abs" style="left:{xx:.1f}px;top:{TOP + H}px;height:9px;border-left:1.5px solid rgba(138,155,176,.6)"></div>'
        if al == "l":
            b += f'<div class="abs" style="left:{xx:.1f}px;top:{TOP + H + 12}px;font-size:14.5px;color:#8A9BB0">{lab}</div>'
        elif al == "r":
            b += f'<div class="abs" style="left:{xx - 100:.1f}px;top:{TOP + H + 12}px;width:100px;text-align:right;font-size:14.5px;color:#8A9BB0">{lab}</div>'
        else:
            b += f'<div class="abs" style="left:{xx - 50:.1f}px;top:{TOP + H + 12}px;width:100px;text-align:center;font-size:14.5px;color:#8A9BB0">{lab}</div>'
    bx0, bx1 = x(161), x(182)
    by = TOP + H + 50
    b += (f'<svg class="abs" style="left:{bx0:.1f}px;top:{by}px" width="{bx1 - bx0 + 2:.1f}" height="14" viewBox="0 0 {bx1 - bx0 + 2:.1f} 14">'
          f'<path d="M1 0 V11 H{bx1 - bx0 + 1:.1f} V0" fill="none" stroke="#E2C265" stroke-width="2"/></svg>')
    mid = (bx0 + bx1) / 2
    b += f'<div class="abs gold" style="left:{mid - 200:.1f}px;top:{by + 20}px;width:400px;text-align:center;font-size:17px;font-weight:700">About 3 weeks of slack on a 6-month term</div>'
    b += stat_card(68, 556, 290, 152, "$2,000", "interest per month", "12% interest-only on $200,000")
    b += stat_card(395, 556, 290, 152, "~$10,600", "interest over 161 days", "$65.75 a day, actual/365")
    b += stat_card(722, 556, 290, 152, "+$2,000", "for each month of delay", "added interest if the flip runs late")
    b += panel(742, 92, "PRICE THE REAL TIMELINE", "Set the term and extension fee for how long projects actually take, not the best case.", 440)
    foot = ("Source: ATTOM, U.S. Home Flipping Report, Q2 2026 (Oct 1, 2026): the typical home flipped took 161 days from purchase to resale. "
            "ATTOM counts a flip as a resale within 12 months of the prior purchase. Interest example: $200,000 at 12% interest-only, actual/365. Illustrative only.")
    return shell("A typical flip takes", "161 days from purchase to resale.",
                 "ATTOM, Q2 2026 &middot; homes resold within 12 months of purchase", b, foot, 868)


# ------------------------------------------------------------ FB Fri 8:00a: DSCR in plain English
def gfx_dscr():
    b = panel(266, 92, "DSCR = INCOME &divide; PAYMENTS", "Monthly property income divided by the monthly debt payments on the loan.", 400, 27)
    b += '<div class="abs lbl" style="left:68px;top:392px">Example</div>'

    def box(x, w, big, small, cls):
        return (f'<div class="abs {cls}" style="left:{x}px;top:424px;width:{w}px;height:104px;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center">'
                f'<div class="mono" style="font-size:42px;line-height:48px">{big}</div><div style="font-size:16px;opacity:.85">{small}</div></div>')

    def op(x, ch):
        return f'<div class="abs mono gold" style="left:{x}px;top:424px;width:48px;height:104px;display:flex;align-items:center;justify-content:center;font-size:44px">{ch}</div>'
    b += box(68, 262, "$2,500", "monthly income", "seg-blue") + op(336, "&divide;")
    b += box(390, 262, "$2,000", "monthly payment", "seg-blue2") + op(658, "=")
    b += box(712, 300, "1.25", "DSCR", "seg-gold")
    X0, W = 88, 904
    K = W / 0.75
    x = lambda v: X0 + (v - 0.75) * K
    b += '<div class="abs lbl" style="left:88px;top:578px;height:26px;display:flex;align-items:center">Where lenders draw the line</div>'
    Y = 628
    b += (f'<div class="abs seg-steel" style="left:{x(0.75):.1f}px;top:{Y}px;width:{x(1.0) - x(0.75):.1f}px;height:58px;border-radius:10px 0 0 10px;display:flex;align-items:center;justify-content:center;font-size:16px">income falls short</div>')
    b += (f'<div class="abs seg-blue" style="left:{x(1.0):.1f}px;top:{Y}px;width:{x(1.5) - x(1.0):.1f}px;height:58px;border-radius:0 10px 10px 0;display:flex;align-items:center;justify-content:center;padding-right:{x(1.5) - x(1.25) + 6:.1f}px;font-size:17px">lenders generally require 1.0 to 1.5</div>')
    b += f'<div class="abs" style="left:{x(1.25) - 2:.1f}px;top:{Y - 14}px;height:86px;border-left:4px solid #E2C265"></div>'
    b += f'<div class="abs gold" style="left:{x(1.25) - 160:.1f}px;top:578px;height:26px;display:flex;align-items:center;justify-content:center;width:320px;font-size:17px;font-weight:700">1.25 &middot; most common minimum</div>'
    for v, lab, sub, al in ((0.75, "0.75", "", "l"), (1.0, "1.0", "just covers the payments", "c"), (1.25, "1.25", "", "c"), (1.5, "1.5", "high end of the range", "r")):
        xx = x(v)
        if al == "l":
            b += f'<div class="abs mono" style="left:{xx:.1f}px;top:{Y + 66}px;font-size:16px;color:#A5B2C3">{lab}</div>'
        elif al == "r":
            b += (f'<div class="abs mono" style="left:{xx - 200:.1f}px;top:{Y + 66}px;width:200px;text-align:right;font-size:16px;color:#A5B2C3">{lab}</div>'
                  + (f'<div class="abs" style="left:{xx - 260:.1f}px;top:{Y + 90}px;width:260px;text-align:right;font-size:14.5px;color:#8A9BB0">{sub}</div>' if sub else ''))
        else:
            b += (f'<div class="abs mono" style="left:{xx - 100:.1f}px;top:{Y + 66}px;width:200px;text-align:center;font-size:16px;color:#A5B2C3">{lab}</div>'
                  + (f'<div class="abs" style="left:{xx - 140:.1f}px;top:{Y + 90}px;width:280px;text-align:center;font-size:14.5px;color:#8A9BB0">{sub}</div>' if sub else ''))
    b += panel(792, 88, "ASK EACH LENDER", "Lenders define income and payments a little differently. Ask which costs they count.", 470)
    foot = ("Sources: SuperMoney, DSCR Loan (updated Apr 8, 2026): lenders generally require 1 to 1.5, most common minimum 1.25. "
            "DSCR Authority, How DSCR Is Calculated (May 21, 2026): residential lenders divide gross rent by PITIA, commercial lenders divide net operating income by debt service. "
            "Sources differ on typical minimums. Example is illustrative.")
    return shell("DSCR in plain English:", "income &divide; debt payments.",
                 "Debt service coverage ratio: how lenders test a rental property.", b, foot, 898)


# ------------------------------------------------------------ FB Fri 5:27p: interest-only vs amortizing
def gfx_io():
    def card(x, label, big, text):
        return (f'<div class="card" style="left:{x}px;top:268px;width:450px;height:158px">'
                f'<div class="abs lbl" style="left:22px;top:20px">{label}</div>'
                f'<div class="abs mono gold" style="left:22px;top:46px;font-size:54px;line-height:62px">{big}</div>'
                f'<div class="abs" style="left:22px;top:112px;width:410px;font-size:19px;line-height:25px;color:#A5B2C3">{text}</div></div>')
    b = card(68, "Interest-only", "$2,000", "a month. The balance stays at $200,000.")
    b += card(562, "30-year amortizing", "$2,057", "a month. Only $57 of it is principal in month one.")
    K = 0.25
    b += '<div class="abs lbl" style="left:68px;top:450px">Where the first payment goes</div>'
    for y, name in ((484, "Interest-only"), (542, "Amortizing")):
        b += f'<div class="abs" style="left:68px;top:{y}px;width:190px;height:44px;display:flex;align-items:center;font-size:19px;font-weight:700">{name}</div>'
        b += (f'<div class="abs seg-blue mono" style="left:268px;top:{y}px;width:{2000 * K:.1f}px;height:44px;border-radius:8px 0 0 8px;display:flex;align-items:center;justify-content:center;font-size:17px">$2,000 interest</div>')
    b += f'<div class="abs seg-gold" style="left:{268 + 2000 * K:.1f}px;top:542px;width:{57 * K:.1f}px;height:44px;border-radius:0 8px 8px 0"></div>'
    b += f'<div class="abs gold mono" style="left:{268 + 2057 * K + 16:.1f}px;top:542px;height:44px;display:flex;align-items:center;font-size:18px">$57 principal</div>'
    b += '<div class="abs lbl" style="left:68px;top:622px">Balance after 12 payments, amortizing</div>'
    W = 944
    sl = W * 0.00363
    b += (f'<div class="abs seg-blue2" style="left:68px;top:656px;width:{W - sl:.1f}px;height:56px;border-radius:10px 0 0 10px;display:flex;align-items:center;padding-left:22px;font-size:22px" >'
          f'<span class="mono">$199,274 still owed</span></div>')
    b += f'<div class="abs seg-gold" style="left:{68 + W - sl:.1f}px;top:656px;width:{sl:.1f}px;height:56px"></div>'
    b += (f'<svg class="abs" style="left:{68 + W - 26}px;top:718px" width="24" height="20" viewBox="0 0 24 20"><path d="M12 18 V3 M5 9 L12 2 L19 9" fill="none" stroke="#E2C265" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    b += f'<div class="abs gold mono" style="left:560px;top:742px;width:452px;text-align:right;font-size:19px">$726 paid down, 0.36%</div>'
    b += panel(790, 88, "$726 IN 12 MONTHS", "At 12%, amortizing barely lowers a short loan&rsquo;s balance. Interest-only keeps payment and payoff simple.", 480)
    foot = ("Illustrative: $200,000 at 12%, 30-year amortization ($2,057.23 a month) vs interest-only ($2,000.00). "
            "After 12 payments the amortizing balance is $199,274, a reduction of $725.76 or 0.36%. "
            "Interest-only payments with a balloon at maturity are common on hard money loans (Fit Small Business, updated May 2025; FlipperForce).")
    return shell("Why private loans are", "usually interest-only.",
                 "$200,000 &middot; 12% &middot; monthly payment and first-year balance", b, foot, 900)


# ------------------------------------------------------------ FB Sat 5:27p: lien waivers
def gfx_waivers():
    b = step_cards([
        ("1", "Draw request", "Contractor submits the request and signs a conditional waiver.", "conditional waiver"),
        ("2", "Payment clears", "The lender funds the draw. Wait for it to clear the bank.", "payment cleared"),
        ("3", "Final step", "Contractor signs an unconditional waiver for that payment.", "unconditional waiver"),
    ])

    def comp(x, label, head, sub):
        return (f'<div class="card" style="left:{x}px;top:520px;width:462px;height:170px">'
                f'<div class="abs lbl" style="left:22px;top:20px">{label}</div>'
                f'<div class="abs" style="left:22px;top:52px;width:418px;font-size:25px;line-height:31px;font-weight:700;color:#F0EDE4">{head}</div>'
                f'<div class="abs" style="left:22px;top:122px;width:418px;font-size:17px;line-height:23px;color:#A5B2C3">{sub}</div></div>')
    b += comp(68, "Conditional", "Takes effect only when the payment clears the bank.", "Safe to sign before the money arrives.")
    b += comp(550, "Unconditional", "Takes effect the moment it is signed.", "Sign only after the money has cleared.")
    b += panel(730, 92, "CONDITIONAL FIRST", "A conditional waiver with each draw request. An unconditional one once the funds clear.", 460)
    foot = ("Source: Corpay, Construction Lien Waivers: Conditional vs Unconditional Explained (updated June 2026). "
            "Waiver forms, timing and legal effect vary by state. General education, not legal advice.")
    return shell("Two kinds of lien waiver.", "One safe order of operations.",
                 "How a contractor&rsquo;s waiver fits around a draw payment.", b, foot, 862)


# ------------------------------------------------------------ FB Sun 10:15a: wire fraud (FBI IC3 2025)
def gfx_wire():
    def tile(x, big, cap):
        return (f'<div class="card" style="left:{x}px;top:268px;width:462px;height:176px">'
                f'<div class="abs mono gold" style="left:24px;top:26px;font-size:68px;line-height:76px;white-space:nowrap">{big}</div>'
                f'<div class="abs" style="left:24px;top:116px;width:414px;font-size:21px;line-height:26px;font-weight:700;color:#F0EDE4">{cap}</div></div>')
    b = tile(68, "12,368", "real estate fraud complaints in 2025")
    b += tile(550, "$275.1M", "in reported losses")
    b += '<div class="abs lbl" style="left:68px;top:484px">Before you wire</div>'
    b += step_cards([
        ("1", "Get the instructions", "Draw, payoff or closing wire details arrive by email or portal.", "wire instructions"),
        ("2", "Call to confirm", "Phone a number you already had. Never one from the email.", "known phone number"),
        ("3", "Wire went wrong?", "Call your bank right away and ask for a recall.", "ask for a recall"),
    ], top=512, h=206)
    b += panel(746, 92, "VERIFY BY PHONE", "Be suspicious of any new or last-minute change to wire instructions. Confirm before you send.", 460)
    foot = ("Source: FBI Internet Crime Complaint Center (IC3), 2025 Internet Crime Report, real estate fraud category: "
            "12,368 complaints and $275.1 million in reported losses. Steps follow guidance from the National Association of REALTORS "
            "(Protect Your Money From Mortgage Closing Scams, 2019) and ALTA HomeClosing101.")
    return shell("Real estate fraud in 2025:", "12,368 complaints, $275.1M lost.",
                 "FBI Internet Crime Report &middot; the wires lenders send every week.", b, foot, 880)


# ------------------------------------------------------------ FB Sun 5:27p: title date-down
def gfx_datedown():
    b = step_cards([
        ("1", "Order a date-down", "Before each draw, ask the title company to continue the search.", None),
        ("2", "Records are searched", "From the policy date to today, for new liens and defects.", None),
        ("3", "Resolve before funding", "A new mechanic&rsquo;s lien gets handled before the next advance.", None),
    ], top=270, h=196)
    b += '<div class="abs lbl" style="left:68px;top:508px">Each draw gets its own check</div>'
    AX = 604
    pts = ((150, "Policy date", "title insured as of this date", True), (400, "Draw 1", "records searched to here", False),
           (650, "Draw 2", "records searched to here", False), (900, "Draw 3", "records searched to here", False))
    b += f'<div class="abs" style="left:150px;top:{AX}px;width:750px;border-top:3px solid rgba(138,155,176,.55)"></div>'
    for xx, name, sub, first in pts:
        col = "#E2C265" if first else "#5B7DAE"
        b += f'<div class="abs" style="left:{xx - 11}px;top:{AX - 11}px;width:22px;height:22px;border-radius:50%;background:{col};border:3px solid #0B1F3A"></div>'
        if not first:
            b += f'<div class="abs" style="left:{xx - 13}px;top:{AX - 62}px">{CHK}</div>'
        b += f'<div class="abs" style="left:{xx - 120}px;top:{AX + 24}px;width:240px;text-align:center;font-size:19px;font-weight:700;color:#F0EDE4">{name}</div>'
        b += f'<div class="abs" style="left:{xx - 120}px;top:{AX + 52}px;width:240px;text-align:center;font-size:14.5px;color:#8A9BB0">{sub}</div>'
    b += panel(726, 104, "LIEN PRIORITY", "In some states, a contractor&rsquo;s lien can outrank money advanced after work began. Ask your title company how it works where you lend.", 560)
    foot = ("Source: Pillsbury Winthrop Shaw Pittman, Keeping Your Place in Line: Title Insurance Protections for Construction Loan Disbursements (2017). "
            "Endorsement names, availability and lien priority rules vary by state.")
    return shell("A title policy is a snapshot.", "A date-down updates it.",
                 "Rehab loans pay out over months, so lenders re-check title before each draw.", b, foot, 860)


# ------------------------------------------------------------ LI Thu 3:40p: borrower divide (Forecasa via AAPL)
def gfx_divide():
    b = ('<div class="card" style="left:68px;top:268px;width:944px;height:150px">'
         '<div class="abs mono gold" style="left:30px;top:36px;font-size:66px;line-height:78px;white-space:nowrap">Nearly 88%</div>'
         '<div class="abs" style="left:470px;top:34px;width:440px;font-size:24px;line-height:31px;font-weight:700;color:#F0EDE4">of private lending borrowers work with a single lender in a year.</div></div>')
    b += '<div class="abs lbl" style="left:68px;top:458px">Borrowers who close 4 or more loans a year</div>'
    X0, W = 290, 722
    for y, name, lo, hi in ((498, "Share of<br>borrowers", 9, 11), (592, "Share of<br>market volume", 29, 39)):
        b += f'<div class="abs" style="left:68px;top:{y}px;width:210px;height:64px;display:flex;align-items:center;font-size:20px;line-height:24px;font-weight:700">{name}</div>'
        b += f'<div class="abs" style="left:{X0}px;top:{y}px;width:{W}px;height:64px;border-radius:10px;background:rgba(138,155,176,.14);border:1px solid rgba(138,155,176,.30)"></div>'
        wlo, whi = W * lo / 100, W * hi / 100
        b += f'<div class="abs seg-gold" style="left:{X0}px;top:{y}px;width:{wlo:.1f}px;height:64px;border-radius:10px 0 0 10px"></div>'
        b += f'<div class="abs" style="left:{X0 + wlo:.1f}px;top:{y}px;width:{whi - wlo:.1f}px;height:64px;background:linear-gradient(180deg,rgba(226,194,100,.55),rgba(184,150,63,.55));border-radius:0 8px 8px 0"></div>'
        b += f'<div class="abs mono gold" style="left:{X0 + whi + 18:.1f}px;top:{y}px;height:64px;display:flex;align-items:center;font-size:34px;white-space:nowrap">{lo} to {hi}%</div>'
    for p in (0, 25, 50, 75, 100):
        xx = X0 + W * p / 100
        al = "left:%dpx" % (xx) if p == 0 else ("left:%dpx;transform:translateX(-100%%)" % xx if p == 100 else "left:%dpx;transform:translateX(-50%%)" % xx)
        b += f'<div class="abs" style="{al};top:670px;font-size:14px;color:#8A9BB0;white-space:nowrap">{p}%</div>'
    b += panel(722, 100, "TWO CUSTOMERS", "<div>Build lasting relationships with repeat borrowers. Serve <span style='white-space:nowrap'>one-time</span> users efficiently.</div>", 470)
    foot = ("Source: Forecasa (Fogliano and Morgan), The Borrower Divide Shaping Lending Today, published by the American Association of Private Lenders (AAPL), May 13, 2026. "
            "Light gold shows the range Forecasa reports for borrowers who close four or more loans a year.")
    return shell("Most borrowers use one lender.", "A small group does the volume.",
                 "Forecasa data, reported by the American Association of Private Lenders", b, foot, 862)


# ------------------------------------------------------------ LI Fri 2:00p: foreclosures H1 2026 (ATTOM)
def gfx_foreclosure():
    X0, S = 404, 12.5
    b = ""
    for p in (0, 10, 20, 30):
        xx = X0 + p * S
        b += f'<div class="abs" style="left:{xx - 30}px;top:268px;width:60px;text-align:center;font-size:14px;color:#8A9BB0">{p}%</div>'
        b += f'<div class="abs" style="left:{xx}px;top:296px;height:416px;border-left:1.5px dotted rgba(138,155,176,.38)"></div>'
    rows = [(318, "Properties with foreclosure filings", "227,548", 21, "seg-blue"),
            (448, "Foreclosure starts", "164,566", 18, "seg-blue2"),
            (578, "Completed foreclosures (REO)", "27,983", 33, "seg-gold")]
    for T, name, count, pct, cls in rows:
        b += (f'<div class="abs" style="left:68px;top:{T}px;width:322px;height:80px;display:flex;flex-direction:column;justify-content:center">'
              f'<div style="font-size:20px;font-weight:700;color:#F0EDE4;line-height:24px">{name}</div>'
              f'<div class="mono" style="font-size:17px;line-height:22px;color:#8A9BB0;margin-top:5px">{count} properties</div></div>')
        b += f'<div class="abs {cls}" style="left:{X0}px;top:{T + 6}px;width:{pct * S:.1f}px;height:68px;border-radius:0 8px 8px 0"></div>'
        b += f'<div class="abs mono gold" style="left:{X0 + pct * S + 22:.1f}px;top:{T + 6}px;height:68px;display:flex;align-items:center;font-size:42px;white-space:nowrap">+{pct}%</div>'
    b += panel(742, 92, "UP ACROSS THE BOARD", "More distress means more deal flow, and more borrowers under pressure.", 420)
    foot = ("Source: ATTOM, 2026 Mid-Year U.S. Foreclosure Market Report (July 16, 2026). "
            "Percent changes compare the first six months of 2026 with the first six months of 2025.")
    return shell("Foreclosure activity is climbing.", "First half of 2026 vs. a year ago.",
                 "U.S. properties, change from the first half of 2025", b, foot, 862)


PAGES = {
    "flip": ("images/2026-10-08/1727-fb-flip-timeline.png", gfx_flip),
    "divide": ("images/2026-10-08/1540-li-borrower-divide.png", gfx_divide),
    "dscr": ("images/2026-10-09/0800-fb-dscr.png", gfx_dscr),
    "fore": ("images/2026-10-09/1400-li-foreclosures.png", gfx_foreclosure),
    "io": ("images/2026-10-09/1727-fb-interest-only.png", gfx_io),
    "waivers": ("images/2026-10-10/1727-fb-lien-waivers.png", gfx_waivers),
    "wire": ("images/2026-10-11/1015-fb-wire-fraud.png", gfx_wire),
    "datedown": ("images/2026-10-11/1727-fb-title-date-down.png", gfx_datedown),
}

if __name__ == "__main__":
    keys = sys.argv[1:] or list(PAGES)
    render([PAGES[k] for k in keys], ROOT)
