---
title: "Design a Habit From the Identity It Votes For, Not the Outcome It Chases"
category: personal-development/habits
description: "Take an identity the user wants to become ('someone who X') and design the smallest repeatable behavior that counts as a vote for it, so each rep is evidence of the identity rather than a step toward a distant outcome."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - RT-02
  - QA-12
difficulty: intermediate
tags:
  - habits
  - identity-based-habits
  - behavior-change
  - evidence
  - self-concept
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/habits/habits_habit_design_blueprint.md
  - domain-personal-development/prompts/habits/habits_implementation_intention_builder.md
  - domain-personal-development/prompts/habits/habits_environment_design_for_habits.md
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-personal-development/prompts/agency/agency_habit_loop_repair.md
---

# Design a Habit From the Identity It Votes For, Not the Outcome It Chases

**Objective:** Convert an identity the user wants ("become someone who X") into the single smallest behavior that counts as a vote for that identity, sized so each rep reads as concrete evidence of who they are — not as a down payment on a far-off result.

**When to use:** The user says they want to *be* a certain kind of person (a writer, a healthy person, someone reliable) but keeps chasing outcomes (a book deal, a weight, a promotion) and stalling. Use when a prior outcome-based attempt died once the outcome felt distant. Not for this: designing the full cue-routine-reward loop mechanics — once the identity vote is chosen, hand off to `habits_habit_design_blueprint.md`.

**Audience:** An individual doing this for themselves. Not for assessing someone else, not clinical. If the identity work surfaces persistent self-worth distress or shame that outlasts the session, this is not a substitute for professional support — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **The desired identity.** Stated as "I want to become someone who ___," in the user's words. Not an outcome ("lose 20 lbs") — an identity ("someone who moves their body daily").
2. **The outcome they've been chasing instead.** The result they were tracking, and roughly how far away it feels.
3. **Two or three past behaviors** that already point — even weakly — toward this identity. What have they done, even once, that a person with this identity would do?
4. **Their honest daily rhythm.** Wake, work, wind-down, and where the reliable anchors and dead time are.
5. **The worst realistic day.** Sick, slammed, low mood — what a bad day looks like.

If the user gives only an outcome and cannot name an identity behind it, do not invent one. Ask: "Who would you have to be for that outcome to be inevitable?" If they still can't, route to `identity_values_clarification.md` first — you cannot vote for an identity that hasn't been named.

---

## Instructions

### Step 1 — Separate the identity from the outcome

Restate input 1 as an identity and input 2 as an outcome, side by side. Confirm they are different in kind: an identity is a repeated way of acting ("someone who writes"); an outcome is a result that either happens or doesn't ("a finished novel"). If the user's "identity" is actually a disguised outcome, name that and rewrite it as a behavior-based identity.

### Step 2 — Classify candidate behaviors by vote strength

Take input 3 and any behaviors the identity implies. Score each against this fixed taxonomy:

| Vote type | Definition | Keep? |
|---|---|---|
| **Evidence-generating** | Doing it *is* the identity in miniature; a witness would say "that's what an X does." | Yes — this is the target. |
| **Symbolic** | Signals the identity without enacting it (buying gear, joining a group, posting about it). | No — feels like progress, produces no evidence. |
| **Contradicting** | A behavior that quietly votes *against* the identity. | Name it as a leak, don't design it. |

Only evidence-generating behaviors qualify as an identity vote.

### Step 3 — Shrink the vote to a floor that survives the worst day

Pick one evidence-generating behavior and reduce it until the floor version would still run on input 5's worst day. The rule: the vote must be small enough to be *undeniable*, so the user never gets to argue "that didn't really count." "Write one sentence" beats "write 500 words" because it survives and still casts a vote for *writer*.

### Step 4 — Make the rep read as evidence

Specify how the user registers the vote so it lands as identity evidence, not chore completion. Convert the tracking language from "task done" to "that's who I am": the mark says "cast a vote for [identity]," not "did the thing." Name the exact anchor the vote attaches to (a preceding action from input 4). Do not recommend an app.

### Step 5 — Produce one identity vote

Output a single sentence in the fixed form, plus the evidence reframe:

> **"I am someone who [identity]. Today's vote: [floor behavior] after [anchor]."**

Then one line naming the most likely contradicting behavior (the leak) and whether to leave it alone or add friction (route to `habits_environment_design_for_habits.md` if friction is needed). One vote, not a slate.

---

## Constraints

### Must
- Restate the identity and the outcome as distinct kinds, and design only for the identity.
- Classify every candidate behavior as evidence-generating, symbolic, or contradicting.
- Design exactly one evidence-generating vote, floor-sized against the worst day.
- Reframe the tracking mark as identity evidence, anchored to a real preceding action.
- Name the most likely contradicting behavior.

### Must Not
- Design a symbolic behavior (gear, membership, announcement) as the vote.
- Reintroduce the outcome as the thing being tracked.
- Design more than one identity or vote per run.
- Moralize, congratulate, or cheerlead the user's chosen identity.
- Recommend affirmations, mantras, or "act as if" as the mechanism — the mechanism is repeated evidence, not repeated self-talk.
- Provide clinical framing; route persistent self-worth distress to `domain-psychology/`.

---

## False-Positive Prevention

1. **Don't accept a disguised outcome as an identity.** "Someone who is fit" collapses into a result. Push until the identity is a repeated action ("someone who trains").
2. **Don't count symbolic behavior as a vote.** Buying running shoes votes for nobody. Only enactment generates evidence.
3. **Don't approve an aspirational floor.** If the vote is "write 1,000 words," it will fail on a bad day and cast a vote *against* the identity. Shrink until undeniable.
4. **Don't confuse wanting the label with wanting the behavior.** If the user wants to be *called* a writer more than they want to write, name it — borrowed identities produce no reps. This is where `identity_values_clarification.md` belongs.
5. **Don't ignore the contradicting behavior.** A daily vote *for* plus a daily vote *against* nets to zero; the leak must at least be named.
6. **Don't stack identities.** Voting for three identities at once dilutes the evidence for each. One.

---

## Output Format

```
## Identity vs. outcome
- Identity (design for this): I am someone who [identity].
- Outcome (do not track): [outcome], ~[distance].
- [If the identity was a disguised outcome, note the rewrite.]

## Candidate behaviors (vote strength)
| Behavior | Vote type | Keep? |
|---|---|---|
| ... | Evidence / Symbolic / Contradicting | ... |

## The vote (this is the habit)
Floor behavior: [smallest undeniable version]
Anchor: [preceding action from daily rhythm]
Worst-day check: on a [worst-day] day this still runs because [reason].

## The identity sentence
"I am someone who [identity]. Today's vote: [floor behavior] after [anchor]."

## Evidence reframe (tracking)
Mark says: "cast a vote for [identity]" — not "task done." No app.

## The leak
Most likely contradicting behavior: [...]. Action: [leave / add friction → habits_environment_design_for_habits.md].

Next action (today): cast the first vote — [floor behavior] after [anchor].
Predicted check: after 7 days, the user can point to 5+ concrete reps as evidence of [identity], with no reference to the outcome.
```

---

## Verification

- [ ] The identity and the outcome are restated as distinct kinds; the design targets only the identity.
- [ ] Every candidate behavior is classified evidence-generating / symbolic / contradicting.
- [ ] Exactly one evidence-generating vote is designed, floor-sized and worst-day-tested.
- [ ] The tracking mark is reframed as identity evidence and anchored to a real preceding action.
- [ ] The most likely contradicting behavior is named.
- [ ] No symbolic behavior, no outcome-tracking, no affirmation mechanism, no stacked identities.
- [ ] No moralizing, no clinical interpretation.
