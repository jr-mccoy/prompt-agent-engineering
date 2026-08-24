---
title: "Inter-Rater Agreement Protocol"
category: prompt-engineering/evaluation/rubrics
description: "Measure and improve agreement across human or LLM judges using kappa-based metrics, calibration sessions, disagreement diagnosis, and a documented remediation plan."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - RT-05
difficulty: advanced
tags:
  - inter_rater_agreement
  - kappa
  - judge_calibration
  - rubric_reliability
  - eval_infrastructure
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/rubrics/rubric_calibrated_anchors.md
  - domain-prompt-engineering/evaluation/rubrics/rubric_llm_judge_designer.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Design and run a complete inter-rater agreement (IRA) protocol: select the appropriate agreement metric, measure current agreement, diagnose sources of disagreement, and produce a calibration plan that raises agreement to the target threshold before the main eval campaign.

## When to Use

- Before launching an eval campaign with ≥2 human judges or ≥2 LLM judge calls
- After discovering inconsistent scores on the same output from different judges
- When onboarding new judges or changing the rubric
- When a dimension shows high variance and you suspect judge disagreement rather than real output variance

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `rubric_dimensions` | Yes | List of dimensions being scored, with scale type (ordinal 1–5 / binary / categorical) |
| `judge_type` | Yes | `human` / `llm` / `hybrid` |
| `judge_count` | Yes | Number of judges rating each output |
| `pilot_scores` | Optional | Scores from a pilot run (same outputs rated by all judges) — needed for measurement |
| `ira_target` | Optional | Minimum acceptable agreement; default κ ≥ 0.60 |

## Constraints

**Must:**
- Select the appropriate agreement metric for each dimension's scale type
- Measure agreement on the pilot set if `pilot_scores` provided
- Diagnose disagreement by type (systematic bias, boundary confusion, rubric ambiguity)
- Produce a calibration plan with ≥2 concrete intervention steps
- State the go/no-go threshold for launching the main eval

**Must Not:**
- Use Cohen's kappa for >2 judges (use Fleiss' kappa)
- Use Fleiss' kappa for ordinal scales without noting it treats ordinal as nominal (use weighted kappa instead)
- Report agreement without also reporting the chance-corrected baseline

## Instructions

**Step 1 — Metric selection**

| Condition | Metric | Formula note |
|-----------|--------|--------------|
| 2 judges, binary/categorical scale | Cohen's κ | κ = (P_o - P_e) / (1 - P_e) |
| 2 judges, ordinal scale (1–5) | Weighted Cohen's κ | Weight by distance: linear or quadratic |
| ≥3 judges, binary/categorical | Fleiss' κ | Generalization of Cohen's |
| ≥3 judges, ordinal | Krippendorff's α | Handles ordinal and missing data |
| Continuous scale | ICC (2,1) or ICC (2,k) | Intraclass correlation |

**Step 2 — Agreement thresholds**

| κ / α range | Interpretation | Eval action |
|------------|----------------|-------------|
| < 0.20 | Slight | Do not launch; rubric redesign required |
| 0.20–0.40 | Fair | Calibration session required; retest before launch |
| 0.40–0.60 | Moderate | Calibration session recommended; may launch with monitoring |
| 0.60–0.80 | Substantial | Launch; monitor for drift |
| ≥ 0.80 | Almost perfect | Launch |

**Step 3 — Disagreement diagnosis**

For each dimension with κ < target, produce:

```
Dimension: [name]
Observed κ: X.XX
Target κ: X.XX
Gap: X.XX

Disagreement pattern:
  [ ] Systematic bias: Judge A consistently scores higher than Judge B on [dimension]
  [ ] Boundary confusion: Disagreements cluster at specific score boundary (X vs X+1)
  [ ] Rubric ambiguity: Certain output types have no clear anchor
  [ ] Context sensitivity: Judges weigh context differently when scoring

Evidence: <specific score pairs or example outputs that illustrate the pattern>
Root cause: <one-sentence diagnosis>
```

**Step 4 — Calibration session design**

For each diagnosed disagreement type:

| Type | Intervention |
|------|--------------|
| Systematic bias | Joint review of 5 cases with known ground truth; judge with bias re-anchors |
| Boundary confusion | Add or sharpen the boundary rule between the confused scores; add anchor examples |
| Rubric ambiguity | Author a new sub-property definition for the ambiguous output type |
| Context sensitivity | Add explicit guidance: "Score the output, not the input context" |

Calibration session structure:
1. Distribute 10 pilot cases (all judges score independently, without discussion)
2. Reveal scores; identify top-3 disagreeing cases
3. Structured discussion: each judge states rationale, then agrees on ground truth
4. Re-score 5 new cases independently; re-measure κ
5. If κ ≥ target → proceed; else repeat with 5 more cases

**Step 5 — LLM-specific agreement issues**

If `judge_type` includes `llm`:
| Issue | Detection | Control |
|-------|-----------|---------|
| Positional bias | Score same pair with A/B swapped; compare | Average both orderings |
| Temperature variance | Run same input 3x at T=0; check for drift | Use T=0 or greedy decoding |
| Prompt sensitivity | Minor rubric phrasing change → big score change | Lock rubric phrasing before launch |
| Self-preference | LLM judge prefers outputs matching its own style | Use judge model ≠ evaluated model |

## Output Format

1. **Metric selection table** — selected metric per dimension with rationale
2. **Agreement measurement** — κ / α per dimension, pilot case count, chance baseline
3. **Disagreement diagnosis** — one block per dimension below target
4. **Calibration plan** — intervention per disagreement type, session structure
5. **Go/no-go checklist** — all dimensions at target before main eval launch

## Verification

- [ ] Correct metric selected for each dimension's scale type
- [ ] Agreement measurement includes chance-corrected baseline (not just raw agreement %)
- [ ] Every dimension below target has a diagnosed root cause
- [ ] Calibration plan includes a re-measurement step (not just one session)
- [ ] LLM judges: positional bias and temperature controls addressed
