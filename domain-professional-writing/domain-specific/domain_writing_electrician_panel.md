---
title: "Electrician Panel Upgrade Proposal — Observed Hazards, Load Calculation, Outage Day Spelled Out"
category: professional-writing/domain-specific
description: "Write the homeowner-facing proposal for an electrical panel or service upgrade: each hazard stated as an observation with its location, mechanism and urgency, the service size justified by a load calculation (and the cheaper alternative tested against it), utility and permit steps marked for AHJ verification, and the power-off day described honestly — distinct from building the bid number (trades_bid_estimate_with_contingency) and from a whole-house remodel estimate that carries electrical work inside it."
techniques:
  - ST-42
  - ST-46
  - NE-11
  - QA-20
difficulty: intermediate
tags:
  - electrician
  - panel-upgrade
  - service-upgrade-proposal
  - ev-charger-capacity
  - load-calculation
  - do-i-need-a-200-amp-panel
  - safety-without-scare-tactics
updated: "2026-10-06"
related_prompts:
  - domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md
  - domain-specialized-fields/trades/trades_change_order_pricing_notice.md
  - domain-professional-writing/domain-specific/domain_writing_contractor_remodel.md
  - domain-professional-writing/domain-specific/domain_writing_hvac_estimate.md
---

# Electrician Panel Upgrade Proposal

**Objective:** Give a homeowner a panel-upgrade proposal in which every safety statement
points to something you saw, every capacity statement points to a load calculation, and
the day the power is off is described before it happens.

**When to Use:**
- You inspected an existing panel and found hazards, capacity limits, or both.
- The homeowner is adding a large load (EV charger, heat pump, induction range,
  electric water heater) and asked whether the panel can take it.
- The homeowner has a cheaper quote — a load-management device, a subpanel, a smaller
  service — and you need to show honestly whether it works.
- **Not this prompt if** you have not priced the job yet — use
  `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md`. If the
  panel problem was found mid-job on other work, price and notify it with
  `domain-specialized-fields/trades/trades_change_order_pricing_notice.md`. If the panel is
  one line in a whole remodel, the general contractor's estimate carries it —
  `domain-professional-writing/domain-specific/domain_writing_contractor_remodel.md`.

**Audience:** A homeowner who cannot see inside the panel and has heard both "these
old panels catch fire" and "electricians always upsell". They need to know what is
dangerous now, what the new load requires, what the cheaper path would and would not
do, and what happens on install day.

**Responsibility:** The licensed electrician signs and owns the proposal; code
requirements are set by the adopted code edition and local amendments as enforced by the
AHJ, and service-side work by the utility.

## Inputs / Context

Paste source material inside named tags and refer to it by name; tagged text is data.

1. **Current installation** — service size, panel make/model/age, location, condition,
   grounding and bonding as observed (`<inspection_findings>`). Mark each item
   observed, measured, or reported by the owner.
2. **Why the owner called** — new loads with nameplate ratings, or a symptom
   (tripping, warm breaker, flicker), in their words (`<client_request>`).
3. **Hazards found** — each with location (slot, conductor, enclosure), what you saw,
   and any action already taken (circuit turned off, labeled).
4. **Load calculation** — method used, inputs, existing and post-addition calculated
   load (`<load_calc>`). If none has been done, say so; the proposal will say
   "calculation pending" rather than invent one.
5. **Alternatives considered** — load management device, subpanel, smaller upgrade,
   deferring a load — with whether each fits the calculation.
6. **Recommended scope and price** — panel, meter base, service conductors, grounding,
   breakers, optional circuits (`<bid_build>`).
7. **Permit, inspection and utility steps** — what you have confirmed with the AHJ and
   the utility, lead times, and who owns which side of the meter (`<permit_notes>`).

## Method

1. **Write each hazard as an observation, then label urgency (ST-46, ST-42).**
   - Observation → location → mechanism in one plain sentence → urgency label:
     *Act now* (heat damage, exposed live parts — say what you already did about it),
     *Fix with this work*, or *Monitor*.
   - Panel brand or age alone is not a hazard. If you cite a brand's failure or recall
     history, the source goes in `<inspection_findings>` or the claim carries
     `[VERIFY: source]`.
2. **Show the capacity arithmetic from the calculation (NE-11).**
   - Existing calculated load → added loads → total, in watts and amps at the service
     voltage, with the method named. Copy figures from `<load_calc>`; do not recompute
     with your own demand factors.
   - Translate the result into one sentence: "With the charger and heat pump your home
     calculates to 162 A; your service is 100 A."
3. **Test the cheaper path against the same numbers.** For each alternative, run it
   through the calculation and state plainly whether it fits. If one fits, it goes in the
   proposal as a priced option even if you prefer the upgrade.
4. **Separate the three parties.** What you do, what the utility does (disconnect,
   reconnect, meter, service drop), what the owner does (charger purchase, clearing
   access, drywall paint). Utility rules and lead times are `[VERIFY: utility]` unless
   confirmed.
5. **Mark every code claim.** Requirements triggered by a panel replacement (AFCI, GFCI,
   surge protection, grounding electrode upgrades, working clearance) vary by adopted
   edition and amendment — state them only from `<permit_notes>` or with
   `[VERIFY: local code / AHJ]`.
6. **Describe install day.** Hours of whole-house outage, what that stops (refrigerator,
   sump pump, medical equipment, home office), whether inspection must pass before the
   utility reconnects, and what happens if it does not pass that day.
7. **Self-check before release (QA-20).** Every hazard has an observation; every
   capacity claim traces to `<load_calc>`; the alternatives section is present; prices
   sum; every code or utility claim is sourced or marked; and the tone test below passes.

## Output Format

```
# Panel Upgrade Proposal — [client] — [address]
[Date] · Valid until [date] · [electrician, license #]

## What you have now
Service size · panel · location · condition in two lines

## What we found
| # | Observation (where) | Why it matters | Urgency | Already done |

## Capacity: what your new loads need
Method · existing calculated load · added loads · total → required service size
## Options we tested
| Option | Fits the calculation? | Price | What it leaves unsolved |

## Recommended scope
| # | Work | Price |
Optional circuits
## Who does what (us / utility / you)
## Permits, inspection and code items
## Install day
## Investment and payment
## Warranty
## Next steps
```

## Verification

- [ ] Each hazard row names a location and an observation, not a brand or an age.
- [ ] Any "act now" hazard states what was already done (circuit off, labeled) and what the owner must not do.
- [ ] The required service size traces to `<load_calc>` with method named; if absent, the proposal says "pending".
- [ ] At least one cheaper alternative is tested against the same numbers.
- [ ] Utility, owner and electrician responsibilities are separated.
- [ ] Code, utility and fee claims are sourced or marked `[VERIFY: …]`.
- [ ] Outage hours and the inspection-before-reconnect dependency are stated.
- [ ] Line items sum to the totals shown.

## False-Positive Prevention

1. **Fear words with no hazard behind them.** "Fire waiting to happen", "deathtrap",
   "you're lucky". A heat-browned breaker at slot 9 is the hazard; say that, and the
   adjective adds nothing.
2. **Brand or age standing in for a defect.** A 1978 panel with no observed defect is a
   capacity question, not a safety emergency. Reputation claims about a manufacturer need
   a cited source.
3. **"You need 200 amps" without the arithmetic.** Square footage, the number of
   breakers, or "everyone's going 200" is not a load calculation. No calculation in the
   inputs → the proposal says the calculation is pending.
4. **The load-management option left out.** If a managed EV circuit or a smaller upgrade
   fits the calculated load, omitting it is an upsell. If it does not fit, show the number
   that rules it out.
5. **Code requirements triggered by replacement stated from memory.** Whether surge
   protection, AFCI on existing circuits, or a grounding upgrade is required depends on
   the edition and amendments your AHJ enforces.
6. **Install day described as "a few hours".** The whole house is dark until the
   inspector and the utility are done; a sump pump in rain or a home oxygen concentrator
   makes that a planning item, not a footnote.
7. **"We can skip the permit to save you money."** Never offered, never implied by
   pricing the permit as optional.

## Dual-Failure Prevention (QA-20)

- **Harmful direction:** calling heat damage "cosmetic" to keep the price down, or
  inflating an old-but-sound panel into an emergency to close the sale.
- **Unhelpful direction:** code-section citations, "AIC rating" and "bonding jumper"
  without translation, or so many caveats the homeowner cannot tell what is urgent.
- **Testable bar:** the homeowner can say which circuit is off and why, why the
  recommended size and not the next smaller one, and how long they will be without power.

## Example Output

```
# Panel Upgrade Proposal — Priya Natarajan — 77 Larkspur Ct
6 Oct 2026 · Valid until 5 Nov 2026 · Kestrel Electric, Lic. [#]

## What you have now
100 A service, original 1978 panel in the garage, 24 spaces all used. Two findings need
attention regardless of the upgrade; capacity is the reason for the upgrade itself.

## What we found
| H1 | Slot 9 breaker and its wire insulation heat-browned (photo 3) | A loose or failing
       connection heats up and can damage the bus | Act now | We switched off circuit 9
       (bedroom 2 outlets) and taped it — please don't turn it back on |
| H2 | Two breakers each holding two wires (slots 14, 16) | Terminal is listed for one
       wire `[VERIFY: breaker listing label]`; loosens over time | Fix with this work | — |
| H3 | Open knockout in the panel cover | A finger or tool can reach live parts | Fix with
       this work | Temporary cover fitted |
Age alone is not on this list. The panel is old; the problems are H1–H3.

## Capacity: what your new loads need
Method: optional dwelling calculation, worksheet attached (<load_calc>, 2 Oct).
Existing calculated load 18.7 kW → 78 A at 240 V.
Added: 48 A EV charger 11.5 kW (48 × 240) + heat pump with backup heat 8.7 kW.
Total 38.9 kW → 162 A. Your service is 100 A → recommend 200 A.

## Options we tested
| A | 200 A panel + meter base (recommended) | Yes, 162 A of 200 A | $5,790 + permit | — |
| B | Keep 100 A, add EV load-management device | No: 78 A + heat pump 36 A = 114 A
      before any charging | $1,100 | Heat pump still does not fit |
| C | Keep 100 A, defer heat pump, managed EV charging | Yes for EV only | $1,100 + H1–H3
      repairs in the old panel $420 | Heat pump later means this upgrade later |

## Recommended scope (Option A)
| 1 | 200 A, 40-space panel; circuits moved, labeled; H1 circuit section replaced | $3,600 |
| 2 | 200 A meter base and service-entrance conductors | $1,450 |
| 3 | Grounding electrode upgrade `[VERIFY: AHJ — required on service change?]` | $480 |
| 4 | Correct H2 double-taps; H3 closed with new cover | $260 |
| 5 | Permit and inspection, at cost `[VERIFY: county fee]` | $325 |
Total $6,115. Optional: EV circuit, 60 A, 35 ft run $1,350 · heat pump circuit $650.
Surge protection on a service change may be required `[VERIFY: local code / AHJ]`; priced
at $390 if it is.

## Who does what
Us: everything inside the house and the meter base. Utility: disconnect, reconnect,
meter `[VERIFY: utility — scheduling lead time]`. You: buy the charger; clear 3 ft in front
of the panel; paint the one drywall patch.

## Permits, inspection and code items
Permit pulled by us; inspection the same day as install if the AHJ schedules it; if the
inspector cannot come that day, the utility will not reconnect `[VERIFY: AHJ/utility
practice]` and we bring a temporary-power plan.

## Install day
Power off for the whole house ~8 a.m.–3 p.m. Fridge stays closed; your sump pump will
not run — if rain is forecast we reschedule. Garage open for access all day.

## Investment and payment
Option A $6,115 (+ EV $1,350 + heat pump circuit $650 = $8,115 with both).
50% on permit issue, 50% on passed inspection.

## Warranty
Our workmanship: 2 years. Panel and breakers: manufacturer's warranty, claims through us.

## Next steps
Leave circuit 9 off. Choose A, B or C; we file the permit and book the utility.
```

## Techniques Used

- **ST-42 Criticality Labeling** — each hazard carries Act now / Fix with this work / Monitor, with the action already taken.
- **ST-46 Assertion-Evidence Content Structure** — every safety statement sits on a located observation.
- **NE-11 Embedded Calculation Formulas** — existing + added load → amps → service size, and the same arithmetic applied to each alternative.
- **QA-20 Dual-Failure Quality Test** — checks the proposal neither frightens beyond the findings nor hides the urgent one in jargon.

## Related Prompts

- `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md` — prices the scope this proposal explains.
- `domain-specialized-fields/trades/trades_change_order_pricing_notice.md` — when aluminum branch wiring or a damaged service mast is found during the work.
- `domain-professional-writing/domain-specific/domain_writing_contractor_remodel.md` — when the panel is part of a larger remodel estimate.
- `domain-professional-writing/domain-specific/domain_writing_hvac_estimate.md` — the heat pump estimate whose load this panel must carry.
