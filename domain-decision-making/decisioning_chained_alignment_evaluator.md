---
title: "Chained Decision Alignment Evaluator"
category: decision-making
description: "Evaluate how a chain of recent or upcoming decisions aligns or diverges against a stated top-level objective. Surfaces drift, contradictions between adjacent decisions, compounding misalignment, and a recovery-step plan to bring the chain back on-objective without re-litigating every link."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - decision-making
  - alignment
  - drift
  - chain-of-decisions
  - recovery
updated: "2026-04-25"
related_prompts:
  - domain-decision-making/decisioning_first_principles_problem_decomposition.md
  - domain-decision-making/decisioning_comprehensive_rapid_tradeoff_analyzer.md
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
  - domain-productivity/operating-cadence/cos_weekly_review.md
---

# Chained Decision Alignment Evaluator

**Objective:** Take a stated top-level objective and a chain of 4–12 recent or upcoming decisions and evaluate whether the chain, taken as a whole, advances the objective. Surface drift (small per-decision misalignments compounding over time), contradictions (adjacent decisions undoing each other), and silent priority changes (the implicit objective the chain is actually serving). Output a recovery-step plan that brings the chain back on-objective without re-litigating every link.

**When to Use:**
- A quarter or initiative is mid-flight and the team is "executing" but the gap between strategy doc and reality is widening.
- You are reviewing the last 30–90 days of decisions (yours, your team's, or a portfolio's) and want to test whether the chain is coherent.
- A new decision is up next and you want to check whether saying yes to it would compound an existing drift.
- You inherited a project mid-stream and need to map whether prior decisions still serve the stated objective.

**When NOT to use:**
- You're evaluating a single decision in isolation. Use a tradeoff analyzer.
- You don't yet have a stated top-level objective. Use a goal-system or objective-clarification prompt first.
- You're auditing past decisions for personal judgment-quality rather than chain coherence. Use the judgment assessment prompt instead.

**Audience:** Founders, project leads, chiefs of staff, individual contributors with decision-tracking responsibility.

---

## Inputs / Context

1. **The stated top-level objective.** One sentence. Include the time horizon. Example: "By end of Q3, our objective is to convert pilot customers into paid contracts at 30% conversion or higher."
2. **The decision chain.** 4–12 decisions, in chronological order, with dates. Each decision should include: what was decided, the alternative not chosen, and the stated rationale at the time.
3. **Anything excluded.** Decisions made by others (sister teams, leadership) that affect the chain but are not in the user's control. List separately.
4. **The forcing function.** What is making the user evaluate the chain right now — a deadline, a pivot, a new constraint, a new hire, a prior commitment coming due.
5. **Optional: prior alignment evaluations.** If this is a recurring evaluation, link to the prior round so we can detect repeat drift patterns.

If the chain has fewer than 4 decisions, **stop** — the prompt is designed for chain-level patterns; for single decisions use a tradeoff analyzer.

---

## Constraints

### Must
- Score each individual decision against the stated objective on a 3-tier scale: **on-objective**, **lateral** (neither advances nor hurts), or **off-objective** (advances a different goal). Each score requires a one-line reason.
- Identify drift: count off-objective decisions; if ≥ 25% of the chain is off-objective, name the drift explicitly.
- Identify contradictions: pairs of decisions in the chain where the second partially undoes the first. Each contradiction must name both decisions and the cost of the undoing (rework, momentum lost, sunk specificity).
- Surface the **revealed objective** — the goal the chain is actually serving, derived from the pattern of decisions. If the revealed objective differs from the stated objective, name that gap.
- Output a recovery plan with three categories: keep (decisions that stand), pause (decisions in flight to halt), reverse (decisions to undo or counter-balance).
- End with a "next decision" guard: a one-paragraph rule for evaluating the next upcoming decision against the chain pattern.

### Must Not
- Re-litigate every decision. The point is chain pattern, not per-decision second-guessing.
- Score against the user's own current preferences. Score against the stated top-level objective only.
- Treat lateral decisions as failures. Lateral is fine in moderation; only flag when laterals dominate.
- Recommend reversing decisions whose reversal cost exceeds the misalignment cost. The recovery plan must be net-positive.
- Hide the revealed objective gap. If the chain is serving a different goal than stated, surface it loudly.

---

## Instructions

### Step 1 — Restate
Restate the top-level objective. Restate the chain in chronological order with dates. Restate the forcing function.

### Step 2 — Per-decision scoring
For each decision, score against the objective:
- **On-objective (O):** decision directly advances the stated objective.
- **Lateral (L):** decision is necessary but does not advance or hurt the objective directly (infra, hires, internal cleanup that the objective doesn't require but doesn't harm).
- **Off-objective (X):** decision advances a different goal, even if a worthy one.

Each score gets a one-line reason. Optional `?` if rationale at the time of decision is unclear.

### Step 3 — Drift detection
Compute the off-objective ratio: `count(X) / total decisions`.
- < 15%: drift not detected.
- 15–25%: early drift; flag.
- 25–40%: significant drift; the chain is partially serving another objective.
- > 40%: chain has effectively re-pointed.

Walk the chain in order; mark whether off-objective decisions cluster at the start, middle, or end. End-clustered drift is recent and easier to recover.

### Step 4 — Contradiction detection
Find pairs of decisions where decision N+k partially undoes decision N. For each contradiction:
- Name decision A and decision B.
- Describe what B undoes about A (work, optionality, commitments, structural choice).
- Estimate cost of the contradiction (rework time, momentum, partner trust, switching cost).
- Surface whether the contradiction is *coherent* (a sign the team learned and corrected) or *thrash* (a sign of weak commitment or shifting framing).

### Step 5 — Revealed objective
From the pattern of off-objective decisions, derive the **objective the chain is actually serving**. State it in one sentence. Compare to the stated objective:
- **Aligned:** revealed = stated. Drift was random noise.
- **Adjacent:** revealed is a sibling goal of stated (e.g., stated "30% conversion," revealed "build long-term customer relationships even at lower near-term conversion"). Useful information but the chain may need re-stating, not redirecting.
- **Diverged:** revealed is a different goal from stated. The chain has quietly re-pointed and the user must either restate the objective or change course.

### Step 6 — Recovery plan
Produce three lists with reasoning:
- **Keep:** decisions that stand. Briefly note why even the off-objective ones are not worth reversing.
- **Pause:** in-flight decisions or follow-ons that should be halted before they compound. Each entry names the trigger to resume.
- **Reverse:** decisions to undo or counter-balance with a corrective decision. Each entry names: (a) the corrective action, (b) its cost, (c) what becomes possible after reversal that wasn't possible before.

Order Reverse decisions by ROI on alignment recovered per unit of cost.

### Step 7 — Next-decision guard
Write a one-paragraph rule for evaluating the next upcoming decision: "If the next decision is X, before committing, check (a) whether it cluster-fits the existing drift pattern, (b) whether it interacts with any active contradiction, and (c) whether it serves the stated or revealed objective." This is the user's pocket check until the next chain review.

---

## False-Positive Prevention

1. **Lateral confused with off-objective.** A lateral decision is neutral; an off-objective decision serves a different goal. Don't flag laterals as drift.
2. **Hindsight contamination.** A decision that was on-objective at the time but is now lateral due to new information should be scored at-the-time. Flag the staleness, but don't punish past selves.
3. **Coherent correction mistaken for thrash.** A reversal because new information arrived is coherent learning, not chain weakness. Distinguish.
4. **Stated-objective protection.** The temptation is to reframe the stated objective so the chain looks aligned. Don't. The whole value is in surfacing the gap between stated and revealed.
5. **Recovery-cost blindness.** Reversing a decision that has already paid most of its cost may not improve alignment net of rework. Check ROI before recommending reverse.
6. **Cluster blindness.** Drift clustered at the end of a chain is recoverable; drift in the middle is harder; drift at the start is structural. Treat the cluster pattern as information, not noise.
7. **Single-author chain.** If decisions in the chain were made by different people, don't attribute pattern to one person's judgment. The chain is a system property.

---

## Output Format

```
# Chain alignment evaluation — [date of evaluation]

**Top-level objective:** [stated objective in one sentence + horizon]
**Forcing function:** [why now]
**Chain length:** [N decisions]
**Period covered:** [start date – end date]

## Per-decision scoring

| # | Date       | Decision (one line)            | Score | Reason                              |
|---|------------|--------------------------------|-------|-------------------------------------|
| 1 | YYYY-MM-DD | [decision]                     | O / L / X | [one-line reason]               |
| 2 | …          | …                              | …     | …                                   |
| … |            |                                |       |                                     |

## Drift summary
- Off-objective ratio: [N/total = X%]
- Drift verdict: [no drift / early / significant / re-pointed]
- Cluster: [start / middle / end]

## Contradictions

| A # | B # | What B undoes about A           | Cost                | Type             |
|-----|-----|---------------------------------|---------------------|------------------|
| 3   | 7   | […]                             | [rework / momentum] | coherent / thrash|
| …                                                                                       |

## Revealed objective
- The chain is actually serving: "[revealed objective in one sentence]"
- Comparison to stated: [Aligned / Adjacent / Diverged]
- Implication: [restate / redirect / continue]

## Recovery plan

**Keep:**
- [#1, #2, …] — [reasoning]

**Pause:**
| In-flight item | Why pause                | Trigger to resume    |
|----------------|---------------------------|----------------------|
| [item]         | [reason]                  | [event / signal]     |

**Reverse (ordered by ROI):**
| Decision # | Corrective action  | Cost            | What becomes possible after |
|------------|--------------------|-----------------|------------------------------|
| [#]        | [action]           | [cost]          | [what unlocks]               |
| …          |                    |                 |                              |

## Next-decision guard
> [one paragraph rule for evaluating the next decision against the chain pattern]
```

---

## Verification

- [ ] Every decision in the chain has an O/L/X score and a one-line reason.
- [ ] Off-objective ratio is computed and a drift verdict is assigned.
- [ ] Drift cluster (start / middle / end) is identified.
- [ ] All contradictions are paired and classified as coherent or thrash.
- [ ] Revealed objective is named in one sentence.
- [ ] Stated-vs-revealed comparison produces one of the three verdicts (Aligned / Adjacent / Diverged).
- [ ] Recovery plan has Keep, Pause, and Reverse buckets, with Reverse ordered by ROI.
- [ ] Each Pause entry names a resume trigger.
- [ ] Each Reverse entry names cost and post-reversal upside.
- [ ] Next-decision guard is present and specific to this chain.
