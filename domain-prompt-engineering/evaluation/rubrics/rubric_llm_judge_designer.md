---
title: "LLM Judge Designer"
category: prompt-engineering/evaluation/rubrics
description: "Design an LLM-as-judge prompt with role, rubric, chain-of-thought structure, bias controls, and a verification protocol that checks for positional, length, and self-preference bias."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - RP-01
difficulty: advanced
tags:
  - llm_judge
  - rubric_design
  - bias_control
  - automated_eval
  - judge_prompt
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/rubrics/rubric_calibrated_anchors.md
  - domain-prompt-engineering/evaluation/rubrics/rubric_inter_rater_agreement_protocol.md
  - domain-prompt-engineering/evaluation/rubrics/rubric_pairwise_vs_pointwise.md
---

## Objective

Design a complete LLM-as-judge prompt for automated scoring of AI outputs. Output includes a ready-to-use judge system prompt with role, rubric, chain-of-thought format, output schema, and a bias verification protocol that detects positional, length, and self-preference biases before the judge is used at scale.

## When to Use

- Replacing or augmenting human judges with an LLM to scale evaluation
- When human annotation cost per case exceeds the acceptable budget
- Designing a judge that can be run in CI/CD on every prompt change
- When setting up a production monitoring system that scores outputs automatically

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `task_description` | Yes | What the evaluated prompt does |
| `rubric_dimensions` | Yes | List of dimensions with 1–5 anchors (from `rubric_calibrated_anchors.md`) |
| `scoring_mode` | Yes | `pointwise` / `pairwise` (from `rubric_pairwise_vs_pointwise.md`) |
| `judge_model` | Yes | Model to use as judge (e.g., `claude-opus-4-7`, `gpt-4o`) |
| `evaluated_model` | Yes | Model being evaluated — used for self-preference bias check |
| `output_format` | Optional | `json` (default) / `markdown` |

## Constraints

**Must:**
- Write the judge prompt as a complete, copy-pasteable system prompt
- Include explicit chain-of-thought (CoT) instruction before score assignment
- Include the full rubric with anchors inline — the judge must not require external reference
- Control for ≥3 known biases (see taxonomy)
- Include an output schema with score per dimension and a CoT rationale field
- Include a bias verification protocol runnable before production use

**Must Not:**
- Use the same model as judge and evaluated model without noting self-preference risk
- Omit CoT — a judge prompt that outputs a score without reasoning is not verifiable
- Allow the judge to score on dimensions not in `rubric_dimensions`

## Instructions

**Step 1 — Judge role and framing**

```
System prompt opening:
"You are an expert evaluator assessing AI-generated outputs. You will read an [task_description] task 
and score the output on the following dimensions. Score each dimension independently on a 1–5 scale 
using the anchors provided. Think step by step before assigning any score."
```

**Step 2 — Bias taxonomy and controls**

| Bias | Description | Control mechanism |
|------|-------------|-------------------|
| Positional (pairwise) | Prefer output listed first/left | Randomize order; score each pair twice (swap); average |
| Length bias | Prefer longer outputs regardless of quality | Add explicit instruction: "Length is not a quality signal unless brevity is a rubric criterion" |
| Self-preference | Judge model prefers outputs matching its own style | Prefer judge model ≠ evaluated model; flag when same |
| Verbosity bias | Judge outputs verbose rationales for high-scored outputs | Length-limit the CoT field (`max_rationale_tokens: 100`) |
| Sycophancy | Judge agrees with any opinion in the output | Add: "Score the output against the rubric, not against your own views" |

**Step 3 — Judge prompt template**

```
[SYSTEM]
You are an expert evaluator. Task being evaluated: {task_description}

IMPORTANT SCORING RULES:
- Score each dimension independently.
- Think step by step before scoring (show reasoning in "rationale").
- Length is not a quality signal unless stated in the rubric.
- Do not let your opinion of one dimension influence another.
- Output only valid JSON matching the schema below.

RUBRIC:
{for each dimension in rubric_dimensions}
Dimension: {dimension_name}
What it measures: {dimension_definition}
Score anchors:
  5 — {anchor_5}
  4 — {anchor_4}
  3 — {anchor_3}
  2 — {anchor_2}
  1 — {anchor_1}
Boundary rule (3→4): {boundary_rule}
{end for}

OUTPUT SCHEMA:
{
  "scores": {
    "{dimension_name}": {
      "score": <1-5>,
      "rationale": "<≤100 words explaining the score against the rubric anchor>"
    }
  },
  "composite_score": <weighted mean, 1 decimal>,
  "flags": ["<any anomalies, e.g., 'output truncated', 'no answer provided'>"]
}

[USER]
INPUT:
{input}

OUTPUT TO SCORE:
{output}
```

**Step 4 — Bias verification protocol**

Run the following checks before production use:

| Check | Method | Pass threshold |
|-------|--------|----------------|
| Positional bias (pairwise only) | Score 20 pairs twice with A/B swapped; compute score delta | Mean |delta| < 0.3 |
| Length bias | Score 10 pairs where shorter output is clearly better; check if shorter wins | Short wins ≥ 70% of pairs |
| Self-preference | Generate 5 outputs with judge model and 5 with a different model; compare mean scores | Difference < 0.3 |
| CoT-score consistency | Check that rationale and score don't contradict each other in 20 cases | Contradiction rate < 5% |
| Rubric coverage | Check that rationale cites rubric anchor language in ≥80% of cases | ≥ 80% |

**Step 5 — Calibration against human scores**

Before production deployment:
1. Human-score 30 outputs independently
2. LLM-judge-score the same 30 outputs
3. Compute Cohen's κ (weighted) between human and LLM scores per dimension
4. Require κ ≥ 0.55 per dimension to proceed

## Output Format

1. **Judge system prompt** — complete, copy-pasteable, with rubric inline
2. **Bias control table** — which 3+ biases are controlled and how
3. **Bias verification protocol** — 5-check table with pass thresholds
4. **Calibration protocol** — human vs. LLM comparison with κ threshold
5. **Output schema** — JSON schema for judge outputs

## Verification

- [ ] Judge system prompt is complete and copy-pasteable without external reference
- [ ] CoT instruction appears before score assignment in the prompt
- [ ] Full rubric with anchors (1–5) inline in the system prompt
- [ ] ≥3 biases controlled with specific mechanisms
- [ ] Bias verification protocol includes ≥4 checks with pass thresholds
- [ ] Human calibration required before production use (κ ≥ 0.55)
