---
title: "LLM-as-Judge Design"
category: AI-ML/genai-llm-engineering
description: "Build a reliable LLM-as-judge: a rubric-anchored evaluator with controls for position, verbosity, and self-preference bias, calibrated against human labels with a reported agreement statistic before it is trusted to gate."
techniques:
  - DS-35
  - QA-12
  - DS-02
  - RT-05
  - ST-02
difficulty: advanced
tags:
  - llm-as-judge
  - evaluation
  - bias-control
  - calibration
  - rubric
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_llm_evaluation_design.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_evaluation_harness.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

# LLM-as-Judge Design

**Objective:** Design an LLM-as-judge that is trustworthy enough to score or gate outputs — a clear rubric, controls for the known biases (position, verbosity, self-preference, formatting), and a calibration step that measures agreement with human judgment — so the judge's verdicts are validated against ground truth, not assumed.

**When to Use:**
- You need to scale evaluation beyond what humans can score, and a rubric exists.
- You're building the judged metrics inside an eval program or RAG harness.
- A prior "ask the LLM if it's good" judge gave numbers you don't trust.

**When NOT to Use:**
- The quality dimension is purely objective/checkable (use exact match, regex, schema validation, unit tests).
- You haven't defined what "good" means yet (use `domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md`).

## Inputs / Context

State the judge model + provider + version (which may differ from the model under test). Provide what you can:
- **What's being judged** — task, the dimension(s) to score, example good/bad outputs.
- **Scoring type** — absolute (score each output) vs pairwise (A vs B preference).
- **Human labels** — any existing human judgments for calibration (or note they must be collected).
- **Stakes** — is the judge gating deploys, ranking models, or filtering data?
- **Budget** — cost/latency per judgment, volume.

## Constraints

**Must:**
- Anchor the judge to an explicit rubric with levels and examples — never "rate this 1–10" with no criteria.
- Apply controls for position bias (pairwise), verbosity/length bias, self-preference (judge favoring its own model family), and formatting bias.
- Calibrate against a human-labeled sample and report an agreement statistic before the judge is trusted to gate.

**Must Not:**
- Treat judge scores as ground truth without the calibration step.
- Use the same model instance that generated the output to also judge it for high-stakes gating (self-preference risk) without acknowledging the bias.
- Report agreement on a sample so small the statistic is meaningless, or omit the agreement number.

**Instructions:**

1. **Define the judgment task precisely.** State the dimension being scored, absolute vs pairwise, and the exact decision the score feeds (gate, rank, filter). One judge per dimension is usually more reliable than one judge scoring everything.

2. **Write the rubric.** Provide leveled criteria with anchor examples (for absolute) or explicit preference criteria (for pairwise). Force the judge to reason against the rubric before emitting a score, and to cite the criterion it applied.

3. **Control position bias.** For pairwise, randomize A/B order and/or run both orders and aggregate; flag cases where the verdict flips on swap as low-confidence.

4. **Control verbosity and formatting bias.** Instruct the judge to score on rubric criteria, not length or polish; consider length-normalizing or explicitly noting that longer ≠ better. Strip or standardize formatting that could bias preference.

5. **Address self-preference.** If the judge model is from the same family as the generator, note the risk; prefer a different model family or ensemble for high-stakes gating, and check whether the judge systematically favors one source.

6. **Calibrate against humans.** Score a human-labeled sample with the judge; report agreement (Cohen's κ, Spearman correlation, or % agreement appropriate to the scale). Set a minimum agreement threshold; if unmet, revise the rubric and re-calibrate rather than shipping.

7. **Quantify and monitor reliability.** Report the agreement statistic, judge self-consistency (same input, repeated), and confidence handling for borderline cases. Define re-calibration triggers (rubric change, judge-model version change).

8. **Specify usage limits.** State where the judge's verdict is authoritative vs advisory, and require human review for high-stakes borderline cases.

**Output Format:**

A markdown judge spec:
- **Judgment Task** — dimension, absolute vs pairwise, downstream decision
- **Rubric** — levels/criteria + anchor examples + required reasoning
- **Bias Controls** — position, verbosity, self-preference, formatting — each with its mitigation
- **Calibration Plan** — human sample size, agreement statistic + threshold, revise loop
- **Reliability Report (template)** — agreement, self-consistency, flip rate
- **Usage Boundaries** — authoritative vs advisory, human-review triggers, re-calibration triggers

## Verification

- [ ] The judge is rubric-anchored with levels and examples, not a bare numeric ask.
- [ ] Position, verbosity, self-preference, and formatting biases each have a stated control.
- [ ] Calibration against a human-labeled sample is specified with an agreement statistic and threshold.
- [ ] Self-consistency (repeat-judgment) and flip-on-swap handling are addressed.
- [ ] Usage boundaries (authoritative vs advisory) and re-calibration triggers are defined.
- [ ] No agreement claims without a sample size that makes them meaningful.

## False-Positive Prevention

❌ **DON'T:**
- Ship a judge because its scores "look reasonable" — looking reasonable is not agreement with humans.
- Use pairwise judging without order randomization; position bias alone can swing preference.
- Let the judge reward longer, more confident, or better-formatted answers regardless of correctness.
- Have a model judge its own family's outputs for a high-stakes gate without flagging self-preference.

✅ **DO:**
- Calibrate against human labels and report κ/correlation before trusting the judge to gate.
- Randomize position and treat swap-flips as low-confidence verdicts.
- Score strictly on rubric criteria and neutralize length/formatting influence.
- Use a different model family (or ensemble) and human review for high-stakes decisions.

## Example Output

```markdown
## LLM-Judge: Answer Faithfulness (judge model: <different family from generator>)

### Judgment Task
Absolute, claim-level: "Is this claim supported by the provided context?" Feeds the
faithfulness gate in genai_rag_evaluation_harness.md.

### Rubric
1 = fully supported by a context span; 0.5 = partially/implied; 0 = unsupported or contradicted.
Judge must quote the supporting span or state "no span" before scoring.

### Bias Controls
- Position: N/A (absolute, single output).
- Verbosity: score per-claim, not per-answer; length irrelevant.
- Self-preference: judge from a different model family than the generator.
- Formatting: claims extracted to plain text before judging.

### Calibration Plan
60 human-labeled claims. Target κ ≥ 0.65. Achieved κ = 0.71 -> accept. If < 0.65, tighten
"partially supported" definition and re-run.

### Reliability Report
κ vs human = 0.71; self-consistency over 3 runs = 96% identical; borderline (0.5) cases -> human spot-check.

### Usage Boundaries
Authoritative for the regression gate at claim level; answer-level abstention decisions get
human review. Re-calibrate on judge-model version bump.
```

**Techniques Used:**
- **DS-35 (LLM-as-Judge with Rubric):** the core method — rubric-anchored judging.
- **QA-12 (False Positives Identification):** bias controls and calibration prevent false-trust verdicts.
- **DS-02 (Metric Specification):** agreement statistics and thresholds make the judge measurable.
- **RT-05 (Evidence-Based Reasoning):** the judge must cite the rubric criterion / supporting span.
- **ST-02 (Structured Sequential Instructions):** rubric → bias controls → calibration → usage limits.

**Related Prompts:**
- `genai_llm_evaluation_design.md` — the program this judge plugs into.
- `genai_rag_evaluation_harness.md` — uses this judge for faithfulness/quality scoring.
- `domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md` — define "correct" before building the judge.
