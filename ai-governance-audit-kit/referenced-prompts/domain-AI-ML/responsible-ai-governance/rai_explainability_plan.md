---
title: "RAI Explainability Plan"
category: AI-ML/responsible-ai-governance
description: "Plan model explanations matched to audience and decision stakes — choosing among SHAP, LIME, counterfactuals, and surrogate models — while respecting the known limits and instability of post-hoc methods."
techniques:
  - RT-02
  - DS-01
  - CM-02
  - RP-02
  - QA-12
difficulty: intermediate
tags:
  - explainability
  - shap
  - counterfactual
  - audience-fit
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_interpretability_analysis.md
  - domain-AI-ML/responsible-ai-governance/rai_model_card_authoring.md
  - domain-AI-ML/responsible-ai-governance/rai_ethics_review_protocol.md
---

# RAI Explainability Plan

**Objective:** Produce an explainability plan that matches explanation methods (SHAP, LIME, counterfactuals, surrogate models, example-based) to the audience and the decision stakes, specifying what each explanation can and cannot legitimately claim, so explanations inform rather than mislead.

**When to Use:**
- When a model affects people and they (or regulators/operators) need to understand its decisions.
- Before choosing an XAI tool, to avoid picking a method that doesn't fit the audience or question.
- When existing explanations are confusing, contradictory, or unstable.

**When NOT to Use:**
- To validate the model's *internal* global behavior — use `rai_interpretability_analysis.md`.
- As a fairness audit — explanations describe behavior, they don't establish fairness.

## Inputs / Context

- **Audience(s)** — affected end users, operators/reviewers, data scientists, auditors/regulators — each needs a different explanation.
- **Decision stakes** — reversible/low-stakes vs irreversible/high-stakes; whether a legal right to explanation may apply (ask the user).
- **Model type** — inherently interpretable (linear/tree) vs opaque (deep net/ensemble); local vs global question.
- **Explanation question** — "why this decision?" (local) vs "how does the model behave overall?" (global) vs "what would change the outcome?" (counterfactual).
- **Operational constraints** — latency budget for real-time explanations, tooling, stability requirements.
- **Regulation/framework in scope** — if any (ask the user; do not assume a right-to-explanation exists).

## Constraints

**Must:**
- Match each explanation method to a specific audience and a specific question (local/global/counterfactual).
- State the known limits of each method: post-hoc explanations approximate the model and can be unstable, can disagree with each other, and do not establish causation.
- Recommend the simplest method that answers the question for the audience.

**Must Not:**
- Present a SHAP/LIME attribution as a causal account of the real-world phenomenon — it explains the model, not the world.
- Promise a "legal right to explanation" is satisfied unless the user confirms the jurisdiction and the obligation; if unknown, say the legal requirement is unconfirmed.
- Recommend a method whose instability is unacceptable for the stakes without saying so.

**Instructions:**

1. **Segment audiences and their questions.** For each audience, state what decision they make with the explanation and whether they need local, global, or counterfactual explanations.

2. **Match stakes to fidelity.** Higher stakes demand more faithful, more stable explanations (or an inherently interpretable model). Decide whether a transparent model should replace post-hoc explanation entirely.

3. **Select methods per audience.** Map candidates — SHAP, LIME, counterfactual/recourse, surrogate, example/prototype — to each audience-question pair, with the reason.

4. **State each method's limits.** For each chosen method, write what it can claim and what it cannot (approximation error, instability across runs, disagreement with other methods, non-causality).

5. **Design counterfactual recourse if decisions are contestable.** For people denied something, specify actionable, realistic recourse explanations ("what would change this") rather than only attributions.

6. **Specify validation and stability checks.** Define how you'll test explanation stability (re-run, perturb) and consistency across methods before trusting them.

7. **Plan delivery.** Specify format, language level, and latency per audience; ensure end-user explanations avoid raw feature jargon.

**Output Format:**

A markdown plan:
- **Audience × Question Matrix** — table: Audience | Decision they make | Local/Global/Counterfactual | Recommended method | Why.
- **Stakes-to-Fidelity Mapping** — and whether an interpretable model should replace post-hoc XAI.
- **Method Limits** — per chosen method: can claim / cannot claim.
- **Recourse Design** (if applicable) — actionable counterfactuals.
- **Validation & Stability Plan** — tests before trusting explanations.
- **Delivery Spec** — format, language, latency per audience.
- **Open Questions** — legal/right-to-explanation items to confirm.

## Verification

- [ ] Each method is tied to a specific audience AND a specific question type.
- [ ] Each method's limits (approximation, instability, non-causality) are stated.
- [ ] Stakes drive the fidelity requirement, including the interpretable-model option.
- [ ] Recourse explanations are actionable where decisions are contestable.
- [ ] A stability/consistency validation step exists before explanations are trusted.
- [ ] Any legal explanation right is user-confirmed, not assumed.

## False-Positive Prevention

❌ **DON'T:**
- Present SHAP values as the real-world causes of an outcome.
- Give an affected end user a raw feature-attribution chart and call it an explanation.
- Trust a single LIME run without checking stability across re-runs/perturbations.
- Assume two XAI methods agreeing means the explanation is correct.

✅ **DO:**
- Frame attributions as explaining the model's behavior, not causation.
- Translate explanations into the audience's language and decisions.
- Test explanation stability and method-agreement before relying on them.
- For high stakes, consider an inherently interpretable model over post-hoc patching.

## Example Output

```markdown
## Explainability Plan: Mortgage Underwriting Assist Model

### Audience × Question Matrix
| Audience | Decision | Type | Method | Why |
|---|---|---|---|---|
| Applicant (denied) | Whether/how to reapply | Counterfactual/recourse | Actionable counterfactuals | Needs "what to change," not attributions |
| Underwriter | Approve/override | Local | SHAP (per-decision) | Familiar, per-feature contribution |
| Compliance auditor | Sign-off | Global + sample local | Surrogate tree + SHAP summaries | Needs overall behavior + spot checks |
| Data scientist | Debug | Local + global | SHAP + PDP | Diagnostic depth |

### Stakes-to-Fidelity Mapping
High stakes (credit denial). Considered an interpretable scorecard model; retained the ensemble but require stability-validated explanations and human override.

### Method Limits
- SHAP: explains the model's output given features; NOT a causal account; values shift with background-data choice.
- Counterfactuals: must be realistic and actionable (don't suggest "reduce age").

### Recourse Design
For denials, surface 2–3 realistic, within-applicant-control changes that would flip the decision (e.g., reduce utilization below X%).

### Validation & Stability Plan
Re-run SHAP across 5 background samples; flag features whose sign flips. Compare SHAP vs counterfactual for consistency on 50 cases.

### Delivery Spec
Applicant: plain-language recourse letter. Underwriter: in-tool SHAP panel, <300ms.

### Open Questions
- Confirm whether a statutory adverse-action explanation requirement applies in scope.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** audience × question × stakes matrix.
- **DS-01 (Framework Application):** applies the XAI method taxonomy.
- **CM-02 (Constraint Specification):** stakes and latency constrain method choice.
- **RP-02 (Audience-Specific Framing):** explanations matched to each audience's decision.
- **QA-12 (False Positives Identification):** prevents attribution-as-causation and trusting unstable explanations.

**Related Prompts:**
- `rai_interpretability_analysis.md` — validate the model's internal/global behavior.
- `rai_model_card_authoring.md` — document the explainability approach.
- `rai_ethics_review_protocol.md` — recourse and contestability in the broader review.
