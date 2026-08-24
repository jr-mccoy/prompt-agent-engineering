---
title: "Judgment Assessment (Post-Decision Meta-Reflection)"
category: decision-making
description: "Assess the quality of your own judgment on a recent decision after the outcome is at least partially visible. Surfaces cognitive biases that operated, information you should have sought, learning signals to encode, and how to update your decision-making heuristics — distinct from pre-ship validation, which is forward-looking."
techniques:
  - ST-01
  - ST-02
  - RT-01
  - RT-02
  - CM-02
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - decision-making
  - judgment
  - meta-reflection
  - cognitive-bias
  - learning
  - post-decision
updated: "2026-04-25"
related_prompts:
  - domain-decision-making/decisioning_blind_spot_mirror_see_what_im_missing.md
  - domain-decision-making/decisioning_chained_alignment_evaluator.md
  - domain-productivity/validation/judgement_assessment.md
  - domain-personal-development/prompts/agency/agency_feedback_extraction.md
---

# Judgment Assessment (Post-Decision Meta-Reflection)

**Objective:** Take a recent decision the user made (where the outcome is at least partially visible) and assess the *judgment* — not the outcome. Separate the quality of the decision-making from the quality of the result, surface the biases that operated, identify information the user should have sought, extract learning signals, and propose specific updates to their decision-making heuristics. Output a judgment scorecard, a bias inventory, an information-gap map, and a heuristic-update list.

**When to Use:**
- A decision made 2–12 weeks ago has produced enough downstream signal to evaluate.
- A bad outcome occurred and you want to separate "wrong choice" from "right choice + bad luck" before drawing lessons.
- A good outcome occurred and you want to verify the judgment was good (not just lucky) before assuming the heuristic that produced it is reliable.
- You're building a personal calibration practice and want a reusable scaffold for post-decision review.

**When NOT to use:**
- The decision is upcoming (use a tradeoff analyzer or pre-ship validation prompt — this prompt is *backward-looking*).
- The outcome is fully unresolved with no signal yet. Wait until something is visible.
- You want to assess a chain of decisions for alignment drift. Use `decisioning_chained_alignment_evaluator.md` instead.
- You want to extract feedback from a shipped artifact (work-output focused). Use `agency_feedback_extraction.md`.

**Distinction from validation prompts:** Validation prompts (`domain-productivity/validation/`) are pre-ship checks — they ask "before I commit, is this sound?" This prompt is post-ship reflection — it asks "now that I've decided and a signal exists, what can I learn about *how I decide*?"

**Audience:** Anyone building decision-making maturity through deliberate post-mortems on their own calls.

---

## Inputs / Context

1. **The decision in one sentence.** Include the date it was made.
2. **What you chose, and what you considered.** The option picked, the alternatives considered, and what you would say (today) was the deciding criterion at the time.
3. **The outcome so far.** What's visible in the world now. Be specific: revenue numbers, user feedback, internal reactions, downstream constraints. Distinguish between full signal and partial signal.
4. **Your prior prediction.** What did you think would happen, ideally written down at the time. If unrecorded, reconstruct as honestly as possible and flag the reconstruction.
5. **Counterfactual signal (if any).** Any evidence about how the alternatives would have played out (a competitor took option B and… / a parallel team did C and…).
6. **What feels off.** A sentence on what is prompting this review now. "I'm surprised by how it played out" / "I want to verify a hunch was correct" / "I notice I'd make this same call again and want to check whether I should."

---

## Constraints

### Must
- Separate the **decision quality** axis from the **outcome quality** axis. Score each independently on a 1–5 scale and place the result in the 2x2 matrix below. (A bad outcome from a good decision is a Type-II review; a good outcome from a bad decision is a Type-III review.)
- Audit for at least 5 specific cognitive biases that may have operated, naming each with its real definition and the evidence it operated here. Do not include a bias if you do not see evidence; do not list biases as a generic checklist.
- Identify information that was available to seek but not sought. Mark each item with a cost-to-acquire estimate (low / medium / high) and a value-of-information estimate (low / medium / high).
- Extract the learning signal, separating: (a) signal about the world (something true now that was not known before), (b) signal about the user's heuristics (something to update in how they decide), (c) noise (random variance, not learning).
- Produce a heuristic-update list with at most 3 specific updates. More than 3 is over-fitting on one data point.
- End with a calibration check: was the user surprised? If yes, by which axis (decision quality, outcome, or own reaction)? Calibration improves only when surprise is named.

### Must Not
- Score decision quality based on outcome alone. The single most common failure of post-decision review is "it worked, so it was a good decision."
- Hindsight-rewrite the priors. The user's prediction at the time stands, even if today they would say "I always knew it would go that way."
- Listing biases the user already corrects for. The audit is for biases that *did* operate, not a textbook recital.
- Recommend more than 3 heuristic updates from a single data point. Wait for the next review.
- Conflate luck with skill or skill with luck. Each must be named distinctly in the outcome breakdown.
- End with self-flagellation or self-congratulation. The output is calibration data, not a verdict on the user.

---

## Instructions

### Step 1 — Restate
Restate the decision, what was chosen, what was considered, the prediction at the time, the outcome so far (with full vs. partial signal flagged), and what's prompting the review.

### Step 2 — Decompose outcome into luck and skill
Take the visible outcome and break it down:
- **Outcome attributable to the decision (skill):** what would have looked different under any reasonable choice in this situation?
- **Outcome attributable to luck:** what factors were genuinely outside the user's control and decision-relevant?
- **Outcome attributable to execution (post-decision):** what happened after the decision was made due to how it was carried out, not the decision itself?

Quantify roughly (e.g., 60% skill / 30% luck / 10% execution) — even rough numbers force the question.

### Step 3 — Decision quality score (1–5)
Score *the decision-making process and choice*, given only what was knowable at the time:
- 1 — Decision was unsupported by available evidence; biased or rushed.
- 2 — Decision was reasonable but missed a major available consideration.
- 3 — Decision was sound; defensible against the alternatives with available info.
- 4 — Decision was strong; correctly weighted the dominant consideration.
- 5 — Decision was excellent; surfaced and weighted considerations the user typically misses.

State the score and the one-line justification.

### Step 4 — Outcome quality score (1–5)
Score *the outcome*, ignoring decision quality:
- 1 — Outcome materially worse than expected.
- 2 — Outcome below expectation.
- 3 — Outcome on expectation.
- 4 — Outcome exceeded expectation.
- 5 — Outcome materially better than expected.

### Step 5 — 2x2 placement
Place the result in the matrix:
| Decision quality | Outcome quality | Type           | Lesson focus                          |
|------------------|------------------|----------------|---------------------------------------|
| High             | High             | Type-I (good)  | Verify it was skill, not lucky-good   |
| High             | Low              | Type-II        | Process was right; absorb the loss    |
| Low              | High             | Type-III (warn)| Lucky win; don't reinforce the heuristic |
| Low              | Low              | Type-IV (bad)  | Heuristic update warranted            |

The Type tells the user *which* lesson focus to use.

### Step 6 — Bias audit
For each candidate bias, evaluate whether it operated:
- **Anchoring** — fixated on first option / first number?
- **Confirmation** — selectively gathered evidence supporting the leaning?
- **Availability** — over-weighted recent or vivid examples?
- **Sunk-cost** — kept option alive due to prior investment?
- **Status-quo / endowment** — over-valued continuing the current path?
- **Optimism / planning fallacy** — under-estimated time, cost, or downside?
- **Outcome bias / hindsight (in the review itself)** — rewriting the prior with current information?
- **Social proof / herd** — defaulted to what the visible majority did?

For each that operated, name the specific moment in the decision where it shaped the choice. Skip biases for which no evidence is visible. Aim for 3–5 *real* findings, not a checklist of all 8.

### Step 7 — Information gap map
List information that was available to seek and not sought. For each:

| Item not sought | Cost to acquire | Value of information | Why not sought             |
|-----------------|------------------|----------------------|----------------------------|
| [item]          | low / med / high | low / med / high     | [time / awareness / cost]  |

Identify the one item with highest VOI relative to cost. That is the standing lesson: *next time a similar decision arises, seek that item first.*

### Step 8 — Learning signal extraction
Three buckets:
- **Signal about the world:** "X is true now that I didn't know" — generalizable beyond this decision.
- **Signal about your heuristics:** "I systematically [over- / under-] [estimate / weight] [thing] when [context]."
- **Noise:** specific to this case; not generalizable. Resist the urge to lesson-mine here.

### Step 9 — Heuristic updates
At most 3. Each update must:
- Name the heuristic being updated (e.g., "When evaluating contracts > 1 year, I assume my willingness-to-stay matches my current excitement").
- Name the update (e.g., "Replace with: discount willingness-to-stay by 30% when current excitement is high").
- Name the trigger (which class of decision this update applies to).

Fewer is better than more. If only one update is warranted, output one.

### Step 10 — Calibration check
- Were you surprised by the decision-quality score, the outcome score, or both?
- If both: which surprised you more?
- If neither: why is this review worth doing? (Sometimes the answer is "it isn't, this was a routine call." That's a valid result.)

---

## False-Positive Prevention

1. **Outcome contamination of decision score.** The deepest failure mode. If the outcome score is set first and the decision score "agrees," restart with the decision score reasoned independently.
2. **Hindsight rewrite of the prior.** "I always knew it would go that way." If the prior wasn't recorded, mark the reconstruction as low-confidence and resist letting it match the outcome.
3. **Bias-checklist theater.** Naming all 8 biases as "yes, also operating" produces no signal. The audit's value is in identifying the *specific* biases that left fingerprints on this decision.
4. **Over-updating from one data point.** Three heuristic updates from one decision is already aggressive. If the model wants 5, suspect over-fitting.
5. **Self-flagellation or self-congratulation.** Outcomes that feel deserved (good or bad) trigger emotional review, not calibration. The output is data, not verdict.
6. **Type-III silence.** Lucky wins (low decision quality, high outcome) are the most dangerous to misclassify. The reinforcement learning baked into "it worked" is hard to override. Mark Type-III reviews loudly.
7. **Reconstruction as fact.** If the user reconstructs a prior because none was recorded, label every downstream claim that depends on the prior as conditional.
8. **Routine-call masquerading as deep review.** If the calibration check finds no surprise on either axis, accept that this was a routine call and stop. Don't manufacture lessons.

---

## Output Format

```
# Judgment assessment — [decision in one sentence] (decision date: [date])

**Outcome state:** [full / partial signal]
**What's prompting this review:** [one sentence]

## Outcome decomposition
- Skill-attributable: ~X%
- Luck-attributable: ~Y%
- Execution-attributable: ~Z%
- Notes: [paragraph explaining the split]

## Decision quality score
- Score (1–5): [N]
- Justification: [one or two sentences using only what was knowable at the time]

## Outcome quality score
- Score (1–5): [N]
- Justification: [one sentence on outcome vs. expectation]

## 2x2 placement
- Type: [I / II / III / IV]
- Lesson focus: [from matrix]

## Bias audit (operated, not checklist)
1. **[Bias name]** — Where it shaped the choice: [specific moment]
2. **[Bias name]** — Where it shaped the choice: [specific moment]
3. …

## Information gap map
| Item not sought | Cost  | VOI   | Why not sought |
|-----------------|-------|-------|-----------------|
| […]             | low   | high  | […]             |

**Highest-VOI standing lesson:** [item] — seek this first next time similar decision arises.

## Learning signal
- **About the world:** [bullet(s)]
- **About your heuristics:** [bullet(s)]
- **Noise (do not generalize):** [bullet(s)]

## Heuristic updates (max 3)
1. **Heuristic:** [old]
   **Update:** [new]
   **Trigger class:** [decisions of type ___]
2. …

## Calibration check
- Surprised by decision quality? [yes / no — by what]
- Surprised by outcome quality? [yes / no — by what]
- Surprised by your reaction? [yes / no]
- Net: [routine call / genuine learning event / signal of pattern]
```

---

## Verification

- [ ] Decision quality score and outcome quality score are reasoned independently.
- [ ] Outcome decomposition splits skill / luck / execution with rough percentages.
- [ ] 2x2 placement assigns one of the four Types.
- [ ] Bias audit names only biases for which specific operating evidence is given (3–5 real findings, not 8).
- [ ] Information gap map includes cost and VOI per item, and names the single highest-VOI standing lesson.
- [ ] Learning signal section separates world / heuristics / noise.
- [ ] Heuristic updates list is at most 3 items, each with a trigger class.
- [ ] Calibration check explicitly names whether surprise was present and on which axis.
- [ ] No outcome contamination of decision score (re-check by inverting the outcome — would the decision score still hold?).
- [ ] Type-III (lucky win) is loudly marked if applicable.
