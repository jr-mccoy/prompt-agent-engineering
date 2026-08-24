---
title: "Compress Retrieved Passages Before Stuffing"
category: prompt-engineering/rag-prompts
description: "Reduce retrieved chunks to question-conditioned, citation-preserving summaries that fit a token budget without dropping facts the answer will depend on."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DC-01
  - QA-01
difficulty: advanced
tags:
  - rag
  - context_compression
  - token_budget
  - extractive_summary
  - selective_context
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_grounding_contract.md
  - domain-prompt-engineering/rag-prompts/rag_conflict_resolution_across_sources.md
  - domain-prompt-engineering/rag-prompts/rag_evaluation_harness_for_groundedness.md
---

# Compress Retrieved Passages Before Stuffing

**Objective:** Given a question and a set of retrieved passages whose total length exceeds the budget, emit a compressed corpus that (a) preserves every span needed to answer, (b) preserves passage IDs for downstream citation, and (c) discards everything else.

**When to use:** Top-K is too large to stuff (long-context cost, or the model degrades on dense context). Run between retrieval and generation.

---

## Inputs

1. `question` — verbatim.
2. `passages` — list of `{id, text, score}` from the retriever.
3. `target_tokens` — hard cap on output length.
4. `compression_mode` — `extractive` (preserve verbatim spans) or `abstractive` (paraphrase). Extractive is required for legal/medical/financial.
5. `keep_minimum_passages` — int, the minimum number of passage IDs that must appear in the output even if some are mostly cut.

---

## Constraints

### Must
- Preserve every passage ID; if a passage has no relevant span, output a stub: `{"id": "...", "kept_spans": [], "reason_kept": "diversity | low_signal | etc."}`.
- For `extractive`, each kept span is a verbatim substring of its source passage (no edits, no ellipses inside the span — use multiple spans instead).
- Each kept span must be tagged with start/end character offsets in the source.
- Total output ≤ `target_tokens`. If impossible without dropping required IDs, return `BUDGET_INFEASIBLE` with the minimum feasible budget.
- For `abstractive`, every emitted sentence carries the source ID(s) and must not introduce a token (number, name, date) absent from sources.

### Must Not
- Merge spans across passages into one quote.
- Reword inside a quote in extractive mode.
- Drop a passage that uniquely supports a sub-question detected in `question`.
- Include passage scores in the output (they leak retriever bias to the generator).
- Insert summary headers, intro, or sign-off — output is data, not prose.

---

## Instructions

1. **Sub-question split.** Decompose `question` into atomic sub-questions; mark each with the entities/attributes it needs.
2. **Per-passage span selection.** For each passage:
   - Score each sentence by overlap with sub-question entities + attributes.
   - Mark sentences with numeric values, dates, named entities, or quoted strings as high-priority.
   - Select top spans that cover the most sub-questions per token.
3. **Coverage check.** Confirm every sub-question is covered by ≥ 1 span. If not, drop the sub-question to `unsupported` rather than fabricate coverage.
4. **Budget pack.** Greedy pack by `coverage_per_token` until `target_tokens` is hit; honor `keep_minimum_passages` first.
5. **Emit.** Output the structured object below.

---

## Output Format

```json
{
  "mode": "extractive | abstractive",
  "target_tokens": <int>,
  "actual_tokens": <int>,
  "sub_questions": [{"text": "...", "covered": true|false, "by_ids": ["..."]}],
  "passages": [
    {
      "id": "<passage_id>",
      "kept_spans": [
        {"text": "<verbatim or paraphrase>", "char_start": <int>, "char_end": <int>, "covers_sub_questions": ["..."]}
      ],
      "reason_kept": "primary_evidence | diversity | low_signal | stub"
    }
  ],
  "dropped_passage_ids": ["<id>", "..."],
  "unsupported_sub_questions": ["..."]
}
```

---

## Verification

- [ ] `actual_tokens ≤ target_tokens` or `BUDGET_INFEASIBLE` returned.
- [ ] Every original passage ID appears in `passages` or `dropped_passage_ids` (no silent loss).
- [ ] In extractive mode, every span is a contiguous substring of its source (offsets verifiable).
- [ ] No numeric, date, or name in abstractive output that is not in any source.
- [ ] Unsupported sub-questions surfaced explicitly.
- [ ] No retriever scores leaked.

---

## Failure Modes

1. **Compressor over-extracts the entity-rich middle and loses the date-bearing tail.** Mitigation: priority bump for dates and numerics.
2. **Extractive spans become so granular that downstream model misses inter-sentence anaphora.** Mitigation: minimum span length 1 sentence + adjacent context if pronoun resolution needed.
3. **Greedy packing starves a low-score-but-uniquely-relevant passage.** Mitigation: `keep_minimum_passages` and sub-question coverage check before budget cut.
