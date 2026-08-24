---
title: "RAI Model Card Authoring"
category: AI-ML/responsible-ai-governance
description: "Author a complete, honest Model Card — intended use, training data, per-group performance, limitations, and ethical considerations — without inflating metrics or inventing evaluation results."
techniques:
  - ST-03
  - DS-01
  - RT-05
  - QA-12
  - RP-02
difficulty: intermediate
tags:
  - model-card
  - documentation
  - transparency
  - per-group-performance
  - responsible-ai
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_bias_detection_audit.md
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_explainability_plan.md
---

# RAI Model Card Authoring

**Objective:** Produce a Model Card that documents a model's intended use, training/evaluation data, performance disaggregated by group, known limitations, and ethical considerations — so downstream users can judge whether the model is appropriate for their context, with every figure traceable to an actual evaluation and no invented results.

**When to Use:**
- Before releasing or handing off a model (internal or external).
- When a governance gate, customer, or regulator requires model documentation.
- When inheriting a model with no documentation and you must reconstruct its card.

**When NOT to Use:**
- As a substitute for the bias audit itself — the card *reports* results from `rai_bias_detection_audit.md`.
- For the risk register or governance process — see `rai_model_risk_assessment.md`.

## Inputs / Context

- **Model basics** — task, version, architecture family, owner, date.
- **Intended use & out-of-scope use** — what it's for and explicitly what it is not for.
- **Training & evaluation data** — sources, time range, size, known gaps, consent/licensing notes, group composition.
- **Performance results** — aggregate AND per-group/intersection metrics from actual evaluations, with sample sizes.
- **Limitations & known failure modes** — observed, not speculative-only.
- **Regulation/framework in scope** — if the card must map to a specific framework (ask the user).

## Constraints

**Must:**
- Include a disaggregated (per-group) performance section; if no group data exists, state that as a documented limitation rather than omitting it.
- Source every metric to a named evaluation set with its size and date.
- State intended use AND out-of-scope/prohibited use explicitly.

**Must Not:**
- Invent or round up metrics, or carry forward numbers from a different model version without labeling them.
- Cite a regulatory framework's required fields unless the user confirms which framework applies; if unknown, write the card to general best practice and note the framework mapping is unconfirmed.
- Present aggregate performance as evidence of fairness — disaggregated results are required for any fairness statement.

**Instructions:**

1. **Capture identity and intended use.** Record model name, version, owner, date, task, and the precise intended-use statement plus explicit out-of-scope/prohibited uses.

2. **Document the data.** Describe training and evaluation data sources, time range, size, group composition, known gaps, and consent/licensing — flagging anything unknown as unknown.

3. **Report aggregate performance with provenance.** State headline metrics, the eval set, its size, and date. No bare numbers.

4. **Report disaggregated performance.** Present per-group and intersectional metrics with sample sizes and intervals. If group labels are absent, document that as a limitation and what would be needed.

5. **State limitations and failure modes.** List observed failure modes, distribution-shift sensitivities, and conditions under which performance degrades — separating observed from hypothesized.

6. **Document ethical considerations.** Cover affected populations, foreseeable harms, mitigations applied (with their tradeoffs), and recourse/contestability for affected people.

7. **Frame for the audience.** Write the card so a downstream user who did not build the model can decide whether to use it; avoid internal jargon and unexplained metric names.

8. **Add maintenance metadata.** Record review cadence, contact, and when the card was last validated against current behavior.

**Output Format:**

A Model Card in markdown with sections:
- **Model Details** (name, version, owner, date, architecture)
- **Intended Use** (and Out-of-Scope / Prohibited Use)
- **Training & Evaluation Data** (sources, composition, gaps, consent)
- **Performance — Aggregate** (with eval set + size + date)
- **Performance — Disaggregated by Group/Intersection** (with sample sizes + intervals)
- **Limitations & Failure Modes**
- **Ethical Considerations & Recourse**
- **Maintenance** (review cadence, contact, last validated)

## Verification

- [ ] Intended use AND out-of-scope use are both stated.
- [ ] Every metric names its eval set, size, and date.
- [ ] A disaggregated performance section exists (or absence of group data is documented as a limitation).
- [ ] No fairness claim rests on aggregate numbers alone.
- [ ] Limitations separate observed from hypothesized.
- [ ] No invented metrics or numbers borrowed from another version unlabeled.
- [ ] Framework mapping is user-confirmed or explicitly marked unconfirmed.

## False-Positive Prevention

❌ **DON'T:**
- Fill the per-group section with the aggregate number repeated, implying parity that wasn't measured.
- State "no known bias" when no disaggregated evaluation was run — that's absence of testing, not absence of bias.
- Copy performance figures from the previous version because retraining "shouldn't have changed much."
- Invent the data's group composition when it was never recorded.

✅ **DO:**
- Report real per-group metrics with sample sizes, or document the gap honestly.
- Phrase untested fairness as "not yet evaluated for disparate performance."
- Tie every number to the exact eval run that produced it.
- Mark unknown data provenance as unknown.

## Example Output

```markdown
## Model Card: Support-Ticket Priority Classifier v1.3

### Model Details
Owner: Platform ML. Version 1.3, released 2026-05-20. Gradient-boosted trees. Multi-class (P0–P3).

### Intended Use
For: routing inbound support tickets to a priority queue to assist (not replace) human triage.
Out-of-scope: SLA breach determinations; any customer-facing automated decision; non-English tickets (not evaluated).

### Training & Evaluation Data
180k tickets, 2024-01 to 2026-03. English only. Region composition: NA 62%, EU 24%, APAC 11%, other 3% — APAC underrepresented (documented gap). Consent: internal operational data per ToS.

### Performance — Aggregate
Eval set: 22k held-out tickets (2026-03), macro-F1 0.79.

### Performance — Disaggregated by Group
| Region | n | Macro-F1 | 95% CI |
|---|---|---|---|
| NA | 13,600 | 0.81 | [0.80,0.82] |
| EU | 5,300 | 0.78 | [0.76,0.80] |
| APAC | 2,400 | 0.71 | [0.68,0.74] |
APAC underperformance is consistent with its training underrepresentation (observed, cause hypothesized).

### Limitations & Failure Modes
- Degrades on tickets >2,000 tokens (observed). Not validated post-2026-03 product changes.

### Ethical Considerations & Recourse
Misrouting can delay urgent issues for underrepresented regions. Mitigation: human triage retains override; mis-priority appeals route to a human within 1 business day.

### Maintenance
Quarterly review. Contact: ml-platform@. Last validated: 2026-05-20.
```

**Techniques Used:**
- **ST-03 (Output Format Specification):** the card is a fixed, complete section structure.
- **DS-01 (Framework Application):** applies the Model Card documentation framework.
- **RT-05 (Evidence-Based Reasoning):** every metric is sourced to an eval run.
- **QA-12 (False Positives Identification):** blocks "no known bias" from untested aggregates.
- **RP-02 (Audience-Specific Framing):** written for a downstream user who didn't build the model.

**Related Prompts:**
- `rai_bias_detection_audit.md` — produces the disaggregated results the card reports.
- `rai_model_risk_assessment.md` — the risk view that complements the card.
- `rai_explainability_plan.md` — how the model's decisions are explained to stakeholders.
