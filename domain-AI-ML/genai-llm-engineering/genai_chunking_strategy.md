---
title: "RAG Chunking Strategy"
category: AI-ML/genai-llm-engineering
description: "Design and evaluate a chunking strategy for RAG — size, overlap, structure-awareness, and metadata — matched to document type and query type, and proven on a retrieval eval set rather than guessed."
techniques:
  - RT-02
  - DS-02
  - CM-02
  - QA-12
  - ST-02
difficulty: intermediate
tags:
  - chunking
  - rag
  - retrieval
  - preprocessing
  - evaluation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_embedding_model_selection.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
---

# RAG Chunking Strategy

**Objective:** Design a chunking strategy for a RAG corpus — chunk size, overlap, structure-awareness (heading/section/semantic boundaries), and per-chunk metadata — matched to the document structure and query type, with chunk parameters chosen by evaluation on a retrieval set rather than by default, because chunking silently caps the ceiling of retrieval quality.

**When to Use:**
- Designing ingestion for a new RAG system and choosing how to split documents.
- Retrieval returns the right document but the wrong fragment, or answer-bearing text is split across chunks.
- Re-tuning chunking to lift recall/precision before touching the embedder or model.

**When NOT to Use:**
- The whole architecture is undecided (use `genai_rag_system_design.md`).
- The problem is the embedding model, not the chunks (use `genai_embedding_model_selection.md`).

## Inputs / Context

Provide what you can:
- **Document types** — structure (headings/sections, tables, code, prose), typical length, format (markdown/PDF/HTML).
- **Query type** — factoid (needs precise small chunks), summarization/multi-hop (needs broader context), exact-lookup.
- **Embedder constraints** — max sequence length (chunks must fit), how the model handles long inputs.
- **Generation budget** — how many/how large chunks the prompt can hold (cross-link `genai_context_window_strategy.md`).
- **Eval set** — labeled query→relevant-passage pairs (or note one must be built).

## Constraints

**Must:**
- Match chunk size and structure-awareness to document type and query type, justifying each choice.
- Keep chunks within the embedder's max sequence length (no silent truncation).
- Attach metadata (source, section/heading, position, date, access scope) to every chunk for filtering and citation.
- Prove the chosen parameters on a retrieval eval set, not by default values.

**Must Not:**
- Recommend a single universal chunk size; tie size/overlap to the corpus and queries and mark them tunable.
- Split mid-sentence or strip structural context (a chunk losing its heading becomes ambiguous).
- Fabricate "optimal" sizes; require A/B evaluation on the user's data.

**Instructions:**

1. **Profile documents and queries.** Characterize document structure and the query types. Factoid queries favor smaller, precise chunks; multi-hop/summarization favor larger or hierarchical chunks. Mixed distributions may need multiple granularities.

2. **Choose a chunking method.** Compare fixed-size (simple, ignores structure), structure-aware (split on headings/sections — preserves meaning), and semantic/recursive (split on natural boundaries). Recommend based on the profile; structure-aware usually beats fixed for structured docs.

3. **Set size and overlap as a starting range.** Propose starting size and overlap tied to query type and embedder max-seq, explicitly framed as values to A/B on the eval set. Overlap prevents answer-bearing text from being severed at a boundary.

4. **Preserve structural context.** Specify carrying heading paths/section titles into each chunk (or prepending them) so a retrieved fragment is self-explanatory and citable. Handle tables/code/lists specially — don't shred them.

5. **Attach metadata.** Define the metadata each chunk carries (source, section, position, date, access scope) for retrieval filtering, recency, permissions, and citation.

6. **Evaluate on the retrieval set.** A/B candidate configs (sizes, overlap, methods) measuring recall@k and precision@k against labeled relevances. Watch the tradeoff: smaller chunks raise precision but may split context; larger chunks raise recall but dilute and crowd the prompt.

7. **Account for downstream effects.** Confirm the chosen chunk count/size fits the generation prompt budget and check for lost-in-the-middle when many chunks are stuffed (cross-link `genai_context_window_strategy.md`).

8. **Recommend and define re-tuning.** State the chosen config, the runner-up, and when to re-tune (new doc types, embedder change, retrieval regression).

**Output Format:**

A markdown chunking spec:
- **Document & Query Profile** — structure + query types
- **Method Choice** — fixed vs structure-aware vs semantic + rationale
- **Size/Overlap Plan** — starting values (marked tunable) + reasoning
- **Structure & Metadata** — context preservation + per-chunk metadata fields
- **Evaluation Plan & Results** — A/B configs + recall/precision@k on user data
- **Downstream Fit** — prompt-budget + lost-in-the-middle check
- **Recommendation & Re-tune Triggers**

## Verification

- [ ] Chunk method/size/overlap are tied to document type and query type, not defaulted.
- [ ] Chunks fit the embedder's max sequence length (no silent truncation).
- [ ] Structural context (headings) is preserved and metadata is attached for filtering/citation.
- [ ] The chosen config is proven via A/B on a retrieval eval set with recall/precision@k.
- [ ] Downstream prompt-budget and lost-in-the-middle effects are checked.
- [ ] No "optimal size" is asserted without evaluation on the user's data.

## False-Positive Prevention

❌ **DON'T:**
- Default to "512 tokens, 50 overlap" for every corpus — optimal chunking is document- and query-dependent.
- Use fixed-size splitting on structured docs and sever sections, tables, or sentences mid-way.
- Maximize chunk size to "capture more context" — large chunks dilute the embedding and crowd the prompt.
- Strip heading/section context, leaving retrieved chunks ambiguous and uncitable.

✅ **DO:**
- Profile documents and queries first, then pick the method that respects structure.
- Keep chunks within the embedder's max sequence length and preserve heading context.
- A/B candidate configs on a labeled retrieval set and let recall/precision decide.
- Re-check that the chosen chunking fits the generation prompt budget and position sensitivity.

## Example Output

```markdown
## Chunking Strategy: Product Documentation RAG

### Document & Query Profile
Markdown docs with deep heading hierarchy; tables of config options. Queries: 70% factoid
("default timeout?"), 20% how-to (multi-step), 10% comparison.

### Method Choice
Structure-aware by heading (H2/H3 boundaries). Fixed-size rejected: it severed config tables
and lost heading context, producing uncitable fragments.

### Size/Overlap Plan
Start: target ~350 tokens, split at H3, 15% overlap; tables kept whole as one chunk regardless
of size. Marked tunable — A/B 250 / 350 / 500.

### Structure & Metadata
Prepend "Doc > H2 > H3" path to each chunk. Metadata: doc_id, heading_path, version, last_updated.

### Evaluation Plan & Results (recall@5 on 100-query set)
| Config | recall@5 | precision@5 |
|---|---|---|
| 250/struct | 0.86 | 0.71 |
| 350/struct | 0.90 | 0.68 |  <- chosen
| 500/struct | 0.91 | 0.58 (dilution) |

### Downstream Fit
350-token chunks x top-5 = ~1.75k tokens context; well within budget. No lost-in-the-middle at k=5.

### Recommendation & Re-tune Triggers
350-token structure-aware + whole-table chunks. Re-tune if API-reference docs (denser tables) are added.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** size/overlap/method weighed against doc and query type.
- **DS-02 (Metric Specification):** chunking decided by recall/precision@k on a labeled set.
- **CM-02 (Constraint Specification):** embedder max-seq and prompt budget bound the choices.
- **QA-12 (False Positives Identification):** guards against default-size and max-size fallacies.
- **ST-02 (Structured Sequential Instructions):** profile → method → size → metadata → eval.

**Related Prompts:**
- `genai_rag_system_design.md` — the system this chunking feeds.
- `genai_embedding_model_selection.md` — chunk size and embedder max-seq interact.
- `genai_rag_retrieval_quality_debug.md` — diagnoses right-doc/wrong-fragment failures chunking fixes.
