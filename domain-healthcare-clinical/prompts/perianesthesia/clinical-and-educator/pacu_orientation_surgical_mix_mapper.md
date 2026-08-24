---
title: PACU Orientation Surgical Mix Mapper
category: pacu/orientation-curriculum
task_type: ANALYZE
audience: PACU charge nurse, educator, or preceptor planning orientee assignments for exposure breadth
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - assignments
  - surgical-mix
  - exposure
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - ED-02
difficulty: intermediate
related_prompts:
  - prompts/pacu_orientation_curriculum_designer.md
  - prompts/pacu_orientee_weekly_learning_plan.md
  - prompts/pacu_orientation_topic_sequencing_optimizer.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
---

# PACU Orientation Surgical Mix Mapper

> Safety reminder: Mapping is a planning aid, not an assignment directive. Charge nurse retains authority over actual assignments per patient acuity and unit flow.

## Objective

Map an orientee's expected shift schedule against the facility's surgical mix and the curriculum's required exposure breadth, surfacing **services likely to be under-represented** in natural scheduling and recommending **engineered exposures** to close gaps.

## Inputs

- **Orientation length and current week:** {{e.g., 10 weeks; currently end of Week 4}}
- **Orientee shift pattern:** {{e.g., 3 × 12s Mon-Wed; 4 × 10s rotating; etc.}}
- **Facility surgical mix:** {{best-known % by service or top services per OR day}}
- **OR day patterns:** {{e.g., Mon = ortho-heavy, Tue = mixed general, Wed = GYN/urology, Thu = ENT, Fri = ambulatory}}
- **Required exposure list from curriculum:** {{services / case types the pathway expects}}
- **Exposures already received:** {{best-known shift log of services seen}}
- **Constraints:** {{e.g., orientee unavailable certain days, certain services not available in current schedule window}}

## Audience / Scope

- **Primary:** Charge nurse + educator + primary preceptor coordinating assignments.
- **Secondary:** Orientee gets a simplified "what to expect" view.
- **Scope:** Engineering exposure breadth across the orientation. Does not assign specific patients.

## Output requirements

```markdown
# Surgical Mix Mapping — Week {current} of {N}

> Safety reminder: Planning aid. Charge nurse retains final say on assignments.

## Current exposure inventory

| Service / case type | Required by curriculum | Exposures received | Status |
|---|---|---|---|
| Ortho (TKA/THA) | yes — high frequency | {n} cases | On track / under / over |
| General (open + lap) | yes | {n} | … |
| GYN | yes | {n} | … |
| Urology | yes — low priority | {n} | … |
| ENT | yes | {n} | … |
| Bariatric | yes if facility offers | {n} or n/a | … |
| Vascular | yes if facility offers | {n} or n/a | … |
| Spinal anesthesia recoveries (cross-service) | yes | {n} | … |
| MAC/sedation recoveries | yes | {n} | … |
| (Add facility-specific services from the input) | … | … | … |

## Gaps surfaced

For each under-represented service:
- **Service:** {name}
- **Curriculum need:** {why this service must be exposed}
- **Natural availability in remaining weeks:** {high / moderate / low}
- **Engineered exposure options:**
  - {option 1 — e.g., reassign orientee from Mon ortho to Tue general for one week}
  - {option 2}
- **Trade-off:** {what gets de-prioritized to make room}

## Over-represented services

Services where exposure is already saturated. Note for context — do not eliminate, but no need to engineer further.

## Recommended assignment adjustments (next 2 weeks)

| Day | Default assignment | Recommended adjustment | Rationale |
|---|---|---|---|
| Wk {n+1} Mon | ortho | hold default | already on curve |
| Wk {n+1} Tue | general (mixed) | seek GYN open if available | close GYN gap |
| Wk {n+1} Wed | GYN | hold default | … |
| Wk {n+2} Mon | ortho | offer to swap to urology day | close urology gap |

## Charge-nurse handoff note

Two-line note the educator can hand to the charge nurse:
"This orientee needs more {service A, service B} exposure in the next 2 weeks. If patient assignments allow, lean toward those service patients on {days}. Defer to acuity."

## What this mapper is not

- Not an assignment system (charge nurse owns).
- Not a guarantee of exposure (case mix on the day decides).
- Not an HR document.

## Sources / reference

- ASPAN *Standards* — scope of expected exposure.
- *Drain's* — service-specific recovery considerations.
```

## Must / Must not

**Must:**
- Honor charge nurse authority — recommendations only, never directives.
- Account for patient acuity over orientee exposure (note explicitly).
- Surface trade-offs (gaining exposure A often defers exposure B).
- Treat exposure inventory as approximate if the input shift log is approximate.

**Must not:**
- Recommend assigning a patient to an orientee whose acuity exceeds scope.
- Invent facility surgical-mix percentages beyond declared.
- Invent OR schedules beyond declared.
- Recommend overriding charge-nurse acuity judgment.
- Reference protected characteristics.

## Quality signals

- A charge nurse can read the handoff note and apply it on the next shift.
- Gaps are tied to curriculum need, not "feels like more would be good."
- Trade-offs are visible, not buried.
- The mapper can be re-run weekly without rewriting the whole pathway.

## Verification

- [ ] Inventory table covers required services.
- [ ] Each gap has at least one engineered option with trade-off.
- [ ] Charge-nurse handoff note ≤ 2 lines.
- [ ] Acuity-over-exposure principle stated.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented surgical-mix percentages** beyond user-declared.
- **No invented OR-day schedules.**
- **No invented patient acuity claims** to justify or deny assignments.
- **No invented facility staffing rules.**
- **No invented case-volume targets** ("must have 10 spinal recoveries to advance").
- **No protected-characteristic-based assignment recommendations.**
- **No license-pathway-based assignment recommendations.**

## Worked Example

<details>
<summary>Example: Wk 4 of 10, 3 × 12s Mon-Wed, ortho-heavy unit, urology under-exposed (click to expand)</summary>

```markdown
## Current exposure inventory (abbreviated)

| Service | Required | Received | Status |
|---|---|---|---|
| Ortho (TKA/THA) | high | 14 | over (on track + buffer) |
| General | yes | 7 | on track |
| GYN | yes | 3 | under |
| Urology | yes | 1 | under |
| ENT | yes | 2 | on track |
| Spinal recoveries cross-service | yes | 9 | on track |
| MAC | yes | 2 | under |

## Gaps surfaced

- **Urology** — curriculum needs minimum 4 by end of orientation; natural availability low because orientee's Mon-Wed misses the unit's Thu urology block. Engineered option: swap one Wk 6 Mon ortho-heavy day to Thu urology day for one week. Trade-off: lose one ortho day; given over-exposure on ortho, acceptable.
- **GYN** — under by ~3 cases. Natural availability moderate (Wed). Engineered option: prioritize GYN-open patients on Wed when census allows; no schedule change needed.
- **MAC** — under by ~3 cases. Engineered option: ask charge to consider MAC patients for orientee on lighter shifts.

## Recommended assignment adjustments (Wk 5–6)

| Day | Default | Adjustment | Rationale |
|---|---|---|---|
| Wk 5 Mon | ortho | hold | exposure saturated |
| Wk 5 Tue | mixed | seek MAC if available | close MAC gap |
| Wk 5 Wed | GYN | prioritize GYN-open | close GYN gap |
| Wk 6 Mon | ortho | swap to Thu urology one-time | close urology gap |
| Wk 6 Tue | mixed | hold | balanced |
| Wk 6 Wed | GYN | prioritize GYN-open | close GYN gap |

## Charge-nurse handoff note

"This orientee needs more urology, GYN-open, and MAC exposure over the next two weeks. Wk 6 Mon: consider swapping their day to Thu urology. Defer to acuity."
```

Notes: charge authority preserved, trade-offs visible, acuity-over-exposure explicit, no invented schedule data.
</details>

## Self-check

- [ ] Charge authority preserved.
- [ ] Gaps surfaced with engineered options + trade-offs.
- [ ] Handoff note short.
- [ ] Acuity-over-exposure stated.
- [ ] No invented schedules or staffing rules.
- [ ] FPP section passed.
