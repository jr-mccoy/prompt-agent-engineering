---
title: "Adversarial Robustness Assessment"
category: AI-ML/model-security
description: "Measure a model's robustness to adversarial inputs under a threat model the deployment actually faces — defining the perturbation budget from the real input channel, evaluating with adaptive rather than fixed attacks, and reporting robust accuracy as a lower bound rather than a guarantee."
techniques:
  - RT-02
  - DS-02
  - QA-12
  - CM-02
  - RT-05
difficulty: advanced
tags:
  - adversarial-examples
  - robust-accuracy
  - adaptive-attack
  - perturbation-budget
  - evaluation
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-security/mlsec_adversarial_defense_strategy.md
  - domain-AI-ML/model-security/mlsec_ml_threat_model.md
  - domain-AI-ML/model-evaluation-validation/mleval_robustness_stress_testing.md
  - domain-AI-ML/model-evaluation-validation/mleval_ood_detection_design.md
---

# Adversarial Robustness Assessment

**Objective:** Measure how a model behaves under adversarial input for the threat model this deployment actually faces — deriving the perturbation budget from the real input channel, evaluating with attacks adapted to the defense rather than a fixed suite, and reporting robust accuracy as a lower bound that a stronger attack can lower further.

**When to Use:**
- Evasion ranked as applicable in `mlsec_ml_threat_model.md` and you need a measurement rather than a judgment.
- Before claiming any robustness property to a customer, a regulator, or a risk committee.
- After adding a defense, to test whether it survives an attacker who knows it is there.

**When NOT to Use:**
- You want general distribution-shift and stress behaviour rather than an adversary — use `../model-evaluation-validation/mleval_robustness_stress_testing.md`.
- No attacker benefits from a flipped prediction — robustness work has no threat to answer to; say so and stop.
- You need to choose and deploy a defense rather than measure one — use `mlsec_adversarial_defense_strategy.md`.

## Inputs / Context

- **Model & input modality** — architecture family, and what a single input physically is (uploaded file, form field, sensor reading, scene).
- **Input channel** — exactly how an input reaches the model, and what is done to it in between (re-encoding, resizing, normalization, validation).
- **Attacker knowledge assumption** — white-box (weights known), grey-box (architecture known), or black-box (query only), and the query budget.
- **Attacker goal** — untargeted (any wrong answer) or targeted (a specific wrong answer); these have different costs and different defenses.
- **Clean performance baseline** — the metric and value the robust number will be compared against.
- **Deployment tolerance** — how much clean accuracy the system can afford to trade for robustness.

## Constraints

**Must:**
- Derive the perturbation budget from the input channel, not from a convention — state the norm or transformation class and why it is the right one for inputs that survive this pipeline.
- Evaluate with attacks **adapted to the defense in place**; a defense evaluated only against attacks that predate it produces a number that means nothing.
- Report robust accuracy explicitly as an upper bound on what a stronger attack would leave, never as a floor or a guarantee.
- Report clean accuracy alongside every robust number, since robustness is bought with it.
- State attack convergence evidence (iterations, step size, restarts, whether loss plateaued) — an unconverged attack manufactures robustness.

**Must Not:**
- Report a single robust-accuracy number for a single attack and describe the model as "robust".
- Quote published robust-accuracy figures, attack success rates, or benchmark leaderboard values from memory; mark any needed figure `[verify against a primary source]`.
- Treat gradient masking or obfuscation as robustness — if gradients are unusable, say so and switch to gradient-free or transfer attacks rather than reporting the resulting high number.
- Generate or include working attack code, payloads, or a reusable exploit harness; describe the evaluation design, not the weapon.
- Extrapolate from one perturbation type to robustness in general.

**Instructions:**

1. **Restate the threat model.** Write the attacker's knowledge, goal, query budget, and what a successful flip is worth. If any is unknown, choose the conservative assumption and label it.

2. **Derive the perturbation budget from the channel.** Determine what perturbations survive the real pipeline — JPEG re-encoding, resizing, tokenization, unit rounding, physical capture. State the budget as a class plus magnitude, and justify it by what an attacker can actually deliver. A budget larger than the channel permits inflates the risk; smaller understates it.

3. **Establish the clean baseline.** Record clean performance on the same slices robustness will be measured on, so the trade is visible per slice rather than only in aggregate.

4. **Design the attack suite.** Cover the attacker-knowledge assumptions in scope: white-box gradient attacks where weights are known, transfer attacks from a surrogate for grey-box, and query-based/decision-based attacks for black-box under the stated query budget. For each, state the stopping criterion.

5. **Adapt the attacks to the defense.** For every defensive component present, describe how an attacker aware of it would change approach — differentiable approximation of a non-differentiable step, expectation over randomized transforms, attacking before rather than after a preprocessing stage. The un-adapted number is reported only as a contrast, never as the headline.

6. **Check for gradient masking.** Look for the signatures: single-step attacks outperforming iterative ones, unbounded budgets failing to reach 0% accuracy, random sampling beating gradient descent, black-box beating white-box. If any appears, the white-box number is invalid — re-run gradient-free and report that instead.

7. **Measure per slice, not only in aggregate.** Report robust accuracy by class and by any slice with operational meaning; adversarial vulnerability concentrates, and an aggregate number hides the class an attacker will actually target.

8. **Quantify the trade.** Put clean and robust accuracy side by side against the deployment tolerance, and state what was given up.

9. **Report as a bound with its conditions.** Present the result as "no attack we ran reduced accuracy below X under budget B and knowledge assumption K", followed by what would invalidate it.

**Output Format:**

A markdown assessment:
- **Threat Model** — knowledge, goal, query budget, value of a flip; assumptions labelled.
- **Perturbation Budget** — class, magnitude, and the channel-based justification.
- **Attack Suite** — table: Attack family | Knowledge assumption | Budget | Stopping criterion | Adapted to which defense.
- **Gradient-Masking Check** — each signature, observed or not, and the consequence.
- **Results** — table: Slice | Clean | Robust (per attack) | Worst-case robust.
- **Robustness Statement** — the bound, its conditions, and what would invalidate it.
- **Trade-off** — clean accuracy given up vs deployment tolerance.
- **Recommended Next Step** — accept, harden (route to the defense prompt), or reduce exposure.
- **INSUFFICIENT EVIDENCE** — the mandatory robustness statement whenever any gradient-masking signature was observed, or where attacks were not adapted to the defense in force. An unadapted attack measures the attack, not the model, and a robustness number produced under masking is an upper bound presented as a floor. Name the unblocking datum: the adapted attack (or gradient-free alternative) that must be run before any number is reported.

## Verification

- [ ] The perturbation budget is justified by the input channel, not by convention.
- [ ] Every defensive component present has a correspondingly adapted attack.
- [ ] All four gradient-masking signatures are checked and reported.
- [ ] Robust accuracy is reported per slice as well as in aggregate.
- [ ] Clean accuracy appears beside every robust number.
- [ ] Attack convergence evidence is stated for each attack family.
- [ ] The headline result is phrased as an upper bound with conditions, never as a guarantee.
- [ ] No published robustness figures are asserted from memory; unknowns are `[verify against a primary source]`.
- [ ] No working attack code or reusable exploit harness appears.
- [ ] Where a masking signature appears or attacks were not adapted to the defense, the robustness statement is INSUFFICIENT EVIDENCE with the adapted attack named — no robust-accuracy figure is reported.

## False-Positive Prevention

❌ **DON'T:**
- Report "92% robust accuracy" as a property of the model — it is a property of the attack you ran, at the budget you chose, under the knowledge you assumed.
- Run a fixed attack suite against a new defense and treat survival as evidence; the defense was designed after those attacks existed.
- Accept a high white-box number without checking for gradient masking — the most common cause of an impressive robustness result is a broken gradient, not a strong model.
- Choose a perturbation budget because it is the conventional one for the dataset rather than because it matches what this channel delivers.
- Report aggregate robust accuracy only; the attacker targets the weakest class, not the mean.
- Describe robustness to one perturbation class as robustness, unqualified.

✅ **DO:**
- State the exact triple — budget, knowledge, attack — that every number is conditional on.
- Adapt each attack to each defensive component, and show the un-adapted number only as a contrast.
- Treat any gradient-masking signature as invalidating the white-box result and switch attack class.
- Justify the budget from re-encoding, resizing, rounding, or physical capture — whatever the channel actually does.
- Break results out by class and operational slice, and lead with the worst.
- Phrase the conclusion as a lower bound on attacker cost and name what would invalidate it.

## Example Output

```markdown
## Adversarial Robustness: Document-Fraud Image Classifier v3
Binary classifier over uploaded document photos; a "genuine" verdict releases a payout.

### Threat Model
Grey-box: architecture family is public, weights are not. Attacker uploads images and
observes only accept/reject. Query budget ~200 per account before rate limiting.
Goal is **targeted** — forged → "genuine". A flip is worth the payout value.

### Perturbation Budget
Uploads are re-encoded to JPEG q=85 and resized to 384×384 before inference. Perturbations
must survive both. Budget stated as bounded L∞ **after** the re-encode/resize stage, plus a
separate physical-print-and-recapture class, since the attacker can print and rephotograph.
Pixel-space budgets defined before re-encoding overstate attacker reach here.

### Attack Suite
| Attack family | Knowledge | Budget | Stopping criterion | Adapted to |
|---|---|---|---|---|
| Iterative gradient, surrogate | grey (surrogate) | L∞ post-encode | loss plateau, 3 restarts | — (transfer baseline) |
| Transfer from 3 surrogates | grey | same | ensemble agreement | preprocessing stage |
| Decision-based query attack | black | 200 queries | query budget exhausted | rate limiter |
| Expectation-over-transform | grey | same | plateau over 20 transform draws | JPEG + resize defense |

### Gradient-Masking Check
| Signature | Observed | Consequence |
|---|---|---|
| Single-step beats iterative | No | — |
| Unbounded budget fails to reach 0% | **Yes** — floors at 11% | White-box surrogate number is unreliable |
| Random sampling beats gradient descent | No | — |
| Black-box beats white-box | No | — |
Because the unbounded budget floors, the surrogate-gradient result is reported only as a
contrast; the **decision-based query attack** result is the headline.

### Results
| Slice | Clean | Transfer | Query-based | EOT | Worst-case |
|---|---|---|---|---|---|
| Overall | 0.971 | 0.905 | **0.842** | 0.878 | **0.842** |
| Passport | 0.983 | 0.941 | 0.902 | 0.925 | 0.902 |
| Utility bill | 0.944 | 0.831 | **0.706** | 0.788 | **0.706** |

Utility bills are the exposed class — 24 points below clean under the query attack, and the
class with the lowest clean accuracy to begin with.

### Robustness Statement
No attack we ran reduced overall accuracy below **0.842** under a post-re-encode L∞ budget
with grey-box knowledge and a 200-query budget. This is an upper bound: a stronger or
better-adapted attack can lower it. It is invalidated by any of — raising the per-account
query budget, exposing scores instead of a binary verdict, or removing the JPEG re-encode.

### Trade-off
Clean accuracy is unchanged (no robust training applied); all robustness here comes from the
preprocessing pipeline, which was not designed as a defense. Deployment tolerance allows a
2-point clean loss, so robust training remains available as a lever.

### Recommended Next Step
Harden the utility-bill class specifically → `mlsec_adversarial_defense_strategy.md`. Do not
publish a robustness claim from the transfer numbers; the masking signature invalidates them.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** attack family × knowledge assumption × slice is the measurement grid.
- **DS-02 (Metric Specification):** robust accuracy is defined together with its budget, knowledge assumption, and attack, so the number is interpretable.
- **QA-12 (False Positives Identification):** the gradient-masking check exists to reject robustness results that are artefacts.
- **CM-02 (Constraint Specification):** adaptive-attack and no-fabrication rules bound what may be claimed.
- **RT-05 (Evidence-Based Reasoning):** every claim is tied to a measured slice under stated conditions.

**Related Prompts:**
- `mlsec_adversarial_defense_strategy.md` — once you know where the model is weak.
- `mlsec_ml_threat_model.md` — establishes whether evasion is worth measuring at all.
- `../model-evaluation-validation/mleval_robustness_stress_testing.md` — non-adversarial distribution shift.
- `../model-evaluation-validation/mleval_ood_detection_design.md` — flagging inputs that fall outside the trained distribution.
