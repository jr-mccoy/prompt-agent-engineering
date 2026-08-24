---
title: "LLM Evaluation Program Design"
category: AI-ML/genai-llm-engineering
description: "Design an end-to-end LLM evaluation program: task rubrics, golden and adversarial sets, blended human + automated scoring with judge calibration, and regression gates wired into CI."
techniques:
  - ST-02
  - DS-02
  - DS-35
  - QA-17
  - QA-12
difficulty: advanced
tags:
  - evaluation
  - golden-set
  - adversarial
  - regression-gate
  - rubric
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_llm_as_judge_design.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_evaluation_harness.md
  - domain-AI-ML/genai-llm-engineering/genai_synthetic_data_with_llms.md
---

# LLM Evaluation Program Design

**Objective:** Design a durable evaluation program for an LLM feature — task-specific rubrics, a golden set plus an adversarial set, a blend of human and automated (LLM-judge) scoring with calibration, and regression gates wired into deployment — so quality is measured against a fixed standard and regressions are caught before users see them.

**When to Use:**
- Standing up evaluation for an LLM feature that currently ships on vibes/spot-checks.
- Before changing a prompt, model version, or pipeline and needing a regression gate.
- Establishing a quality bar that survives model-version churn.

**When NOT to Use:**
- The task is specifically RAG (use `genai_rag_evaluation_harness.md` for the retrieval/faithfulness decomposition).
- You only need to build the judge itself (use `genai_llm_as_judge_design.md`).

## Inputs / Context

State the model + provider + version. Provide what you can:
- **Task definition** — what the feature does and what "good output" means in concrete terms.
- **Quality dimensions** — correctness, format, safety, tone, completeness — and their relative priority.
- **Existing data** — past outputs, user feedback, any human labels.
- **Known failure modes** — what it gets wrong today; edge cases that matter.
- **Operational fit** — how often evals run, cost/time budget, who can label.

## Constraints

**Must:**
- Translate each quality dimension into a rubric with explicit, distinguishable levels and anchor examples.
- Build both a golden set (representative) and an adversarial set (known-hard, edge, failure-inducing cases).
- Calibrate any automated judge against human labels and report agreement before trusting it as a gate.

**Must Not:**
- Use a single blended score that hides which dimension regressed.
- Treat an LLM judge's output as ground truth without human calibration and bias controls (cross-link `genai_llm_as_judge_design.md`).
- Fabricate baseline numbers; all targets must be measured on the user's sets or marked to-be-measured.

**Instructions:**

1. **Define the task and quality dimensions.** Make "good output" concrete per dimension (correctness, format, safety, tone, completeness) and rank them so tradeoffs are explicit.

2. **Write rubrics with anchors.** For each dimension, define scoring levels with descriptions and at least one anchor example per level so human and automated scorers apply the same standard.

3. **Build the golden set.** Sample cases that reflect the real input distribution; record reference outputs or acceptance criteria; document sampling and labeling (who, how, inter-rater agreement). Keep it frozen for regression comparisons.

4. **Build the adversarial set.** Collect known-failure inputs, edge cases, ambiguous prompts, prompt-injection attempts, and safety-sensitive cases. This set guards against silent degradation on the hard tail.

5. **Choose the scoring blend.** Decide which dimensions need human scoring (subjective/high-stakes) vs automated/LLM-judge (scalable). For judged dimensions, define the judge rubric, bias controls, and the human-calibration sample with an agreement target.

6. **Set baselines and gates.** Measure the current model/prompt on both sets to establish baselines with confidence intervals. Define per-dimension regression thresholds and the rule that blocks a deploy.

7. **Wire into the workflow.** Specify what runs in CI (fast subset) vs scheduled (full + human), how results are stored/trended, and how new production failures feed back into the sets.

8. **Plan for model-version churn.** Define how the program re-baselines and re-calibrates judges when the underlying model version changes.

**Output Format:**

A markdown program spec:
- **Quality Dimensions & Priority** — ranked list with definitions
- **Rubrics** — per dimension: levels + anchor examples
- **Golden Set Spec** — composition, sampling, labeling, size, agreement
- **Adversarial Set Spec** — failure/edge/safety categories
- **Scoring Blend** — human vs automated per dimension + judge calibration plan
- **Baselines & Gates** — current numbers (or to-measure) + regression thresholds
- **Run Plan** — CI vs scheduled, storage/trending, feedback loop, re-baseline policy

## Verification

- [ ] Each quality dimension has a leveled rubric with anchor examples.
- [ ] Both a golden set and an adversarial/edge set exist, with documented construction.
- [ ] Automated judges are calibrated against humans with a reported agreement statistic.
- [ ] Per-dimension scores are reported (no single hidden blend) with confidence intervals.
- [ ] Regression gates define a concrete deploy-blocking rule.
- [ ] A re-baseline/re-calibration policy exists for model-version changes.

## False-Positive Prevention

❌ **DON'T:**
- Average everything into one score — a format regression can hide behind a correctness gain.
- Build only a representative golden set and skip adversarial cases; degradation usually shows on the hard tail first.
- Gate on an LLM judge without first checking its agreement with humans on a labeled sample.
- Treat a small-sample improvement as real without a confidence interval / significance check.

✅ **DO:**
- Score and report each dimension separately so regressions are attributable.
- Pair the golden set with an adversarial set that targets known and safety-sensitive failures.
- Calibrate judges to humans, control for position/verbosity bias, and re-check on model changes.
- Feed confirmed production failures back into the sets so the program hardens over time.

## Example Output

```markdown
## Eval Program: Meeting-Notes Summarizer (model: <provider/model vX>)

### Quality Dimensions (ranked)
1. Factual fidelity (no invented action items)  2. Completeness (all decisions captured)
3. Format (sectioned: Decisions / Actions / Risks)  4. Tone (neutral, concise)

### Rubrics (excerpt — Factual fidelity)
3 = every statement traceable to transcript; 2 = minor omission, no invention;
1 = one invented/wrong item; 0 = multiple inventions. Anchors attached per level.

### Golden Set
150 transcripts across 5 meeting types; reference summaries by 2 reviewers (κ=0.74). Frozen.

### Adversarial Set
40 cases: overlapping speakers, unresolved debates (must NOT fabricate a decision),
PII-laden transcripts (must redact), empty/irrelevant audio.

### Scoring Blend
Fidelity + completeness: LLM-judge (calibrated, κ=0.71 vs 30 human labels) with claim-level checks.
Tone/format: automated regex/structure checks. Adversarial set: human-reviewed monthly.

### Baselines & Gates
Current: fidelity 2.6, completeness 2.3, format 0.97. Gate: block if fidelity drops >0.2
(paired bootstrap p<0.05) or any fabricated-decision on the adversarial set.

### Run Plan
CI: 30-case subset. Nightly: full golden. Monthly: adversarial + human. Re-baseline on model bump.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** dimensions → rubrics → sets → scoring → gates.
- **DS-02 (Metric Specification):** each dimension is a defined, scored metric.
- **DS-35 (LLM-as-Judge with Rubric):** automated scoring uses calibrated rubrics.
- **QA-17 (Named Scores for Multi-Dimensional Metrics):** per-dimension scores prevent hidden regressions.
- **QA-12 (False Positives Identification):** the adversarial set catches silent tail degradation.

**Related Prompts:**
- `genai_llm_as_judge_design.md` — build the calibrated judge this program relies on.
- `genai_rag_evaluation_harness.md` — the RAG-specific variant with retrieval/faithfulness layers.
- `genai_synthetic_data_with_llms.md` — expand eval sets without contaminating them.
