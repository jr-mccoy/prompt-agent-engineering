---
title: "Cloud Bill Spike Investigation — Is It Real, Where Is It, and Is It Growth or an Anomaly?"
category: cloud
description: "Investigate a sudden rise in a cloud bill in a fixed order: rule out billing artefacts (data lag, amortisation views, credits ending, one-off purchases, commitments expiring), then decompose the increase by account or project, service, usage type or SKU, and resource or tag until one line explains most of it, and classify it as growth (unit cost flat, volume up), efficiency regression (unit cost up), or anomaly (spend with no matching demand) — ending with an owner, a containment step, and an estimate of the month-end impact."
techniques:
  - DD-03
  - RT-06
  - RT-09
  - RT-23
difficulty: intermediate
tags:
  - cloud-cost
  - cost-anomaly
  - finops
  - billing-data
  - usage-type-analysis
  - unit-cost
  - cloud-bill-jumped
  - unexpected-cloud-charges
  - why-did-costs-go-up
updated: "2026-10-03"
related_prompts:
  - domain-software-engineering/cloud/cloud_finops_cost_allocation.md
  - domain-software-engineering/cloud/cloud_cost_optimization.md
  - domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md
---

# Cloud Bill Spike Investigation

**Objective:** Explain a specific jump in cloud spend down to the team, service, SKU, and
resource that caused it; say whether it is healthy growth, a regression, or an anomaly;
contain it if needed; and forecast what it will do to this month's bill.

**When to Use:**
- A budget alert or anomaly alert fired, or finance asked why last month was 30% higher.
- Daily spend stepped up and has stayed up since a release, migration, or new customer.
- A single day's charge looks absurd (a forgotten GPU cluster, a runaway loop).
- You need to tell a team "this is yours" with evidence they will accept.
- **Not this prompt if** you are designing the tagging, allocation, showback, and anomaly
  alerting *program* — use `cloud_finops_cost_allocation.md`; this prompt investigates one
  spike using whatever allocation exists. For a broad savings sweep with no specific spike,
  use `cloud_cost_optimization.md`. For committed-use purchasing, use
  `cloud_commitment_rightsizing_plan.md`. A solo developer's GCP budget guardrails are
  `gcp_solo_dev_cost_management.md`; ML training/inference spend attribution is
  `domain-AI-ML/mlops-infrastructure/mlops_cost_attribution_showback.md`.

## Inputs / Context

1. **Billing data access**: cost explorer / billing reports, or the detailed billing export
   (e.g. AWS CUR, GCP billing export to BigQuery, Azure cost exports) — daily granularity
   at minimum.
2. **The spike as seen**: amount, dates, which view (invoice, unblended, amortised).
3. **Allocation available**: account/project structure, tag coverage %.
4. **Demand drivers**: requests, active customers, jobs run, data volume — per day.
5. **Change log**: deploys, migrations, new regions, contract or commitment changes.

## Method

1. **Rule out billing artefacts first (DD-03).** Cheapest checks before any resource hunt:
   - Is the period complete? Detailed billing data lags hours to a day and late charges
     post after month end.
   - Which cost view? An upfront commitment purchase appears as one huge charge in an
     unblended/cash view and as a daily amount in the amortised view.
   - Did credits (startup, promotional, migration) end, or a discount program change?
   - One-off or annual charges: support plan, marketplace annual subscription, domain or
     certificate renewals, tax.
   - Did a reservation or savings plan *expire*? Usage unchanged + cost up on exactly the
     covered service is the signature.
2. **Normalise to daily spend.** Compare the same weekdays before and after; find the
   first day of the step. A step (sustained shift) and a spike (one to three days) have
   different causes.
3. **Decompose top-down.** Account/project → service → usage type/SKU (e.g. "data
   processed by NAT gateway", "log ingestion", "GPU instance hours", "cross-zone
   transfer") → resource id or tag. At each level keep the line that explains ≥ 50% of the
   delta. Stop when one or two lines explain ≥ 80%.
4. **Correlate with demand and changes (RT-06).** Put the cost line next to its demand
   driver and the change log. Compute unit cost (cost ÷ driver) before and after:
   - Volume up, unit cost flat → **growth** (expected; check it was forecast).
   - Unit cost up → **efficiency regression** (a release changed behaviour: chattier
     calls, debug logging, a lost cache, cross-region reads).
   - Cost up with no matching demand → **anomaly** (forgotten resource, runaway retry
     loop, leaked credentials mining crypto, misconfigured autoscaling).
5. **Explain the mechanism (RT-09).** Cause → billing line it produced → why that rate →
   fix. Example: "Debug logging enabled in 3.14 → +1.9 TB/day log ingestion → billed per
   GB ingested → revert log level and add an ingestion budget alert."
6. **Tag every number's provenance (RT-23).** `[billing]` from billing data, `[metric]` from
   monitoring, `[estimate]` for forecasts and unit-cost estimates. Forecast the month-end
   impact from days remaining at the post-step daily rate.
7. **Contain and assign.** Anomaly → stop or scale down now (with the owner), and if
   unexplained compute appears in unused regions, treat as a possible credential
   compromise and involve security. Regression → ticket to owning team with the unit-cost
   evidence. Growth → update forecast and budget.

## Output Format

```
# Cloud spend investigation — [account/org], [period]
Spike: [amount] over [dates] in [view: amortised/unblended] · Status: open/contained/explained

## Billing artefact checks
| Check | Result | Evidence |

## Decomposition
| Level | Line | Before (daily) | After (daily) | Δ | Share of total Δ |

## Demand and unit cost
| Line | Driver | Unit cost before | Unit cost after | Verdict (growth/regression/anomaly) |

## Mechanism
Cause → billing line → rate → fix

## Impact and actions
Month-end impact: [estimate] · Containment: [...] · Owner: [...] · Follow-ups: [...]

## Open questions / unexplained remainder
```

## Verification

- [ ] All billing-artefact checks are recorded before any resource-level conclusion.
- [ ] The cost view (amortised vs unblended) is stated and consistent throughout.
- [ ] The explained lines cover ≥ 80% of the delta, or the remainder is listed as unexplained.
- [ ] The verdict rests on unit cost against a named demand driver.
- [ ] Every number is tagged billing, metric, or estimate.
- [ ] Containment and owner are named for anomalies and regressions.

## False-Positive Prevention

1. **A commitment purchase read as a spike.** In a cash view a 1-year upfront purchase is
   one day's enormous charge; check the amortised view.
2. **Expiry read as usage growth.** Coverage ending raises cost with flat usage; the fix is
   a renewal decision, not an engineering hunt.
3. **Growth labelled waste.** If unit cost is flat and the demand was planned, the bill is
   doing what it should; update the forecast.
4. **Incomplete days compared to complete ones.** Today's partial data makes every
   dashboard look like a drop, and last month's late charges make it look like a rise.
5. **Tag-based conclusions on low tag coverage.** If 40% of spend is untagged, "team X
   is up 20%" may be a tagging change; check by account/resource too.
6. **Stopping at the service level.** "EC2 went up" is not an explanation; usage type and
   resource are.

## Example Output

```
# Cloud spend investigation — Fieldnote prod org (AWS), Sept 2026
Spike: +$38,400 vs August (amortised; org daily Δ +$1,865), step began 2026-09-11 · Status: explained, contained 10-02

## Billing artefact checks
| Period complete | Sept closed; CUR final 10-02 | [billing] |
| Cost view | amortised throughout | — |
| Credits ending | none active | [billing] |
| One-off charges | Enterprise support +$1,100 (usage-linked) | [billing] |
| Commitment expiry | Compute SP 1 of 2 expired 09-30; affects Oct only | [billing] |

## Decomposition (daily averages, 09-01..10 vs 09-11..30)
| Account   | prod-data         | $2,140 → $3,690 | +$1,550 | 83% |
| Service   | EC2-Other         | $310 → $1,610   | +$1,300 | 70% |
| Usage type| NatGateway-Bytes (us-east-1) | $95 → $1,320 | +$1,225 | 66% |
| Resource  | nat-0a1… (private subnet of ingest workers) | — | — | — |
| Service   | CloudWatch Logs ingestion | $60 → $290 | +$230 | 12% |

## Demand and unit cost
| NAT bytes | events ingested/day 410 M → 430 M (+5%) | $0.23 → $3.07 per M events | regression |
| Logs      | same driver | $0.15 → $0.67 per M events | regression |

## Mechanism
Release 3.14 (09-11) moved ingest workers to fetch enrichment data from S3 through the NAT
gateway instead of the S3 gateway endpoint (route table dropped in Terraform refactor) →
~27 TB/day processed at the per-GB NAT rate [billing ÷ rate]. Debug logs left on in the
same release → ~0.46 TB/day extra log ingestion.
Fix: restore S3 gateway endpoint route; log level back to INFO.

## Impact and actions
Sept impact (20 days after the step): regression $29,100 (NAT $24,500 + logs $4,600)
[billing]; growth ~$7,700 in compute and storage tracking +5% events [estimate]; support
uplift $1,100 [billing].
Contained 10-02 14:00; NAT bytes back to $92/day on 10-03 [billing, partial day].
Owner: Data Platform. Follow-ups: Terraform plan check for endpoint routes; anomaly alert on
NAT bytes per account > 2× 14-day median; October renewal decision for expired SP → see
commitment plan.
## Unexplained remainder: ~$500 (1.3%) spread across 40 small lines.
```

## Techniques Used

- **DD-03 Fail-Fast Ordering** — billing-artefact checks run before any resource-level hunt.
- **RT-06 Correlation and Cross-Analysis** — cost lines set against demand drivers and the change log to compute unit cost.
- **RT-09 Root Cause Explanation Pattern** — cause → billing line → rate → fix.
- **RT-23 Input Provenance Tagging** — every figure tagged billing, metric, or estimate.

## Related Prompts

- `cloud_finops_cost_allocation.md` — the tagging and anomaly-alerting program this investigation relies on.
- `cloud_cost_optimization.md` — a broad savings sweep when there is no single spike to explain.
- `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` — the same "is it real, then decompose" discipline for business metrics.
