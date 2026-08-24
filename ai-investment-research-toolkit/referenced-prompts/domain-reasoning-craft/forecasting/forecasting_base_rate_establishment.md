---
title: "Base Rate Establishment — Anchor on History Before Anchoring on Case Features"
category: reasoning-craft/forecasting
description: "For a forecast about to be made, establish the historical base rate of the event class before incorporating case-specific information. Define the event class, sample comparable past cases, compute historical frequency, check stability/trend, and produce the base rate as a range. Lighter and faster than reasoning_reference_class_forecast.md; designed as a pre-step before case-specific reasoning."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - forecasting
  - base-rate
  - reference-class
  - calibration
  - inside-view
updated: "2026-05-10"
reasoning:
  styles: [base-rate, inductive, outside-view]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: base_rate_with_range
  user_role: [forecaster, analyst, pm, founder, individual]
  mode: [forecast, audit]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_reference_class_forecast.md
  - domain-reasoning-craft/reasoning-moves/reasoning_outside_view_inside_view.md
  - domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md
---

# Base Rate Establishment

**Objective:** Before applying case-specific reasoning to a forecast, establish the **historical base rate** of the event class. Define the event class crisply, sample 5+ comparable past cases, compute the historical frequency or distribution, check whether the rate is stable or trending, and produce the base rate as a range. Pre-step before any case-specific adjustment. Lighter than `reasoning_reference_class_forecast.md` (which is full reference-class forecasting); this prompt is for the quick "what's the base rate?" check.

**When to use:**
- Before any forecast that involves an event with prior comparable cases.
- When you catch yourself reasoning purely from case features without checking history.
- Pair with `reasoning_outside_view_inside_view.md` to formalize the outside view.

**When NOT to use:**
- Truly unprecedented events (no reference class).
- The base rate is well-known to all parties (skip to adjustment).
- Case features dominate so heavily that base rate is irrelevant (rare).
- You need case-specific adjustments to the base rate or an inside-view vs outside-view comparison — use `reasoning_reference_class_forecast.md`.

**Audience:** Anyone making forecasts.

---

## Inputs / Context

1. **The forecast question** (operationalized).
2. **What event is being predicted.**
3. **Available historical data or the user's recall of comparable cases.**

---

## Constraints

### Must
- Define the **event class** crisply (the set of cases comparable on relevant dimensions).
- Sample at least **5 prior cases** (or note when fewer; small-N base rates are noisy).
- Compute **historical frequency** (% of cases that resolved yes) OR **distribution** (median outcome with quartiles).
- Check **stability / trend**: is the rate stable over time, rising, falling? Recent base rate may differ from long-run.
- Output base rate as a **range**, not a point.
- End with: "Now apply case-specific adjustment from this base rate, not from scratch."

### Must Not
- Define the event class so narrowly that only one or two cases qualify.
- Define the event class so loosely that the base rate is meaningless.
- Use a point estimate when N is small.
- Skip the trend check.

---

## Instructions

### Step 1 — Forecast question
Restate.

### Step 2 — Event class definition
What features must a past case share to count as comparable? 3–5 inclusion criteria.

### Step 3 — Sample prior cases
List 5+ comparable past cases with their outcome on the forecast variable. (For yes/no questions: outcome = yes or no. For numeric: outcome = value.)

### Step 4 — Compute base rate
- Yes/no: % yes. Round to 5%.
- Numeric: median, P25, P75. Round.

### Step 5 — Trend / stability check
- Is the rate stable over the time window?
- Has it shifted recently? (Recent vs older subsets.)
- Implication for forecast: anchor on long-run, recent, or blend?

### Step 6 — Output base rate as range
- Best estimate: [X%]
- Plausible range: [X–Y%]
- N: [...]
- Caveats: [small-N / survivor bias / source quality]

### Step 7 — Hand-off
"Now apply case-specific adjustment, but start from this base rate, not from intuition."

---

## False-Positive Prevention

1. **Class-of-one trap.** Declaring "no comparable cases exist" to skip the lookup entirely — in a quick check, loosening one inclusion criterion usually yields a usable class.
2. **Class gerrymandering.** Tuning the 3–5 inclusion criteria until the handful of sampled cases supports the answer you wanted before the lookup.
3. **Survivorship in the sample.** A fast recall-based sample over-pulls memorable successes; failures are quieter. Ask which failed cases would qualify but aren't on the list.
4. **Recency-only.** Recent base rate may not be the right one if the underlying process hasn't changed.
5. **Long-run-only.** If something changed recently, long-run base rate is misleading.
6. **Point estimate from sparse data.** With N=5, report a range.

---

## Output Format

```
# Base rate — [forecast question]

## Forecast question
> [...]

## Event class
- Inclusion criteria:
  - [...]
  - [...]
  - [...]

## Prior cases
| # | Case | Outcome on forecast variable | Source |
|---|------|------------------------------|--------|
| 1 | [...] | [yes / no / value] | [...] |
| 2 | [...] | [...] | [...] |
| ... | | | |

## Base rate
- Best estimate: [X%] (or median X)
- Plausible range: [X–Y%] (or P25–P75)
- N: [...]
- Caveats: [...]

## Trend / stability
- Stable / rising / falling: [...]
- Recent (last K cases) vs long-run: [...]
- Implication: anchor on [long-run / recent / blend]

## Hand-off
- Apply case-specific adjustment from base rate of [X], not from intuition.
```

---

## Verification

- [ ] Event class defined with 3–5 criteria.
- [ ] At least 5 cases sampled (or smaller-N flagged).
- [ ] Base rate as range, not point.
- [ ] Trend checked.
- [ ] Caveats noted.
- [ ] Hand-off statement explicit.
