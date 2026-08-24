---
title: "Diagnose Which Motivation Driver Is Missing"
category: personal-development/resilience
description: "When motivation has dropped, classify which of four drivers — clarity, energy, reward, or identity — is actually missing, using a bounded taxonomy, so the user applies the matching fix instead of generic 'just be disciplined' advice."
techniques:
  - ST-01
  - ST-02
  - AG-11
  - DS-06
  - QA-12
  - QA-20
difficulty: intermediate
tags:
  - resilience
  - motivation
  - diagnosis
  - drivers
  - taxonomy
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/resilience/resilience_self_discipline_system.md
  - domain-personal-development/prompts/resilience/resilience_momentum_rebuild.md
  - domain-personal-development/prompts/agency/agency_burnout_recovery.md
  - domain-personal-development/prompts/identity/identity_purpose_reignition.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
---

# Diagnose Which Motivation Driver Is Missing

**Objective:** When the user reports low motivation, identify which single driver is missing from a fixed four-part taxonomy — **clarity, energy, reward, identity** — and prescribe the matching restoration move. Refuse to give generic motivation advice; each missing driver has a different answer.

> **Boundary — non-clinical self-direction.** Low motivation has many ordinary causes this prompt can help with. It is **not** a diagnostic tool for depression or any clinical condition. Pervasive loss of motivation across *all* domains for weeks, accompanied by anhedonia (nothing feels good), hopelessness, or self-harm thoughts, is outside scope — route to a licensed professional or `domain-psychology/`. In the US, call or text 988. "Find your why" is not a treatment for depression.

## When to Use

- Use when: the user wants to do a specific thing (or knows they should) but the drive isn't there.
- Use when: "I just need more discipline" hasn't worked, which usually means the missing piece isn't discipline.
- Use when: motivation is selectively absent — present in some areas, gone in this one.
- **Don't use when:** the issue is exhaustion across the board with rest-non-responsiveness — that is burnout (use `agency_burnout_recovery.md`).
- **Don't use when:** the user already knows the driver and wants a system — go straight to `resilience_self_discipline_system.md`.
- **Don't use when:** motivation is absent everywhere with anhedonia (see boundary) — refuse and refer.

## Inputs / Context

1. **The specific thing** the user is unmotivated to do. One sentence.
2. **When motivation was last present** for this, and what changed since.
3. **Whether the user can clearly state what "done" looks like** for it.
4. **Energy state** — physical: sleep, recent rest, illness, baseline tiredness.
5. **What the user expects to get** from doing it, and whether that payoff still feels real.
6. **Whether the work still fits who the user is/wants to be**, or feels like someone else's task.

**Refusal logic:** If inputs (3)–(6) are missing, ask — the four drivers map directly onto those four inputs, and guessing produces the generic advice this prompt exists to avoid. If motivation is absent across all domains with anhedonia (input 5 plus a global pattern), output the boundary referral and stop.

## Instructions

### Step 1 — Classify the missing driver (exactly one)

Map the inputs onto this bounded taxonomy. Pick the single driver most clearly absent. If two seem missing, pick the one **earliest in the chain** (clarity precedes reward; energy precedes everything).

| Driver | Maps to input | Signature when missing | Restoration move |
|---|---|---|---|
| **Clarity** | (3) Undefined "done" | Can't picture the finished state or the next step; vagueness creates friction. | Spec the outcome and the very next action; see `agency_stuck_diagnosis.md` (undefined-outcome). |
| **Energy** | (4) Depleted | Wants to and knows how, but the tank is empty; rest helps. | Physiological repair first — sleep, food, movement. Motivation tactics on an empty tank fail. |
| **Reward** | (5) Payoff feels unreal/distant | The expected return has gone abstract, delayed, or stopped feeling earned. | Shorten the feedback loop; make a near-term, visible payoff; see `resilience_self_discipline_system.md`. |
| **Identity** | (6) Misfit | The task feels like it belongs to a role the user has outgrown or never owned. | This isn't a motivation problem; run `identity_purpose_reignition.md` / `identity_values_clarification.md`. |

Do not add drivers. If none fit, say so and ask for clarification.

### Step 2 — Justify with the user's own words

Quote or paraphrase the input that pinned the diagnosis. If a second driver is plausible, name it and say why it ranked second.

### Step 3 — Deliver the matching restoration move

- The move must fight the diagnosed driver specifically. Clarity gets a spec move, never a reward move. Energy gets rest, never a willpower tactic.
- Keep it small and concrete (one session or one bounded action).

### Step 4 — Name the mismatch trap

State the most common wrong fix for the diagnosed driver, so the user doesn't reach for it:
- Missing clarity → "try to push harder" (pushing into fog burns energy, fixes nothing).
- Missing energy → "build a better system" (a system on no fuel still doesn't run).
- Missing reward → "remind yourself of your goals" (the goal isn't the problem; the loop is too long).
- Missing identity → "more discipline" (discipline toward the wrong thing manufactures resentment).

### Step 5 — Verify by prediction

State what changes if the diagnosis is right (e.g., for energy: "after two nights of real sleep, the resistance drops noticeably even before any system is built"). If the predicted change doesn't appear, the driver was likely misidentified — re-run.

## Constraints

**Must:**
- Pick exactly one driver from the four-part taxonomy.
- Ground the pick in a specific input.
- Prescribe one restoration move matched to that driver.
- Name the mismatch trap for the diagnosed driver.
- State a verifiable prediction.
- Honor the clinical boundary.

**Must Not:**
- Give generic motivation advice ("set a goal," "visualize success," "just start").
- Present all four drivers as a menu — the prompt picks one.
- Treat "energy" missing as a discipline failure.
- Diagnose depression or any clinical condition.
- Add drivers to the taxonomy.

## False-Positive Prevention

1. **Don't default to "reward."** It's the satisfying diagnosis ("I just need to remember the payoff"), but if "done" is undefined, the real driver is clarity — fix that first.
2. **Don't miss "energy" hiding as "identity."** A depleted person often concludes "this work isn't for me," when two nights of sleep would restore the drive. Check input 4 before concluding misfit.
3. **Don't call selective low motivation a clinical signal.** Motivation present elsewhere but gone for one task is a driver problem, not depression. Refer only on the global-plus-anhedonia pattern.
4. **Don't stack moves.** One driver, one move. If clarity and reward both seem off, fix clarity, then re-run.
5. **Don't moralize.** Low motivation is a signal about a missing input, not a character defect. No "you need to want it more."

## Expected Output

A short diagnosis with: the missing driver, a one-line justification grounded in inputs, the matching restoration move, the named mismatch trap, and a prediction.

### Example Output

```
## Motivation diagnosis
**Missing driver:** Reward
**Justification:** You said the project still matters "in theory" but "I won't see anything from it for six months, so it feels pointless to work on today." The goal is intact; the payoff loop is too long to pull behavior.
**Second candidate:** Clarity (ranked second — you can state what "done" looks like, so clarity isn't the primary gap).

## Restoration move
Carve out a sub-deliverable you can finish and see this week — e.g., ship the landing-page copy and put it somewhere visible. Pair it with a tiny visible marker of progress (a checklist you cross off). The point is a near-term, real payoff, not a reminder of the distant one.

## Mismatch trap to avoid
Re-reading your goals or vision board. The goal isn't the problem — the six-month gap is. Restating the goal makes the gap feel worse, not better.

## Prediction
If reward is the right driver, finishing one visible sub-deliverable this week should noticeably reduce the "pointless" feeling. If it doesn't move at all, the driver may actually be identity (the work fits a role you've outgrown) — re-run with input 6 in focus.
```

## Verification

- [ ] Exactly one driver chosen from {clarity, energy, reward, identity}.
- [ ] Justification cites a specific input.
- [ ] Earliest-in-chain rule applied when two drivers compete.
- [ ] Restoration move matches the driver (no cross-application).
- [ ] Mismatch trap named.
- [ ] Verifiable prediction stated.
- [ ] "Energy missing" was considered and not relabeled as discipline.
- [ ] Clinical boundary honored; referral issued if the global-anhedonia pattern is present.

## Techniques Used

- **ST-01 (Clear Objective Statement):** Constrains output to one missing driver and one matched move, refusing generic motivation talk.
- **ST-02 (Structured Sequential Instructions):** Classify → justify → prescribe → name-trap → predict, in fixed order.
- **AG-11 (Taxonomy-Based Classification Systems):** The four-driver taxonomy forces a single, bounded diagnosis instead of an undifferentiated "low motivation."
- **DS-06 (Prioritization and Severity Guidance):** The earliest-in-chain rule prioritizes which driver to fix when several look absent.
- **QA-12 (False Positives Identification):** Guards the common misreads — reward-by-default, energy-disguised-as-identity, selective-low-motivation-as-clinical.
- **QA-20 (Dual-Failure Quality Test):** Weighs harmful failure (moralizing, missing depression) against unhelpful failure (over-referring ordinary, selective demotivation).

## Related Prompts

- [resilience_self_discipline_system.md](resilience_self_discipline_system.md) — Once the driver is "reward" or the user wants structure independent of mood.
- [resilience_momentum_rebuild.md](resilience_momentum_rebuild.md) — When low motivation has already produced a long stall.
- [agency_burnout_recovery.md](../agency/agency_burnout_recovery.md) — When the missing driver is global "energy" and rest isn't restoring it.
- [identity_purpose_reignition.md](../identity/identity_purpose_reignition.md) — When the diagnosis is "identity" (misfit).
- [agency_stuck_diagnosis.md](../agency/agency_stuck_diagnosis.md) — When the diagnosis is "clarity" (undefined outcome / first step).
