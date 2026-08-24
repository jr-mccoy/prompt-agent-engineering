---
title: "Fairness Metric Selection"
category: AI-ML/responsible-ai-governance
description: "Choose a defensible fairness definition and metric for a specific decision context, surfacing the mathematical impossibility tradeoffs between competing criteria."
techniques:
  - RT-02
  - CM-02
  - DS-02
  - QA-12
  - RP-02
difficulty: advanced
tags:
  - fairness
  - metric-selection
  - impossibility-theorem
  - responsible-ai
  - tradeoffs
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_bias_detection_audit.md
  - domain-AI-ML/responsible-ai-governance/rai_fairness_mitigation_strategy.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
---

# Fairness Metric Selection

**Objective:** Help a team select an appropriate, defensible fairness definition and metric for a specific decision context — making explicit which harms the metric protects against, which it ignores, and the mathematical tradeoffs that make it impossible to satisfy several fairness criteria at once.

**When to Use:**
- Before a bias audit, to fix the definition the audit will measure against.
- When stakeholders disagree about what "fair" means for a system.
- When a model must satisfy a contractual, policy, or regulatory fairness obligation.
- When a previously chosen metric is producing perverse or contested outcomes.

**When NOT to Use:**
- To measure disparities (use `rai_bias_detection_audit.md` once a definition is set).
- To pick a mitigation technique (use `rai_fairness_mitigation_strategy.md`).
- When the system makes no consequential decision about people (a different review applies).

## Inputs / Context

Provide what you can:
- **Decision and harm profile** — what the model decides, who is affected, and whether the dominant harm is a false positive or false negative for the affected person.
- **Base rates** — whether the true outcome prevalence differs by group, and how reliable the labels are per group.
- **Intervention type** — punitive (e.g., fraud flag), allocative (e.g., loan, job), or assistive (e.g., outreach), since this changes which metric matters.
- **Applicable framework/regulation** — ask the user which one governs; do not assume.
- **Operational constraints** — whether a single threshold must apply to everyone, and whether group-specific thresholds are permissible.

## Constraints

**Must:**
- Map each candidate fairness definition to the specific harm it protects against and the harm it tolerates.
- State explicitly that demographic parity, equalized odds, and calibration generally cannot all hold simultaneously when base rates differ, and explain the consequence for this context.
- Recommend a primary definition with a justification grounded in the decision's harm profile, plus secondary metrics to monitor.

**Must Not:**
- Recommend a fairness metric as "the fair one" without naming what it sacrifices.
- Invent statutory or framework requirements; if the legal/standard requirement is unknown, say so and ask the user to confirm which regulation applies.
- Imply a single metric guarantees freedom from discrimination claims.

**Instructions:**

1. **Characterize the harm profile.** Determine whether the costly error for the affected person is a false positive or false negative, and whether the decision allocates a benefit, imposes a burden, or offers assistance.

2. **Enumerate candidate definitions.** Lay out the realistic options (e.g., demographic/statistical parity, equal opportunity, equalized odds, predictive parity/calibration, treatment equality) with a one-line meaning each.

3. **Map definition → protected harm → tolerated harm.** For each candidate, state precisely what it equalizes and what disparity it permits to persist.

4. **Surface the impossibility tradeoff.** Given the base-rate situation, name which definitions are mutually exclusive here and what choosing one implies for the others.

5. **Filter by operational and legal constraints.** Eliminate definitions ruled out by single-threshold requirements or by the governing framework (as confirmed by the user), noting where the requirement is unknown.

6. **Recommend a primary + monitoring set.** Choose one definition as the optimization/compliance target and list secondary metrics to watch so a regression on a sacrificed dimension is visible.

7. **Document the value judgment.** State, in plain terms, the ethical/business choice the selection encodes, so reviewers can contest it deliberately rather than by accident.

**Output Format:**

A markdown decision brief:
- **Context Summary** — decision, harm profile, base-rate situation, governing framework (or "to be confirmed")
- **Candidate Definitions** — table: Definition | Equalizes | Tolerates | Fits this harm profile?
- **Impossibility Note** — which criteria conflict here and why
- **Recommendation** — primary definition + justification; monitoring metrics
- **Value Judgment Stated** — the explicit ethical/business choice
- **Open Questions** — unknown legal requirements, missing base-rate data

## Verification

- [ ] The dominant harm (FP vs FN, allocative vs punitive) is identified before metrics are compared.
- [ ] Each candidate states both what it protects and what it tolerates.
- [ ] The impossibility tradeoff is named explicitly for this base-rate situation.
- [ ] The recommendation includes the value judgment it encodes, in plain language.
- [ ] No framework/statute requirement is invented; unknowns are flagged for user confirmation.

## False-Positive Prevention

❌ **DON'T:**
- Present demographic parity as universally "fair" without noting it can require unequal treatment of equally qualified people when base rates differ.
- Claim a model can simultaneously satisfy calibration and equalized odds under unequal base rates.
- Pick a metric because it is popular rather than because it matches the harm profile.
- Treat metric selection as purely technical — it is a value choice.

✅ **DO:**
- Tie the choice to whether a false positive or false negative is worse for the affected person.
- State the impossibility tradeoff explicitly and which criteria are sacrificed.
- Name the ethical/business judgment the chosen metric encodes.
- Keep secondary metrics to detect regression on the dimensions you sacrificed.

## Example Output

```markdown
## Fairness Metric Selection: Pretrial Risk-Assistance Tool (assistive framing)

### Context Summary
- Decision: flags defendants for *supportive services*, not detention (assistive).
- Costly error for the person: a false negative (missing someone who needs support).
- Base rates: differ across groups; label quality (rearrest) is itself contested.
- Governing framework: **to be confirmed by user.**

### Candidate Definitions
| Definition | Equalizes | Tolerates | Fits? |
|---|---|---|---|
| Demographic parity | Selection rate across groups | Unequal error rates | Partial |
| Equal opportunity | TPR (catch rate) across groups | Unequal FPR | Strong (FN is the harm) |
| Calibration | Score meaning across groups | Unequal TPR/FPR | Weak here |

### Impossibility Note
With differing base rates, equal opportunity and calibration cannot both hold. Choosing equal opportunity sacrifices exact calibration parity.

### Recommendation
Primary: **equal opportunity** — the dominant harm is a missed person who needs support. Monitor selection-rate disparity and calibration drift as secondary metrics.

### Value Judgment Stated
We are choosing to equalize who gets *helped* among those who need it, accepting that score-to-risk mapping may differ slightly by group.

### Open Questions
- Confirm whether any regulation mandates a specific definition before locking this in.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** definitions compared across protected vs tolerated harms.
- **CM-02 (Constraint Specification):** operational/legal constraints filter candidates.
- **DS-02 (Metric Specification):** maps each definition to its concrete metric.
- **QA-12 (False Positives Identification):** guards against "one true fairness metric" errors.
- **RP-02 (Audience-Specific Framing):** states the value judgment for non-technical stakeholders.

**Related Prompts:**
- `rai_bias_detection_audit.md` — measure against the chosen definition.
- `rai_fairness_mitigation_strategy.md` — reduce disparities on the chosen metric.
- `rai_model_risk_assessment.md` — situate the fairness harm in overall model risk.
