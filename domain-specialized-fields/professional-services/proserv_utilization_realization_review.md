---
title: "Utilization and Realization Review for a Professional Services Firm — Chargeable Hours by Grade, the Realization Chain, Write-Down Causes, Leverage, and the Profit-per-Partner Levers"
category: specialized-fields/professional-services
description: "Review a quarter or year of a multi-person accounting, consulting, engineering or architecture firm's economics: fix the definitions of available and chargeable hours, compute utilization by grade against grade-specific targets, walk standard value to billed to collected (billing, collection and overall realization), split write-downs by cause, measure leverage and effective rate, and use the margin × productivity × leverage identity to show which lever moves profit per partner — distinct from a solo practice's forward capacity plan (services_capacity_and_utilization_planner) and from one engagement's close-out post-calc (finance_engagement_profitability_postcalc)."
techniques:
  - DS-01
  - DS-02
  - NE-11
  - QA-21
difficulty: intermediate
tags:
  - utilization
  - realization-rate
  - write-downs
  - leverage-ratio
  - professional-services-firm
  - practice-management
  - team-not-billing-enough
  - why-are-we-writing-off-time
  - is-our-firm-profitable
updated: "2026-10-03"
reasoning:
  styles: [quantitative, analytic, diagnostic]
  stakes: medium
  horizon: months
  uncertainty: risk
  evidence_quality: mixed
  domain_complexity: moderate
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [managing_partner, practice_leader, firm_administrator, finance_director]
  mode: [evaluate, diagnose]
related_prompts:
  - domain-business-strategy/client-services/services_capacity_and_utilization_planner.md
  - domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md
  - domain-specialized-fields/professional-services/proserv_fixed_fee_overrun_diagnosis.md
---

# Utilization and Realization Review

**Objective:** Show a firm's leaders where the hours went and where the money
leaked — how busy each grade was against a fair target, how much of the work's
standard value was billed and then collected, why the rest was written down, and
which single lever (utilization, realization, leverage or margin) would most
improve profit per partner.

**When to Use:**
- Quarter- or year-end review in a firm of roughly 10–500 professionals that
  records time.
- Partners argue about whether the problem is "not enough work" or "not getting
  paid for the work we do".
- Write-downs are rising and nobody can say why.
- **Not this prompt if** you are a **solo practitioner or very small practice**
  asking whether pipeline will cover your next empty month — use
  `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md`.
  To reconcile **one finished engagement's** estimate against actual, use
  `domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md`. A
  fixed-fee engagement still running over budget is
  `domain-specialized-fields/professional-services/proserv_fixed_fee_overrun_diagnosis.md`.

## Inputs / Context

1. **People**: headcount by grade, standard hours, leave and holidays, and anyone
   in non-chargeable roles.
2. **Time records**: chargeable and non-chargeable hours by person, grade, service
   line and engagement for the period.
3. **Rates**: standard (rack) rate by grade.
4. **Billing and collections**: billed amounts by engagement, write-downs at
   billing with reason codes if any, collections and write-offs.
5. **Fee basis** per engagement: hourly, fixed fee, capped, retainer.
6. **Targets**: utilization targets by grade and the firm's margin.

Tag inputs `[data]` (time and billing system), `[estimate]` or `[assumption]`.
Firm financial figures are for management discussion with the firm's accountant;
this is not accounting or tax advice.

## Method

1. **Fix definitions first (DS-02).** Available hours = standard hours − leave and
   holidays. Chargeable = hours recorded to client engagements (state whether
   written-down hours still count — they should). Utilization = chargeable /
   available. Standard value = chargeable hours × standard rate. A firm comparing
   numbers built on different denominators is comparing nothing.
2. **Utilization by grade.** Targets differ by grade (partners sell and manage;
   staff deliver). Report each grade against its own target, and the firm total.
3. **Walk the realization chain (NE-11).**
   `Billing realization = billed / standard value`;
   `Collection realization = collected / billed`;
   `Overall realization = collected / standard value`;
   `Effective rate = collected / chargeable hours`. Split by service line and fee
   basis.
4. **Decompose write-downs by cause.** Agreed rate discount at pricing,
   fixed-fee overrun, scope delivered without a change order, training or rework
   time charged to the client, billing disputes. Pricing discounts are a pricing
   decision; the rest are execution.
5. **Leverage and pyramid.** Professionals per partner (headcount) and non-partner
   to partner chargeable hours. Too little leverage means partners doing staff
   work; too much with low realization often means under-supervised work.
6. **Profit levers (DS-01).** Use the identity
   `profit per partner = margin × (fees / professional) × (professionals / partner)`
   and quantify one realistic move on each lever.
7. **Audit the incentives (QA-21).** Utilization targets reward charging hours to
   clients that will be written down; realization targets reward under-recording
   time. Check for both: chargeable hours with unusually high write-downs, and
   engagements with suspiciously low recorded hours.

## Output Format

```
# Utilization and realization — [firm]   Period: [..]   Professionals: [n]
Definitions: available = [..] · chargeable = [..] · written-down hours [counted / not]

## 1. Utilization by grade
| Grade | Headcount | Available h | Chargeable h | Utilization | Target |
## 2. Realization chain
Standard value $[..] → billed $[..] ([..]%) → collected $[..] ([..]%) · overall [..]%
Effective rate $[..]/h vs blended standard $[..]/h
## 3. By service line / fee basis
## 4. Write-downs by cause
| Cause | $ | Share | Pricing or execution |
## 5. Leverage
## 6. Profit levers (margin × productivity × leverage)
## 7. Incentive audit
## 8. Actions
```

## Verification

- [ ] Utilization and realization definitions are stated before any figure.
- [ ] Every grade is measured against its own target.
- [ ] The realization chain recomputes from standard value to collected.
- [ ] Write-down causes sum to total write-downs.
- [ ] Pricing discounts are separated from execution write-downs.
- [ ] Each profit lever is quantified with the same identity.

## False-Positive Prevention

1. **Utilization as the goal.** High utilization with low realization is unpaid
   work; the two are read together.
2. **One target for everyone.** Partners at 80% chargeable are not selling or
   supervising; juniors at 50% are under-deployed.
3. **Realization blamed on clients.** Most write-downs are decided inside the
   firm — pricing, scoping and supervision.
4. **Excluding written-down hours.** Removing them from chargeable hours makes
   both utilization and realization look better at once.
5. **Collection timing.** Bills issued late in the period are not yet collectible;
   state the measurement date.
6. **Average rate hides mix.** A rising effective rate can come from more partner
   hours on the same work, not better pricing.

## Example Output

```
# Utilization and realization — Harlow & Pike (accounting and advisory, illustrative)
Period: Q3   Professionals: 42 (5 partners)   Available: 480 h/person [data]
Written-down hours counted as chargeable. Collections measured 45 days after quarter-end.

## 1. Utilization by grade
| Partner  | 5  | 2,400 | 1,080 | 45.0% | 45% |
| Manager  | 9  | 4,320 | 2,940 | 68.1% | 70% |
| Senior   | 12 | 5,760 | 4,490 | 78.0% | 80% |
| Staff    | 16 | 7,680 | 5,680 | 74.0% | 82% |
| Firm     | 42 | 20,160 | 14,190 | 70.4% |    |
Staff 8 pts below target = 614 h unused.

## 2. Realization chain
Standard value: 1,080×$450 + 2,940×$300 + 4,490×$210 + 5,680×$150 = $3,162,900
Billed $2,720,000 (86.0%) → collected $2,610,000 (96.0%; $38k written off, $72k > 60 days)
Overall realization 82.5%. Effective rate $183.9/h vs blended standard $222.9/h.

## 3. By service line
Audit & assurance (mostly fixed fee): standard $1,580,000 → billed $1,201,000 (76.0%)
Tax & advisory (mostly hourly):     standard $1,582,900 → billed $1,519,000 (96.0%)

## 4. Write-downs ($442,900)
| Fixed-fee overruns (audit)              | 168,000 | 38% | Execution |
| Rate discounts agreed at engagement     | 96,000  | 22% | Pricing   |
| Scope delivered without change order    | 84,000  | 19% | Execution |
| Training / rework charged to client     | 62,000  | 14% | Execution |
| Billing disputes                        | 32,900  | 7%  | Execution |

## 5. Leverage
37 non-partner professionals / 5 partners = 7.4 (the identity below uses all 42 / 5 = 8.4);
non-partner : partner chargeable hours = 13,110 / 1,080 = 12.1.

## 6. Profit levers (margin 30% [data])
Profit per partner = 0.30 × ($2,610k / 42) × (42 / 5) = $156.6k for the quarter.
+5 pts audit billing realization = $79k → +$15.8k per partner.
Staff to 82% target: +614 h × $150 × 76% audit realization ≈ $70k, only if there is
billable work for it — check against the overruns first.
Largest lever: audit fixed-fee overruns — run proserv_fixed_fee_overrun_diagnosis on
the three worst engagements.

## 7. Incentive audit
Two managers record > 90% chargeable with 31% write-downs: rework charged to clients.

## 8. Actions
Reprice the 6 audits renewing in Q1 using actual hours; require change orders for
scope above SOW; code training time non-chargeable; supervision review of audit files.
```

## Techniques Used

- **DS-01 Framework Application** — the realization chain and the margin × productivity × leverage identity.
- **DS-02 Metric Specification** — available, chargeable and standard value defined before any number.
- **NE-11 Embedded Calculation Formulas** — utilization, realization, effective rate and the profit-lever arithmetic.
- **QA-21 Metric Gaming Vector Enumeration** — how utilization and realization targets get gamed.

## Related Prompts

- `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` — a solo or small practice's sellable days and bench date.
- `domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md` — one closed engagement's estimate-versus-actual.
- `domain-specialized-fields/professional-services/proserv_fixed_fee_overrun_diagnosis.md` — diagnosing a running fixed-fee engagement that is over budget.
