---
title: "Privacy Technique Selection"
category: AI-ML/responsible-ai-governance
description: "Choose among anonymization, synthetic data, differential privacy, federated learning, and access control by first naming the specific disclosure each is meant to prevent, then matching techniques to threats rather than assembling a portfolio of privacy-sounding controls."
techniques:
  - RT-02
  - DS-06
  - CM-02
  - QA-12
  - RT-10
difficulty: advanced
tags:
  - privacy
  - differential-privacy
  - federated-learning
  - synthetic-data
  - technique-selection
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_differential_privacy_design.md
  - domain-AI-ML/responsible-ai-governance/rai_federated_learning_governance.md
  - domain-AI-ML/responsible-ai-governance/rai_privacy_pii_assessment.md
  - domain-AI-ML/model-security/mlsec_membership_inference_defense.md
---

# Privacy Technique Selection

**Objective:** Pick the privacy techniques an ML system actually needs by naming the specific disclosure each is meant to prevent, matching techniques to those disclosures, and rejecting the ones that address a threat this system does not face — so the result is a defensible set of controls rather than a portfolio of privacy-sounding measures.

**When to Use:**
- Before committing to differential privacy, federated learning, or synthetic data, when the choice has not yet been made on evidence.
- When a privacy review has produced a list of recommended techniques and you need to know which ones earn their utility cost.
- When a stakeholder asks "are we doing enough for privacy?" and the honest answer requires naming what "enough" is protecting against.

**When NOT to Use:**
- The technique is already chosen and you need to implement it — use the specific prompt (`rai_differential_privacy_design.md`, `rai_federated_learning_governance.md`).
- You need a regulatory obligation mapping rather than a technical selection — use `rai_gdpr_automated_decisioning_assessment.md` or `rai_privacy_pii_assessment.md`.
- The concern is an attacker extracting the model or its training content — use `../model-security/`.

## Inputs / Context

- **Data subjects and sensitivity** — who is in the data, and what disclosure would harm them.
- **Disclosure scenarios feared** — stated concretely: who learns what, how, and with what consequence.
- **Data topology** — centralized, siloed across organizations, or on user devices; this constrains what is even possible.
- **Who sees what today** — model outputs, training data, aggregates, and the artifact itself, by audience.
- **Utility floor** — the performance below which the system stops being worth building.
- **Regulatory or contractual constraints** — obligations already in force, as stated by the people who own them.

## Constraints

**Must:**
- Require at least one concrete disclosure scenario before recommending any technique — "who learns what about whom, and what happens then". A technique without a named threat is unjustifiable.
- State for each candidate technique what it protects against **and what it leaves fully exposed**; every one of these has a large uncovered area, and conflating them is the standard error.
- Separate the **unit of protection** — record, user, group, or organization — and check it against the disclosure scenario, since a mismatch silently voids the protection.
- Price utility cost for each candidate against the stated floor.
- Recommend *not* applying a technique where its threat is absent, and say so explicitly.

**Must Not:**
- Present anonymization or pseudonymization as protection against inference attacks; they address stored fields, not model behaviour.
- Present synthetic data as private by construction — a generative model trained on sensitive data can reproduce it, and the synthetic set inherits whatever the generator memorized.
- Assert privacy-budget values, re-identification rates, or utility-loss figures from memory; mark any needed figure `[verify against a primary source]` or `[measure on your data]`.
- Recommend a stack of techniques without stating how they interact and which ones are redundant.
- Treat any technique here as satisfying a legal obligation — route that determination to the people who own it.

**Instructions:**

1. **Write the disclosure scenarios.** For each fear, state the adversary, what they learn, through what channel, and the consequence. Vague scenarios produce vague controls; if none can be written, the honest output is that no technique is currently justified.

2. **Classify each scenario by channel.** Which of these is the leak path: the stored data, an aggregate or report, model outputs, the model artifact, or a cross-organization data movement? The channel determines the candidate set — techniques that act on a different channel are irrelevant regardless of merit.

3. **Fix the unit of protection per scenario.** Record, user, group, or organization. A user with many records is not protected by a record-level guarantee; a group is not protected by a per-user one. This step is where most privacy stacks quietly fail.

4. **Screen candidates against channel and unit.**
   - *Access control and minimization* — stored data. Cheapest, always applicable, never sufficient alone.
   - *Anonymization / pseudonymization* — stored fields. Does nothing about model behaviour or inference.
   - *Aggregation thresholds* — reports and aggregates. Nothing about a trained model.
   - *Synthetic data* — data sharing. Protects only if the generator itself is privacy-protected; otherwise it moves the problem.
   - *Differential privacy* — a formal bound on individual influence, at the unit it is defined over. Applies to training, aggregates, or queries — say which.
   - *Federated learning* — data movement only. Prevents raw data centralization; does **not** by itself bound what the model reveals.
   - *Output restriction* — model outputs. Direct effect on inference attacks, cost paid by legitimate consumers.

5. **Price utility for each surviving candidate** against the stated floor, marking estimates as `[measure on your data]` rather than asserting figures.

6. **Check interactions and redundancy.** Federated learning plus DP is a common and coherent pair — federated addresses movement, DP addresses what the model reveals. Synthetic data plus DP is coherent only if DP is applied to the generator. Anonymization plus DP is largely redundant for the inference channel. Name the redundancies so budget is not spent twice.

7. **Recommend, including the declines.** For each scenario, the technique chosen, the unit, and the residual. For each rejected candidate, the scenario it would have addressed and why that scenario does not apply here.

8. **State the residual disclosure.** What remains possible after everything recommended, in the terms of the original scenarios.

**Output Format:**

A markdown selection memo:
- **Disclosure Scenarios** — table: Scenario | Adversary | What they learn | Channel | Unit of protection needed | Consequence.
- **Candidate Screening** — table: Technique | Channel it acts on | Unit it protects | Protects against | Leaves exposed | Utility cost.
- **Recommendation** — per scenario: technique, unit, residual.
- **Declined** — technique, the scenario it would address, why that scenario is absent here.
- **Interactions & Redundancy** — which combinations are coherent, which are duplicative.
- **Residual Disclosure** — what is still possible, in scenario terms.

## Verification

- [ ] At least one concrete disclosure scenario exists before any technique is recommended.
- [ ] Each scenario names adversary, channel, unit, and consequence.
- [ ] Every candidate states both what it protects against and what it leaves exposed.
- [ ] The unit of protection is checked against each scenario, not assumed.
- [ ] Utility costs are marked as estimates to measure rather than asserted.
- [ ] Redundant combinations are identified.
- [ ] At least one technique is explicitly declined with its reason, where applicable.
- [ ] Residual disclosure is stated in the language of the original scenarios.
- [ ] No privacy budgets or re-identification rates are asserted from memory.
- [ ] No technique is described as satisfying a legal obligation.

## False-Positive Prevention

❌ **DON'T:**
- Recommend differential privacy because privacy matters — without a scenario it addresses, you have bought a utility loss and no protection.
- Treat federated learning as a privacy guarantee; it changes where data sits, and a model trained federatively can still leak its training records.
- Call synthetic data private because no real record was copied — the generator can memorize, and the synthetic set inherits exactly what it memorized.
- Apply a record-level guarantee to a scenario about a person with many records and report the person as protected.
- Stack five techniques and describe it as defense-in-depth when three of them act on a channel this system's threat does not use.
- Quote a privacy budget as though it were a standard setting; the number is meaningless without its unit and its scenario.

✅ **DO:**
- Demand a concrete scenario — adversary, channel, consequence — before any technique enters consideration.
- Match technique to channel first; a control acting on a different channel is irrelevant however strong it is.
- State the unit explicitly and re-check it against the scenario, since this is where stacks silently fail.
- Write what each technique leaves exposed next to what it covers.
- Name redundant pairs so effort is not spent twice on the same channel.
- Decline techniques out loud, with the absent scenario named, so the omission is reviewable.

## Example Output

```markdown
## Privacy Technique Selection: Multi-Hospital Sepsis-Risk Model
Three hospitals want a shared model. Data cannot leave each site.

### Disclosure Scenarios
| # | Adversary | Learns | Channel | Unit needed | Consequence |
|---|---|---|---|---|---|
| S1 | Partner hospital | Another site's raw patient records | data movement | organization | contractual and regulatory breach |
| S2 | Model consumer | That a named person was a patient at site B | model outputs | **patient** (multi-visit) | disclosure of a care episode |
| S3 | Researcher with the artifact | Reconstructed attributes of rare-condition patients | artifact | patient | re-identification of a small cohort |
| S4 | Internal analyst | Identified records while building dashboards | stored data | record | avoidable over-access |

### Candidate Screening
| Technique | Channel | Unit | Protects against | Leaves exposed | Utility cost |
|---|---|---|---|---|---|
| Access control + minimization | stored data | record | S4 | S1–S3 entirely | none |
| Pseudonymization | stored fields | record | part of S4 | **all of S2, S3** — inference is unaffected | none |
| Aggregation thresholds | reports | record | dashboard leakage | S2, S3 | small |
| Federated learning | **data movement** | organization | **S1** | **S2, S3 — model still leaks** | coordination + convergence cost |
| DP-SGD, patient-level | training | **patient** | S2, S3 | cross-site correlation of the same patient | AUC cost `[measure on your data]` |
| Synthetic data | sharing | depends on generator | nothing here unless the generator is DP | S2, S3 if generator is not protected | high |
| Output banding | model outputs | record | part of S2 | S3 | clinicians lose fine ordering |

### Recommendation
| Scenario | Technique | Unit | Residual |
|---|---|---|---|
| S1 | Federated learning | organization | update contents still reveal site-level distributions |
| S2, S3 | **DP-SGD at patient level** | patient | budget bounds influence; does not cover a patient treated at two sites under different IDs |
| S4 | Access control + minimization | record | ordinary insider risk |

Federated learning and patient-level DP are the coherent pair here: federated answers "the raw
data must not move", DP answers "the model must not reveal the person". Choosing only one would
leave a named scenario uncovered — which is exactly the mistake this selection exists to prevent.

### Declined
- **Synthetic data** — would address a data-sharing scenario nobody has raised; the sites want a
  shared *model*, not a shared dataset. Applying it would cost utility and address nothing.
- **Pseudonymization as a privacy control** — retained as hygiene for S4, but it is explicitly
  **not** counted toward S2 or S3; identifier removal has no effect on what a trained model reveals.

### Interactions & Redundancy
- Federated + DP: **coherent**, different channels.
- Pseudonymization + DP for the inference channel: **redundant** — DP does the work; do not
  budget pseudonymization as an inference control.
- Output banding + DP: partially redundant for S2; adopt banding only if the DP budget lands at a
  utility cost the clinical team refuses.

### Residual Disclosure
A patient treated at two of the three sites under different identifiers is protected as two
patients, not one. Nothing recommended here closes that, because no site can link them without
undoing S1. If that scenario matters, it needs a governance answer — a shared linkage authority —
not another technique.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** scenario × channel × unit × technique is the selection grid.
- **DS-06 (Prioritization and Severity Guidance):** scenarios are ranked by consequence so utility budget goes to the disclosure that matters.
- **CM-02 (Constraint Specification):** the scenario-first rule and the leaves-exposed requirement bound what may be recommended.
- **QA-12 (False Positives Identification):** rejects techniques that act on a channel this system's threat does not use.
- **RT-10 (Troubleshooting Decision Tree):** channel then unit then candidate is a decision path, not a checklist.

**Related Prompts:**
- `rai_differential_privacy_design.md` — once DP is selected, to choose the unit and budget properly.
- `rai_federated_learning_governance.md` — once federated learning is selected.
- `rai_privacy_pii_assessment.md` — the compliance-facing assessment this informs.
- `../model-security/mlsec_membership_inference_defense.md` — measures whether the output-channel scenario is real before you pay for it.
