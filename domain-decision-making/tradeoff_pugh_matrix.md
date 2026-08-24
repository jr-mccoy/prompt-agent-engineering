---
title: "Pugh Matrix — Baseline-Relative Option Comparison"
category: decision-making/tradeoffs
description: "Compare options against a single baseline (often the status quo) by scoring each criterion as better (+1), same (0), or worse (-1) relative to that baseline, then summing and ranking. Deliberately less precise than MCDA's absolute scoring — it trades resolution for speed and for forcing an explicit 'compared to what' frame. Includes a weighted variant and a concordance/discordance read so a high sum built on one criterion doesn't masquerade as broad superiority."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - decision-making
  - pugh-matrix
  - baseline-comparison
  - concept-selection
  - tradeoffs
updated: "2026-05-10"
reasoning:
  styles: [comparative, relative-scoring, taxonomic]
  stakes: variable
  horizon: variable
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: matrix
  user_role: [engineer, designer, pm, analyst, founder, individual]
  mode: [converge, decide, synthesize]
related_prompts:
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
---

# Pugh Matrix

**Objective:** Compare 2–8 options against a chosen **baseline** across a set of criteria, scoring each option-on-criterion as **+1** (better than baseline), **0** (same as baseline), or **−1** (worse than baseline). Sum per option, rank, and read the pattern. The Pugh method (concept selection / controlled convergence) deliberately refuses the false precision of absolute scoring: you never claim option A scores "7.3 on cost," only that it is better, same, or worse than the reference on cost. That constraint is the method's value — it is fast, hard to game with fake decimals, and it forces every comparison through the question "compared to what?"

This prompt produces the unweighted Pugh matrix, an optional **weighted variant** (weights × relative scores), and a **concordance/discordance** read so that a positive sum carried by a single criterion is not mistaken for across-the-board dominance.

**When to use:**
- Engineering or design concept selection, where one option (current design, incumbent vendor, status quo) is the obvious reference point.
- Early-stage convergence on a long list of options, before you've earned the data for absolute scoring.
- A quick product or vendor comparison where "is this better than what we have?" is the real question.
- As a fast first pass *before* MCDA — Pugh narrows the field, MCDA resolves the finalists.
- Iterative design: run, identify weak criteria on the leading option, improve it, re-run.

**When NOT to use:**
- There is no sensible baseline and no option is a natural reference. Use MCDA's absolute scoring instead.
- You need magnitude, not direction (e.g., "how *much* cheaper" decides the call). Pugh hides magnitude by design.
- A single criterion legitimately dominates. Just compare on that.
- The options are not comparable on shared criteria at all.

**Audience:** Engineers, designers, PMs, analysts, founders, and individuals selecting among concrete options where one option is the natural "compared-to-what" anchor.

---

## Inputs / Context

1. **The decision.** A question with named options (2–8).
2. **The baseline.** Which option is the reference. If unspecified, default to the status quo / incumbent / current design and say so.
3. **The criteria** (4–12). If unspecified, surface them in Step 2.
4. **Information per option-criterion.** Enough to judge direction (better / same / worse) relative to baseline. Magnitude not required.
5. **Whether weighting is wanted.** If criteria differ materially in importance, run the weighted variant.

---

## Constraints

### Must
- Name the **baseline** explicitly and score everything relative to it. The baseline's row is all zeros by definition.
- Define criteria **before** scoring. Each must be operationalizable as a better/same/worse judgment against the baseline.
- Use the strict **{+1, 0, −1}** scale. No "+2 for much better" in the base matrix — that reintroduces the magnitude the method exists to suppress. (Magnitude lives in the weighted variant via weights, not via score inflation.)
- For each non-zero score, attach a **one-line reason** naming the direction and why.
- Report, per option: **sum of scores**, **count of +1s, 0s, −1s** (this is the concordance/discordance read), and rank.
- Flag any option whose positive sum depends on a single +1 while carrying multiple −1s — a "spiky winner."
- If weighting: weights need not sum to 100; relative weights are fine. Weighted score = Σ(weight × relative score). Report both unweighted and weighted ranks and note where they diverge.
- Recommend a next move: adopt the leader, run a second Pugh iteration after improving the leader, or promote the top 2–3 to MCDA.

### Must Not
- Score against an absolute standard instead of the baseline. Every cell answers "vs. baseline," not "good/bad in the abstract."
- Smuggle magnitude into the base matrix with ±2/±3. Direction only.
- Change the baseline mid-matrix. One reference per matrix.
- Treat a tie on sum as uninformative. A tie with different +/−/0 profiles means the options trade differently against the baseline — surface the trade.
- Let a single dominant criterion's +1 drive the recommendation without flagging it as concentration risk.
- Present the sum as a precise score. It is an ordinal signal, not a measurement.

---

## Instructions

### Step 1 — Restate the decision and pick the baseline
State the question, the named options, and which one is the baseline (and why — usually status quo / incumbent). The baseline row will be all 0s.

### Step 2 — Define criteria
List 4–12 criteria. For each: name, the direction that counts as "better," and why it matters. Drop criteria where every option would tie the baseline (they carry no signal).

### Step 3 — Score each non-baseline option per criterion
For each cell: **+1 / 0 / −1** vs. baseline, with a one-line reason. Where direction is genuinely unclear, mark `S` (≈ same, scored 0) and flag the uncertainty rather than guessing a sign.

### Step 4 — Sum and profile
Per option compute: sum (Σ scores), and the **profile** = (#+1, #0, #−1). The profile is the concordance/discordance read.

### Step 5 — Rank (unweighted) and spot spiky winners
Rank by sum. Flag any leader whose sum is carried by one criterion (e.g., +1 once, −1 three times, sum still positive only because that one +1 is on a criterion that happens to be present). A high sum with a thin profile is fragile.

### Step 6 — Weighted variant (if criteria importance varies)
Assign each criterion a relative weight. Weighted score = Σ(weight × relative score). Re-rank. Compare to the unweighted rank: where they agree, confidence is higher; where they diverge, the divergence is itself the finding (the result rides on the weights).

### Step 7 — Read the pattern, not just the number
- **Clear leader:** top by both sum and profile (more +1s, few −1s), stable under weighting.
- **Spiky leader:** high sum, thin profile. Treat as provisional; the −1s may be disqualifying.
- **Trading pair:** two options tie or near-tie with opposite profiles. Name what each trades for what.

### Step 8 — Iterate or promote
- **Improve and re-run:** take the leader, attack its −1 criteria, redesign, re-score. Controlled convergence.
- **Promote to MCDA:** if the top 2–3 are close and the decision is high-stakes, hand them to `tradeoff_multi_criteria_decision_analysis.md` for absolute scoring + sensitivity.
- **Adopt:** if the leader is clean and stakes are modest, decide.

### Step 9 — Recommendation
State the leader, its profile, whether it's clean or spiky, whether weighting changed the order, and the recommended next move (adopt / iterate / promote).

---

## False-Positive Prevention

1. **Absolute-scoring drift.** Scoring "how good is cost" instead of "better/worse than baseline on cost." Every cell is relative to the baseline, full stop.
2. **Magnitude smuggling.** Using ±2/±3 to express "much better." Banned in the base matrix; importance is expressed via weights, not score size.
3. **Spiky-winner blindness.** A positive sum built on one +1 and several −1s looks like a win. Always report the profile (#+/#0/#−) alongside the sum and flag concentration.
4. **Baseline drift.** Silently changing the reference option partway through. Lock one baseline per matrix.
5. **Criterion padding.** Adding near-duplicate criteria to inflate a favored option's +1 count. Merge overlapping criteria first.
6. **Tie dismissal.** Calling equal sums "inconclusive." Equal sums with different profiles encode a real tradeoff — name it.
7. **Weight-tuning to outcome.** Setting weights after seeing scores to make the preferred option win. Set weights before the weighted pass, from criterion importance alone.
8. **Direction faking.** Forcing a +1/−1 where the data only supports "same / unknown." Use 0 with an uncertainty flag.

---

## Output Format

```
# Pugh Matrix — [decision]

## Decision
> [Question]
- Options: [list]
- Baseline: [option] — [why it's the reference]

## Criteria
| # | Criterion | "Better" means | Why it matters | Weight (optional) |
|---|-----------|----------------|----------------|-------------------|
| 1 | [...]     | [...]          | [...]          | 3                 |
| 2 | [...]     | [...]          | [...]          | 1                 |
| … |           |                |                |                   |

## Matrix (scores relative to baseline; baseline = all 0)
| Criterion        | BASELINE | Option A | Option B | Option C |
|------------------|----------|----------|----------|----------|
| C1               | 0        | +1       | 0        | −1       |
| C2               | 0        | −1       | +1       | +1       |
| C3               | 0        | +1       | +1       | 0        |
| …                | 0        |          |          |          |
| **Sum**          | 0        | +1       | +2       | 0        |
| **Profile (+/0/−)** | —     | 2/1/1    | 2/1/0    | 1/1/1    |
| **Rank (unwtd)** | —        | 2        | 1        | 3        |

## Score reasons (non-zero cells)
- A, C1 (+1): [reason]
- A, C2 (−1): [reason]
- C, C1 (−1): [reason]
- 0-with-uncertainty cells: [list — what would resolve the direction]

## Weighted variant (if used)
| Option | Weighted score (Σ w×score) | Rank (wtd) | Diverges from unwtd? |
|--------|----------------------------|------------|----------------------|
| A      | [...]                      | [...]      | [yes/no]             |
| B      | [...]                      | [...]      | [...]                |
| C      | [...]                      | [...]      | [...]                |
- Where weighted and unweighted ranks diverge: [the result rides on these weights]

## Pattern read
- Leader: [option] — [clean / spiky]
- Spiky-winner flag: [option, if its sum rides on one +1 with multiple −1s]
- Trading pair (if any): [A trades X for Y vs B]

## Recommendation
- Leader: [option]
- Next move: [adopt / improve-and-re-run / promote top N to MCDA]
- If iterating: attack [option]'s −1 criteria: [list]
```

---

## Verification

- [ ] Baseline named explicitly; baseline row is all 0s.
- [ ] Criteria defined before scoring, with a "better means" direction each.
- [ ] Strict {+1, 0, −1} scale in the base matrix (no ±2/±3).
- [ ] Every non-zero cell has a one-line reason.
- [ ] Per-option sum AND profile (#+/#0/#−) reported.
- [ ] Spiky winners (sum carried by one +1) flagged.
- [ ] Weighted variant run if criterion importance varies; divergence from unweighted noted.
- [ ] Ties read as tradeoffs (via profile), not dismissed.
- [ ] No absolute scoring; every cell relative to baseline.
- [ ] Recommendation names a next move (adopt / iterate / promote).
