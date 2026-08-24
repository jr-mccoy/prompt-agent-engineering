---
title: "Rewrite a User Question into a Retrieval-Friendly Query"
category: prompt-engineering/rag-prompts
description: "Convert a raw user question into one or more queries optimized for vector / BM25 / hybrid retrieval, using HyDE, decomposition, and term expansion as the situation requires."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DC-01
  - QA-01
difficulty: intermediate
tags:
  - rag
  - query_rewriting
  - hyde
  - decomposition
  - retrieval
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/rag-prompts/rag_multi_query_expander.md
  - domain-prompt-engineering/rag-prompts/rag_grounding_contract.md
  - domain-prompt-engineering/rag-prompts/rag_followup_question_handler.md
---

# Rewrite a User Question into a Retrieval-Friendly Query

**Objective:** Transform one user question into the smallest set of retrieval queries that maximize the probability the relevant passage is inside the top-K. Output is consumed by a retriever, not a human.

**When to use:** Before any RAG retrieval call when (a) the user question is conversational, (b) it bundles multiple sub-questions, or (c) it uses terms that do not match the corpus vocabulary.

---

## Inputs

1. `user_question` — verbatim.
2. `corpus_profile` — domain, vocabulary style (lay / technical / legal / medical), language, time range.
3. `retriever_type` — `dense`, `bm25`, or `hybrid`.
4. `top_k` — integer, default 8.
5. `prior_turn_summary` — optional; used only if the question is a follow-up.

If `corpus_profile` is unknown, return error `MISSING_CORPUS_PROFILE` and stop. Do not guess.

---

## Constraints

### Must
- Choose exactly one rewrite strategy per query: `literal`, `hyde`, `decomposed`, `expanded`, or `keyword_extraction`.
- Justify the strategy choice in one sentence tied to the inputs.
- Produce ≤ 4 queries total. If more are needed, mark the question `OUT_OF_SCOPE_FOR_SINGLE_RETRIEVAL`.
- For `hyde`, generate a 40–80 word hypothetical answer, not a question.
- For `decomposed`, each sub-query must be independently answerable from a single passage.
- For `expanded`, list ≥ 1 synonym or domain-equivalent term and ≥ 1 acronym expansion (or state `none_applicable`).

### Must Not
- Echo the user question unchanged unless strategy is `literal` and justification names why.
- Add filler such as "Please find information about…".
- Produce queries longer than 256 characters.
- Mix strategies inside a single query.
- Invent corpus-specific identifiers, file names, or URLs.

---

## Instructions

1. **Classify question shape** against this table:

   | Shape | Signal | Default strategy |
   |---|---|---|
   | Single factual lookup | one named entity + one attribute | `literal` or `expanded` |
   | Conceptual / definitional | "what is", "how does X work" | `hyde` |
   | Multi-hop | "compare", "and", "vs", "then" | `decomposed` |
   | Vocabulary mismatch | lay terms over technical corpus | `expanded` |
   | Keyword-poor for BM25 | dense narrative, no nouns | `keyword_extraction` |

2. **Pick strategy** using the table; if `retriever_type=bm25`, prefer `keyword_extraction` or `expanded` over `hyde`.
3. **Write the queries.** Strip discourse markers ("could you", "I was wondering"). Keep proper nouns verbatim.
4. **Self-check** with the verification list below.

---

## Output Format

```json
{
  "shape": "single_factual | conceptual | multi_hop | vocab_mismatch | keyword_poor",
  "strategy": "literal | hyde | decomposed | expanded | keyword_extraction",
  "justification": "<one sentence tied to inputs>",
  "queries": [
    {"text": "<query string>", "intended_top_k": 8, "filter_hints": {"date_range": null, "doc_type": null}}
  ],
  "discarded_alternatives": ["<rejected rewrite>: <one-line reason>"],
  "scope_flag": "in_scope | out_of_scope_for_single_retrieval"
}
```

---

## Examples (one each)

- **Conceptual → HyDE.** User: "how does retrieval-augmented generation actually work" → one 60-word hypothetical paragraph as the dense query.
- **Multi-hop → Decomposed.** User: "did revenue grow faster than headcount last year" → two queries: revenue YoY, headcount YoY.
- **Vocabulary mismatch → Expanded.** User: "kid won't sit still" over a clinical corpus → query includes `hyperactivity`, `ADHD`, `attention deficit`.

---

## Verification

- [ ] Strategy is one of the five allowed values.
- [ ] Justification cites a specific input field.
- [ ] No query exceeds 256 chars or 4-query cap.
- [ ] No invented identifiers.
- [ ] If `retriever_type=bm25`, no `hyde` strategy used.
- [ ] If shape is `multi_hop`, queries are independent.
