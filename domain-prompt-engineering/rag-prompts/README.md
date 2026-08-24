# rag-prompts/

Prompts that govern the design, generation, and evaluation of retrieval-augmented generation paths. Each prompt is a contract or harness — system-prompt blocks, query rewriters, refusal schemas, compressors, evaluators — not a one-off chat.

## When to use this subdirectory

Designing or hardening a RAG pipeline. Pair with `hallucination-control/` for the per-claim guards that ride on top of these contracts.

## Files

| File | Description |
|------|-------------|
| `rag_query_rewriter.md` | Convert a user question into one or more retrieval-friendly queries (literal / HyDE / decomposed / expanded / keyword). |
| `rag_multi_query_expander.md` | Generate N variant queries along named axes to widen recall. |
| `rag_grounding_contract.md` | System-prompt block constraining the model to answer only from passages, with span-ID tags per sentence. |
| `rag_citation_format_designer.md` | Choose inline / footnote / hover / sidecar pattern by surface and audience; pin the emit and resolver rules. |
| `rag_no_answer_refusal.md` | Structured refusal schema with classified cause, named missing fact, and one next action. |
| `rag_passage_compression_prompt.md` | Question-conditioned, citation-preserving compression of retrieved chunks under a token budget. |
| `rag_conflict_resolution_across_sources.md` | Authority / recency / specificity / plurality policy for resolving or surfacing inter-source disagreement. |
| `rag_followup_question_handler.md` | Decide reuse / re-retrieve / augment / clarify per follow-up turn; emit the resolved query when retrieval is needed. |
| `rag_freshness_aware_prompt.md` | Tag time-sensitive claims with passage dates; refuse, caveat, or "as-of" on stale evidence. |
| `rag_evaluation_harness_for_groundedness.md` | Spec a four-metric eval (faithfulness, answer relevance, context precision, context recall) with judge prompts and pass thresholds. |

## Companion subdirectories

- `hallucination-control/` — claim-level guards (citation required, calibrated uncertainty, invented-entity audit, etc.).
- `evaluation/` — broader correctness-and-eval prompts (`correctness_*`, `taskdifficulty_*`).
- `system-prompts/` — generic system-prompt design (role, refusal policy, versioning).
