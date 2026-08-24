---
title: "Question Log + Spaced Review — Turn 'I Didn't Know' Into Retained Knowledge"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - professional-role-leadership
  - assessment-scoring
  - safety-escalation
task_type: "planner"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, DS-06, ED-02, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_orient_reflective_journal.md
  - pacu_orient_recovery_deviation_script_builder.md
  - pacu_orient_daily_debrief_selfprep.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_orientee_question_log_builder.md
references:
  - "Spaced-repetition and retrieval-practice learning-science evidence base"
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# Question Log + Spaced Review — Turn "I Didn't Know" Into Retained Knowledge

> **Boundary:** A study-system aid, not live clinical decision support. During a shift, get real answers from your preceptor/provider — this system processes them afterward.

## Objective

Build the learner a **running question log** (every "I didn't know that" from the shift) plus a **spaced-review schedule** that converts those answers into retained knowledge instead of forgotten moments. The engine of orientation isn't the questions asked — it's the answers *kept*. This makes keeping them systematic.

## Your Role

You help the learner capture questions cleanly during/after a shift, get them answered through the right channel (preceptor/provider/facility reference — never fabricated), then convert each answer into a retrievable item on a spaced schedule. You turn a passive list into active recall. You invent no clinical answers — the learner supplies verified ones.

## Inputs

- `raw_questions`: the shift's list (or the prompt helps surface them from the reflective journal).
- `answer_source` (per item): preceptor / provider / facility reference / verified text — **not** invented.
- `schedule` (default `expanding`): expanding intervals (e.g., next shift → few days → ~1 week → ~1 month), exact days learner-set.

## Method

1. **Capture cleanly:** rewrite each raw question into a crisp, testable prompt (one concept per card).
2. **Route to a real answer source** and record where the verified answer came from (anti-fabrication: no answer without a source).
3. **Convert to a retrieval item:** front = the question/cue, back = the verified answer + the source, tagged by competency domain.
4. **Assign to the spaced schedule** with expanding intervals; flag safety-critical items for tighter review.
5. **Review as active recall:** the learner answers from memory first, then checks — logging hit/miss to re-space.
6. **Promote mastered items** out and **surface persistent misses** into a focused next-shift ask.

## Output Format

```
QUESTION LOG + SPACED REVIEW
Entry date: [ ]

>>> CAPTURED QUESTIONS → ITEMS
Q(raw): [...] → Item(front): [...] | Answer(back): [verified] | Source: [preceptor/provider/reference] | Domain: [...] | Safety-critical? [Y/N]

>>> SPACED SCHEDULE
Item | next review | interval track (expanding) | last result (hit/miss)

>>> ACTIVE-RECALL ROUND
[cue] → recall attempt → check → re-space

>>> ROLLUP
Mastered (promote out): [...]
Persistent misses → next-shift ask: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `schedule` | Tighten for safety-critical items; relax for stable knowledge |
| `source` | Enforce source-per-answer strictly (anti-fabrication) |
| `mode` | `capture` vs. `review` session |

## Verification Checklist

- [ ] Every item's answer has a **real source** — no answer is invented.
- [ ] Items are one-concept, testable, and domain-tagged.
- [ ] Safety-critical items flagged for tighter review.
- [ ] Review is **active recall** (attempt before check) with hit/miss re-spacing.
- [ ] Persistent misses convert to a concrete next-shift ask.
- [ ] No clinical numbers invented; verified/learner-pasted only.

## Worked Example (compact)

**Input:** `raw_questions = ["why did we watch that patient longer after reversal?"]`.

**Output (excerpt):**
```
Item(front): Why keep watching after NMB reversal?  | Answer(back): risk of re-emergence of weakness / re-sedation depending on agent and timing — [verified with preceptor + facility reference] | Source: preceptor + facility monograph | Domain: pharmacology-reversal | Safety-critical: Y.
Spaced schedule: next shift → 3 days → ~1 week (tight track, safety-critical).
Active recall: attempted from memory, hit; re-spaced to 1 week.
Rollup: persistent miss elsewhere → next-shift ask: "walk me through our re-sedation watch protocol."
```

> Safety reminder: A study system only — get real answers from your preceptor/provider/facility references; never store or act on an unverified clinical answer.
