---
title: "Inventory Reorder Policy — ABC/XYZ Segmentation, Safety Stock, Reorder Point, EOQ Sanity, and Service Level"
category: operations/supply-chain-procurement
description: "Set a reorder policy for stocked items: segment SKUs by value (ABC) and demand variability (XYZ), assign a target service level per segment, compute safety stock including lead-time variability, derive the reorder point, sanity-check order quantity against EOQ and MOQ, and state the cost of each extra point of service — with intermittent items routed to methods built for them."
techniques:
  - NE-11
  - DS-06
  - QA-04
  - QA-02
difficulty: intermediate
tags:
  - inventory-management
  - safety-stock
  - reorder-point
  - eoq
  - abc-xyz
  - service-level
  - stock-levels
  - when-to-reorder
  - purchase-orders
  - supplier-lead-time
updated: "2026-09-24"
related_prompts:
  - domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md
  - domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md
  - domain-AI-ML/specialized-ml/time-series/ts_intermittent_demand_forecasting.md
---

# Inventory Reorder Policy

**Objective:** Produce a reorder policy a buyer can load into the ERP or a
spreadsheet — segment, service level, safety stock, reorder point, and order quantity
per SKU class — with every formula shown and every input's source stated.

**When to Use:**
- Stockouts and excess stock exist at the same time across your SKUs.
- Reorder points were set once, by feel, and never revisited.
- A supplier's lead time or reliability changed and you need to know what it costs.
- You are deciding what service level to promise and what it will tie up in stock.
- **Not this prompt if** your problem is forecasting **intermittent or lumpy demand**
  (spare parts, slow movers with many zero periods) — use
  `domain-AI-ML/specialized-ml/time-series/ts_intermittent_demand_forecasting.md`
  first; normal-distribution safety stock below is wrong for those items. Perishable
  or single-period items (newsvendor problems) and multi-echelon networks need
  different models; this prompt flags them rather than forcing them.

## Inputs / Context

1. **SKU list** with annual usage (units) and unit cost.
2. **Demand history** per SKU at a consistent period (daily or weekly), ideally
   12+ months, with stockout periods flagged (they understate demand).
3. **Lead time** per supplier: average and variability (standard deviation or range),
   in the **same period unit** as demand.
4. **Costs**: order/setup cost per order, holding cost rate (% of unit cost per year).
5. **Supplier constraints**: MOQ, pack size, order days.
6. **Service target** or the business's tolerance for stockouts per segment.

## Method

1. **Segment (DS-06).** ABC by annual usage value (commonly A ≈ top 80% of value,
   B next 15%, C last 5%). XYZ by coefficient of variation of period demand
   (e.g. X < 0.5, Y 0.5–1.0, Z > 1.0). State the cut-offs used.
2. **Assign service levels per cell.** Define the metric: **cycle service level
   (CSL)** = probability of no stockout during a replenishment cycle; **fill rate** =
   share of demand met from stock. They are different numbers. Typical starting
   points: AX high CSL, CZ lower; Z items get flagged for a different method.
3. **Compute safety stock (NE-11).** With demand and lead-time variability:
   `SS = z × √(LT × σd² + d̄² × σLT²)`
   where d̄ = mean demand per period, σd = its standard deviation, LT = mean lead time
   in periods, σLT = its standard deviation. Show the demand-only term
   (`z × σd × √LT`) alongside, so the cost of lead-time unreliability is visible.
4. **Reorder point.** `ROP = d̄ × LT + SS`. If review is periodic rather than
   continuous, use `LT + review period` in place of LT and say so.
5. **Order quantity sanity (EOQ).** `EOQ = √(2DS ÷ H)` with D = annual demand,
   S = cost per order, H = unit cost × holding rate. Round to MOQ and pack size, and
   show the total-cost penalty of deviating — it is usually small near EOQ.
6. **Cost of service (QA-02).** Recompute SS at one lower and one higher service
   level; state the annual holding-cost difference per SKU and the expected stockout
   cycles per year (`(1 − CSL) × orders per year`).
7. **Flag assumptions (QA-04).** Normality of demand over lead time, stationarity,
   history censored by stockouts. Mark each SKU's policy `confident`, `review`, or
   `wrong model — route`.

## Output Format

```
# Reorder policy — [site / category]   Period unit: [day | week]   Review: [continuous | every N]

## Segmentation (cut-offs: ABC [..], XYZ CV [..])
| Cell | SKUs | % of value | Service metric & target | Method |

## Per-SKU policy
| SKU | d̄ | σd | LT | σLT | z | SS (demand-only) | SS (full) | ROP | EOQ | Order qty | Status |

## Cost of service
| SKU | CSL | SS | SS holding $/yr | Expected stockout cycles/yr |

## Assumptions and routed items
```

## Verification

- [ ] Demand and lead time use the same period unit.
- [ ] Cut-offs for ABC and XYZ are stated.
- [ ] The service metric (CSL or fill rate) is named, not just "service level".
- [ ] Safety stock includes lead-time variability, or states why it is omitted.
- [ ] Order quantity respects MOQ/pack size and the EOQ penalty is shown.
- [ ] Z-class and intermittent items are routed, not forced into the formula.
- [ ] Stockout-censored history is flagged.

## False-Positive Prevention

1. **Unit mismatch.** Daily demand with lead time in calendar weeks, or working-day
   demand with calendar-day lead time, silently mis-sizes stock. Convert first.
2. **Ignoring lead-time variability.** When suppliers are unreliable, the σLT term
   often dominates safety stock; demand-only formulas under-protect.
3. **Treating CSL as fill rate.** A 95% CSL can deliver a fill rate well above 95%;
   promising customers the CSL number misstates the service.
4. **Normal formulas on intermittent demand.** Mostly-zero demand breaks the
   normal assumption; route those SKUs.
5. **Demand history that hides stockouts.** Periods with no stock record zero sales,
   not zero demand. Exclude or adjust them.
6. **EOQ as gospel.** EOQ is flat near its minimum and sensitive to guessed order
   and holding costs. Use it as a sanity check against MOQ, not a precise answer.
7. **One service level for everything.** Uniform 99% on C items ties up cash where
   stockouts cost least.

## Example Output

```
# Reorder policy — Fasteners category   Period: working day (250/yr)   Review: continuous

## Segmentation (ABC 80/15/5 by value; XYZ CV <0.5 / 0.5–1.0 / >1.0)
| AX | 62  | 51% | CSL 97.5% | formula below          |
| AY | 41  | 27% | CSL 95%   | formula below          |
| CZ | 310 | 2%  | —         | route: intermittent method |

## Per-SKU policy  (SKU FS-2210, AX; LT from 14 POs)
d̄ 40/day  σd 12  LT 9 days  σLT 2 days  z 1.96 (CSL 97.5%)
SS demand-only = 1.96 × 12 × √9 = 71
SS full        = 1.96 × √(9 × 144 + 1,600 × 4) = 1.96 × √7,696 = 1.96 × 87.7 = 172
ROP = 40 × 9 + 172 = 532
EOQ: D 10,000, S $60, H = $25 × 24% = $6 → √(2 × 10,000 × 60 ÷ 6) = 447
MOQ 500 → order 500. Annual cost at 447: $1,342 + $1,341 = $2,683; at 500:
$1,200 + $1,500 = $2,700 → +$17/yr. Status: confident.
Note: lead-time variability adds 101 units of safety stock — worth raising with the
supplier (see scorecard).

## Cost of service (FS-2210, 20 orders/yr; SS holding at $6/unit/yr)
| CSL 95%   | SS 144 | $864/yr   | 1.0 |
| CSL 97.5% | SS 172 | $1,032/yr | 0.5 |
| CSL 99%   | SS 204 | $1,224/yr | 0.2 |

## Assumptions and routed items
Demand over lead time assumed ~normal (CV 0.3). 3 weeks of Q1 history excluded
(stockout). 310 CZ SKUs routed to intermittent forecasting before any policy.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — SS, ROP, EOQ, and stockout-cycle formulas shown with values.
- **DS-06 Prioritization and Severity Guidance** — ABC/XYZ segmentation sets service by value and variability.
- **QA-04 Uncertainty Acknowledgment** — assumption flags and per-SKU status.
- **QA-02 Adversarial Stress-Test** — service level recomputed up and down to price each point.

## Related Prompts

- `ops_supplier_selection_scorecard.md` — lead time and reliability as sourcing criteria.
- `ops_capacity_and_bottleneck_model.md` — when the replenishment constraint is internal capacity.
- `domain-AI-ML/specialized-ml/time-series/ts_intermittent_demand_forecasting.md` — Croston/SBA/TSB for intermittent SKUs.
