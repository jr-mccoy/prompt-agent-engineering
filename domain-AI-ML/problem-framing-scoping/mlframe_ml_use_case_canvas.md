---
title: "ML Use-Case Canvas"
category: AI-ML/problem-framing-scoping
description: "Compress an ML initiative onto one page: the problem, the prediction, the decision it drives, the data available, the value, the risks, and the baseline — so everyone aligns before any model is built."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - RT-02
  - RP-02
difficulty: beginner
tags:
  - use-case-canvas
  - problem-framing
  - scoping
  - alignment
  - baseline
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_is_this_an_ml_problem.md
  - domain-AI-ML/problem-framing-scoping/mlframe_success_metric_selection.md
  - domain-AI-ML/problem-framing-scoping/mlframe_data_readiness_assessment.md
---

# ML Use-Case Canvas

**Objective:** Produce a single-page canvas that captures every decision-relevant fact about a proposed ML use case — problem, prediction, the decision it drives, data, value, risks, and the baseline to beat — so technical and business stakeholders can align (or disagree concretely) before committing build effort.

**When to Use:**
- Kicking off a new ML initiative and needing one shared artifact.
- Aligning a product owner, a data scientist, and an engineer on the same framing.
- Triaging a backlog of ML ideas to a comparable format for prioritization.

**When NOT to Use:**
- The question is still "should this be ML at all?" (use `mlframe_is_this_an_ml_problem.md` first).
- You need a deep technical design — the canvas is a framing artifact, not an architecture.

## Inputs / Context

Provide what you can; gaps become explicit "unknown — to confirm" cells rather than blanks:
- **The business problem** and who owns the outcome.
- **What you'd predict** and at what unit of analysis (user, transaction, session...).
- **The decision/action** the prediction triggers and who/what acts.
- **Data on hand** — sources, volume, labels, history, freshness.
- **Expected value** — revenue, cost, risk, or time saved.
- **Known constraints/risks** — latency, fairness, regulatory, privacy.

## Constraints

**Must:**
- Fill every canvas cell; where a fact is unknown, write "unknown — to confirm" rather than guessing.
- Name an explicit baseline (current process, simple rule, or majority class) the model must beat.
- Tie the prediction to a concrete decision and the value to a measurable quantity.

**Must Not:**
- Invent data availability, label counts, value figures, or volumes — mark unknowns as unknowns.
- Conflate the prediction (what the model outputs) with the decision (what someone does with it).
- Let "value" remain a vague adjective ("improve experience") without a measurable proxy.

**Instructions:**

1. **Name the problem and owner.** One sentence on the outcome someone wants changed, and the single accountable owner. If no owner exists, flag it.

2. **Define the prediction precisely.** State the output, its type (probability, label, number, ranking), and the unit of analysis. Ambiguity here propagates into every later stage.

3. **Trace the decision and action.** Who or what consumes the prediction, what action it triggers, and what happens when the model is uncertain or wrong. A prediction with no action is a red flag.

4. **Inventory the data honestly.** List sources, approximate volume, whether labels exist and how they're generated, history length, and freshness. Mark each as confirmed or unknown.

5. **Quantify value with a proxy.** Translate "value" into a measurable quantity (e.g., dollars per false negative avoided, hours saved per week). If it can't be quantified yet, name the proxy you'd use.

6. **Surface risks and constraints.** Latency/throughput, fairness/regulatory exposure, privacy, explainability needs, and failure consequences. Note any that could be a hard stop.

7. **State the baseline and the bar.** Name the current approach and the threshold ML must clear to be worth building. Without a baseline, "success" is undefined.

8. **List the top open questions.** The 3–5 unknowns that most threaten the case, in the order they should be resolved.

**Output Format:**

A single-page canvas (markdown table or labeled sections):
- **Problem & Owner**
- **Prediction** (output, type, unit)
- **Decision / Action** (consumer, trigger, fallback when wrong)
- **Data** (sources, volume, labels, history, freshness — each confirmed/unknown)
- **Value** (quantity + proxy)
- **Risks & Constraints**
- **Baseline & Bar-to-Beat**
- **Top Open Questions** (ranked)

## Verification

- [ ] Every cell is filled or explicitly marked "unknown — to confirm."
- [ ] The prediction and the decision are distinct and both stated.
- [ ] A measurable value proxy is named, not a vague benefit.
- [ ] An explicit baseline and a bar-to-beat are present.
- [ ] Open questions are ranked by threat to the case.
- [ ] No data availability or value figure is asserted without a source.

## False-Positive Prevention

❌ **DON'T:**
- Write a prediction so vague ("predict churn risk") that the unit, horizon, and threshold are undefined.
- Assume labels exist because the outcome is observable somewhere downstream.
- List "value" as an unmeasurable adjective and call the cell done.
- Skip the baseline cell — a canvas without a bar-to-beat can't be evaluated later.

✅ **DO:**
- Pin the prediction to a unit and horizon (e.g., "P(user churns within 30 days)").
- State exactly how labels are produced and how stale they may be.
- Force value into a quantity even if it's a rough proxy to validate.
- Always name the current process as the baseline ML must beat.

## Example Output

```markdown
## ML Use-Case Canvas: Proactive Support Ticket Routing

| Cell | Content |
|---|---|
| Problem & Owner | Tickets sit in the wrong queue, raising time-to-first-response. Owner: Head of Support Ops |
| Prediction | P(ticket belongs to each of 6 queues); output: ranked queues. Unit: per inbound ticket |
| Decision / Action | Auto-route top queue if top prob > τ; else leave in triage. Fallback: human triage (today's path) |
| Data | Sources: 24 mo ticket text + final-queue labels (confirmed); volume ~400k (confirmed); labels = human-resolved final queue (confirmed); freshness: daily (confirmed) |
| Value | Reduce avg time-to-first-response; proxy: minutes saved/ticket × volume (target TBD — to confirm) |
| Risks & Constraints | Mis-route delays urgent tickets; latency < 2s; no PII to third parties |
| Baseline & Bar-to-Beat | Keyword rules route ~55% correctly today; ML must beat ~55% routing accuracy AND not worsen urgent-ticket SLA |
| Top Open Questions | 1) Label noise in old tickets? 2) Class imbalance across queues? 3) Acceptable mis-route rate for urgent? |
```

**Techniques Used:**
- **ST-01 (Clear Objective Statement):** the canvas forces a single, shared framing.
- **ST-03 (Output Format Specification):** the fixed cell set makes use cases comparable.
- **CM-02 (Constraint Specification):** captures latency/fairness/baseline as first-class constraints.
- **RT-02 (Multi-Dimensional Analysis Framework):** value, risk, data, and baseline are weighed together.
- **RP-02 (Audience-Specific Framing):** one artifact readable by both business and technical stakeholders.

**Related Prompts:**
- `mlframe_is_this_an_ml_problem.md` — decide whether ML is warranted before filling the canvas.
- `mlframe_success_metric_selection.md` — turn the value cell into a concrete metric.
- `mlframe_data_readiness_assessment.md` — pressure-test the data cell in depth.
