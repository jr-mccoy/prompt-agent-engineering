---
title: "Agency Performance Measures — Outputs vs Outcomes, Operational Definitions, Baselines and Targets, Paired Measures, and Gaming Risks"
category: policy/public-administration
description: "Build a performance-measure set for a public agency or program: trace the logic model from inputs to end outcomes, sort candidate measures into how much, how well, and is anyone better off, write an operational definition and data source for each, set targets from baseline, trend and capacity rather than aspiration, pair every measure that can be gamed with a counter-measure, and separate what the measures can show from what only an evaluation can — distinct from designing a causal program evaluation (policy_program_evaluation_design) and from business KPI definition (analytics_metric_definition_spec)."
techniques:
  - DS-01
  - DS-02
  - QA-21
  - NE-11
difficulty: intermediate
tags:
  - performance-measurement
  - outcome-measures
  - results-based-accountability
  - public-sector-kpis
  - target-setting
  - metric-gaming
  - measure-agency-results
  - set-government-targets
  - show-program-is-working
updated: "2026-10-03"
reasoning:
  styles: [analytic, quantitative, adversarial, structural]
  stakes: high
  horizon: years
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: team
  output_format: [structured, matrix]
  user_role: [performance_analyst, program_manager, budget_analyst, oversight_staff]
  mode: [design, evaluate]
related_prompts:
  - domain-policy/policy_program_evaluation_design.md
  - domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md
  - domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md
---

# Agency Performance Measures

**Objective:** Give an agency a small set of measures that tell leaders, the
legislature and the public whether the program is doing what it is for — each one
defined tightly enough to be reproduced, targeted honestly, and protected against the
ways staff and contractors will predictably move the number without moving the result.

**Audience:** Performance and budget analysts, program managers, chief data
officers, and legislative or audit staff reviewing an agency's measures.

**When to Use:**
- A budget process, strategic plan or funder requires performance measures and
  targets.
- Existing measures count activity (calls answered, inspections done) and nobody
  can say whether anyone is better off.
- A measure improved sharply and you suspect the definition, not the program.
- **Not this prompt if** you need to know whether the program **caused** an outcome
  change — that needs a counterfactual: `domain-policy/policy_program_evaluation_design.md`.
  For a company's business metric spec use
  `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md`, and to
  decompose a single top-line metric into drivers
  `domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md`.

## Inputs / Context

1. **Mission and statutory purpose** of the program, and who it serves.
2. **Logic model** or a plain description of inputs, activities and intended
   results.
3. **Existing measures** and their definitions, data sources and history.
4. **Data systems**: what is recorded, by whom, with what lag and quality checks.
5. **Reporting requirements**: budget documents, strategic plans, funder or
   statutory measures (e.g. national performance frameworks) that must be included.
6. **Baseline data** for at least 2–3 years where available, by subgroup.

Tag every baseline `[data]` (system extract, audited), `[sampled (n=)]` or
`[estimate]`. A measure with no data source is listed as `[develop]`, not dropped
and not filled with a plausible number.

## Method

1. **Trace the logic model.** Inputs → activities → outputs → intermediate
   outcomes → end outcomes. A measure belongs to one link; know which.
2. **Sort candidates with Results-Based Accountability (DS-01).** *How much did we
   do?* (outputs), *How well did we do it?* (quality, timeliness, cost per unit), *Is
   anyone better off?* (outcomes). Keep 1–2 of each per program, not 30.
3. **Write operational definitions (DS-02).** Numerator, denominator, inclusions
   and exclusions, time window, data source, owner, frequency, and how missing or
   unknown values are counted. Unknowns counted as neither success nor failure are
   the commonest hidden lever.
4. **Set baselines and targets (NE-11).** Target = baseline + expected trend +
   modelled effect of new capacity, shown as arithmetic; state the target method
   (trend, benchmark, standard, or capacity). Aspirational targets go in a separate
   "goal" line, not the accountability target.
5. **Enumerate gaming risks (QA-21).** For each measure: cream-skimming (serving
   easier cases), reclassification (moving cases to a category that is not
   counted), threshold effects (clustering just inside a time limit), output
   substitution (doing the measured thing instead of the useful thing), and data
   quality drift. Pair each exposed measure with a counter-measure.
6. **Disaggregate.** Report key outcomes by the subgroups the program must serve
   equitably; a rising average can hide a widening gap.
7. **Say what the measures cannot show.** Outcome trends reflect the economy,
   demographics and other programs too. Attribution needs evaluation; say so on the
   dashboard.
8. **Set the review rhythm.** Who reviews monthly versus annually, and the rule for
   changing a definition (logged, with the series restated).

## Output Format

```
# Performance measures — [program]   Agency: [..]   Reporting to: [..]

## 1. Logic model (one line per link)
## 2. Measure set
| # | Measure | Type (how much / how well / better off) | Link | Baseline | Target | Target method |
## 3. Operational definitions
| # | Numerator | Denominator | Exclusions | Unknowns treated as | Source | Owner | Frequency |
## 4. Gaming risks and paired measures
| Measure | Risk | Paired counter-measure |
## 5. Disaggregation
## 6. What these measures cannot show
## 7. Review rhythm and definition-change rule
```

## Verification

- [ ] Every measure sits on one logic-model link and one RBA question.
- [ ] At least one "better off" measure exists per program.
- [ ] Each definition states how unknown or missing records are counted.
- [ ] Target arithmetic is shown and its method named.
- [ ] Every outcome measure exposed to gaming has a paired measure.
- [ ] Key outcomes are disaggregated by the populations served.
- [ ] Attribution limits are stated alongside the measures.

## False-Positive Prevention

1. **Output dressed as outcome.** "Clients enrolled" is how much was done, not
   whether anyone is better off.
2. **Improvement from definitions.** A jump the quarter a definition changed is the
   definition. Restate the series or annotate it.
3. **Unknowns quietly excluded.** Dropping "unknown" exits from the denominator
   raises a success rate without any client doing better.
4. **Targets set by aspiration.** A target the trend cannot reach becomes a
   reason to game, not a reason to improve.
5. **Outcome credited to the program.** A falling unemployment rate lifts
   job-placement rates everywhere; attribution needs a comparison.
6. **Too many measures.** Thirty measures are monitored by nobody; a few, well
   defined, are used.

## Example Output

```
# Performance measures — Homeless Services Division, Coastal County (illustrative)
Reporting to: county budget book and board; federal system measures also required [verify]

## 1. Logic model
Funding, 9 providers → outreach, shelter, rapid rehousing (RRH), case management →
households assessed, sheltered, housed → exits to permanent housing (PH) → stays housed.

## 2. Measure set
| 1 | Households served                       | How much  | Output       | 4,250  | — (tracked) | — |
| 2 | Median days homeless (entry → PH move-in) | How well | Intermediate | 148 d  | 130 d | Capacity |
| 3 | Exits to PH, % of exits                 | Better off | Outcome     | 38.0%  | 42%   | Trend + capacity |
| 4 | Returns to homelessness within 12 mo    | Better off | End outcome | 22%    | ≤ 20% | Trend |
| 5 | Exits with destination unknown          | How well (data) | —     | 19%    | ≤ 10% | Standard |

## 3. Definition — measure 3
Numerator: exits to rental with or without subsidy, owned, or permanent supportive
housing. Denominator: ALL exits in the year, including unknown destination (unknown
counts as not-PH). Source: HMIS [data]; owner: data manager; quarterly.

## Target arithmetic — measure 3
Baseline 612 PH exits / 1,610 exits = 38.0% [data]. Trend +1.0 pt/yr (3-yr) [data].
New RRH capacity: 120 households × 0.85 expected PH success [estimate] = 102 → if
exits hold at 1,610: (612 + 16 trend + 102) / 1,610 = 45.3% modelled; target set at
42% because 60% of new RRH starts after Q2.

## 4. Gaming risks
| 3 Exits to PH  | Cream-skimming low-need households       | % of entrants with high assessed need (hold ≥ 40%) |
| 3 Exits to PH  | Short leases that end at month 3          | Measure 4, returns within 12 months             |
| 2 Days homeless| Reset clock by re-entering as a new case  | De-duplicated client ID; time since first entry |
| 5 Unknown exits| Recoding unknown as "staying with family" | Quarterly file audit, 30 random exits            |

## 5. Disaggregation
Measure 3 by race/ethnicity, household type and age: families 51%, single adults
33%, youth 18–24 29% [data] → youth gap flagged for the board.

## 6. Cannot show
Whether the Division caused the change: rents rose 9% this year; PH exits fell in
neighbouring counties too. Attribution → evaluation of RRH expansion.
```

## Techniques Used

- **DS-01 Framework Application** — logic model and Results-Based Accountability's three questions to sort measures.
- **DS-02 Metric Specification** — numerator, denominator, exclusions and unknown-handling written before targets.
- **QA-21 Metric Gaming Vector Enumeration** — each exposed measure paired with a counter-measure.
- **NE-11 Embedded Calculation Formulas** — baseline, trend and capacity arithmetic behind each target.

## Related Prompts

- `domain-policy/policy_program_evaluation_design.md` — when the question is whether the program caused the outcome.
- `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` — the business-side metric specification.
- `domain-data-analytics/framing-and-metrics/analytics_kpi_tree_decomposition.md` — decomposing one top-line measure into its drivers.
