---
title: "Diagnose Procrastination as a System Failure, Not a Character Failure"
category: productivity/bottlenecks
description: "Classify procrastination on a specific task into one of six system-level causes — ambiguous next action, environment friction, decision fatigue, calendar mismatch, capture failure, or hidden dependency — and prescribe a system fix. Refuses motivation/discipline framings."
techniques:
  - ST-01
  - ST-02
  - AG-11
  - RT-09
  - OC-09
difficulty: intermediate
tags:
  - procrastination
  - bottleneck
  - systems-diagnosis
  - execution
  - friction
updated: "2026-05-08"
related_prompts:
  - domain-productivity/bottlenecks/bottleneck_locator.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
  - domain-productivity/deep-work/deepwork_environment_friction_design.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/agency/agency_planning_masquerade_detector.md
---

# Diagnose Procrastination as a System Failure, Not a Character Failure

**Objective:** Diagnose why a specific task is being procrastinated by classifying the cause into one of six system-level patterns. Each pattern has a specific system fix. The prompt explicitly **refuses to treat procrastination as a motivation, discipline, or character problem** — those framings are out of scope for productivity and route to `domain-personal-development/`.

**When to use:** A specific task has been on the list for ≥ 5 days without progress and the user can't tell why. Use *after* `bottleneck_locator.md` has identified execution as the binding lane (or in parallel for a single-task drill-down). Distinct from `agency_stuck_diagnosis.md` which is project-scoped; this is task-scoped within the productivity domain.

**Audience:** An individual diagnosing their own procrastination on a specific task. Not for diagnosing other people. Not for general "I procrastinate everything" — that's a `bottleneck_locator.md` or personal-development question.

---

## Inputs Required

1. **The specific task.** One sentence. If the user's answer is multi-task ("I procrastinate everything") or vague ("the project"), refuse and ask for the *most-procrastinated single task this week*.
2. **How long it's been on the list.** Days.
3. **What "done" looks like for this task.** One sentence. If the user can't say, that's a finding (Cause #1 likely).
4. **The next physical motion.** What is the very next thing the user would have to type, click, open, or say to start? If the user can't name a physical motion, that's also a finding.
5. **Five most recent attempts to start.** What happened — what they opened, where they got stuck, what they did instead. If "I haven't tried in a week," note that.
6. **Calendar position of the work.** Where in the week did the user *plan* to do it? Where did the planned block fall in their energy curve (morning / mid-day / late-day)?
7. **What gets done easily this week.** 2–3 tasks the user *did* complete with little friction. Often diagnostic — they reveal the system's working path.
8. **Anything explicitly waiting on someone or something else.** Be specific: what's blocked, who/what it depends on, when it was last checked.

If the user's framing of the procrastination is "I'm lazy," "I lack discipline," "I'm just unmotivated," refuse the framing and respond: *"Procrastination on a specific task is almost always a systems failure with a specific cause. This prompt diagnoses that. Motivation/discipline framings are out of scope here — if a system fix doesn't resolve it, see `agency_stuck_diagnosis.md`."* Then proceed to diagnosis.

---

## Instructions

### Step 1 — Classify into exactly one cause

Use only this taxonomy. Pick the one that fits best. If two fit, pick the one earliest in the chain.

| # | Cause | Diagnostic signal | System fix |
|---|---|---|---|
| 1 | **Ambiguous next physical action** | User can't name input 4 in physical-motion terms. The task is at "do the migration" not "open file `db.go`, run command X." | Run `agency_next_action_spec.md`. Output: a single typeable / clickable next move. Do not work on the task before this is done. |
| 2 | **Environment friction** | The first physical motion requires multiple steps before any value-producing work begins (login, find file, locate context, set up state). The friction itself is the deferral. | Run `deepwork_environment_friction_design.md`. Reduce the path-to-first-keystroke to under 30 seconds, or pre-stage state at the end of the previous session. |
| 3 | **Decision fatigue / unmade upstream decision** | Input 5 shows the user opening the work and immediately hitting a fork they don't want to make — naming, scope, approach. Procrastination is hiding a decision deferral. | Make the decision *outside* the work block, with constraints from `cm-02`. Schedule the decision before the work; the work is not on the calendar until the decision is made. |
| 4 | **Calendar mismatch** | Planned block falls in low-energy window (input 6); easy tasks (input 7) consistently happen in high-energy windows. The block is set up to fail. | Move the block to a high-energy window. If high-energy windows are saturated, the underlying issue is calendar (`deepwork_calendar_audit.md`), not this task. |
| 5 | **Capture / context failure** | The task isn't being procrastinated; the user isn't seeing it consistently in their inbox / list / calendar. They keep "forgetting" or "rediscovering" it. | The task is leaking capture/triage; run `bottleneck_capture_triage_system_design.md`. The procrastination is downstream of the capture failure. |
| 6 | **Hidden dependency** | Input 8 reveals the task is actually waiting on someone else / something else, but is sitting on the user's list as if it were theirs to start. | Move the task off the user's "do" list onto a "waiting-on" list with a trigger; nudge the dependency once. Procrastinating something that isn't yours is rational. |

If the user's case fits *none* of these patterns, that's diagnostic: the procrastination is probably not a systems-level failure on this specific task. Route to `agency_stuck_diagnosis.md`.

### Step 2 — Justify the classification

In one or two sentences, cite the specific input that tipped the diagnosis. Examples:

- "Cause #2 (environment friction). Input 5 shows three of five attempts ended at 'couldn't find the file / had to set up the env again.' The procrastination is the time cost of restarting context."
- "Cause #4 (calendar mismatch). Input 6: the work was planned at 4pm. Input 7: the easy tasks all happened in the morning. The block is set up to lose."

### Step 3 — Run the corresponding system fix

State the specific fix and link to the prompt that implements it (where applicable). Each cause has a defined fix; do not improvise.

State what the fix outputs, so the user knows what to expect:
- Cause #1 → output is a one-sentence next-action spec.
- Cause #2 → output is an environment change (pre-staged state, reduced friction path).
- Cause #3 → output is a scheduled decision block before the work.
- Cause #4 → output is a moved calendar block.
- Cause #5 → output is a capture-and-triage spec.
- Cause #6 → output is the task moved to a waiting-on list with a trigger.

### Step 4 — Predict the post-fix observable

State what should be true *after* the fix runs, before the next attempt. This is the prompt's diagnostic check — if the prediction doesn't hold, the diagnosis was wrong.

- Cause #1: a one-sentence "next action" exists; the user can read it and start within 60 seconds.
- Cause #2: from "open laptop" to "first value-producing keystroke" is < 30 seconds.
- Cause #3: a written decision exists before the work block.
- Cause #4: the work block is in a high-energy window.
- Cause #5: the task is in the user's primary inbox / triage flow.
- Cause #6: the task is on a "waiting-on" list, not the do list.

### Step 5 — Refuse the motivation framing explicitly

Close with one sentence stating that if, after the fix, the task is still not getting done, the next move is *not* "try harder" — it is to re-run this prompt with the new evidence, then route to `agency_stuck_diagnosis.md` if the cause is no longer system-level.

---

## Constraints

### Must
- Refuse motivation / discipline / character framings on intake. State the refusal explicitly.
- Pick exactly one cause from the taxonomy.
- Justify the pick with specific reference to inputs 3–8.
- Output the named system fix (and link the implementing prompt where applicable).
- State a post-fix observable prediction.

### Must Not
- Recommend "be more disciplined," "build willpower," "just start," or any motivation-class advice.
- Diagnose ADHD, depression, executive-function disorders, or any clinical condition.
- Add causes to the taxonomy.
- Output multiple system fixes. One cause, one fix.
- Recommend a productivity app or tool as the fix. Tools are downstream.

---

## False-Positive Prevention

1. **Don't default to Cause #1 (ambiguous next action).** It's the most common cause but also the over-diagnosis trap. Confirm via input 4: if the user *can* state a physical motion clearly, Cause #1 is not it.
2. **Don't miss Cause #5 (capture failure).** It looks like procrastination but the actual signal is "I keep forgetting." Input 5 will show inconsistent attempts at the task interleaved with surprise at re-finding it.
3. **Don't use Cause #6 (hidden dependency) as a license to wait passively.** The fix includes one nudge to the dependency. Procrastinating something that *was* waiting and is now your turn is not Cause #6.
4. **Don't confuse Cause #3 (decision fatigue) with Cause #1 (ambiguous next action).** Cause #1: user can't name the physical motion. Cause #3: user can name it but the motion forks at step 2 onto a fork they haven't decided. The fix differs.
5. **Don't conflate task-level procrastination with project-level stuckness.** This prompt is task-scoped. If the user keeps producing tasks in the procrastination class and abandoning them, escalate to `agency_stuck_diagnosis.md` or `bottleneck_locator.md`.
6. **Don't accept "I'm just lazy" mid-diagnosis.** That's the framing the prompt refused at intake; if it shows up later, name it again and continue with the cause taxonomy.

---

## Output Format

```
[If user framed it as motivation/discipline: one-sentence refusal of that framing, redirecting to systems diagnosis.]

## Diagnosis
**Cause:** #N — [name]
**Justification:** [1–2 sentences citing specific inputs]
**Secondary candidate (if any):** [cause + brief reason, or "none"]

## System fix
[Named fix from the table, with link to the implementing prompt if applicable. State what the fix outputs.]

## Post-fix observable (prediction)
After the fix runs and before the next attempt, the following will be true: [specific check].

If this prediction doesn't hold, re-run this prompt with the new evidence.

## What this diagnosis is not doing
- Not telling you to "try harder."
- Not diagnosing a clinical condition.
- Not prescribing a tool or app.
- Not generalizing from this task to "you procrastinate."

If the system fix runs and the task still doesn't get done, the next move is `agency_stuck_diagnosis.md`, not motivation work.
```

---

## Verification

- [ ] Motivation/discipline framing refused at intake.
- [ ] Exactly one cause from the six-cause taxonomy selected.
- [ ] Justification cites specific inputs.
- [ ] System fix matches the cause; implementing prompt linked where applicable.
- [ ] Post-fix observable prediction is concrete and testable.
- [ ] No motivation-class advice, no clinical diagnosis, no tool prescription.
- [ ] No new causes added to the taxonomy.
