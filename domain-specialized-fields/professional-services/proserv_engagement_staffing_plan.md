---
title: "Firm Capacity and Staffing Plan Across Engagements — Supply and Demand by Grade and Week, Hard and Soft Bookings, the Binding Grade, and Gap-Closing Moves"
category: specialized-fields/professional-services
description: "Build a rolling 8–13 week staffing plan for a multi-person consulting, accounting, engineering or agency firm: compute supply by grade and skill after leave at sustainable utilization, load signed work and probability-weighted pipeline under explicit hard-book and soft-book rules, find the grade that binds, close gaps in a fixed order (push work down, re-sequence, borrow, subcontract, hire, decline) with the margin cost of each, and check named assignments for over-allocation, key-person risk and client or independence restrictions — distinct from a solo practitioner's sellable-days and bench-date plan (services_capacity_and_utilization_planner)."
techniques:
  - NE-10
  - DP-09
  - NE-11
  - QA-08
difficulty: intermediate
tags:
  - resource-planning
  - staffing-plan
  - capacity-planning
  - pipeline-weighting
  - subcontracting
  - professional-services-firm
  - who-works-on-which-project
  - team-is-overbooked
  - hire-or-subcontract
updated: "2026-10-03"
reasoning:
  styles: [quantitative, structural, decisional]
  stakes: medium
  horizon: weeks
  uncertainty: risk
  evidence_quality: mixed
  domain_complexity: moderate
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [resource_manager, practice_leader, operations_director, engagement_manager]
  mode: [plan, decide]
related_prompts:
  - domain-business-strategy/client-services/services_capacity_and_utilization_planner.md
  - domain-specialized-fields/professional-services/proserv_utilization_realization_review.md
  - domain-specialized-fields/professional-services/proserv_independence_conflict_check.md
---

# Firm Capacity and Staffing Plan Across Engagements

**Objective:** Tell the firm, week by week for the next two to three months, whether
it has the people to deliver what it has sold and is likely to sell — by grade and
skill, not in aggregate — which grade is the constraint, and which moves close the
gap at the least cost to margin, quality and people.

**When to Use:**
- Weekly or fortnightly resourcing meeting in a firm of roughly 10–300 people.
- A large opportunity may close and partners need to know whether it can be staffed.
- Some people are on the bench while others are working 55-hour weeks.
- Deciding whether to hire, subcontract or push a start date.
- **Not this prompt if** you are **one person or a very small practice** working out
  how many days you can sell and when you run out of work — use
  `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md`.
  To review last quarter's utilization and realization, use
  `domain-specialized-fields/professional-services/proserv_utilization_realization_review.md`.
  General resource-constrained choices outside a services firm:
  `domain-decision-making/decisioning_resource_constrained_solver.md`.

## Inputs / Context

1. **People**: name or ID, grade, skills, office, standard hours, sustainable
   chargeable target by grade, leave and training dates.
2. **Signed engagements**: hours by grade and week (from each engagement plan),
   start and end dates, named team members already committed.
3. **Pipeline**: each opportunity's hours by grade, expected start, and a
   probability calibrated against the firm's past close rates at that stage.
4. **Restrictions**: client-imposed staffing limits, independence or conflict
   restrictions on individuals, required certifications.
5. **Flex options**: subcontractor rates and availability, other offices, hiring
   lead time, internal cost rates.

Tag pipeline probabilities `[calibrated]` (from history) or `[judgement]`. People
data stays inside the firm; the plan uses IDs where it will be circulated.

## Method

1. **Compute supply (NE-11).** `Supply = people × hours/week × chargeable target ×
   weeks − leave and training hours`, by grade and key skill. Use the sustainable
   target, not 100%.
2. **Set booking rules (QA-08).** **Hard-book** signed work and opportunities at
   ≥ 90% with a start date; **soft-book** 50–89% at probability-weighted hours;
   list but do not book < 50%. Rules are fixed before the numbers are run.
3. **Load demand (NE-10).** Signed + hard-booked + weighted soft-booked hours by
   grade and week; show the unweighted figure for each soft booking too, because a
   70% deal arrives at 100% or 0%.
4. **Find the binding grade (DP-09).** Balance = supply − demand per grade. The
   grade with the largest shortfall relative to its supply is the constraint; solve
   it first, since moves for other grades often shift work onto it.
5. **Close gaps in order, pricing each move.** (1) Push work down to a grade with
   spare capacity, adding review hours above; (2) re-sequence start dates with
   client agreement; (3) borrow from other offices or practices; (4) subcontract
   (margin cost = hours × (subcontract rate − internal cost)); (5) overtime within
   limits; (6) hire (lead time usually beyond the horizon — decide now for the next
   one); (7) decline or defer pipeline.
6. **Check named assignments.** No one above 100% of standard hours for more than
   two consecutive weeks; no single person as the only holder of a critical skill
   on an engagement without a pair; client and independence restrictions respected;
   development needs considered.
7. **Scenario for the big swing.** Show the plan if the largest soft-booked deal
   lands at 100% and if it is lost.

## Output Format

```
# Staffing plan — [firm/practice]   Weeks [..]–[..]   People: [n]
Booking rules: hard ≥ [..]% · soft [..]–[..]% weighted · list < [..]%

## 1. Supply by grade (after leave)
| Grade | People | Target h/wk | Weeks | Leave h | Supply h |
## 2. Demand
| Grade | Signed | Hard-booked | Soft-booked (weighted / unweighted) | Total |
## 3. Balance and binding grade
| Grade | Supply | Demand | Balance |
## 4. Gap-closing moves (in order)
| Move | Grade effect | Margin / quality cost | Owner |
Balance after moves: [..]
## 5. Named assignments and checks (over-allocation · key person · restrictions)
## 6. Scenarios (largest soft deal won / lost)
## 7. Decisions needed (hire, subcontract, decline)
```

## Verification

- [ ] Supply uses sustainable targets and subtracts leave.
- [ ] Booking rules are stated before demand is loaded.
- [ ] Soft bookings show weighted and unweighted hours.
- [ ] Balance is computed per grade, not only in total.
- [ ] Every gap-closing move states its effect on each grade and its cost.
- [ ] Named assignments pass the over-allocation, key-person and restriction checks.

## False-Positive Prevention

1. **Total hours balance, grades don't.** Spare analysts do not cover a senior
   shortfall without review time and risk.
2. **Weighted pipeline as real demand.** Probability weighting is right for the
   firm's average, wrong for any single deal; plan the swing.
3. **100% as capacity.** Planning to full standard hours leaves nothing for
   sales, training, or the overrun that will happen.
4. **Optimistic probabilities.** Deals at 70% that historically close at 40%
   overstate demand; calibrate against history.
5. **Hiring as this month's fix.** Recruiting and onboarding usually take longer
   than the planning horizon.
6. **Ignoring restrictions.** Staffing someone a client or independence rule bars
   creates a problem the plan will not show.

## Example Output

```
# Staffing plan — Data & analytics practice (18 people)   Weeks 41–48
Booking rules: hard ≥ 90% · soft 50–89% weighted · list < 50%

## 1. Supply (8 weeks)
| Principal | 2 | 20 | 8 | 0   | 320   |
| Manager   | 4 | 30 | 8 | 60  | 900   |
| Senior    | 6 | 34 | 8 | 136 | 1,496 |
| Analyst   | 6 | 34 | 8 | 0   | 1,632 |

## 2. Demand
Signed: P 210 · M 860 · S 1,640 · A 1,180
Hard: Opp Z renewal (90%, wk 41) M 60 · S 120 · A 80
Soft: Opp X (70% [calibrated], wk 43) M 160 / S 320 / A 240 → weighted 112 / 224 / 168
Listed: Opp Y (40%, wk 45) M 80 · S 160 · A 160
Total: P 210 · M 1,032 · S 1,984 · A 1,428

## 3. Balance
P +110 · M −132 · S −488 · A +204 → binding grade: Senior (−33% of supply).

## 4. Moves
| Push 200 h data prep and testing from S to A; +30 h M review | S −288 · A +4 · M −162 | Review load | EM |
| Move X start wk 43 → 45 (client flexible) | S −213 · M −125 · A +60 | Later revenue | Partner |
| Subcontract 200 S-hours, wks 43–48, $95 vs $70 internal | S −13 | −$5,000 margin | Ops |
| Principals take steering and QA, 100 h from managers | M −25 · P +10 | — | Principals |
After moves: P +10 · M −25 · S −13 · A +60 (within overtime tolerance; A spare → training).

## 5. Checks
Over-allocation: S-03 at 44 h/wk wks 41–43 on two engagements → 6 h/wk to subcontractor.
Key person: only S-05 knows the client's ERP data model on Brightwater → pair A-02.
Restriction: M-02 barred from Kestrel engagement (client contract: no staff from a
competitor within 12 months) → M-04 assigned.

## 6. Scenarios
(X in horizon after the move, weighted: S 149 · M 75 · A 112; unweighted: S 213 · M 107 · A 160.)
X lost: S −13 + 149 = +136, A +172, M +50 → cut subcontract to 64 h (2-week notice),
saving $3,400; spare analysts to training and Y pre-work.
X at 100%: S −13 − 64 = −77 → extend subcontract or push Y's start past wk 48.
Y (if it closes): cannot be staffed before wk 49 — agree the start date in the proposal.

## 7. Decisions
Open a senior requisition now (third consecutive plan with a senior shortfall; lead
time ~12 weeks). Approve the 200 h subcontract. Partner to confirm X start date.
```

## Techniques Used

- **NE-10 Probability-Weighted Scenarios** — weighted soft bookings plus the won/lost swing for the largest deal.
- **DP-09 Single Primary Constraint Identification** — the binding grade solved first.
- **NE-11 Embedded Calculation Formulas** — supply, demand, balance and the margin cost of subcontracting.
- **QA-08 Gate-Based Verification** — booking rules and assignment checks applied as pass/fail gates.

## Related Prompts

- `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` — the solo or small-practice version: sellable days and bench date.
- `domain-specialized-fields/professional-services/proserv_utilization_realization_review.md` — looking back at how the plan's hours turned into fees.
- `domain-specialized-fields/professional-services/proserv_independence_conflict_check.md` — the restrictions that decide who may staff which client.
