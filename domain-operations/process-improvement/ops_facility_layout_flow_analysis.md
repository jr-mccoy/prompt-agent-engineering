---
title: "Facility Layout Flow Analysis — Spaghetti Diagram, From-To Matrix, Load-Distance Score, and Layout Options Compared"
category: operations/process-improvement
description: "Analyse how material and people move through a building — a spaghetti diagram of one product's path, a from-to matrix of trips between areas, a load × distance score for the current layout and each alternative, adjacency requirements and fixed constraints — and compare two or three layout options on flow, cost, disruption, and safety review needs."
techniques:
  - NE-11
  - RT-02
  - CM-02
  - QA-02
difficulty: intermediate
tags:
  - facility-layout
  - spaghetti-diagram
  - from-to-matrix
  - material-flow
  - travel-distance
  - plant-layout
  - rearrange-the-warehouse
  - too-much-walking
  - where-to-put-equipment
updated: "2026-10-02"
related_prompts:
  - domain-operations/process-improvement/ops_process_map_and_waste_scan.md
  - domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md
  - domain-operations/process-improvement/ops_standard_work_and_kaizen_event.md
---

# Facility Layout Flow Analysis

**Objective:** Quantify how far material and people travel under the current layout,
find the adjacencies that drive that travel, and compare layout options on a
load-distance score plus cost, disruption, and constraints — so a re-layout is
chosen on flow evidence, not on where the empty floor space happens to be.

**When to Use:**
- Operators or forklifts cross the building repeatedly and nobody knows how far.
- You are adding equipment, a new product line, or moving into a new building.
- A warehouse re-slot or shop re-layout is proposed and needs a before/after case.
- Congestion or forklift–pedestrian conflicts are rising.
- **Not this prompt if** the question is how much the process can produce — use
  `domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md`
  (capacity, not space). If you need the step-by-step value stream with touch and
  queue time, start with `ops_process_map_and_waste_scan.md`. If the redesign is
  inside one cell or workstation, use `ops_standard_work_and_kaizen_event.md`.
  Building systems, structural loads, egress, and fire code belong to the qualified
  engineer and authority having jurisdiction, not to this prompt.

## Inputs / Context

1. **Floor plan** with dimensions, columns, doors, docks, aisles, and fixed items
   ("monuments": pits, cranes, ovens, compressors, sprinkler-restricted zones).
2. **Areas or departments** to place, with required floor area.
3. **Flow data**: trips or unit loads per day between each pair of areas — from
   routings × volumes, WMS/forklift logs, or a 1–2 day observation. Tag `measured`,
   `sampled (n=)`, or `estimated`.
4. **Product routings** for the main product families.
5. **Qualitative adjacency needs**: must be close (shared operator, quality check),
   must be apart (noise, contamination, heat, hazardous storage).
6. **Constraints and budget**: move cost per item, downtime allowed, lease limits.

## Method

1. **Spaghetti diagram.** Trace one representative product (or one picker's shift)
   on the plan; count path length per unit and crossings with other flows. This
   shows the problem; it is not the dataset.
2. **From-to matrix (NE-11).** For every pair of areas, record loads per day.
   Distances measured along the aisle path (rectilinear), not straight line.
   `load-distance score = Σ (loads_ij × distance_ij)` — in load-metres per day.
   Rank pairs by load: typically 20% of pairs carry most of the flow.
3. **Adjacency requirements.** Combine the top flow pairs with qualitative needs
   into a relationship chart (A absolutely necessary, E especially important,
   I important, O ordinary, U unimportant, X undesirable) — the Muther SLP scale.
4. **Constraints (CM-02).** List what cannot move or cannot be adjacent: monuments,
   floor load limits, utilities, egress routes, hazardous material separation,
   dock positions. Every option must respect them.
5. **Generate 2–3 options.** Typically: (a) minimal move — relocate the top one or
   two flow pairs; (b) product-family flow — line or U-shaped cells by routing;
   (c) the ideal ignoring cost, as a reference. Compute the load-distance score for
   each (RT-02: also score cost, disruption days, flexibility, safety).
6. **Stress-test (QA-02).** Re-score with next year's product mix or ±30% on the
   biggest family. A layout tuned to today's mix can be wrong in 12 months.
7. **Recommend** with modeled travel savings converted to hours and cost, the
   one-time move cost, payback, and the items that need qualified review (racking,
   egress, fire, electrical, floor loading).

## Output Format

```
# Layout analysis — [facility / area]   Data: [source, dates]

## Current-state spaghetti (product / route: [..])
Path per unit: [..] m   Crossings: [..]   Notable backtracks: [..]

## From-to matrix (loads/day)
| From \ To | A | B | C | ... |
Top pairs: | Pair | Loads/day | Distance (m) | Load × distance |
Current load-distance score: [..] load-m/day

## Adjacency chart (A/E/I/O/U/X)
| Pair | Rating | Reason |

## Constraints
[monuments, egress, utilities, separation rules]

## Options
| Criterion | Current | Option 1 | Option 2 | Option 3 |
| Load-distance (load-m/day) | | | | |
| Travel hours/day (modeled) | | | | |
| One-time cost | | | | |
| Downtime (days) | | | | |
| Flexibility | | | | |
| Safety review needed | | | | |

## Stress test
## Recommendation   (savings, cost, payback, review items)
```

## Verification

- [ ] Distances are aisle-path, not straight-line.
- [ ] The from-to matrix source and period are stated; estimated cells are tagged.
- [ ] The load-distance score is recomputed for every option on the same basis.
- [ ] Every option respects the listed constraints.
- [ ] Savings are labelled modeled and converted with a stated travel speed.
- [ ] Stress-test result reported.
- [ ] Items requiring qualified review are listed, not decided.

## False-Positive Prevention

1. **Spaghetti as data.** One traced path dramatises; the from-to matrix quantifies.
   Do not size savings from a single spaghetti trace.
2. **Straight-line distance.** Forklifts follow aisles; Euclidean distance can
   understate travel by 30% or more.
3. **Counting trips not loads.** A trip carrying one pallet and a trip carrying
   one box are not equal flows; agree the unit load.
4. **Optimising for one product.** A layout perfect for the top family can double
   travel for the rest. Score the whole mix.
5. **Travel savings as headcount.** Saved minutes are spread across people; only
   claim labour savings that can actually be redeployed.
6. **Ignoring the move.** Downtime, racking relocation, and re-permitting can exceed
   a year of travel savings. Show payback.
7. **Layout as a code decision.** Egress widths, sprinkler coverage, racking
   anchorage, and floor loading are decided by qualified engineers and the authority
   having jurisdiction.

## Example Output

```
# Layout analysis — Fabrication shop, Building 2   Data: routings × Q3 volumes, measured

## Current-state spaghetti (bracket family)
Path per unit batch: 410 m; 4 crossings of the main aisle; backtrack Weld → Saw.

## From-to matrix (pallet loads/day; distance = aisle path, m)
| Pair             | Loads/day | Distance | Load × distance |
| Receiving → Saw  | 30        | 60       | 1,800           |
| Saw → Press      | 28        | 85       | 2,380           |
| Press → Weld     | 26        | 95       | 2,470           |
| Weld → Paint     | 24        | 40       | 960             |
| Paint → Ship     | 24        | 70       | 1,680           |
| Saw → Weld       | 6         | 110      | 660             |
| Other 14 pairs   | 22        | —        | 1,450           |
Current score: 11,400 load-m/day

## Adjacency chart (excerpt)
| Saw–Press   | A | 28 loads/day |
| Press–Weld  | A | 26 loads/day |
| Weld–Paint  | X | sparks/solvent separation — fire protection review required |

## Constraints
Paint booth fixed (ventilation, permitted); press on reinforced pad; dock doors on east wall.

## Options
| Criterion                  | Current | 1 Move press | 2 Saw-Press-Weld line | 3 Ideal (new pad) |
| Load-distance              | 11,400  | 8,900        | 6,700                 | 5,900             |
| Travel h/day (1.5 m/s fork, ×2 empty return) | 4.2 | 3.3 | 2.5          | 2.2               |
| One-time cost              | —       | $95,000 (new pad) | $38,000          | $160,000          |
| Downtime                   | —       | 6 days       | 3 days                | 10 days           |
| Safety review              | —       | structural   | racking, egress       | structural, egress|
Option 2 moves saw and weld beside the press (pad stays); Weld–Paint stays 40 m apart.

## Stress test
Bracket volume +30%: Option 2 still best (8,200 vs 10,600 for Option 1).

## Recommendation
Option 2. Modeled travel saving 1.7 h/day ≈ 425 h/yr ≈ $25,500 at $60/h fork+driver.
Payback ≈ 1.5 years on $38,000. Before work starts: racking relocation and egress
path reviewed by the facilities engineer; fire protection reviews weld screen.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — the from-to matrix, load × distance score, travel hours, payback.
- **RT-02 Multi-Dimensional Analysis Framework** — flow, cost, downtime, flexibility, and safety scored separately.
- **CM-02 Constraint Specification** — monuments, separation, and egress fixed before options are drawn.
- **QA-02 Adversarial Stress-Test** — re-scoring under a shifted product mix.

## Related Prompts

- `ops_process_map_and_waste_scan.md` — the value stream whose transport waste this quantifies.
- `ops_capacity_and_bottleneck_model.md` — capacity of the steps the layout connects.
- `ops_standard_work_and_kaizen_event.md` — re-layout inside one cell or workstation.
