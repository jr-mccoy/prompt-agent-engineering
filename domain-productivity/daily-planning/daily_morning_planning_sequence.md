---
title: "Daily Morning Planning Sequence"
category: productivity/daily-planning
description: "A structured 10–15 minute morning startup routine that reviews yesterday, checks today's calendar, picks 1–3 MITs, and produces a concrete plan for the day."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - RT-09
difficulty: beginner
tags:
  - morning-routine
  - daily-planning
  - mit
  - startup-ritual
updated: "2026-05-12"
related_prompts:
  - domain-productivity/daily-planning/daily_task_list_builder.md
  - domain-productivity/daily-planning/daily_end_of_day_shutdown.md
  - domain-productivity/deep-work/deepwork_match_tasks_to_calendar.md
  - domain-productivity/reviews/reviews_weekly_systems_review.md
---

# Daily Morning Planning Sequence

**Objective:** Run a fast, structured morning planning session (10–15 minutes) that closes out yesterday's open loops, checks today's calendar and constraints, picks 1–3 Most Important Tasks, and produces a one-page plan for the day. Not a deep-planning session — a startup ritual.

**When to use:** At the start of each workday, before opening email, Slack, or social media. Works best as the first deliberate act of the day. Also useful after an interrupted start when you've lost your morning footing and need to re-anchor to a plan.

**Audience:** Anyone who wants a repeatable morning startup that takes under 15 minutes. Works for remote workers, students, freelancers, and hybrid workers. Not for mornings with fewer than 20 minutes before the first commitment — in that case, just name one MIT and go. Not a replacement for weekly or monthly planning.

---

## Inputs Required

1. **Time available this morning.** How many minutes do you have before your first commitment or before you need to be in execution mode? "I have 20 minutes" is enough. This determines how deep to go.

2. **Yesterday's state.** Did you finish what you planned, or are there open loops? A one-line summary is fine: "Got the proposal done, didn't finish the invoices, left one email unanswered." If yesterday was clean, say so.

3. **Today's calendar.** Fixed commitments with approximate times. Meetings, appointments, pickups, deadlines. "Standup at 9, client call at 2pm, pick up kids at 5" is sufficient.

4. **One open question or uncertainty.** Is there anything you're unsure about that will affect today — a decision you're waiting on, a task you're anxious about, something that might derail the plan? Optional, but surfacing this early prevents it from festering.

---

## Instructions

### Step 1 — Clear Yesterday's Open Loops (2 minutes)

Review what the user said about yesterday. For each unfinished item:
- Is it still relevant today? If yes, add it to today's candidate pool.
- Can it be deferred without consequence? If yes, mark it deferred.
- Has it become irrelevant or someone else handled it? Drop it.

Do not carry every unfinished item forward automatically. Yesterday's incomplete tasks re-compete for today's slots on merit — they do not jump to the top by virtue of being old.

### Step 2 — Read the Calendar Constraints (1 minute)

From today's calendar, extract:
- The first hard commitment (this determines when execution mode ends if starting immediately)
- The largest open block of discretionary time
- Any hard deadlines embedded in the schedule

State this summary in one line: "Your first commitment is at [time]. Your largest open block is [time range]. Hard deadline today: [item, if any]."

### Step 3 — Pick 1–3 MITs

From the pool of available tasks (open loops from yesterday that survived Step 1, plus anything the user holds in mind), identify 1–3 Most Important Tasks for today.

Rules:
- If time available is under 4 hours: one MIT only.
- If time available is 4–6 hours: up to two MITs.
- If time available is over 6 hours: up to three MITs.

The MITs must be tasks where completion today moves something meaningful forward. They are not the most urgent items by default — urgent items that are low-importance belong on a separate quick-handle list.

Name each MIT with a one-sentence completion definition: "Done means: [what the finished state looks like]." Vague MITs ("work on the report") do not count — they need a boundary.

### Step 4 — Build the Day's Plan

Sketch the day using time blocks:
- Place the first MIT in the first available focused block (before the first meeting if possible)
- Place hard-deadline items at appropriate times
- Leave a 15-minute buffer before any important meeting
- Mark the largest open block as protected work time

Do not fill every hour. A day plan with slack is more likely to succeed than a fully optimized schedule that breaks on the first interruption.

### Step 5 — Name the Open Question

If the user provided an open question or uncertainty, state it explicitly and ask whether it needs to be resolved today or can wait. If it needs resolving today, add "resolve [question]" to the MIT list or quick-handle list. Do not let an ambient worry float through the day unaddressed.

---

## Constraints

### Must
- Complete the full sequence in a way that produces output within a single interaction — this is a startup ritual, not a deep-planning session
- Name 1–3 MITs with completion definitions ("done means")
- State the day's largest open block explicitly
- Handle yesterday's open loops — do not skip this step even if the user didn't mention them

### Must Not
- Exceed the MIT count limits based on available time
- Accept a vague MIT like "work on X" — require a completion boundary
- Build a schedule that fills every available hour (leave at least 20% as buffer)
- Recommend starting with email or messages — the day plan comes before reactive communication
- Turn this into a full task list build — that is a separate prompt (Daily Task List Builder)

---

## False-Positive Prevention

1. **The everything-is-an-MIT trap:** Three MITs is a maximum, not a target. When everything feels important, ask: "If you could only finish one thing today, which one would make you feel the day was worthwhile?" That is the MIT. The others are secondary.

2. **The calendar-ignoring trap:** A plan that ignores real calendar constraints is fiction. If the user has 6 hours of meetings, the plan must reflect that — not pretend there's focus time that doesn't exist.

3. **The vague-MIT trap:** "Work on the proposal" is not an MIT. "Complete the executive summary section of the proposal (3 paragraphs)" is. Push for specificity — the completion definition is the difference between a task that gets started and one that gets avoided.

4. **The carryover-inflation trap:** Yesterday's unfinished items feel urgent because of psychological incompleteness, not actual importance. They re-compete on merit. Do not automatically front-load the day with yesterday's leftovers.

5. **The no-buffer trap:** A morning plan that schedules all available hours is a plan that fails at the first interruption. Flag any plan that has less than 20% unscheduled time and recommend cuts.

---

## Output Format

```
## Morning Plan — [Date]

**Time available before first commitment:** [X minutes/hours]
**First commitment:** [Time — what it is]
**Largest open block:** [Time range]
**Hard deadlines today:** [Item / None]

---

### Today's MITs

1. **[MIT name]**
   Done means: [Specific completion definition]
   Planned time: [Block in the schedule below]

2. **[MIT name]** *(if applicable)*
   Done means: [Specific completion definition]
   Planned time: [Block]

3. **[MIT name]** *(if applicable)*
   Done means: [Specific completion definition]
   Planned time: [Block]

---

### Day Sketch

| Time | Block |
|------|-------|
| [Start]–[Time] | [MIT 1 / focused work] |
| [Time]–[Time] | [Commitment: meeting/appointment] |
| [Time]–[Time] | [Buffer / transition] |
| [Time]–[Time] | [MIT 2 / focused work / protected block] |
| [Time]–[Time] | [Quick-handle tasks / admin] |
| [Time]–[End] | [Buffer / shutdown ritual] |

---

### Yesterday's Open Loops — Handled

- [Item] → [Added to MITs / Deferred to [date] / Dropped]
- ...

---

### Open Question

**[Question]** → [Resolve today: add to plan / Can wait: flag for weekly review]
```

---

## Verification

- [ ] MITs have completion definitions ("done means"), not just task names
- [ ] MIT count matches available time (1 for under 4h, up to 3 for 6h+)
- [ ] Day sketch accounts for all known calendar commitments
- [ ] At least 20% of available time is unscheduled (buffer)
- [ ] Yesterday's open loops are addressed — not silently carried forward
- [ ] No MIT is a vague category ("work on X") — all have boundaries
- [ ] Output was produced in a single interaction (not an extended planning session)
