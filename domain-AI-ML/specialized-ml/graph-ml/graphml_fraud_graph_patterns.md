---
title: "Fraud-Graph Modeling Patterns"
category: AI-ML/specialized-ml/graph-ml
description: "Model fraud and abuse on heterogeneous graphs (users/devices/transactions) under extreme label scarcity and adversarial drift — with time-respecting features and operating-point evaluation, not just AUC."
techniques:
  - ST-02
  - RT-02
  - QA-12
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - graph-ml
  - fraud-detection
  - heterogeneous-graph
  - imbalance
  - adversarial-drift
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/graph-ml/graphml_task_framing.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_link_prediction_design.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_gnn_scalability.md
---

# Fraud-Graph Modeling Patterns

**Objective:** Help a practitioner model fraud or abuse as a graph problem where the data fights back. Fraud graphs are heterogeneous (users, devices, payment instruments, transactions, IPs), labels are scarce and delayed, classes are extremely imbalanced, and adversaries adapt the moment a pattern is exploited. This prompt structures the modeling decisions — graph schema, time-respecting features, label handling, and operating-point evaluation — so the system catches real abuse at the threshold a review team can actually action, instead of celebrating an AUC that evaporates in production or trains on edges that secretly encode the label.

**When to Use:**
- You are detecting fraud, abuse, fake accounts, or collusion rings on a graph of entities and interactions.
- Your positive labels are rare, delayed (chargebacks arrive weeks later), and partially noisy.
- You need to decide which entities to send to a capacity-limited review queue.

**When NOT to Use:**
- Your task is plain link prediction with abundant labels and no adversary — use `graphml_link_prediction_design.md`.
- You are framing the general graph-ML approach for the first time — start with `graphml_task_framing.md`.
- Your blocker is purely scaling training to a huge graph — use `graphml_gnn_scalability.md`.

## Inputs / Context

Provide what you can:
- **Graph schema** — node types (user/device/txn/IP/instrument), edge types, and directedness.
- **Label source** — how fraud is confirmed (chargebacks, manual review, reports) and the labeling delay.
- **Class balance** — rough positive rate and whether it drifts over time.
- **Time information** — timestamps on edges/transactions and the inference latency budget.
- **Operating constraint** — review-team capacity (alerts/day) or the precision target at deployment.
- **Adversary model** — known evasion behaviors and how fast patterns change.
- **Feature inventory** — entity, aggregate, and graph-structural features available at scoring time.

## Constraints

**Must:**
- Define the heterogeneous graph schema and which entity is scored before modeling.
- Build only time-respecting features: every feature must be computable strictly from information available before the decision time.
- Evaluate at the deployable operating point (precision@k / review-capacity, recall at fixed alert budget) in addition to AUC.
- Use a temporal split and account for label delay when assigning labels to the train/test boundary.

**Must Not:**
- Include label-derived or future edges (e.g., a "chargeback" or "banned" edge) in the scoring graph.
- Report AUC alone as evidence of production readiness on a heavily imbalanced graph.
- Fabricate metric/benchmark numbers from memory; reason from the user's graph and mark unknowns — measure on your graph.
- Ignore adversarial drift by assuming the test-period distribution matches training.

**Instructions:**

1. **Define the schema and scoring target.** Name node/edge types and decide what is scored (account? transaction? device cluster?). Heterogeneity is the point — homogenizing throws away signal.
2. **Trace the label lifecycle.** Document how positives are confirmed and the delay. Set the train/test cutoff so that "unlabeled at cutoff" entities are handled honestly, not silently treated as negative.
3. **Audit for label-derived edges.** Remove any edge or feature that exists only because the label exists (a chargeback link, a fraud-cluster tag). These are the classic leakage trap in fraud graphs.
4. **Engineer time-respecting features.** Velocity, shared-device counts, and neighbor-risk aggregates must be computed from a graph snapshot strictly before the decision time.
5. **Handle imbalance deliberately.** Choose among class weighting, focal loss, or curated sampling — and verify the choice on a temporal validation split, not a random one.
6. **Model the adversary.** Plan for drift: a rolling/temporal evaluation, drift monitors, and a retraining cadence. Assume patterns that work will be evaded.
7. **Evaluate at the operating point.** Compute precision@k matched to review capacity, recall at the alert budget, and the alert-to-confirmed-fraud rate — the numbers the review team lives with.
8. **Stage the baseline ladder.** Rules/heuristics → tabular model on entity features → GNN that adds structure, so any graph lift is attributable and worth its operational cost.

**Output Format:**

A markdown modeling brief:
- **Graph Schema** — node/edge types and scoring target.
- **Label Lifecycle** — confirmation source, delay, cutoff handling.
- **Leakage Checklist** — label-derived and future-edge checks specific to fraud.
- **Time-Respecting Features** — feature list with the as-of-time rule.
- **Imbalance Strategy** — chosen approach and validation method.
- **Adversarial-Drift Plan** — monitors, rolling eval, retraining cadence.
- **Operating-Point Evaluation** — precision@k / recall-at-budget definition tied to capacity.
- **Baseline Ladder** — rules → tabular → GNN.
- **Open Questions** — quantities to measure on the user's graph.

## Verification

- [ ] Graph schema and scoring target are defined before any model is named.
- [ ] Every feature is time-respecting (computable strictly before decision time).
- [ ] Label-derived and future edges are explicitly removed from the scoring graph.
- [ ] Evaluation reports a deployable operating point, not AUC alone.
- [ ] An adversarial-drift plan (rolling eval + retraining cadence) is included.
- [ ] No metric or benchmark number is asserted from memory — all are marked "measure on your graph."

## False-Positive Prevention

❌ **DON'T:**
- Include a chargeback/ban edge or a fraud-cluster tag in the scoring graph — this **label-derived edge leakage** lets the model read the answer, producing a near-perfect AUC that collapses at the deployable alert threshold.
- Treat all unlabeled-at-cutoff entities as confirmed negatives when labels arrive weeks late.
- Validate imbalance handling on a random split that mixes future and past entities.
- Assume the adversary is static and skip drift monitoring.

✅ **DO:**
- Rebuild the scoring graph from edges that exist strictly before the decision time, and re-derive features from it.
- Report precision@k at review capacity and recall at the alert budget alongside AUC.
- Use temporal validation and a rolling evaluation window that mirrors deployment.
- Treat delayed labels honestly (censoring/abstain), and plan a retraining cadence against drift.

## Example Output

```markdown
# Fraud-Graph Modeling — Account Takeover

## Graph Schema
- Nodes: user, device, IP, txn. Score: user account per session.

### Label Lifecycle
- Positive = confirmed ATO from support tickets; ~21-day delay.
- Cutoff: train ≤ Mar 1; entities unlabeled at cutoff = abstain, not negative.

### Leakage Checklist
- [ ] "account_locked" edge removed (label-derived)
- [ ] Device-share counts computed as-of session time only

### Time-Respecting Features
- Shared-device count (pre-session), neighbor-risk mean (pre-session), login velocity.

### Imbalance Strategy
- Focal loss; validated on temporal split (positive rate ~0.4%, drifting).

### Adversarial-Drift Plan
- Rolling 2-week eval; PSI drift monitor; weekly retrain.

### Operating-Point Evaluation
- Precision@500/day (review capacity); recall at that budget.

### Open Questions
- Graph lift over tabular at precision@500 — measure on your graph.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered steps from schema through operating-point evaluation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Frames the model as a fraud-graph modeling reviewer.
- **QA-12 (False Positives Identification):** Fraud-specific checklist for label-derived and future edges.
- **CM-02 (Constraint Specification):** Hard rules on time-respecting features and operating-point evaluation.
- **DS-06 (Prioritization & Severity Guidance):** Maps metrics to review capacity and the deployable threshold.

**Related Prompts:**
- `graphml_task_framing.md` — overall graph-ML framing and task selection.
- `graphml_link_prediction_design.md` — edge-formation framing, splits, and negative sampling.
- `graphml_gnn_scalability.md` — scaling the chosen GNN to large fraud graphs.
