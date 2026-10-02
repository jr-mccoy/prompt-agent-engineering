---
title: "Freight Mode Selection — Parcel, LTL, FTL, Intermodal, Air, and Ocean on Landed Cost, Service, and Risk, with the Incoterms Consequences"
category: operations/supply-chain-procurement
description: "Choose a freight mode for a recurring shipping lane by computing total landed cost per unit — freight, accessorials, in-transit and safety-stock carrying cost, damage — against the service the customer needs and the risk each mode carries, and state who pays, insures, and bears risk under the chosen Incoterm."
techniques:
  - RT-02
  - NE-11
  - IT-22
  - QA-02
difficulty: intermediate
tags:
  - freight
  - logistics
  - mode-selection
  - ltl-vs-ftl
  - incoterms
  - landed-cost
  - shipping-costs-too-high
  - cheaper-way-to-ship
  - truck-or-container
updated: "2026-10-02"
related_prompts:
  - domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md
  - domain-operations/supply-chain-procurement/ops_inventory_reorder_policy.md
  - domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md
---

# Freight Mode Selection

**Objective:** Recommend a freight mode (or a mix) for one recurring lane by comparing
landed cost per unit, transit time and its variability, and risk — then translate
the choice into its Incoterms consequences and the stock it forces you to carry.

**When to Use:**
- Freight spend is rising and someone asks whether you should "just switch to LTL",
  consolidate to full truckloads, or move from air to ocean.
- A lane's shipment size has grown or shrunk across a mode break point.
- A new supplier or customer location needs a shipping plan.
- Expedited air has become routine and you want to know what it actually costs.
- **Not this prompt if** you are choosing *which supplier* to buy from — use
  `domain-operations/supply-chain-procurement/ops_supplier_selection_scorecard.md`
  (it takes a freight cost as one TCO line; this prompt is how you set that line).
  If you are tendering the lane to carriers, use
  `domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md`. If the
  question is how much stock the chosen lead time requires, finish with
  `ops_inventory_reorder_policy.md`.

## Inputs / Context

1. **Lane**: origin, destination, distance, border crossings.
2. **Shipment profile**: annual volume, typical shipment weight and cube, pallet
   count, frequency, and how often it varies. Tag each `measured` or `estimated`.
3. **Goods**: value per unit, density, fragility, temperature, hazmat class, shelf life.
4. **Service need**: required delivery window, customer penalty for lateness, and
   whether late equals lost sale.
5. **Rates**: current quotes per mode, including fuel surcharge and accessorials
   (liftgate, residential, detention, reclass). A quote without accessorials is partial.
6. **Carrying cost rate** (typically 15–30% per year of inventory value) and current
   safety-stock basis.
7. **Commercial terms**: current or proposed Incoterm (2020 rules) and who arranges
   insurance and customs.

## Method

1. **Screen modes by physical fit.** Rule out modes that cannot carry the goods
   (hazmat on passenger air, temperature on dry van, oversize in parcel). Use the
   usual break points as a starting screen, not a rule:
   parcel ≤ ~70 kg per piece; LTL ~70 kg to ~6 pallets or ~4,500 kg; volume LTL /
   partial to ~12 pallets; FTL above that or ~10,000 kg+; intermodal for FTL-sized
   lanes over ~1,200 km; ocean FCL vs. LCL break near 13–15 m³ (IT-22).
2. **Compute landed cost per unit (NE-11)** for each surviving mode:
   `landed = (linehaul + fuel + accessorials) / units
   + in-transit carrying = unit value × carrying rate × transit days / 365
   + safety-stock carrying = unit value × carrying rate × z × σ_LT × demand rate / annual units
   + damage = damage rate × unit value`.
   Lead-time variability matters as much as lead time: a mode that is 2 days slower
   but ±1 day may need less stock than a faster mode at ±4 days.
3. **Score service and risk separately (RT-02).** Service: mean transit, P90
   transit, on-time history, tracking. Risk: damage and claims history, capacity
   availability in peak, single-carrier dependence, port or border congestion,
   cargo-theft exposure.
4. **Apply Incoterms.** For the chosen mode, state who books the freight, who pays
   main carriage, where risk transfers, who insures, and who clears customs.
   Remember: FCA/CPT/CIP suit containerised and multimodal freight; FOB/CFR/CIF are
   for sea and inland waterway only, with risk passing on board the vessel. EXW leaves
   export clearance with the buyer, which is often impractical. Customs and duty
   classification itself goes to a licensed customs broker.
5. **Stress-test (QA-02).** Re-run the comparison with fuel +20%, volume −30%, and a
   peak-season rate spike. If the winner changes, recommend a mix or a trigger
   ("ship FTL when ≥ 18 pallets accumulate, otherwise LTL").
6. **Recommend** a mode or mixed policy, the annual cost difference, the stock change
   it implies, and a review trigger.

## Output Format

```
# Freight mode selection — [lane]   Annual volume: [..]   Shipment size: [..]

## Feasible modes
| Mode | Fits? | Reason if excluded |

## Landed cost per unit (modeled)
| Component | Mode A | Mode B | Mode C |
Annual landed cost: [..]

## Service and risk
| Mode | Mean transit | P90 transit | On-time | Key risks |

## Incoterms consequence (chosen mode)
Term: [..]  Books freight: [..]  Pays carriage: [..]  Risk transfers at: [..]
Insurance: [..]  Export/import clearance: [..]

## Stress test
| Scenario | Winner | Margin |

## Recommendation
[mode or rule] — annual difference [..] — inventory effect [..] — review trigger [..]
```

## Verification

- [ ] Every mode's rate includes fuel and the accessorials the lane actually incurs.
- [ ] In-transit and safety-stock carrying cost are included, not only freight.
- [ ] Transit is given as mean and P90, not a single quoted day count.
- [ ] Incoterm rule matches the mode (no FOB on a road shipment).
- [ ] Stress-test results are reported with the margin.
- [ ] Modeled figures are labelled; input sources are tagged.

## False-Positive Prevention

1. **Rate per kg as cost.** The cheaper rate can lose once accessorials, reclasses,
   and minimum charges are added. Use invoiced history, not the rate card.
2. **Ignoring the inventory side.** Slower and more variable modes raise in-transit
   and safety stock; on high-value goods this can outweigh the freight saving.
3. **Quoted transit as actual.** Carrier transit times are targets. Use your own
   delivery data or the carrier's on-time history.
4. **FOB used for trucks.** FOB is a sea term. On road or multimodal freight it
   leaves the risk-transfer point ambiguous; use FCA.
5. **Freight class guessed.** An LTL shipment reclassed on density can cost 20–40%
   more than quoted. Measure and declare density.
6. **One peak week as the average.** Model normal and peak separately.
7. **Customs as an afterthought.** Duty and clearance are not decided here; route
   classification to a licensed broker.

## Example Output

```
# Freight mode selection — Dallas DC → Atlanta customer (1,250 km)
Annual volume: 52,000 units   Shipment size: weekly, 8 pallets (~1,000 units, 3,600 kg)
Unit value: $40   Carrying rate: 22%/yr   Demand: 1,000 units/week (σ 180)

## Feasible modes
| Parcel     | No  | 8 pallets per week               |
| LTL        | Yes |                                  |
| FTL (weekly)| Yes | 8 of 26 pallet positions used   |
| FTL (biweekly, 16 pallets) | Yes | holds 1 extra week of stock |
| Intermodal | No  | 1,250 km is at the break point and 8 pallets do not fill a container |

## Landed cost per unit (modeled; rates = 6-mo invoices, measured)
| Component                 | LTL weekly | FTL weekly | FTL biweekly |
| Freight + fuel + access.  | $1,180/1,000 = 1.180 | $2,050/1,000 = 2.050 | $2,050/2,000 = 1.025 |
| In-transit (days)         | 3 d → 0.072 | 2 d → 0.048 | 2 d → 0.048 |
| Safety stock (z=1.65)     | σ_LT 1.5 d → 0.059 | σ_LT 0.5 d → 0.020 | 0.020 |
| Cycle stock (extra week)  | —           | —           | 500 avg units → 0.085 |
| Damage                    | 0.6% → 0.240 | 0.1% → 0.040 | 0.1% → 0.040 |
| Landed per unit           | 1.551       | 2.158       | 1.218       |
Annual: LTL $80,650  FTL weekly $112,220  FTL biweekly $63,340

## Service and risk
| LTL          | 3 d | 5 d | 88% | 2 cross-docks, damage claims 6/yr |
| FTL biweekly | 2 d | 2.5 d | 97% | customer must accept 16 pallets per drop [verify dock] |

## Incoterms consequence (FTL biweekly, domestic: commercial terms, not Incoterms;
if this lane were export, FCA Dallas DC with seller loading would apply)
Seller books and pays carriage; risk transfers at customer dock per sales terms.

## Stress test
| Fuel +20%          | FTL biweekly | $1.31 vs LTL $1.67 |
| Volume −30%        | LTL          | $1.62 vs FTL biweekly $1.66 — winner flips |
| Peak FTL rate +35% | FTL biweekly | $1.58 vs LTL $1.62 — near tie |

## Recommendation
FTL every two weeks: ~$17,300/yr below LTL (modeled), damage down from 6 claims.
Inventory: +500 average units on hand (~$20,000). Break-even is ~750 units/week
(2,050 / 2V + 0.193 = LTL 1.551). Review trigger: if weekly volume falls below
750 units for 6 weeks, revert to LTL.
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — cost, service, and risk kept as separate dimensions.
- **NE-11 Embedded Calculation Formulas** — landed cost per unit including in-transit and safety-stock carrying.
- **IT-22 Workflow Decision Matrix** — mode screen by shipment size, distance, and goods type.
- **QA-02 Adversarial Stress-Test** — fuel, volume, and peak-rate scenarios to find a fragile winner.

## Related Prompts

- `ops_supplier_selection_scorecard.md` — supplier choice, which uses this freight cost as a TCO line.
- `ops_inventory_reorder_policy.md` — safety stock and reorder point once the mode's lead time is set.
- `ops_rfp_procurement_package.md` — tendering the lane to carriers.
