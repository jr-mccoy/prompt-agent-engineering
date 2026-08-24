---
title: "Scenario Probability Assignment — Probabilities Across Mutually-Exclusive Scenarios"
category: reasoning-craft/forecasting
description: "Once a scenario set exists, assign probabilities to the enumerated scenarios plus a mandatory 5–10% 'other / unforeseen' reserve, together summing to 1.0; justify each via base rate or mechanism, identify the two most uncertain probabilities, stress-test by varying ±20%, and surface implications for which scenarios deserve preparation, monitoring, or can be ignored."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - forecasting
  - scenarios
  - probability
  - sensitivity
  - planning
updated: "2026-05-10"
reasoning:
  styles: [probabilistic, scenario, sensitivity]
  stakes: variable
  horizon: months_to_years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: scenario_probability_table
  user_role: [strategist, executive, founder, analyst, policy]
  mode: [forecast, plan]
related_prompts:
  - domain-decision-making/scenario_two_by_two_matrix.md
  - domain-decision-making/scenario_robustness_test.md
  - domain-reasoning-craft/forecasting/forecasting_super_forecaster_decomposition.md
---

# Scenario Probability Assignment

**Objective:** Once a scenario set exists (typically from `scenario_two_by_two_matrix.md`), assign probabilities to each scenario plus a mandatory 5–10% reserve for "other / unforeseen", together summing to 1.0. Each probability is justified via base rate or mechanism, the two most uncertain probabilities are flagged, sensitivity is tested by varying each ±20%, and the output translates probabilities into preparation / monitoring / ignore decisions.

**When to use:**
- After scenario construction; before resource-allocation decisions.
- Pressure-testing a strategy against probability-weighted scenarios.
- Communicating to leadership the relative likelihood of different futures.

**When NOT to use:**
- Scenario set is not mutually exclusive (fix that first).
- Scenarios are too radically uncertain to probability-rate (use posture-based reasoning from `forecasting_long_horizon_radical_uncertainty.md`).
- The user wants a single point forecast (different prompt).

**Audience:** Strategists, executives, founders, analysts, policy people.

---

## Inputs / Context

1. **Scenario set** (typically 2–6 scenarios from prior work).
2. **Time horizon.**
3. **Resources for preparation.** Affects how many scenarios deserve explicit prep.

---

## Constraints

### Must
- Enumerated scenario probabilities plus a **mandatory 5–10% "other / unforeseen" reserve** together sum to **1.0**.
- Each probability has a **base-rate or mechanism justification** (not bare assertion).
- Identify the **2 most uncertain** probabilities (where small input changes would meaningfully shift the assignment).
- **Sensitivity test**: vary each ±20% (relative, i.e., ×0.8 to ×1.2; or to plausible bounds) and show how downstream decisions change.
- Translate probabilities into **action posture** (the probability-band × impact grid must be exhaustive):
  - **Plan for** (>30% probability with high impact): explicit preparation
  - **Contingency-hedge** (<10% with high impact): cheap hedges plus a tripwire — low-probability/high-impact tails are the canonical reason scenario planning exists
  - **Monitor** (10–30% with high impact, OR >30% with low impact): leading indicators tracked
  - **Monitor (light)** (10–30% with low impact): occasional check, no dedicated resources
  - **Ignore** (<10% with low impact): no resource allocation

### Must Not
- Default-uniform probabilities (each scenario = 1/N) without justification.
- Pretend high precision; round to 5%.
- Skip "other / unforeseen" reserve. Scenarios are never exhaustive.
- Treat probability as decisive; impact × probability drives action.

---

## Instructions

### Step 1 — Restate scenarios
List the scenarios (with names from the source set).

### Step 2 — Assign probabilities
For each scenario:
- Probability (5% increments)
- Justification (base rate from comparable past situations, mechanism that pushes toward this scenario, expert / market consensus reference)

Sum check: enumerated scenarios plus the reserve (Step 3) should equal 1.0.

### Step 3 — Reserve "other / unforeseen"
Allocate 5–10% to scenarios not enumerated. Note what kinds of futures this reserve covers.

### Step 4 — Identify uncertain probabilities
Which 2 probabilities are most uncertain (where you'd accept a wide range)? These are the ones to revisit as new information arrives.

### Step 5 — Sensitivity test
For each scenario, vary probability by ±20% (relative, ×0.8 to ×1.2; or to plausible bounds), keeping others proportional. Does any decision change?

### Step 6 — Action posture per scenario
| Scenario | Probability | Impact | Posture | Resources |
|----------|-------------|--------|---------|-----------|
| ... | ... | ... | ... | ... |

### Step 7 — Implications
- Which scenarios deserve plans now?
- Which deserve monitoring (with named signposts)?
- Which can be ignored?
- What single piece of information would most update the probability assignment?

---

## False-Positive Prevention

1. **Uniform-default.** Without justification, equal probabilities mask ignorance.
2. **Sum-check skip.** Probabilities that don't sum to 1.0 (or near it) hide assumptions.
3. **No reserve.** Scenario sets are never exhaustive.
4. **Over-precision.** 23.7% is false precision.
5. **Probability-as-action.** Action depends on probability × impact, not probability alone.
6. **Sensitivity skip.** Small probability changes shouldn't flip decisions if the assignment is robust.

---

## Output Format

```
# Scenario probability assignment — [scenario set]

## Scenarios
| # | Scenario | Probability | Justification |
|---|----------|-------------|----------------|
| A | [...] | 35% | [base rate / mechanism] |
| B | [...] | 25% | [...] |
| C | [...] | 20% | [...] |
| D | [...] | 15% | [...] |
| Other | unforeseen | 5% | [kinds of futures covered] |

Sum: 100%

## Most uncertain probabilities
- Scenario [#]: probability could plausibly range [X–Y%]
- Scenario [#]: probability could plausibly range [X–Y%]

## Sensitivity test
| Scenario | Prob ±20% | Decision flips? |
|----------|-----------|------------------|
| A | [X% to Y%] | no |
| B | [X% to Y%] | yes — scenario B becomes plan-for instead of monitor |
| ... | | |

## Action posture
| Scenario | Probability | Impact | Posture | Resources |
|----------|-------------|--------|---------|-----------|
| A | 35% | high | plan-for | full preparation |
| B | 25% | medium | monitor | signposts tracked |
| C | 20% | high | monitor | signposts tracked |
| D | 15% | low | monitor (light) | occasional check |

## Implications
- Plans now: [scenarios]
- Monitoring with signposts: [scenarios + signposts]
- Ignored: [scenarios]
- Highest-leverage info that would update assignment: [...]
```

---

## Verification

- [ ] Enumerated scenarios plus the 5–10% reserve sum to 1.0.
- [ ] Each probability has base-rate or mechanism justification.
- [ ] "Other / unforeseen" reserve included.
- [ ] Most uncertain probabilities flagged.
- [ ] Sensitivity test performed for each scenario.
- [ ] Action posture matched to probability × impact.
- [ ] Highest-leverage info to update named.
- [ ] No uniform default.
- [ ] No false precision.
