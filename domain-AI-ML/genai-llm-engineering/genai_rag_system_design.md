---
title: "RAG System End-to-End Design"
category: AI-ML/genai-llm-engineering
description: "Design a retrieval-augmented generation system across ingestion, chunking, retrieval, reranking, prompt assembly, and grounded citation — with an evaluation plan baked into the design."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - rag
  - retrieval
  - grounding
  - system-design
  - citations
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_evaluation_harness.md
  - domain-AI-ML/genai-llm-engineering/genai_chunking_strategy.md
  - domain-AI-ML/genai-llm-engineering/genai_embedding_model_selection.md
---

# RAG System End-to-End Design

**Objective:** Produce a concrete, end-to-end design for a retrieval-augmented generation system — covering ingestion, chunking, embedding, indexing, retrieval, reranking, prompt assembly, generation, and grounded citation — with the key tradeoffs made explicit and an evaluation plan attached so the design can be verified rather than assumed.

**When to Use:**
- You are building a new RAG application and need a defensible architecture before writing code.
- An existing RAG prototype works in demos but you need to harden each stage for production.
- You must justify component choices (chunker, embedder, vector store, reranker) to a reviewer.

**When NOT to Use:**
- The task is a one-off Q&A over a small static document that fits in the context window — just put it in context (see `genai_context_window_strategy.md`).
- You only need to *debug* an existing RAG system's bad answers (use `genai_rag_retrieval_quality_debug.md`).
- You only need to *evaluate* a built system (use `genai_rag_evaluation_harness.md`).

## Inputs / Context

State the target model + provider and version up front; design choices depend on it. Provide what you can:
- **Corpus profile** — document types, volume, update frequency, structure (PDFs, HTML, tables, code), and language(s).
- **Query profile** — expected question types (factoid, multi-hop, summarization, comparison), volume, latency SLA.
- **Grounding requirement** — must answers cite sources? Is "I don't know" acceptable? Regulatory/audit needs?
- **Generation model** — name, version, context window, cost per token.
- **Constraints** — budget, latency, on-prem vs hosted, existing vector store, privacy/PII rules.

## Constraints

**Must:**
- Make each stage decision explicit with its rationale and the alternative rejected.
- Define grounding/citation behavior precisely — what gets cited, at what granularity, and how unsupported claims are prevented.
- Attach measurable acceptance criteria per stage (e.g., retrieval recall@k target) so the design is testable.

**Must Not:**
- Recommend a specific embedding model, vector DB, or reranker as "best" without tying it to the corpus/query/latency profile — defer the empirical pick to evaluation on the user's data.
- Invent benchmark numbers, MTEB scores, or latency figures from memory; mark unknowns as "measure on your data."
- Assume the LLM will refuse to hallucinate — grounding must be enforced by retrieval + prompt design + verification, not hope.

**Instructions:**

1. **Frame the retrieval contract.** Define what a "correct answer" requires from retrieval: how many relevant chunks, at what granularity, and the acceptable failure mode (miss vs. wrong-context). This contract governs every downstream choice.

2. **Design ingestion and normalization.** Specify how raw documents are parsed (layout-aware for PDFs/tables), cleaned, de-duplicated, and enriched with metadata (source, section, date, permissions) that retrieval and citation will rely on.

3. **Choose a chunking strategy with metadata.** Pick size/overlap and structure-awareness based on document type and query type; carry section/source metadata into each chunk. Defer final parameters to `genai_chunking_strategy.md` evaluation.

4. **Specify embedding + indexing.** State the embedding approach and index type (dense, sparse/BM25, hybrid) and why, given domain vocabulary and query style. Defer the empirical embedding pick to `genai_embedding_model_selection.md`.

5. **Design retrieval + reranking.** Define top-k, hybrid fusion, filters (metadata/permissions), and whether a cross-encoder reranker is justified by the precision requirement vs. its latency cost.

6. **Assemble the grounded prompt.** Specify how retrieved context is ordered, deduplicated, and budgeted into the context window; how citations are attached; and the instruction that forces the model to answer only from context and abstain when unsupported.

7. **Define the abstention + fallback path.** Specify behavior when retrieval returns nothing relevant, when context conflicts, and when the query is out of scope.

8. **Attach the evaluation plan.** For each stage, name the metric and target (retrieval recall@k, faithfulness/groundedness, answer quality) and the golden set needed — pointing to `genai_rag_evaluation_harness.md` for execution.

**Output Format:**

A markdown design document:
- **Retrieval Contract** — what correct retrieval must deliver
- **Architecture Diagram (textual)** — stage-by-stage flow
- **Stage Decisions Table** — Stage | Choice | Rationale | Alternative Rejected | Acceptance Metric
- **Grounding & Citation Spec** — granularity, abstention rules, anti-hallucination instruction
- **Failure & Fallback Paths** — no-hit, conflict, out-of-scope
- **Evaluation Plan** — metrics, targets, golden-set requirements
- **Open Questions / To Measure** — choices deferred to empirical testing

## Verification

- [ ] Target model + provider + version is stated and used to inform context-budget and cost choices.
- [ ] Every stage has an explicit choice, rationale, and rejected alternative.
- [ ] Grounding/citation behavior is specified at a concrete granularity, not "cite sources."
- [ ] Abstention and conflict-handling paths are defined, not assumed.
- [ ] Each stage carries a measurable acceptance criterion tied to evaluation.
- [ ] No fabricated benchmark/latency numbers; empirical picks are deferred to evaluation on the user's data.

## False-Positive Prevention

❌ **DON'T:**
- Declare a stack "production-ready" because it answers demo questions — demos rarely exercise multi-hop, out-of-scope, or conflicting-source queries.
- Pick a reranker or larger embedding model "for quality" without quantifying the latency/cost it adds versus the precision it buys.
- Assume citations make answers grounded — a model can cite a chunk and still assert claims the chunk doesn't support.
- Treat higher top-k as strictly better; more context can dilute precision and trigger lost-in-the-middle effects.

✅ **DO:**
- Define the retrieval contract first and let it justify k, reranking, and chunk size.
- Tie every component choice to the corpus/query profile and defer the final pick to evaluation on the user's data.
- Enforce grounding with an explicit answer-only-from-context instruction plus a faithfulness check, not citations alone.
- Budget the context window deliberately and test for position sensitivity (see `genai_context_window_strategy.md`).

## Example Output

```markdown
## RAG Design: Internal Policy Assistant (model: <provider/model vX>, 128k ctx)

### Retrieval Contract
Most questions are single-fact policy lookups; ~20% are multi-hop ("does policy A override B for contractors?").
Correct retrieval = the 1–3 governing policy sections in top-5. Worse to return a *wrong* policy than to miss.

### Stage Decisions
| Stage | Choice | Rationale | Rejected | Acceptance Metric |
|---|---|---|---|---|
| Ingestion | Layout-aware PDF parse + section metadata | Policies are nested headings; section is the citation unit | Plain text extract | 100% sections retain heading path |
| Chunking | Structure-aware by section, ~400 tokens, 15% overlap | Sections are self-contained | Fixed 1000-token | Eval per genai_chunking_strategy |
| Index | Hybrid (BM25 + dense) | Policy IDs/codes need lexical match | Dense only | recall@5 ≥ 0.9 on golden set |
| Rerank | Cross-encoder on top-20 → top-5 | Precision matters more than latency here | None | precision@5 ↑ vs no-rerank |
| Prompt | Ordered by rerank score, per-chunk citation tags, answer-only-from-context | Audit requires traceability | Concatenate raw | faithfulness ≥ 0.95 |

### Grounding & Citation Spec
- Citation granularity: section ID. Every claim sentence maps to ≥1 cited section.
- Abstention: if no chunk scores above threshold T, respond "Not covered in current policy set."
- Conflict: surface both sections and flag the conflict rather than silently choosing one.

### Evaluation Plan
Golden set: 120 questions (80 single-fact, 30 multi-hop, 10 out-of-scope). Metrics: recall@5,
faithfulness, answer correctness (rubric), abstention precision. See genai_rag_evaluation_harness.md.

### Open Questions / To Measure
- Embedding model: shortlist 3, run MTEB-style eval on our policy corpus (genai_embedding_model_selection).
- Optimal chunk size: A/B 300 vs 400 vs 600 tokens against recall@5.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the design walks ingestion → generation in fixed order.
- **RT-02 (Multi-Dimensional Analysis Framework):** each stage weighs quality vs latency vs cost.
- **CM-02 (Constraint Specification):** the retrieval contract and grounding rules govern all choices.
- **DS-02 (Metric Specification):** every stage carries a measurable acceptance criterion.
- **QA-01 (Self-Verification):** the design ships with its own evaluation plan.

**Related Prompts:**
- `genai_rag_evaluation_harness.md` — execute the evaluation plan this design attaches.
- `genai_chunking_strategy.md` — finalize chunk parameters empirically.
- `genai_embedding_model_selection.md` — pick the embedder on your own data.
