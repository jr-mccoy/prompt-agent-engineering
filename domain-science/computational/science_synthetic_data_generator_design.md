---
title: "Synthetic / Surrogate Data Generation Designer"
category: science/computational
description: "Design surrogate data that preserves the structure needed for code testing or privacy-preserving sharing while breaking real identities, with explicit privacy-vs-utility tradeoff, disclosure-risk checks, and utility checks."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
  - NE-10
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_data_dictionary_designer.md
  - domain-science/computational/science_data_management_plan_drafter.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Synthetic / Surrogate Data Generation Designer

**Objective:** Specify a synthetic-data generation design that preserves the structural properties needed for downstream use (schema, types, ranges, marginal distributions, key correlations, missingness pattern) while deliberately breaking real identities and exact records — so the surrogate can be shared or used to test code without disclosure risk. The design pairs a generation approach with a disclosure-risk check and a utility check, and is framed as a controlled-data-handling aid, not a license to share real data.

**When to use:** Real data cannot be shared (consent, law, governance) but you need a shareable test fixture, a privacy-preserving public companion dataset, or a fixture to develop and CI-test analysis code against.

**Required inputs:**
- **Discipline.** Field of study.
- **Study type.** Observational / experimental / survey / computational.
- **Use case.** Code testing/CI fixture, privacy-preserving public sharing, demo/teaching, or stress-testing.
- **Source data description.** Schema / variable list / data dictionary (mark `[user-supplied]` if not yet documented).
- **Disclosure sensitivity.** Why the real data cannot be shared (human subjects, CARE-governed Indigenous data, commercial, location-sensitive).

**Optional inputs:**
- Which structural properties matter most for the use case (drives preserve/break decisions).
- Acceptable privacy budget / re-identification risk tolerance.
- Whether differential-privacy guarantees are required.
- Existing real-data summary statistics that may be released.
- Governance approval status for releasing summary statistics.

**Constraints — Must:**
- Produce a SPEC TABLE mapping each structural property → preserve or break → generation method → check.
- Explicitly enumerate what must be preserved (schema, column types, valid ranges, marginal distributions, key correlations/joint structure, missingness pattern) versus deliberately broken (real identities, exact records, true linkages).
- Cover candidate generation approaches and their tradeoffs: rule/distribution-based sampling, resampling/bootstrap with perturbation, model-based generation (e.g., CTGAN-class generative models, described conceptually), and differential-privacy mechanisms (noise addition / DP synthesizers).
- State the privacy-vs-utility tradeoff explicitly and pick a point on it with justification (probability-weighted: characterize the likelihood and impact of disclosure under each option).
- Include a disclosure-risk check: confirm no real record is reproduced verbatim, assess re-identification and membership-inference risk, and apply a k-anonymity-style sanity check on quasi-identifiers.
- Include a utility check: confirm code/tests behave as on real data, and that preserved distributions/correlations match within stated tolerance.
- State explicitly that synthetic data is NOT a substitute for IRB / data-governance / CARE approval to share real data, and that releasing even summary statistics may itself require approval.

**Constraints — Must Not:**
- Do not invent citations, DOIs, funder policy text, repository names, or accession numbers. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not claim a method is "privacy-preserving" without a stated disclosure-risk check and threat model.
- Do not assume differential privacy is in effect unless a mechanism and budget are specified.
- Do not reproduce or memorize real records; the design generates surrogates, it does not copy.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in the spec.

**Instructions:**

1. **Confirm scope.** Restate discipline, study type, use case, and why real data cannot be shared. Set the framing: this is a controlled-data-handling, non-default branch of Open Science.
2. **Inventory structure to preserve vs break.** From the schema/dictionary, list each property and decide preserve or break against the use case (code-testing needs schema/types/edge cases; public sharing needs distributions/correlations but must break identities and exact records).
3. **Define the threat model.** Name the adversary and attack of concern (re-identification via quasi-identifiers, membership inference, attribute disclosure), and the risk tolerance (mark `[user-supplied]` if not given).
4. **Choose a generation approach.** Compare rule/distribution-based, resampling+perturbation, model-based (CTGAN-class), and DP mechanisms; pick one (or a hybrid) and justify against utility needs and the threat model. Use probability-weighted reasoning over disclosure likelihood × impact.
5. **Set the privacy-vs-utility point.** State the tradeoff explicitly: what utility is intentionally sacrificed to lower disclosure risk, and vice versa. If DP is used, specify the mechanism and that a budget must be set (`[user-supplied]`).
6. **Specify the generation recipe.** Per variable/group: distribution or model, parameters or fit source (mark `[user-supplied]`), how missingness is reproduced, and how correlations are induced.
7. **Design the disclosure-risk check (adversarial).** No verbatim real records; nearest-neighbor distance to real records above threshold; quasi-identifier k-anonymity-style check; membership-inference sanity test. State pass/fail criteria.
8. **Design the utility check.** Schema/type validity; marginal and key-joint distribution comparison within tolerance; code/test suite passes identically; edge cases represented.
9. **State boundaries and approvals.** Reaffirm that synthetic data does not replace IRB/governance/CARE approval, note any approval still required (including for summary-stat release), and list residual risks.

**Output format (locked):**

```
## Synthetic-data design
Discipline: [...] | Study type: [...] | Use case: [...] | Branch: Controlled-data-handling (non-default)
Why real data not shareable: [...] | Risk tolerance: [...]/[user-supplied]
Threat model: [re-identification / membership inference / attribute disclosure]
Generation approach: [rule | resample+perturb | model-based (CTGAN-class) | DP mechanism] | Justification: [...]
Privacy-vs-utility point: [what is preserved vs sacrificed]

## Property spec table
| Structural property | Preserve / Break | Generation method | Check |
|---|---|---|---|
| Schema & column types | Preserve | [...] | Schema/type validation |
| Valid ranges | Preserve | [...] | Range check |
| Marginal distributions | Preserve | [...] | Distribution comparison (tol [...]) |
| Key correlations / joint structure | Preserve | [...] | Correlation comparison (tol [...]) |
| Missingness pattern | Preserve | [...] | Missingness comparison |
| Real identities | Break | [...] | No verbatim record; NN-distance > threshold |
| Exact records / true linkages | Break | [...] | Membership-inference sanity test |

## Disclosure-risk check (pass criteria)
- [ ] No real record reproduced verbatim
- [ ] Nearest-neighbor distance to real records above threshold [user-supplied]
- [ ] k-anonymity-style check on quasi-identifiers (k ≥ [user-supplied])
- [ ] Membership-inference advantage below tolerance

## Utility check (pass criteria)
- [ ] Schema & types valid; downstream code/tests pass as on real data
- [ ] Marginals & key joints within tolerance
- [ ] Edge cases represented

## Boundaries
- Synthetic data does NOT substitute for IRB / data-governance / CARE approval to share real data.
- Residual risks & approvals still required: [...]/[user-supplied]
```

**Reporting-standard alignment:** FAIR principles (the synthetic companion supports reuse); CARE principles (Indigenous data governance) where applicable; differential-privacy framing for formal guarantees; disclosure-risk concepts (re-identification, membership inference, k-anonymity). Governance/policy specifics referenced by intent only — `[user-supplied]`/verify.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, and use case are stated; branch labeled controlled-data-handling.
- [ ] Preserve/break decision is explicit for every structural property.
- [ ] A threat model is named, not assumed away.
- [ ] Generation approach is chosen with a stated privacy-vs-utility tradeoff.
- [ ] Both a disclosure-risk check and a utility check have pass/fail criteria.
- [ ] No verbatim real records are reproduced; the design generates surrogates only.
- [ ] DP is only claimed if a mechanism and budget are specified.
- [ ] The IRB/governance/CARE non-substitution boundary is stated; no promotional language.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Privacy theater | "Synthetic" data that memorizes/copies real outlier records | Require no-verbatim + nearest-neighbor-distance check; outliers are highest risk |
| Unstated DP | Calling Gaussian noise "differential privacy" with no budget | Only claim DP with a named mechanism and a set/marked budget |
| Utility collapse | Privacy so aggressive that code behaves differently than on real data | Require the utility check; compare distributions/correlations within tolerance |
| Correlation loss | Marginals match but joint structure (key correlations) is destroyed | Test joint/correlation structure, not just per-variable marginals |
| Approval bypass | Treating synthetic generation as governance clearance to share real data | State explicitly it is not a substitute for IRB/governance/CARE approval |
