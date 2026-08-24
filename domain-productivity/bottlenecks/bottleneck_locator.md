---
title: "Locate the True Personal Bottleneck (Clarity / Execution / Distribution)"
category: productivity/bottlenecks
description: "Diagnose which of three lanes — clarity (do I know what I want), execution (can I do the work), or distribution (does the work reach anyone) — is the real bottleneck on the user's progress, so effort stops going to the easiest lane and starts going to the binding one."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - bottleneck
  - constraints
  - diagnostics
  - clarity
  - execution
  - distribution
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-productivity/bottlenecks/bottleneck_clarity_ambition_surfacer.md
  - domain-productivity/bottlenecks/bottleneck_daily_execution_habits.md
  - domain-productivity/bottlenecks/bottleneck_distribution_constraint_finder.md
---

# Locate the True Personal Bottleneck (Clarity / Execution / Distribution)

**Objective:** Name which of three lanes is actually binding on the user's progress — clarity, execution, or distribution — and produce one-sentence evidence plus a single next move in that lane. Not three balanced suggestions; one binding constraint.

**When to use:** The user has been putting in real effort and not advancing. They suspect something is off but not what. Use before committing to a new habit, course, or ship sprint — those answers are useless if aimed at the wrong lane.

**Audience:** An individual reviewing their own progress, not a coach diagnosing someone else.

---

## Inputs Required

1. **The ambition or goal at stake.** One sentence. Can be fuzzy.
2. **What the user has done in the last 30 days** toward that goal. 5–15 concrete actions. Commits, drafts, conversations, outreach, reading — whatever actually happened.
3. **What the user produced in those 30 days.** Shipped artifacts, published pieces, sent applications, shipped releases. Different from actions; actions can be large without producing anything.
4. **Who has actually seen or used what was produced.** Names, rough count, or "nobody / haven't shared."
5. **Their current best guess at the bottleneck.** Optional. Often wrong.
6. **Time budget spent in last 30 days across three categories:** thinking/planning, executing, sharing/promoting. Rough hours.

If inputs 2 and 3 are empty, the bottleneck is not one of the three lanes — it's upstream (stuckness, agency, or motivation). Refer to `agency_stuck_diagnosis.md` and stop.

---

## Instructions

1. **Define each lane concretely:**
   - **Clarity** — the user does not yet know precisely what they want or what "done" looks like. Symptom: plans keep changing; "pivoting" monthly; can't finish because can't decide.
   - **Execution** — the user knows what to do but isn't doing it at useful volume or quality. Symptom: drafts unfinished, features half-built, deliverables late.
   - **Distribution** — the user produces real work that goes nowhere. Symptom: finished artifacts with no audience, shipped features with no users, written pieces with no readers.

2. **Score each lane on observed signal, not self-report:**
   - Clarity: does input 1 sound like a decision or a fog? Did input 2 change direction mid-period?
   - Execution: ratio of actions (input 2) to shipped artifacts (input 3). If artifacts = 0, execution is a candidate.
   - Distribution: ratio of shipped artifacts (input 3) to actual reach (input 4). If artifacts > 0 but reach = 0, distribution is a candidate.

3. **Pick exactly one lane as the binding constraint.** Prefer distribution > execution > clarity when signals tie, because most people under-invest in distribution. Break ties with input 6: where is time *not* going?

4. **Write one-sentence evidence** from inputs 2–4 and 6 supporting the chosen lane. No appeals to "it feels like."

5. **Name one next move in that lane only.** Specific, physical, this-week:
   - Clarity → "Write a one-page 'what I want and what done looks like' and show it to one person by Friday."
   - Execution → "Ship a smaller version of X by end of week; accept that it's 40% of the target."
   - Distribution → "Send the thing you already made to five named people by Thursday; collect their replies."

6. **State what not to work on.** Name the lane the user is most tempted to work on instead, and why that's a distraction from the binding constraint.

7. **Produce a 14-day check-in question** that will reveal whether this was the right diagnosis. Example: "In two weeks, have five named people seen the work? If yes, distribution was it."

---

## Output Format

```
## Goal
[Input 1 restated]

## Lane Signals
| Lane | Signal | Score |
|---|---|---|
| Clarity | [observed signal] | strong / mixed / not binding |
| Execution | [ratio of actions to ships] | ... |
| Distribution | [ratio of ships to reach] | ... |

## Binding Constraint
[One lane] — evidence: [one sentence from inputs]

## Next Move (this week)
[Specific, physical, by when, to whom]

## What Not to Work On
[The tempting other lane] — why it's a distraction: [one sentence]

## 14-Day Check-In
[Question that would reveal whether the diagnosis was right]
```

---

## Constraints

**Must:**
- Pick exactly one lane.
- Ground the pick in numeric signals from inputs 2–4 (or flag that inputs were insufficient).
- Produce one next move in the chosen lane only.
- Name the tempting wrong lane as a distraction.

**Must not:**
- Recommend parallel work across lanes ("focus on all three").
- Recommend work in the wrong lane just because it's easier.
- Accept the user's guess from input 5 without checking it against observed signals.
- Prescribe courses, books, or content consumption. The output is action, not learning.

---

## False-Positive Prevention

- **Clarity bait:** Users facing hard distribution work often retreat into "I need to clarify my vision." Unless the signals show real clarity rot (vision changes monthly, can't articulate done), distribution is usually the real answer.
- **Execution washing:** "I just need to work harder" often hides a distribution problem. If artifacts exist but nobody has seen them, execution is not the binding lane.
- **Self-report override:** Input 5 (user's guess) is data, not the answer. Compare it to signals — a mismatch is informative.
- **Insufficient signal:** If inputs 2–4 are thin (< 5 actions, 0 artifacts), the diagnosis is "agency/stuckness" not lane — redirect to `agency_stuck_diagnosis.md`.

---

## Self-Verification (before finalizing)

- [ ] Exactly one lane named as binding constraint.
- [ ] Evidence cites inputs 2–4, not just feelings.
- [ ] Next move is specific, physical, dated, this-week.
- [ ] The "tempting wrong lane" is named as distraction.
- [ ] 14-day check-in question is answerable with a yes/no or a number.
- [ ] No parallel-lane recommendations.
- [ ] If inputs 2–3 are empty, redirected to stuckness prompt.
