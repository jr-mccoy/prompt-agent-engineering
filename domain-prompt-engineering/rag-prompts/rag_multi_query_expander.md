---
title: "Multi-Query Expansion for Recall"
category: prompt-engineering/rag-prompts
description: "Generate N diverse query variants from one user question to maximize the probability the relevant passage appears in the merged top-K across runs."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DC-01
  - QA-01
difficulty: intermediate
tags:
  - rag
  - query_expansion
  - recall
  - retrieval_diversity
  - mmr
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_query_rewriter.md
  - domain-prompt-engineering/rag-prompts/rag_passage_compression_prompt.md
  - domain-prompt-engineering/rag-prompts/rag_evaluation_harness_for_groundedness.md
---

# Multi-Query Expansion for Recall

**Objective:** Produce N variant queries from one source question, each rewritten along a single named axis of variation, so that union-of-results coverage exceeds any single query.

**When to use:** Recall-bounded retrieval (the right passage exists but the single query misses it). Do not use for latency-bounded paths or when the corpus is small enough for exhaustive search.

---

## Inputs

1. `user_question` — verbatim.
2. `n_variants` — integer, 3–8. Reject `n>8` with `TOO_MANY_VARIANTS`.
3. `axes_allowed` — subset of: `synonym`, `specificity_up`, `specificity_down`, `paraphrase`, `entity_substitution`, `temporal`, `perspective`, `language_register`.
4. `prior_failed_queries` — optional list of queries that returned irrelevant results.

---

## Constraints

### Must
- Every variant uses exactly one axis from `axes_allowed`; declare the axis per variant.
- Across the N variants, use ≥ ⌈N/2⌉ distinct axes.
- Each variant differs from the source and from every other variant by at least one content word (not just punctuation).
- Preserve any quoted strings, IDs, dates, or proper nouns from the source verbatim.
- Mark one variant `anchor=true` — the most literal rewrite, used as a baseline.

### Must Not
- Generate variants that change the answer requested (only the phrasing).
- Use the `entity_substitution` axis on a question whose entity is the subject of the answer.
- Output more than `n_variants` items.
- Translate to another language unless `language_register` is explicitly in `axes_allowed`.
- Repeat axes if other allowed axes remain unused.

---

## Instructions

1. Parse the source question; list its content words and any quoted spans.
2. Rank the allowed axes by expected lift given the question shape:
   - Vague noun → `specificity_up`.
   - Over-narrow → `specificity_down`.
   - Jargon-heavy → `synonym` or `language_register`.
   - Time-sensitive → `temporal`.
   - First-person → `perspective`.
3. Generate one variant per top-ranked axis until N is reached.
4. If `prior_failed_queries` is provided, ensure no new variant collides with any failed query (Jaccard token overlap < 0.7).
5. Self-check against verification list.

---

## Output Format

```json
{
  "source_question": "<verbatim>",
  "anchor_variant": "<string>",
  "variants": [
    {"text": "<query>", "axis": "<one of axes_allowed>", "lift_hypothesis": "<one phrase>"},
    "..."
  ],
  "axes_used": ["<axis>", "..."],
  "coverage_note": "<one line: which gap each axis is meant to close>"
}
```

---

## Verification

- [ ] Exactly `n_variants` items returned, one marked anchor.
- [ ] Every variant has a declared axis from `axes_allowed`.
- [ ] ≥ ⌈N/2⌉ distinct axes used.
- [ ] All quoted spans, IDs, and proper nouns preserved verbatim.
- [ ] No collision with `prior_failed_queries` (token-Jaccard < 0.7).
- [ ] No variant changes the requested answer.

---

## Notes

- Pair this with re-ranking (e.g., MMR or cross-encoder) downstream; raw union of top-K from N queries inflates noise.
- For `n_variants ≥ 5`, expect diminishing recall gains; budget a stop rule in the calling code.
- If retrieval still misses after expansion, the failure is likely chunking or embedding, not querying — switch tools, not variants.
