---
title: "ML Datasheet Authoring"
category: AI-ML/data-for-ml
description: "Author a Datasheet for a dataset across motivation, composition, collection, preprocessing, uses, distribution, and maintenance — documenting limitations and known biases honestly, not just contents."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - datasheet
  - dataset-documentation
  - data-governance
  - transparency
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_dataset_curation_plan.md
  - domain-AI-ML/data-for-ml/mldata_data_versioning_lineage.md
  - domain-AI-ML/data-for-ml/mldata_sampling_bias_audit.md
---

# ML Datasheet Authoring

**Objective:** Produce a Datasheet for a dataset following the Datasheets-for-Datasets structure — Motivation, Composition, Collection, Preprocessing/Cleaning/Labeling, Uses, Distribution, and Maintenance — that documents not only what the dataset contains but its limitations, known biases, consent basis, and inappropriate uses, so downstream users can judge fitness honestly.

**When to Use:**
- Releasing, sharing, or formally registering a dataset (internally or externally).
- Onboarding a dataset into a governed catalog or model-risk process.
- A dataset is widely reused and its limitations/intended uses are undocumented.

**When NOT to Use:**
- You are planning how to build the dataset (use `mldata_dataset_curation_plan.md`).
- You need versioning/lineage infrastructure rather than a content document (use `mldata_data_versioning_lineage.md`).

## Inputs / Context

Provide what you can; the datasheet flags gaps where information is missing rather than inventing it:
- **Dataset overview** — name, version, size, format, what one instance represents.
- **Purpose & creator** — why it was created, by whom, funding/sponsor.
- **Composition** — fields, label scheme, splits, sensitive attributes, known subpopulations.
- **Collection process** — sources, sampling, time period, consent/licensing basis.
- **Preprocessing/labeling** — cleaning, transforms, labeling process and guidelines used.
- **Known issues** — biases, gaps, errors, distribution caveats already understood.
- **Distribution & maintenance** — how it's shared, license, who maintains it, update cadence.

## Constraints

**Must:**
- Cover all seven Datasheet sections; where information is unavailable, state "Unknown" or "Not documented" explicitly rather than omitting the question.
- Document limitations, known biases, sensitive attributes, and *inappropriate* uses, not just contents.
- State the consent/licensing basis and any PII handling honestly.

**Must Not:**
- Invent collection details, demographic composition, consent status, or bias assessments the user did not provide — mark them as gaps to fill.
- Present the dataset as bias-free or universally applicable; absence of evidence is not evidence of fairness.
- Recommend uses the data cannot support, or omit known risky/inappropriate uses.

**Instructions:**

1. **Establish identity and motivation.** Capture name/version/size and *why* the dataset was created, by whom, and for what task — this frames every later judgment of fitness.

2. **Document composition.** Describe what an instance is, the fields and label scheme, splits, the presence of sensitive attributes, subpopulations, and any relationships between instances; note missing data honestly.

3. **Document the collection process.** Record sources, sampling method, time window, who/what collected it, and the consent/licensing basis; flag where the sample may diverge from a target population.

4. **Document preprocessing, cleaning, and labeling.** Describe transforms applied, what raw data was kept, and the labeling process (annotators, guideline version, agreement) so reuse can reconstruct or question it.

5. **Specify uses — including inappropriate ones.** State the intended task, uses the dataset is known to support, and uses it should *not* be put to given its limitations and biases.

6. **Document distribution and licensing.** Record how the dataset is/should be distributed, the license/terms, access restrictions, and any IP or regulatory constraints.

7. **Document maintenance.** Name the maintainer, update/versioning cadence, deprecation/erratum process, and how consumers learn of changes (cross-link versioning/lineage).

8. **Surface limitations and gaps.** Consolidate known biases, coverage gaps, and undocumented items into an explicit limitations section so the datasheet's honesty is visible at a glance.

**Output Format:**

A markdown Datasheet with these sections:
- **Motivation** — purpose, creators, funding.
- **Composition** — instances, fields, labels, splits, sensitive attributes, missingness.
- **Collection Process** — sources, sampling, time, consent/licensing.
- **Preprocessing / Cleaning / Labeling** — transforms, labeling process, agreement.
- **Uses** — intended, supported, and *inappropriate* uses.
- **Distribution** — license, access, restrictions.
- **Maintenance** — maintainer, cadence, errata.
- **Limitations & Known Biases** — consolidated, explicit; unknowns marked.

## Verification

- [ ] All seven Datasheet sections are present; unavailable items say "Unknown/Not documented," not omitted.
- [ ] Sensitive attributes, known biases, and a limitations section are documented, not glossed.
- [ ] Inappropriate / unsupported uses are stated, not only intended uses.
- [ ] Consent/licensing basis and PII handling are stated honestly.
- [ ] No collection, composition, or bias detail is invented; gaps are flagged for follow-up.

## False-Positive Prevention

❌ **DON'T:**
- Fill unknown fields (demographics, consent, agreement) with plausible-sounding guesses to make the datasheet look complete.
- Describe only contents and intended use while omitting limitations, biases, and inappropriate uses.
- Imply the dataset is representative or fair without slice evidence to support it.
- Bury the consent/licensing status or PII handling.

✅ **DO:**
- Mark every unavailable item explicitly as "Unknown/Not documented" so gaps are visible and assignable.
- Devote a real section to limitations, known biases, sensitive attributes, and uses to avoid.
- Tie any fairness/representativeness claim to actual slice evidence, or state that none exists.
- Document consent, licensing, and PII handling plainly, including restrictions on reuse.

## Example Output

```markdown
## Datasheet: Customer Support Intent Dataset v2

### Motivation
- Created to train intent classification for the support chatbot. Built by the ML Platform team; internally funded.

### Composition
- 142,000 instances; one = a support message. Fields: text, intent (5 classes), channel, timestamp.
- Splits: 70/15/15 grouped by customer_id. Sensitive attributes: none collected directly; language field present.
- Missingness: channel null in 3.2% of rows (legacy import). Subpopulations: 88% English; other languages sparse.

### Collection Process
- Source: production support inbox, Jan 2024–Mar 2026. Sampling: stratified by channel.
- Consent/licensing: covered by support ToS; customer text pseudonymized at intake. PII scrubbing applied (see below).

### Preprocessing / Cleaning / Labeling
- PII redaction (emails, phone, order IDs) via regex + review. Labeling: internal ops, guideline v1.3; Bug↔How-to κ=0.71.

### Uses
- Intended: intent routing. Supported: intent classification, weak-supervision signals.
- INAPPROPRIATE: non-English routing (sparse); sentiment/PII inference; demographic analysis (attributes absent).

### Distribution
- Internal only; not for external release. License: internal use; subject to data-handling policy.

### Maintenance
- Maintainer: ML Platform. Quarterly refresh; errata logged; changes signaled via dataset version bump.

### Limitations & Known Biases
- English-skewed; non-English performance untested. Bug↔How-to boundary noisy. No demographic slices → fairness UNKNOWN.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** authoring proceeds through the seven Datasheet sections in order.
- **ST-03 (Output Format Specification):** locks the standardized Datasheet structure.
- **DS-01 (Framework Application):** applies the Datasheets-for-Datasets framework.
- **RT-05 (Evidence-Based Reasoning):** representativeness/bias claims must be evidence-backed or marked unknown.
- **QA-01 (Self-Verification):** the checklist enforces completeness and honesty about gaps.

**Related Prompts:**
- `mldata_dataset_curation_plan.md` — produces much of the collection/sampling content this documents.
- `mldata_data_versioning_lineage.md` — the versioning the maintenance section references.
- `mldata_sampling_bias_audit.md` — generates the representativeness evidence for the limitations section.
