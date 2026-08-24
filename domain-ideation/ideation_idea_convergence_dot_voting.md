---
title: "Idea Convergence — Dot-Voting and Weighted Scoring to a Shortlist"
category: ideation/convergence
description: "The convergence companion to the divergence prompts: take a long idea list and narrow it to a defensible shortlist of 3–7 against explicit criteria. Runs three stages — dot-voting for fast signal, weighted scoring for the survivors, and a final shortlist with rationale and dissent captured. Distinct from multi-criteria decision analysis (which picks among committed options); this narrows an ideation list toward what's worth testing next."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - ideation
  - convergence
  - dot-voting
  - weighted-scoring
  - shortlisting
updated: "2026-05-27"
reasoning:
  styles: [convergent, evaluative, comparative]
  stakes: moderate
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: matrix
  user_role: [pm, designer, founder, facilitator, strategist]
  mode: [converge, decide]
related_prompts:
  - domain-ideation/ideation_forced_quantity_100_ideas.md
  - domain-ideation/ideation_idea_kill_list.md
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
---

# Idea Convergence — Dot-Voting and Weighted Scoring to a Shortlist

**Objective:** Take a long, unfiltered idea list — typically the output of a divergence prompt — and narrow it to a defensible shortlist of 3–7 ideas against explicit criteria. The prompt runs three deliberately-sequenced stages: **dot-voting** for fast, cheap signal that culls the obvious non-starters; **weighted scoring** for the survivors, which exposes the tradeoffs the dots hid; and a **final shortlist** with stated rationale and captured dissent. The sequencing matters — scoring all 80 ideas is wasteful, but dot-voting alone is too coarse to choose between close finalists. This is convergence on an *ideation list* (what's worth testing next), distinct from `tradeoff_multi_criteria_decision_analysis.md`, which is for choosing among a few already-committed options where the decision is the deliverable.

**When to use:**
- After a divergence sprint (quantity, crazy-eights, SCAMPER, persona) that produced more ideas than you can pursue.
- A group needs to narrow without a single voice dominating.
- You have criteria for "worth pursuing" and want them applied transparently rather than by gut.
- Picking which ideas advance to prototyping or a discovery test.

**When NOT to use:**
- You're choosing among 2–4 fully-specified options and the choice is the final decision — use multi-criteria decision analysis instead.
- The list is short enough (≤7) that you can just score it; skip the dot-voting stage.
- The ideas aren't comparable yet (too vaguely stated to evaluate). Sharpen them first.
- You're still diverging — converging too early caps the idea space.

**Audience:** PMs, designers, founders, facilitators, and strategists narrowing a long idea list toward what to test or build next.

---

## Inputs / Context

1. **The idea list.** The full set to narrow, each idea stated clearly enough to evaluate.
2. **Selection criteria.** What makes an idea worth pursuing — e.g., impact, feasibility, novelty, time-to-test, cost, strategic fit. (If unsupplied, propose a default set and confirm.)
3. **Criteria weights.** Relative importance of each criterion. Used in the scoring stage.
4. **Voter pool.** Solo, or a group (how many voters, and any weighting of voices — e.g., domain experts).
5. **Dot budget.** How many dots each voter gets (default: ~⅓ the idea-count, with a cap of 3 dots per idea to prevent stacking).
6. **Shortlist size.** How many finalists are wanted (default 3–7).

---

## Constraints

### Must
- Run the three stages **in order**: dot-vote → weighted-score survivors → shortlist with rationale.
- **Dot-vote stage:** allocate dots across ideas; cap dots-per-idea to force spread; cull everything below a stated threshold. State the threshold *before* counting.
- **Scoring stage:** score only the dot-vote survivors. Score each on every criterion (1–5), multiply by criterion weight, sum to a weighted total. Show the matrix.
- **Capture dissent:** record any idea a minority felt strongly about even if it scored low (the "passion pick"). High-variance ideas are flagged, not silently averaged away.
- Produce a **final shortlist of 3–7** with, for each: weighted score, one-line rationale, and what it would take to test it.
- **Separate the criteria from the ideas' authors** — score the idea on merit, not on who proposed it.
- Note the **runner-ups and the reason each missed**, so a later round can revisit them.

### Must Not
- Score the entire long list — that's the waste the dot-vote stage exists to prevent.
- Average away high-variance ideas. An idea scored 5,5,1 is not the same as 3,3,3; flag the disagreement.
- Let the highest-status voter's dots silently dominate. If voices are weighted, state the weighting; otherwise one-person-one-budget.
- Pick the shortlist purely by weighted score if a flagged passion-pick or strategic outlier deserves a slot. Score informs; it doesn't dictate.
- Treat this as the final decision. The shortlist advances to testing/prototyping, not to launch.

---

## Instructions

### Step 1 — Confirm criteria and weights
List the selection criteria and their weights. If none supplied, propose a default (impact, feasibility, novelty, time-to-test, cost, fit) and confirm. Define each criterion's 1–5 scale in one line so scores are comparable.

### Step 2 — Prepare the list
Ensure each idea is stated clearly enough to evaluate. Merge exact duplicates (note the merge); leave near-duplicates separate for now.

### Step 3 — Dot-vote
State the dot budget per voter and the per-idea cap. Allocate dots (in solo mode, the user allocates by gut "what's worth a closer look"). State the cull threshold before counting. Cull everything below it. Record the surviving set.

### Step 4 — Weighted scoring
For each survivor, score every criterion 1–5. Multiply by weight, sum to a weighted total. Build the matrix. Note score variance where a group disagreed.

### Step 5 — Flag the outliers
Identify: high-variance ideas (strong disagreement), passion-picks (a minority championed it), and strategic outliers (low score but uniquely important on one dimension). These get considered for the shortlist alongside top scorers.

### Step 6 — Build the shortlist
Select 3–7 finalists: primarily the top weighted scores, plus any flagged outlier that earns a slot. For each, write a one-line rationale and the smallest test that would validate it.

### Step 7 — Record runner-ups and dissent
List the ideas that just missed and why, and any dissent worth preserving. A future round may revisit them.

### Step 8 — Hand off
The shortlist advances to prototyping or a discovery test — not to a launch decision. If a true commit-decision among the finalists is needed later, hand to `tradeoff_multi_criteria_decision_analysis.md`.

---

## False-Positive Prevention

1. **Scoring everything.** Applying the full weighted matrix to all 80 ideas burns effort on obvious non-starters. Dot-vote first; score only survivors.
2. **Variance laundering.** Averaging 5,5,1 to "3.7" hides a real split. Flag high-variance ideas; the disagreement is information.
3. **Status capture.** The senior person's dots quietly deciding everything defeats the point of voting. Equal budgets unless weighting is explicit and stated.
4. **Score worship.** Treating the weighted total as the verdict ignores the strategic outlier that scores low but matters uniquely. Score informs the shortlist; judgment finalizes it.
5. **Threshold-after-counting.** Setting the cull line after seeing the dot counts lets bias creep in. State the threshold first.
6. **Author bias.** Scoring an idea higher because the founder proposed it corrupts the matrix. Score the idea, not the proposer.
7. **Premature finality.** Treating the shortlist as the decision skips the cheap learning a test would provide. The shortlist is what to *test*, not what to *ship*.
8. **Criterion vagueness.** Undefined criteria ("impact: 1–5") produce non-comparable scores. Define each scale in a line before scoring.

---

## Output Format

```
# Idea convergence — [brief / source list]

## Criteria and weights
| Criterion | Weight | 1–5 scale definition |
|-----------|--------|----------------------|
| Impact | 0.30 | 1 = trivial … 5 = transformative |
| Feasibility | 0.25 | 1 = near-impossible … 5 = trivial to build |
| Novelty | 0.15 | … |
| Time-to-test | 0.15 | … |
| Cost | 0.10 | … |
| Fit | 0.05 | … |

## Stage 1 — Dot-vote
- Voters: [N] | Dot budget each: [N] | Per-idea cap: [N]
- Cull threshold (stated first): [≥ X dots]
| Idea (short) | Dots | Survives? |
|--------------|------|-----------|
| [...] | 7 | yes |
| [...] | 1 | no |
| … | | |
- Survivors: [N ideas]

## Stage 2 — Weighted scoring (survivors only)
| Idea | Impact | Feas | Nov | TTT | Cost | Fit | Weighted total | Variance? |
|------|--------|------|-----|-----|------|-----|----------------|-----------|
| [...] | 5 | 3 | 4 | 4 | 3 | 5 | [w-sum] | low |
| [...] | 4 | 5 | 2 | 5 | 4 | 3 | [w-sum] | HIGH (5,5,1 on impact) |
| … | | | | | | | | |

## Flagged outliers
- High-variance: [ideas + the split]
- Passion-picks: [idea + who championed + why]
- Strategic outliers: [low score, uniquely important on X]

## Final shortlist (3–7)
| Idea | Weighted total | Rationale (1 line) | Smallest test |
|------|----------------|--------------------|---------------|
| [...] | [score] | [...] | [...] |
| … | | | |

## Runner-ups and dissent
- Just missed: [idea — reason]
- Dissent preserved: [...]
- Next: prototyping / discovery test. (Commit-decision among finalists → tradeoff_multi_criteria_decision_analysis.md.)
```

---

## Verification

- [ ] Criteria listed with weights and 1–5 scale definitions.
- [ ] Three stages run in order (dot-vote → score survivors → shortlist).
- [ ] Cull threshold stated before counting dots.
- [ ] Only dot-vote survivors scored on the weighted matrix.
- [ ] High-variance ideas flagged, not averaged away.
- [ ] Passion-picks and strategic outliers considered for the shortlist.
- [ ] Final shortlist of 3–7 with rationale and a smallest test each.
- [ ] Runner-ups and dissent recorded.
- [ ] Shortlist framed as what-to-test, not the final decision.
