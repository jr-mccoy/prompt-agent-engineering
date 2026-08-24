---
title: "RAG Retrieval Quality Debug"
category: AI-ML/genai-llm-engineering
description: "Root-cause a RAG system's bad answers by isolating the failing stage — retrieval, chunking, generation, or grounding — using a decision tree and stage-by-stage evidence rather than guesswork."
techniques:
  - RT-10
  - RT-09
  - ST-02
  - RT-05
  - QA-12
difficulty: advanced
tags:
  - rag
  - debugging
  - retrieval
  - grounding
  - root-cause
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_evaluation_harness.md
  - domain-AI-ML/genai-llm-engineering/genai_chunking_strategy.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
---

# RAG Retrieval Quality Debug

**Objective:** Given a RAG system producing wrong, incomplete, or hallucinated answers, isolate which stage is responsible — retrieval (wrong/missing context), chunking (right document, wrong fragment), generation (good context, bad answer), or grounding (answer ignores or contradicts context) — by running a decision tree against actual traces, so the fix targets the real cause instead of the most visible symptom.

**When to Use:**
- A specific set of queries returns wrong, partial, or fabricated answers.
- Your eval harness flagged a quality drop and you need to localize it.
- You're tempted to "just swap the model" or "raise top-k" and want to confirm the cause first.

**When NOT to Use:**
- You haven't built any measurement yet (start with `genai_rag_evaluation_harness.md`).
- The architecture itself is undecided (use `genai_rag_system_design.md`).

## Inputs / Context

Provide what you can; each missing piece becomes a probe to run:
- **Failing examples** — the query, the answer produced, and the expected answer.
- **Retrieval trace** — what chunks were retrieved (text + scores + source) for each failing query.
- **Prompt sent to the model** — the assembled context + instruction (after retrieval/reranking).
- **System config** — embedding model, chunking, top-k, reranker, generation model & version (ask if unspecified).
- **Pattern** — do failures cluster (a topic, query type, document set) or look random?

## Constraints

**Must:**
- Inspect the retrieval trace before blaming the model — most "hallucinations" are actually retrieval misses.
- Follow the decision tree: confirm whether the *gold* context was retrievable, retrieved, and present in the prompt before evaluating generation.
- Tie each diagnosis to evidence from the actual trace, not to a general failure mode.

**Must Not:**
- Recommend swapping the generation model as a first move without ruling out retrieval and grounding.
- Conclude "chunking is the problem" without showing the relevant info was split or buried.
- Invent what the retriever returned — if the trace is missing, list capturing it as the first action.

**Instructions:**

1. **Reproduce and classify the failure.** For each failing example, record query, produced answer, expected answer, and whether the answer is wrong-fact, incomplete, fabricated, or contradicts the provided context. Note any clustering.

2. **Check retrievability (ceiling test).** Does the gold passage exist in the corpus and could *any* query retrieve it? Manually search the index for the gold passage. If it's not findable, the problem is upstream (chunking/indexing/embedding), not generation.

3. **Check retrieval (was it fetched?).** In the trace, did the gold chunk appear in the top-k at all? If it ranked below the cutoff, it's a ranking/embedding/hybrid-weight issue. If absent entirely, an indexing or query-mismatch issue.

4. **Check chunking (right doc, wrong fragment?).** If the right document was retrieved but the answer-bearing sentence was split across chunks, truncated, or stripped of its heading/context, route to chunking (cross-link `genai_chunking_strategy.md`).

5. **Check prompt assembly (did it reach the model?).** Confirm the gold chunk survived reranking, dedup, and context-budget truncation and was actually in the prompt — and where (lost-in-the-middle). Cross-link `genai_context_window_strategy.md`.

6. **Check generation & grounding.** If the gold context was present and correct but the answer is still wrong: is the answer unsupported by context (grounding/instruction failure) or a reasoning error (model capability)? Distinguish "ignored the context" from "couldn't synthesize it."

7. **Localize and prescribe.** Output the single most likely failing stage per failure cluster, the evidence, and the targeted fix — plus the cheapest confirming experiment for each.

**Output Format:**

A markdown debug report:
- **Failure Inventory** — table: Query | Produced | Expected | Failure type | Cluster
- **Decision-Tree Trace** — per cluster: retrievability → retrieval → chunking → assembly → generation, with the verdict and evidence at the stage that fails
- **Root Cause(s)** — the failing stage(s), ranked by how many failures they explain
- **Targeted Fixes** — fix + confirming experiment per root cause
- **Ruled-Out Stages** — what you checked and cleared (so it isn't re-litigated)

## Verification

- [ ] The retrieval trace was inspected before any generation-side conclusion.
- [ ] Each diagnosis cites evidence from the actual trace, not a generic failure mode.
- [ ] The decision tree was followed in order (retrievability → retrieval → chunking → assembly → generation).
- [ ] "Hallucination" verdicts distinguish ungrounded answers from genuine retrieval misses.
- [ ] Each root cause has a cheap confirming experiment attached.
- [ ] Stages that were checked and cleared are listed.

## False-Positive Prevention

❌ **DON'T:**
- Call an answer a "hallucination" when the trace shows the gold context was never retrieved — that's a retrieval miss.
- Raise top-k as a reflex; more context can dilute precision and worsen lost-in-the-middle.
- Blame the embedding model when the query and documents simply use different vocabulary (a hybrid/sparse or query-rewrite fix).
- Swap to a bigger model before confirming the right context was even in the prompt.

✅ **DO:**
- Run the ceiling test: confirm the gold passage is retrievable at all before judging anything else.
- Separate "context absent" (retrieval/chunking) from "context present but ignored" (grounding) from "context present, reasoning failed" (generation).
- Attach a cheap confirming experiment to each root cause (e.g., inject gold chunk manually and re-ask).
- Look for clustering — random failures and topic-clustered failures have different causes.

## Example Output

```markdown
## RAG Debug: "What's our refund window for enterprise?" returns wrong answer

### Failure Inventory
| Query | Produced | Expected | Type | Cluster |
|---|---|---|---|---|
| enterprise refund window | "30 days" | "90 days (enterprise)" | wrong-fact | enterprise-policy |
| enterprise SLA credits | fabricated | per contract table | fabricated | enterprise-policy |

### Decision-Tree Trace (enterprise-policy cluster)
- Retrievability: gold section "Enterprise Terms > Refunds" EXISTS and is findable by keyword. ✓
- Retrieval: top-5 returned the *consumer* refund chunk (score 0.71); enterprise chunk ranked #9 (0.63). ✗ FAILS HERE
- (downstream not reached — fix retrieval first)

### Root Cause
Retrieval ranking: enterprise and consumer refund language are near-duplicates; dense
similarity favors the more common consumer phrasing. Affects all enterprise-policy queries.

### Targeted Fixes
- Add hybrid BM25 weighting so the literal token "enterprise" boosts the right chunk.
  Confirming experiment: re-run the 2 queries with hybrid on; expect enterprise chunk into top-3.
- Add `audience` metadata filter when the query names a tier.

### Ruled-Out Stages
- Generation/grounding: not reached — given the wrong chunk, a "30 days" answer is faithful, not hallucinated.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** the retrievability → generation tree drives diagnosis.
- **RT-09 (Root Cause Explanation):** each failure is traced to its originating stage.
- **ST-02 (Structured Sequential Instructions):** stages are checked in a fixed, dependency-respecting order.
- **RT-05 (Evidence-Based Reasoning):** verdicts cite the actual retrieval trace.
- **QA-12 (False Positives Identification):** separates true hallucination from retrieval miss.

**Related Prompts:**
- `genai_rag_evaluation_harness.md` — build the measurement that surfaces failures to debug.
- `genai_chunking_strategy.md` — fix right-doc/wrong-fragment failures.
- `genai_rag_system_design.md` — revisit the architecture if failures are systemic.
