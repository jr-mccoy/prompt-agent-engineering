---
title: "Feature Ideation Workshop"
category: AI-ML/feature-engineering
description: "Systematically brainstorm candidate features from domain knowledge and available data, framed as testable hypotheses with a defined availability-at-prediction-time check."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - feature-ideation
  - hypotheses
  - domain-knowledge
  - feature-engineering
  - leakage-aware
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_selection_strategy.md
  - domain-AI-ML/feature-engineering/mlfeature_leakage_safe_pipeline.md
  - domain-AI-ML/problem-framing-scoping/mlframe_problem_to_ml_task_translator.md
---

# Feature Ideation Workshop

**Objective:** Generate a structured, prioritized set of candidate features from domain knowledge and the available data, each expressed as a testable hypothesis ("signal X should help because mechanism Y") with its availability-at-prediction-time and leakage risk noted — so feature work is hypothesis-driven, not a random scrape of every column.

**When to Use:**
- Starting feature engineering on a new model.
- A model is plateauing and you need fresh, mechanism-grounded feature ideas.
- You want a backlog of features ranked by expected value and feasibility.

**When NOT to Use:**
- You already have candidates and need to *select* among them (use `mlfeature_selection_strategy.md`).
- You're deciding how to encode features you've chosen (use `mlfeature_encoding_strategy.md`).

## Inputs / Context

Provide what you can:
- **Task & target** — what's predicted, the unit of analysis, the prediction-time boundary.
- **Available data sources** — tables/streams, fields, and when each is observed.
- **Domain context** — how the outcome arises; expert intuitions about drivers.
- **Existing features** (if any) and known strong/weak signals.
- **Constraints** — latency, online-availability of sources, privacy/regulatory limits on fields.

## Constraints

**Must:**
- Express each feature as a hypothesis with a stated mechanism (why it should carry signal).
- Tag each candidate with its availability at prediction time and a leakage-risk flag.
- Group ideas by source/theme and prioritize by expected signal × feasibility.

**Must Not:**
- Propose features that can only be computed using information unavailable at inference time (or, if proposed, flag them clearly as leakage-risk, not usable).
- Invent the existence of data fields the user didn't provide — mark "would need: …" instead.
- Assert that a feature "will be important" — frame as a hypothesis to test.

**Instructions:**

1. **Anchor on the prediction-time boundary.** Restate the instant of inference and what's observable by then. Every candidate must be computable from data available at or before that instant.

2. **Mine the domain mechanism.** From how the outcome actually arises, list the drivers a domain expert would expect to matter, and turn each into a candidate signal.

3. **Mine the data structure.** Walk the available sources and derive feature families: raw fields, aggregations (counts, sums, rates), recency/frequency, ratios, deltas/trends, interactions, and time-windowed summaries.

4. **Write each as a testable hypothesis.** For each candidate: the feature, the mechanism ("recent login frequency proxies engagement, which drives retention"), and how you'd test its contribution.

5. **Flag availability and leakage risk.** Mark each as available-at-inference / needs-source / leakage-risk, applying the prediction-time boundary strictly. Window-based features must use only past windows.

6. **Note encoding/latency feasibility.** Briefly flag high-cardinality, sparse, or expensive-to-compute-online features that may be costly to serve.

7. **Prioritize the backlog.** Rank candidates by expected signal × feasibility (incl. availability and serving cost), and mark a small "test first" set.

**Output Format:**

A markdown feature backlog:
- **Prediction-Time Boundary** — restated.
- **Candidate Features** — table: Feature | Hypothesis/Mechanism | Source | Availability/Leakage flag | Feasibility | Priority.
- **Themes / Families** — grouped summary.
- **Test-First Set** — the top few to validate quickly.
- **Needs-Data Notes** — sources that would unlock high-value candidates.

## Verification

- [ ] Every candidate has a stated mechanism, not just a name.
- [ ] Each is tagged available-at-inference / needs-source / leakage-risk against the boundary.
- [ ] Window/aggregate features are constrained to past-only windows.
- [ ] No invented data fields; missing sources are marked "would need."
- [ ] A prioritized test-first set is identified.

## False-Positive Prevention

❌ **DON'T:**
- Propose a feature computed from post-outcome data (e.g., "number of refund tickets after purchase" to predict a purchase outcome) — that's target leakage dressed as a feature.
- Use a full-history aggregate that includes the future relative to the prediction time.
- Brainstorm column names with no mechanism — unmotivated features inflate the search space and overfitting risk.
- Assume a field that exists in the warehouse is also available *online* at inference latency.

✅ **DO:**
- State the causal/behavioral mechanism for each feature so it's testable, not a fishing expedition.
- Apply the prediction-time boundary to every window and aggregate (past-only).
- Separate "available offline for training" from "available online at serving" to avoid train/serve skew later.
- Prioritize by expected signal AND serving feasibility, not novelty.

## Example Output

```markdown
## Feature Backlog: 30-Day Churn (predicted end-of-day D; label D+1..D+30)

### Prediction-Time Boundary
All features computed from data observed ≤ end of day D. No D+1..D+30 information.

### Candidate Features
| Feature | Hypothesis / Mechanism | Source | Avail/Leakage | Feasibility | Priority |
|---|---|---|---|---|---|
| logins_last_14d | Recent activity proxies engagement → retention | events | Available | High | P0 |
| days_since_last_login | Disengagement precedes churn | events | Available | High | P0 |
| support_tickets_last_30d | Friction predicts churn | support | Available | Med | P1 |
| pct_feature_adoption | Value realization lowers churn | usage | Available | Med | P1 |
| refund_after_churn | (post-outcome) | billing | LEAKAGE — exclude | — | — |
| nps_score | Satisfaction → retention | survey | Needs-source (sparse) | Low | P2 |

### Themes / Families
Engagement recency/frequency; friction signals; value-realization; (survey — sparse).

### Test-First Set
logins_last_14d, days_since_last_login, support_tickets_last_30d.

### Needs-Data Notes
NPS coverage is too sparse to rely on; would need broader survey capture to use.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** boundary → domain → data → hypotheses → flags → rank.
- **RT-02 (Multi-Dimensional Analysis Framework):** prioritizes by signal × feasibility × availability.
- **RT-05 (Evidence-Based Reasoning):** each feature carries a stated mechanism to test.
- **CM-02 (Constraint Specification):** the prediction-time boundary governs admissibility.
- **QA-12 (False Positives Identification):** flags post-outcome features as leakage before they enter.

**Related Prompts:**
- `mlfeature_selection_strategy.md` — narrow the backlog to a working set.
- `mlfeature_leakage_safe_pipeline.md` — implement the past-only computation safely.
- `mlframe_problem_to_ml_task_translator.md` — sets the boundary and unit ideation depends on.
