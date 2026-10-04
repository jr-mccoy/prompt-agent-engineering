---
title: "OEE Loss Analysis — Availability, Performance, Quality, the Six Big Losses, and the Data-Honesty Traps"
category: operations/quality-safety
description: "Compute overall equipment effectiveness for one machine or line from planned time, run time, ideal cycle time, and good count; convert it into a time-loss waterfall across the six big losses so the largest recoverable loss is named in hours; and audit the inputs for the definitional choices that make OEE look better without the equipment getting better."
techniques:
  - NE-11
  - DS-02
  - QA-21
  - DP-06
difficulty: intermediate
tags:
  - oee
  - six-big-losses
  - availability
  - performance-rate
  - downtime-analysis
  - tpm
  - machine-keeps-stopping
  - why-is-output-low
  - equipment-efficiency
updated: "2026-10-02"
related_prompts:
  - domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md
  - domain-operations/quality-safety/ops_spc_control_chart_review.md
  - domain-operations/process-improvement/ops_root_cause_a3_report.md
---

# OEE Loss Analysis

**Objective:** Turn equipment data into a defensible OEE with its three factors, a
waterfall of lost hours by the six big losses, and the single largest recoverable
loss — with every definition stated so the number can be compared over time and is
not quietly inflated.

**When to Use:**
- A machine or line is "running" but output is well below its nameplate rate.
- Leadership quotes an OEE figure and you want to know what it is hiding.
- You are choosing where to start a TPM, SMED, or reliability effort.
- Two plants report OEE and the numbers are not comparable.
- **Not this prompt if** you need to know which step limits the whole process and how
  queues behave — use
  `domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md` (OEE
  is about one asset; first confirm it is the constraint). If the quality loss is a
  variation problem, chart it with `ops_spc_control_chart_review.md`. Once the
  largest loss is named, find its cause with
  `domain-operations/process-improvement/ops_root_cause_a3_report.md`.

## Inputs / Context

1. **Period and asset**: one machine or line, at least 2–4 weeks.
2. **Time**: calendar time, planned shutdowns (no orders, holidays, planned
   maintenance), and the source of each.
3. **Stops**: each stop with start, duration, and reason code; how short stops are
   captured (automatic sensor vs. operator entry). Tag `measured` or `estimated`.
4. **Ideal cycle time** per product (the design or demonstrated best sustained rate)
   and its source.
5. **Counts**: total count, good count first time, rework, scrap, startup rejects.
6. **Changeovers**: number and duration.

## Method

1. **Fix definitions (DS-02).** Write down: what counts as planned downtime; whether
   changeovers are availability loss (standard) or excluded; the minimum stop
   duration logged as downtime vs. a minor stop (commonly 2–5 min); the ideal cycle
   time source; whether rework counts as good (it should not).
2. **Compute (NE-11).**
   `Planned production time = calendar − planned shutdown`
   `Run time = planned production time − stop time`
   `Availability = run time / planned production time`
   `Performance = (ideal cycle time × total count) / run time`
   `Quality = good count / total count`
   `OEE = A × P × Q = (ideal cycle time × good count) / planned production time`
   Cross-check: the two OEE forms must agree.
3. **Six big losses waterfall.** Convert each into hours:
   - Availability: (1) breakdowns, (2) setup and adjustment (changeovers).
   - Performance: (3) minor stops and idling, (4) reduced speed.
   - Quality: (5) process defects (scrap, rework), (6) startup/reduced yield.
   Performance loss hours = run time − ideal cycle time × total count; split minor
   stops (from sensor data) from speed loss (the remainder).
   Quality loss hours = ideal cycle time × (total − good).
4. **Name the dominant loss (DP-06)** in hours per week and in units, and the next
   two. Stratify the dominant loss by reason code, product, and shift.
5. **Audit the data for gaming and drift (QA-21).** Check each trap in the
   False-Positive section and report which apply and their effect on the number.
6. **Translate to a target.** State the recoverable hours if the dominant loss were
   halved, as modeled capacity — not as achieved.

## Output Format

```
# OEE — [asset]   Period: [..]   Data source: [..]

## Definitions
Planned shutdown includes: [..]  Changeovers: [availability loss]  Minor-stop threshold: [..]
Ideal cycle time: [..] s (source: [..])  Rework counted as: [not good]

## Calculation
| Item | Value |
Availability [..]%  Performance [..]%  Quality [..]%  OEE [..]%
Cross-check (ICT × good / planned): [..]%

## Six big losses (hours in period)
| Loss | Hours | % of planned | Top reason codes |

## Dominant loss and stratification
## Data-honesty audit
| Trap | Applies? | Effect on OEE |
## Modeled recovery
```

## Verification

- [ ] Every definition is written before the calculation.
- [ ] A × P × Q equals ICT × good / planned time within rounding.
- [ ] The six losses plus valuable operating time sum to planned production time.
- [ ] Performance never exceeds 100%; if it does, the ideal cycle time is wrong.
- [ ] Good count excludes rework.
- [ ] Recovery is labelled modeled.

## False-Positive Prevention

1. **Generous ideal cycle time.** Using a slowed "standard" rate instead of the
   design or best demonstrated rate hides speed loss. Performance >100% is the tell.
2. **Changeovers as planned downtime.** Moving setups out of planned time inflates
   availability and removes the SMED opportunity from view.
3. **Unlogged minor stops.** Operator-entered stops under 5 minutes are usually
   missing; they reappear as "speed loss". Use sensor data or a sampled study.
4. **Rework counted as good.** Quality looks perfect while capacity goes to
   reprocessing.
5. **"No orders" removed silently.** Excluding idle time is legitimate in OEE but
   must be shown; TEEP (OEE × loading) reveals it.
6. **Averaging OEE across machines.** Average of ratios misweights; compute from
   summed times and counts, and never compare a bottleneck's OEE with a non-bottleneck's.
7. **85% "world class" as a target.** Benchmarks vary by industry and asset;
   trend against yourself with fixed definitions.

## Example Output

```
# OEE — Bottling line 3 filler (the line constraint)   Period: 4 weeks, 5 days × 2 shifts
Data: MES stop log (sensor, measured), counts from filler and case checker.

## Definitions
Planned shutdown: weekends, 30 min/shift breaks (crew leaves line). Changeovers = availability loss.
Minor stop: < 3 min (sensor-captured). Ideal cycle time: 0.15 s/bottle (400/min nameplate,
demonstrated 2025 trials). Rework not counted as good.

## Calculation
Planned production time: 20 days × 2 × (480 − 30) min = 18,000 min = 300.0 h
Stops ≥ 3 min: breakdowns 31.0 h + changeovers 27.0 h = 58.0 h
Run time: 242.0 h   Availability = 242.0 / 300.0 = 80.7%
Total count: 4,560,000   ICT × total = 0.15 × 4,560,000 = 684,000 s = 190.0 h
Performance = 190.0 / 242.0 = 78.5%
Good count: 4,446,000   Quality = 4,446,000 / 4,560,000 = 97.5%
OEE = 0.807 × 0.785 × 0.975 = 61.8%
Cross-check: 0.15 × 4,446,000 = 666,900 s = 185.25 h / 300.0 = 61.8% ✓

## Six big losses (hours)
| Breakdowns            | 31.0 | 10.3% | capper jams 14.5, conveyor motor 9.0 |
| Setup / changeover    | 27.0 | 9.0%  | 18 changeovers, avg 90 min           |
| Minor stops           | 33.5 | 11.2% | bottle fallen at infeed (sensor, 1,340 stops) |
| Reduced speed         | 18.5 | 6.2%  | run at 360/min after capper jams     |
| Process defects       | 3.5  | 1.2%  | underfill 84,000                     |
| Startup rejects       | 1.25 | 0.4%  | 30,000 after changeovers             |
| Valuable operating    | 185.25 | 61.8% |                                    |
Sum: 300.0 h ✓

## Dominant loss
Minor stops: 33.5 h (≈ 804,000 bottles). 81% occur on 2 SKUs with lightweight 500 ml bottles.
Next: breakdowns (capper) and changeovers.

## Data-honesty audit
| ICT from nameplate, not a reduced standard | OK | — |
| Changeovers kept in availability           | OK | moving them out would show A = 242/273 = 88.6% |
| Breaks excluded with crew absent           | OK | shown |
| Rework (re-capped bottles)                 | Applies | 12,000 re-capped counted good → Q overstated 0.3 pt |

## Modeled recovery
Halving infeed minor stops: +16.75 h per 4 weeks → OEE ~67.3% (modeled; measure after change).
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas** — the A/P/Q chain, the cross-check, and loss hours.
- **DS-02 Metric Specification** — definitions fixed before any number is computed.
- **QA-21 Metric Gaming Vector Enumeration** — the data-honesty audit of ways OEE rises without improvement.
- **DP-06 Dominant Driver Identification** — one named loss in hours, stratified.

## Related Prompts

- `domain-operations/process-improvement/ops_capacity_and_bottleneck_model.md` — confirm the asset is the constraint first.
- `ops_spc_control_chart_review.md` — when the quality loss is a variation problem.
- `domain-operations/process-improvement/ops_root_cause_a3_report.md` — cause of the dominant loss.
