---
title: "AI/ML Use-Case Prioritization"
category: AI-ML/ai-product-leadership
description: "Rank candidate AI/ML use cases against value, feasibility, data readiness, and risk to produce a defensible, sequenced portfolio rather than a wishlist."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - NE-13
  - CM-02
difficulty: intermediate
tags:
  - prioritization
  - portfolio
  - feasibility
  - data-readiness
  - ai-strategy
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_ml_project_scoping.md
  - domain-AI-ML/ai-product-leadership/aipm_roi_business_case.md
  - domain-AI-ML/ai-product-leadership/aipm_ai_roadmap_design.md
---

# AI/ML Use-Case Prioritization

**Objective:** Take a list of candidate AI/ML use cases and produce a transparent, multi-dimensional ranking — scored on value, feasibility, data readiness, and risk — so leadership can fund the few that compound and defer the many that don't, with the reasoning visible and challengeable.

**When to Use:**
- A backlog of AI ideas exists and everyone has a favorite, but there is no shared way to compare them.
- Annual or quarterly planning where AI investment must be allocated across competing bets.
- A new AI mandate arrives and you must convert enthusiasm into a sequenced plan.

**When NOT to Use:**
- A single use case is already chosen and needs scoping (use `aipm_ml_project_scoping.md`).
- You need the financial case for one initiative (use `aipm_roi_business_case.md`).
- The question is build-vs-buy for a settled capability (use `aipm_build_buy_partner_decision.md`).

## Inputs / Context

Provide what you can; the analysis degrades gracefully:
- **Candidate use cases** — short description of each, the business problem, and who owns it.
- **Business context** — strategic priorities, time horizon, budget envelope (range is fine).
- **Data reality per case** — does the relevant data exist, who owns it, how clean/labeled/accessible is it.
- **Org capability** — current ML/data maturity, team size, MLOps state.
- **Risk surface** — regulatory exposure, customer-facing vs internal, reversibility.

## Constraints

**Must:**
- Score every case on all four dimensions with an explicit, stated rubric (e.g., 1–5 anchors), not vibes.
- Translate each score into business language a non-technical executive can act on.
- Surface data readiness as a first-class gate — a high-value, low-data case is a research bet, not a delivery bet, and must be labeled as such.

**Must Not:**
- Invent precise ROI figures, accuracy numbers, or market sizes the user did not provide; use ranges and scenarios and mark assumptions.
- Collapse the four dimensions into a single number without showing the components.
- Rank a case highly on "value" without naming the mechanism by which value is realized.

**Instructions:**

1. **Normalize the candidates.** Restate each use case in one line: problem, decision/action it improves, and the unit of value (revenue, cost, risk, time). Flag any that are solutions in search of a problem.

2. **Score value.** Assess upside magnitude and confidence. Use ranges/scenarios (conservative / expected / optimistic) and name the value mechanism. Do not fabricate dollar figures — express as relative bands plus stated assumptions.

3. **Score feasibility.** Judge technical tractability: is this a solved class of problem, an emerging one, or research? Factor team capability and dependency complexity.

4. **Score data readiness.** Assess existence, access, quality, labeling, volume, and freshness of the needed data. This is the most common silent killer — weight it accordingly and gate research-only cases.

5. **Score risk.** Cover regulatory/compliance, reputational/fairness, safety, reversibility, and failure blast radius. Higher stakes demand stronger controls before delivery.

6. **Compute and sequence.** Combine scores with a transparent weighting tied to the stated strategy. Sequence into Now / Next / Later and a Park/Kill list, noting enabling dependencies (e.g., "this needs a feature store first").

7. **Translate for the room.** For the top recommendations, write a one-sentence executive rationale and the single biggest risk to watch.

**Output Format:**

A markdown brief:
- **Prioritization Scorecard** — table: Use Case | Value | Feasibility | Data Readiness | Risk | Weighted Rank | Verdict
- **Sequenced Portfolio** — Now / Next / Later / Park-Kill, with one-line rationale each
- **Dependencies & Enablers** — shared infrastructure or data work that unlocks multiple cases
- **Key Assumptions & Open Questions** — what would change the ranking if wrong
- **Recommended Next Step** per top-3 case

## Verification

- [ ] Every case scored on all four dimensions with the rubric anchors shown.
- [ ] No invented precise financials; value expressed as ranges/scenarios with assumptions named.
- [ ] Data readiness explicitly gates any high-value/low-data case into "research bet."
- [ ] The weighting reflects the stated business strategy, not a default.
- [ ] Each top recommendation has a plain-language rationale and a named top risk.

## False-Positive Prevention

❌ **DON'T:**
- Rank a use case #1 on dazzling value while ignoring that the data to train it doesn't exist yet.
- Treat "the CEO is excited about it" as a value score.
- Assume feasibility because a vendor demo looked good — demos run on curated data.
- Bundle a research bet and a delivery bet in the same priority tier.

✅ **DO:**
- Make data readiness a hard gate; a great idea with no labeled data is a data project first.
- Anchor value to a specific decision or workflow it changes, and to whether that value is measurable.
- Separate "we can build this" from "we can operate and trust this in production."
- Mark every fabricated-looking number as an assumption with a range, not a fact.

## Example Output

```markdown
## AI/ML Use-Case Prioritization — FY26 Planning

### Prioritization Scorecard (1–5; weights: Value 35 / Feasibility 20 / Data 30 / Risk 15)
| Use Case | Value | Feas. | Data | Risk | Rank | Verdict |
|---|---|---|---|---|---|---|
| Support ticket auto-triage | 4 | 4 | 4 | 4 | 1 | NOW |
| Churn early-warning | 5 | 3 | 2 | 3 | 4 | NEXT (data first) |
| Dynamic pricing | 5 | 2 | 3 | 1 | 5 | PARK (risk + research) |
| Sales email drafting (GenAI) | 3 | 5 | 5 | 4 | 2 | NOW |
| Demand forecasting refresh | 4 | 4 | 4 | 4 | 3 | NEXT |

### Sequenced Portfolio
**Now:** Auto-triage (proven pattern, data clean, internal-facing) and GenAI email drafting (fast win, low blast radius).
**Next:** Demand forecasting (clear value, data ready) → Churn (high value but needs 1 quarter of label engineering first).
**Later/Park:** Dynamic pricing — high value but regulatory/fairness risk + immature modeling; revisit after a governance review.

### Dependencies & Enablers
- A shared feature store unlocks churn + forecasting + pricing; fund it as infrastructure, not per-project.

### Key Assumptions & Open Questions
- Churn value (expected: meaningful retention lift) assumes the model output is wired into a retention play — unconfirmed. If it isn't, value drops to "insight only."

### Recommended Next Steps
- Auto-triage: 6-week scoped pilot. Churn: 1-quarter data-readiness sprint before committing to modeling.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** fixed normalize→score×4→sequence flow.
- **RT-02 (Multi-Dimensional Analysis Framework):** the four-axis scorecard is the core.
- **DS-06 (Prioritization & Severity Guidance):** Now/Next/Later/Park sequencing.
- **NE-13 (Technical-to-Business Translation):** technical feasibility/data reality rendered as executive verdicts.
- **CM-02 (Constraint Specification):** data readiness as a hard gate.

**Related Prompts:**
- `aipm_ml_project_scoping.md` — scope the winners into deliverable projects.
- `aipm_roi_business_case.md` — build the financial case for the top pick.
- `aipm_ai_roadmap_design.md` — turn the sequenced portfolio into a phased roadmap.
