---
title: "Diagnose Stage of Burnout and Choose a Recovery Path"
category: personal-development/agency
description: "Differentiate depletion vs. burnout vs. boredom-burnout vs. mismatch-burnout from observed signals, and prescribe a stage-appropriate recovery — rest design, not productivity tweaks."
techniques:
  - ST-01
  - ST-02
  - AG-11
  - RT-09
  - AG-10
  - QA-12
difficulty: intermediate
tags:
  - burnout
  - recovery
  - depletion
  - rest
  - mismatch
  - agency
updated: "2026-05-08"
related_prompts:
  - domain-personal-development/prompts/solo-dev/solo_dev_burnout_prevention.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/identity/identity_purpose_reignition.md
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-personal-development/prompts/identity/identity_self_talk_audit.md
---

# Diagnose Stage of Burnout and Choose a Recovery Path

**Objective:** Classify what the user is actually experiencing — simple depletion, full burnout, boredom-burnout, or mismatch-burnout — and prescribe a stage-appropriate recovery path. Productivity tweaks are explicitly off the menu when the diagnosis is burnout; rest is the move, and the prompt names the *kind* of rest.

**When to use:** The user has been pushing for a while, output and energy have dropped, and the usual "try harder" responses aren't working. Use this *after* simple things (sleep, illness, schedule disruption) have been ruled out as the sole cause. Closes the referral gap from `agency_stuck_diagnosis.md` category 10 (legitimate depletion).

**Audience:** An individual diagnosing their own state. **This prompt is not therapy.** Burnout that includes persistent hopelessness, suicidal ideation, panic disorder symptoms, or substance dependence is out of scope — refer to professional help.

---

## Inputs Required

1. **Duration.** How long has the current low state been running? Days / weeks / months.
2. **Energy curve.** Rough description: weekday energy, weekend energy, recovery from a full day off (does it come back the next morning, or not).
3. **Cynicism check.** Does the user feel detached from / negative about the work itself? Or do they still care but can't access the energy?
4. **Output collapse vs. effort collapse.** Both, or one? Some users still produce while burning; some stop producing first.
5. **Sleep, food, movement, alcohol.** Real numbers, not aspirational. Hours of sleep, meals skipped, exercise sessions, drinks per week.
6. **Last real rest.** Last time the user took ≥ 4 consecutive days fully off (no laptop, no work-thinking). Approximate.
7. **What still feels good (if anything).** Specific activities or moments in the last 30 days that produced any positive state.
8. **One sentence: what does the user think this is?** Their own guess.

If input 7 is "nothing — I can't think of anything that has felt good in 30+ days" *and* input 1 is "weeks to months," refuse this prompt. Output: "This pattern is consistent with conditions that benefit from professional evaluation. Please contact a primary care physician or mental health professional. In the US, dial or text 988 for immediate support." Do not proceed to diagnosis.

---

## Instructions

### Step 1 — Classify into exactly one stage

| # | Stage | Defining signature | Recovery axis |
|---|---|---|---|
| 1 | **Depletion** | Real but rest-responsive. A full day or weekend restores function. < 4 weeks duration. Inputs 5–6 show real deprivation. | Sleep, food, movement, time off — *physiological repair*. |
| 2 | **Early burnout** | Weeks to a few months. Rest helps but doesn't fully restore. Effort-to-output ratio has risen sharply. Cynicism is starting. | Reduced load + protected rest blocks for 2–6 weeks. Not heroic time off; structural reduction. |
| 3 | **Full burnout** | Months running. Cynicism present. Rest no longer reliably restores function. The thought of returning to the work itself produces dread. | Extended distance from the work (weeks-to-months scale). Recovery is non-linear. May require professional support. |
| 4 | **Boredom-burnout** | Energy is fine in other domains but absent for this work. The work has become repetitive, predictable, or unstretched. Output may be stable; engagement is gone. | Not rest. Stretch, novelty, or scope change. |
| 5 | **Mismatch-burnout** | Burnout-shaped, but the underlying issue is that the work is wrong for the person now (values shifted, role drifted, environment toxic). Rest will not fix this. | Diagnostic review of fit, not recovery. See `identity_purpose_reignition.md` and `identity_values_clarification.md`. |

Pick exactly one. Justify the pick using inputs 1, 2, 3, and 6 specifically. If two stages overlap, pick the earlier-stage diagnosis and name the second as risk.

### Step 2 — Verify the diagnosis isn't really clinical

Before recommending recovery, check the inputs against the refusal trigger above. State explicitly: *"This is not [depression / anxiety disorder / panic / substance issue] — those would require a different kind of help. If any of those describe what's happening, please seek professional support."*

### Step 3 — Prescribe stage-specific recovery

Output recovery as a **specific shape**, not generic rest advice:

**Depletion (Stage 1):**
- Specific physiological move: protect 8 hours sleep × 14 nights, two real meals/day, 20 min outdoor light/morning. Drop one optional commitment this week.
- Predicted check: by day 10, weekday energy returns to ~ 80%.
- If the check fails, re-run the prompt — diagnosis may have been Stage 2.

**Early burnout (Stage 2):**
- Structural reduction: identify the 3 commitments consuming the most energy and remove or reduce *one* this week. Calendar audit (`deepwork_calendar_audit.md`) is the right second step.
- Protected rest blocks: 2 fully off-work days/week for 4 weeks, no laptop.
- Predicted check: by week 4, ability to start the work without dread; output efficiency partially restored.
- Refuse the temptation to "just push through to the deadline." Pushing through Stage 2 is the most common path to Stage 3.

**Full burnout (Stage 3):**
- Recovery is a months-scale process, not weeks. The prompt does not prescribe a heroic plan; it prescribes a posture.
- Explicit recommendation: speak to a doctor or therapist before designing the recovery. Burnout at this stage often co-occurs with conditions that need professional support.
- If continuing in current role: protected leave (1–4 weeks fully off, all work access removed). Return at reduced capacity for ≥ 60 days.
- If the work is leaving: that's a separate decision; do not make it from inside Stage 3.
- The prompt explicitly refuses to provide a 30-day recovery plan. Stage 3 recovery is not a plan; it is rest plus help plus time.

**Boredom-burnout (Stage 4):**
- Not rest. Identify one stretch dimension this week: a harder problem in the role, a new domain to learn, a scope change, or — if those aren't possible — a structural conversation about role evolution.
- If the role itself has nothing left to teach, this may be a Stage 5 dressed as Stage 4.
- See `agency_skill_gap_reframe.md` and `bottleneck_clarity_ambition_surfacer.md`.

**Mismatch-burnout (Stage 5):**
- Recovery is not the move. Diagnosis is the move.
- Run `identity_values_clarification.md` and `identity_purpose_reignition.md` before any role / project decision.
- Resist the temptation to take a sabbatical and return to the same situation; the symptoms will return.

### Step 4 — Name the trap for this stage

Each stage has a characteristic mistake. Name it:

- **Stage 1 trap:** treating depletion as burnout, taking weeks off when days were enough, returning fearful.
- **Stage 2 trap:** "I'll rest after the deadline." Pushing through is how Stage 2 becomes Stage 3.
- **Stage 3 trap:** trying to recover while still inside the situation that caused it, without professional support.
- **Stage 4 trap:** rest. Rest doesn't help boredom; it amplifies it.
- **Stage 5 trap:** treating it as Stage 2 or 3 and recovering back into a situation that will burn you again.

### Step 5 — Set a re-evaluation point

State a specific date / horizon to re-run this diagnosis. Not "keep an eye on it." A specific check-in.

---

## Constraints

### Must
- Pick exactly one stage.
- Justify the pick using specific inputs (duration, energy curve, cynicism, last real rest).
- Refuse and refer if inputs are consistent with clinical conditions outside scope.
- Prescribe stage-specific recovery — different stages get different shapes of intervention.
- Name the characteristic trap for the diagnosed stage.
- Set a specific re-evaluation point.

### Must Not
- Recommend "self-care" generically. Prescribe specific actions.
- Recommend a productivity-system overhaul as recovery for any stage. Productivity systems do not cure burnout.
- Diagnose depression, anxiety, ADHD, or any clinical condition.
- Tell the user to "push through" any stage.
- Promise that recovery will be linear or fast. Stage 3 is months.
- Add stages to the taxonomy.

---

## False-Positive Prevention

1. **Don't default to Stage 2 ("early burnout").** It's the diagnosis users hope for because it sounds manageable. If the duration is < 4 weeks and rest restores function, it's Stage 1. If duration is months and dread is present, it's Stage 3.
2. **Don't miss Stage 4.** A bored-burned-out senior IC sounds like a burned-out junior IC on the surface. The signature is energy-elsewhere-but-not-here. Stage 4 + rest = worse.
3. **Don't miss Stage 5.** Mismatch hides as burnout. Tell: rest doesn't help, the work itself doesn't fit who the user has become, values have shifted. Don't prescribe more rest.
4. **Don't escalate to Stage 3 for dramatic effect.** Stage 3 has a high recovery cost and a real risk of misdiagnosis-driven over-correction. Reserve it for months-running cynicism + dread + non-responsive rest.
5. **Don't prescribe sabbatical without role-fit diagnosis.** A sabbatical that ends with a return to the same Stage 5 situation just delays the symptoms.
6. **Don't conflate Stage 1 burnout with character weakness.** Depletion is data, not failure.

---

## Output Format

```
## Stage diagnosis
**Stage:** [1–5, name]
**Justification:** [2–3 sentences citing inputs 1, 2, 3, 6 specifically]
**Risk diagnosis (second-most-likely stage):** [stage + brief reason]

## Out-of-scope check
[Explicit statement that this is not clinical depression / anxiety / etc., and the conditions under which to escalate.]

## Recovery prescription
[Stage-specific, as detailed above. Specific actions, durations, structural changes — not generic.]

## Stage trap to avoid
[Named, one sentence.]

## Predicted check
By [date], the following should be true: [specific observable]. If not, re-run this prompt.

## Re-evaluation point
[Specific date or horizon.]
```

---

## Verification

- [ ] Exactly one stage selected.
- [ ] Justification uses input numbers (1, 2, 3, 6) specifically.
- [ ] Refusal-and-referral block triggered if clinical conditions are likely.
- [ ] Recovery prescription is stage-specific, not generic "rest more."
- [ ] Productivity-system advice is absent.
- [ ] Stage trap is named.
- [ ] Re-evaluation date/horizon is concrete.
- [ ] Stage 5 (mismatch) considered, not skipped.
