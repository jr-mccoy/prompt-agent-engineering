---
title: "Rapid Tradeoff Analyzer (Weighted Multi-Criteria)"
category: decision-making
description: "Time-boxed, structured tradeoff analysis across 3–5 options and 4–6 weighted criteria. Produces scored options, a sensitivity check on the winning margin, and an explicit reversibility note — in under 10 minutes of focused work."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - decision-making
  - tradeoff-analysis
  - weighted-scoring
  - rapid-decision
  - sensitivity
updated: "2026-04-23"
related_prompts:
  - domain-decision-making/decisioning_time_boxed_decision_protocol.md
  - domain-decision-making/decisioning_multi_constraint_optimizer.md
  - domain-decision-making/decisioning_first_principles_problem_decomposition.md
---

# Rapid Tradeoff Analyzer (Weighted Multi-Criteria)

**Objective:** Evaluate 3–5 options against 4–6 weighted criteria, score each, compute a weighted total, sanity-check the margin with a one-pass sensitivity analysis, and return a recommendation with a named loser and a reversibility note — all within 10 minutes of focused work.

**When to use:**
- You are stuck between a few real options and starting to ruminate.
- A decision needs to be made this week, the choices are known, and you want structure without a full business case.
- You want to force yourself to name the criteria *before* picking the winner (rather than rationalizing a chosen option).

**Do not use** for strategic, irreversible, multi-million-dollar decisions — those warrant a longer, multi-source analysis. Use this as the first-pass structuring step before committing to a deeper analysis if the margin is thin.

**Audience:** Individual contributors, managers, or small teams making a concrete choice (tool selection, vendor pick, feature prioritization, hire vs. contract, location decisions).

---

## Inputs / Context

1. **The decision in one sentence.** "Which CRM should we pick?" "Should I take job A, B, or stay?" "Which of these three features ships this quarter?"
2. **The options.** 3–5 named options. If you have more than 5, first cull the obvious non-starters. If you have only 2, name a third ("do nothing" or "delay") to force tradeoff thinking.
3. **The deadline.** When does this need to be decided. If the answer is "ASAP" ask for a specific day.
4. **Reversibility.** One-way door (hard to reverse) or two-way door (easy to reverse). Changes how hard you should push the analysis.
5. **Who must agree.** Solo decision, or needs sign-off from others.

If you have fewer than 3 options or cannot name them, **stop** and use `decisioning_first_principles_problem_decomposition.md` to structure the problem first.

---

## Constraints

### Must
- Define 4–6 criteria **before** scoring any option. Criteria that surface after scoring are rationalizations.
- Assign a weight to each criterion summing to 100. Use only these buckets: 30 / 20 / 15 / 10 / 5 (or similar whole-number splits). Avoid 11, 17, 23 — false precision.
- Score each option on each criterion on a 1–5 scale with a one-line reason.
- Compute the weighted total: `sum(score × weight/100)` per option.
- Run a sensitivity pass: if the top-two margin is < 10% of the max possible score, the decision is too close to trust and you must name which criterion weight, if shifted by ±5, would flip the winner.
- Name the **loser** explicitly and state what would have to be true for the loser to become the winner. (This surfaces rationalization.)
- End with a reversibility note: if one-way, flag what's irreversible; if two-way, state the review date to revisit.

### Must Not
- Add criteria after seeing the scores.
- Use weights that sum to anything other than 100.
- Assign a 5 to every criterion for a favored option. If an option is genuinely best on everything, the criteria are probably collinear — re-examine.
- Skip the sensitivity check just because the winner "feels" right.
- Produce a single-digit recommendation without naming why the losers lost.
- Spend more than 10 minutes on a two-way-door decision.

---

## Instructions

### Step 1 — Frame
Restate the decision in one sentence. Name the options (3–5). Name the deadline and reversibility.

### Step 2 — Criteria first
List 4–6 criteria that *actually* matter for this decision. A good criterion is:
- Measurable or at least rankable (not "good vibes")
- Not a synonym of another listed criterion (avoid collinearity)
- Framed as positive (higher = better); if a criterion is negative (cost, risk), either invert it or score it so lower raw becomes higher score.

### Step 3 — Weight
Assign weights summing to 100. Use chunks of 5 or 10. If you cannot differentiate two criteria in weight, collapse them or drop the weaker one.

### Step 4 — Score
For each option × criterion, assign a 1–5 score with a one-line reason. If you don't know enough to score (e.g., cost of Option C is unknown), assign `?` and note what you would need to look up. Don't guess.

### Step 5 — Compute
Weighted total per option = Σ (score × weight / 100). Rank the options.

### Step 6 — Sensitivity check
Compute the margin between top-1 and top-2. Express it as a percentage of the max possible score (5.0).
- If margin ≥ 15% of max: robust winner.
- If margin 5–15%: name the single weight shift (±5 on one criterion) that would flip the winner.
- If margin < 5%: decision is genuinely close; consider a tiebreaker (the most reversible option, the option that preserves optionality, or running a time-boxed experiment).

### Step 7 — Name the loser
Pick the lowest-scoring option. Name the criterion where it scored worst, and state what would need to change for it to become competitive. This is a calibration check on your scoring.

### Step 8 — Reversibility
If one-way door: name what's irreversible (cost, reputation, relationships, switching cost). If two-way: set a calendar date to review the decision.

---

## False-Positive Prevention

1. **Don't let the favored option generate the criteria.** A smell test: if your criteria list reads like the marketing page of your favorite option, start over.
2. **Don't use "fit with our values" as a 30-weight criterion.** Either unpack what "fit" means into concrete criteria or drop it.
3. **Don't resolve ties by re-weighting after scoring.** If the decision is close, it is close — treat that as information, not a problem to score your way out of.
4. **Don't score what you don't know.** A 3 on "unclear" is the same as guessing. Mark `?` and say what you need to find out.
5. **Don't confuse a tradeoff analysis with a consensus-builder.** This tool helps you think. The final decision may still require a conversation with stakeholders.
6. **Don't skip the "name the loser" step.** It's the most effective antidote to rationalization.

---

## Output Format

```
# Tradeoff analysis — [decision in one sentence]

**Deadline:** [date]
**Reversibility:** one-way / two-way
**Decision-maker:** [name]
**Time spent:** [minutes]

## Options
1. [Option A]
2. [Option B]
3. [Option C]

## Criteria (weights sum to 100)
| # | Criterion             | Weight | Higher = better? |
|---|-----------------------|--------|------------------|
| C1| [Criterion]           | 30     | Yes              |
| C2| [Criterion]           | 25     | Yes              |
| …                                                      |

## Scores (1–5 scale)
| Criterion | A | B | C | Reasons (one line each)          |
|-----------|---|---|---|----------------------------------|
| C1        | 4 | 3 | 2 | A: … / B: … / C: …               |
| …                                                      |

## Weighted totals
| Option | Weighted total |
|--------|----------------|
| A      | 3.85           |
| B      | 3.40           |
| C      | 2.90           |

## Sensitivity
- Margin top-1 vs top-2: [N]% of max
- Robust / close / genuinely-tied: [verdict]
- Weight shift that would flip: "If C[n] weight drops from X to X-5 and C[m] rises, winner becomes [option]."

## Loser
- Lowest-scoring option: [option]
- Why it lost: [main criterion]
- What would have to be true to save it: [condition]

## Recommendation
- **Pick:** [option]
- **Why, in one sentence:** [reason linked to the top-weighted criterion]

## Reversibility note
- One-way door: [what's irreversible]
OR
- Two-way door: revisit by [date]; signals to watch: [2–3 signals]
```

---

## Verification

- [ ] Options are named (3–5).
- [ ] 4–6 criteria listed **before** any scores were assigned.
- [ ] Weights sum to exactly 100.
- [ ] Every cell in the scores table has a score and a one-line reason (or `?` with a lookup note).
- [ ] Weighted totals are computed and shown.
- [ ] Sensitivity pass explicitly states the margin category (robust / close / tied).
- [ ] Loser is named with a "what would save it" note.
- [ ] Reversibility note present with either an irreversibility flag or a revisit date.
- [ ] No criterion was added after scoring began.
