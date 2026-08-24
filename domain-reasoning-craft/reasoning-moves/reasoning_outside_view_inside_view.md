---
title: "Outside View vs Inside View — Force Both, Then Reconcile"
category: reasoning-craft/reasoning-moves
description: "Capture the inside view (case-specific reasoning about why this case will go well/poorly), then independently capture the outside view (what comparable cases actually did), then reconcile the gap. Diagnose: planning fallacy if inside is rosier, pessimism if inside is darker, calibrated if aligned. Output a blended estimate with named weights."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - reasoning
  - outside-view
  - inside-view
  - reconciliation
  - calibration
updated: "2026-05-10"
reasoning:
  styles: [meta-cognitive, dialectical, calibration]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: paired_views_plus_reconciliation
  user_role: [analyst, founder, pm, executive, individual]
  mode: [audit, forecast, synthesize]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_reference_class_forecast.md
  - domain-reasoning-craft/forecasting/forecasting_super_forecaster_decomposition.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
---

# Outside View vs Inside View

**Objective:** Force the user to articulate both the **inside view** (case-specific reasoning: why *this* case will go a particular way given its specifics) and the **outside view** (reference-class reasoning: what comparable cases actually did) — independently, then reconcile the gap. The discipline is meta-cognitive: most reasoners default to inside view, and the gap between inside and outside view is itself diagnostic. Distinct from `reasoning_reference_class_forecast.md`, which is built for forecasts with a computable statistical base rate; this prompt is for judgments where no computable base rate exists (qualitative reference classes, sparse analogies) or where the reconciliation / gap-diagnosis is itself the contested step.

**When to use:**
- Forecasts where the user has strong intuitions about the specific case.
- Project / launch / hire estimates where planning fallacy is endemic.
- Investment / strategic-bet decisions.
- Personal high-stakes decisions ("I'm different from the average person who tried this").
- Any time the inside view feels obvious — that's exactly when checking against outside view matters most.

**When NOT to use:**
- A computable statistical base rate exists for the forecast variable and the main work is deriving it — use `reasoning_reference_class_forecast.md` instead.
- Cases where no reference class can plausibly be constructed (genuinely radical novelty).
- Decisions where the reference class is well-established and inside-view detail genuinely overrides (rare).
- The user has already done both views deliberately.

**Audience:** Analysts, founders, PMs, executives, individuals making consequential predictions or decisions.

---

## Inputs / Context

1. **The forecast or judgment.** What's being predicted, with deadline if applicable.
2. **Inside-view material the user is drawing on.** Case features they think matter.
3. **Whether a reference class exists** for the question.
4. **Stakes.** Higher stakes warrant slower reconciliation.

---

## Constraints

### Must
- Capture **inside view first**, in detail, before any outside-view work. (Inside view is what's natively available; suppressing it is unrealistic.)
- Capture **outside view independently** — do not let the inside-view estimate influence the reference-class construction.
- Quantify both views as estimates with confidence ranges.
- Compute the **gap** explicitly.
- Diagnose:
  - **Aligned** → both views coincide; high confidence in estimate.
  - **Inside more optimistic / faster / cheaper than outside** → planning fallacy candidate.
  - **Inside more pessimistic** → either private bad-news information or undue pessimism; probe.
  - **Inside dramatically different in either direction** → either user has private info or inside view is anchoring on irrelevant features.
- Produce a **reconciled estimate** as a weighted blend with weights named explicitly.

### Must Not
- Reference or adjust toward the sealed inside-view number while constructing the reference class / outside view — the seal exists so the outside view is built blind to it.
- Default to averaging the two views; the right blend depends on the diagnosis.
- Let the user discount the outside view because "this case is different" without naming a *specific* feature that justifies the discount.
- Let the user discount the inside view because "outside view is more rigorous" — sometimes inside view captures private information.

---

## Instructions

### Step 1 — Inside view (sealed)
Capture in detail:
- User's estimate (range OK)
- Reasoning: case-specific features driving the estimate
- Confidence

Set this aside. Do not reference during outside-view step.

### Step 2 — Outside view (independent)
Build using `reasoning_reference_class_forecast.md` discipline (lighter version OK):
- Define reference class
- Sample 5+ comparable cases
- Compute outcome distribution (median, P25, P75 if data; rough range otherwise)
- Outside-view estimate = adjusted reference-class median

### Step 3 — Compare
| | Inside view | Outside view | Gap |
|-|-------------|---------------|-----|
| Central estimate | [...] | [...] | [direction, magnitude] |
| Range | [...] | [...] | |
| Confidence | [...] | [...] | |

### Step 4 — Diagnose
- **Aligned (gap < ~20%):** views agree; trust the estimate.
- **Inside << outside (planning fallacy):** the user is over-optimistic. Default toward outside view unless private info justifies the gap.
- **Inside >> outside (over-pessimism):** user is under-confident. Investigate for over-discounting.
- **Inside ~~ outside but qualitatively different:** values overlap but reasoning paths differ; investigate which view's logic actually fits the situation.

### Step 5 — Probe the gap
If the gap is large, ask:
- What specific feature of *this* case justifies departing from the outside view?
- Is that feature actually unusual within the reference class?
- Have past cases in the reference class also had unusual features that didn't actually move outcomes?

### Step 6 — Reconcile
Produce the reconciled estimate as a blend. Weights depend on diagnosis:
- Aligned: 50/50 doesn't matter much
- Planning fallacy candidate: 70–90% outside view, 10–30% inside (the more compelling the case-specific feature, the more inside view weight)
- Over-pessimism: 50–70% outside, 30–50% inside
- Genuine private information: weight inside view more, but justify

### Step 7 — Final estimate and uncertainty
Range with P50, P75, P90. Note which view dominates.

### Step 8 — Decision implication
What should the user do given the reconciled estimate vs what they were going to do based on inside view alone?

---

## False-Positive Prevention

1. **Anchoring contamination.** Referencing or adjusting toward the sealed inside-view number while constructing the reference class biases the outside view. Capture-and-seal first is correct; the seal only works if the outside view is then built blind to the sealed number.
2. **"This case is different" without specifics.** A general feeling of difference is not a justification.
3. **Symmetric averaging.** Averaging inside and outside views ignores the diagnosis. Weights should reflect direction and magnitude of gap.
4. **Outside-view dismissal by quality concerns.** "The reference class is noisy, so I'll trust my intuition." Sometimes correct, but most often this is rationalization.
5. **Inside-view dismissal in the name of rigor.** Inside view captures real local information; ignoring it sacrifices signal.
6. **Single-pass reconciliation.** Sometimes the outside-view construction itself reveals features that change the inside view. Iterate if the gap closes meaningfully on second pass.

---

## Output Format

```
# Outside view vs inside view — [forecast / judgment]

## Inside view (captured first, sealed)
- Estimate: [range]
- Confidence: [...]
- Case-specific reasoning: [bullet list]

## Outside view (built independently)
- Reference class: [definition]
- Sample (N): [...]
- Outcome distribution: median [...], P25 [...], P75 [...]
- Outside-view estimate: [range]

## Comparison
| | Inside | Outside | Gap |
|-|--------|---------|-----|
| Central | [...] | [...] | [...] |
| Range | [...] | [...] | |

## Diagnosis
- [Aligned / Planning fallacy / Over-pessimism / Qualitatively different]
- Reasoning: [...]

## Gap probe (if gap large)
- Specific feature justifying departure: [...]
- Is feature unusual in reference class? [yes / no / unclear]
- Past unusual features in class moved outcomes? [yes / no / unclear]

## Reconciliation
- Weights: inside [%], outside [%]
- Justification: [matched to diagnosis]

## Reconciled estimate
- P50: [...]
- P75: [...]
- P90: [...]
- Dominant view: [inside / outside / blended]

## Decision implication
- Original action (inside view): [...]
- Revised action (reconciled): [...]
- What changes: [...]
```

---

## Verification

- [ ] Inside view captured before outside-view work.
- [ ] Outside view built independently.
- [ ] Both views quantified with ranges.
- [ ] Gap explicit and diagnosed.
- [ ] If gap large, "this case is different" claim probed for specifics.
- [ ] Reconciliation weights matched to diagnosis, not defaulted to 50/50.
- [ ] Final estimate as range with P-values.
- [ ] Decision implication stated.
