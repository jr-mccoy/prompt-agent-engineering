---
title: "Build Personal 'Taste' for AI Output Quality Through Calibrated Comparison"
category: prompt-engineering/evaluation
description: "A structured practice for developing reliable intuition about AI output quality on a recurring task type: blind-score 10–20 outputs against a spec, compare personal scores to the spec's objective score, find where intuition and spec disagree, and correct the mismatch by updating either the spec or the intuition. Builds taste that is calibrated, not just confident."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-06
  - CM-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - task-difficulty
  - taste
  - calibration
  - blind-scoring
  - spec-refinement
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/evaluation/taskdifficulty_decompose_by_axes.md
  - domain-prompt-engineering/evaluation/taskdifficulty_workflow_axis_optimizer.md
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/skill-development/promptcraft_eval_harness.md
---

# Build Personal "Taste" for AI Output Quality Through Calibrated Comparison

**Objective:** Develop calibrated intuition for whether an AI output is good on a recurring task type. The method: blind-score 10–20 outputs both against a spec and against personal judgment, surface the disagreements, and correct them by either refining the spec or retraining the intuition. The output isn't a single number; it's a diagnosis of where the user's taste and their spec diverge, with a plan for closing the gap.

**When to use:** The user works on a recurring task where "is this output good?" is a frequent question and the answer is currently felt rather than reasoned. Or: the user has a spec (via `promptcraft_specification_defines_done.md`) that passes everything on paper but the outputs still feel off. Or: the user wants to stop accepting plausible-looking-but-wrong outputs.

**Audience:** Users who produce and evaluate AI outputs regularly, have a task type they care about, and are willing to invest an hour on deliberate practice.

**Taste, calibrated.** Most users have strong intuitions about their AI outputs. Untested, those intuitions are worth little — they correlate with familiarity as much as with quality. Calibration means finding the specific cases where the intuition is wrong, and either fixing the intuition (it missed something) or fixing the spec (the intuition knows something the spec doesn't). Both failures happen; both matter.

---

## Inputs Required

1. **A recurring task type** the user runs often enough to have 10–20 real past outputs. Not a one-off.
2. **The current spec** for the task — via `promptcraft_specification_defines_done.md` or equivalent. If no spec exists, stop and build one first; scoring without a spec is measuring fog.
3. **10–20 real past outputs of the task.** A mix: some the user accepted, some the user rejected. Variety matters more than total count.
4. **A second person or a time delay.** Blind scoring requires the user not to know, at scoring time, which outputs they previously accepted. Either have someone else anonymize the set, or let 2+ weeks pass so the user has forgotten which was which.

Refuse to run on <10 outputs (not enough variance to find calibration gaps) or on a task without a spec (scoring against intuition alone is just intuition; the calibration depends on spec-vs-intuition divergence).

---

## Instructions

### Step 1 — Prepare the blind set

Strip the outputs of any labels, dates, original authorship cues, or identifiers that would remind the user which output was accepted. Number them 1 to N. If the user can't reliably blind the set themselves, have a second person do it.

### Step 2 — Score each output against the spec

For each output, score per the spec's rubric: must-pass (binary), should-pass (0 / 0.5 / 1), nice-to-have (0 / 1).

Record the per-criterion scores, not just the aggregate. The per-criterion breakdown is where divergences will show up.

Do not look at the next step until this step is complete.

### Step 3 — Score each output on personal intuition

Separately, score each output on gut:
- Overall gut score: 1–5.
- One-line reason: "why does it feel [good / mediocre / bad]?"

Do this without looking at the Step 2 scores.

### Step 4 — Unblind and tabulate

For each output, line up:
- Spec score (aggregate: % must-pass + avg should-pass)
- Intuition score (1–5)
- User's past accept/reject decision

Compute:
- Correlation between spec score and intuition score.
- Cases where spec said "pass" and intuition said "bad" (spec gap).
- Cases where intuition said "good" and spec said "fail" (intuition gap or spec too strict).
- Cases where past-user accepted and current-user rejects, or vice versa (time drift — a finding about the user, not the outputs).

### Step 5 — Diagnose the gaps

For each spec-vs-intuition disagreement, decide: who's right, and why?

**Spec gap (spec passes but intuition rejects):**
- The intuition knows something the spec doesn't.
- Interview the intuition: "why does it feel bad?" Usually the answer is a missing criterion.
- If the answer is a genuine criterion, add it to the spec (rewrite observable, rank, re-close the set per `promptcraft_specification_defines_done.md`).
- If the answer is taste-drift or familiarity bias, the intuition is wrong; note it and move on.

**Intuition gap (spec fails but intuition approves):**
- The user was about to accept an output that objectively misses requirements.
- This is the dangerous kind of divergence — plausible-looking wrong answers passing.
- Do not loosen the spec to match. Force the intuition to update.
- Ask: what did the output do that made it feel right? Often it was a shallow signal (tone, length, fluency) that correlated historically with quality but doesn't this time.

**Time drift (past decisions disagree with current ones):**
- Either the user's standards have risen (fine; nothing to fix except the old specs).
- Or the user's standards have drifted without deliberate change (concerning; calibration is now unreliable).
- Either way, update the spec's revision date to match current standards.

### Step 6 — Update artifacts

Produce the concrete changes:

- **Spec additions.** Observable criteria added in response to spec gaps. Rewrite as must-pass / should-pass / nice-to-have per the spec format.
- **Spec removals.** Criteria the calibration revealed as non-load-bearing — intuition and spec disagree consistently and intuition is right. Rare but possible.
- **Watch list.** Biases in intuition the user is now aware of. ("I systematically overrate fluent outputs." "I systematically underrate short outputs even when they meet the spec.")
- **Next practice.** What to run next to continue calibration — usually another calibrated-comparison pass in 4–6 weeks on a fresh batch.

### Step 7 — Cross-check against workflow drag

A calibration pass often surfaces axis drag the user hadn't noticed. If the intuition gaps concentrate on outputs from one step of a larger workflow, consider running `taskdifficulty_workflow_axis_optimizer.md` on that workflow — the issue may be upstream.

### Step 8 — Close the loop

At the end of the calibration session, the user should leave with:
1. A updated spec.
2. A watch list of known intuition biases.
3. A retest date.
4. One concrete change to how they accept outputs going forward.

Without item 4, the calibration is an intellectual exercise. The test of calibration is whether the next real-world output is judged differently than it would have been without the session.

---

## Constraints

### Must
- Run on 10–20 outputs minimum.
- Require an existing spec.
- Blind the outputs before intuition scoring.
- Score spec and intuition independently, not sequentially on the same output.
- Diagnose every spec-vs-intuition disagreement; don't wave them off.
- Produce a concrete change to how outputs are accepted going forward.

### Must Not
- Be run on a task without a spec.
- Be run on <10 outputs.
- Let spec or intuition "win" by default. Each divergence is a question, not a verdict.
- Weaken the spec to match intuition when intuition gap is really a bias.
- Treat the session as complete without a watch list and a retest date.
- Use this prompt to replace a spec — calibration refines a spec, it doesn't substitute for one.

---

## False-Positive Prevention

1. **Scoring order contamination.** If the user scores spec first, then intuition, the intuition score inherits the spec score. Blinding the order is not optional.
2. **"Good fluency" bias.** Outputs that read smoothly score high on intuition and often fail on spec. Watch for this pattern — it's the single most common intuition gap.
3. **Familiarity bias.** Outputs matching patterns the user has accepted before score higher on intuition regardless of whether the pattern is good. If the user can't explain why it feels right except "it looks like the ones I usually keep," the intuition is pattern-matching, not judging.
4. **Weakening the spec on taste.** When intuition and spec disagree and intuition "really wants" to win, the temptation is to soften the spec. Only soften on specific, observable, defended grounds.
5. **Over-adding to the spec.** Every spec gap identified gets scrutiny — is this really a criterion, or is it once-off taste? A spec bloated with one-off criteria overfits to the calibration set and underperforms on new outputs.
6. **Not blinding sufficiently.** A user who kind-of remembers which outputs were accepted isn't truly blind. Either use longer delays, use a second person, or accept that the calibration is partial.
7. **Running once and stopping.** Calibration is recurring work. One pass gives a snapshot; ongoing calibration gives direction.
8. **Using this when the real problem is the spec is too loose.** If every intuition score disagrees with the spec, the spec isn't tight enough; fix the spec first and re-run calibration after.
9. **Spec-as-goal.** The spec is a tool; matching intuition to spec is not an end in itself. The end is reliable, shippable output.

---

## Output Format

```markdown
## Task type
[Named.]

## Spec in use
[Reference.]

## Blind set
- Outputs scored: [N] (floor: 10)
- Blinding method: [second person / time delay / other]

## Scoring

| # | Spec (% must-pass / avg should-pass) | Intuition (1–5) | Past decision | Divergence type |
|---|---|---|---|---|
| 1 | ... | ... | accepted / rejected | spec gap / intuition gap / aligned / time drift |
| ... | | | | |

## Correlation
- Spec-vs-intuition correlation: [strong / moderate / weak]
- Divergence concentration: [per-criterion or per-case notes]

## Diagnosed gaps

### Spec gaps (intuition caught something spec missed)
- [Criterion] — [evidence] — [add as must / should / nice-to-have]

### Intuition gaps (intuition missed something spec caught)
- [Bias] — [evidence] — [watch-list entry]

### Time drift
- [Standards change since past decisions] — [note + spec revision date update]

## Updated spec (diff)
- Added: [...]
- Removed: [...]
- Reranked: [...]

## Watch list
- [Bias] — [how to notice it next time]

## One concrete change to how outputs are accepted going forward
[Specific rule. E.g.: "Require the must-pass list to clear before deciding whether it 'feels' right."]

## Retest
- Next calibration pass on [date], fresh batch of N outputs.

## Possible upstream issue
[If intuition gaps concentrate on one workflow step, recommend running
taskdifficulty_workflow_axis_optimizer.md on that workflow.]
```

---

## Verification

- [ ] 10–20 outputs scored.
- [ ] Outputs blinded before intuition scoring.
- [ ] Spec scored independently from intuition (no order contamination).
- [ ] Every spec-vs-intuition divergence diagnosed (spec gap / intuition gap / time drift).
- [ ] Spec changes (if any) are observable and defended, not taste-weighted.
- [ ] Watch list of intuition biases is produced.
- [ ] One concrete change to how outputs are accepted going forward is named.
- [ ] Retest date set.
