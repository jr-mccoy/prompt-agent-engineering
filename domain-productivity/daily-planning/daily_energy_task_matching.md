---
title: "Daily Energy-Task Matching"
category: productivity/daily-planning
description: "Match today's tasks to the user's energy curve so cognitively demanding work lands in high-energy windows and administrative work in low-energy ones."
techniques:
  - ST-01
  - DS-01
  - DS-02
  - CM-02
  - QA-01
  - RT-02
difficulty: intermediate
tags:
  - energy-management
  - task-sequencing
  - scheduling
  - cognitive-load
  - daily-planning
updated: "2026-05-12"
related_prompts:
  - domain-productivity/daily-planning/daily_task_list_builder.md
  - domain-productivity/daily-planning/daily_morning_planning_sequence.md
  - domain-productivity/deep-work/deepwork_match_tasks_to_calendar.md
  - domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md
---

# Daily Energy-Task Matching

**Objective:** Resequence today's task list by matching task cognitive demands to the user's energy curve throughout the day. Produces a better-ordered daily schedule that places deep or creative work in high-energy windows and administrative or routine tasks in low-energy ones.

**When to use:** After a task list is built for the day, when you want to sequence it intelligently rather than randomly. Most useful when you have a mix of cognitively demanding, administrative, and social tasks that can be moved to different times. Less useful when the calendar is already full and every hour is committed.

**Audience:** People who have meaningful discretionary control over when they do different types of work during the day — knowledge workers, students, freelancers, and self-directed professionals. Not for people whose entire day is externally scheduled (meetings back-to-back, shift workers with fixed tasks). Not a substitute for the weekly planning that creates protected deep-work blocks — this operates within whatever schedule already exists today.

---

## Inputs Required

1. **Today's task list.** The full list of tasks you intend to work on today. For each task, a rough sense of what it involves is helpful ("write the Q2 analysis" vs. "reply to the email" vs. "call the vendor"). Does not need to be pre-sorted.

2. **Today's fixed calendar.** All fixed commitments with their times — meetings, calls, appointments, pickups. These are constraints the schedule must work around, not elements that can be moved.

3. **Your energy pattern.** A self-reported description of how your energy typically moves through the day. Examples:
   - "Sharp and focused from 7–10am, foggy from 1–3pm, decent from 4–6pm"
   - "Slow start, peak from 10am–1pm, dead in the afternoon, second wind around 7pm"
   - "Good all morning, need caffeine after lunch, reasonable until 5pm"
   - "Varies a lot — I don't have a reliable pattern"

   If the user says they have no reliable pattern, ask them to describe today specifically: how do they feel right now, and when do they expect to feel sharper or more sluggish?

4. **Task flexibility.** Are there any tasks that must happen at a specific time regardless of energy (a call at 2pm, a report due by noon)? Flag these separately — they anchor the schedule and cannot be moved.

---

## Instructions

### Step 1 — Map the Energy Curve

From the user's energy description, create a simple three-tier map of today:

- **High-energy windows:** When alertness and cognitive capacity are at their best. Reserve for deep, creative, or analytical work.
- **Moderate-energy windows:** Functional but not peak. Good for social tasks, meetings, communication, and tasks requiring judgment but not deep concentration.
- **Low-energy windows:** The post-lunch slump, late-afternoon trough, or early-morning fog. Suited for administrative work, email, routine processing, and low-stakes decisions.

If fixed calendar commitments occupy windows that would otherwise be high-energy, note this — it is a structural loss, not something this prompt can fix, but the user should be aware.

### Step 2 — Classify Each Task by Cognitive Demand

Assign each task to one of four categories:

- **Deep / Creative:** Requires sustained focus and original thinking — writing, analysis, coding, design, complex problem-solving. Best in high-energy windows.
- **Administrative / Routine:** Mechanical tasks with known steps — email replies, filing, scheduling, expense reports, form completion. Best in low-energy windows.
- **Social / Communicative:** Calls, meetings, negotiations, interviews, presentations. Require moderate energy and presence. Best in moderate-energy windows or when the user is naturally more verbal and social.
- **Physical / Errand:** Tasks that require movement or physical presence but minimal cognitive load. Can often be placed in low-energy windows as a natural reset.

Flag any task the user labeled as "quick" but which, on inspection, requires sustained focus — these are often misclassified and need high-energy placement despite the user's instinct to squeeze them into low-energy gaps.

### Step 3 — Place Anchored Tasks

Place all time-constrained tasks first — anything with a hard deadline or fixed time. These do not move.

Note any anchored task that falls in a high-energy window: if a routine meeting occupies 9–10am and 9–10am is the user's peak window, that is a planning loss worth naming. Do not solve it in this prompt — just name it.

### Step 4 — Fill the Windows

Into the remaining open time, place tasks by matching their demand category to the energy tier:

- High-energy windows → Deep / Creative tasks (MIT first)
- Moderate-energy windows → Social / Communicative tasks
- Low-energy windows → Administrative / Routine tasks, Physical / Errand tasks

If there are more deep tasks than high-energy time allows, rank them by importance and place the overflow in the next-best available window with a note that this is a suboptimal placement. Do not pretend the match is clean if it isn't.

Leave at least 15 minutes of unscheduled buffer in each half-day. A fully-packed energy schedule fails on the first interruption.

### Step 5 — Produce the Resequenced Schedule

Output a time-blocked schedule for the day that shows which task occupies which window, why (energy match), and the task's demand category. Also note the "energy cost" of any placements that don't fit the ideal pattern (deep work placed in a low-energy window due to constraint).

---

## Constraints

### Must
- Map the user's energy curve explicitly before sequencing tasks
- Classify each task by cognitive demand (Deep, Administrative, Social, Physical)
- Place the MIT in the user's first high-energy window that isn't already claimed by a fixed commitment
- Flag energy-cost placements when a task lands in a mismatched window due to constraints
- Leave buffer time unscheduled in each half-day

### Must Not
- Rearrange anchored tasks (hard deadlines, fixed meetings) — these are constraints, not variables
- Place all deep tasks in the morning by default without checking the user's actual energy pattern (not everyone peaks in the morning)
- Fill every open hour — the schedule must have slack
- Classify a task as "administrative" just because the user calls it quick — inspect the actual cognitive demand
- Produce a schedule that requires continuous switching between deep and social tasks with no transition time

---

## False-Positive Prevention

1. **The morning-peak assumption trap:** Not everyone has peak energy in the morning. Some people peak at 10am, some at 2pm, some in the evening. Use the user's stated pattern, not the cultural default. If the user says their best window is 4–6pm, place the MIT there.

2. **The misclassified-quick-task trap:** Tasks described as "quick" are frequently deep tasks that the user is underestimating or avoiding. "Just write a quick email to the board" may be a 45-minute communication task requiring careful thinking. Inspect before classifying.

3. **The meeting-as-recovery trap:** Many people schedule meetings in their low-energy windows thinking meetings are low-demand. But meetings that require persuasion, conflict navigation, or complex discussion are social tasks that need moderate energy. A poorly-timed difficult meeting in a low-energy slot is worse than placing it in a moderate-energy window.

4. **The overcrowded-deep-window trap:** High-energy windows are finite and valuable. If four deep tasks compete for a two-hour high-energy window, the schedule is lying to the user. Acknowledge the overflow explicitly and recommend which tasks to defer or place in lower-quality windows.

5. **The energy-pattern volatility trap:** Energy patterns are tendencies, not guarantees. If the user reports high variability ("I never know when I'll feel good"), build the schedule around the most likely pattern but note that it should be reassessed in the first 30 minutes of the day.

---

## Output Format

```
## Energy-Task Schedule — [Date]

### Energy Map

| Window | Energy Tier | Best task types |
|--------|-------------|-----------------|
| [Time range] | High | Deep, creative, analytical |
| [Time range] | Moderate | Social, communicative, meetings |
| [Time range] | Low | Admin, email, routine, errands |
| [Time range] | [Tier] | [Types] |

---

### Task Classifications

| Task | Demand type | Ideal energy tier |
|------|-------------|-------------------|
| [Task] | Deep | High |
| [Task] | Administrative | Low |
| [Task] | Social | Moderate |
| ... | | |

---

### Resequenced Daily Schedule

| Time | Task | Energy tier | Match quality |
|------|------|-------------|---------------|
| [Time]–[Time] | [Anchored commitment] | [Tier it falls in] | Fixed |
| [Time]–[Time] | [Task] | High | Optimal |
| [Time]–[Time] | [Task] | Low | Optimal |
| [Time]–[Time] | [Task] | Low (placed in moderate due to constraint) | Suboptimal — [reason] |
| [Time]–[Time] | [Buffer / transition] | — | — |
| ... | | | |

---

### Energy-Cost Flags

- [Task] placed in [Tier] window instead of [Ideal Tier] because [reason]. Expected impact: [lighter output / may take longer / consider deferring].

---

### Notes

- MIT ([task name]) placed in [time range] — your first high-energy window.
- [Any structural observation about today's energy pattern vs. calendar constraints]
```

---

## Verification

- [ ] Energy curve is mapped explicitly with at least three tiers
- [ ] Every task is classified by cognitive demand type
- [ ] MIT is placed in the first available high-energy window
- [ ] Anchored tasks (fixed commitments) are not moved
- [ ] Buffer time is present in each half-day (at least 15 minutes)
- [ ] Suboptimal placements are flagged with a reason and expected impact
- [ ] Energy pattern is user-reported, not assumed from time of day
- [ ] No window is fully packed without slack
