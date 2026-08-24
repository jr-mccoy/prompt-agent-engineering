---
title: "Adversarial Defense Strategy"
category: AI-ML/model-security
description: "Choose and layer defenses against adversarial inputs — weighing robust training, input transformation, detection, and architectural containment against their clean-accuracy and latency costs, and committing to re-evaluate each under an attacker who knows the defense is there."
techniques:
  - ST-02
  - DS-06
  - CM-02
  - QA-12
  - AG-44
difficulty: advanced
tags:
  - adversarial-defense
  - robust-training
  - input-transformation
  - defense-in-depth
  - model-security
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_adversarial_robustness_assessment.md
  - domain-AI-ML/model-security/mlsec_secure_inference_endpoint_design.md
  - domain-AI-ML/model-security/mlsec_ml_threat_model.md
  - domain-AI-ML/model-evaluation-validation/mleval_selective_prediction_abstention.md
---

# Adversarial Defense Strategy

**Objective:** Select and layer defenses against adversarial inputs for a measured weakness — weighing each candidate against its clean-accuracy, latency, and operational cost, placing containment outside the model where the model cannot be made strong enough, and committing every chosen defense to re-evaluation under an attacker who knows it is deployed.

**When to Use:**
- `mlsec_adversarial_robustness_assessment.md` has produced a measured weakness and you must decide what to do about it.
- A defense is already deployed and you need to judge whether it is doing anything.
- The honest answer may be containment rather than robustness, and you need that option on the table.

**When NOT to Use:**
- You have no measurement yet — defenses chosen before measurement optimize for the wrong class. Run the assessment first.
- The exposure is the serving surface rather than the model's decision boundary — use `mlsec_secure_inference_endpoint_design.md`.
- The problem is ordinary distribution shift — robustness machinery adds cost for no security benefit.

## Inputs / Context

- **Measured weakness** — which slices, which attack class, at what budget and knowledge assumption.
- **Clean-accuracy tolerance** — how much the deployment can afford to lose, expressed on the metric that matters.
- **Latency and cost budget** — per-request headroom for preprocessing, ensembling, or detection.
- **Retraining feasibility** — whether robust training is available at all given data, compute, and release cadence.
- **Downstream containment options** — human review, transaction limits, secondary checks, delay windows, reversibility.
- **Consequence of a successful evasion** — what actually happens when one gets through, which sets how much defense is worth.

## Constraints

**Must:**
- Tie every candidate defense to the specific measured weakness it addresses; a defense with no measurement behind it does not enter the plan.
- State the clean-accuracy and latency cost of each candidate, and check both against the stated tolerance before recommending.
- Include **containment outside the model** as a first-class option, ranked alongside model-side defenses rather than as a fallback.
- Commit each chosen defense to re-evaluation with attacks adapted to it, and name the date or gate for that re-evaluation.
- State for each defense whether it prevents the attack or raises its cost, and by roughly how much.

**Must Not:**
- Recommend a defense on the strength of its published results; results transfer poorly across threat models, and many published defenses have documented adaptive-attack bypasses. Where a specific published result matters, mark it `[verify against a primary source]`.
- Stack defenses and assume their effects compose — layered obfuscation frequently produces one gradient-masking artefact rather than additive robustness.
- Recommend detection without specifying the false-positive rate the deployment can absorb, since a detector that rejects legitimate traffic is an availability incident.
- Present a defense as complete when the residual attack path is known and unaddressed.

**Instructions:**

1. **Restate the weakness precisely.** Slice, attack class, budget, knowledge assumption, and the measured gap between clean and robust. Everything is chosen against this.

2. **Set the acceptance target.** What robust accuracy on which slice would make the deployment acceptable, and how much clean accuracy may be spent reaching it. If no target can be stated, the work has no stopping rule — say so.

3. **Enumerate candidate defenses across four layers.** Do not skip a layer because an earlier one looks sufficient.
   - **Robust training** — adversarial training and its variants. Highest cost in clean accuracy and compute; the only layer that changes the decision boundary itself.
   - **Input transformation** — normalization, re-encoding, quantization, randomized transforms. Cheap, sometimes already present incidentally, and the layer most prone to producing gradient-masking artefacts rather than robustness.
   - **Detection and abstention** — flag or refuse suspicious inputs rather than classify them. Converts an integrity failure into an availability cost; needs an explicit false-positive budget.
   - **Architectural containment** — limit what a wrong answer can do: human review above a threshold, value caps, delay windows, reversibility, secondary independent checks. Does not make the model stronger; makes being wrong survivable.

4. **Cost each candidate honestly.** For each: expected clean-accuracy change, latency change, compute and retraining cost, operational burden, and whether it prevents or merely costs.

5. **Check composition, not just addition.** For any proposed stack, state how the layers interact and whether the combination could mask gradients rather than add robustness. Prefer stacks whose layers fail independently.

6. **Choose, and say what is left.** Recommend a layered plan against the acceptance target, and state the residual attack path that remains — the one an attacker aware of every layer would take.

7. **Set the re-evaluation gate.** Name the attacks that must be adapted to each deployed defense, and the point (release, date, or trigger) at which that re-evaluation happens. A defense that is never re-evaluated under adaptation is an assumption, not a control.

8. **Define the operational signals.** What tells you in production that the defense is degrading — detector rate drift, abstention-rate change, clean-accuracy regression, distributional change in rejected inputs.

**Output Format:**

A markdown defense plan:
- **Weakness & Acceptance Target** — the measured gap and the bar that ends the work.
- **Candidate Matrix** — table: Layer | Defense | Addresses which weakness | Clean cost | Latency cost | Prevents or raises cost | Verdict.
- **Recommended Stack** — ordered, with the interaction analysis between layers.
- **Residual Attack Path** — what an attacker who knows the full stack does.
- **Re-evaluation Gate** — attacks to adapt, and when.
- **Production Signals** — what degradation looks like.
- **Rejected Candidates** — each with the reason, so the omission is reviewable.

## Verification

- [ ] Every candidate names the measured weakness it addresses.
- [ ] All four layers are considered, including containment outside the model.
- [ ] Clean-accuracy and latency costs are stated per candidate and checked against tolerance.
- [ ] Each defense is labelled as preventing or as raising cost, with the rough new cost.
- [ ] The stack's layer interaction is analysed rather than assumed additive.
- [ ] Any detection layer has an explicit false-positive budget.
- [ ] The residual attack path is stated, not omitted.
- [ ] A re-evaluation gate with adapted attacks is scheduled for every deployed defense.
- [ ] No published defense result is asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Pick adversarial training because it is the strongest defense in the literature without pricing the clean-accuracy loss against this deployment's tolerance.
- Add an input transformation and treat the resulting robust-accuracy jump as real — it is the layer most likely to be masking gradients rather than removing the vulnerability.
- Stack four defenses and describe the system as defense-in-depth when all four fail to the same adaptive attack.
- Deploy a detector without a false-positive budget; rejecting 3% of legitimate traffic can cost more than the evasions it stops.
- Leave containment out because it "doesn't fix the model" — where the model cannot be made strong enough, containment is the only thing that changes the outcome.
- Declare the weakness closed while a known residual path is unaddressed and unstated.

✅ **DO:**
- Choose against the measured slice and the stated acceptance target, and stop when the target is met.
- Price every candidate in clean accuracy, latency, and operational burden before ranking it.
- Say plainly which layer prevents and which only costs, and estimate the new attacker cost.
- Analyse how the layers interact and prefer stacks that fail independently.
- Rank containment beside model-side defenses; a value cap or a review threshold is often the cheapest real control.
- Publish the residual attack path and schedule the adapted re-evaluation that would find it.

## Example Output

```markdown
## Defense Strategy: Document-Fraud Image Classifier v3 (utility-bill slice)

### Weakness & Acceptance Target
Utility-bill slice falls from 0.944 clean to **0.706** under a 200-query decision-based
attack (grey-box). Target: **≥0.88 robust** on that slice, spending **≤2 points** of clean
accuracy overall. Below 0.88 the expected payout loss exceeds the defense's running cost.

### Candidate Matrix
| Layer | Defense | Addresses | Clean cost | Latency | Prevents / costs | Verdict |
|---|---|---|---|---|---|---|
| Robust training | Adversarial training on the bill slice | decision boundary | ~1.5–3 pts `[verify on your data]` | none at serve | raises cost substantially | **Adopt (scoped to slice)** |
| Input transform | Add randomized resize before inference | query attack | ~0.2 pts | +8 ms | raises cost; masking risk | **Adopt with masking re-check** |
| Detection | Query-pattern detector per account | iterative querying | 0 pts | +2 ms | prevents *this* attack shape | **Adopt — FP budget 0.5%** |
| Detection | Per-input adversarial detector | crafted inputs | 0 pts | +40 ms | raises cost | **Reject** — FP rate unbounded at our volume |
| Containment | Manual review for bills above payout threshold | consequence | 0 pts | async | **prevents payout**, not evasion | **Adopt — highest leverage** |
| Containment | 24 h payout delay on first-time accounts | consequence | 0 pts | async | prevents irreversible loss | **Adopt** |

### Recommended Stack
1. **Containment first** — review threshold + delay window. Neither touches the model, both
   cap the loss from an evasion that succeeds, and they fail independently of everything else.
2. **Query-pattern detection** — the measured attack needed ~200 queries per account; making
   that expensive attacks the delivery mechanism rather than the boundary.
3. **Scoped adversarial training** — on the bill slice only, to hold the overall clean cost
   inside the 2-point budget.
4. **Randomized resize** — cheapest layer, but adopted *last* and re-measured, because it is
   the one most likely to inflate the number without improving the model.

**Interaction:** layers 1 and 2 fail independently of 3 and 4 (one attacks consequence, one
delivery, two the boundary). Layers 3 and 4 do **not** fail independently — randomized resize
can mask the gradients that adversarial training is supposed to have hardened, so the
post-deployment measurement must use expectation-over-transform, not a fixed-input attack.

### Residual Attack Path
An attacker who knows the full stack spreads queries across many accounts to stay under the
per-account detector, keeps each forged bill under the review threshold, and accepts the
24-hour delay. This converts a fast high-value attack into a slow low-value one — the loss
becomes rate-limited rather than eliminated. That is the intended outcome, and it should be
stated as such rather than described as prevention.

### Re-evaluation Gate
Before release: re-run the decision-based query attack **adapted** to the detector (distributed
across accounts) and expectation-over-transform adapted to the randomized resize. Re-check all
four gradient-masking signatures. Gate: ship only if the bill slice holds ≥0.88 under the
adapted attacks, not the original ones.

### Production Signals
- Detector trigger rate drifting from its baseline in either direction.
- Bill-slice clean accuracy regressing more than 1 point after the scoped robust training.
- Rejected-input distribution shifting toward a single account cohort.
- Review-queue volume rising without a matching rise in confirmed fraud.

### Rejected Candidates
- **Per-input adversarial detector** — at our request volume the false-positive rate would
  exceed the 0.5% budget, and a rejected legitimate document is a support cost plus a churn risk.
- **Full-dataset adversarial training** — would exceed the 2-point clean budget; scoping to the
  weak slice buys most of the benefit for a fraction of the cost.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the four-layer walk forces containment to be considered rather than reached for last.
- **DS-06 (Prioritization and Severity Guidance):** candidates are ranked by benefit against the acceptance target and priced costs.
- **CM-02 (Constraint Specification):** the adapted-re-evaluation and no-fabrication rules bound what may be adopted or claimed.
- **QA-12 (False Positives Identification):** separates defenses that remove a vulnerability from those that hide it, and prices detector false positives.
- **AG-44 (Impossible-vs-Tedious Control Test):** every defense must declare whether it prevents or merely costs.

**Related Prompts:**
- `mlsec_adversarial_robustness_assessment.md` — produces the measurement this plan is chosen against, and re-runs the gate.
- `mlsec_secure_inference_endpoint_design.md` — the serving-side rate limiting and output shaping this plan relies on.
- `mlsec_ml_threat_model.md` — re-run when the deployment surface changes.
- `../model-evaluation-validation/mleval_selective_prediction_abstention.md` — designing the abstention layer properly.
