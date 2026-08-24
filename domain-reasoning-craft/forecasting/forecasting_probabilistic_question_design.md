---
title: "Probabilistic Question Design — Convert Vague Predictions into Resolvable Questions"
category: reasoning-craft/forecasting
description: "Convert a fuzzy claim ('the market will turn', 'this will work out', 'X will happen soon') into 1–3 well-formed forecast questions where any informed observer would agree on resolution. Specifies who judges, by what observable, by what date, with what threshold for yes/no, and what edge cases. Calibrated to Good Judgment / Metaculus standards."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - forecasting
  - operationalization
  - resolution-criteria
  - metaculus
  - good-judgment
updated: "2026-05-10"
reasoning:
  styles: [operational, precise, taxonomic]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: question_specs
  user_role: [forecaster, analyst, founder, executive, researcher]
  mode: [design, document]
related_prompts:
  - domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
  - domain-reasoning-craft/forecasting/forecasting_super_forecaster_decomposition.md
  - domain-research-academic/research_question_formulation.md
---

# Probabilistic Question Design

**Objective:** Convert a vague prediction into 1–3 well-formed forecast questions. Each question must be specific enough that any informed observer at resolution time would agree on the answer. Specifies: who judges resolution, what the resolving observable is, the date, the yes/no threshold (or numeric resolution), and edge-case handling. Calibrated to question-writing standards from Good Judgment Project and Metaculus.

**When to use:**
- Building a personal forecasting practice.
- Operationalizing a strategic / business / investment thesis.
- Preparing forecasts for a team or organization to track.
- Resolving an "obvious" prediction someone is making that, when written precisely, turns out to be ambiguous.

**When NOT to use:**
- Predictions about unobservable internal states.
- Pure expressions of preference ("I hope X").
- Predictions whose resolution would require unethical or impossible measurement.

**Audience:** Forecasters, analysts, executives, founders, researchers — anyone who wants to make predictions auditable.

---

## Inputs / Context

1. **The fuzzy claim.** As the user states it.
2. **Time horizon they have in mind.**
3. **Why this prediction matters** (decision tied to it).
4. **What "yes" looks like to the user** intuitively (we'll sharpen).

---

## Constraints

### Must
- Produce **resolvable** questions: any informed observer at resolution time would agree on the answer.
- Specify **resolver**: who decides yes/no (often: a named external observable like "Bureau of Labor Statistics monthly release" rather than the user's judgment).
- Specify **observable**: the specific data point or event that resolves the question.
- Specify **date**: when the question resolves.
- Specify **threshold**: for yes/no, the cut-off value; for numeric, the resolving measurement.
- Specify **edge cases**: what happens if the observable isn't published, gets revised, partially resolves, or is delayed.
- Generate **1–3 alternatives** to the user's first try; the original is rarely the cleanest.
- Mark each question's **answer type**: yes/no, multiple choice, numeric range, date range.

### Must Not
- Use vague terms in the resolution criteria ("significant", "successful", "soon", "many").
- Make the user the sole resolver unless unavoidable; subjective resolution undermines forecasts.
- Leave edge cases unspecified.
- Conflate prediction-of-event with prediction-of-perception ("X will be considered a success" is harder to resolve than "X will hit metric Y").

---

## Instructions

### Step 1 — Capture the fuzzy claim
Verbatim.

### Step 2 — Surface what's ambiguous
List the ambiguities: vague terms, undefined timing, unclear who/what is being predicted, unspecified threshold.

### Step 3 — Generate 1–3 candidate operationalizations
For each:
- **Question (one sentence)** — the resolvable form
- **Resolver** — who decides yes/no or measures
- **Observable** — what data point or event
- **Date** — when resolved
- **Threshold** — cut-off or numeric resolution
- **Edge cases** — what happens if data is missing, revised, partial, or delayed
- **Answer type** — yes/no, MC, numeric range, date

### Step 4 — Audit each question
For each candidate, ask:
- Would two informed observers agree on the answer at resolution time?
- Is the resolver named and accessible?
- Are edge cases handled?
- Does this question actually capture what the user cares about?

### Step 5 — Recommend
- Which question best captures the user's underlying interest while being clean to resolve.
- What's lost in the operationalization (the part of the fuzzy claim the question doesn't capture).

### Step 6 — Calibration anchor
Once the question is set, the user states their probability (e.g., 65%) and writes a one-line reasoning note. This becomes the auditable forecast.

---

## False-Positive Prevention

1. **Vague-term smuggling.** "Significant decline" → state the threshold.
2. **Self-resolution.** User as resolver invites motivated reasoning at resolution.
3. **Edge-case blindness.** Most ambiguous resolutions come from unspecified edge cases.
4. **Observable-event confusion.** "X will happen" needs to specify the observable that proves X happened.
5. **Sentiment-prediction.** "X will be considered a success" depends on perception; harder to resolve than measurable outcomes.
6. **Single-candidate output.** First operationalization is rarely best.

---

## Output Format

```
# Probabilistic question design — [fuzzy claim]

## Original claim
> [Verbatim]

## Ambiguities surfaced
- [...]
- [...]

## Candidate questions

### Candidate 1
- **Question:** [one sentence]
- **Resolver:** [...]
- **Observable:** [...]
- **Date:** [...]
- **Threshold / numeric resolution:** [...]
- **Edge cases:** [missing data / revisions / partial / delayed]
- **Answer type:** [yes/no / MC / numeric / date]

### Candidate 2
[Same structure]

### Candidate 3 (optional)
[Same structure]

## Audit
| Candidate | Two-observer agreement? | Edge cases handled? | Captures user's interest? |
|-----------|------------------------|----------------------|----------------------------|
| 1 | yes | yes | mostly |
| 2 | yes | partial | yes |
| 3 | partial | yes | partially |

## Recommendation
- Recommended: Candidate [N]
- Why: [...]
- What's lost: [the part of the original claim this doesn't capture]

## Calibration anchor (user fills)
- Probability: [%]
- One-line reasoning: [...]
- Logged on: [date]
```

---

## Verification

- [ ] Original fuzzy claim captured verbatim.
- [ ] Ambiguities surfaced.
- [ ] 1–3 candidate operationalizations.
- [ ] Each has resolver, observable, date, threshold, edge cases, answer type.
- [ ] Two-observer agreement test passed.
- [ ] User as resolver only if unavoidable.
- [ ] Recommendation states what's lost in operationalization.
- [ ] Calibration anchor fields ready for user.
