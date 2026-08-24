---
title: "Graph Link Prediction Design"
category: AI-ML/specialized-ml/graph-ml
description: "Frame a link-prediction task on a graph — define what an edge means, choose a negative-sampling strategy, pick transductive vs inductive (and temporal) splits, and select ranking metrics — without leaking future edges into training."
techniques:
  - ST-02
  - RT-02
  - QA-12
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - graph-ml
  - link-prediction
  - negative-sampling
  - inductive-split
  - ranking-metrics
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/graph-ml/graphml_task_framing.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_fraud_graph_patterns.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_gnn_scalability.md
---

# Graph Link Prediction Design

**Objective:** Help a practitioner turn a vague "predict which nodes connect" goal into a rigorously specified link-prediction problem. The hard part is rarely the model — it is defining what an edge means, generating honest negative examples, splitting the graph so that no test edge is visible during message passing, and choosing ranking metrics that reflect the real decision. This prompt walks through edge semantics, negative sampling, split strategy (transductive / inductive / temporal), and evaluation so the reported numbers survive contact with production rather than collapsing once trivial leakage is removed.

**When to Use:**
- You are predicting whether (or how likely) two nodes form an edge: recommendations, knowledge-graph completion, social connections, molecule interactions.
- Your graph evolves over time and you need a split that respects edge timestamps.
- Your offline AUC looks suspiciously high and you suspect the evaluation, not the model.

**When NOT to Use:**
- You are classifying nodes or whole graphs rather than edges — that is node/graph classification, framed in `graphml_task_framing.md`.
- Your task is anomaly/fraud detection on a heterogeneous graph where labels are scarce and adversarial — use `graphml_fraud_graph_patterns.md`.
- Your bottleneck is fitting a large graph in memory or training throughput — use `graphml_gnn_scalability.md`.

## Inputs / Context

Provide what you can:
- **Graph definition** — node types, edge types, whether the graph is directed/heterogeneous, and rough scale (|V|, |E|).
- **Edge semantics** — what "an edge exists" means and whether edges have timestamps or weights.
- **Prediction target** — new-edge prediction, missing-edge completion, or ranking candidate edges for a query node.
- **Temporality** — does the graph grow over time, and do you have edge creation times?
- **Node coverage at inference** — will you score edges only between nodes seen in training (transductive) or also unseen nodes (inductive)?
- **Candidate set** — for each query, the universe of candidate targets you actually rank in production.
- **Decision use** — top-K recommendation, threshold-based link suggestion, or full-ranking retrieval.

## Constraints

**Must:**
- Define edge semantics and the positive/negative example construction before discussing any model.
- Choose a split strategy (transductive, inductive, or temporal) explicitly and state which edges are removed from the message-passing graph at evaluation.
- Tie metric choice (Hits@K, MRR, AUC, PR-AUC) to the production decision and candidate-set size.
- State the negative-sampling strategy and how negatives are matched between training and evaluation.

**Must Not:**
- Allow test/validation edges to remain in the training graph used for message passing (future-edge leakage).
- Treat random negatives as sufficient when production candidates are non-uniform — report only AUC without a ranking metric.
- Fabricate metric/benchmark numbers from memory; reason from the user's graph and mark unknowns — measure on your graph.
- Assume a transductive split when the production system must score unseen nodes.

**Instructions:**

1. **Pin down edge semantics.** Establish what a positive edge is (observed interaction? confirmed relation?), whether it is directed, and whether duplicates/weights matter. Ambiguity here corrupts every downstream choice.
2. **Decide the prediction framing.** Distinguish "will this specific edge form" (binary) from "rank candidate targets for a query node" (ranking). The framing drives metrics and negative sampling.
3. **Design the split.** Choose transductive (same nodes, held-out edges), inductive (held-out nodes), or temporal (train on edges before time t, test after). Make the message-passing graph contain only edges visible at training time — explicitly remove evaluation edges.
4. **Construct negatives.** Pick random negatives, degree-matched negatives, or hard negatives (close-but-unconnected nodes). Match the production candidate distribution; mismatched negatives inflate AUC.
5. **Guard against leakage.** Verify no test edge participates in any training-time aggregation, and that no feature encodes the future edge (e.g., a count that already includes the target link).
6. **Select metrics.** For ranking, prefer Hits@K and MRR computed over a realistic candidate set; report AUC and PR-AUC for binary framing but never as the sole number when the candidate set is non-uniform.
7. **Plan the baseline ladder.** Heuristics first (common neighbors, Adamic-Adar, preferential attachment), then a simple embedding, then a GNN — so any GNN gain is attributable, not assumed.
8. **Specify the evaluation protocol.** Fix the candidate set per query, the negative ratio, and seeds so results are reproducible and comparable across models.

**Output Format:**

A markdown design brief:
- **Task Framing** — edge semantics, directedness, binary vs ranking.
- **Split Strategy** — transductive/inductive/temporal, with the exact edge-removal rule.
- **Negative Sampling** — strategy, ratio, and train/eval matching.
- **Leakage Checklist** — concrete checks for future-edge and feature leakage.
- **Metrics** — chosen metrics, candidate-set definition, and why each fits the decision.
- **Baseline Ladder** — ordered baselines from heuristic to GNN.
- **Evaluation Protocol** — reproducibility settings and reporting template.
- **Open Questions** — unknowns to measure on the user's graph.

## Verification

- [ ] Edge semantics and positive/negative construction are defined before any model is named.
- [ ] The split strategy is chosen explicitly and the message-passing graph excludes evaluation edges.
- [ ] Negative-sampling strategy is stated and matched between training and evaluation.
- [ ] Metrics map to the production decision and candidate-set size (not AUC alone).
- [ ] A heuristic-to-GNN baseline ladder is specified for attribution.
- [ ] No metric or benchmark number is asserted from memory — all are marked "measure on your graph."

## False-Positive Prevention

❌ **DON'T:**
- Leave validation/test edges in the graph used for message passing — this **future-edge leakage** lets the model see the answer and inflates every metric.
- Use only random negatives and report a 0.98 AUC; trivial negatives make almost any model look perfect while production hard negatives crater it.
- Pick a transductive split when production must score brand-new nodes.
- Engineer features that secretly encode the target edge (e.g., a neighbor count computed after the edge was added).

✅ **DO:**
- Build a separate message-passing graph containing only training-time edges, and re-derive features from it.
- Sample hard negatives that resemble the real candidate distribution, and report a ranking metric (Hits@K / MRR) alongside AUC.
- Match the split to inference reality (inductive or temporal when nodes/time matter).
- Audit every feature for "could this only be known after the edge exists?"

## Example Output

```markdown
# Link Prediction Design — User→Item Recommendation

## Task Framing
- Edge = a confirmed purchase (directed user→item). Ranking task: rank items per user.

### Split Strategy
- Temporal: train on purchases before 2026-04-01; test on April purchases.
- Message-passing graph rebuilt from pre-April edges only; April edges removed.

### Negative Sampling
- Train: 4 degree-matched negatives per positive.
- Eval: rank true item against 200 in-catalog candidates per user (popularity-stratified).

### Leakage Checklist
- [ ] April edges absent from MP graph
- [ ] User-item co-purchase features recomputed pre-April only

### Metrics
- Primary: Hits@10, MRR over the 200-candidate set (matches top-10 carousel).
- Secondary: PR-AUC (class-imbalanced).

### Baseline Ladder
1. Popularity  2. Common-neighbors  3. Matrix factorization  4. GraphSAGE

### Open Questions
- Hard-negative ratio vs Hits@10 — measure on your graph.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered steps from edge semantics through evaluation protocol.
- **RT-02 (Multi-Dimensional Analysis Framework):** Frames the model as a link-prediction design reviewer.
- **QA-12 (False Positives Identification):** Dedicated leakage checklist for future edges and features.
- **CM-02 (Constraint Specification):** Hard Must/Must-Not rules on splits and negatives.
- **DS-06 (Prioritization & Severity Guidance):** Maps metric choice to the production decision and candidate set.

**Related Prompts:**
- `graphml_task_framing.md` — overall graph-ML framing and task selection.
- `graphml_fraud_graph_patterns.md` — link/anomaly modeling under extreme label scarcity.
- `graphml_gnn_scalability.md` — scaling the chosen GNN to large graphs.
