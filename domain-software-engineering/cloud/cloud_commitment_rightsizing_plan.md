---
title: "Commitment and Rightsizing Plan — Remove Waste, Rightsize, Then Commit to the Floor: Coverage, Break-Even Utilisation, Flexibility, and Laddered Purchases"
category: cloud
description: "Sequence cloud savings so commitments are bought against the usage that will still exist: remove idle waste and schedule non-production first, rightsize from percentile utilisation with stated exclusions, re-measure the hourly baseline, then size reserved-capacity or savings-plan commitments to the usage floor using break-even utilisation, choose the flexibility each workload's roadmap needs, ladder purchases so expiries are staggered, and stress-test the plan against planned migrations and demand loss."
techniques:
  - NE-11
  - NE-10
  - QA-02
  - DP-07
difficulty: advanced
tags:
  - reserved-instances
  - savings-plans
  - committed-use-discounts
  - rightsizing
  - commitment-coverage
  - commitment-utilization
  - cloud-waste
  - lower-cloud-bill
  - paying-for-unused-servers
  - should-we-prepay-cloud
updated: "2026-10-03"
related_prompts:
  - domain-software-engineering/cloud/cloud_cost_optimization.md
  - domain-software-engineering/cloud/cloud_finops_cost_allocation.md
  - domain-software-engineering/cloud/cloud_bill_spike_investigation.md
---

# Commitment and Rightsizing Plan

**Objective:** Produce a purchase-ready commitment plan — what to commit, which instrument,
what term, how much, and when — that is sized after waste removal and rightsizing, priced
with break-even utilisation, and robust to the roadmap changes that would strand it.

**When to Use:**
- Commitments are expiring, or coverage is low and finance wants a purchase recommendation.
- Someone proposes "buy 3-year reservations for everything" and you need the numbers.
- Utilisation of existing commitments has fallen below ~90% and you need to know why.
- Rightsizing and commitment are being worked by different people in the wrong order.
- **Not this prompt if** you want a broad audit of every savings lever (storage tiers,
  network, spot, serverless) — use `cloud_cost_optimization.md`; this prompt goes deep on
  the commitment decision and the rightsizing that must precede it. Designing who owns
  commitments, tagging, and showback is `cloud_finops_cost_allocation.md`. If spend just
  jumped and you do not know why, start with `cloud_bill_spike_investigation.md`.

## Inputs / Context

1. **Hourly usage history**, 60–90 days, in on-demand-equivalent cost per hour, by service
   and (where relevant) instance family and region.
2. **Existing commitments**: type, scope, term, hourly amount, expiry dates, utilisation and
   coverage over the last 30 days.
3. **Utilisation metrics** for rightsizing: CPU and memory percentiles per instance or
   node group; database and cache utilisation.
4. **Provider discount rates** for the candidate instruments, terms, and payment options —
   from the provider's current pricing pages or calculator for your actual mix.
5. **Roadmap**: migrations (architecture change, region move, containers, serverless,
   different processor family), planned decommissions, expected growth or contract risk.
6. **Finance constraints**: cash vs. opex preference, cost of capital, approval thresholds.

## Method

1. **Remove waste first.** Idle and orphaned resources (unattached volumes, idle load
   balancers, stale snapshots, stopped-but-billed resources) and non-production running
   24×7. Scheduling non-prod to 12 h × 5 weekdays cuts its hours to 60 of 168 (≈ 64% off).
   Commitments bought before this lock in waste.
2. **Rightsize from percentiles.** Candidate: p95 CPU < 40% and p99 memory < 60% over 30
   days with no scheduled peaks missing from the window. Step down one size (usually ~50%
   cost) or move family (compute vs memory optimised). Exclude with reasons: per-core
   licensed software, JVMs whose heap is pinned to instance memory, latency-critical
   services with headroom requirements, anything scaling horizontally where the fix is the
   autoscaling policy instead.
3. **Re-measure the baseline.** After changes settle (2–4 weeks), compute the hourly
   on-demand-equivalent distribution: minimum, P10, median, P90. The commitable floor is
   about P10 — the level usage exceeds ~90% of hours.
4. **Price the commitment (NE-11).** For a commitment priced at discount *d*:
   - Hourly commitment covering on-demand usage *U*: `C = U × (1 − d)`.
   - Break-even utilisation = `1 − d`: at a 28% discount the commitment beats on-demand only
     if ≥ 72% of it is used every hour on average.
   - Annual saving at full use = `U × d × 8,760`.
   Report coverage (share of eligible usage covered) and expected utilisation separately;
   high coverage with low utilisation is the expensive failure.
5. **Choose flexibility per workload.** More flexible instruments (spend-based plans that
   follow you across instance families, regions, or compute services) pay a lower discount
   than instruments locked to a family and region. Use the locked, deeper discount only for
   workloads whose family and region will not change within the term; use flexible
   instruments for anything on the migration roadmap. 3-year terms only for usage that has
   existed and is expected to exist for the full term.
6. **Ladder the purchases.** Buy in tranches (e.g. 50% of target now, 25% each in two later
   quarters) so expiries stagger, each purchase uses newer baseline data, and no single
   renewal date carries the whole estate.
7. **Stress-test against the roadmap (NE-10, QA-02, DP-07).** For each planned change and
   a demand-loss case (largest customer churns), estimate the probability and the new
   floor; compute utilisation of the proposed commitment under each. Name how the plan
   fails: which scenario pushes utilisation below break-even, and what the plan does then
   (reduce later tranches, shift workload onto the commitment, marketplace resale where
   the instrument allows).

## Output Format

```
# Commitment and rightsizing plan — [org/scope], [date]

## Step 1–2: waste and rightsizing
| Action | Resources | Monthly saving | Owner | Status |
Excluded from rightsizing (with reason): [...]

## Step 3: re-measured baseline (on-demand-equivalent $/h)
min [..] · P10 [..] · median [..] · P90 [..] · existing commitment cover [..]

## Step 4–5: commitment proposal
| Workload group | Instrument (flexibility) | Term / payment | Discount d | Covered U ($/h) | C ($/h) | Break-even util. | Expected util. | Annual saving (full use) |

## Step 6: ladder
| Tranche | Date | Amount ($/h) | Expires |

## Step 7: stress test
| Scenario | Probability | New floor ($/h) | Utilisation of plan | Below break-even? | Response |

## Totals and assumptions
```

## Verification

- [ ] Waste removal and rightsizing come before commitment sizing, with the baseline re-measured after.
- [ ] Commitment is sized to a stated percentile floor, not average or peak usage.
- [ ] Break-even utilisation is computed for each instrument from its discount.
- [ ] Discount rates are cited as inputs from current pricing, not assumed.
- [ ] Every roadmap item is checked against instrument flexibility.
- [ ] Purchases are laddered; no single month holds all expiries.
- [ ] At least one stress scenario is run and the response is stated.

## False-Positive Prevention

1. **Committing to average usage.** Average sits above the floor; the hours below it are
   paid twice — once in the commitment, once as unused commitment.
2. **Deepest discount by default.** A locked instrument on a workload migrating processor
   family next quarter strands most of its value.
3. **Rightsizing from CPU alone.** Memory-bound and I/O-bound services look idle on CPU;
   check memory, network, and disk before downsizing.
4. **Low utilisation read as "buy less" only.** Sometimes the fix is moving eligible
   workload onto the commitment (scope, region, or account sharing settings).
5. **Quoting a provider's maximum discount.** "Up to" figures assume the longest term and
   full upfront payment; price your actual mix.
6. **Treating rightsizing savings as additive to commitment savings.** Rightsizing lowers
   the base the discount applies to; compute them in sequence, not separately.

## Example Output

```
# Commitment and rightsizing plan — Fieldnote prod + staging (AWS), 2026-10-03

## Step 1–2: waste and rightsizing
| Delete 212 unattached volumes, 1,900 snapshots > 180 d | storage | $6,300/mo | Platform | done |
| Staging off 20:00–08:00 and weekends | 46 instances | $9,800/mo | Platform | live 10-07 |
| Downsize 38 instances (p95 CPU 9–31%, p99 mem 22–55%) | API, workers | $11,200/mo | Service owners | 2 weeks |
Excluded: 6 search nodes (heap pinned to 50% RAM), 4 licensed DB hosts (per-core licence).

## Step 3: baseline after changes (on-demand equivalent, compute only)
min $118/h · P10 $126/h · median $161/h · P90 $214/h · existing cover: $64/h OD-equivalent
(remaining Compute SP, expires 2027-03-31)

## Step 4–5: proposal (rates from AWS pricing for this mix, 1-yr no upfront)
| General compute (moving 30% to ARM in Q1) | Compute SP (cross-family) | 1 yr / no upfront | 28% | 47 | 33.8 | 72% | 96% | $115k |
| Data-warehouse ETL nodes (stable family/region) | EC2 Instance SP | 1 yr / no upfront | 35% | 15 | 9.75 | 65% | 99% | $46k |
Total new cover $62/h → with existing $64/h = $126/h = P10. Coverage of eligible usage ≈ 78%.

## Step 6: ladder
| T1 | 2026-10-10 | Compute SP $20/h + Instance SP $9.75/h | 2027-10 |
| T2 | 2027-01-10 | Compute SP $14/h (after ARM migration re-measure) | 2028-01 |
| Existing | — | $46/h commitment | 2027-03 → re-size at renewal |

## Step 7: stress test
| ARM migration done (no floor change; SP flexible) | 0.8 | $126/h | 100% | no | — |
| Largest customer (14% of load) churns | 0.15 | $108/h | 86% | no | skip T2 |
| Batch moved to Spot in Q2 | 0.4 | $112/h | 89% | no | reduce renewal of existing |
| Churn + Spot together | 0.06 | $94/h | 75% | close to 72% | skip T2, shrink renewal |

## Totals: waste + rightsizing $27,300/mo [estimate, after rollout]; new commitments ≈ $161k/yr
at full use, ≈ $144k at expected utilisation [estimate]. 3-year terms rejected: roadmap too uncertain beyond 12 months.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — commitment sizing, break-even utilisation, and annual saving computed from the discount.
- **NE-10 Probability-Weighted Scenarios** — roadmap and demand-loss scenarios with probabilities and new floors.
- **QA-02 Adversarial Stress-Test** — utilisation of the plan checked under each scenario against break-even.
- **DP-07 Failure Mode Prediction** — how the plan fails and the pre-agreed response for each scenario.

## Related Prompts

- `cloud_cost_optimization.md` — the broad audit of every savings lever.
- `cloud_finops_cost_allocation.md` — commitment ownership, tagging, and showback as an operating program.
- `cloud_bill_spike_investigation.md` — explaining a jump in spend, including one caused by an expired commitment.
