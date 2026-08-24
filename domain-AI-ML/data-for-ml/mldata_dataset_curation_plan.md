---
title: "ML Dataset Curation Plan"
category: AI-ML/data-for-ml
description: "Plan how to assemble and curate a dataset for a defined ML task — sources, sampling, coverage, quality gates, and governance — so the data reflects the deployment population and is defensible later."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - dataset-curation
  - sampling
  - coverage
  - data-governance
  - data-collection
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_sampling_bias_audit.md
  - domain-AI-ML/data-for-ml/mldata_datasheet_authoring.md
  - domain-AI-ML/data-for-ml/mldata_data_quality_audit.md
---

# ML Dataset Curation Plan

**Objective:** Produce a concrete, end-to-end plan for assembling and curating a dataset for a clearly defined ML task — specifying which sources to draw from, how to sample, what coverage to guarantee, what quality gates to apply, and how to govern access and consent — so that the resulting dataset matches the deployment population and survives later scrutiny.

**When to Use:**
- You are starting a new ML project and need to build (not just download) the training data.
- An existing dataset is being expanded or rebuilt and you want a principled plan rather than ad-hoc scraping.
- You need a curation plan reviewers (legal, privacy, ML lead) can sign off on before collection starts.

**When NOT to Use:**
- The dataset already exists and you only need to check its quality (use `mldata_data_quality_audit.md`).
- You only need to decide how to split an assembled dataset (use `mldata_train_test_split_strategy.md`).
- You only need to document an existing dataset (use `mldata_datasheet_authoring.md`).

## Inputs / Context

Provide what you can; the plan degrades gracefully if some are missing:
- **Task definition** — prediction target, unit of analysis (row = ?), and the moment of inference in production.
- **Deployment population** — who/what the model will run on (geographies, segments, device types, time period), and how it may differ from any data you already have.
- **Candidate sources** — internal tables, logs, vendors, public datasets, manual collection; their licensing/consent status.
- **Volume & budget** — target size, labeling budget, time constraints.
- **Constraints** — privacy/PII rules, regulatory regime, retention limits, fairness requirements.

## Constraints

**Must:**
- Tie every sourcing and sampling decision back to matching the *deployment population*, not just maximizing volume.
- State coverage targets across the dimensions that matter for the task (segments, classes, time, edge cases) and how each will be hit.
- Specify governance for each source: license/consent, PII handling, retention, and access control.

**Must Not:**
- Recommend a specific dataset size, source quality, or class distribution as fact when it depends on inputs the user has not given — ask, or present it as a parameter to set.
- Assume a convenience sample (whatever is easiest to collect) represents the deployment population without flagging the gap.
- Invent licensing or consent status for a source; if unknown, list it as a blocking open question.

**Instructions:**

1. **Restate the task and the unit of analysis.** Fix what one row represents, the target, and the prediction-time boundary, since these govern every sampling choice. Surface ambiguity now.

2. **Characterize the deployment population.** Enumerate the dimensions along which the live data will vary (segment, geography, time, class, rare-but-critical cases). This is the target distribution the curated set must approximate.

3. **Inventory and rank candidate sources.** For each source, capture availability, volume, freshness, label availability, license/consent, PII exposure, and known biases. Rank by fit-to-population and governance risk.

4. **Design the sampling strategy.** Choose how rows are drawn (random, stratified by segment/class, time-windowed, targeted oversampling of rare cases) and justify it against the population characterization. State target counts per stratum.

5. **Define coverage and edge-case targets.** List the slices that must be represented and the minimum count each needs to be analyzable, including failure-prone and safety-critical cases.

6. **Specify quality gates at intake.** Define what is rejected or flagged on entry (dedup rules, validity checks, schema conformance) so curation, not cleanup-later, enforces quality.

7. **Lay out governance.** For each source: license/consent basis, PII minimization/redaction, retention window, access controls, and the sign-offs required before collection.

8. **Sequence the plan and name the risks.** Give an ordered collection plan with milestones, plus the top risks (coverage gaps, source drift, consent blockers) and how each will be detected and mitigated.

**Output Format:**

A markdown plan:
- **Task & Population Summary** — unit of analysis, target, deployment-population dimensions.
- **Source Inventory** — table: Source | Volume | Labels | License/Consent | PII | Known Bias | Fit (H/M/L).
- **Sampling & Coverage Plan** — strata, target counts, edge-case quotas.
- **Quality Gates at Intake** — accept/reject/flag rules.
- **Governance** — per-source consent, PII, retention, access, sign-offs.
- **Sequenced Plan & Risks** — milestones + ranked risks with mitigations and open questions.

## Verification

- [ ] Every sampling decision is justified against the named deployment population, not convenience.
- [ ] Coverage targets name specific slices and minimum counts, including edge/safety-critical cases.
- [ ] Each source has an explicit license/consent and PII status (or is flagged as an open question).
- [ ] Intake quality gates are concrete enough to implement (rules, not aspirations).
- [ ] Top coverage and governance risks are listed with a detection and mitigation for each.

## False-Positive Prevention

❌ **DON'T:**
- Treat "more data" as the goal — a larger convenience sample that misses deployment segments is worse than a smaller representative one.
- Assume a source represents the live population just because it is internal and large.
- Copy a class distribution from the available data when the deployment base rate differs.
- Defer all licensing/PII questions to "legal later" and present an unconstrained plan.

✅ **DO:**
- Anchor sampling to the deployment population and call out where available sources under-cover it.
- Set explicit per-slice coverage quotas, including rare-but-critical cases, before collection starts.
- Mark unknown license/consent/PII status as a blocking open question, not an assumption.
- Distinguish the distribution you *have* from the distribution you *need*, and plan the gap closure.

## Example Output

```markdown
## Dataset Curation Plan: Merchant Fraud Classifier v1

### Task & Population Summary
- Unit of analysis: one transaction at authorization time.
- Target: fraud / not-fraud, label confirmed via chargeback within 90 days.
- Deployment population: ~6 countries, card-present + card-not-present, all merchant
  categories; live base rate of fraud estimated ~0.4%.

### Source Inventory
| Source | Volume | Labels | License/Consent | PII | Known Bias | Fit |
|---|---|---|---|---|---|---|
| Internal auth logs (24mo) | ~180M | Partial (chargebacks) | Owned, ToS covers | High (PAN, geo) | Skews US/large merchants | H |
| Manual review queue | ~40K | Strong (analyst label) | Owned | High | Only suspicious cases | M |
| Vendor consortium feed | ~5M | Strong | License TBD ⚠ | Tokenized | Unknown sampling | M |

### Sampling & Coverage Plan
- Stratify by country × channel; floor of 20K labeled fraud cases per major country.
- Oversample card-not-present fraud (rare but rising) to ≥15% of positives.
- Edge-case quotas: first-time-merchant txns ≥5K; refund-abuse pattern ≥2K.

### Quality Gates at Intake
- Reject rows missing auth timestamp or merchant_id.
- Flag and quarantine exact-duplicate auth IDs.
- Validate amount ≥ 0 and currency in supported set.

### Governance
- Internal logs: PAN tokenized at intake; 24-month retention; row-level access via fraud-team role.
- Vendor feed: BLOCKED pending license confirmation (open question O-1).

### Sequenced Plan & Risks
1. Lock task + population sign-off → 2. Pull/stratify internal logs → 3. Resolve vendor license →
   4. Manual-label edge-case shortfalls.
- Risk: US-skew under-covers EU merchants (detect via per-country counts; mitigate with targeted EU pull).
- Open question O-1: vendor consortium license terms unknown — blocks that source.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** task → population → sources → sampling → governance proceeds in fixed order.
- **RT-02 (Multi-Dimensional Analysis Framework):** sources and coverage are evaluated across volume, fit, governance, and bias.
- **CM-02 (Constraint Specification):** deployment population and governance act as governing constraints on every choice.
- **DS-06 (Prioritization & Severity Guidance):** sources ranked by fit; risks ranked with mitigations.
- **QA-01 (Self-Verification):** the verification checklist gates the plan before collection.

**Related Prompts:**
- `mldata_sampling_bias_audit.md` — after collection, check the sample against the deployment population.
- `mldata_datasheet_authoring.md` — document the curated dataset for reuse and audit.
- `mldata_data_quality_audit.md` — verify intake quality gates actually held.
