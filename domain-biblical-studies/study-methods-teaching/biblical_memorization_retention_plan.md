---
title: "Scripture Memorization & Retention Plan — Spaced, Verse-Accurate"
category: biblical-studies/study-methods-teaching
description: "Design a spaced-repetition memorization schedule for a passage or set of verses, using a translation the user names, with exact wording supplied by the user, plus review cadence, chunking strategy, and recall checks. Requires verse-accurate text; never quotes Scripture from memory."
techniques:
  - ST-01
  - ST-02
  - ED-01
difficulty: beginner
tags:
  - memorization
  - spaced-repetition
  - retention
  - habit
updated: "2026-06-06"
related_prompts:
  - domain-biblical-studies/study-methods-teaching/biblical_reading_plan_designer.md
  - domain-biblical-studies/study-methods-teaching/biblical_soap_devotional_method.md
---

# Scripture Memorization & Retention Plan

**Objective:** Build a realistic, spaced memorization plan for a chosen passage or verse set in a named translation — chunking, schedule, review cadence, and recall checks — that fits the user's time and sticks.

**When to use:**
- You want to memorize a verse, passage, or set and actually retain it.
- Helping a group or family memorize together.

**When NOT to use:**
- You want a reading (not memorization) plan — use `biblical_reading_plan_designer.md`.

**Audience:** Laypeople (L), group leaders (G). Beginner-friendly.

---

## Inputs / Context

1. **What to memorize.** The verse(s)/passage **wording, pasted by the user**, in a named translation. The model must not supply or alter the text from memory.
2. **Time budget.** Minutes/day and target date.
3. **Experience.** New to memorization or experienced.

---

## Constraints

### Must
- Use the **exact user-supplied wording** and named translation throughout; if not supplied, request it before building the plan.
- Apply spaced repetition: introduce, then review at expanding intervals.
- Chunk longer passages sensibly (phrases/clauses), building cumulatively.
- Include periodic **recall checks** the user runs against their own supplied text.

### Must Not
- Quote, complete, paraphrase, or "correct" the verse text from memory.
- Mix translations or alter wording.
- Add interpretive doctrine; this is a retention tool.

### Tradition-neutral stance (Must / Must Not)
- **Must:** respect the user's chosen translation without comment on its tradition.
- **Must Not:** push a "better" translation or a doctrinal reading.

---

## Instructions

### Step 1 — Confirm the text
Echo the user-supplied wording and translation. If missing, ask for it.

### Step 2 — Chunk
Break the passage into memorable chunks (for single verses, into phrases).

### Step 3 — Schedule
Lay out a day-by-day plan: new material + spaced review at expanding intervals, fitting the time budget and target date.

### Step 4 — Recall checks
Define checkpoints where the user recites/writes from memory and compares to their supplied text.

### Step 5 — Retention tips
Brief, practical reinforcement techniques (association, writing, speaking aloud).

---

## Output Format

```
# Memorization Plan — [reference] ([translation])

## Text to memorize (as supplied by user)
"[user-supplied wording]"

## Chunks
1. [chunk] / 2. [chunk] / ...

## Schedule
- Day 1: learn [chunk]; review [..]
- Day 2: learn [chunk]; review [Day-1] ...
- [expanding-interval reviews to target date]

## Recall checks
- [checkpoint]: recite/write and compare to your text.

## Retention tips
- [tip] / ...
```

---

## Verification

- [ ] Exact user-supplied wording used; nothing supplied/altered from memory.
- [ ] One named translation throughout.
- [ ] Spaced repetition with expanding intervals.
- [ ] Sensible chunking; cumulative build.
- [ ] Recall checks against the user's own text.

---

## False-Positive Prevention

❌ **DON'T:**
- Type out the verse from memory or "fix" the user's wording.
- Switch translations mid-plan.
- Turn the plan into a doctrinal lesson.

✅ **DO:**
- Use only the user's supplied text and translation.
- Schedule spaced, expanding reviews to the target date.
- Have the user self-check recall against their own text.
