---
name: pacu-study-guide-builder
description: Build a structured study guide for a PACU topic — learning objectives, key concepts, self-check items, and a spaced-repetition schedule. Use when the user asks for a "study guide", "orientation study packet", "self-study material", or wants a learner-facing document for prep before a competency check. Output is self-paced, organized around objectives, and ends with a review plan.
tags:
  - pacu
  - nursing-education
  - study-guide
  - self-study
updated: "2026-04-14"
---

# PACU Study Guide Builder

## Purpose

Produce a self-study packet for a PACU topic that takes a learner from baseline to ready-for-competency-check. Organized around explicit learning objectives, with deliberate self-check points and a spaced review schedule.

## When to use

- Preceptor hands an orientee a topic to study before their next shift.
- Educator wants a self-paced review packet ahead of a scheduled quiz.
- Orientee requests material for a topic they struggled with.

## When NOT to use

- User wants the assessment itself → `pacu-quiz-generator`.
- User wants drill cards for recall → `pacu-flashcard-deck-builder`.
- User wants a mechanistic teaching doc → `pacu-in-depth-explainer`.

## Inputs required

1. **Topic.**
2. **Learner's current gap** — what do they already know, what's weak. If unknown, ask.
3. **Deadline / schedule** — when will the competency check happen. Drives the spaced-repetition layout.
4. **Source chapters** (user provides; this skill will structure around them).
5. **Time budget** — hours the learner has available.

## Workflow

1. **Confirm inputs.** Without a deadline, default to a 7-day plan.
2. **Write 4–8 learning objectives** using measurable verbs (describe, identify, interpret, perform — not "understand").
3. **Map each objective to a source chapter or section.**
4. **For each objective, produce:**
   - *Key concepts* — 3–6 bullets the learner must be able to state.
   - *Self-check* — 2–4 questions (mix of recall and application).
   - *Anchor scenario* — one real bedside situation where the objective applies.
5. **Assemble a review schedule.** For a 7-day deadline:
   - Day 1: Objectives 1–2 (read, self-check).
   - Day 2: Objectives 3–4.
   - Day 3: Objectives 5–6.
   - Day 4: Mixed review; redo missed self-checks.
   - Day 5: Anchor scenarios; think aloud with a peer.
   - Day 6: Full mock quiz (can pair with `pacu-quiz-generator`).
   - Day 7: Targeted re-study of any objective with < 80% mock-quiz score.
   Adjust for other timeframes by compressing or expanding mid-days.
6. **End with "Signs you're ready"** — concrete behaviors (not feelings): "Can recite X without looking; can sort Y red flags from non-red flags; can give the escalation trigger for Z".
7. **Safety reminder at top. Self-check below.**

## Output format

```markdown
# {Topic} — PACU Study Guide

> Safety reminder: Educational self-study aid only — clinical competency is verified at the bedside by a preceptor, not by this document.

## Learning objectives
By the end of this packet you will be able to:
1. ...
2. ...

## Source map
| Objective | Primary source | Secondary |
|---|---|---|
| 1 | *Drain's* Ch. XX | ... |

## Objective 1 — {verb + content}
### Key concepts
- ...
### Self-check
1. ...
### Anchor scenario
[1-paragraph bedside situation]

[repeat for each objective]

## Review schedule ({N}-day plan)
| Day | Focus | Activity |
|---|---|---|
| 1 | ... | ... |

## Signs you're ready
- ...
- ...

## Sources
- ...
```

## Source-fidelity rules

Cite chapters. Do not invent timeframes, doses, or facility protocols in self-check items or anchor scenarios. Anchor scenarios may be fictional but clinically plausible and must use generic supplies / orders.

## Self-check

- [ ] 4–8 learning objectives with measurable verbs.
- [ ] Every objective mapped to a source.
- [ ] Every objective has key concepts + self-check + anchor scenario.
- [ ] Review schedule matches deadline or defaults to 7 days.
- [ ] "Signs you're ready" is behavior-based, not affective.
- [ ] Safety reminder at top.
