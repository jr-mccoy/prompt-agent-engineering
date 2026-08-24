---
title: "RAI Interpretability Analysis"
category: AI-ML/responsible-ai-governance
description: "Analyze and validate a model's internal and global behavior — what it has actually learned — while distinguishing genuine interpretability from unstable post-hoc artifacts and predictive-vs-causal claims."
techniques:
  - ST-02
  - RT-05
  - RT-09
  - QA-12
  - DS-02
difficulty: advanced
tags:
  - interpretability
  - global-behavior
  - feature-effects
  - post-hoc-limits
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_explainability_plan.md
  - domain-AI-ML/responsible-ai-governance/rai_bias_detection_audit.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
---

# RAI Interpretability Analysis

**Objective:** Characterize and validate what a model has actually learned at the global level — dominant features, interactions, decision regions, and reliance on proxies or spurious correlations — while explicitly bounding the reliability of the post-hoc methods used and never conflating "the model relies on X" with "X causes the outcome."

**When to Use:**
- To validate that a model learned sensible structure before trusting it in production.
- When debugging surprising behavior or suspected reliance on spurious features.
- As input to a bias audit or risk assessment (what the model leans on).

**When NOT to Use:**
- To explain a single decision to an end user — use `rai_explainability_plan.md`.
- To establish causal effects in the real world — interpretability describes the model, not reality.

## Inputs / Context

- **Model & access** — architecture, whether you have model internals (weights/activations) or only input-output query access.
- **Feature semantics** — names and meanings; which are protected/sensitive; suspected proxies.
- **Representative data** — a dataset to probe behavior across, with group/segment labels if available.
- **Hypotheses** — any suspected spurious correlations, shortcut features, or expected drivers.
- **Method availability** — global SHAP, permutation importance, PDP/ALE, surrogate models, concept probing, activation analysis.

## Constraints

**Must:**
- Distinguish *what the model relies on* (a property of the model) from *what causes the outcome* (a property of the world).
- Report the reliability of each interpretability method used: instability across runs, sensitivity to correlated features, and disagreement between methods.
- Validate findings with at least two methods or a confirmatory probe before asserting a global behavior.

**Must Not:**
- Read high global feature importance as a causal lever for intervention.
- Trust a single permutation-importance or PDP result when features are correlated (effects get split or distorted) — flag the correlation issue.
- Fabricate benchmark comparisons or claim the model is "interpretable enough" without stated criteria.

**Instructions:**

1. **State the question and method palette.** Define what global behavior you need to validate and which methods are feasible given your access (internals vs query-only).

2. **Map global feature reliance.** Use global importance (e.g., permutation, global SHAP) to rank what the model leans on, noting correlation among features that may distort attributions.

3. **Characterize effect shapes and interactions.** Use PDP/ALE and interaction analysis to see how predictions change with key features — preferring ALE when features are correlated.

4. **Probe for shortcuts and proxies.** Test whether the model relies on spurious correlations or sensitive-attribute proxies (e.g., zip code for race). Confirm with targeted perturbations.

5. **Cross-validate with a second method or probe.** Confirm each material finding with an independent method or an intervention test (perturb the feature, observe output change).

6. **Assess method reliability.** Re-run unstable methods; report which findings are robust vs fragile to background-data or seed changes.

7. **Separate predictive from causal language.** For each finding, write the predictive claim ("model relies on X") and explicitly withhold or qualify any causal claim.

8. **Summarize trust implications.** State whether the learned structure supports trusting the model for its intended use, and what remains uncertain.

**Output Format:**

A markdown report:
- **Question & Methods** — what's validated, which methods, what access.
- **Global Reliance Map** — ranked features with method(s) and correlation caveats.
- **Effect Shapes & Interactions** — key features' effect curves and notable interactions.
- **Shortcut / Proxy Findings** — confirmed vs suspected, with the probe used.
- **Method Reliability Notes** — robust vs fragile findings.
- **Predictive-vs-Causal Statement** — explicit separation per finding.
- **Trust Implications & Open Questions**
- **INSUFFICIENT EVIDENCE** — the honest verdict for a shortcut or proxy finding where attribution methods disagree and no intervention was run. Attribution is a hypothesis-generating instrument; name the unblocking datum: the perturbation, ablation, or retrain-without-the-feature that would confirm the reliance.

## Verification

- [ ] Each global finding is confirmed by ≥2 methods or a perturbation probe.
- [ ] Correlated-feature distortion of importance/PDP is flagged where relevant.
- [ ] Every finding states the predictive claim and withholds/qualifies the causal claim.
- [ ] Method instability is reported (robust vs fragile).
- [ ] Proxy/shortcut findings are labeled confirmed vs suspected with their probe.
- [ ] No benchmark/SOTA figures are invented.
- [ ] Shortcut and proxy findings that rest on attribution alone, or on disagreeing methods, are reported as INSUFFICIENT EVIDENCE with the confirming intervention named.

## False-Positive Prevention

❌ **DON'T:**
- Conclude "the model uses income to drive risk, so raising income lowers risk" — that's a causal leap from a predictive pattern.
- Trust permutation importance ranking when two features are highly correlated.
- Declare a shortcut from a single PDP wiggle without a confirmatory perturbation.
- Call the model "interpretable" without saying interpretable-for-what and how validated.

✅ **DO:**
- Phrase findings as "the model relies on X," reserving causal claims for actual causal analysis.
- Prefer ALE and check correlation before trusting feature effects.
- Confirm shortcuts/proxies with targeted perturbation tests.
- Report which findings survive re-runs and which are fragile.

## Example Output

```markdown
## Interpretability Analysis: Insurance Claim Fraud Model

### Question & Methods
Validate global behavior before deployment. Access: query-only. Methods: permutation importance, ALE, surrogate tree, targeted perturbation.

### Global Reliance Map
1. claim_amount (robust across methods)
2. days_to_report (robust)
3. provider_id (high importance BUT correlated with region — attribution likely split/distorted; flagged)
4. zip3 (suspected proxy for demographic group)

### Effect Shapes & Interactions
ALE: fraud score rises sharply for days_to_report > 30. Interaction: claim_amount × provider_id concentrates risk in a few providers.

### Shortcut / Proxy Findings
- zip3 as demographic proxy: SUSPECTED. Perturbation test: holding all else fixed and shuffling zip3 moves score by up to 0.08 — material; needs bias audit.
- provider_id reliance: CONFIRMED reliance, but correlation with region means importance rank is uncertain.

### Method Reliability Notes
Robust: claim_amount, days_to_report. Fragile: exact rank of provider_id vs region (correlation).

### Predictive-vs-Causal Statement
Model RELIES ON days_to_report; we do NOT claim late reporting causes fraud — it may correlate with legitimate circumstances.

### Trust Implications & Open Questions
Sensible top drivers, but zip3 proxy risk blocks unconditional trust → route to bias audit.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** question → reliance → effects → shortcuts → validate.
- **RT-05 (Evidence-Based Reasoning):** findings anchored to method outputs and probes.
- **RT-09 (Root Cause Explanation):** traces surprising behavior to learned structure.
- **QA-12 (False Positives Identification):** blocks causal leaps and unstable-method trust.
- **DS-02 (Metric Specification):** defines perturbation/effect measurements.

**Related Prompts:**
- `rai_explainability_plan.md` — local, audience-facing explanations.
- `rai_bias_detection_audit.md` — follow up on suspected proxy reliance.
- `rai_model_risk_assessment.md` — feed learned-behavior risks into the register.
