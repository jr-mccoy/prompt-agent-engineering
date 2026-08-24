---
title: "A/B Test Runner Design"
category: prompt-engineering/evaluation/regression
description: "Design a rigorous A/B experiment over two prompt variants: hypothesis, primary metric, sample size, blinding protocol, scoring rubric, and a pre-committed decision rule."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - QA-01
  - QA-08
difficulty: advanced
tags:
  - ab_testing
  - prompt_variants
  - sample_size
  - statistical_significance
  - eval_design
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/regression/regression_change_impact_estimator.md
  - domain-prompt-engineering/evaluation/regression/regression_canary_set_designer.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Design a complete A/B experiment comparing two prompt variants (control A vs. challenger B) with a stated hypothesis, primary metric, sample size calculation, blinding protocol, scoring rubric, and a pre-committed decision rule. Output is an experiment spec that can be executed without further design decisions.

## When to Use

- When a prompt change is significant enough to warrant measurement before full deployment
- When intuition conflicts about which variant is better and you need evidence
- When a previous eval showed a difference but you're unsure if it was noise
- When multiple stakeholders need to agree on a ship decision based on shared criteria

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `prompt_a` | Yes | Control prompt (current production) |
| `prompt_b` | Yes | Challenger prompt (proposed change) |
| `task_description` | Yes | What the prompt does |
| `primary_metric` | Yes | The one metric that determines the ship decision |
| `secondary_metrics` | Optional | Additional metrics to track but not ship on |
| `budget` | Optional | Max API calls or cost allowed for the experiment |

## Constraints

**Must:**
- State a falsifiable hypothesis before designing the experiment
- Calculate minimum sample size with stated assumptions (effect size, α, power)
- Define blinding protocol: how scorers are prevented from knowing which variant produced each output
- Specify the scoring rubric with ≥3 score anchors per metric dimension
- Pre-commit the decision rule before running (not after seeing results)
- Specify the rollout plan for the winning variant

**Must Not:**
- Use the same data for hypothesis generation and hypothesis testing (no HARKing)
- Define the decision rule after seeing partial results
- Use a single overall score if the primary metric has multiple dimensions — decompose them

## Instructions

**Step 1 — Hypothesis statement**

```
H0 (null): Prompt B produces outputs scoring ≤ Prompt A on [primary_metric]
H1 (alternative): Prompt B produces outputs scoring > Prompt A on [primary_metric]
Direction: one-tailed
Expected effect size: <X% relative improvement or N point improvement on rubric>
Justification: <why you expect this direction and magnitude>
```

**Step 2 — Sample size calculation**

Use the formula for comparing two proportions or two means:
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Effect size (δ) | X | Minimum improvement that justifies shipping B |
| Significance level (α) | 0.05 | Standard |
| Power (1-β) | 0.80 | Standard; raise to 0.90 for high-stakes decisions |
| Baseline metric value | X | From historical data or pilot run |
| **Minimum N per variant** | **N** | Result |
| **Total samples** | **2N** | |

If budget constrains N below the minimum, state: "This experiment is underpowered. Accept wider uncertainty or reduce effect size threshold."

**Step 3 — Input sampling protocol**

| Decision | Specification |
|----------|---------------|
| Input source | Production logs / golden set / synthetic |
| Sampling method | Random / stratified by [dimension] |
| Stratification rationale | Ensure coverage of [behavior cluster] |
| Excluded inputs | [Any inputs excluded and why] |

**Step 4 — Blinding protocol**

1. Run both variants against each sampled input; store outputs labeled only with UUID
2. Scorers receive only (input, output, rubric) — no variant label
3. Score all outputs before unblinding
4. Unblind only after all scores are recorded and locked

**Step 5 — Scoring rubric**

Define the primary metric as a 1–5 scale with named anchors:

| Score | Anchor definition | Example output property |
|-------|-------------------|------------------------|
| 5 | [Specific description of best] | |
| 3 | [Specific description of middle] | |
| 1 | [Specific description of worst] | |
| 2 | Between 1 and 3 | |
| 4 | Between 3 and 5 | |

**Step 6 — Pre-committed decision rule**

```
Ship B if:
  mean(B) - mean(A) > δ (effect size threshold)
  AND p-value < α
  AND no secondary metric degrades by > [threshold]%

Do not ship B if:
  p-value ≥ α
  OR any secondary metric degrades by > [threshold]%

Revisit if:
  0 < p-value < 0.10 AND B shows direction but experiment is underpowered
  → Action: extend sample size by N and re-run
```

## Output Format

1. **Hypothesis block** — H0, H1, direction, expected effect, justification
2. **Sample size table** — parameters, minimum N, total samples, budget check
3. **Sampling protocol** — source, method, stratification, exclusions
4. **Blinding protocol** — step-by-step procedure
5. **Scoring rubric** — primary metric with 5 anchors; secondary metrics listed
6. **Decision rule** — ship / do not ship / revisit conditions, pre-committed and dated

## Verification

- [ ] Hypothesis stated before sample size calculation (not derived from it)
- [ ] Sample size includes effect size, α, and power assumptions explicitly
- [ ] Blinding protocol prevents scorers from knowing variant until all scores locked
- [ ] Decision rule pre-committed with ship, no-ship, and revisit conditions
- [ ] Scoring rubric has named anchors at 1, 3, and 5 (not just "low/medium/high")
