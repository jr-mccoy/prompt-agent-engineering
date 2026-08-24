---
title: "RAI Fair-Lending & ECOA Assessment"
category: AI-ML/responsible-ai-governance
description: "Assess a credit/lending model for fair-lending risk under ECOA / Regulation B concepts — prohibited-basis disparate treatment vs disparate impact, adverse-action reason generation, and a less-discriminatory-alternative search — without inventing statutory cites, dollar thresholds, or enforcement figures."
techniques:
  - DS-01
  - ST-02
  - DS-06
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - fair-lending
  - ecoa
  - regulation-b
  - adverse-action
  - responsible-ai
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_fairness_metric_selection.md
  - domain-AI-ML/responsible-ai-governance/rai_bias_detection_audit.md
  - domain-AI-ML/responsible-ai-governance/rai_explainability_plan.md
---

# RAI Fair-Lending & ECOA Assessment

**Objective:** Assess a credit/lending model for fair-lending risk under ECOA / Regulation B concepts — distinguishing prohibited-basis disparate treatment from disparate impact, confirming the model can generate specific adverse-action principal reasons, and structuring a less-discriminatory-alternative (LDA) search — while requiring the user (and counsel) to confirm jurisdiction/regulator and without inventing statutory citations, dollar thresholds, or enforcement figures.

**When to Use:**
- To structure a first-pass fair-lending risk review of a credit underwriting, pricing, or line-assignment model.
- To verify a model can produce specific, accurate adverse-action reasons before deployment.
- To scope a less-discriminatory-alternative search alongside model development.

**When NOT to Use:**
- As legal advice — this is a structured pre-assessment; route conclusions to compliance/counsel.
- As a substitute for qualified counsel or a fair-lending specialist when binding obligations attach.
- For non-credit decisions or jurisdictions the user has not confirmed — confirm the regulatory context first.

## Inputs / Context

- **Model description** — decision type (approve/decline, pricing, line/limit), features, and target.
- **Prohibited-basis context** — which protected characteristics are in scope under the confirmed regime.
- **Proxy/feature concerns** — features that may correlate with prohibited bases (e.g., geography, certain alternative data).
- **Adverse-action mechanism** — how principal reasons are derived and surfaced today.
- **Performance & disparity data** — outcomes by group, if available, and how they were computed.
- **User-confirmed regime** — jurisdiction, applicable regulator, and version (ask; do not assume).

## Constraints

**Must:**
- Distinguish disparate treatment (use of a prohibited basis or close proxy) from disparate impact (a neutral practice with disproportionate effect) throughout.
- Verify the model can generate *specific, accurate* principal reasons for adverse actions, not generic ones.
- Structure (not conclude) a less-discriminatory-alternative search and route disparity findings to counsel.

**Must Not:**
- NO-FABRICATION: never invent statutory or regulatory citations, section numbers, regulatory text, numeric thresholds (e.g., disparity ratios), dollar amounts, deadlines, or enforcement/case figures from memory; the user confirms jurisdiction/regulator and version; map the model to the regime's STRUCTURE and obligations at a conceptual level and explicitly flag any specific citation, threshold, or figure as "verify against the current official source."
- Declare the model "fair," "compliant," or "discriminatory" — produce a risk assessment and route to counsel.
- Assume which protected characteristics or which regulator apply; confirm with the user.

**Instructions:**

1. **Confirm regime, regulator, and scope.** Establish jurisdiction, applicable regulator, prohibited bases in scope, and the decision type. Mark unknowns as open legal questions.

2. **Screen for disparate treatment.** Check whether any prohibited basis — or a close proxy — is used directly or indirectly in the model. Flag features that act as proxies and require review.

3. **Screen for disparate-impact risk.** Where group-outcome data exists, characterize disparities descriptively (without inventing a "legal" threshold) and frame them as risk indicators to verify, not verdicts.

4. **Verify adverse-action reason generation.** Confirm the model/system can produce specific, accurate principal reasons tied to the actual drivers of the decision — not vague or templated reasons disconnected from the model.

5. **Structure the LDA search.** Outline how to search for a less-discriminatory alternative that meets the legitimate business need (e.g., feature changes, alternative model forms, threshold adjustments), and how to compare candidates on both performance and disparity.

6. **Connect to fairness metrics and bias audit.** Recommend which fairness metric(s) fit the decision and reference a structured bias audit; do not pick a metric that contradicts the decision context.

7. **Compile risk findings and route to counsel.** Rank fair-lending risks by significance and effort; mark every item needing legal interpretation.

**Output Format:**

A markdown fair-lending risk assessment:
- **Regime & Scope** — jurisdiction, regulator, prohibited bases, decision type, open questions.
- **Disparate-Treatment Screen** — direct/proxy use of prohibited bases; flagged features.
- **Disparate-Impact Risk** — descriptive disparities (no invented thresholds); indicators to verify.
- **Adverse-Action Reason Check** — can the model produce specific principal reasons? Gaps.
- **LDA Search Plan** — candidate alternatives + comparison method.
- **Fairness-Metric & Bias-Audit Linkage**.
- **Ranked Risks & Counsel Handoff** — significance × effort; items needing legal interpretation.
- **INSUFFICIENT EVIDENCE** — the correct disparate-impact finding where prohibited-basis data is not collected, which is the ordinary situation in lending. Absence of demographic data is absence of measurement, not absence of disparity. Name the unblocking datum: the proxy-derivation or self-reported-data route permitted under the applicable regime, confirmed with counsel before it is used.

## Verification

- [ ] Jurisdiction, regulator, and prohibited bases are user-confirmed (or flagged open).
- [ ] Disparate treatment and disparate impact are kept distinct.
- [ ] No statutory cites, numeric disparity thresholds, dollar amounts, or enforcement figures are invented.
- [ ] Adverse-action reasons are checked for specificity and accuracy, not just presence.
- [ ] An LDA search is structured (not concluded) and disparities are routed to counsel.
- [ ] No "fair/compliant/discriminatory" verdict is issued.
- [ ] Where prohibited-basis data is not collected, the disparate-impact finding is INSUFFICIENT EVIDENCE with the permitted measurement route named — it is not reported as no disparity.

## False-Positive Prevention

❌ **DON'T:**
- Cite a specific ECOA/Reg B section or a "legal" disparity threshold (e.g., a fixed ratio) from memory — these must be verified against the current official source.
- Treat the absence of a protected attribute in the features as proof of no disparate impact — proxies and impact can persist without it.
- Accept generic, templated adverse-action reasons as adequate — they must reflect the model's actual drivers.
- Declare the model "fair" because a single fairness metric passes — metric choice can mask the relevant disparity.

✅ **DO:**
- Keep disparate treatment (use of a basis/proxy) and disparate impact (neutral practice, disproportionate effect) separate.
- Confirm the model produces specific, accurate principal reasons before deployment.
- Structure an LDA search comparing candidates on both business need and disparity.
- Route all disparity findings and thresholds to counsel for verification against the current official source.

## Example Output

```markdown
## Fair-Lending Risk Assessment: Personal-Loan Underwriting Model

### Regime & Scope
Jurisdiction/regulator: user-confirmed (US, applicable agency). Prohibited bases in scope: as confirmed by counsel. Decision: approve/decline. Open: whether state-level obligations also apply — verify.

### Disparate-Treatment Screen
No prohibited basis used directly. Flagged proxy: ZIP-code-derived feature correlates with a prohibited basis — requires review/removal-or-justification.

### Disparate-Impact Risk
Descriptive: approval-rate gap observed between two groups in backtest (figure recorded internally). Framed as a risk indicator to verify — no legal threshold asserted here.

### Adverse-Action Reason Check
System currently returns top-3 SHAP features as reasons. Gap: reasons are sometimes non-actionable/opaque; confirm they map to specific, accurate principal reasons before deployment.

### LDA Search Plan
Candidates: (a) drop ZIP proxy, (b) monotonic GBM with constrained features, (c) threshold recalibration. Compare on AUC/approval-rate + group disparity. Document tradeoffs for counsel.

### Fairness-Metric & Bias-Audit Linkage
Recommend a metric aligned to approve/decline harm (see fairness-metric selection) + a structured bias audit before sign-off.

### Ranked Risks & Counsel Handoff
1. Proxy feature (high × moderate) — counsel + DS.
2. Adverse-action reason specificity (high × low) — engineering.
Route disparity figures and any thresholds to counsel for verification against the current official source.
```

**Techniques Used:**
- **DS-01 (Framework Application):** structures the review against ECOA / Reg B fair-lending concepts.
- **ST-02 (Structured Sequential Instructions):** regime → treatment → impact → adverse action → LDA → handoff.
- **DS-06 (Prioritization & Severity Guidance):** ranks fair-lending risks by significance and effort.
- **QA-12 (False Positives Identification):** prevents fabricated cites/thresholds and premature fairness verdicts.
- **CM-02 (Constraint Specification):** the no-invented-legal-text constraint governs the analysis.

**Related Prompts:**
- `rai_fairness_metric_selection.md` — choose the fairness metric that fits the credit-decision context.
- `rai_bias_detection_audit.md` — the structured disparity audit feeding the impact screen.
- `rai_explainability_plan.md` — supports specific, accurate adverse-action reason generation.
