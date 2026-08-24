---
title: "Bayesian Belief Update — Transparent Prior-to-Posterior Reasoning"
category: reasoning-craft/reasoning-moves
description: "Take a stated prior belief and a piece of new evidence, then walk transparently from prior probability through likelihood ratio to posterior probability. Force the reasoner to name the prior, score the evidence's diagnostic strength, and end with an explicit posterior plus the next evidence that would move the belief further."
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
  - bayesian
  - probability
  - belief-update
  - calibration
updated: "2026-05-10"
reasoning:
  styles: [bayesian, probabilistic]
  stakes: variable
  horizon: variable
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: single_domain
  collaboration: solo
  output_format: structured_table
  user_role: [analyst, researcher, forecaster, strategist]
  mode: [audit, synthesize]
related_prompts:
  - domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
  - domain-reasoning-craft/reasoning-moves/reasoning_reference_class_forecast.md
---

# Bayesian Belief Update

**Objective:** Walk a belief from prior to posterior in one transparent step. Take a claim, the user's stated prior probability, and a piece of new evidence. Estimate the likelihood ratio (how much more likely the evidence is under the claim than under its negation), compute or reason to the posterior, and end with an explicit "next-evidence" pointer that would meaningfully move the belief further.

**When to use:**
- The user has a belief and just encountered new information that should update it (or shouldn't).
- A research finding, news event, expert opinion, or data point has shifted the conversation and the user wants the update made explicit.
- The user is tracking a forecast and wants disciplined evidence integration rather than gut adjustment.

**When NOT to use:**
- The claim cannot be reasonably operationalized as a probability of a single proposition. Reframe first.
- The user has no prior at all. Run a base-rate or reference-class step before this prompt.
- The new "evidence" is itself the same claim restated by a different source. Surface that and stop.

**Audience:** Analysts, researchers, forecasters, strategists, anyone who wants their belief updates auditable rather than vibes-based.

---

## Inputs / Context

1. **The claim.** A single proposition that can be either true or false (e.g., "This product will hit $1M ARR in 12 months").
2. **The prior probability.** A number between 0.01 and 0.99 reflecting belief before seeing this evidence. If the user gives a range, take the midpoint and flag the range width.
3. **The new evidence.** One specific item of evidence — a study, a data point, an observation, a source statement. Multiple items should be processed sequentially, not bundled.
4. **Source quality and independence.** Where the evidence comes from and whether it is independent of the sources that produced the prior.
5. **Stakes.** Optional but useful — high-stakes updates deserve a sensitivity check at the end.

---

## Constraints

### Must
- Restate the claim, the prior, and the evidence verbatim before reasoning.
- Estimate two likelihoods explicitly: P(evidence | claim true) and P(evidence | claim false). Express each as a rough fraction or percent with a one-sentence justification.
- Compute the likelihood ratio = P(E|H) / P(E|¬H). Show the arithmetic.
- Produce a posterior probability using either Bayes' rule (`posterior_odds = prior_odds × LR`) or a reasoned approximation. Show the conversion.
- Name the **direction** of the update (toward / away from the claim) and the **magnitude** (negligible / modest / large / decisive).
- End with one piece of next evidence that would, if observed, meaningfully move the posterior further in either direction.

### Must Not
- Pretend numerical precision the inputs don't support. Round to one significant figure and say so.
- Skip the likelihood-under-negation step. The most common Bayesian failure is updating only on P(E|H).
- Treat correlated evidence as independent. If the new evidence shares sources with the prior, the LR shrinks toward 1; flag this.
- Move the posterior past 0.99 or below 0.01 without naming what would have to be true to get there.
- Smuggle in the user's preferred conclusion. The math should be done before the verdict is read.

---

## Instructions

### Step 1 — Restate
Write the claim, the prior `P(H)`, and the evidence `E` verbatim. If the prior was a range, take the midpoint and note the width.

### Step 2 — Likelihood under the claim
Estimate `P(E | H)`: if the claim is true, how surprising is this evidence? Justify in one sentence.

### Step 3 — Likelihood under the negation
Estimate `P(E | ¬H)`: if the claim is false, how surprising is this evidence? Justify in one sentence. This is the step most reasoners skip; do it explicitly.

### Step 4 — Likelihood ratio
`LR = P(E|H) / P(E|¬H)`. Compute it. An LR near 1 means the evidence is non-diagnostic; LR > 10 is strong; LR > 100 is decisive; LR < 0.1 strongly disconfirms.

### Step 5 — Posterior
Convert the prior to odds: `prior_odds = P(H) / (1 − P(H))`. Multiply by LR to get posterior odds. Convert back to a probability: `posterior = posterior_odds / (1 + posterior_odds)`. Show the arithmetic.

### Step 6 — Independence and source-correlation check
Was this evidence already partially baked into the prior (same source, same dataset, same upstream argument)? If yes, shrink the LR toward 1 by a stated factor and recompute.

### Step 7 — Direction and magnitude
State the direction (up / down / unchanged) and magnitude (negligible / modest / large / decisive) of the update.

### Step 8 — Next-evidence pointer
Name one piece of evidence that, if observed, would move the posterior meaningfully (e.g., "A randomized trial of N>500 with effect size > 0.3 would push the posterior above 0.85").

### Step 9 — Sensitivity (optional, for high stakes)
Recompute with the LR estimate doubled and halved. Report the posterior range. If the qualitative verdict changes inside that range, the update is fragile — flag it.

---

## False-Positive Prevention

1. **Likelihood-of-evidence fallacy.** "This evidence is likely if the claim is true" is not enough. The evidence must be *more* likely under the claim than under its negation. Always estimate both.
2. **Strong-evidence inflation.** Reasoners over-weight vivid evidence (a personal anecdote, a single dramatic study). Cap LR estimates from single sources at ~10 unless the methodology is unusually clean.
3. **Correlated evidence double-counting.** Three op-eds citing the same paper are one piece of evidence, not three. Apply the source-correlation check.
4. **Anchoring on the prior.** Sometimes the prior is wrong, not the evidence. If the LR is large and consistently pointed in one direction across multiple updates, the issue may be a mis-specified prior. Flag this if the posterior crosses 0.5.
5. **Numerical false precision.** A prior of 0.62 is rarely meaningful. Round to nearest 0.05 unless the user has a calibrated probability.
6. **Motivated stopping.** Don't stop updating because the answer matches the user's gut. Run the full pipeline.

---

## Output Format

```
# Bayesian update

**Claim:** [verbatim]
**Prior P(H):** [value, with range width if any]
**Evidence E:** [verbatim, with source]

## Likelihoods
- P(E | H)  = [value] — [reason]
- P(E | ¬H) = [value] — [reason]
- **Likelihood ratio (LR):** [P(E|H) / P(E|¬H)] = [value]

## Posterior
- prior_odds  = [P(H) / (1 − P(H))]
- posterior_odds = prior_odds × LR = [value]
- **Posterior P(H | E):** [value]

## Independence check
- Source overlap with prior: [none / partial / heavy]
- Adjusted LR (if needed): [value] → adjusted posterior: [value]

## Verdict
- Direction: [up / down / unchanged]
- Magnitude: [negligible / modest / large / decisive]
- One-line summary: [posterior moved from X to Y because the evidence was [moderately/strongly/weakly] more consistent with the claim than its negation]

## Next evidence that would move the belief
- [Specific observable that, if seen, would push posterior above [value] or below [value]]

## Sensitivity (if high-stakes)
- LR doubled  → posterior = [value]
- LR halved   → posterior = [value]
- Verdict robust? [yes / fragile]
```

---

## Verification

- [ ] Claim, prior, and evidence are restated verbatim.
- [ ] Both `P(E|H)` and `P(E|¬H)` are estimated with one-sentence justifications.
- [ ] Likelihood ratio is computed and shown.
- [ ] Posterior is computed via odds form, with arithmetic visible.
- [ ] Source-correlation check is performed and any adjustment is shown.
- [ ] Direction and magnitude are explicit.
- [ ] One specific next-evidence pointer is named.
- [ ] Numerical precision matches input precision (no false decimals).
- [ ] No conclusion was written before the math was done.
