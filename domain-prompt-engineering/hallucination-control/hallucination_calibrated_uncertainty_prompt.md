---
title: "Calibrated Uncertainty — Emit Confidence with a Calibration Rubric"
category: prompt-engineering/hallucination-control
description: "Force the model to attach a confidence value to each claim using a fixed verbal-numeric rubric tied to evidence strength, with calibration test cases."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - PR-02
difficulty: advanced
tags:
  - hallucination
  - calibration
  - uncertainty
  - confidence
  - rubric
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/hallucination-control/hallucination_known_unknown_separator.md
  - domain-prompt-engineering/hallucination-control/hallucination_self_consistency_check.md
  - domain-prompt-engineering/hallucination-control/hallucination_premortem_for_factual_task.md
---

# Calibrated Uncertainty Prompt

**Objective:** Make the model emit a confidence value per claim using a fixed verbal-numeric rubric anchored to evidence types — and make those confidences calibratable (i.e., a 0.7-confidence claim is right ~70% of the time over the eval set).

**When to use:** Fact-rich generation where downstream consumers (humans or systems) act differently on high vs. low confidence. Calibrated values are required; uncalibrated "I'm pretty sure" is worse than no value.

---

## Inputs

1. `evidence_types_present` — subset of `[direct_quote, paraphrase, derived, parametric, none]`.
2. `confidence_scale` — `5_band` (very_low–very_high) or `decimal` (0.0–1.0 in 0.1 steps).
3. `calibration_set_path` — path to a labeled set used to verify calibration.
4. `forbid_parametric` — boolean; if true, parametric claims auto-receive confidence 0 and are dropped.

---

## Constraints

### Must
- Attach exactly one confidence value to each atomic claim.
- Map confidence to evidence type per the rubric below; never assign higher than the rubric allows.
- Compute `expected_calibration_error` (ECE) on the calibration set; report it.
- Use the same scale across the entire response.
- Provide one-sentence justification for any claim with confidence ≥ 0.8.

### Must Not
- Use vague hedges ("possibly", "maybe") in place of a numeric value.
- Boost confidence based on how confident the model "feels"; only the rubric.
- Average confidences across claims into a single response score.
- Hide low-confidence claims; they must appear with their value.
- Emit a confidence without naming the evidence type that supports it.

---

## Confidence Rubric

| Evidence type | Max confidence (decimal) | 5-band |
|---|---|---|
| `direct_quote` from supplied source | 0.95 | very_high |
| `paraphrase` of single source | 0.85 | high |
| `paraphrase` corroborated by ≥ 2 sources | 0.90 | high |
| `derived` (logical inference from sources) | 0.70 | medium |
| `parametric` (model knowledge, no source) | 0.40 if allowed; else 0.0 | low |
| `none` (guess) | 0.0 | very_low |

Cap, do not floor: a `direct_quote` from a contradictory or stale source can be lower.

---

## Instructions

1. Decompose response into atomic claims.
2. For each claim, label evidence type strictly.
3. Apply the rubric cap. Adjust down for any of: contradictory source, stale source, ambiguous referent, low retriever score.
4. If `forbid_parametric=true`, drop parametric claims; do not silently substitute.
5. Run the calibration check: bin claims by confidence (0.1 bins for decimal, 5 bins for 5_band); compare bin accuracy to bin midpoint; report ECE.

---

## Output Format

```json
{
  "scale": "5_band | decimal",
  "claims": [
    {
      "text": "<claim>",
      "evidence_type": "direct_quote | paraphrase | derived | parametric | none",
      "evidence_ids": ["..."],
      "confidence": <value>,
      "justification": "<sentence; required if confidence >= 0.8>"
    }
  ],
  "calibration_report": {
    "set": "<path>",
    "ece": <float>,
    "n_per_bin": {"0.0-0.1": <int>, "...": <int>}
  }
}
```

---

## Verification

- [ ] Every claim has both `evidence_type` and `confidence`.
- [ ] No confidence exceeds the rubric cap for its evidence type.
- [ ] No vague hedge words appear instead of a value.
- [ ] ECE computed and reported.
- [ ] Justifications present for all `confidence ≥ 0.8`.
- [ ] If `forbid_parametric=true`, no parametric claims remain.

---

## Anti-Patterns

1. Reporting "high confidence" without naming evidence — uncalibratable.
2. Calibrating once and never re-running — calibration drifts with model and corpus changes.
3. Truncating low-confidence claims for brevity — users lose the option to act differently.
4. Using a 7-point Likert scale with no rubric — produces noise, not signal.
