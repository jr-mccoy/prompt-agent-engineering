---
title: "Multi-Criteria Decision Analysis (MCDA) — Weighted Scoring with Sensitivity Audit"
category: decision-making/tradeoffs
description: "Compare 2–7 options against 4–10 weighted criteria, producing a weighted score per option. Includes a mandatory sensitivity analysis to test whether the result is robust to plausible weight changes — the primary failure mode of MCDA is false precision from arbitrary weights, and the sensitivity step exists to defeat it."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - decision-making
  - mcda
  - weighted-scoring
  - sensitivity-analysis
  - tradeoffs
updated: "2026-05-10"
reasoning:
  styles: [analytic, multi-criteria, sensitivity]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: scored_matrix_with_sensitivity
  user_role: [analyst, executive, pm, founder, individual, consultant]
  mode: [audit, synthesize, decide]
related_prompts:
  - domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
---

# Multi-Criteria Decision Analysis (MCDA)

**Objective:** Compare 2–7 options against 4–10 weighted criteria. Produce a weighted score per option, but treat the score as a starting point for discussion, not a verdict — and run a mandatory **sensitivity analysis** to test whether the recommended option remains the recommended option under plausible variations in weights and scores. The primary failure mode of MCDA is false precision from arbitrary weights; the sensitivity step exists to defeat it.

**When to use:**
- A real decision between defined options where multiple criteria genuinely matter and no single criterion dominates.
- A team disagreement that's about weights (which criterion matters most) more than about facts. MCDA surfaces the disagreement.
- Vendor selection, hire-vs-build, technology choice, partner selection, location choice — anything with comparable options on multiple axes.
- Pre-mortem on a leaning: if the favored option doesn't win the MCDA, why is it favored?

**When NOT to use:**
- A binary or single-criterion decision. MCDA is overkill.
- The criteria are not commensurable in any meaningful way (e.g., weighing "ethical principles" against "monthly cost"). MCDA forces commensuration; if it shouldn't be forced, use a different method.
- The user wants the score to make the decision. MCDA informs decisions; it doesn't make them.
- Stakes are low. MCDA has overhead.

**Audience:** Analysts, executives, PMs, founders, consultants, individuals making structured choices.

---

## Inputs / Context

1. **The decision.** As a question with named options (2–7).
2. **The criteria** the decision should be judged on (4–10). If unspecified, surface them in step 2.
3. **Stakeholders.** Whose preferences inform the weights. Different stakeholders may produce different weight sets.
4. **Information available.** What's known about each option on each criterion. Gaps are flagged, not invented.
5. **Reversibility / stakes.** Affects how much sensitivity matters. High-stakes irreversible decisions warrant deeper sensitivity work.

---

## Constraints

### Must
- Define criteria **before** scoring options. Criteria must be:
  - **Mutually exclusive** (no double-counting): two criteria measuring the same thing collapse.
  - **Operationalizable** (can be scored with at least rough comparison).
  - **Aligned to the decision** (each criterion meaningfully affects what success looks like).
- Assign **weights** that sum to 100 (or 1.0). Weights elicited from explicit ranking, not by sliders alone.
- Score each option on each criterion using a **consistent scale** (e.g., 1–5 or 0–10). Use the same scale across criteria.
- For each score, attach a **one-line justification** with information source.
- Compute weighted scores: `weighted_score(option) = Σ (weight_i × score(option, i))`.
- Run **sensitivity analysis**:
  - Per-criterion: vary each weight by ±25% and recompute. If the winner changes, the result is fragile on that criterion.
  - Per-score: where information is sparse, vary the score by ±1 unit. If the winner changes, that data gap matters.
  - Result: report the winner under the central case AND the conditions under which a different option wins.
- End with a recommendation that names the winner, the confidence (high/medium/low based on sensitivity), and the conditions that would flip it.

### Must Not
- Pretend the weights are objective. They're judgments. Surface whose judgment.
- Add criteria after seeing scores to make the favored option win.
- Use a 0–100 scale that suggests precision the inputs don't support. 1–5 or 1–10 is honest.
- Treat tied or near-tied results as "MCDA was inconclusive." Near-ties are themselves informative — they mean the criteria don't discriminate.
- Score on an absent criterion as zero. Zero implies it scored badly, not that data is missing. Use `[unknown]` and flag.

---

## Instructions

### Step 1 — Restate the decision
The question and the named options (2–7).

### Step 2 — Surface and define criteria
Generate or refine 4–10 criteria. For each:
- **Name**
- **Definition** (what does scoring high mean)
- **Why it matters for this decision**
- **Mutually exclusive of other criteria?** (Test: would two criteria move together for any option?)

Drop or merge criteria that overlap.

### Step 3 — Elicit weights
Multiple methods:
- **Direct allocation:** distribute 100 points across criteria.
- **Pairwise comparison:** for each pair of criteria, which matters more? Aggregate to weights.
- **Stakeholder elicitation:** if multiple stakeholders, capture each set and compare.

Output: weights summing to 100. Note who provided them.

### Step 4 — Score options
For each (option × criterion) cell:
- Score on the chosen scale (1–5 or 1–10)
- One-line justification with source
- If data is missing: mark `[unknown]` and note what would close the gap

### Step 5 — Compute
Weighted score per option = Σ (weight × score). Show the arithmetic.

### Step 6 — Sensitivity — weights
For each criterion, vary the weight by ±25%, redistribute the change pro-rata across other criteria, and recompute. Report:
- Does the winner change? If yes, on which criterion?
- Robust criteria: weight changes don't flip the winner.
- Sensitive criteria: small weight changes flip the winner. The decision rides on these.

### Step 7 — Sensitivity — scores
For cells with low-confidence scores (sparse data), vary the score by ±1 unit. Report:
- Does the winner change?
- If yes, the data gap matters; recommend filling it before deciding.

### Step 8 — Robust winner identification
- **Robust winner:** wins the central case AND survives sensitivity.
- **Conditional winner:** wins central case but loses under plausible sensitivity. Flag the conditions.
- **Unstable result:** central case has a tight margin and sensitivity flips frequently. Decision is not yet ready; either gather more information or use a different method.

### Step 9 — Discussion of close calls
If two options are within ~5% of each other, MCDA is not discriminating. Surface:
- Which criterion would have to be weighted differently for option B to win?
- Is that weighting defensible?
- If yes, the user can pick either; if not, the central case stands.

### Step 10 — Recommendation
- Recommended option
- Confidence: high (robust) / medium (conditional) / low (unstable)
- Conditions that would flip the decision
- Information that would meaningfully reduce uncertainty

---

## False-Positive Prevention

1. **Weight-tuning to outcome.** Adjusting weights after seeing scores until the favored option wins. Lock weights before scoring.
2. **Criterion stacking.** Adding criteria that overlap to inflate the favored option's score. Mutual exclusivity check.
3. **False precision.** Reporting `73.4` as the weighted score implies precision the inputs don't support. Round to 1 decimal at most; report ranges.
4. **Skipped sensitivity.** MCDA without sensitivity analysis is theater. The sensitivity step is mandatory.
5. **Unknown-as-zero.** Marking missing data as 0 penalizes options unfairly. Use `[unknown]` and flag.
6. **Stakeholder muting.** When stakeholders' weights differ, averaging hides the disagreement. Show the per-stakeholder result and surface where the difference matters.
7. **Decision-by-score.** Treating the highest score as the decision. The score informs; the decision belongs to a person.
8. **Over-criterion fatigue.** 15+ criteria dilute everything to noise. Cap at 10; merge or drop.

---

## Output Format

```
# MCDA — [decision]

## Decision
> [Question]
- Options: [list]

## Criteria
| # | Criterion | Definition (high score means)               | Why it matters | Weight |
|---|-----------|---------------------------------------------|----------------|--------|
| 1 | [...]     | [...]                                       | [...]          | 25     |
| 2 | [...]     | [...]                                       | [...]          | 20     |
| … |           |                                             |                | (sum=100)|

## Weight elicitation method
- Method: [direct allocation / pairwise / stakeholder]
- Source(s): [whose weights]
- If multiple stakeholders: weights per stakeholder shown

## Score matrix (scale: 1–5)
|              | C1 (w=25) | C2 (w=20) | C3 (w=15) | … | Weighted total |
|--------------|-----------|-----------|-----------|---|----------------|
| Option A     | 4 [src]   | 3 [src]   | 5 [src]   |   | [computed]     |
| Option B     | 3 [src]   | 5 [src]   | 4 [src]   |   | [computed]     |
| Option C     | 5 [src]   | 2 [src]   | 3 [src]   |   | [computed]     |

## Score notes
- Option A, C2: [justification, source]
- Option B, C3: [...]
- Option C, C1: [...]
- `[unknown]` cells: [list, with what would close the gap]

## Sensitivity — weights
| Criterion changed | New winner if w ±25% | Robust? |
|-------------------|----------------------|---------|
| C1                | A → A                | yes     |
| C2                | A → B                | no — sensitive |
| C3                | A → A                | yes     |
| …                 |                      |         |

## Sensitivity — scores
| Cell varied      | New winner if score ±1 | Notes                |
|------------------|------------------------|----------------------|
| Option B, C2     | A                      | tight; data gap matters |
| …                |                        |                      |

## Result
- Central-case winner: Option [X]
- Robust winner: [yes / no / conditional]
- Confidence: [high / medium / low]
- Conditions that would flip the decision: [list]
- Information that would reduce uncertainty: [list]

## Close-call discussion (if within ~5%)
- [Which criterion weight would need to change for the runner-up to win]
- [Is that change defensible]

## Recommendation
- Recommended: Option [X]
- Stakes / reversibility consideration: [...]
- Decision-maker: [name]
- By: [date]
```

---

## Verification

- [ ] Criteria defined before scoring.
- [ ] Criteria mutually exclusive (no overlap).
- [ ] Weights sum to 100; source named.
- [ ] Same scale used across criteria.
- [ ] Every score has a justification with source.
- [ ] Missing data marked `[unknown]`, not zero.
- [ ] Weighted scores computed with arithmetic shown.
- [ ] Sensitivity analysis on both weights AND scores.
- [ ] Robust vs sensitive criteria identified.
- [ ] Result classified robust / conditional / unstable.
- [ ] Recommendation includes confidence and flip conditions.
- [ ] No weight-tuning after scoring.
- [ ] No false precision in scores.
