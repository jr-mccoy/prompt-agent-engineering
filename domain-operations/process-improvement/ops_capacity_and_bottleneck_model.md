---
title: "Capacity and Bottleneck Model — Constraint Identification, Effective Utilization, Little's Law, and a Queueing Sanity Check"
category: operations/process-improvement
description: "Model the capacity of a multi-step physical or service process: effective capacity per step after availability losses, utilization against average and peak demand, the one constraint that sets throughput, a Little's Law cross-check of WIP against lead time, and a queueing sanity check that explains why running the constraint near 100% makes lead times erratic."
techniques:
  - NE-11
  - DP-09
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - capacity-planning
  - bottleneck
  - theory-of-constraints
  - littles-law
  - utilization
  - queueing
updated: "2026-09-24"
related_prompts:
  - domain-operations/process-improvement/ops_process_map_and_waste_scan.md
  - domain-operations/process-improvement/ops_dmaic_project_charter.md
  - domain-business-strategy/client-services/services_capacity_and_utilization_planner.md
---

# Capacity and Bottleneck Model

**Objective:** Identify the single step that limits a process's throughput, quantify
how close it runs to its effective capacity at average and peak demand, cross-check
the data with Little's Law, and name the change that raises throughput — including
where the constraint moves next.

**When to Use:**
- Output is short of demand and every step claims to be busy.
- Lead times swing wildly day to day even though volume looks stable.
- You are deciding where to add a person, a shift, or a machine.
- A peak (Mondays, month-end, seasonal) creates a backlog that takes days to clear.
- **Not this prompt if** you are planning billable consultant days in a services
  practice — use
  `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md`.
  If you have not yet mapped the process, start with `ops_process_map_and_waste_scan.md`.
  For software system throughput, use `domain-software-engineering/analysis/performance/`.

## Inputs / Context

1. **Steps in flow order**, with resources at each (people, machines, stations).
2. **Rate per resource** (units/hour) — from time study or output records, with source.
3. **Availability losses** per step: breaks, changeovers, material waits, downtime.
4. **Demand**: average rate and peak rate, on the same time unit.
5. **Observed WIP** (units in process at a moment) and **observed lead time** (from
   timestamps), if available.
6. **Mix**: if units differ in work content, the rates per type or a weighted average.

## Method

1. **Normalize units (DS-02).** One unit of flow (order, case, patient visit), one
   time base (per hour of operating time). Convert everything before comparing.
2. **Compute effective capacity per step (NE-11).**
   `Effective capacity = resources × rate per resource × availability`.
   Nominal capacity is what the machine or person can do; effective is what the step
   delivers after the losses it actually suffers.
3. **Compute utilization.** `ρ = demand rate ÷ effective capacity` at average and at
   peak demand. Any ρ > 1 means the backlog grows by `(demand − capacity)` per hour.
4. **Name the constraint (DP-09).** The step with the highest ρ. There is one; if two
   are within a few points, name both and state which the data cannot distinguish.
   Confirm on the floor: the constraint has WIP piled in front of it and starved
   steps after it.
5. **Cross-check with Little's Law.** `WIP = throughput × lead time`. Compute the
   implied lead time from observed WIP and throughput and compare with measured
   lead time. A large mismatch means one of the three numbers is wrong — find which
   before modeling further.
6. **Queueing sanity check.** Waiting grows with `ρ ÷ (1 − ρ)` and with variability
   in arrivals and service. At ρ = 0.80 the factor is 4; at 0.90 it is 9; at 0.98 it is
   49. Use this to explain erratic lead times, not to predict them precisely.
7. **Options and where the constraint moves (QA-02).** For each option (raise
   availability, add resource, offload work, level demand), recompute ρ at every step.
   Show the new constraint; a fix that only moves the bottleneck one step is still a
   fix, but say so.

## Output Format

```
# Capacity model — [process]      Unit: [..]   Time base: [per operating hour]

## Step capacity
| Step | Resources | Rate/resource | Availability | Effective cap. | Source |

## Utilization
| Step | ρ at avg demand [..] | ρ at peak [..] | Backlog growth at peak |

## Constraint
[step] — ρ avg [..], peak [..]. Floor evidence: [...]

## Little's Law check
WIP [..] ÷ throughput [..] = implied lead time [..] vs measured [..] → [consistent | investigate]

## Queueing note
ρ/(1−ρ) at the constraint: [..] — [what it implies for lead-time stability]

## Options
| Option | New ρ by step | New constraint | Cost / effort | Confidence |

## Recommendation and what to measure after
```

## Verification

- [ ] All rates use one unit and one time base.
- [ ] Effective capacity includes availability losses with a source.
- [ ] Utilization is shown at both average and peak demand.
- [ ] Exactly one constraint is named (or a stated tie).
- [ ] Little's Law check is done, or the missing input is named.
- [ ] Each option recomputes utilization at every step and names the new constraint.

## False-Positive Prevention

1. **Nominal capacity as reality.** A station rated 30/hour that loses 15% to supply
   runs is a 25.5/hour station. Model effective capacity.
2. **Busiest people = bottleneck.** Non-constraint steps can look busy because they
   overproduce into queues. The constraint is found by utilization and by where WIP
   piles up, not by who looks stressed.
3. **Targeting 100% utilization.** Near ρ = 1 small variability produces large
   queues. A constraint planned at 98% will have unstable lead times; plan it at the
   level the queueing note supports.
4. **Averages across a peak.** A process at 70% average utilization can be at 130%
   every Monday. Model the peak separately.
5. **Little's Law with mismatched boundaries.** WIP, throughput, and lead time must
   cover the same start and end points and the same period; otherwise the check
   proves nothing.
6. **Improving a non-constraint.** An hour saved at a non-bottleneck step is a
   mirage for throughput; it may still reduce lead time or cost, but say which.
7. **Precise queue predictions from rough data.** The ρ/(1−ρ) factor is directional.
   Detailed wait-time predictions need measured variability or a simulation.

## Example Output

```
# Capacity model — E-commerce fulfilment, pick→pack→ship   Unit: order   Base: per op. hour

## Step capacity
| Pick       | 2 pickers | 55/h | 90% | 99.0 | WMS output, 4 wks |
| Pack       | 3 packers | 28/h | 85% | 71.4 | time study n=120; supply runs ~15% |
| Label/ship | 1 station | 110/h| 90% | 99.0 | WMS                |

## Utilization   (avg 70/h = 560 orders / 8 h; Monday peak 95/h)
| Pick       | 71% | 96%  | —              |
| Pack       | 98% | 133% | +23.6 orders/h |
| Label/ship | 71% | 96%  | —              |

## Constraint
Pack — ρ 0.98 avg, 1.33 Monday. Floor: 120–200 orders staged before pack mid-shift;
label/ship idle 20+ min/hour. Monday backlog ≈ 23.6 × 8 ≈ 189 orders into Tuesday.

## Little's Law check
WIP 290 ÷ 70/h = 4.1 h implied vs 4.3 h measured (timestamp mean) → consistent.

## Queueing note
ρ/(1−ρ) at pack = 49 on normal days — explains lead-time swings of 2–7 h with flat volume.

## Options
| Pre-stage supplies (availability 85→92%) | Pack 77.3 → ρ 0.91 avg, 1.23 Mon | Pack | low | Med |
| + 4th packer Mondays (with pre-stage)     | Pack 103 → ρ 0.92 Mon; Pick 0.96 Mon | Pick (Mon) | 1 temp/wk | Med |
| Cross-train ship operator to pack 2 h/day | small; ship has slack  | Pack | low | Low — measure |

## Recommendation and what to measure after
Pre-stage supplies now; add a Monday packer. Expect Monday constraint to move to
pick (0.96) — watch staged WIP before pack and before pick for 4 weeks. Figures after
change are modeled, not measured.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — effective capacity, ρ, Little's Law, ρ/(1−ρ).
- **DP-09 Single Primary Constraint Identification** — one named constraint, confirmed on the floor.
- **DS-02 Metric Specification** — normalized unit and time base.
- **QA-02 Adversarial Stress-Test** — each option recomputed to find where the constraint moves.

## Related Prompts

- `ops_process_map_and_waste_scan.md` — map before modeling.
- `ops_dmaic_project_charter.md` — when throughput needs a formal project.
- `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` — billable-day capacity for services firms.
