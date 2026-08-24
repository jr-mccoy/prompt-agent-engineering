---
title: "Apply Two or Three Fitting Mental Models to a Problem You're Facing"
category: personal-development/thinking
description: "Take one specific problem the user is stuck on, select the 2–3 mental models that genuinely fit its structure (not a grab-bag), run the problem through each to generate a non-obvious angle, and converge on the single insight that changes the user's next move."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - RT-05
  - QA-12
difficulty: intermediate
tags:
  - mental-models
  - problem-solving
  - reframing
  - decision
  - non-obvious
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/thinking/thinking_fresh_perspective_generator.md
  - domain-personal-development/prompts/thinking/thinking_blind_spot_mirror_see_what_im_missing.md
  - domain-personal-development/prompts/thinking/thinking_interrogative_mode.md
  - domain-reasoning-craft/reasoning-moves/reasoning_first_principles_reconstruction.md
  - domain-reasoning-craft/systems/systems_leverage_point_analysis.md
---

# Apply Two or Three Fitting Mental Models to a Problem You're Facing

**Objective:** Run one real problem through the 2–3 mental models that actually fit its structure, surface the non-obvious angle each produces, and hand back the single insight that changes the user's next concrete move.

**When to use:** The user is stuck on a specific decision or problem and keeps circling the same framing; they suspect they're missing an angle; or they want more than one lens on a call before committing. Not for vague dissatisfaction with no defined problem (route to `../identity/` or `agency_stuck_diagnosis.md`), and not for learning mental models in the abstract — this applies them to one live case.

**Audience:** An individual thinking through their own problem. Not for analyzing another person, not clinical. If the "problem" is persistent distress rather than a solvable situation, this is the wrong tool — see `domain-psychology/` and professional support.

---

## Inputs Required

1. **The problem, stated concretely.** One specific situation the user is trying to move on — a decision, a stuck project, a recurring failure, a tradeoff. Not a topic ("my career") but a call ("whether to shut down the side project I've spent 8 months on").
2. **What the user has already considered.** Their current framing and the options they've already weighed. Required so the output can be non-obvious *relative to what they've already thought*.
3. **The constraint that makes it hard.** What actually makes this a problem — scarce time, money, information, a relationship, a deadline, sunk cost. One or two real constraints.
4. **What "solved" would look like.** The observable state the user is trying to reach. If they can't name it, that gap is itself a finding.

If the problem is a topic rather than a specific stuck situation, refuse and ask the user to narrow to one concrete call. Mental models applied to a vague topic produce vague platitudes.

---

## Instructions

### Step 1 — Diagnose the problem's structure

Before choosing any model, classify what *kind* of problem this is, from a fixed taxonomy. This is what makes model selection non-arbitrary.

| Structure | Signature | Models that fit |
|---|---|---|
| Sunk-cost / continue-vs-quit | Past investment is driving a forward choice | Opportunity cost, sunk-cost fallacy, second-order thinking |
| Hidden constraint / bottleneck | One factor gates everything else | Theory of constraints / leverage points, 80-20, bottleneck analysis |
| Over-complex / tangled | Too many moving parts, no clear cause | First principles, inversion, Occam's razor |
| Risk / irreversibility | Downside is large or one-way | Margin of safety, expected value, reversible-vs-irreversible |
| Competing / others involved | Outcome depends on others' choices | Incentives ("show me the incentive"), game theory, comparative advantage |
| Prediction / uncertainty | Depends on how the future breaks | Base rates, probabilistic thinking, scenario planning |

Pick the row that best fits inputs 1 and 3. It's fine if two rows apply — that's where the model set comes from.

### Step 2 — Select 2–3 fitting models, and name what you rejected

Choose 2–3 models from the fitting row(s). State in one line why each fits *this* problem's structure. Then name at least one model you deliberately did **not** use and why it doesn't fit — this proves the selection is structural, not a grab-bag. More than three models produces noise, not insight.

### Step 3 — Run the problem through each model

For each selected model, produce:
- **The lens in one line** (what the model asks you to look at).
- **The non-obvious angle** it generates for *this* problem — something not already in input 2.
- **What it implies about the constraint** from input 3.

If a model, honestly applied, produces nothing the user hasn't already thought, say so and drop it. A model that only restates the obvious is a false positive.

### Step 4 — Compare what the models say

Lay the angles side by side. Do they agree, point in different directions, or expose a tension? The comparison is where the real insight usually lives — often two models disagree, and the disagreement names the actual crux of the decision.

### Step 5 — Converge on the one insight

Select the single angle that most changes the user's next move — highest leverage on the constraint, most at odds with their current framing (input 2). Not a summary of all three; one insight, stated as a sentence the user could not have written before this exercise.

### Step 6 — Convert to one next move

Translate the insight into one concrete, bounded action that tests or acts on it this week. Physical and observable — a conversation, a calculation, a cut, a small reversible bet — not "think about it through this lens."

---

## Constraints

### Must
- Classify the problem's structure from the fixed taxonomy before selecting models.
- Select 2–3 models and justify each against the problem's structure.
- Name at least one deliberately-rejected model and why it doesn't fit.
- Produce a genuinely non-obvious angle per model, relative to input 2, or drop the model.
- Converge on exactly one insight and one bounded next move.

### Must Not
- List more than three models, or offer a "menu of lenses to explore."
- Apply a model whose output merely restates the user's existing framing.
- Use models as decoration — every model must change something about the analysis.
- Give generic model definitions the user could get from a glossary; apply them to the live case.
- Command the decision or moralize about the sunk cost / choice.

---

## False-Positive Prevention

1. **Don't grab-bag models.** Applying five famous models to look thorough dilutes the signal. Fit-to-structure is the whole discipline; two well-chosen models beat six sprinkled on.
2. **Don't mistake restatement for insight.** If the "non-obvious angle" is something the user already said in input 2, it's not an angle — drop it rather than dress it up.
3. **Don't force a model onto the wrong structure.** Opportunity cost on a pure risk-of-ruin problem, or expected value on an irreversible one-way door, gives confidently wrong guidance. Match the taxonomy.
4. **Don't let a famous model override the user's real constraint.** The angle must engage input 3's actual constraint, not the constraint the model is usually taught with.
5. **Don't converge on the comfortable insight.** The single insight should often be the one most at odds with the user's current framing; picking the reassuring one defeats the exercise.
6. **Don't confuse a thinking problem with a distress problem.** If the block is emotional rather than structural, models won't move it — say so and route out.

---

## Output Format

```
## Problem (restated)
[One-line concrete problem] | Constraint: [input 3] | Solved looks like: [input 4]

## Problem structure
[Taxonomy row] — because [signature from inputs 1 & 3]

## Models selected (2–3)
1. [Model] — fits because [structural reason]
2. [Model] — fits because ...
Rejected: [Model] — doesn't fit because [reason]

## Running the problem through each
### [Model 1]
- Lens: ...
- Non-obvious angle (vs. what you'd already considered): ...
- Implication for your constraint: ...
### [Model 2]
...

## Where the models agree / disagree
[The comparison — and the crux it exposes]

## The one insight
[A single sentence the user could not have written before this exercise.]

## Next move (this week)
[One bounded, observable action that tests or acts on the insight.]

Predicted check: after this move, [observable change in the problem or the user's read of the constraint].
```

---

## Verification

- [ ] Problem is a concrete stuck call, not a topic; refused/narrowed if it was a topic.
- [ ] Structure classified from the fixed taxonomy before model selection.
- [ ] 2–3 models selected with per-model structural justification, and ≥1 model explicitly rejected.
- [ ] Each retained model produced an angle absent from input 2; any restating model was dropped.
- [ ] The models were compared, and the crux/tension surfaced.
- [ ] Exactly one insight and one bounded, observable next move; no menu, no commanded decision.
