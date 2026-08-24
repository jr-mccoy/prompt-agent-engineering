---
title: "Machine Unlearning and Deletion Requests"
category: AI-ML/responsible-ai-governance
description: "Design how a deletion request propagates into trained models — separating deleting the record from removing its influence, choosing between retraining, approximate unlearning, and containment, and stating precisely what was and was not achieved."
techniques:
  - RT-10
  - ST-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - machine-unlearning
  - deletion
  - right-to-erasure
  - retraining
  - data-lifecycle
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_privacy_technique_selection.md
  - domain-AI-ML/model-security/mlsec_model_inversion_leakage_audit.md
  - domain-AI-ML/data-for-ml/mldata_data_versioning_lineage.md
  - domain-AI-ML/mlops-infrastructure/mlops_model_registry_design.md
---

# Machine Unlearning and Deletion Requests

**Objective:** Design how a deletion request actually propagates into trained models — distinguishing deleting a record from removing its influence, choosing among retraining, approximate unlearning, and containment on cost and evidence, and producing a precise statement of what was achieved rather than an implied guarantee.

**When to Use:**
- Deletion or erasure requests arrive and the current process stops at the database.
- Before a system that will receive such requests goes live, so the model lifecycle can be designed to make them answerable.
- When someone must state, to a regulator or a customer, what happened to a person's data inside a model.

**When NOT to Use:**
- You need the legal determination of what is required — that belongs to `domain-legal/`; this prompt designs the technical response to a requirement someone else states.
- The question is what the model currently leaks — use `../model-security/mlsec_model_inversion_leakage_audit.md`.
- Data is deleted before training and never reaches a model; the request stops at the pipeline and this depth is unnecessary.

## Inputs / Context

- **The obligation, as stated by whoever owns it** — quoted, not interpreted here.
- **Request volume and cadence** — one-off, occasional, or continuous, since this decides whether per-request retraining is viable at all.
- **Model inventory** — every model trained on the data, including derived, distilled, and cached artifacts.
- **Training-data lineage** — whether a specific record can be traced to the models it influenced.
- **Retraining cost and cadence** — wall-clock and money per full retrain, and the natural retrain schedule.
- **Checkpoint availability** — whether checkpoints predating a given record exist and are retained.

## Constraints

**Must:**
- Separate three distinct things throughout: **deleting the record** from stores, **removing its influence** from trained models, and **preventing its reconstruction** from a deployed model. Most deletion processes do the first and imply the other two.
- Require lineage as the precondition — if a record cannot be traced to the models it influenced, no honest claim about those models is possible, and that is the first finding.
- State the evidence standard for any influence-removal claim: what test was run, what it shows, and what it cannot show.
- Include **containment** as a legitimate option — restricting or retiring a model can achieve the outcome where influence removal is infeasible.
- Cover derived artifacts explicitly: distilled models, embeddings, caches, backups, and downstream models trained on this model's outputs.

**Must Not:**
- Claim influence is removed on the basis of an approximate method without stating the evidence and its limits; approximate unlearning gives an approximation, and the word carries weight.
- Assert legal deadlines, statutory requirements, or regulatory expectations from memory — quote the obligation as the accountable owner stated it, and mark anything else `[verify with the obligation owner]`.
- Treat deleting the training row as removing model influence; the model was updated during training and does not consult the row afterwards.
- Promise a response time that per-request retraining cannot meet at the observed request volume.
- Ignore backups and derived artifacts because they are inconvenient.

**Instructions:**

1. **Record the obligation verbatim.** As stated by its owner, with the owner named. Everything technical is designed against that text rather than against an interpretation formed here.

2. **Establish lineage feasibility.** Can a given record be traced to the models it influenced? If not, that is the primary finding and the first thing to fix — provenance tags in the training manifest — because without it every downstream claim is unfounded.

3. **Inventory every affected artifact.** Production models, prior versions retained for rollback, distilled or fine-tuned descendants, embeddings and vector indexes, feature-store values, caches, evaluation snapshots, and backups. Deletion processes typically stop at the first item.

4. **Choose the response per artifact.**
   - *Retrain without the record* — the only approach that removes influence with certainty. Cost is a full training cycle; viable when requests batch to the natural retrain cadence.
   - *Retrain from a pre-contribution checkpoint* — cheaper, requires the checkpoint to exist and to predate the record.
   - *Approximate unlearning* — lower cost, gives an approximation. State the method and what evidence would support the claim.
   - *Containment* — restrict access, coarsen outputs, or retire the model. Achieves the outcome without touching the weights when nothing else is feasible.
   - *No action, with justification* — where the record demonstrably had no influence, evidenced rather than assumed.

5. **Batch against the retrain cadence.** Per-request retraining rarely survives contact with volume. Define the batching window, the maximum time a request waits, and whether that meets the obligation. If it does not, the design must change rather than the promise.

6. **Define the evidence produced.** For each response type, what is recorded: the manifest excluding the record, the checkpoint lineage, the unlearning verification run, or the containment decision. This is what an auditor or the requester will be shown.

7. **Verify, where verification is possible.** After influence removal, test whether the record is still recoverable — a targeted extraction or membership probe on that record. State plainly that a null result bounds rather than proves removal.

8. **Write the response to the requester.** In plain language: what was deleted, what was retrained or contained, what remains and why, and by when the remainder resolves. Do not imply more than was achieved.

9. **Fix the lifecycle so the next request is cheaper.** Provenance tags, checkpoint retention aligned to request patterns, and a deletion-aware retrain schedule.

**Output Format:**

A markdown design:
- **Obligation** — quoted, with its owner named.
- **Lineage Feasibility** — can a record be traced to models; if not, the remediation.
- **Affected-Artifact Inventory** — table: Artifact | Contains influence? | Response chosen | Cost | Timeline.
- **Batching Design** — window, maximum wait, whether it meets the obligation.
- **Evidence Produced** — per response type.
- **Verification** — test run, result, and its limits.
- **Requester Response Template** — plain language, no overclaim.
- **Lifecycle Fixes** — what makes the next request cheaper.

## Verification

- [ ] The obligation is quoted from its owner, not interpreted here.
- [ ] Lineage feasibility is established before any removal claim.
- [ ] The inventory covers derived artifacts, caches, embeddings, and backups.
- [ ] Each artifact has a chosen response with cost and timeline.
- [ ] Batching is designed against real request volume and checked against the obligation.
- [ ] Any approximate-unlearning claim states its evidence and its limits.
- [ ] Verification results are described as bounding rather than proving removal.
- [ ] The requester response does not imply more than was achieved.
- [ ] Containment appears as a legitimate option, not only as failure.
- [ ] No legal deadlines or requirements are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Report a deletion complete when the row is gone but three trained models still carry its influence — that is the single most common gap in a deletion process.
- Claim influence removal without lineage; if you cannot say which models saw the record, you cannot say anything about those models.
- Describe approximate unlearning as removal — the approximation is the whole point of the method and belongs in the claim.
- Promise a turnaround that per-request retraining cannot meet, then discover the arithmetic at the first busy month.
- Omit embeddings, vector indexes, caches, and distilled descendants because they are not "the model".
- Treat a null result from a membership probe as proof the record is gone; it bounds recoverability at the effort you spent.

✅ **DO:**
- Hold record deletion, influence removal, and reconstruction prevention apart in every statement you make.
- Fix lineage first — provenance tags are the precondition for every honest claim that follows.
- Inventory derived artifacts explicitly, including the ones nobody thinks of as models.
- Batch to the retrain cadence and check the resulting wait against the obligation before promising anything.
- Offer containment where influence removal is infeasible; the requester's outcome can be met without touching weights.
- Write the requester response in plain language that matches exactly what was done.

## Example Output

```markdown
## Deletion Design: Recommendation Platform — User Erasure Requests

### Obligation
As stated by the Data Protection Officer (owner): *"On a verified erasure request we must cease
using the individual's personal data and must not retain it in a form that identifies them.
Where full removal from a derived system is not technically feasible, we must document why and
what compensating measure is in place."* No deadline or statutory reference is reproduced here —
`[verify all timing requirements with the DPO]`.

### Lineage Feasibility
**Currently infeasible.** The training manifest records dataset versions, not per-user
provenance, so we cannot say which models a given user influenced. **This is the primary
finding.** Remediation: add `user_id_hash` provenance tags to the training manifest at the next
pipeline release. Until then, every claim about a specific model must be made at dataset-version
granularity, which is weaker and should be described as such.

### Affected-Artifact Inventory
| Artifact | Contains influence? | Response | Cost | Timeline |
|---|---|---|---|---|
| Production ranker v12 | Yes | retrain without user at next scheduled retrain | absorbed by schedule | ≤14 days |
| Ranker v10, v11 (rollback) | Yes | **retire** — v12 is stable, rollback targets move to post-deletion builds | none | immediate |
| Distilled on-device model | Yes (from v11) | rebuild from the retrained v12 | 1 distillation run | ≤21 days |
| User-embedding table | Yes — directly identifying | **hard delete row** | trivial | immediate |
| ANN index | Yes — contains the embedding | rebuild index | 1 index build | ≤24 h |
| Feature store values | Yes | delete keyed rows + TTL sweep | trivial | immediate |
| Offline eval snapshots | Yes | delete snapshots containing the user | trivial | ≤7 days |
| Backups (35-day retention) | Yes | **containment** — no restore-to-production without a deletion replay step | process change | immediate |

The embedding table and ANN index are the artifacts most often missed, and they are the ones
that hold data in the most directly identifying form.

### Batching Design
Observed volume: ~40–70 requests/week. Per-request retraining is not viable — one full retrain
per request would exceed the training cluster's capacity many times over.
**Design:** requests batch into the fortnightly retrain. Maximum wait 14 days; immediate actions
(embedding, feature store, index) run within 24 hours of verification, so the identifying
artifacts go first and only model influence waits for the batch. Whether 14 days satisfies the
obligation is `[verify with the DPO]` — if it does not, the retrain cadence changes, not the
promise.

### Evidence Produced
| Response | Evidence recorded |
|---|---|
| Retrain without user | training manifest excluding the user's provenance tag + build ID |
| Retire old versions | registry record marking versions withdrawn, with reason |
| Hard delete | deletion log entry with timestamp and operator |
| Containment (backups) | documented restore procedure requiring a deletion replay |

### Verification
After the retrain, run a targeted membership probe on the erased user's records against the new
model. Result recorded per request. **This bounds rather than proves removal** — it shows the
record is not recoverable at the effort we spent, which is a narrower statement than absence,
and the requester response is worded accordingly.

### Requester Response Template
> We have deleted your account data, your profile embedding, and the derived values we held for
> you. These were removed on [date]. Our recommendation models are rebuilt on a fortnightly
> cycle; the next rebuild, on [date], will be trained without your data, and the earlier model
> versions that were trained with it have been withdrawn from use. Encrypted backups are
> retained for 35 days for disaster recovery and cannot be selectively edited; any restore from
> them re-applies your deletion before the system returns to service. We will confirm when the
> rebuild completes.

### Lifecycle Fixes
1. Per-user provenance tags in the training manifest — makes every future claim specific rather
   than dataset-version-wide. Highest value, do first.
2. Retain one checkpoint predating each fortnightly batch, enabling checkpoint-based retraining
   instead of full retraining.
3. Add the embedding table, ANN index, and feature store to the deletion runbook as first-class
   targets, since they hold the most identifying form of the data and are the easiest to miss.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** artifact type and lineage availability drive the choice among retrain, checkpoint, approximate, and containment.
- **ST-02 (Structured Sequential Instructions):** obligation, then lineage, then inventory, then response — so no claim precedes the evidence that could support it.
- **CM-02 (Constraint Specification):** the three-way separation and the no-overclaim rule bound what may be told to a requester.
- **QA-12 (False Positives Identification):** rejects row deletion reported as influence removal and null probes reported as proof.
- **DS-06 (Prioritization and Severity Guidance):** identifying artifacts are handled first; influence removal batches.

**Related Prompts:**
- `../data-for-ml/mldata_data_versioning_lineage.md` — the provenance work this depends on.
- `../model-security/mlsec_model_inversion_leakage_audit.md` — measures whether a record is still recoverable.
- `../mlops-infrastructure/mlops_model_registry_design.md` — where version retirement and checkpoint retention are implemented.
- `rai_privacy_technique_selection.md` — upstream design that can make deletion cheaper.
