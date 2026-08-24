---
title: "Structured Recovery After a Concrete Setback"
category: personal-development/resilience
description: "After a specific setback or failure, run a bounded recovery sequence — stabilize, contain the damage, extract the controllable cause, and define one re-entry action — instead of either spiraling or rushing back in pretending nothing happened."
techniques:
  - ST-01
  - ST-02
  - RT-09
  - DS-06
  - QA-12
  - QA-20
difficulty: intermediate
tags:
  - resilience
  - setback
  - recovery
  - failure
  - re-entry
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/resilience/resilience_failure_reframe.md
  - domain-personal-development/prompts/resilience/resilience_momentum_rebuild.md
  - domain-personal-development/prompts/agency/agency_decision_post_mortem.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/identity/identity_self_talk_audit.md
---

# Structured Recovery After a Concrete Setback

**Objective:** Take a single named setback and walk the user through a four-stage recovery sequence — stabilize, contain, attribute, re-enter — producing one concrete re-entry action rather than a motivational pep talk.

> **Boundary — non-clinical self-direction.** This prompt is a structured recovery aid for ordinary setbacks (a failed launch, a rejection, a blown deadline, a lost client, a bad review). It is **not** therapy or crisis support. If the setback is accompanied by persistent hopelessness, depression, panic, an inability to function for more than a couple of weeks, or any thought of self-harm, stop and route to a licensed professional or `domain-psychology/`. In the US, call or text 988. Recovery framing does not substitute for clinical care.

## When to Use

- Use when: a specific, identifiable thing went wrong recently and the user is between the event and getting back to work.
- Use when: the user is oscillating between rumination ("I keep replaying it") and avoidance ("I can't look at it").
- Use when: the user wants to return to the work without either denying the setback or being paralyzed by it.
- **Don't use when:** the setback is diffuse and chronic with no single event — that is closer to burnout (use `agency_burnout_recovery.md`) or a stall (use `resilience_momentum_rebuild.md`).
- **Don't use when:** the user mainly needs to decide whether a past *choice* was correct — use `agency_decision_post_mortem.md` for regret analysis.
- **Don't use when:** the signals are clinical (see boundary note) — refuse and refer.

## Inputs / Context

1. **The setback, in one or two sentences.** What concretely happened and when.
2. **Current state, in the user's words.** Verbatim. "I feel humiliated" recovers differently than "I'm just angry at the client."
3. **What is actually at stake now.** The real downstream consequence (financial, reputational, relational, or none beyond feeling bad).
4. **What is still standing.** Assets, relationships, skills, or work that the setback did *not* destroy.
5. **What the user has done since.** Avoided it / over-worked it / talked to someone / nothing.

**Refusal logic:** If inputs (2) and (3) are missing, ask for them before proceeding — recovery depth depends on knowing the real stakes versus the felt stakes. If input (2) describes pervasive hopelessness or self-harm, do not run the framework; output the boundary referral and stop.

## Instructions

### Step 1 — Stabilize (separate signal from heat)

- Reflect the user's verbatim state back, then name the **felt stakes** (input 2) and the **actual stakes** (input 3) side by side.
- Do not minimize the feeling. Do not amplify it either. State the gap between felt and actual stakes plainly if one exists.
- Output one stabilizing fact drawn from input 4 (what is still standing) — grounded in their evidence, not a platitude.

### Step 2 — Contain the damage

- Identify whether the damage is **bounded** (already done, finite) or **still spreading** (ongoing — e.g., a relationship deteriorating, money still bleeding).
- If still spreading: the first move is a containment action *today*, before any reflection. Name it.
- If bounded: state that explicitly so the user stops bracing for more.

### Step 3 — Attribute the cause across a fixed split

Classify the controllable share of the cause. Use this bounded split:

| Share | Meaning | What it implies for recovery |
|---|---|---|
| **Controllable** | A decision or action the user owns and could repeat or change. | This is the learnable part. Carry it forward. |
| **Influenceable** | Partly the user's, partly external (timing, other people, conditions). | Note the lever; don't over-own it. |
| **Uncontrollable** | Luck, market, others' choices, randomness. | Release it. Owning this part is where rumination lives. |

Assign a rough percentage to each. **The controllable share is the only part that becomes a lesson** — extract one specific, behavioral lesson from it (defer deep reframing to `resilience_failure_reframe.md`).

### Step 4 — Define re-entry

- Produce **exactly one** re-entry action: small, specific, doable within 48 hours, and chosen so that completing it re-establishes contact with the work.
- The re-entry action is not "fix everything." It is the smallest motion that proves the user is back in the arena.

### Step 5 — Verify by prediction

State what should be observable 48 hours after the re-entry action if recovery is on track (e.g., "the user has touched the work once without the dread that input 2 described"). If the prediction fails, the likely cause is unfinished Step 1 (still in heat) or miscounted stakes — re-run.

## Constraints

**Must:**
- Distinguish felt stakes from actual stakes using the user's inputs.
- Split the cause into controllable / influenceable / uncontrollable before extracting any lesson.
- Produce exactly one re-entry action, bounded to 48 hours.
- State a verifiable prediction.
- Honor the clinical boundary and refuse-and-refer when triggered.

**Must Not:**
- Offer reassurance unconnected to the user's evidence ("you've got this," "everything happens for a reason").
- Extract lessons from the uncontrollable share — that manufactures false guilt.
- Prescribe a multi-week recovery plan; this prompt covers stabilize-to-re-entry only.
- Diagnose any mental health condition.

## False-Positive Prevention

1. **Don't label the whole setback "controllable."** Self-blame feels like accountability but corrupts the attribution. Force a genuine three-way split; if the user assigns 100% to themselves, push back.
2. **Don't label the whole setback "uncontrollable."** That feels like absolution but blocks learning. If the user assigns 0% to themselves, probe the decisions that led in.
3. **Don't skip containment when damage is still spreading.** Reflection on a still-bleeding wound is premature; the body keeps bracing. Stop the bleed first.
4. **Don't confuse a strong emotional reaction with a clinical signal.** Acute disappointment, embarrassment, or anger after a real setback is normal and recoverable. Refer only on the specific signals in the boundary note (persistence, hopelessness, self-harm, prolonged non-function).
5. **Don't let the re-entry action be a disguised "fix it all" plan.** If it can't be done in 48 hours, it's too big — shrink it.

## Expected Output

A short report with five labeled sections: stabilization, damage containment, cause attribution (with the three-way split and percentages), one lesson from the controllable share, one re-entry action, and a 48-hour prediction.

### Example Output

```
## Stabilization
You said you feel "completely humiliated" after the demo crashed in front of the client.
- Felt stakes: career-ending embarrassment, the client thinks you're incompetent.
- Actual stakes (from your input): one client, mid-size contract, relationship of 8 months, not yet cancelled.
- Still standing: the product works in every other environment; the client agreed to a reschedule.
The gap between "career-ending" and "one rescheduled demo with an 8-month relationship intact" is large. That gap is where the heat is.

## Damage containment
Bounded. The crash already happened; the demo is rescheduled. Nothing is actively getting worse.
You do not need to brace for further fallout — there is no second shoe.

## Cause attribution
- Controllable (~40%): you demoed on the office wifi without a tested offline fallback.
- Influenceable (~20%): the client moved the demo up two days, compressing your prep.
- Uncontrollable (~40%): the venue's network dropped mid-call.
Lesson (controllable only): always run a tested offline fallback for any live demo. That is the single carry-forward behavior.

## Re-entry action (next 48 hours)
Send the client a two-line reschedule confirmation and record a 3-minute backup demo video as your fallback. Done = video exists.

## Prediction
Within 48 hours you'll have touched this work once (the video) without the "can't look at it" reaction. If you still can't open the file, you're still in Step 1 heat — re-run before pushing on re-entry.
```

## Verification

- [ ] The setback is a single named event, not a diffuse condition.
- [ ] Felt stakes and actual stakes are stated separately.
- [ ] Damage is classified bounded vs. spreading; containment came first if spreading.
- [ ] Cause is split three ways with rough percentages summing to ~100%.
- [ ] The lesson is drawn only from the controllable share and is behavioral.
- [ ] Exactly one re-entry action, bounded to 48 hours.
- [ ] A 48-hour observable prediction is stated.
- [ ] Clinical boundary honored; referral issued if triggered.

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the goal to one named setback and a single re-entry action, blocking scope creep into life-coaching.
- **ST-02 (Structured Sequential Instructions):** The stabilize → contain → attribute → re-enter sequence enforces order (you can't learn from a wound that's still bleeding).
- **RT-09 (Root Cause Explanation Pattern):** Step 3 traces the setback to its causes before prescribing the carry-forward behavior.
- **DS-06 (Prioritization and Severity Guidance):** Felt-vs-actual stakes and the controllable/uncontrollable split prioritize where attention and learning should go.
- **QA-12 (False Positives Identification):** False-positive rules guard against the two attribution traps (100% self-blame, 0% self-blame) and against misreading normal acute distress as clinical.
- **QA-20 (Dual-Failure Quality Test):** Balances the harmful failure (toxic positivity, false guilt) against the unhelpful failure (over-referring normal disappointment to a professional).

## Related Prompts

- [resilience_failure_reframe.md](resilience_failure_reframe.md) — Deeper signal extraction from the failure once the user has stabilized.
- [resilience_momentum_rebuild.md](resilience_momentum_rebuild.md) — When the setback turned into a multi-week stall.
- [agency_decision_post_mortem.md](../agency/agency_decision_post_mortem.md) — When the question is whether the underlying *decision* was right.
- [agency_stuck_diagnosis.md](../agency/agency_stuck_diagnosis.md) — If re-entry doesn't take and the user is now stuck.
- [identity_self_talk_audit.md](../identity/identity_self_talk_audit.md) — If the heat in Step 1 is driven by a harsh inner-critic script.
