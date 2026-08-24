---
title: "RAI Privacy & PII Assessment"
category: AI-ML/responsible-ai-governance
description: "Assess an ML system's privacy risk — PII exposure, membership inference, and memorization — and select proportionate mitigations (minimization, differential privacy) measured against utility, without overclaiming protection."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - privacy
  - pii
  - membership-inference
  - memorization
  - differential-privacy
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_red_teaming_plan.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_ethics_review_protocol.md
---

# RAI Privacy & PII Assessment

**Objective:** Assess where an ML system creates privacy risk — PII flowing into training/inference, membership-inference exposure, and memorization/extraction of training data — and recommend proportionate mitigations (data minimization, de-identification, differential privacy, access controls) measured against their utility cost, without overstating the protection they provide.

**When to Use:**
- Before training or deploying a model on data about people.
- When a model (especially generative) may memorize and reveal training data.
- To assess privacy risk for a governance/legal review.

**When NOT to Use:**
- As the legal privacy/DPIA determination — this is a technical pre-assessment that feeds legal review.
- For fairness/bias — use `rai_bias_detection_audit.md`.

## Inputs / Context

- **Data inventory** — what personal data enters training, fine-tuning, prompts, logs; sensitivity tiers; sources and consent basis.
- **Model type & exposure** — generative vs discriminative; public vs internal; whether outputs/logs are retained or shown to others.
- **Attack surface** — can an adversary query freely (membership inference), or extract verbatim training text (memorization)?
- **Existing controls** — minimization, de-identification, encryption, access control, retention limits, DP if any.
- **Regulation/framework in scope** — if any (ask the user; do not assume a specific privacy law applies).

## Constraints

**Must:**
- Trace personal data through the full lifecycle (collection → training → inference → logging → retention), flagging exposure points.
- Distinguish risk *types*: PII exposure (data flow), membership inference (was X in the training set), and memorization/extraction (verbatim reproduction).
- Pair each mitigation with its utility cost and its actual protection scope/limit.

**Must Not:**
- Claim a technique "anonymizes" data or "guarantees privacy" — de-identification can be re-identifiable; DP provides a *bounded, parameterized* guarantee, not absolute privacy.
- State a differential-privacy epsilon's "safety" categorically; report the parameter and its meaning, and note it as a tradeoff, not a guarantee of no harm.
- Fabricate a legal privacy threshold or claim compliance; ask the user which regulation applies and route legal conclusions to counsel.

**Instructions:**

1. **Map the data lifecycle.** Trace personal data from collection through retention; mark each point where PII is stored, processed, exposed, or logged, and its sensitivity.

2. **Assess PII exposure.** Identify unnecessary PII collection, PII in prompts/logs, and PII shown across users; apply the minimization lens (is each field necessary?).

3. **Assess membership-inference risk.** Judge whether an adversary could infer that a specific record was in the training set, considering model overfitting, output confidence exposure, and query access.

4. **Assess memorization/extraction risk.** For generative models, assess the chance of regurgitating verbatim training data (especially rare/unique records); recommend extraction tests (link to red-team).

5. **Evaluate candidate mitigations.** For each risk, consider minimization, de-identification/pseudonymization, aggregation, access/retention controls, output filtering, and differential privacy — stating protection scope and utility cost.

6. **State the limits honestly.** For each mitigation, note what it does NOT protect against (e.g., de-identification ≠ anonymization; output filtering ≠ preventing inference).

7. **Rank risks and recommend a treatment plan.** Prioritize by sensitivity × likelihood × population, and recommend a proportionate mitigation set with measured utility impact where possible.

8. **Route legal questions.** Flag determinations (lawful basis, anonymization standard, breach thresholds) for counsel under the user's confirmed jurisdiction.

**Output Format:**

A markdown assessment:
- **Data Lifecycle Map** — exposure points with sensitivity.
- **Risk Findings** — table: Risk | Type (PII/MI/memorization) | Likelihood | Affected | Evidence vs estimate.
- **Mitigation Options** — table: Mitigation | Protects against | Does NOT protect against | Utility cost.
- **Recommended Treatment Plan** — ranked, proportionate.
- **Tests Needed** — e.g., extraction/membership-inference probes.
- **Legal Handoff** — items for counsel + confirmed jurisdiction.
- **INSUFFICIENT EVIDENCE** — an enumerated value in the evidence column, and the correct state of the memorization and membership-inference rows until a probe has actually been run. Model architecture and training-set size do not establish leakage in either direction; name the unblocking datum, which is the probe listed under Tests Needed.

## Verification

- [ ] Personal data is traced across the full lifecycle, not just training.
- [ ] The three risk types are assessed distinctly.
- [ ] Each mitigation states what it does AND does NOT protect against.
- [ ] DP is described as a bounded/parameterized tradeoff, not absolute privacy.
- [ ] No claim of "anonymized" without justification, and no fabricated legal thresholds.
- [ ] Legal determinations are routed to counsel under a confirmed jurisdiction.
- [ ] Memorization and membership-inference risks are marked INSUFFICIENT EVIDENCE until the corresponding probe has run — architecture alone establishes neither presence nor absence.

## False-Positive Prevention

❌ **DON'T:**
- Call de-identified data "anonymous" — re-identification via linkage is common.
- Claim differential privacy "guarantees" privacy without stating epsilon and its meaning.
- Assume a discriminative model can't leak training data (membership inference still applies).
- Declare compliance with a privacy law from a technical assessment.

✅ **DO:**
- Distinguish de-identification from anonymization and state re-identification risk.
- Report DP as a parameterized tradeoff with a stated epsilon and utility cost.
- Assess membership inference even for non-generative models.
- Route compliance conclusions to legal under the confirmed jurisdiction.

## Example Output

```markdown
## Privacy & PII Assessment: Personalized Recommendation Model

### Data Lifecycle Map
Collection: account + behavioral data (PII: email, location-coarse). Training: includes user_id-linked features. Inference: real-time. Logging: prompts+outputs retained 1yr (contains PII). Exposure point: logs accessible to support team (broad access).

### Risk Findings
| Risk | Type | Likelihood | Affected | Evidence/Est |
|---|---|---|---|---|
| PII in 1yr logs, broad access | PII exposure | High | All users | Evidenced |
| Precise location collected, unused | PII over-collection | High | All users | Evidenced |
| Membership inference via confidence | MI | Medium | Outlier users | Estimate (untested) |

### Mitigation Options
| Mitigation | Protects against | Does NOT protect | Utility cost |
|---|---|---|---|
| Drop precise location | Over-collection | MI, memorization | None (unused) |
| Log access control + 30d retention | PII exposure | Inference attacks | None |
| Output confidence rounding | MI (partial) | Memorization | Minor ranking impact |
| DP-SGD (ε to be set) | MI + memorization (bounded) | Absolute privacy | Measurable accuracy drop |

### Recommended Treatment Plan
1. Drop precise location (free win). 2. Tighten log access + retention. 3. Run MI/extraction test before deciding on DP-SGD.

### Tests Needed
Membership-inference probe; extraction test (route to red-team).

### Legal Handoff
Confirm jurisdiction + lawful basis + retention limits with counsel.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** lifecycle → three risk types → mitigations → plan.
- **RT-02 (Multi-Dimensional Analysis Framework):** mitigations across protection scope and utility.
- **DS-06 (Prioritization & Severity Guidance):** ranks by sensitivity × likelihood × population.
- **QA-12 (False Positives Identification):** blocks "anonymized"/"guaranteed privacy" overclaims.
- **CM-02 (Constraint Specification):** minimization and the DP tradeoff as governing constraints.

**Related Prompts:**
- `rai_red_teaming_plan.md` — run extraction/membership-inference probes.
- `rai_model_risk_assessment.md` — fold privacy risks into the register.
- `rai_ethics_review_protocol.md` — consent and data-use ethics.
