---
title: "Query Rewriting and Expansion"
category: AI-ML/genai-llm-engineering
description: "Improve retrieval by transforming the query before it reaches the index — diagnosing which failure the rewriting must fix, choosing among expansion, decomposition, and hypothetical-document techniques, and measuring retrieval rather than end-answer quality."
techniques:
  - RT-10
  - DS-02
  - CM-02
  - QA-12
  - RT-02
difficulty: advanced
tags:
  - query-rewriting
  - query-expansion
  - retrieval
  - rag
  - multi-turn
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_retrieval_quality_debug.md
  - domain-AI-ML/genai-llm-engineering/genai_reranking_strategy.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_evaluation_harness.md
  - domain-AI-ML/genai-llm-engineering/genai_vector_index_tuning.md
---

# Query Rewriting and Expansion

**Objective:** Fix retrieval failures that originate in the query rather than the index — diagnosing which specific failure mode applies, choosing the transformation that addresses it, and measuring the change in *retrieval* quality before crediting it with any improvement in answers.

**When to Use:**
- Retrieval misses documents that a human searcher would obviously find with a rephrased query.
- Multi-turn conversations break retrieval because follow-up queries are not self-contained.
- Users write short, ambiguous, or jargon-mismatched queries and the index is fine.

**When NOT to Use:**
- Retrieval fails because the content is not in the index — no rewriting recovers a missing document.
- The problem is ranking among retrieved candidates — use `genai_reranking_strategy.md`.
- The index or embedding configuration is the issue — use `genai_vector_index_tuning.md`.

## Inputs / Context

- **Failure examples** — real queries that retrieve the wrong thing, with what should have been retrieved.
- **Query characteristics** — length, whether multi-turn, jargon or entity density, language.
- **Corpus characteristics** — vocabulary, and whether it uses different terminology from users.
- **Retrieval setup** — dense, sparse, or hybrid; each responds differently to rewriting.
- **Latency budget** — rewriting adds a model call before retrieval begins.
- **Retrieval metrics currently measured** — recall@k and any ranking metric, without which improvement is unmeasurable.

## Constraints

**Must:**
- Diagnose the specific query-side failure before choosing a technique — vocabulary mismatch, under-specification, multi-intent, missing conversational context, or entity ambiguity all look alike in an end-to-end metric and need different fixes.
- Measure **retrieval quality** (recall@k, ranking of the known-correct document) separately from answer quality; a rewriting that improves answers via a lucky generation is not a retrieval improvement and will not generalize.
- State the latency and cost added, since rewriting inserts a model call on the critical path before retrieval starts.
- Preserve the original query as a fallback and measure the union of original and rewritten retrieval, since rewriting can lose the one good result the original found.
- Check that rewriting does not change the user's intent — an expansion that drifts is worse than no expansion.

**Must Not:**
- Assert retrieval-improvement figures or technique-comparison results from memory; mark quantities `[measure on your corpus]`.
- Apply rewriting to fix a missing-content problem; the ceiling is what the index contains.
- Evaluate only end-to-end answer quality — the generator can mask a retrieval regression, and the improvement then vanishes when the generator changes.
- Expand every query indiscriminately; short precise entity queries are usually hurt by expansion.
- Let a rewriter hallucinate entities or constraints the user did not state.

**Instructions:**

1. **Classify the failure from real examples.** For each failing query, determine why the right document was not retrieved:
   - *Vocabulary mismatch* — user words differ from corpus words.
   - *Under-specification* — the query is too short to be discriminative.
   - *Multi-intent* — one query needs several different documents.
   - *Missing conversational context* — a follow-up that is meaningless standalone.
   - *Entity ambiguity* — the query term denotes several things.
   Count the distribution; the largest class determines what to build.

2. **Match the technique to the failure.**
   - *Synonym / terminology expansion* — vocabulary mismatch. Cheap; can be a static mapping rather than a model call.
   - *Query decomposition* — multi-intent. Produces several retrievals to merge.
   - *Conversational rewriting* — resolves references into a self-contained query. Usually the highest-value fix in chat.
   - *Hypothetical document generation* — write a passage that would answer the query and embed that instead; helps under-specification in dense retrieval.
   - *Entity disambiguation* — add context or ask the user.

3. **Decide where rewriting applies.** Not all queries need it. Define the condition — length, turn index, detected ambiguity — under which rewriting runs, so precise queries are left alone.

4. **Design the fallback and the union.** Retrieve with both original and rewritten query and merge, unless measurement shows the rewritten alone is strictly better. This protects against the rewriter losing the one correct result.

5. **Guard intent preservation.** Constrain the rewriter against adding entities, constraints, or assumptions the user did not express. Include an evaluation slice specifically for drift, since a fluent rewrite that changes the question is the failure mode a general metric hides.

6. **Measure retrieval, not answers.** Recall@k and rank of the known-correct document, before and after, on the failure classes identified in step 1 and on a control set of previously-working queries. The control set catches regressions on queries that were already fine.

7. **Price the latency.** Rewriting is a model call before retrieval, so its latency is fully on the critical path. Report the added p50 and p99, and consider a smaller model or a cached static mapping where the failure is vocabulary mismatch.

8. **Decide the failure behaviour.** If the rewriter errors or times out, retrieval proceeds with the original query rather than failing.

**Output Format:**

A markdown design:
- **Failure Classification** — table: Failure class | Count | Example.
- **Technique Selection** — table: Failure class | Technique | Cost | Why.
- **Application Condition** — when rewriting runs and when it does not.
- **Fallback & Union** — retrieval merge strategy.
- **Intent-Drift Guard** — constraints and the drift evaluation slice.
- **Retrieval Measurement** — table: Query set | Recall@k before | after | Rank change.
- **Latency Impact** — added p50/p99 on the critical path.
- **Failure Behaviour** — rewriter unavailable.

## Verification

- [ ] Failures are classified from real examples with counts per class.
- [ ] Each technique addresses a specific classified failure.
- [ ] An application condition prevents indiscriminate rewriting.
- [ ] Original-query fallback and union retrieval are specified.
- [ ] An intent-drift guard and its evaluation slice exist.
- [ ] Retrieval metrics are measured before and after, including a control set.
- [ ] Added latency is reported at p50 and p99.
- [ ] Failure behaviour degrades to the original query.
- [ ] No improvement figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Add query rewriting because retrieval is poor without diagnosing why — the five failure classes need different fixes and a generic rewriter addresses none of them well.
- Measure only end-answer quality; a strong generator can paper over a retrieval regression, which then reappears the moment the generator is changed.
- Expand short precise queries — a specific product code or error identifier is usually made worse by adding terms.
- Ship a rewriter that can introduce entities the user never mentioned; a fluent rewrite of a different question retrieves confidently and wrongly.
- Replace the original query entirely without checking that the rewrite never loses a result the original found.
- Ignore that rewriting sits before retrieval, so its latency is not overlappable with anything.

✅ **DO:**
- Classify real failures and let the largest class decide what to build.
- Use the cheapest technique that addresses the class — a static synonym map beats a model call for vocabulary mismatch.
- Gate rewriting on a condition so precise queries pass through untouched.
- Retrieve with both queries and merge until measurement justifies dropping one.
- Evaluate intent drift as its own slice.
- Report recall@k on both failure and control sets, and the latency the user actually pays.

## Example Output

```markdown
## Query Rewriting: Internal Engineering Knowledge Base

### Failure Classification
Sampled 120 queries where the known-correct document was not in the top 10:
| Failure class | Count | Example |
|---|---|---|
| **Missing conversational context** | 44 | "what about for staging?" (turn 3) |
| Vocabulary mismatch | 31 | user "deploy stuck" vs docs "rollout pending" |
| Under-specification | 22 | "auth error" |
| Multi-intent | 14 | "how do I rotate creds and update the runbook" |
| Entity ambiguity | 9 | "the gateway" (three services share the word) |

Conversational context is the largest class by a clear margin, so it gets built first. A generic
"add an LLM rewriter" approach would have spread effort across all five and fixed none properly.

### Technique Selection
| Failure class | Technique | Cost | Why |
|---|---|---|---|
| Conversational context | LLM rewrite to a self-contained query using prior turns | 1 model call | only reliable fix; the query is genuinely incomplete |
| Vocabulary mismatch | **Static terminology map** (user term → doc term) | negligible | corpus vocabulary is stable and small; a model call would be waste |
| Under-specification | Hypothetical document generation | 1 model call | dense retrieval; short queries embed poorly |
| Multi-intent | Decomposition into sub-queries, merge results | 1 model call | needs several documents |
| Entity ambiguity | Add workspace/team context from session metadata | negligible | disambiguates without asking the user |

Two of five classes are fixed without any model call — worth finding before adding latency.

### Application Condition
Rewriting runs when **any** of: turn index > 1; query length below a threshold; a detected
ambiguous entity. Otherwise the query goes straight to retrieval. Precise queries — error codes,
exact filenames — bypass rewriting entirely, since expansion reliably degrades them.

### Fallback & Union
Retrieve with **both** the original and the rewritten query; merge and deduplicate before
ranking. Measured `[measure]` whether rewritten-only ever loses a correct result the original
found. Only if it never does should the union be dropped for latency.

### Intent-Drift Guard
The rewriter is constrained to resolve references and add terminology **only from prior turns or
the session context** — it may not introduce entities, constraints, or scope the user has not
expressed. A dedicated drift evaluation slice of 50 multi-turn cases is judged on "does the
rewrite ask the same question?", separately from whether retrieval improved. A fluent rewrite of
a subtly different question is invisible in recall@k against the wrong gold document.

### Retrieval Measurement
| Query set | Recall@10 before | after | Median rank change |
|---|---|---|---|
| Conversational failures (n=44) | `[measure]` | `[measure]` | `[measure]` |
| Vocabulary failures (n=31) | `[measure]` | `[measure]` | `[measure]` |
| Under-specified (n=22) | `[measure]` | `[measure]` | `[measure]` |
| **Control: previously working (n=200)** | `[measure]` | `[measure]` | **must not regress** |

The control set is the one that catches an expansion strategy that helps failures and quietly
damages the queries that already worked.

### Latency Impact
Rewriting is **before** retrieval, so it is fully on the critical path and cannot overlap with
anything. Added p50 `[measure]`, p99 `[measure]`. Because the two static techniques need no model
call, only the conditions that trigger LLM rewriting pay this cost — which is why the application
condition matters for latency as well as quality.

### Failure Behaviour
Rewriter error or timeout → retrieve with the original query. Retrieval never blocks on the
rewriter; a degraded retrieval beats a failed request.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** the classified failure routes to the technique that addresses it.
- **DS-02 (Metric Specification):** retrieval metrics are specified separately from answer quality as the measure of success.
- **CM-02 (Constraint Specification):** the intent-preservation and original-query-fallback rules bound the rewriter.
- **QA-12 (False Positives Identification):** the control set and drift slice reject improvements that are regressions elsewhere.
- **RT-02 (Multi-Dimensional Analysis Framework):** failure class × technique × cost × latency is the selection grid.

**Related Prompts:**
- `genai_rag_retrieval_quality_debug.md` — diagnosing whether the problem is query-side at all.
- `genai_reranking_strategy.md` — improving order among retrieved candidates.
- `genai_vector_index_tuning.md` — when the index rather than the query is the constraint.
- `genai_rag_evaluation_harness.md` — the harness these retrieval measurements belong in.
