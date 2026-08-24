---
title: "Between-Session Homework Helper (Client-Side)"
category: psychology/client-self-use/session-prep-integration
description: "Help a client work with therapy homework they were assigned but are stuck on — clarify, troubleshoot, scale down, or surface what's making it hard."
techniques:
  - ST-04
  - DT-02
  - NE-01
  - ED-03
  - QA-04
difficulty: beginner
tags:
  - client-self-use
  - therapy-homework
  - between-session
  - troubleshooting
intended_use: model-testing
updated: "2026-05-08"
---

# Between-Session Homework Helper (Client-Side)

## Objective

Help a client get traction on assigned therapy homework when they're stuck. Output should:

1. Clarify what was actually assigned (clients often misremember).
2. Identify what specifically is stuck — unclear instructions, the size of the task, emotional load, time, skill gap.
3. Scale the homework down to the smallest version the client could do today.
4. Or surface that the homework isn't working and that's worth bringing back to session.

## When to Use

- Mid-week when the homework hasn't been touched.
- The day before next session, panicking that nothing got done.
- When the homework was attempted but felt wrong.
- When the assignment itself is unclear in retrospect.

## Inputs / Context

- What the homework was, as best the client recalls.
- What the modality is (CBT thought record, behavioral activation activity, exposure, DBT diary card, ACT values exercise, IFS parts work, journaling).
- What's been attempted and what happened.
- What the client thinks is making it hard.
- Days remaining until next session.

## Constraints

### Must

- Output sections in order: **What I Was Asked to Do**, **What's Stuck**, **The Smallest Version I Could Do Today**, **If Even That Is Too Much**, **What to Bring Back to My Therapist**.
- Distinguish between "I don't have time" and "I'm avoiding it" — both are valid; only the second one is therapeutic data.
- Always preserve a "bring it back to session" option; some stuckness is the work.
- For exposure / trauma / DBT chain analysis homework that may activate distress, scale down rather than push.

### Must Not

- Don't redesign the homework into a different exercise.
- Don't substitute an AI-generated alternative for what the therapist assigned.
- Don't push exposure or trauma processing the client isn't currently with their therapist on.
- Don't shame the client for not doing it.

## Instructions

1. Ask the client to recall the homework verbatim if possible.
2. Diagnose stuckness across 5 categories: clarity, size, emotional load, time, skill gap.
3. Generate the smallest viable version (often 90% smaller than the original).
4. Give an "even smaller" backup.
5. Frame what's stuck as material for the next session — the stuckness is itself useful.

## Output Format

```
=== HOMEWORK HELPER ===

What I Was Asked to Do:
- [Homework as I recall it]
- Modality: [CBT thought record / behavioral activation / exposure / DBT diary card / ACT exercise / journaling / other]
- Days until next session: [N]

What's Stuck:
- Clarity: [Do I know what was actually being asked?]
- Size: [Is the task bigger than I have capacity for right now?]
- Emotional load: [Does the topic itself activate enough distress that I bounce off?]
- Time: [Do I literally not have the time, or is it that I'm not making it?]
- Skill gap: [Do I lack a skill the homework assumes I have?]

Primary stuck point: [...]

The Smallest Version I Could Do Today:
- [Specific, time-bounded, ≤ 10 minutes when possible]
- When: [Day, time, trigger]
- Where: [Place]
- If-then backup: [If [obstacle], then I'll [smaller version]]

If Even That Is Too Much:
- [Even-smaller fallback — sometimes "write down the title of the exercise on a sticky note" is enough to count as not-zero]

What to Bring Back to My Therapist:
- "I got stuck on [specific] because [diagnosis]. The smallest version I could manage was [X]. Can we [adjust / break it down further / pick a different target]?"
```

## Verification

- [ ] Homework restated in client's recall, not paraphrased to clinical language.
- [ ] Stuck diagnosis across 5 categories.
- [ ] Smallest version is concrete (when, where, if-then).
- [ ] Even-smaller fallback included.
- [ ] Bring-back-to-therapist script generated.
- [ ] No substitution of an alternative exercise.
- [ ] No shame language.
