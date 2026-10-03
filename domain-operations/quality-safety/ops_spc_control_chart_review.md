---
title: "SPC Control Chart Review — Chart Selection, Control Limits vs. Specification Limits, Western Electric and Nelson Rules, and Capability Caveats"
category: operations/quality-safety
description: "Review or set up a statistical process control chart: choose the chart from the data type and subgrouping, compute control limits from the process rather than the spec, read signals with a stated rule set and its false-alarm cost, and report Cp/Cpk only when the process is stable, the data are adequate, and the measurement system has been checked."
techniques:
  - DS-01
  - NE-11
  - QA-12
  - QA-18
difficulty: advanced
tags:
  - spc
  - control-chart
  - process-capability
  - cpk
  - western-electric-rules
  - variation
  - is-this-process-in-control
  - which-control-chart
  - out-of-spec-parts
updated: "2026-10-02"
related_prompts:
  - domain-operations/process-improvement/ops_dmaic_project_charter.md
  - domain-operations/process-improvement/ops_root_cause_a3_report.md
  - domain-operations/quality-safety/ops_oee_loss_analysis.md
---

# SPC Control Chart Review

**Objective:** Decide whether a process is stable and capable — the right chart for
the data, limits computed from the process, signals read with a declared rule set,
and capability indices reported only with the conditions that make them meaningful.

**When to Use:**
- You have measurements from a process and someone asks "is it in control?"
- An existing chart has limits nobody can explain, or uses spec limits as control limits.
- A customer asks for Cpk and you want to know whether the number will mean anything.
- Operators are adjusting the process after every reading (tampering).
- **Not this prompt if** you are scoping an improvement project — use
  `domain-operations/process-improvement/ops_dmaic_project_charter.md` (this prompt
  feeds its Measure and Control phases). If a signal has already been found and you
  need the cause, use `ops_root_cause_a3_report.md`. For a business KPI that moved
  week to week (orders, churn), use
  `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md`.
  Research inference and designed experiments belong in `domain-science/statistics/`.

## Inputs / Context

1. **The characteristic**: what is measured, unit, specification (LSL/USL or one-sided),
   and target.
2. **Data**: in time order, with timestamps, subgroup identifiers, and any known
   events (tool change, new lot, shift). At least 20–25 subgroups or 25+ individuals
   before limits are trusted. Tag `measured`.
3. **Data type**: continuous (variables) or count/proportion (attributes); for
   attributes, the sample size per point.
4. **Sampling plan**: how subgroups are formed (consecutive parts, one per hour).
5. **Measurement system evidence**: gauge R&R or at least a repeatability check.
6. **Current chart and rules**, if reviewing an existing one.

## Method

1. **Select the chart (DS-01).**
   | Data | Subgroup | Chart |
   | Continuous | n = 1 | I-MR (individuals and moving range) |
   | Continuous | 2 ≤ n ≤ ~9 | X̄-R |
   | Continuous | n ≥ ~10 | X̄-S |
   | Defectives (pass/fail) | varying n | p chart (np if n constant) |
   | Defects per unit | varying area/units | u chart (c if constant) |
   Rare events (days between incidents) → a t or g chart, or I-MR on time between events.
2. **Compute control limits from the process (NE-11).**
   I-MR: `CL = x̄; UCL/LCL = x̄ ± 2.66 × MR̄`.
   X̄-R: `UCL/LCL = X̿ ± A2 × R̄` (A2 = 0.577 for n = 5); R chart `UCL = D4 × R̄`
   (D4 = 2.114 for n = 5). p chart: `p̄ ± 3√(p̄(1−p̄)/n)`.
   Use a baseline period with no known special causes; freeze limits; recalculate
   only after a deliberate, verified process change.
3. **Keep spec limits off the control chart.** Control limits are the voice of the
   process; spec limits are the voice of the customer. Compare them only in the
   capability step.
4. **Declare the rule set before reading (QA-12).** Western Electric: (1) one point
   beyond 3σ; (2) 2 of 3 beyond 2σ same side; (3) 4 of 5 beyond 1σ same side;
   (4) 8 in a row on one side of centre. Nelson adds trends (6 increasing), 14
   alternating, 15 within 1σ (stratification), 8 outside 1σ on both sides (mixture).
   Each added rule raises false alarms; with all four WE rules the false-alarm rate is
   roughly 1 in 90 points versus 1 in 370 for rule 1 alone. State the rules and the
   response to each.
5. **Read signals and their timing.** For each signal: the point(s), the rule, the
   coincident event, and the action. Common-cause variation gets no point-by-point
   reaction — that is tampering.
6. **Capability only if stable.** `Cp = (USL − LSL) / 6σ_within`;
   `Cpk = min(USL − μ, μ − LSL) / 3σ_within`, σ_within = R̄/d2 or MR̄/1.128.
   Report Ppk (overall σ) alongside. State the conditions: stable, ≥ 100 values,
   roughly normal or transformed, gauge R&R acceptable (commonly < 10% of tolerance;
   10–30% conditional). Give a confidence interval or at least the sample size.
7. **Domain smell tests (QA-18).** Limits suspiciously equal to specs; zero points
   near limits for months (limits too wide or data filtered); a chart with only
   in-spec data (rejects removed); subgroups mixing machines or cavities.

## Output Format

```
# SPC review — [characteristic], [process]   Data: [period, n]

## Chart choice
Data type: [..]  Subgroup: [..]  Chart: [..]  Reason: [..]

## Control limits (baseline [period], frozen [date])
| Chart | CL | UCL | LCL |
Spec: LSL [..] USL [..] (shown only in capability section)

## Rule set and response
| Rule | Meaning | Response |
Expected false-alarm rate: [..]

## Signals
| Point / date | Rule | Coincident event | Action |

## Stability verdict
[stable | not stable — special causes: ..]

## Capability (only if stable)
Cp [..]  Cpk [..]  Ppk [..]  n [..]  Normality [..]  Gauge R&R [..]%
Interpretation and caveats: [..]

## Smell-test findings
```

## Verification

- [ ] Chart type matches data type and subgroup size.
- [ ] Limits are computed from process data with the correct constants, not from specs.
- [ ] Baseline period is named and excludes known special causes.
- [ ] Rule set is declared before signals are reported, with its false-alarm cost.
- [ ] Capability is reported only for a stable process, with n, σ basis, and gauge status.
- [ ] Cpk and Ppk are both shown when they differ materially.

## False-Positive Prevention

1. **Spec limits drawn as control limits.** A process can be in control and out of
   spec, or in spec and out of control.
2. **Cpk on an unstable process.** It predicts nothing; the next shift may look
   different. Fix stability first.
3. **Cpk from 30 parts.** The 95% interval on a Cpk of 1.33 at n = 30 is roughly
   0.96–1.70. Report n and the interval.
4. **Every rule switched on.** More rules mean more false alarms and alarm fatigue.
   Choose the rules that match the failure modes you care about.
5. **Recalculating limits every month.** Rolling limits absorb drift and hide it.
6. **Ignoring the gauge.** If gauge R&R consumes 40% of the tolerance, the chart is
   mostly measuring the gauge.
7. **Attribute charts with tiny n.** A p chart with n = 20 and p̄ = 1% has an LCL of
   zero and cannot show improvement.

## Example Output

```
# SPC review — Bore diameter Ø12.00 ±0.05 mm, CNC lathe 4   Data: 25 subgroups of 5, 1–19 Sep

## Chart choice
Continuous; 5 consecutive parts per hour → X̄-R.

## Control limits (baseline 1–12 Sep, 25 subgroups, frozen 13 Sep)
X̿ = 12.008   R̄ = 0.018
| X̄ | 12.008 | 12.008 + 0.577×0.018 = 12.0184 | 11.9976 |
| R  | 0.018  | 2.114×0.018 = 0.0381            | 0       |
The existing chart used 11.95/12.05 (the specs) as limits — replaced.

## Rule set and response
| WE1 beyond 3σ        | special cause likely   | stop, check tool, log  |
| WE4 8 on one side    | shift                  | check offset, material lot |
Rules 2–3 not used: operators already overloaded with checks; ~1 in 150 points false-alarm rate (vs ~1 in 90 with all four).

## Signals (13–19 Sep, monitored)
| 16 Sep 10:00–17:00 | WE4 (8 above CL) | insert changed 09:40 | offset −0.006 applied 17:10 |
| 18 Sep 14:00       | WE1 (12.021)     | coolant concentration low | topped up; next 5 in limits |

## Stability verdict
Baseline stable; two assignable causes since, both explained and corrected.

## Capability (baseline only; n = 125; gauge R&R 8% of tolerance; normal, AD p = 0.41)
σ_within = R̄/d2 = 0.018/2.326 = 0.00774
Cp = 0.10 / (6×0.00774) = 2.15
Cpk = min(12.05−12.008, 12.008−11.95)/(3×0.00774) = 0.042/0.0232 = 1.81
Ppk (overall σ 0.0091) = 1.54
Process is off-centre by +0.008; centring would move Cpk toward 2.15.
Caveat: 12 days of one material lot; re-verify after the next lot change.

## Smell-test findings
Previous chart showed no point outside limits for 9 months — because limits were the specs.
```

## Techniques Used

- **DS-01 Framework Application** — Shewhart chart selection and Western Electric/Nelson rule sets.
- **NE-11 Embedded Calculation Formulas** — limits with A2, D4, d2 constants and the capability indices.
- **QA-12 False Positives Identification** — the declared rule set and its false-alarm rate.
- **QA-18 Domain-Specific Smell Tests** — spec-as-limit, filtered data, mixed streams, gauge dominance.

## Related Prompts

- `domain-operations/process-improvement/ops_dmaic_project_charter.md` — the project this chart baselines and later controls.
- `domain-operations/process-improvement/ops_root_cause_a3_report.md` — finding the cause behind a signal.
- `ops_oee_loss_analysis.md` — where quality losses sit among equipment losses.
