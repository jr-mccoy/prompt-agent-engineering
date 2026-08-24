---
title: "GNN Scalability Design"
category: AI-ML/specialized-ml/graph-ml
description: "Scale GNN training to large graphs — choose neighbor sampling vs full-graph training, partition and distribute, and reason about memory/throughput tradeoffs and how sampling changes accuracy and the effective receptive field."
techniques:
  - ST-02
  - RT-02
  - QA-12
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - graph-ml
  - gnn-scalability
  - neighbor-sampling
  - graph-partitioning
  - distributed-training
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/graph-ml/graphml_task_framing.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_link_prediction_design.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_fraud_graph_patterns.md
---

# GNN Scalability Design

**Objective:** Help a practitioner scale GNN training and serving to graphs that no longer fit comfortably in memory. The naive full-batch approach explodes: each added layer pulls in a node's neighbors-of-neighbors, and on a dense graph the receptive field can swallow much of the graph per batch. This prompt structures the scaling decisions — neighbor sampling vs full-graph training, mini-batch construction, graph partitioning, and distributed training — and forces explicit reasoning about memory/throughput tradeoffs and how sampling silently alters accuracy, so the design doesn't quietly OOM or train on a different receptive field than it serves.

**When to Use:**
- Your graph is large enough that full-graph or full-neighborhood training runs out of memory or is too slow.
- You need to choose a sampling strategy (node-wise, layer-wise, or subgraph) and reason about its accuracy cost.
- You are planning distributed or partitioned GNN training and want to anticipate the failure modes.

**When NOT to Use:**
- Your graph is small and fits in memory — scaling machinery adds complexity for no benefit; framing lives in `graphml_task_framing.md`.
- Your problem is defining the link-prediction task, splits, or negatives — use `graphml_link_prediction_design.md`.
- You are modeling fraud under label scarcity and drift — use `graphml_fraud_graph_patterns.md`.

## Inputs / Context

Provide what you can:
- **Graph scale** — |V|, |E|, average and max degree, and density/skew.
- **Feature footprint** — per-node feature dimensionality and total feature memory.
- **Model shape** — number of GNN layers (hops) and hidden sizes.
- **Hardware budget** — GPU/CPU memory, number of devices, and interconnect.
- **Task** — node/edge/graph-level, and whether inference is batch or low-latency online.
- **Throughput target** — epochs/time budget and acceptable accuracy tolerance.
- **Serving constraint** — whether serving must use the same neighborhood construction as training.

## Constraints

**Must:**
- Estimate the receptive-field / neighbor-explosion footprint for the proposed layer count before committing to full-batch training.
- Choose a sampling/training strategy explicitly (full-graph, node-wise sampling, layer-wise, or subgraph/cluster) with its memory and accuracy implications stated.
- Ensure the serving-time neighborhood construction matches (or is reconciled with) the training-time one.
- State partitioning and communication costs when proposing distributed training.

**Must Not:**
- Assume full-batch training fits without estimating the per-batch neighbor footprint.
- Change the effective receptive field via sampling without acknowledging the accuracy impact.
- Fabricate metric/benchmark/throughput numbers from memory; reason from the user's graph and mark unknowns — measure on your graph.
- Introduce a train/serve neighbor mismatch that silently shifts predictions.

**Instructions:**

1. **Estimate the footprint.** For an L-layer model, approximate the per-seed-node neighbor count (roughly degree^L for full neighborhoods) and the resulting feature memory. This is where OOM hides.
2. **Pick a training regime.** Decide between full-graph training (small graphs), node-wise neighbor sampling (e.g., fixed fan-out per layer), layer-wise sampling, or subgraph/cluster-based mini-batching — and justify it from the footprint and degree skew.
3. **Set the sampling budget.** Choose per-layer fan-out / subgraph size, and note that smaller fan-out trims memory but shrinks and randomizes the receptive field — an accuracy tradeoff to validate.
4. **Reconcile train vs serve.** Define how neighborhoods are built at inference; if serving uses a different (e.g., truncated) neighborhood than training, flag the mismatch and plan to align or measure it.
5. **Plan partitioning.** If distributed, choose a partitioning scheme (edge-cut / vertex-cut / cluster) and reason about cross-partition edges, which drive communication cost and can dominate runtime.
6. **Budget communication and memory.** State where feature/embedding transfer happens across devices, and the memory/throughput tradeoff of caching vs recomputing neighbor features.
7. **Define the accuracy guardrail.** Compare the sampled-training model against a full-neighborhood reference on a tractable subgraph to quantify the sampling cost — don't assume it's negligible.
8. **Specify the throughput evaluation.** Report epochs/sec, peak memory, and accuracy at the chosen budget, all measured — not assumed.

**Output Format:**

A markdown scaling brief:
- **Footprint Estimate** — receptive-field / neighbor-explosion calculation.
- **Training Regime** — chosen strategy and why.
- **Sampling Budget** — fan-out/subgraph size and its receptive-field effect.
- **Train/Serve Reconciliation** — neighborhood construction alignment.
- **Partitioning & Distribution** — scheme and cross-partition cost.
- **Memory/Throughput Tradeoffs** — caching vs recompute, communication cost.
- **Accuracy Guardrail** — sampled-vs-full comparison plan.
- **Throughput Evaluation** — metrics to measure.
- **Open Questions** — quantities to measure on the user's graph.

## Verification

- [ ] The receptive-field / neighbor-explosion footprint is estimated before any full-batch decision.
- [ ] A training regime and sampling budget are chosen explicitly, with the accuracy tradeoff named.
- [ ] Train-time and serve-time neighborhood construction are reconciled (no silent mismatch).
- [ ] Partitioning and communication costs are stated for any distributed plan.
- [ ] An accuracy guardrail (sampled vs full-neighborhood reference) is specified.
- [ ] No metric, benchmark, or throughput number is asserted from memory — all are marked "measure on your graph."

## False-Positive Prevention

❌ **DON'T:**
- Assume full-batch training "should fit" — **neighbor-explosion / OOM assumed away** is the classic failure: a 3-layer model on a high-degree graph can pull most of the graph into one batch.
- Cut fan-out to save memory while reporting unchanged accuracy — sampling silently changes the **effective receptive field** and can degrade results.
- Train on full neighborhoods but serve with a truncated one (or vice versa), creating a **train/serve neighbor mismatch** that shifts predictions.
- Ignore cross-partition edges when estimating distributed runtime.

✅ **DO:**
- Compute the degree^L neighbor footprint up front and let it drive the sampling choice.
- Quantify the sampling accuracy cost against a full-neighborhood reference on a tractable subgraph.
- Define one neighborhood-construction contract used by both training and serving (or measure the gap).
- Account for cross-partition communication as a first-class cost in the distributed plan.

## Example Output

```markdown
# GNN Scalability — Citation Graph (|V|=20M, avg deg 25)

## Footprint Estimate
- 3 layers, fan-out 25 → ~25^3 ≈ 15.6K neighbors/seed; full-batch infeasible.

### Training Regime
- Node-wise neighbor sampling (GraphSAGE-style), fan-out [15,10,5].

### Sampling Budget
- Fan-out [15,10,5] → ~750 neighbors/seed; receptive field narrowed — validate accuracy.

### Train/Serve Reconciliation
- Serving uses identical [15,10,5] sampler; one shared neighborhood contract.

### Partitioning & Distribution
- METIS edge-cut, 8 partitions; cross-partition edges cached locally.

### Accuracy Guardrail
- Compare vs full-neighborhood model on a 200K-node subgraph.

### Open Questions
- Accuracy drop from fan-out truncation; peak memory at batch 1024 — measure on your graph.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered steps from footprint estimate through throughput evaluation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Frames the model as a GNN scaling-design reviewer.
- **QA-12 (False Positives Identification):** Guards against train/serve neighbor mismatch and silent receptive-field changes.
- **CM-02 (Constraint Specification):** Hard rules on footprint estimation and train/serve reconciliation.
- **DS-06 (Prioritization & Severity Guidance):** Maps the sampling/partitioning choice to memory, throughput, and accuracy tradeoffs.

**Related Prompts:**
- `graphml_task_framing.md` — overall graph-ML framing and task selection.
- `graphml_link_prediction_design.md` — link-prediction task framing, splits, and negatives.
- `graphml_fraud_graph_patterns.md` — fraud-graph modeling under label scarcity and drift.
