---
title: "Replication Audit — Assess Likelihood a Published Finding Will Replicate"
category: research-academic/critical-appraisal
description: "Assess whether a published finding is likely to replicate. Walks through study design strength, sample size and power, novelty (lower base rate), p-value and effect-size patterns, conflicts of interest, prior independent confirmation, fit with adjacent literature, and pre-registration / open data signals. Outputs a replication-likelihood estimate with the highest-leverage check the user could do."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - replication
  - critical-appraisal
  - p-hacking
  - publication-bias
  - methodology
updated: "2026-05-10"
reasoning:
  styles: [adversarial, statistical, base-rate]
  stakes: variable
  horizon: hours_to_days
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: audit_with_estimate
  user_role: [researcher, clinician, analyst, journalist, methodologist]
  mode: [audit, diagnose]
related_prompts:
  - domain-research-academic/research_evidence_map.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md
  - domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
---

# Replication Audit

**Objective:** Assess whether a published finding is likely to replicate. Walk through the predictors of non-replication that have emerged from the meta-science literature, score the finding against them, and produce an estimated replication likelihood with the highest-leverage check the user could perform if they want to invest more.

**When to use:**
- Considering whether to act on a single study's finding (clinical, policy, business decisions).
- Evaluating a recent finding before citing it.
- Adversarial review of a paper.
- Teaching critical appraisal.

**When NOT to use:**
- Findings already replicated in independent samples (use the replication evidence directly).
- Findings from very small / early literatures where any single result is preliminary by design.
- Findings irrelevant to your decision (replication audit is expensive; spend it where it matters).

**Audience:** Researchers, clinicians, journalists, methodologists, analysts evaluating single-study evidence.

---

## Inputs / Context

1. **The finding.** Specific claim, with paper citation.
2. **Field.** Different fields have different baseline replication rates.
3. **Decision tied to the finding.** Affects how much rigor to spend on the audit.
4. **Whether independent replications already exist.**

---

## Predictors of non-replication (from meta-science)

| Predictor | What weakens replication |
|-----------|--------------------------|
| Small sample | Underpowered to detect true effects; if positive, may be inflated |
| p-value near 0.05 | Suggests p-hacking pressure; "just significant" findings replicate worse |
| Large effect size | Often regression-to-mean candidate; second study finds smaller |
| Novel finding | Lower prior probability; many novel findings don't survive |
| Single study, no independent replication | Replication unknown |
| Field-baseline | Some fields replicate ~40%, some ~80% |
| Lack of pre-registration | More researcher degrees of freedom |
| Lack of open data | Cannot independently verify analysis |
| Conflicts of interest | Publication / analytic bias possible |
| Result inconsistent with adjacent literature | Either a real surprise or an error |
| Outcome-switch suspicion | Reported outcome differs from pre-specified |
| Multiple comparisons without correction | Inflated false-positive rate |
| Author career incentive (junior, tenure) | More publication-bias pressure |
| Hot media topic | Higher pressure to publish positive |

## Constraints

### Must
- Score the finding against each predictor.
- Estimate **field baseline replication rate** if known (e.g., clinical psychology ~40%, economics ~60%, biomedical varies wildly).
- Compute estimated replication likelihood as **base rate adjusted by predictor scores**.
- Identify the **single highest-leverage check** the user could do (often: looking for an independent replication, checking pre-registration, examining the supplement for outcome switch, computing observed power).
- Include an **adversarial caveat**: ways the audit itself could be wrong.

### Must Not
- Replace replication audit with citation count or journal prestige.
- Use a single predictor as decisive.
- Skip the field baseline.
- Estimate replication likelihood to two decimals.
- Treat "we couldn't find a replication" as evidence of non-replication; it may simply mean nobody tried.

---

## Instructions

### Step 1 — Finding and field
Restate finding. Identify field and field's known replication baseline.

### Step 2 — Score predictors
Per predictor: positive (replication-favorable), neutral, negative (replication-unfavorable). Justify each.

### Step 3 — Replication-evidence search
- Has any independent replication been attempted? Result?
- Has any meta-analysis included this finding? Pooled direction?
- Is there a registered replication report?

### Step 4 — Estimate replication likelihood
Base rate (field) + adjustments:
- Predictor scores
- Replication evidence (if any)
- Adjacent literature consistency

Output as a range (e.g., "30–50%") rather than point.

### Step 5 — Highest-leverage check
The single check most likely to update your estimate substantially. Common high-leverage checks:
- Look up the pre-registration document and compare to reported outcomes
- Compute observed power
- Search for unpublished replication attempts
- Examine the supplement for analytic flexibility signals

### Step 6 — Decision implication
Given replication likelihood, what should the user do?
- **High (>70%):** treat the finding as likely real.
- **Moderate (40–70%):** treat as suggestive; don't make load-bearing decisions on it alone.
- **Low (<40%):** treat as preliminary; require independent confirmation before action.

### Step 7 — Adversarial caveat
- The audit could be wrong because: [reasons — e.g., field baseline may not apply, predictors may not generalize to this study, audit may miss strengths the study has]
- Confidence in the audit itself: [low / moderate / high]

---

## False-Positive Prevention

1. **Citation count as proxy.** Citation count tracks attention, not replicability. Don't use.
2. **Journal prestige as proxy.** High-prestige journals have publication-bias pressure too.
3. **Single-predictor lock.** Small sample alone isn't fatal if other predictors are strong.
4. **Replication-attempt blindness.** Search for replications before estimating; their result is the strongest signal.
5. **Field-baseline ignorance.** A 60% replication estimate is meaningless without knowing the field baseline.
6. **False precision.** Round to 10% increments.
7. **Adversarial-caveat skip.** Audits can be wrong.

---

## Output Format

```
# Replication audit — [finding]

## Finding
> [Verbatim claim with citation]

## Field
- Field: [...]
- Baseline replication rate (if known): [...]

## Predictor scores
| Predictor | Score | Justification |
|-----------|-------|----------------|
| Sample size | [+/0/−] | [...] |
| p-value pattern | [+/0/−] | [...] |
| Effect size | [+/0/−] | [...] |
| Novelty | [+/0/−] | [...] |
| Pre-registration | [+/0/−] | [...] |
| Open data | [+/0/−] | [...] |
| Conflicts of interest | [+/0/−] | [...] |
| Adjacent-lit consistency | [+/0/−] | [...] |
| Multiple comparisons | [+/0/−] | [...] |
| Author incentives | [+/0/−] | [...] |
| Outcome-switch signals | [+/0/−] | [...] |

## Replication evidence
- Independent replications attempted: [list / none found]
- Meta-analyses including: [list]
- Registered replication reports: [list / none]

## Estimated replication likelihood
- Base rate: [field baseline]
- Adjustments: [direction and magnitude]
- **Estimated likelihood: [range]**

## Highest-leverage check
- [Specific action]
- Why: [most likely to update the estimate]
- Cost: [time / access]

## Decision implication
- Likelihood [high / moderate / low]
- Recommended action: [act / suggestive / require confirmation]

## Adversarial caveat
- Audit could be wrong because: [...]
- Confidence in audit: [low / moderate / high]
```

---

## Verification

- [ ] Field baseline replication rate stated.
- [ ] All predictors scored with justification.
- [ ] Replication evidence search performed.
- [ ] Likelihood expressed as range, not point.
- [ ] Highest-leverage check identified.
- [ ] Decision implication matched to likelihood.
- [ ] Adversarial caveat present.
- [ ] No citation-count or journal-prestige proxies.
- [ ] No false precision.
