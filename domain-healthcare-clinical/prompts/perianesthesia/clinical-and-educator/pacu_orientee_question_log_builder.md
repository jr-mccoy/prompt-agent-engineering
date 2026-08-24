---
title: PACU Orientee Question Log Builder
category: pacu/orientation-curriculum
task_type: CREATE
audience: PACU orientee building a running "questions for my preceptor" log
intended_use: orientee learning tool
updated: "2026-05-15"
tags:
  - pacu
  - orientation
  - question-log
  - orientee
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-02
difficulty: beginner
related_prompts:
  - prompts/pacu_orientee_reflective_journal_prompts.md
  - prompts/pacu_orientee_topic_self_study_planner.md
  - prompts/pacu_preceptor_debrief.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
---

# PACU Orientee Question Log Builder

> Safety reminder: The question log is a learning tool. It is not a clinical record and does not replace bedside cueing or direct conversation with your preceptor.

## Objective

Set up a **running question log** the orientee fills throughout each shift and consolidates at end-of-shift. Designed to defeat the "I had a question but forgot" failure mode and to surface patterns over time (which categories of question keep coming up).

## Inputs

- **Format preference:** {{paper notebook / phone notes / digital — describe}}
- **Orientation week:** {{n}}
- **Cadence:** {{end-of-shift / mid-shift jot then end-of-shift consolidation}}

## Audience / Scope

- **Primary:** Orientee, self-use.
- **Secondary:** Primary preceptor reviews the log at the 1:1 / debrief; orientee chooses which questions to surface.
- **Scope:** Log structure only. Specific question content varies by orientee + shift.

## Output requirements

```markdown
# My Question Log — Wk {n}

> This is my log. I decide what to bring to my preceptor.

## Mid-shift jot (one line, anywhere — phone, pocket card)

Whenever a question pops up:
- 4–8 word jot: just enough to remember.
- Don't write the full question now; you'll lose the moment if you stop.

## End-of-shift consolidation (10 min)

For each jot, sort it into one of the categories below and write the full question.

### Categories

**Clinical pattern** — "Why does X happen / look the way it does?"
- Examples: "Why does post-spinal hypotension come back at 30 min?" / "Why does this patient look fine on the surface and not be ready for discharge?"

**Process step** — "How do I do X / what's the unit's way?"
- Examples: "How do we document a PONV reassessment?" / "How does the inbound handoff differ when the patient was intubated longer than expected?"

**Who do I call** — "What role do I escalate to in situation X?"
- Examples: "Who do I call when post-spinal BP keeps drifting at 60 min?" / "Who handles a bay reassignment mid-admission?"

**Source to revisit** — "I read something I want to come back to."
- Examples: "Drain's section on emergence — the part about the awareness threshold."

**Self-pattern** — "Something about how I'm working that I want to think about."
- Examples: "I keep checking the chart before listening to the SBAR — is that the right order?"

### Log table

| Date | Jot | Category | Full question | Status |
|---|---|---|---|---|
| {date} | "post-spinal 30 min?" | clinical pattern | "Why does post-spinal hypotension persist past the initial resolution window?" | open |
| {date} | "PONV reassess doc?" | process step | "How do we document PONV reassessment when there's no provider order yet?" | asked Wk 3 — answered |

## Weekly review (15 min)

End of each week:
1. Which category is biggest? (That's where the most growth is right now.)
2. Which questions are still open after 2 weeks? (Surface to preceptor.)
3. Which questions answered themselves once I had more exposure? (Note — useful pattern.)

## Bring to preceptor 1:1

You don't bring the whole log. You bring:
- The 2–3 questions you want answered this week.
- The category that's biggest (preceptor may suggest exposure or reading).
- One question you're "embarrassed to ask but want to."

## What this log is not

- Not a clinical record.
- Not a competency assessment.
- Not subject to review by anyone unless you share.

## Sources / reference

- ASPAN *Standards* — orientation reflection.
```

## Must / Must not

**Must:**
- Frame mid-shift jot as short (4–8 words) to avoid losing the moment.
- Provide explicit categories that cover the realistic question types.
- Include the weekly review.
- Keep the log owned by the orientee.
- Explicitly include an "embarrassed to ask" question as a regular slot.

**Must not:**
- Treat the log as a competency record.
- Direct the orientee to share the full log.
- Force a question per shift ("you must log 5/day").
- Project clinical priority on which categories matter most.
- Reference protected characteristics in example questions.

## Quality signals

- Within 2 weeks of starting, the orientee surfaces a pattern (e.g., "I keep asking process questions, not clinical").
- The "embarrassed to ask" slot actually gets used.
- The log table is short enough to keep, not long enough to become a chore.

## Verification

- [ ] Mid-shift jot framed as short.
- [ ] Five categories present.
- [ ] Log table includes Status column.
- [ ] Weekly review prompts included.
- [ ] Orientee ownership explicit.
- [ ] Embarrassed-to-ask slot included.
- [ ] Safety + FPP sections present.

## False-Positive Prevention

- **No invented orientation requirements** ("must log ≥ 3 questions per shift to advance").
- **No invented clinical content** in example questions (no specific doses, thresholds).
- **No invented standardized question taxonomies.**
- **No invented research claims** about question-logging.
- **No protected-characteristic example questions.**
- **No license-pathway-based question categories.**

## Worked Example

<details>
<summary>Example: end-of-shift consolidation (click to expand)</summary>

```markdown
## End-of-shift consolidation (Wk 3, Tue)

Jots: "post-spinal 30 min?", "PONV reassess doc?", "who picks bay?"

### Log table

| Date | Jot | Category | Full question | Status |
|---|---|---|---|---|
| Tue Wk 3 | "post-spinal 30 min?" | clinical pattern | Why does post-spinal hypotension persist past the initial resolution window even when the patient's volume status looks adequate? | open |
| Tue Wk 3 | "PONV reassess doc?" | process step | How do I document a PONV reassessment when the previous antiemetic was 20 min ago and there's no new order? | answered by preceptor Tue eve |
| Tue Wk 3 | "who picks bay?" | who do I call | When the bay assignment changes mid-admission, who is the right person to talk to — preceptor, charge, or in-room CRNA? | answered by charge Tue |

## Weekly review (end of week)

- Biggest category: clinical pattern (5/9). Suggests I'm hungry for "why" content.
- Open after 2 weeks: none yet.
- Answered by exposure: "who picks bay" — answered itself once I saw two reassignments.

## Bring to preceptor Mon

- Clinical pattern: post-spinal 30 min question.
- Embarrassed-to-ask: "do I really still need to manually take a BP cycle to verify or does the monitor cycle count?"
```

Notes: short jots, categories used, weekly review pattern, embarrassed-to-ask slot used.
</details>

## Self-check

- [ ] Five categories.
- [ ] Log table format clear.
- [ ] Weekly review included.
- [ ] Ownership explicit.
- [ ] Embarrassed-to-ask slot included.
- [ ] FPP section passed.
