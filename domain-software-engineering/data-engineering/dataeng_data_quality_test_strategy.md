---
title: "Data Quality Test Strategy — What to Check at Which Layer, Block vs Warn, Who Owns Each Test, and Alerts People Act On"
category: software-engineering/data-engineering
description: "Design the data quality checks for a warehouse or lakehouse as a whole system: which of freshness, volume, schema, uniqueness, referential, validity, distribution and reconciliation checks belong at ingestion, staging, and published marts; which failures block publication and which only warn; who owns each test and its alert; and how to keep the test suite from becoming either silent or ignored."
techniques:
  - DD-03
  - DS-06
  - IPC-08
  - DS-02
  - QA-12
difficulty: intermediate
tags:
  - data-quality
  - data-tests
  - data-freshness
  - schema-checks
  - circuit-breaker
  - data-ownership
  - alert-routing
  - bad-data-in-dashboard
  - who-owns-this-table
  - catch-broken-data-early
updated: "2026-10-03"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_contract_design.md
  - domain-agentic-resources/skills/data-engineering/data-quality-frameworks/SKILL.md
  - domain-software-engineering/data-engineering/dataeng_data_downtime_postmortem.md
---

# Data Quality Test Strategy

**Objective:** Produce a placement plan for data quality checks across the pipeline — each
check at the cheapest layer that can catch the failure, with a severity that decides
whether bad data is published, an owner who receives the alert, and a review loop that
retires tests nobody acts on.

**When to Use:**
- Stakeholders keep finding bad numbers before the data team does.
- There are hundreds of dbt/expectation tests, most failing quietly, and nobody reads the
  alerts channel.
- A new domain (finance, billing, product events) is moving into the warehouse and needs
  checks before anyone relies on it.
- You need to decide what should stop a publish versus post a warning.
- **Not this prompt if** you are writing the producer–consumer agreement itself (fields,
  semantics, SLAs, breaking-change policy) — `domain-AI-ML/data-for-ml/mldata_data_contract_design.md`
  covers that interface and its method applies beyond ML consumers; enforcing a contract in
  CI is `domain-AI-ML/data-for-ml/mldata_data_contract_enforcement_ci.md`. For writing the tests in Great
  Expectations or dbt syntax, use the tool skill
  `domain-agentic-resources/skills/data-engineering/data-quality-frameworks/`. When a data
  failure has already reached users, use `dataeng_data_downtime_postmortem.md`.

## Inputs / Context

1. **Pipeline layers**: sources, raw/landing, staging, intermediate, published marts, BI
   and reverse-ETL consumers.
2. **Critical datasets** and who depends on them (finance close, customer-facing
   features, executive dashboards).
3. **Existing tests**: count, type, failure rate over 30 days, where alerts go.
4. **Past incidents**: what went wrong, who noticed first, how long it took.
5. **Team structure**: producing teams, data platform team, analytics engineers, on-call.

## Method

1. **Rank datasets by consequence.** Tier 1: wrong data causes money movement, customer
   impact, or external reporting errors. Tier 2: internal decisions. Tier 3: exploratory.
   Test depth and blocking behaviour follow the tier.
2. **Place checks cheapest-first (DD-03).** Catch each failure class at the earliest layer
   that can see it:
   - *Ingestion*: freshness (latest event timestamp vs expected), volume (row count vs
     same-weekday baseline), schema (columns, types, nullability against the expected set).
   - *Staging*: primary-key uniqueness and not-null, accepted values, referential integrity
     to reference tables, valid ranges and formats.
   - *Published marts*: grain uniqueness, reconciliation to a system of record (counts and
     control totals for a closed period), business rules (e.g. refunds ≤ original amount),
     distribution checks on key measures.
   - *Consumption*: freshness indicator shown on dashboards, so a stale tile says so.
   A failure caught only at the mart has already cost a full pipeline run.
3. **Decide block vs warn (DS-06).** Block (circuit-break publication, keep last good
   version) when publishing would cause a Tier 1 consequence and the check has a low
   false-alarm history. Warn when the check is new, statistical, or Tier 2–3. Every
   blocking check needs a documented override path and who may use it.
4. **Quarantine, don't repair (IPC-08).** Rows that fail validity checks go to a quarantine
   table with the failing rule, not silently coerced (null → 0, bad date → today).
   Repairs happen at the source or by an explicit, reviewed rule.
5. **Assign ownership.** Each check has one owning team and one alert route. Source-level
   failures route to the producer; transformation failures to the model owner; consumers
   are notified, not paged. An unowned test is deleted or assigned within a sprint.
6. **Set thresholds from data (DS-02).** Volume and distribution checks use baselines (e.g.
   ±3 median absolute deviations against the last 8 same weekdays), with known seasonality
   (month-end, holidays) encoded, not ignored.
7. **Keep the suite honest (QA-12).** Monthly: tests failing > 20% of runs (noise — fix
   threshold or delete), tests never failing in 12 months on Tier 3 data (candidates to
   retire), incidents not caught by any test (gap — add one), mean time from failure to
   acknowledgement per owner.

## Output Format

```
# Data quality test strategy — [platform/domain], [date]

## Dataset tiers
| Dataset | Tier | Consumers | Consequence if wrong |

## Check placement
| Layer | Check | Dataset(s) | Threshold / rule | Block or warn | Owner | Alert route |

## Quarantine and override
Quarantine tables · override procedure · who may override · how overrides are logged

## Ownership map
| Team | Owns checks on | Receives alerts via | Escalation |

## Suite health review (monthly)
| Signal | Threshold | Action |

## Gaps from past incidents
| Incident | Would any planned check have caught it? Where? |
```

## Verification

- [ ] Every Tier 1 dataset has freshness, volume, schema, uniqueness, and reconciliation checks.
- [ ] Each check sits at the earliest layer able to detect its failure.
- [ ] Every blocking check has an override path and named overrider.
- [ ] No check silently repairs data; failing rows are quarantined.
- [ ] Every check has exactly one owner and alert route.
- [ ] Each past incident is mapped to the check that would have caught it.

## False-Positive Prevention

1. **More tests = better quality.** Two hundred unowned failing tests are worse than twenty
   owned ones; the alert channel learns to be ignored.
2. **Static thresholds on seasonal data.** "Row count > 10,000" fails every Sunday and
   every holiday; use same-weekday baselines and encode the calendar.
3. **Blocking on new statistical checks.** A distribution check without a false-alarm
   history should warn for a month before it is allowed to stop publication.
4. **Not-null everywhere.** Some nulls are meaningful (no discount, not yet shipped); test
   validity against the business definition.
5. **Consumers paged for producer failures.** Route to whoever can fix; notify the rest.
6. **Green tests as proof of correct data.** Tests catch the failures you anticipated;
   reconciliation to a system of record catches some you did not.

## Example Output

```
# Data quality test strategy — Billing domain (Stripe + internal ledger → warehouse), 2026-10-01

## Dataset tiers
| fct_invoices        | 1 | finance close, revenue dashboard | misstated revenue, audit finding |
| fct_payment_events  | 1 | dunning reverse-ETL to CRM       | customers emailed wrongly |
| dim_plan            | 2 | product analytics                | wrong plan mix |

## Check placement
| Ingestion | freshness: max(created) within 2 h of now (06–23 UTC) | raw_stripe_* | 2 h | warn → block at 6 h | Data Platform | #billing-data-alerts + page at 6 h |
| Ingestion | volume vs last 8 same weekdays ±3 MAD | raw_stripe_invoices | baseline | warn | Data Platform | channel |
| Ingestion | schema matches expected column set | raw_stripe_* | exact | block | Data Platform | page |
| Staging   | invoice_id unique, not null | stg_invoices | 0 dupes | block | Analytics Eng (billing) | page |
| Staging   | currency in ISO-4217 set; amount ≥ 0 except credit notes | stg_invoices | rule | quarantine + warn | Analytics Eng | channel |
| Mart      | monthly invoice total = ledger total ±0.05% for closed months | fct_invoices | 0.05% | block | Analytics Eng + Finance Systems | page + email Finance |
| Mart      | refunded_amount ≤ amount_paid | fct_payment_events | rule | block reverse-ETL sync only | Analytics Eng | page |
| BI        | freshness badge on revenue dashboard | dashboard | > 6 h stale shows banner | — | BI team | — |

## Override: Finance Systems lead or data on-call may publish past a reconciliation block
for ≤ 24 h with a logged reason; dashboard shows "provisional".

## Suite health (Sept): 214 tests → 61 failing > 20% of runs (all warn, never acted on) →
delete 38, re-baseline 23. Incident 2026-08-14 (duplicate webhook events doubled 3 days of
payments) → would have been caught by staging uniqueness on event_id: added, blocking.
```

## Techniques Used

- **DD-03 Fail-Fast Ordering** — cheap freshness/volume/schema checks at ingestion before expensive mart reconciliations.
- **DS-06 Prioritization and Severity Guidance** — dataset tiers drive block vs warn.
- **IPC-08 Validation Gate, Reject-Don't-Repair** — failing rows quarantined rather than coerced.
- **DS-02 Metric Specification** — thresholds expressed as baselines and tolerances.
- **QA-12 False Positives Identification** — monthly pruning of noisy and never-acted-on tests.

## Related Prompts

- `domain-AI-ML/data-for-ml/mldata_data_contract_design.md` — the producer–consumer agreement these checks enforce.
- `domain-agentic-resources/skills/data-engineering/data-quality-frameworks/SKILL.md` — implementing the checks in Great Expectations or dbt.
- `dataeng_data_downtime_postmortem.md` — when a failure gets past the checks.
