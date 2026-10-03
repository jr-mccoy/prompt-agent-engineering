---
title: "Fixed-Fee Engagement Overrun Diagnosis — Earned Hours, Estimate at Completion, Variance by Cause, Staffing-Mix Effect, and Recovery Options Before the Margin Is Gone"
category: specialized-fields/professional-services
description: "Diagnose a fixed-fee or capped professional engagement that is running over budget while it is still running: measure percent complete by deliverable evidence rather than hours spent, compute earned hours, cost performance and estimate at completion two ways, split the overrun into scope added, client-caused delay or breached assumptions, estimate error, internal rework and staffing-mix cost, then price the recovery options (change request, re-staffing, descoping, phasing, absorbing) against the firm's margin floor — distinct from closing out a finished engagement (finance_engagement_profitability_postcalc) and from the scope-drift checkpoint in client-services-studio."
techniques:
  - NE-11
  - RT-09
  - DP-07
  - NE-17
difficulty: advanced
tags:
  - fixed-fee
  - engagement-economics
  - estimate-at-completion
  - earned-value
  - scope-creep
  - change-request
  - project-going-over-budget
  - fixed-price-job-losing-money
  - client-work-over-hours
updated: "2026-10-03"
reasoning:
  styles: [quantitative, diagnostic, decisional]
  stakes: high
  horizon: weeks
  uncertainty: risk
  evidence_quality: mixed
  domain_complexity: moderate
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [engagement_manager, engagement_partner, project_controller]
  mode: [diagnose, decide]
related_prompts:
  - domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md
  - domain-specialized-fields/trades/trades_change_order_pricing_notice.md
  - domain-specialized-fields/professional-services/proserv_utilization_realization_review.md
---

# Fixed-Fee Engagement Overrun Diagnosis

**Objective:** While an over-budget fixed-fee engagement can still be saved, establish
how far through it really is, where it will finish, why the hours ran over — each
cause separated, because each has a different remedy — and which recovery moves
restore the margin, with the partner decision and client conversation set up.

**When to Use:**
- Hours to date on a fixed-fee or capped engagement are ahead of progress.
- The engagement manager says "we'll catch up" and the partner wants a number.
- You suspect some of the overrun is scope the client added or delays the client
  caused, and want to know whether a change request is justified.
- **Not this prompt if** the engagement is **finished** and you are recording what
  it earned — `domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md`.
  For a solo practice's structural scope-drift check against the agreed record,
  use stage 7 of `client-services-studio/` (scope ledger). Pricing a construction
  change mid-job is `domain-specialized-fields/trades/trades_change_order_pricing_notice.md`.
  Firm-wide write-down patterns across many engagements are
  `domain-specialized-fields/professional-services/proserv_utilization_realization_review.md`.

## Inputs / Context

1. **The deal**: fee, fee basis (fixed, capped, milestone), the SOW's deliverables,
   assumptions, exclusions and client responsibilities.
2. **The budget**: hours by deliverable and by grade, internal cost rates, target
   margin, and the firm's margin floor.
3. **Actuals**: hours to date by deliverable and grade, with time narratives.
4. **Progress evidence**: deliverables accepted, drafts reviewed, workshops held,
   data received — not opinions about percent complete.
5. **Events**: client requests, late inputs, changes of client contact, internal
   staffing changes, with dates.

Contract positions (whether an assumption was breached, whether a change can be
charged) are flagged for the engagement partner and, where disputed, counsel. Tag
figures `[data]`, `[estimate]`, `[assumption]`.

## Method

1. **Measure percent complete from evidence.** By deliverable: accepted = 100%,
   otherwise count completed milestones within it. Hours spent are not progress.
2. **Compute earned hours and EAC (NE-11).**
   `Earned hours (EV) = Σ budget hours × % complete`;
   `CPI = EV / actual hours`;
   `EAC (trend) = actual + (budget − EV) / CPI`;
   `EAC (bottom-up) = actual + re-estimated remaining hours by deliverable`.
   Report both; the gap between them is the forecast risk.
3. **Split the overrun by cause (RT-09).** For each deliverable, actual − earned
   hours, assigned to: **scope added** (work outside the SOW), **client dependency**
   (late or poor inputs, breached assumptions), **estimate error** (in-scope work
   harder than estimated), **internal rework** (review cycles, quality fixes),
   each traced to time narratives or events.
4. **Separate the mix effect.** More senior hours than planned raises cost even
   when hours are on plan: `mix effect = actual hours × (actual cost/h − planned
   cost/h)`.
5. **Forecast margin.** EAC cost at actual mix and at planned mix, margin against
   the floor.
6. **Price recovery options and how each fails (DP-07).** Change request for scope
   and breached assumptions (with SOW reference); re-staff remaining work to plan
   mix; descope or phase with client agreement; tighten review; absorb. For each:
   hours or dollars recovered, likelihood, client-relationship cost, and how it could
   go wrong.
7. **Decide and set up the conversation (NE-17).** The partner decision needed, the
   client message (anchored to the SOW, not to the firm's problem), and the date.

## Output Format

```
# Overrun diagnosis — [engagement]   Fee $[..] ([basis])   Week [x] of [y]
Budget [..] h / $[..] cost · target margin [..]% · floor [..]%

## 1. Progress by deliverable (evidence-based)
| Deliverable | Budget h | % complete (evidence) | Earned h | Actual h | Variance |
## 2. Performance and forecast
CPI [..] · EAC trend [..] h · EAC bottom-up [..] h
## 3. Overrun by cause
| Cause | Hours | Evidence | Chargeable? |
Mix effect: $[..]
## 4. Margin forecast
| Scenario | EAC cost | Fee | Margin |
## 5. Recovery options
| Option | Recovers | Likelihood | Relationship cost | How it fails |
## 6. Decision needed · client message · date
```

## Verification

- [ ] Percent complete is evidenced per deliverable, not derived from hours.
- [ ] Earned hours, CPI and both EACs recompute.
- [ ] Overrun causes sum to total variance and each cites evidence.
- [ ] Mix effect is computed separately from hours variance.
- [ ] Margin is forecast against the stated floor in each scenario.
- [ ] Change requests cite the SOW clause or assumption they rely on.

## False-Positive Prevention

1. **Percent spent as percent complete.** 75% of hours used does not mean 75% done;
   that assumption is how overruns stay hidden until the last month.
2. **All overrun as scope creep.** Clients recognise when estimate error is being
   billed back; claim only what the SOW supports.
3. **Ignoring mix.** A partner doing manager work keeps hours on budget and the
   margin off it.
4. **Optimistic EAC only.** The bottom-up estimate is the team's view; the trend
   EAC is what usually happens. Show both.
5. **Absorbing silently.** An unflagged overrun becomes a write-down and a precedent
   for the next renewal price.
6. **Contract positions asserted.** Whether an assumption was breached is a
   judgement for the partner; disputed ones go to counsel.

## Example Output

```
# Overrun diagnosis — Revenue-cycle redesign, Mercy Valley Hospital (illustrative)
Fee $180,000 fixed   Week 8 of 12
Budget 820 h: Partner 60 @ $220, Manager 220 @ $140, Consultant 540 @ $80 = $87,200
Planned cost/h $106.3 · target margin 51.6% · floor 35%

## 1. Progress
| D1 Current-state assessment | 220 | 100% (accepted wk 5)         | 220 | 300 | +80 |
| D2 Future-state design      | 300 | 60% (3 of 5 workshops, draft) | 180 | 250 | +70 |
| D3 Implementation roadmap   | 180 | 0%                            | 0   | 0   | 0   |
| D4 PM and steering          | 120 | 67% (8 of 12 weeks)           | 80  | 90  | +10 |
| Total                       | 820 |                               | 480 | 640 | +160 |

## 2. Forecast
CPI = 480 / 640 = 0.75. EAC trend = 640 + 340 / 0.75 = 1,093 h.
EAC bottom-up = 640 + (D2 150 + D3 200 + D4 40) = 1,030 h.

## 3. Overrun by cause (160 h)
| Scope added: second clinic site (SOW §2: one site)         | 50 | Client email wk 3 | Yes |
| Scope added: weekly steering (SOW: fortnightly)             | 10 | Calendar          | Yes |
| Client dependency: billing extract late and incomplete     | 30 | SOW assumption 4 (clean extract by wk 2) | Arguable |
| Estimate error: workshops needed 2 sessions each            | 50 | Time narratives   | No  |
| Internal rework: design draft rewritten after review        | 20 | Review log        | No  |
Mix: actual 70 P / 250 M / 320 C = $76,000 → $118.75/h vs $106.3 planned
→ mix effect 640 × $12.41 ≈ $7,940.

## 4. Margin forecast (bottom-up 1,030 h)
| No action (remaining 390 h at actual mix)  | $122,300 | $180,000 | 32.1% |
| Re-staff to planned mix                    | $117,500 | $180,000 | 34.7% |
| Re-staff + change request $19,800 accepted | $117,500 | $199,800 | 41.2% |
| Re-staff + second site only ($11,000)      | $117,500 | $191,000 | 38.5% |

## 5. Recovery options
| Change request: site 2 + weekly steering (60 h × $220) | $13,200 | High | Low | Client argues site 2 was implied — SOW §2 is explicit |
| Change request: data clean-up (30 h × $220) | $6,600 | Medium | Medium | Assumption wording loose — partner judgement |
| Re-staff remaining work (mainly D3) to planned mix, manager review only | $4,840 | High | None | Quality slips if review is skipped |
| Descope D3 to a 2-page roadmap | 100 h | Low | High | Client sees it as a cut deliverable |

## 6. Decision
Partner approval needed: without a change request, margin falls below the 35% floor.
Recommend re-staff now + change request for site 2 and weekly steering; raise data
clean-up as a request, not a demand. Client message, steering 14 Oct: "The SOW covered
one site and fortnightly steering; you asked for two sites and weekly meetings, which
we were glad to do. Here is the change request for that additional work."
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — earned hours, CPI, two EACs, mix effect and margin scenarios.
- **RT-09 Root Cause Explanation Pattern** — overrun traced to cause with evidence, because each cause has a different remedy.
- **DP-07 Failure Mode Prediction** — how each recovery option could go wrong before choosing it.
- **NE-17 Call-to-Action Mandatory Close** — the partner decision, the client message and its date.

## Related Prompts

- `domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md` — the close-out reckoning after the engagement ends.
- `domain-specialized-fields/trades/trades_change_order_pricing_notice.md` — the construction-trades version of pricing a change mid-job.
- `domain-specialized-fields/professional-services/proserv_utilization_realization_review.md` — firm-wide realization and write-down patterns.
