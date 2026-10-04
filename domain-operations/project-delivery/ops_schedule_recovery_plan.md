---
title: "Schedule Recovery Plan — Re-Forecast the Slip, Then Buy Back Days Cheapest-First on the Critical Path"
category: operations/project-delivery
description: "Recover a fixed-date non-software project that is running late: re-forecast the finish from remaining work at the observed rate rather than from percent spent, find the current critical path, price every recovery option (fast-track, crash, defer scope, remove waits, move the date) in cost per day saved, apply them cheapest-first while recomputing the path after each, and take a dated sponsor decision with a trigger for moving the date."
techniques:
  - NE-11
  - RT-07
  - DS-06
  - QA-02
  - NE-10
difficulty: advanced
tags:
  - schedule-recovery
  - critical-path
  - crashing
  - fast-tracking
  - re-baseline
  - cost-of-delay
  - project-running-late
  - behind-schedule
  - will-we-make-the-date
updated: "2026-10-03"
related_prompts:
  - domain-operations/project-delivery/ops_non_software_project_plan.md
  - domain-specialized-fields/professional-services/proserv_fixed_fee_overrun_diagnosis.md
  - domain-risk/risk_register_builder.md
---

# Schedule Recovery Plan

**Objective:** Turn "we're behind" into a priced decision: an honest forecast of the
finish date, the days that must be bought back, the cheapest credible way to buy them
on the path that actually sets the date, and the point at which moving the date becomes
cheaper than recovering it.

**When to Use:**
- A fixed-date physical or organizational project (store opening, facility move,
  equipment install, event, multi-site rollout) has slipped and the date still matters.
- A vendor or crew is running slower than planned and everyone is still reporting
  "on track overall".
- A sponsor has asked "what will it cost to hold the date?" and needs options, not hope.
- **Not this prompt if** you are building the plan from scratch — use
  `domain-operations/project-delivery/ops_non_software_project_plan.md` (this prompt
  consumes its network). If the overrun is **budget** on a fixed-fee client engagement,
  use `domain-specialized-fields/professional-services/proserv_fixed_fee_overrun_diagnosis.md`.
  If the project is software in sprints, scope negotiation lives in
  `domain-product-management/prompts/product_delivery_sprint_planner.md`. For the
  after-the-fact review, use `ops_project_closeout_and_lessons_learned.md`.

## Inputs / Context

1. **The baseline network**: activities, durations, predecessors, the fixed date, and
   the original buffer.
2. **Status at a stated date**: per activity, done / in progress / not started, with
   evidence of completion (inspected, signed off, delivered) — not hours spent.
3. **Observed rates**: planned vs. actual output for in-progress work (rooms finished
   per week, units installed per day), tagged `measured` or `estimated`.
4. **Recovery levers available**: extra crews, extended shifts, expedite fees, vendor
   alternatives, scope items that could move after the date, approvals that could be
   pulled forward.
5. **Cost of delay**: what a later date costs (lost revenue, rent, penalties, rebooking,
   reprinting), each line tagged `measured` or `estimated`.
6. **Hard holds**: inspections, permits, cure or drying times, safety sign-offs,
   blackout dates — durations that money cannot shorten.

## Method

1. **Re-forecast from remaining work (NE-11).** For each in-progress activity:
   `remaining duration = remaining planned work ÷ observed rate`. Where the rate is a
   *rate* problem (crew consistently at 60% of plan), apply it to that crew's later
   activities too; where it was a one-off event (a delivery lost for a week), do not.
   Run the forward pass from the status date. Gap = forecast finish − fixed date.
   Label the forecast *modeled*.
2. **Find today's critical path (RT-07).** Recompute float from the forecast, not the
   baseline. The path that slipped is often no longer the only critical path; list
   every path with float ≤ the gap as near-critical.
3. **Price every option in cost per day saved.** For each lever on a critical activity:
   days saved, direct cost, `cost/day = added cost ÷ days saved`, and the risk it adds.
   - *Fast-track*: overlap sequential work (zone handovers). Cheap; adds rework and
     crowding risk. Cap overlap at what the work allows (e.g. ≤ 40% of the predecessor).
   - *Crash*: add a crew, a second shift, or a faster vendor. Prefer added crews to
     sustained overtime — long weeks lose productivity after a few weeks.
   - *Defer scope*: move non-essential items after the date. Free in cash, not in
     commitments — sponsor decision.
   - *Remove waits*: pre-book inspections, pull approvals forward, pay to expedite.
   - *Move the date*: cost of delay. This is the ceiling for every other option.
4. **Apply cheapest-first, recompute after each (DS-06).** Take the lowest cost/day
   option on the critical path, rerun the forward pass, and check whether another path
   has become critical. Stop when the forecast clears the date with the target buffer
   (state it: e.g. ≥ 2 working days, or ≥ 10% of remaining duration).
5. **Stress-test the recovered plan (QA-02, NE-10).** What if the slow crew stays slow
   after crashing? What if the fast-track overlap causes rework? Give a base and a
   downside forecast; if the downside misses the date, say so.
6. **Protect the holds.** No option may shorten an inspection, cure time, permit, or
   safety sign-off. Recovery that relies on skipping one is rejected and flagged for the
   qualified person or authority.
7. **Decide and re-baseline.** Present 2–3 packages (days recovered, cost, residual
   buffer, risk) against the cost of delay; name the decider and the decision date. Set
   a **date-move trigger**: the checkpoint and forecast value at which moving the date
   is chosen deliberately, early enough to save the commitments that a late move breaks.

## Output Format

```
# Schedule recovery — [project]   Status date: [..]   Fixed date: [..]

## Re-forecast (modeled)
| Activity | Status (evidence) | Planned rate | Observed rate | Remaining | Rate or one-off? |
Forecast finish: [..]   Gap to fixed date: [..] days   Original buffer: [..]

## Critical and near-critical paths (from forecast)
[path] — float [..]

## Recovery options
| Option | Activity | Days saved | Added cost | Cost/day | Risk added | Decider |

## Cheapest-first application
| Step | Option applied | New forecast finish | Critical path now | Gap |

## Packages for decision
| Package | Days recovered | Cost | Residual buffer | Downside forecast | Risk |
Cost of delay if the date moves: [..] (lines tagged measured/estimated)

## Holds that cannot be compressed
## Decision: [package] — decider [..] by [date]
## Date-move trigger: if forecast > [..] at [checkpoint], move the date by [..]
```

## Verification

- [ ] Remaining durations come from remaining work ÷ observed rate, not percent spent.
- [ ] Rate problems are propagated to the same crew's later work; one-offs are not.
- [ ] Critical path is recomputed from the forecast, and recomputed after every option.
- [ ] Every option has days saved, cost, and cost/day; costs are tagged.
- [ ] No option compresses an inspection, permit, cure time, or safety sign-off.
- [ ] A downside forecast is reported alongside the base.
- [ ] A named decider, a decision date, and a date-move trigger are stated.

## False-Positive Prevention

1. **Percent spent as percent done.** "70% of the budget used" says nothing about the
   finish. Count evidenced completion and forecast from rate.
2. **Crashing a non-critical activity.** Money spent off the critical path buys no
   days. Check float before paying.
3. **Recovering one path while another becomes critical.** After a big crash, a
   parallel path (inspection booking, signage) often sets the date. Recompute.
4. **Overtime as free capacity.** Sustained long weeks lower output and raise error and
   injury rates; a second crew usually buys days more reliably.
5. **Fast-track without the rework cost.** Overlapping trades in one space causes
   damage and re-dos; cap the overlap and price a supervisor.
6. **Scope deferral nobody approved.** Deferring the back room is a commitment change;
   the sponsor decides it, in writing.
7. **"We'll make it up later."** Later activities were estimated at the planned rate;
   if the rate problem is real, they will slip too.
8. **Moving the date too late.** The cheapest date move is the early one; a trigger
   fixed in advance prevents the drift to the last week.

## Example Output

```
# Schedule recovery — Store opening, Riverside   Status: working day 30   Opening: day 50

## Re-forecast (modeled)
| Fit-out (A)       | in progress, 6 of 13 zones signed off | 1.0 zone/d | 0.6 zone/d (measured, 10 d) | 7 planned-d ÷ 0.6 = 12 d | rate |
| Fixtures (B)      | not started; vendor mobilises after A | — | — | 8 d (vendor quote) | — |
| Stock & merch (C) | not started | — | — | 6 d | — |
| Walk-through (W)  | not started | — | — | 1 d | — |
| Inspection (D)    | not started; after B | — | — | 2 d (+ 3 d booking lead) | hold |
Forward pass: A 30–42 → B 42–50 → C 50–56 → W 56–57
Forecast open-ready: day 57   Gap: 7 days late   Original buffer: 2 days

## Critical path: A → B → C → W (float −7). Near-critical: A → B → D (float −2).

## Recovery options
| Defer back-room shelving | B | 1 | $0      | $0     | stockroom unfinished 2 wks | Sponsor |
| Fast-track C on B (3 d)  | C | 3 | $1,500  | $500   | crowding; supervisor priced | PM |
| Night shift fixtures     | B | 2 | $4,000  | $2,000 | fatigue; vendor confirmed | PM |
| Second fit-out crew      | A | 4 | $9,600  | $2,400 | site access; induction 1 d incl. | PM |
| Move opening 2 weeks     | — | — | $38,000 | ceiling | lost sales $28k (est), reprint $6k, rent $4k | Sponsor |

## Cheapest-first application
| 1 | Defer back room (B 8→7)      | day 56 | A-B-C-W | 6 |
| 2 | Fast-track C (start B−3)     | day 53 | A-B-C-W | 3 |
| 3 | Night shift (B 7→5; overlap capped at 2 d) | day 52 | A-B-C-W | 2 |
| 4 | Second crew (A 12→8)         | day 48 | A-B-C-W; D path float 3 | buffer +2 |

## Packages for decision
| P1: steps 1–2 only     | 4 | $1,500  | −3 (late) | day 55 | low cost, misses the date |
| P2: steps 1–4          | 9 | $15,100 | +2 days   | day 50 if the second crew ramps slowly (A = 10 d) | medium |
| P3: move date 2 weeks  | — | $38,000 | +7        | —      | low; marketing reprint |
Recommendation: P2 — $15,100 against a $38,000 cost of delay. Downside lands exactly on
day 50 with zero buffer, so the trigger below matters.

## Holds that cannot be compressed
Occupancy inspection (book now for day 43–45); fire-alarm commissioning; no stock on
the floor before inspection passes.

## Decision: P2 — Regional director, by day 31
## Date-move trigger: if forecast open-ready > day 49 at the day-38 checkpoint, move
opening to day 60 on day 40, before print and radio buys commit.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — remaining duration from rate, cost per day saved, gap arithmetic.
- **RT-07 Cascade Effect Analysis** — forward pass after each option shows when another path becomes critical.
- **DS-06 Prioritization and Severity Guidance** — cheapest-per-day first, critical path only.
- **QA-02 Adversarial Stress-Test** — "the slow crew stays slow" downside on the recovered plan.
- **NE-10 Probability-Weighted Scenarios** — base and downside forecasts against the cost of delay.

## Related Prompts

- `domain-operations/project-delivery/ops_non_software_project_plan.md` — the baseline network this re-forecasts.
- `domain-specialized-fields/professional-services/proserv_fixed_fee_overrun_diagnosis.md` — budget overrun on a fixed-fee engagement.
- `domain-risk/risk_register_builder.md` — logging the residual schedule risks the recovery leaves.
