---
title: "Calibration Self-Audit — Score Past Predictions, Surface Calibration Patterns"
category: reasoning-craft/forecasting
description: "Score a log of past predictions: of forecasts you said were 70% likely, what fraction came true? Group by probability bin, compute resolution per bin, identify systematic over- or underconfidence, and identify domains where calibration is best vs worst. Output: calibration improvement plan."
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
  - calibration
  - brier
  - self-audit
  - improvement
updated: "2026-05-10"
reasoning:
  styles: [statistical, self-referential, calibration]
  stakes: variable
  horizon: weeks_to_years
  uncertainty: variable
  evidence_quality: rich
  domain_complexity: variable
  collaboration: solo
  output_format: calibration_curve_plus_plan
  user_role: [forecaster, analyst, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/forecasting/forecasting_brier_tracker_design.md
  - domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
  - domain-reasoning-craft/epistemic/epistemic_bias_specific_audit.md
---

# Calibration Self-Audit

**Objective:** Score the user's past predictions to surface calibration patterns. Of forecasts assigned 70% probability, what fraction resolved yes? Group by probability bin (0–10%, 10–20%, ..., 90–100%), compute resolution per bin, identify systematic over- or underconfidence, identify domains where calibration is best vs worst. Output a calibration-improvement plan: which biases the user has, what discipline to apply on the next forecast.

**When to use:**
- The user has a log of past forecasts with stated probabilities and resolved outcomes.
- Periodic (quarterly / annual) review of forecasting practice.
- Before high-stakes forecasts: knowing your calibration profile improves the new forecast.
- After a notable surprise: calibration audit can reveal the surprise was actually predictable.

**When NOT to use:**
- Fewer than ~30 resolved forecasts (calibration metrics are noisy at small N).
- Unresolved forecasts only (audit needs resolution).
- Forecasts without stated probabilities (use `forecasting_brier_tracker_design.md` to start logging).

**Audience:** Forecasters, analysts, individuals running personal calibration practice.

---

## Inputs / Context

1. **Log of past forecasts.** Each with: question, stated probability, reasoning, resolution date, actual outcome (yes/no), domain.
2. **N resolved forecasts.** ≥30 ideal, ≥15 acceptable for rough audit.
3. **Time window.** Recent N or all-time.

---

## Constraints

### Must
- Group by **probability bin** (0–10%, 10–20%, ..., 90–100%; or finer if N is large).
- Compute **resolution rate per bin**: % of forecasts in bin that resolved yes.
- Compute **calibration error per bin**: predicted probability minus actual resolution rate.
- Compute **overall Brier score** as a single number.
- Identify **systematic patterns**:
  - Overconfidence (forecasts too extreme): high-probability forecasts (80–90%) resolve less often than stated; low-probability forecasts resolve more often than stated.
  - Underconfidence (forecasts too timid toward 50%): high-probability forecasts resolve more often than stated; low-probability forecasts resolve less often than stated.
  - Domain-specific calibration: best vs worst domains.
  - Recency: improving or worsening over time.
- Output a **calibration improvement plan**: 2–3 disciplines to apply on next forecast based on identified patterns.

### Must Not
- Overinterpret with N < 15.
- Treat single-bin deviations as systematic.
- Compute Brier without explaining what it means in plain terms.
- Skip domain breakdown — calibration often varies wildly across domains.

---

## Instructions

### Step 1 — Catalog the log
Tabulate forecasts with question, probability, outcome, domain, date.

### Step 2 — Bin by probability
Group: 0–10%, 10–20%, ..., 90–100% (or coarser if N is small).

### Step 3 — Per-bin resolution
For each bin: N forecasts, count resolved yes, compute % yes.

### Step 4 — Calibration error per bin
(Bin midpoint is a shortcut; the mean stated probability within the bin is preferable when forecasts cluster at a bin edge.)

| Bin | N | % resolved yes | Predicted prob (mid-bin) | Calibration error |
|-----|---|----------------|--------------------------|-------------------|
| 70–80% | 12 | 50% | 75% | +25 pp (overconfident) |
| ... | | | | |

### Step 5 — Overall Brier
Brier = mean of (probability − outcome)² across all forecasts.
- 0.0 = perfect. 0.25 is the score of always forecasting 50%. The proper naive benchmark is forecasting the base rate b of your question set, which scores b(1−b); compare against that, not the fixed 0.25.
Report with one-line interpretation.

### Step 6 — Pattern identification
- Overall over/under-confidence pattern
- Domain best vs worst
- Recency (recent vs older subsets)

### Step 7 — Improvement plan
2–3 specific disciplines based on patterns:
- If overconfident at high probabilities: pre-mortem; require stronger evidence to assign 80%+
- If underconfident at low probabilities: events resolve even less often than your stated low probabilities — trust the analysis and be more willing to assign extreme low values (e.g., 5% instead of 15%)
- Domain weakness: more reference-class work in weak domains, or accept lower probabilities until domain knowledge improves
- General: log reasoning, not just numbers; review monthly

### Step 8 — Next-forecast checklist
A short checklist to apply on the next forecast based on this audit's findings.

---

## False-Positive Prevention

1. **Small-N overinterpretation.** Single bins with N=3 produce noisy resolution rates.
2. **Brier without context.** A Brier of 0.18 means nothing without comparison.
3. **Overconfidence diagnosis from one bin.** Pattern across bins is the signal.
4. **Domain-blind audit.** Aggregate calibration can hide domain-specific patterns.
5. **Plan without discipline.** "Be more humble" is not a plan.

---

## Output Format

```
# Calibration self-audit

## Log
- Time window: [...]
- Total forecasts: [N]
- Resolved: [N]
- Domains: [...]

## Per-bin calibration
| Bin | N | % resolved yes | Predicted (mid-bin) | Error (pp) | Pattern |
|-----|---|----------------|---------------------|------------|---------|
| 0–10% | [...] | [...] | 5% | [...] | [...] |
| 10–20% | [...] | [...] | 15% | [...] | [...] |
| ... | | | | | |

## Overall Brier
- Score: [...]
- Interpretation: [better than base-rate benchmark / similar / worse]

## Patterns
- Overall confidence: [overconfident / underconfident / well-calibrated]
- Best-calibrated domain: [...]
- Worst-calibrated domain: [...]
- Recency trend: [improving / stable / worsening]

## Improvement plan (2–3 disciplines)
1. [...]
2. [...]
3. [...]

## Next-forecast checklist
- [ ] [...]
- [ ] [...]
- [ ] [...]
```

---

## Verification

- [ ] N stated and large enough for inference (≥15 minimum).
- [ ] Per-bin breakdown with N, resolution, error.
- [ ] Brier with plain interpretation.
- [ ] Domain breakdown.
- [ ] Recency trend.
- [ ] Improvement plan with specific disciplines.
- [ ] Next-forecast checklist actionable.
