---
title: "Model Risk Brief for Executives"
category: AI-ML/ai-product-leadership
description: "Translate a model's technical risks and controls into a one-page executive brief that an accountable leader can read, question, and sign off on without an ML background."
techniques:
  - ST-03
  - RP-02
  - NE-13
  - DS-01
  - CM-02
difficulty: intermediate
tags:
  - model-risk
  - governance
  - executive-brief
  - accountability
  - controls
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_ai_policy_authoring.md
  - domain-AI-ML/ai-product-leadership/aipm_jargon_translator_for_stakeholders.md
  - domain-AI-ML/ai-product-leadership/aipm_mlops_maturity_for_leaders.md
---

# Model Risk Brief for Executives

**Objective:** Produce a concise, plain-language executive brief on a model's material risks and the controls that mitigate them — so an accountable leader (who is not an ML practitioner) can understand the exposure, ask the right questions, and make an informed go/no-go or sign-off decision.

**When to Use:**
- A model is approaching launch and needs executive or risk-committee sign-off.
- A regulator, auditor, or board asks "what could go wrong with this model and how do we control it?"
- Periodic governance review of a deployed model.

**When NOT to Use:**
- You need the full technical validation report for ML reviewers (that's an eval/validation artifact, not this brief).
- You're authoring org-wide AI policy (use `aipm_ai_policy_authoring.md`).

## Inputs / Context

- **Model purpose** — what decision/action it drives and who is affected.
- **Deployment context** — customer-facing vs internal, automated vs human-in-loop, scale.
- **Known performance** — headline metrics, slice/fairness results, calibration, failure modes (provide real numbers; do not let the brief invent them).
- **Existing controls** — monitoring, human review, fallback, kill switch, retraining cadence.
- **Regulatory/compliance surface** — applicable regimes (e.g., EU AI Act risk tier, sector rules).

## Constraints

**Must:**
- Write for a non-technical accountable executive; every technical term is either avoided or defined in one clause.
- State, for each material risk, the likelihood, the impact if it happens, and the specific control that reduces it — no risk without a paired control or an explicit "unmitigated" flag.
- Make the residual risk and the recommended decision explicit.

**Must Not:**
- Fabricate metrics, fairness results, or incident statistics; if a number is unknown, say "not yet measured" and flag it as a gap.
- Hide a serious unmitigated risk behind reassuring language.
- Substitute generic "AI can be biased" boilerplate for risks specific to this model's data and use.

**Instructions:**

1. **State the model in one sentence.** What it predicts/generates, the decision it drives, and who bears the consequences if it's wrong.

2. **Classify the stakes.** Map the use to a risk tier (harm-if-wrong, who's affected, reversibility, regulatory tier). This sets how much scrutiny the rest deserves; reference a recognized framework (e.g., NIST AI RMF, EU AI Act tiers) where it helps.

3. **Enumerate material risks.** Cover performance/accuracy, fairness across groups, robustness/drift, security/misuse, explainability gaps, and operational/dependency risk. Keep only risks that are material for THIS model.

4. **Pair each risk with a control.** For every risk, name the mitigation in place (monitoring threshold, human review, fallback, retraining) and rate residual exposure as Low/Med/High.

5. **Flag the gaps.** Explicitly list risks with weak or missing controls, and what it would take to close them.

6. **Translate metrics to consequence.** Convert key numbers into "what this means" — e.g., what a given error rate implies for affected users per month.

7. **Recommend and assign.** Give a clear recommendation (ship / ship-with-conditions / hold), the conditions, the named accountable owner, and the review cadence.

**Output Format:**

A one-to-two-page markdown brief:
- **What This Model Does** — one paragraph, plain language.
- **Risk Tier & Why** — classification and the standard referenced.
- **Material Risks → Controls** — table: Risk | Likelihood | Impact | Control | Residual.
- **Open Gaps** — risks not yet adequately controlled + what closes them.
- **Recommendation** — ship/conditions/hold, accountable owner, review cadence.

## Verification

- [ ] No undefined jargon; an MBA-level reader can follow it.
- [ ] Every material risk paired with a control and a residual rating, or flagged unmitigated.
- [ ] All numbers are real inputs or marked "not yet measured" — none invented.
- [ ] Risk tier references a recognized framework.
- [ ] Recommendation names an accountable owner and a review cadence.

## False-Positive Prevention

❌ **DON'T:**
- Reassure the executive that "controls are in place" when a key risk has no actual control.
- List generic AI risks that don't apply to this model's data/use.
- Bury a high residual-risk item in the middle of a long list.
- Present aggregate accuracy as evidence of fairness.

✅ **DO:**
- State residual risk honestly, including "High — no mitigation yet" where true.
- Tailor risks to this model's actual data, population, and decision.
- Lead with the highest residual-risk items so they aren't missed.
- Require slice/fairness evidence (not aggregate metrics) before claiming the model is equitable.

## Example Output

```markdown
## Model Risk Brief — Credit Pre-Qualification Model v2

### What This Model Does
Estimates the likelihood an applicant pre-qualifies for a card, ranking applicants
so reviewers prioritize the most promising. A human makes every final decision.

### Risk Tier & Why
High-risk under EU AI Act (creditworthiness / access to financial services). Affects
consumers; outcomes are consequential. → Strong controls + documentation required.

### Material Risks → Controls
| Risk | Likelihood | Impact | Control | Residual |
|---|---|---|---|---|
| Disparate approval rates by protected group | Med | High | Quarterly fairness audit (4/5 ratio); slice monitoring | Med |
| Drift as economy shifts | Med | Med | Monthly PSI monitoring; retrain trigger | Low |
| Over-reliance (reviewers rubber-stamp) | Med | High | UI shows score as advisory; audit of override rate | Med |
| Explainability for adverse-action notices | High | High | SHAP-based reason codes mapped to compliant language | Low |

### Open Gaps
- Intersectional fairness (e.g., age × geography) not yet measured. Closing it: ~2 weeks
  of slice analysis before next review. Until then, residual on fairness stays "Med, partially blind."

### Recommendation
**Ship with conditions:** human-in-loop preserved, intersectional fairness measured within
30 days, override-rate audit live. Accountable owner: VP Credit Risk. Review: quarterly.
```

**Techniques Used:**
- **ST-03 (Output Format Specification):** a fixed one-page brief structure.
- **RP-02 (Audience-Specific Framing):** written for a non-technical accountable executive.
- **NE-13 (Technical-to-Business Translation):** metrics rendered as consequence.
- **DS-01 (Framework Application):** risk tiering via NIST RMF / EU AI Act.
- **CM-02 (Constraint Specification):** every risk constrained by a paired control or gap flag.

**Related Prompts:**
- `aipm_ai_policy_authoring.md` — the org-wide rules this model must comply with.
- `aipm_jargon_translator_for_stakeholders.md` — tune the language for other audiences.
- `aipm_mlops_maturity_for_leaders.md` — assess whether the controls can actually be operated.
