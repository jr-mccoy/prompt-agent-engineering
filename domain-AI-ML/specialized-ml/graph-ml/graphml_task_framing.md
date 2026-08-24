---
title: "Graph ML Task Framing"
category: AI-ML/specialized-ml/graph-ml
description: "Design a graph machine-learning approach — frame the task (node/edge/graph level), choose a GNN family, plan neighbor sampling for scale, and prevent the leakage that graph splits invite."
techniques:
  - ST-02
  - RT-02
  - QA-12
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - graph-ml
  - gnn
  - graph-splits
  - leakage
  - neighbor-sampling
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/graph-ml/graphml_link_prediction_design.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_fraud_graph_patterns.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_gnn_scalability.md
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_anomaly_outlier_detection.md
---

# Graph ML Task Framing

**Objective:** Design a graph machine-learning approach for relational data — correctly framing the prediction level (node / edge / graph), choosing a GNN family and depth, planning neighbor sampling for scale, and (most importantly) constructing splits and message-passing that do not leak label or structure information — while checking whether a non-graph model would do just as well.

**When to Use:**
- You have relational data (entities + relationships) and a prediction over nodes, edges, or whole graphs.
- A GNN underperforms a tabular baseline and you suspect the graph framing or sampling.
- Offline graph metrics look strong and you need to rule out graph-specific leakage.

**When NOT to Use:**
- The relationships add no signal and a tabular model on node features is enough (establish that first).
- The task is purely sequence/text/audio (use the relevant modality prompt).

## Inputs / Context

Provide what you can:
- **Graph definition** — what nodes and edges represent, directed/undirected, weighted, homogeneous vs heterogeneous (multiple node/edge types), static vs dynamic/temporal.
- **Prediction task** — node classification/regression, link/edge prediction, or graph-level prediction.
- **Scale** — node/edge counts, degree distribution, whether the graph fits in memory.
- **Features** — node/edge/graph features available; how informative alone (tabular baseline).
- **Temporal structure** — do edges/labels have timestamps (critical for split design).
- **Inductive vs transductive** — must the model generalize to unseen nodes/graphs?

## Constraints

**Must:**
- Establish a non-graph baseline (tabular on node features, or simple heuristics like common-neighbors for links) the GNN must beat.
- Design splits that prevent graph-specific leakage: target edges excluded from message passing, temporal order respected, no test-node information bleeding through neighbors.
- Match the GNN family and depth to the task level, heterogeneity, and over-smoothing risk.

**Must Not:**
- Use a random edge split for link prediction without removing test edges from the message-passing graph — that leaks the answer.
- Ignore temporal order in a dynamic graph (future edges informing past predictions).
- Invent graph statistics (degree, homophily) the user didn't provide; mark them to-measure.

**Instructions:**

1. **Frame the prediction level.** Decide node-level, edge/link-level, or graph-level, and state the exact target and what is observable at prediction time. This determines splits, sampling, and readout.

2. **Establish the non-graph baseline.** Define a tabular model on node/edge features and (for links) structural heuristics (common neighbors, Adamic-Adar). The GNN must beat these; if it can't, the graph structure isn't adding signal.

3. **Characterize the graph.** Homogeneous vs heterogeneous, directed, weighted, static vs temporal, degree distribution, and homophily (do connected nodes share labels). These drive family and depth.

4. **Choose the GNN family and depth.** Match to characteristics: convolutional/aggregation (homophilous), attention-based (variable neighbor importance), heterogeneous-graph variants (typed nodes/edges). Keep depth shallow (often 2–3 hops) to avoid over-smoothing; justify any deeper stack.

5. **Plan sampling and scale.** For large graphs, specify neighbor sampling / subgraph sampling / clustering to make training feasible, and confirm sampling doesn't systematically drop informative neighbors.

6. **Design leakage-safe splits — the critical step.** Node tasks: ensure test-node labels aren't reachable through message passing in transductive setups. Link prediction: remove target/test edges from the message-passing graph and sample negatives carefully (avoid trivial negatives). Temporal graphs: split by time and ensure features/messages use only past edges.

7. **Decide transductive vs inductive.** If unseen nodes/graphs must be scored at deployment, require an inductive method and an inductive evaluation (held-out nodes/graphs), not just transductive splits.

8. **Deliver the design + leakage audit.** Output the task frame, baseline, family/depth, sampling, the leakage-safe split protocol, and the ablations proving the graph earns its place.

**Output Format:**

A markdown report:
- **Task Frame** — level, target, observability.
- **Baseline & Justification** — non-graph baseline; must-beat threshold.
- **Graph Characterization** — type, homophily, scale (or to-measure).
- **GNN Family & Depth** — choice + rationale + over-smoothing note.
- **Sampling & Scale Plan** — for large graphs.
- **Leakage-Safe Split Protocol** — node/edge/temporal specifics.
- **Transductive vs Inductive** — decision + matching eval.
- **Ablation Plan** — graph-vs-tabular, depth, sampling.

## Verification

- [ ] The prediction level (node/edge/graph) and exact target are stated.
- [ ] A non-graph baseline is defined and the GNN is required to beat it.
- [ ] For link prediction, test edges are removed from the message-passing graph.
- [ ] Temporal graphs split by time; messages/features use only past edges.
- [ ] Transductive vs inductive is decided and the eval matches it.
- [ ] Over-smoothing is considered when choosing depth.
- [ ] Unprovided graph statistics are flagged as to-measure, not invented.

## False-Positive Prevention

❌ **DON'T:**
- Random-split edges for link prediction while leaving those edges in the graph the model passes messages over — the target is then visible to the model.
- Let test-node labels propagate through neighbors in a transductive node-classification split and call the result generalization.
- Use future edges to predict past links in a temporal graph.
- Stack many GNN layers assuming "deeper is better" — node representations over-smooth into uniformity.

✅ **DO:**
- Remove target/test edges from message passing and choose hard negatives for link prediction.
- Split temporal graphs by time and restrict messages to past edges.
- Compare against a tabular baseline to confirm structure adds real signal.
- Evaluate inductively (held-out nodes/graphs) when deployment sees unseen nodes.

## Example Output

```markdown
## Graph ML Design: Fraud Detection on Transaction Network

### Task Frame
Edge-level: predict whether a transaction (edge between account nodes) is fraudulent at the time it occurs. Observable: account features + past transactions only.

### Baseline & Justification
Tabular gradient-boosted model on account+transaction features: AUC 0.88 (measured). GNN must clear 0.88. Structural heuristic (shared-device common neighbors) AUC 0.71.

### Graph Characterization
Heterogeneous (accounts, devices, merchants), directed, temporal. Homophily: fraud clusters via shared devices. Scale: 40M nodes, 300M edges — does not fit in memory. (Degree distribution to-measure.)

### GNN Family & Depth
Heterogeneous attention-based GNN, 2 hops (device→account→merchant). Depth 2 to avoid over-smoothing across the dense device hubs.

### Sampling & Scale Plan
Temporal neighbor sampling: for each target edge, sample fixed-size neighborhoods using only edges with timestamp < target time. Cap high-degree hub fan-out.

### Leakage-Safe Split Protocol
- Split by time: train on months 1–9, test on 10–12.
- Message passing for a target edge uses ONLY earlier transactions — never the target or future edges.
- Negatives: real non-fraud transactions from the same period (not random node pairs).

### Transductive vs Inductive
Inductive required — new accounts appear daily. Eval on held-out future accounts/edges.

### Ablation Plan
1. GNN vs tabular (confirm structure adds ≥0.02 AUC).
2. 2-hop vs 3-hop (over-smoothing check).
3. With vs without temporal sampling restriction (confirms no future leakage).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** frame → baseline → characterize → family → sampling → split.
- **RT-02 (Multi-Dimensional Analysis Framework):** GNN family choice across homophily/heterogeneity/scale axes.
- **QA-12 (False Positives Identification):** core to catching link-prediction and temporal graph leakage.
- **CM-02 (Constraint Specification):** prediction-time edge availability as the governing constraint.
- **DS-06 (Prioritization & Severity Guidance):** ablation plan ranks what must be proven.

**Related Prompts:**
- `graphml_link_prediction_design.md` — once the task is framed as edge prediction.
- `graphml_fraud_graph_patterns.md` — for fraud/abuse on heterogeneous graphs under label scarcity.
- `graphml_gnn_scalability.md` — when the graph outgrows full-batch training.
- `../other-modalities/mlmodal_anomaly_outlier_detection.md` — graph anomaly detection under imbalance.
