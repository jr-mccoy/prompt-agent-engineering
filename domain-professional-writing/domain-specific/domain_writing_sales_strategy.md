---
title: "Head of Sales Strategy Document — Segment Choices, Ramp-Adjusted Capacity, Quotas That Reconcile to the Number"
category: professional-writing/domain-specific
description: "Write a Head of Sales's annual or half-year sales strategy for the sales team and executives: a segment baseline from CRM data, priorities including the segment being deprioritised, ramp-adjusted capacity against the plan number, quotas and territories recomputed to reconcile with plan plus over-assignment, pipeline requirements derived from the team's own win rates, and metrics with exact definitions. Distinct from a single-account plan, a period forecast call, and marketing go-to-market strategy."
techniques:
  - NE-11
  - QA-15
  - RT-23
  - DS-02
  - RP-02
difficulty: advanced
tags:
  - head-of-sales
  - sales-strategy
  - sales-capacity-planning
  - quota-setting
  - territory-design
  - pipeline-coverage
  - annual-sales-kickoff-document
updated: "2026-10-06"
related_prompts:
  - domain-sales-customer/sales/sales_strategic_account_plan.md
  - domain-sales-customer/sales/sales_forecast_commit_review.md
  - domain-business-strategy/go-to-market/workflow_marketing_campaign_brief_development.md
  - domain-business-strategy/startup/monetization_pricing_strategy.md
---

# Head of Sales Strategy Document

**Objective:** Produce a sales strategy in which the plan number, the team's ramp-adjusted
capacity, the sum of quotas and the pipeline requirement all reconcile, and every rep
can find their segment, territory, quota and the metrics they are judged on.

**When to Use:**
- You are setting the sales plan for a fiscal year or half and presenting it to the
  executive team and the sales organisation (often for a kickoff).
- The plan number has gone up, the team is changing shape (hires, segment moves), or
  the motion is changing (a segment moving to self-serve or inside sales).
- Last year's quotas did not add up to the plan, or territories overlapped.
- **Not this prompt if** you are planning one named key account — use
  `domain-sales-customer/sales/sales_strategic_account_plan.md`; calling this period's
  number deal by deal is `domain-sales-customer/sales/sales_forecast_commit_review.md`;
  building outbound sequences for a territory is
  `domain-sales-customer/sales/sales_outbound_prospecting_sequence.md`. Positioning,
  messaging and marketing campaigns are `domain-business-strategy/go-to-market/`; setting
  prices themselves is `domain-business-strategy/startup/monetization_pricing_strategy.md`.
  This document takes the price book as an input.

**Audience:** Executives (CEO, CFO) need to see that the number is reachable with the
headcount funded, what it costs, and where the risk sits. Reps and managers need their
segment, territory, quota, motion and metrics, stated so nobody has to ask what they are
accountable for.

## Inputs / Context

Paste source material inside named tags and refer to it by name, e.g.
`<crm_export>`, `<plan>`, `<roster>`, `<price_book>`, `<win_loss>`.

1. **Current state** `<crm_export>` — trailing four quarters by segment: new ACV, win rate
   (with its definition), average deal size, cycle length, open pipeline by stage.
2. **Plan number** `<plan>` — the bookings target from finance, its definition (new ACV?
   total contract value? including expansion?), and any portion not owned by sales
   (self-serve, partner).
3. **Market context** — customer landscape, competitive moves, win/loss reasons
   `<win_loss>`.
4. **Strategic priorities** — segments, verticals, deal sizes, and which segment gets
   less attention.
5. **Go-to-market approach** — motion per segment, pricing and packaging from
   `<price_book>`, discount authority.
6. **Team structure and capacity** `<roster>` — reps by segment, ramped or not, hire
   start dates, ramp history (how productive new hires were in year one), attrition
   history, territories, current quotas, over-assignment policy.
7. **Enablement and tools** — training, collateral, systems the team needs.
8. **Success metrics** — what will be measured, and how each is defined today.

## Method

1. **Build the baseline with provenance (RT-23).**
   - Per segment from `<crm_export>`: new ACV, win rate, deal size, cycle, open pipeline.
     Tag each figure `[data]`, `[estimate]` (rep survey, manager judgement) or
     `[assumption]`.
   - Note where definitions differ between sources (a win rate by count vs by value).
2. **Choose priorities, including what gets less.** Rank segments; for the
   deprioritised one, say what happens to existing accounts (who renews them), to
   inbound leads, and to quota credit.
3. **Compute capacity against plan (NE-11).**
   - Segment capacity = ramped reps × ramped productivity + Σ(new hires × year-one ramp
     factor × ramped productivity).
   - Use productivity and ramp from history, not from quota.
   - Sales-owned plan = plan − portions owned elsewhere. Cushion = capacity −
     sales-owned plan; rerun with the attrition assumption.
   - If capacity is below plan, state the gap and the options (hires, plan change,
     accepted risk); do not close it with an assumed win-rate improvement.
4. **Set quotas and territories, then recompute (QA-15).**
   - Σ quotas ≥ sales-owned plan × (1 + over-assignment policy). Compute both totals
     twice — once by segment, once by rep — and show the check line.
   - Every target account or geography is assigned exactly once; new hires get named
     territories; overlays state how credit splits so nothing is double counted.
   - Quota relative to productivity should be the same across a segment unless a
     difference is explained.
5. **Derive pipeline requirements from the team's own win rates.**
   Required pipeline = expected bookings ÷ win rate; generation needed = required −
   current open pipeline expected to close in the period. State the coverage ratio this
   implies rather than quoting a rule of thumb.
6. **Set the motion per segment.** Field, inside or self-serve; pricing and discount
   authority from `<price_book>` exactly; any packaging change only if in the inputs.
7. **Tie enablement to diagnosed gaps.** Each enablement item names the loss reason or
   metric it targets from step 1 or `<win_loss>`.
8. **Define metrics exactly (DS-02).** For each: definition, owner, cadence, and the
   threshold that triggers action.
9. **Write for both readers (RP-02).** Executive summary first (number, capacity,
   cushion, cost, risk); then a "what this means for you" section per role.
10. **Verify.** Capacity, quota and pipeline totals recompute from their components;
    every input figure has a provenance tag; the deprioritised segment's accounts all
    have an owner.

## Output Format

```
# Sales Strategy: [period]
For: [exec team; sales organisation]   Plan: [number and definition]

## Summary
[plan, sales-owned portion, capacity and cushion, quota total and over-assignment,
the three priorities, the main risk]

## Where we are   (trailing 4Q, provenance tagged)
| Segment | New ACV | Win rate | Avg deal | Cycle | Open pipeline |

## Market context
## Priorities and what gets less
## Motion by segment   | Segment | Motion | Pricing / discount authority |

## Capacity vs plan
[formula; per-segment computation; cushion; attrition case]

## Territories and quotas
| Segment | Territories | Reps | Quota per rep | Segment quota |
Check: [sum] = [total]; over-assignment = [..]%

## Pipeline requirements
| Segment | Expected bookings | Win rate | Required pipeline | Open now | To generate |

## Enablement   | Gap (evidence) | Enablement | Owner | Date |
## Metrics and cadence   | Metric | Definition | Owner | Cadence | Action threshold |
## What this means for you   [by role]
## Risks and assumptions   | Assumption | Provenance | If wrong |
```

## Verification

- [ ] Every baseline figure carries a provenance tag and a stated definition.
- [ ] Capacity uses historical productivity and ramp, not quota.
- [ ] Sales-owned plan excludes portions sales does not control.
- [ ] Σ quotas recomputed by segment and by rep agree, and meet the over-assignment
      policy.
- [ ] Every account or geography in scope is assigned once; new hires have territories.
- [ ] Pipeline requirements use the team's own win rates.
- [ ] The deprioritised segment's existing accounts and inbound leads have an owner.
- [ ] Each metric has a definition and an action threshold.

## False-Positive Prevention

1. **Quotas that do not reconcile to the number.** Managers set quotas by region, the
   sheet totals to something near plan, and nobody checks the over-assignment.
   Recompute Σ quotas by segment and by rep against sales-owned plan × (1 + policy)
   and print the check line.
2. **Capacity built from quota instead of history.** Multiplying reps by quota
   produces exactly the plan by construction. Capacity comes from what ramped reps
   actually closed, and new hires at their measured year-one ramp.
3. **A plan number that silently includes self-serve or partner bookings.** If finance's
   number includes revenue sales does not drive, sales quotas built on the full number
   double-assign it; built on a reduced number, sales cannot cover a self-serve miss.
   Split it and say which.
4. **Pipeline coverage by folklore.** "We need 3x coverage" is a rule of thumb; the
   team's own 22% win rate implies 4.5x. Derive coverage from the win rate in
   `<crm_export>` and label it.
5. **Every segment a priority.** A strategy where SMB, mid-market and enterprise all
   grow with no change in motion has not chosen. Name the segment that gets less, and
   what happens to its accounts.
6. **Win-rate improvement as the gap-closer.** Closing a capacity shortfall by assuming
   win rates rise five points turns a staffing problem into a hope. Show the gap at
   current win rates first.
7. **Metrics with drifting definitions.** "Pipeline" that means Stage 1+ in one review
   and Stage 2+ in another makes coverage incomparable month to month. Fix the stage
   and close-date window in the metric definition.

## Example Output

```
# Sales Strategy: FY27
For: CEO, CFO; all sales staff   Plan: $12.0M new ACV (<plan>: first-year contract value
of new logos and expansions; excludes renewals and services)

## Summary
Sales-owned plan $11.2M ($0.8M is self-serve, owned by Growth). Ramp-adjusted capacity
$11.9M: cushion $0.7M, $0.45M after expected attrition. Quotas total $12.53M (11.9%
over-assignment). Priorities: (1) enterprise with SE coverage from Stage 2, (2)
mid-market price-loss recovery, (3) SMB moves to self-serve. Main risk: enterprise
pipeline generation must reach $1.6M a month, nearly double the current rate.

## Where we are (trailing 4Q, <crm_export> [data] unless tagged)
| Segment      | New ACV | Win rate* | Avg deal | Cycle    | Open Stage 2+ |
| Enterprise   | $5.1M   | 22%       | $85k     | 118 days | $9.4M |
| Mid-market   | $4.6M   | 30%       | $32k     | 54 days  | $6.1M |
| SMB (AE-sold)| $1.1M   | 41%       | $9k      | 21 days  | —     |
Total $10.8M; FY27 plan is +11.1% ($12.0M ÷ $10.8M = 1.111).
*Won ÷ (won + lost), by count, Stage 2+ opportunities closed in period.
SMB deals took ~25% of mid-market AE time [estimate: rep survey].

## Market context
Two competitors launched lower-priced mid-market tiers; 9 of the last 31 mid-market
losses cited price (<win_loss>). Enterprise losses cluster at security review
(7 of 19).

## Priorities and what gets less
1 Enterprise (≥1,000 employees): 320 named accounts, SE assigned by Stage 2.
2 Mid-market (200–999): recover price losses with value case, not discount.
3 SMB (<200) gets less: inbound goes to self-serve; 410 existing SMB accounts move to
  Customer Success for renewal; no AE quota credit for new deals under $15k ACV.

## Motion by segment
| Segment    | Motion            | Pricing / discount authority (<price_book>) |
| Enterprise | Field AE + SE     | List; AE ≤10%, manager ≤20%, above → deal desk |
| Mid-market | Inside AE         | List; AE ≤10%, manager ≤15% |
| SMB        | Self-serve        | Published plans only |

## Capacity vs plan
Capacity = ramped AEs × ramped productivity + new hires × year-one ramp × productivity.
Productivity [data]: Enterprise $900k, Mid-market $500k. Ramp [data: last two cohorts]:
Enterprise hires (start 1 Feb) 0.5; Mid-market hires (start 1 Apr) 0.4.
  Enterprise: 6 × 900k + 2 × 0.5 × 900k = 5.40M + 0.90M = $6.30M
  Mid-market: 10 × 500k + 3 × 0.4 × 500k = 5.00M + 0.60M = $5.60M
  Capacity $11.90M − sales-owned plan $11.20M = cushion $0.70M (6.3%)
Attrition [assumption: one mid-market AE leaves mid-year, as in each of the last two
years] −$0.25M → cushion $0.45M (4.0%).

## Territories and quotas
| Segment    | Territories                         | Reps        | Quota per rep | Segment quota |
| Enterprise | 8 × 40 named accounts               | 6 ramped    | $950k         | $5.70M |
|            |                                     | 2 new       | $475k         | $0.95M |
| Mid-market | 13 geographic                       | 10 ramped   | $525k         | $5.25M |
|            |                                     | 3 new       | $210k         | $0.63M |
Check by rep: 6×950k + 2×475k + 10×525k + 3×210k = 5.70 + 0.95 + 5.25 + 0.63 = $12.53M
Check by segment: 6.65 + 5.88 = $12.53M ✓   Over-assignment 12.53 ÷ 11.20 = 11.9% (policy ≥10%)
Managers' draft set quotas equal to productivity: total $11.90M, 6.3% over — below
policy; replaced by the above. Every quota is 95% of expected productivity, both
segments, ramped and new. Territory potential within ±15% of mean (RevOps scoring).

## Pipeline requirements
| Segment    | Expected bookings | Win rate | Required | Open now | To generate | Per month |
| Enterprise | $6.30M            | 22%      | $28.6M   | $9.4M    | $19.2M      | $1.6M |
| Mid-market | $5.60M            | 30%      | $18.7M   | $6.1M    | $12.6M      | $1.05M |
Implied coverage: 4.5x enterprise, 3.3x mid-market. Assumes open pipeline closes this
FY at the same win rate. Current enterprise generation ≈ $0.85M/month [data: last 2Q].

## Enablement
| Gap (evidence)                          | Enablement                       | Owner      | Date   |
| 7 of 19 ENT losses at security review    | Security pack; SE from Stage 2   | SE lead    | 31 Jan |
| 9 of 31 MM losses on price               | Value calculator; competitor card| Enablement | 28 Feb |
| New hires at 0.4–0.5 ramp                | 30/60/90 onboarding, shadowing   | Managers   | Start date |

## Metrics and cadence
| Metric | Definition | Owner | Cadence | Action threshold |
| New ACV | As <plan> definition | Head of Sales | Weekly forecast | <90% of quarter-to-date target |
| Pipeline generated | New Stage 2+ value, close date ≤2 quarters out | Marketing + SDR lead | Monthly | ENT < $1.3M (80% of $1.6M) |
| Win rate | As defined above | Segment managers | Quarterly | 3 pts below baseline |
| SE coverage | ENT Stage 2+ opps with SE assigned | SE lead | Monthly | <90% |

## What this means for you
Enterprise AE: 40 named accounts, $950k quota ($475k in year one), SE on every Stage 2.
Mid-market AE: your geography, $525k ($210k in year one), no SMB deals under $15k.
Managers: territory review each quarter; weekly forecast on the definitions above.
SDRs: enterprise target $1.6M Stage 2+ pipeline a month, split across 4 SDRs.

## Risks and assumptions
| Assumption | Provenance | If wrong |
| Win rates hold (22% / 30%) | [data] trailing 4Q | 2-pt ENT drop → required pipeline $31.5M |
| Year-one ramp 0.5 / 0.4 | [data] two cohorts | Each 0.1 lower on ENT hires → −$0.18M |
| Enterprise generation doubles | [assumption] | Main risk; monthly threshold above |
| Self-serve delivers $0.8M | Growth's plan, not sales | Shortfall not covered by sales quotas |
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — ramp-adjusted capacity, cushion, and pipeline
  required from win rate.
- **QA-15 Self-Consistency** — quotas totalled by rep and by segment, and checked against
  plan × over-assignment.
- **RT-23 Input Provenance Tagging** — data, estimate and assumption tags on every baseline
  and risk figure.
- **DS-02 Metric Specification** — each metric with definition, owner, cadence and action
  threshold.
- **RP-02 Audience-Specific Framing** — executive summary and a per-role "what this means
  for you".

## Related Prompts

- `domain-sales-customer/sales/sales_strategic_account_plan.md` — plans for the named
  enterprise accounts in each territory.
- `domain-sales-customer/sales/sales_forecast_commit_review.md` — the weekly forecast call
  against these quotas.
- `domain-business-strategy/go-to-market/workflow_marketing_campaign_brief_development.md`
  — the campaigns behind the pipeline-generation target.
- `domain-business-strategy/startup/monetization_pricing_strategy.md` — setting the price
  book this document takes as given.
