---
title: "RAG Evaluation Harness Design"
category: AI-ML/genai-llm-engineering
description: "Build a grounded evaluation harness for a RAG system — separating retrieval quality (precision/recall) from faithfulness/groundedness and end-answer quality, anchored to a golden set with human calibration."
techniques:
  - ST-02
  - DS-02
  - QA-17
  - DS-35
  - QA-12
difficulty: advanced
tags:
  - rag
  - evaluation
  - faithfulness
  - golden-set
  - retrieval-metrics
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_as_judge_design.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
---

# RAG Evaluation Harness Design

**Objective:** Design an evaluation harness for a RAG system that measures the three independent failure surfaces — retrieval (did we fetch the right context?), faithfulness/groundedness (is the answer supported by the fetched context?), and answer quality (is it correct and useful?) — anchored to a golden set, with automated metrics calibrated against human judgment.

**When to Use:**
- Before trusting a RAG system in production, or before/after any change to chunking, embedding, retrieval, or prompt.
- To set up a regression gate so RAG quality doesn't silently drift as the corpus or model changes.
- To localize *where* RAG quality is failing (retrieval vs generation) with numbers, not intuition.

**When NOT to Use:**
- For diagnosing a single bad answer interactively (use `genai_rag_retrieval_quality_debug.md`).
- For general LLM eval not involving retrieval (use `genai_llm_evaluation_design.md`).

## Inputs / Context

State the model + provider + version. Provide what you can:
- **System under test** — the RAG pipeline stages and what's changeable.
- **Corpus + query distribution** — so the golden set is representative.
- **Existing labeled data** — any Q/relevant-doc pairs, expert answers, or user feedback.
- **Grounding requirement** — is abstention expected? Citation required?
- **Decision being made** — accept/reject, A/B between configs, regression gate threshold.

## Constraints

**Must:**
- Measure retrieval, faithfulness, and answer quality as *separate* metrics so failures can be localized.
- Require a golden set with documented construction (how queries were sampled, who labeled relevance/answers).
- If an LLM-as-judge scores faithfulness or quality, require human calibration on a sample and an agreement statistic.

**Must Not:**
- Collapse RAG quality into a single end-to-end score that hides whether retrieval or generation failed.
- Report metrics without confidence intervals / sample sizes, or compare configs without a significance check.
- Invent benchmark numbers; all targets must come from the user's golden set or be marked as to-be-measured.

**Instructions:**

1. **Construct the golden set.** Sample queries to cover the real distribution (factoid, multi-hop, out-of-scope, conflicting-source). For each, record gold relevant chunks/sources and a reference answer (or acceptance rubric). Document sampling and labeling so it's auditable.

2. **Define retrieval metrics.** Specify recall@k, precision@k, and MRR/NDCG against gold relevant chunks. State k values that match the production prompt budget. Include an out-of-scope subset to measure correct empty-retrieval.

3. **Define faithfulness/groundedness metrics.** Measure whether each answer claim is supported by the *retrieved* context (not by world knowledge). Specify granularity (claim-level vs answer-level) and how unsupported claims and unsupported-but-true claims are both penalized.

4. **Define answer-quality metrics.** Specify correctness vs the reference (rubric-scored), completeness, and citation accuracy. Separate "wrong because retrieval missed" from "wrong despite good retrieval."

5. **Design the judging method and calibrate it.** If using LLM-as-judge for faithfulness/quality, define the rubric, control for position/verbosity bias, and validate against human labels on a sample; report agreement (e.g., Cohen's κ / % agreement). Defer judge construction to `genai_llm_as_judge_design.md`.

6. **Add abstention and adversarial cases.** Include queries that *should* be refused and queries with misleading near-duplicate context; measure false-answer rate.

7. **Set regression gates and report with uncertainty.** Define pass/fail thresholds per metric, sample sizes, and confidence intervals; require a significance check when comparing two configurations.

8. **Wire it for CI.** Specify how the harness runs on each change, what it logs, and how a regression blocks a deploy.

**Output Format:**

A markdown spec:
- **Golden Set Spec** — composition, sampling, labeling protocol, size
- **Metric Suite** — table: Surface | Metric | Definition | Target | Sample/CI
- **Judging & Calibration** — judge rubric pointer, bias controls, human-agreement target
- **Failure Localization Map** — how each metric pattern points to retrieval vs generation vs grounding
- **Regression Gate** — thresholds, significance test, CI wiring
- **Example Scorecard** — filled-in numbers with intervals

## Verification

- [ ] Retrieval, faithfulness, and answer quality are measured separately.
- [ ] The golden set's construction (sampling + labeling) is documented and covers out-of-scope/multi-hop/conflict cases.
- [ ] Any LLM-judge is calibrated against humans with a reported agreement statistic and bias controls.
- [ ] Metrics carry sample sizes and confidence intervals; config comparisons include a significance check.
- [ ] Thresholds map to a concrete accept/reject or regression-gate decision.
- [ ] No fabricated numbers; targets trace to the golden set.

## False-Positive Prevention

❌ **DON'T:**
- Report a single "RAG accuracy" number — it hides whether the failure was retrieval or generation.
- Score faithfulness by asking the judge "is this a good answer?" — quality and groundedness are different surfaces.
- Trust an LLM-judge's faithfulness scores without checking them against human labels on a sample.
- Declare a config "better" from a few percentage points on a small set without a significance test.
- Let answers that are *true but unsupported by the retrieved context* pass faithfulness — that's still a grounding failure.

✅ **DO:**
- Decompose into retrieval / faithfulness / answer-quality and report each.
- Build the golden set to include out-of-scope and conflicting-source queries so abstention is measured.
- Calibrate the judge against humans and report agreement; control for position/verbosity bias.
- Attach confidence intervals and run significance tests on comparisons.
- Trace each wrong answer to its stage so fixes target the real failure.

## Example Output

```markdown
## RAG Eval Harness: Policy Assistant (model <provider/model vX>)

### Golden Set
180 queries: 100 factoid, 40 multi-hop, 20 conflicting-source, 20 out-of-scope.
Relevant sections labeled by 2 SMEs (κ=0.81); reference answers written by SMEs.

### Metric Suite
| Surface | Metric | Definition | Target | Sample/CI |
|---|---|---|---|---|
| Retrieval | recall@5 | gold sections in top-5 | ≥ 0.90 | n=160, ±0.04 |
| Retrieval | OOS empty-rate | correct no-hit on OOS | ≥ 0.85 | n=20 |
| Faithfulness | claim-support | % answer claims supported by retrieved ctx | ≥ 0.95 | judge, κ_vs_human=0.78 |
| Answer | correctness | rubric 0–3 vs reference | ≥ 2.5 mean | n=160, ±0.12 |
| Answer | false-answer rate | answered when should abstain | ≤ 0.05 | n=20 OOS |

### Judging & Calibration
LLM-judge per genai_llm_as_judge_design.md: claim-level rubric, randomized answer order,
length-normalized. Validated on 50 human-labeled items → κ=0.78 (acceptable; recheck quarterly).

### Failure Localization
- recall@5 low + faithfulness high → fix retrieval/chunking.
- recall@5 high + faithfulness low → fix prompt/grounding instruction.
- both high + correctness low → reference/rubric or model capability issue.

### Regression Gate
Block deploy if recall@5 drops >0.03 (paired bootstrap p<0.05) or faithfulness <0.95.
Runs on every chunking/embedding/prompt change in CI.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** golden set → metrics → calibration → gate.
- **DS-02 (Metric Specification):** precise, separated retrieval/faithfulness/quality metrics.
- **QA-17 (Named Scores for Multi-Dimensional Metrics):** the scorecard names each surface.
- **DS-35 (LLM-as-Judge with Rubric):** judged metrics use a calibrated rubric.
- **QA-12 (False Positives Identification):** abstention/adversarial cases catch false answers.

**Related Prompts:**
- `genai_rag_system_design.md` — the design whose stages this harness verifies.
- `genai_llm_as_judge_design.md` — build the calibrated judge used here.
- `genai_rag_retrieval_quality_debug.md` — drill into individual failures the harness surfaces.
