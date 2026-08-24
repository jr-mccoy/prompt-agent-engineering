---
title: "GraphRAG and Knowledge-Graph Retrieval Design"
category: AI-ML/genai-llm-engineering
description: "Decide whether graph-structured retrieval earns its construction and maintenance cost — identifying the query classes vector retrieval genuinely cannot serve, and designing extraction, traversal, and graph upkeep against those queries alone."
techniques:
  - RT-10
  - ST-02
  - RT-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - graphrag
  - knowledge-graph
  - multi-hop
  - entity-extraction
  - retrieval
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/genai-llm-engineering/genai_reranking_strategy.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_task_framing.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_evaluation_harness.md
---

# GraphRAG and Knowledge-Graph Retrieval Design

**Objective:** Determine whether graph-structured retrieval is justified for a corpus and design it if so — identifying the specific query classes that vector retrieval cannot serve, and building extraction, traversal, and maintenance against those classes rather than adopting a graph because the corpus contains entities.

**When to Use:**
- Queries require connecting facts across documents that no single passage contains.
- Answers need aggregation over a set defined by relationships, not by similarity.
- The corpus has strong, explicit entity-relationship structure that similarity search discards.

**When NOT to Use:**
- Queries are answerable from single passages — vector retrieval is far cheaper and a graph adds construction and maintenance cost for nothing.
- Entity extraction on this corpus is unreliable; a graph built on noisy extraction propagates errors into every traversal.
- The real problem is ranking or recall — use `genai_reranking_strategy.md` or `genai_vector_index_tuning.md`.

## Inputs / Context

- **Failing query examples** — real queries vector retrieval cannot answer, with the reason.
- **Corpus structure** — how explicit entities and relationships are in the text.
- **Entity and relation types** — what the graph would contain, and whether a schema exists.
- **Corpus update rate** — since graph maintenance cost scales with it and is the usually-underestimated cost.
- **Extraction quality achievable** — measured, not assumed.
- **Answer requirements** — whether answers need traversal paths, aggregations, or both.

## Constraints

**Must:**
- Justify the graph from **query classes vector retrieval provably cannot serve**, demonstrated on real failing queries. A corpus containing entities is not a reason; almost every corpus does.
- Measure entity and relation extraction quality before building — a graph is only as good as its extraction, and errors compound along traversal paths rather than staying local.
- Cost graph **maintenance**, not only construction. Incremental updates, entity resolution as new documents arrive, and schema drift are ongoing and routinely omitted from the business case.
- Design the hybrid: almost every real system needs both graph and vector retrieval, with a router deciding which serves a query.
- Evaluate on the query classes that motivated the graph, and separately confirm no regression on the queries vector retrieval already answered.

**Must Not:**
- Assert extraction accuracy, traversal-depth recommendations, or performance comparisons from memory; mark quantities `[measure on your corpus]`.
- Build a graph before demonstrating a query class that needs one.
- Ignore entity resolution — the same entity appearing under several surface forms fragments the graph and silently breaks traversal, producing confident wrong answers.
- Traverse unboundedly; deep traversal returns weakly-related context that degrades generation.
- Treat extraction errors as local; a wrong relation misroutes every path through it.

**Instructions:**

1. **Collect the failing queries and classify them.** For each query vector retrieval cannot answer, identify why:
   - *Multi-hop* — the answer requires linking facts across documents.
   - *Aggregation* — "how many", "which of these", over a relationship-defined set.
   - *Global/thematic* — requires synthesis across the corpus rather than a passage.
   - *Relationship-specific* — the query is about a connection, not a topic.
   Count them. If the count is small, the graph is not justified and the honest recommendation is to say so.

2. **Test whether cheaper fixes suffice.** Some apparent multi-hop queries are solved by better chunking, larger context windows, or query decomposition into several vector retrievals. Try these first — they are dramatically cheaper than a graph, and they resolve a meaningful share of apparent graph needs.

3. **Define the schema against those queries.** Entity types and relation types needed to answer the classified queries — nothing more. An open-ended extraction schema produces a large noisy graph that answers nothing better than vector search did.

4. **Measure extraction quality.** Precision and recall for entities and for relations, on a hand-labelled sample. State the achieved quality plainly: relation extraction is typically much weaker than entity extraction, and a traversal crossing three relations compounds those errors multiplicatively.

5. **Design entity resolution.** How the same entity under different surface forms is unified, and what happens on ambiguity. This is the single most common point of silent failure: unresolved duplicates fragment the graph, so traversals return nothing and the system answers confidently from whichever fragment it reached.

6. **Design traversal.** Maximum depth, relation types followed, and how results are ranked. Bound the depth — beyond a short path the retrieved context is only weakly related and actively degrades generation.

7. **Design the hybrid router.** Which query classes go to graph retrieval, which to vector, and which to both. Most queries will still be vector; the graph serves a minority well rather than replacing the pipeline.

8. **Cost construction and maintenance separately.** Initial extraction across the corpus, then per-update extraction, entity resolution against the existing graph, and periodic schema review. Maintenance is where graph projects fail, and it belongs in the decision.

9. **Evaluate on both sets.** The motivating query classes, and a control set of queries vector retrieval already answered, which must not regress.

**Output Format:**

A markdown design:
- **Failing Query Classification** — table: Class | Count | Example | Why vector fails.
- **Cheaper Fixes Tested** — table: Fix | Queries resolved | Sufficient?
- **Schema** — entity and relation types, tied to query classes.
- **Extraction Quality** — precision/recall for entities and relations; compounding note.
- **Entity Resolution** — method and ambiguity handling.
- **Traversal Design** — depth bound, relations followed, ranking.
- **Hybrid Router** — which queries go where.
- **Cost** — construction and maintenance, separately.
- **Evaluation** — motivating classes and control set.

## Verification

- [ ] The graph is justified by counted, classified failing queries.
- [ ] Cheaper fixes are tested and their coverage recorded before the graph is built.
- [ ] The schema is limited to what the motivating queries need.
- [ ] Extraction precision and recall are measured for entities and relations separately.
- [ ] Error compounding along traversal paths is stated.
- [ ] Entity resolution is designed, with ambiguity handling.
- [ ] Traversal depth is bounded with a stated reason.
- [ ] A hybrid router assigns query classes to retrieval modes.
- [ ] Maintenance cost is estimated separately from construction.
- [ ] A control set confirms no regression on previously-working queries.

## False-Positive Prevention

❌ **DON'T:**
- Build a knowledge graph because the corpus has entities — nearly every corpus does, and that fact justifies nothing.
- Skip the cheaper fixes; better chunking and query decomposition resolve a substantial share of apparent multi-hop needs at a fraction of the cost.
- Assume extraction quality; relation extraction is typically much weaker than entity extraction, and a three-hop traversal multiplies those error rates.
- Leave entity resolution undesigned — unresolved duplicates fragment the graph so traversals silently return nothing, and the system answers from a fragment with full confidence.
- Traverse deeply for more context; past a short path the results are weakly related and degrade the answer.
- Budget construction and forget maintenance; per-update extraction and re-resolution are where these projects quietly become unaffordable.

✅ **DO:**
- Collect and count real failing queries, and let a small count end the proposal.
- Exhaust chunking, context-window, and decomposition fixes first.
- Constrain the schema to the motivating query classes.
- Measure extraction on a hand-labelled sample and state the compounding effect explicitly.
- Design entity resolution as a first-class component with defined ambiguity handling.
- Route most queries to vector retrieval and let the graph serve the minority it is built for.

## Example Output

```markdown
## GraphRAG Assessment: Corporate Compliance Knowledge Base
Policies, contracts, regulatory correspondence, org records.

### Failing Query Classification
Collected 90 queries the current RAG cannot answer:
| Class | Count | Example | Why vector fails |
|---|---|---|---|
| **Multi-hop** | 34 | "which vendors are covered by the policy that Legal updated in Q2?" | needs policy→vendor→contract links across documents |
| **Aggregation** | 21 | "how many contracts reference the superseded clause?" | needs a count over a relationship-defined set |
| Global/thematic | 18 | "summarize our data-retention posture" | needs corpus-wide synthesis |
| Relationship-specific | 17 | "who approved the exception for this supplier?" | the answer is an edge, not a topic |

Multi-hop and aggregation together account for the majority — a real, countable justification
rather than an intuition that a graph would help.

### Cheaper Fixes Tested — before building anything
| Fix | Queries resolved | Sufficient? |
|---|---|---|
| Larger chunks with section context | `[measure]` | `[assess]` |
| Query decomposition into sequential vector retrievals | `[measure — expect meaningful share of multi-hop]` | `[assess]` |
| Metadata filters on document type and date | `[measure — expect share of aggregation]` | `[assess]` |

Query decomposition in particular resolves many apparent multi-hop questions by retrieving twice.
Whatever these three resolve is subtracted from the graph's justification; building a graph for
queries decomposition already handles would be paying construction and maintenance for nothing.

### Schema — constrained to the remaining query classes
| Entity types | Relation types |
|---|---|
| Policy, Contract, Vendor, Person, Regulation, Clause | supersedes, references, approved_by, applies_to, owned_by |

Nothing beyond what the remaining classes require. An open-ended schema would produce a large,
noisy graph that answers these queries no better than vector search already does.

### Extraction Quality
| Target | Precision | Recall |
|---|---|---|
| Entities | `[measure]` | `[measure]` |
| **Relations** | `[measure — expect materially lower]` | `[measure]` |

**Compounding:** a three-hop traversal crosses three relations, so path reliability is roughly
the product of three relation precisions, not any one of them. This is why relation extraction
quality, not entity extraction quality, governs whether deep traversal is usable at all — and it
is the number to check before promising multi-hop answers.

### Entity Resolution
"Acme Corp", "Acme Corporation", and "ACME" must resolve to one vendor node. Method:
normalization plus embedding similarity, with a review queue above an ambiguity threshold rather
than an automatic merge. **Unresolved duplicates are the silent killer here** — the graph
fragments, traversal returns nothing, and the system answers confidently from whichever fragment
it landed in, with no signal that half the evidence was on the other node.

### Traversal Design
Maximum depth **2**, justified by the compounding above: at depth 3 the path reliability falls
below what the answer quality can tolerate. Relations followed depend on the query class —
`supersedes` and `references` for clause questions, `applies_to` and `owned_by` for coverage
questions. Results ranked by path reliability, not path length.

### Hybrid Router
| Query class | Route |
|---|---|
| Single-fact lookup (**expected majority of traffic**) | vector only |
| Multi-hop | graph traversal + vector for supporting passages |
| Aggregation | graph query |
| Thematic | vector with a wide window; graph adds little here |

The graph serves a minority of traffic well. It does not replace the pipeline, and a design that
routes everything through it would be slower and worse on the common case.

### Cost
| Phase | Cost |
|---|---|
| Initial extraction over the corpus | `[estimate]` |
| **Per-update extraction** | `[estimate]` — ongoing |
| **Entity resolution against the existing graph** | `[estimate]` — ongoing, grows with graph size |
| Schema review as new document types arrive | periodic |

Maintenance, not construction, is the line item that decides this. A graph built once and left to
drift answers worse than vector retrieval within a few quarters.

### Evaluation
- **Motivating classes** (multi-hop, aggregation): accuracy before and after.
- **Control set**: queries vector retrieval already answered — **must not regress**. Routing
  changes can silently degrade the common case while the headline multi-hop numbers improve.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** the failing-query class routes to cheaper fixes or to graph construction.
- **ST-02 (Structured Sequential Instructions):** justification and cheaper fixes precede schema design, so the graph is built only against a demonstrated need.
- **RT-02 (Multi-Dimensional Analysis Framework):** query class × retrieval mode × cost is the routing and justification grid.
- **CM-02 (Constraint Specification):** the schema-constrained-to-queries and bounded-traversal rules bound the design.
- **QA-12 (False Positives Identification):** rejects entity presence as justification and surfaces entity-resolution fragmentation as silent failure.

**Related Prompts:**
- `genai_rag_system_design.md` — the vector pipeline this augments rather than replaces.
- `genai_query_rewriting_expansion.md` — decomposition, the cheaper fix for many multi-hop queries.
- `../specialized-ml/graph-ml/graphml_task_framing.md` — when the graph itself is the modelling target.
- `genai_rag_evaluation_harness.md` — where the motivating-class and control-set evaluations live.
