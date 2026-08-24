---
title: "Evaluation Harness for RAG Groundedness, Relevance, and Context Precision"
category: prompt-engineering/rag-prompts
description: "Specify a test harness that scores a RAG system on faithfulness, answer relevance, context precision, and context recall — with judge prompts, datasets, and pass thresholds."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - PR-02
difficulty: advanced
tags:
  - rag
  - evaluation
  - faithfulness
  - context_precision
  - groundedness
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_grounding_contract.md
  - domain-prompt-engineering/rag-prompts/rag_passage_compression_prompt.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

# Evaluation Harness for RAG Groundedness

**Objective:** Produce a runnable evaluation specification for a RAG system covering four metrics — `faithfulness`, `answer_relevance`, `context_precision`, `context_recall` — with judge prompts, scoring rules, sample sizing, and pass/fail thresholds tied to defect tolerances.

**When to use:** Before shipping a RAG path; after any change to retriever, chunker, embedder, generator, prompt, or model. Re-run on a frozen eval set; deltas are the signal.

---

## Inputs

1. `system_under_test` — the RAG path to evaluate (retriever, generator, system prompt).
2. `gold_set` — `{question, ideal_answer, must_cite_ids[], must_not_cite_ids[]}` records, ≥ 50.
3. `defect_tolerance` — max acceptable rate per metric (e.g., faithfulness ≥ 0.95).
4. `judge_model` — explicit model + version for LLM-as-judge calls.
5. `human_audit_fraction` — float, 0–1; fraction of judge outputs reviewed by a human.

---

## Constraints

### Must
- Define each metric with a one-sentence operational definition AND a judge prompt.
- Sample size per metric ≥ statistical power minimum for the tolerance (state the power calc).
- Score every record on every metric; no skipped cells.
- Report deltas vs. previous run when present.
- Treat the judge model as a dependency: pin its version; record it in the run metadata.

### Must Not
- Combine metrics into a single score; report separately.
- Use the same model as both generator and judge in the primary run.
- Average over questions where retrieval failed entirely; segment instead.
- Replace human audit with model self-audit.
- Move the threshold to make a run pass.

---

## Metric Definitions and Judge Prompts

| Metric | Definition | Judge prompt skeleton |
|---|---|---|
| `faithfulness` | Fraction of generated claims that are entailed by the retrieved context. | "List atomic claims from <answer>. For each, mark `entailed | contradicted | not_in_context` against <context>." |
| `answer_relevance` | How well the answer addresses the question (irrespective of correctness). | "On a 0–1 scale, does <answer> address <question>? Penalize off-topic content." |
| `context_precision` | Fraction of retrieved passages that contain question-relevant content. | "For each passage, mark `relevant | partially_relevant | irrelevant` to <question>." |
| `context_recall` | Fraction of `ideal_answer` claims that are findable in the retrieved context. | "List atomic claims from <ideal_answer>. For each, mark `present | partial | absent` in <context>." |

---

## Instructions

1. **Freeze gold set.** Lock IDs and ideal answers; changes mean a new eval, not a re-run.
2. **Stratify.** Tag each record with `difficulty`, `topic`, `time_sensitive`. Report metrics per stratum.
3. **Run.** For each record, capture: question, retrieved passage IDs, generated answer, judge scores per metric.
4. **Audit.** Sample `human_audit_fraction` of records; compute judge-human agreement (Cohen's kappa). If kappa < 0.6, judge prompt is broken — fix before trusting metrics.
5. **Compare.** Diff vs. last run; flag any metric regressing more than tolerance/2.
6. **Decide.** Ship if all metrics ≥ tolerance AND no stratum below tolerance × 0.9.

---

## Output Format

```json
{
  "run_id": "<uuid>",
  "system_under_test": {"retriever": "...", "generator": "...", "prompt_hash": "..."},
  "judge_model": "<name>@<version>",
  "metrics": {
    "faithfulness": {"score": <float>, "n": <int>, "by_stratum": {"...": <float>}, "delta_vs_prior": <float>},
    "answer_relevance": {"score": <float>, "n": <int>, "by_stratum": {}, "delta_vs_prior": <float>},
    "context_precision": {"score": <float>, "n": <int>, "by_stratum": {}, "delta_vs_prior": <float>},
    "context_recall": {"score": <float>, "n": <int>, "by_stratum": {}, "delta_vs_prior": <float>}
  },
  "human_audit": {"fraction": <float>, "kappa_per_metric": {"faithfulness": <float>, "...": <float>}},
  "decision": "ship | block | investigate",
  "blocking_reasons": ["..."]
}
```

---

## Verification

- [ ] All four metrics scored on every record.
- [ ] Kappa reported and ≥ 0.6 for each judged metric.
- [ ] Stratum-level scores included.
- [ ] Judge model and version recorded.
- [ ] Decision logic uses tolerance + stratum floor, not aggregate only.
- [ ] No metric average computed over retrieval-zero records.

---

## Anti-Patterns

1. Single composite "RAG score" — hides which dimension regressed.
2. Judge model = generator model — circular evaluation.
3. Re-using the same gold set after retraining the embedder on it — leakage.
4. Reporting only mean — variance and stratum floor matter.
