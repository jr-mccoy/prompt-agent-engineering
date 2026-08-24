---
title: "Super-Forecaster Decomposition — Tetlock-Style Sub-Question Tree"
category: reasoning-craft/forecasting
description: "Decompose a fuzzy forecast into a tree of sub-questions whose answers can be estimated more reliably than the parent. Combine sub-question estimates back into a parent probability with explicit aggregation logic. Improves forecast resolution by isolating estimable components from speculative ones."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - forecasting
  - decomposition
  - sub-questions
  - tetlock
  - probabilistic
updated: "2026-05-10"
reasoning:
  styles: [decomposition, probabilistic, conjunctive]
  stakes: variable
  horizon: months_to_years
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: question_tree_with_aggregation
  user_role: [analyst, forecaster, founder, investor, executive, policy]
  mode: [forecast, audit]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_reference_class_forecast.md
  - domain-reasoning-craft/reasoning-moves/reasoning_fermi_estimation.md
  - domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
---

# Super-Forecaster Decomposition

**Objective:** Take a fuzzy or compound forecast question and decompose it into a tree of 3–7 sub-questions whose individual answers can be estimated more reliably than the parent. Estimate each sub-question's probability or magnitude with a base-rate or reference class. Aggregate the sub-question estimates into a parent estimate using explicit logic (conjunction, disjunction, or weighted combination). The diagnostic value is isolating the *estimable* components of the forecast from the speculative ones.

**When to use:**
- A forecast as posed feels unanswerable ("Will this category exist in five years?") and needs to be broken into components.
- A team's forecast disagreement seems unresolvable; decomposition surfaces which sub-question they actually disagree on.
- Reference-class forecasting alone is insufficient because the forecast involves multiple conjunctive or disjunctive conditions.
- The user is a regular forecaster building a personal track record and wants disciplined decomposition.

**When NOT to use:**
- The forecast is clean enough to estimate directly via base rate (single class, single event). Use `reasoning_reference_class_forecast.md`.
- The decomposition would produce more sub-questions than can be reliably estimated. (If 8+ sub-questions are needed, the forecast is too compound to be useful.)
- The deadline is too tight for sub-question research.

**Audience:** Analysts, forecasters, founders, investors, executives, policy people building probabilistic theses.

---

## Inputs / Context

1. **The parent forecast question.** Phrased as a yes/no with horizon, OR as a quantitative outcome with horizon.
2. **Resolution criteria.** What evidence will count as "yes" / "no" / measured value at the resolution date? If unclear, sharpen first.
3. **The user's current rough estimate.** Captured up front to detect anchoring or motivated reasoning later.
4. **Available evidence and reference classes.** What data exists for the sub-questions?
5. **Aggregation logic intuition.** Does the parent question hold only if *all* sub-questions hold (conjunction)? *Any* (disjunction)? Weighted combination?

---

## Constraints

### Must
- Decompose into 3–7 sub-questions. Fewer than 3 isn't decomposition; more than 7 destroys reliability.
- Each sub-question must be **more estimable** than the parent (closer to a known reference class, more directly observable, or shorter horizon).
- Each sub-question gets its own probability or value estimate with a justification.
- The aggregation logic must be stated explicitly (conjunction / disjunction / weighted combination) and shown mathematically.
- Compare the aggregated estimate to the user's pre-decomposition estimate. Large gaps surface either decomposition errors or anchoring errors.
- For each sub-question, mark whether its estimate is **data-anchored** (reference class exists), **mechanism-anchored** (reasoning from how the world works), or **judgment-anchored** (informed guess). Different anchors carry different weight.

### Must Not
- Decompose into sub-questions that are themselves as fuzzy as the parent. The whole point is increased estimability.
- Pretend conjunctive logic produces high probabilities. If the forecast requires 5 things to all happen at 70% each, the parent is roughly 17% under independence — higher if the sub-events are positively correlated.
- Treat sub-question estimates as independent when they share dependencies. Correlated sub-questions need to be modeled jointly or the aggregation is wrong.
- Anchor every sub-question on the same source. Diverse sub-question anchoring is part of the value.
- Smuggle the user's intuition back in by tuning sub-question estimates until the parent matches their gut.

---

## Instructions

### Step 1 — Capture and seal the user's rough estimate
Get the user's current best probability/value for the parent. Record it. Do not let it influence subsequent steps.

### Step 2 — Sharpen resolution criteria
Restate the parent question with crisp resolution criteria: who decides yes/no, by what observable, by what date. If the user can't answer this, the forecast is not yet meaningful.

### Step 3 — Decompose
Generate 3–7 sub-questions whose answers, jointly, determine the parent. The decomposition can be:
- **Sequential:** sub-questions chained in time (Q1 happens, then Q2, then Q3).
- **Conjunctive:** parent is true iff all sub-questions are true.
- **Disjunctive:** parent is true iff any sub-question is true.
- **Pathway:** multiple paths to the parent outcome, each pathway is a conjunction.
- **Quantitative:** parent quantity = function of sub-quantities.

Pick the structure that matches the parent question's logic. State it.

### Step 4 — Estimate each sub-question
For each sub-question:
- Probability or value (range)
- Base rate or reference class used
- Anchor type: data / mechanism / judgment
- One-sentence justification
- Confidence: low / moderate / high

### Step 5 — Check independence
For each pair of sub-questions whose joint outcome matters: independent or correlated? If correlated, by how much? Correlation collapses conjunctions and inflates disjunctions; build it into the aggregation.

### Step 6 — Aggregate
Apply the aggregation logic:
- Conjunction (independent): `P(parent) = ∏ P(sub_i)`
- Conjunction (correlated): adjust toward higher value if positively correlated.
- Disjunction (independent): `P(parent) = 1 − ∏(1 − P(sub_i))`
- Pathway: `P(parent) = 1 − ∏(1 − P(pathway_j))` for independent pathways.
- Quantitative: combine via the model function.
- Weighted combination: state the weights and justify them.

Show the arithmetic.

### Step 7 — Compare to inside-view estimate
- User's rough estimate: [X]
- Aggregated decomposed estimate: [Y]
- Gap: [direction, magnitude]
- Diagnosis:
  - **Aligned:** the user's intuition was calibrated against the implicit decomposition.
  - **Inside high vs decomposed low:** likely conjunction blindness — the user underestimated how many things have to go right.
  - **Inside low vs decomposed high:** likely overlooking pathways or correlated wins.
  - **Anchoring contamination:** if the user revises sub-question estimates after seeing the gap, restart with a fresh decomposition.

### Step 8 — Identify the load-bearing sub-question
Which sub-question's uncertainty contributes the most to parent uncertainty? That's where additional research moves the forecast most.

### Step 9 — Final estimate
- Point estimate: [P]
- 80% credible interval: [low, high]
- Confidence: low / moderate / high (anchored on weakest sub-question and aggregation reliability)
- Next-research pointer: [load-bearing sub-question to investigate further]

---

## False-Positive Prevention

1. **Conjunction blindness.** People systematically overestimate the probability of compound events. A forecast requiring 5 things at 80% each is at 33% under independence, not 70%.
2. **Sub-question redundancy.** Two sub-questions that are slight rewordings of the same underlying observable are one question, not two. Multiplying their probabilities would double-discount.
3. **False independence.** Most real-world sub-questions are correlated. For positively correlated sub-events, naïve product gives misleading low probabilities for conjunctions and misleading high probabilities for disjunctions (negative correlation reverses the direction).
4. **Anchored decomposition.** Building a decomposition that conveniently aggregates to the user's gut estimate. Test by sharing the decomposition without the parent estimate and asking a peer to aggregate independently.
5. **Sub-question fuzziness.** If a sub-question is no easier to estimate than the parent, it adds noise rather than signal. Discard or replace.
6. **Premature precision.** Reporting `P(parent) = 0.387` from sub-question estimates each marked "low confidence" is false precision. Round and report a range.
7. **Aggregation mismatch.** Treating a pathway question as a pure conjunction (or vice versa) yields a wrong number. Validate the structure with a quick sanity check: list 2–3 ways the parent could resolve "yes" and confirm the aggregation captures them.

---

## Output Format

```
# Decomposed forecast — [parent question]

## Resolution criteria
- Yes / no / value defined as: [criteria]
- Resolution date: [date]
- Resolver: [user / explicit external observable]

## User's pre-decomposition estimate (sealed)
- Estimate: [P or value]
- Justification: [one line]

## Decomposition structure
- Type: [conjunction / disjunction / pathway / quantitative / weighted combination]
- Justification for structure: [one line]

## Sub-questions
| # | Sub-question | Estimate (range) | Reference / anchor | Anchor type | Confidence |
|---|--------------|------------------|--------------------|-------------|------------|
| 1 | [Q]          | 0.6 (0.5–0.7)    | [base rate / mech] | data        | moderate   |
| 2 | [Q]          | 0.8 (0.7–0.9)    | [...]              | mechanism   | low        |
| … |              |                  |                    |             |            |

## Independence / correlation
| Pair | Correlation | Direction | Adjustment |
|------|-------------|-----------|------------|
| 1,2  | moderate    | positive  | +5pp on conjunction |
| …    |             |           |            |

## Aggregation
- Formula: [explicit]
- Computation: [show arithmetic]
- Aggregated parent estimate: [P or value]

## Inside vs decomposed
- User's estimate:      [P]
- Decomposed estimate:  [P]
- Gap:                  [magnitude, direction]
- Diagnosis:            [aligned / conjunction-blind / pathway-blind / anchoring]

## Load-bearing sub-question
- Sub-question: [#]
- Why load-bearing: [highest variance contribution]
- Recommended next research: [specific]

## Final
- Point estimate:       [P or value]
- 80% credible interval: [low, high]
- Confidence:           [low / moderate / high]
- Next-evidence pointer: [observable that would meaningfully shift the forecast]
```

---

## Verification

- [ ] User's pre-decomposition estimate captured before sub-question work.
- [ ] Resolution criteria sharpened and explicit.
- [ ] 3–7 sub-questions, each more estimable than the parent.
- [ ] Each sub-question has anchor type (data / mechanism / judgment) labeled.
- [ ] Aggregation logic is named and arithmetic shown.
- [ ] Independence / correlation between sub-questions assessed.
- [ ] Inside-view vs decomposed comparison performed and gap diagnosed.
- [ ] Load-bearing sub-question identified.
- [ ] Final estimate as range, not point, with confidence rating.
- [ ] No conjunction blindness in the aggregation.
