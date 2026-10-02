---
title: "Sales and Operations Planning Cycle — Demand Review, Supply Review, Pre-S&OP, Executive Meeting, and the Decisions Log"
category: operations/supply-chain-procurement
description: "Run one monthly S&OP cycle in product families, not SKUs: an unconstrained consensus demand plan with its bias and error shown, a supply review that states the constraint in units and weeks, a pre-S&OP meeting that reduces the gaps to two or three priced scenarios, an executive meeting that decides rather than reviews, and a decisions log carried into next month."
techniques:
  - AG-40
  - NE-11
  - DS-40
  - QA-04
difficulty: advanced
tags:
  - sales-and-operations-planning
  - s-and-op
  - demand-planning
  - supply-planning
  - capacity-planning
  - consensus-forecast
  - sales-and-ops-disagree
  - monthly-planning-meeting
  - plan-demand-and-supply
updated: "2026-10-02"
related_prompts:
  - domain-operations/supply-chain-procurement/ops_inventory_reorder_policy.md
  - domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md
  - domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md
---

# Sales and Operations Planning Cycle

**Objective:** Take one month's S&OP cycle from raw sales forecast to a signed set of
executive decisions — each demand–supply gap stated in units, weeks, and currency,
resolved by a named choice, and logged so next month starts from what was decided
rather than from a blank agenda.

**When to Use:**
- Sales forecasts one number, operations plans to another, and finance budgets a third.
- Stockouts on some families coincide with overtime or excess on others, and nobody
  owns the trade-off.
- The monthly "S&OP meeting" is a 40-slide review that ends without a decision.
- You are standing up S&OP for the first time and need the five steps in order.
- **Not this prompt if** you are setting SKU-level safety stock and reorder points —
  use `domain-operations/supply-chain-procurement/ops_inventory_reorder_policy.md`
  (policy per SKU, not the monthly family plan). If one resource is overloaded and you
  need its effective capacity and queueing behaviour, use
  `domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md`. If
  the job is designing the finance team's P&L re-forecast process, use
  `domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md`. Your
  own weekly planning rhythm is `domain-productivity/operating-cadence/`.

## Inputs / Context

1. **Product families** (6–15) that share capacity or a planning logic, and the
   unit of measure for each (cases, units, tonnes, labour hours).
2. **Demand history**: 24+ months of shipments *and* orders by family — shipments
   alone hide unmet demand. Tag `measured`.
3. **Statistical baseline forecast** and the sales/marketing overlay (promotions,
   new customers, lost accounts) with each overlay's owner.
4. **Supply data**: capacity by key resource (line, cell, supplier allocation),
   planned downtime, inventory on hand, and open orders by family.
5. **Financial plan**: the annual budget in units and revenue by family, so the
   cycle can show the gap to plan.
6. **Last month's decisions log** and the forecast it was based on.

Missing capacity or forecast inputs become `[measure]` with an owner and date, not a
plausible number.

## Method

Each step has an entry condition, actions, and an exit artefact (AG-40). A step does
not start until the previous exit artefact exists.

1. **Data gathering (business day 1–3).** Close the month: actual shipments, orders,
   and inventory by family. Compute forecast error for the last 3 months:
   `bias = Σ(forecast − actual) / Σ actual`; `WMAPE = Σ|forecast − actual| / Σ actual`
   (NE-11). Exit: one table per family, error stated.
2. **Demand review (day 4–6).** Start from the statistical baseline, then add each
   overlay as a separate, owned line ("+1,200 cases — new retailer, owner: K. Diaz,
   confidence: signed contract"). The output is **unconstrained** demand — what
   customers would buy, not what you can make. Show a range, not a point (QA-04):
   at minimum a high/low from the last 12 months' error. Exit: consensus demand plan
   by family for 18 months, first 3 months monthly.
3. **Supply review (day 7–9).** Load the demand plan onto key resources. For each
   family, state the gap as `required − available` in units and in weeks of
   capacity. List the options that close each gap — overtime, extra shift, pre-build,
   outsourcing, allocation — with lead time to enact and cost per unit. Exit: a
   constrained supply plan and a gap list.
4. **Pre-S&OP (day 10–12).** Cross-functional leads reduce the gap list to the few
   that need an executive decision (cost, service, or policy beyond their authority).
   For each, build 2–3 priced scenarios with revenue, margin, inventory, and service
   effect, and a recommendation. Everything else is decided here and logged. Exit:
   the decision pack — usually 5–8 pages, never 40.
5. **Executive S&OP meeting (day 13–15, 60–90 min).** Agenda in this order: decisions
   log follow-up, KPI scorecard (forecast bias, WMAPE, OTIF, inventory days vs.
   target), then **only** the decision items. Each item ends in a decision, an owner,
   and a date, or an explicit deferral with what information is missing.
6. **Decisions log (DS-40).** Record every decision with the scenario chosen, the
   assumption it depends on, the trigger that would reopen it, and its owner. Next
   month's cycle opens by checking each trigger.
7. **Reconcile to finance.** Convert the agreed plan to revenue and margin by family
   and state the gap to annual budget, so finance and operations carry one number.

## Output Format

```
# S&OP cycle — [month]   Horizon: 18 mo   Families: [n]   Cycle owner: [..]

## 1. Forecast performance (last 3 months)
| Family | Forecast | Actual | Bias % | WMAPE % | Note |

## 2. Consensus demand plan (unconstrained)
| Family | Baseline | Overlays (owner, confidence) | Plan | Range (low–high) |

## 3. Supply review
| Family | Required | Available | Gap (units) | Gap (weeks) | Options (lead time, cost/unit) |

## 4. Decision items for executive meeting
### Item [n]: [gap]
| Scenario | Revenue | Margin | Inventory | Service (OTIF) | Cost |
Recommendation: [..]   Decided at pre-S&OP instead: [list]

## 5. KPI scorecard
| KPI | Target | Actual | Trend |

## 6. Decisions log
| # | Decision | Scenario | Depends on | Reopen trigger | Owner | Date |

## 7. Reconciliation to financial plan
| Family | Plan revenue | Budget revenue | Gap | Explanation |
```

## Verification

- [ ] Forecast error is computed from actuals, with bias and WMAPE both shown.
- [ ] The demand plan is unconstrained; capacity limits appear only in the supply review.
- [ ] Every overlay has an owner and a confidence basis.
- [ ] Every gap is stated in units, weeks of capacity, and the cost of each option.
- [ ] Executive items each have 2–3 scenarios with revenue, margin, inventory, and service.
- [ ] Every executive item ends in a decision, owner, and date — or a deferral with the missing input named.
- [ ] Last month's reopen triggers were checked before new items.

## False-Positive Prevention

1. **Constrained demand.** If sales lowers the forecast because "the plant can't make
   it anyway", unmet demand disappears from the record and the capacity case is never made.
2. **Shipments as demand.** In a short month, shipments understate demand. Use orders,
   or flag the gap.
3. **WMAPE without bias.** A 12% WMAPE can hide a forecast that is 10% high every
   month. Bias is the fixable part; report it first.
4. **Point forecast as fact.** A family with ±25% historical error needs a supply
   plan that survives the low and high case, not just the midpoint.
5. **The review meeting.** If the executive session walks through every family, it is
   a review, not a decision forum. Only gaps that need executive authority go up.
6. **Sandbagged overlays.** An overlay with no owner or confidence basis is a hope.
   Log it as unowned and exclude it from the plan.
7. **Modeled margin as achieved.** Scenario margins are modeled. Next month's actuals
   decide whether the chosen scenario delivered.

## Example Output

```
# S&OP cycle — October 2026   Horizon: 18 mo   Families: 8   Owner: Supply chain director
(Excerpt: 2 of 8 families; units = cases)

## 1. Forecast performance (Jul–Sep, measured)
| Family         | Forecast | Actual  | Bias % | WMAPE % | Note                       |
| Sparkling 12pk | 186,000  | 171,500 | +8.5   | 11.2    | over-forecast 3 of 3 months |
| Still 24pk     | 95,000   | 97,800  | −2.9   | 6.4     | within tolerance           |

## 2. Consensus demand plan — Nov (unconstrained)
| Family         | Baseline | Overlays                                       | Plan   | Range         |
| Sparkling 12pk | 58,000   | −2,000 bias correction (demand planner, history)| 56,000 | 49,700–62,300 |
| Still 24pk     | 31,000   | +6,500 new club-store listing (K. Diaz, signed) | 37,500 | 35,100–39,900 |
Range = plan ± trailing WMAPE.

## 3. Supply review — Line 2 (both families), Nov
Available: 20 shifts × 4,400 cases = 88,000 cases. Required: 93,500.
Gap: 5,500 cases = 1.25 shifts (0.3 weeks).
| Option                   | Lead time | Cost/case | Covers |
| Saturday overtime ×2     | 1 week    | $0.42     | 8,800  |
| Pre-build Still in Oct   | now       | $0.18 carrying (6 wk) | up to 6,000 (warehouse limit) |
| Co-packer                | 5 weeks   | $1.10     | any    |

## 4. Decision item 1: Line 2 November gap (5,500 cases)
| Scenario                | Revenue   | Margin    | Inventory | OTIF  | Cost    |
| A Overtime ×2 Saturdays | +$0       | −$2,310   | flat      | 98%   | $2,310  |
| B Pre-build 5,500 Still | +$0       | −$990     | +5,500 Oct| 98%   | $990    |
| C Ship short Sparkling  | −$63,250  | −$19,000  | flat      | 91%   | lost sale |
Recommendation: B; warehouse holds it, cheapest, reversible.
Decided at pre-S&OP: Still 24pk label change timing; Q1 promotion volume.

## 5. KPI scorecard
| Forecast bias (all) | ±5% | +4.1% | improving |
| OTIF                | 97% | 95.8% | flat      |
| Inventory days      | 28  | 31    | worsening |

## 6. Decisions log
| 1 | Pre-build 5,500 Still in Oct | B | club-store PO confirmed by 15 Oct | PO not confirmed by 15 Oct → stop pre-build | Plant mgr | 13 Oct |
| 2 | Reduce Sparkling baseline 3.5% | — | bias persists | 2 months bias within ±3% → restore | Demand planner | 13 Oct |

## 7. Reconciliation (Nov)
| Sparkling 12pk | $644,000 | $690,000 | −$46,000 | bias correction; budget built on over-forecast |
| Still 24pk     | $431,250 | $356,500 | +$74,750 | new listing not in budget |
```

## Techniques Used

- **AG-40 Numbered Phase Discipline** — five steps, each with entry, actions, and an exit artefact.
- **NE-11 Embedded Calculation Formulas** — bias, WMAPE, gap in units and weeks, scenario cost.
- **DS-40 Follow-Up Action Extraction** — the decisions log with owner, dependency, and reopen trigger.
- **QA-04 Uncertainty Acknowledgment** — demand stated as a range from measured forecast error.

## Related Prompts

- `ops_inventory_reorder_policy.md` — SKU-level safety stock and reorder points beneath the family plan.
- `domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md` — effective capacity of the constraining resource.
- `domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md` — the finance-side re-forecast process the plan reconciles to.
