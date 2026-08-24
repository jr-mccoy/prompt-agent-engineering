---
title: "Daily Task List Builder"
category: productivity/daily-planning
description: "Turn a raw brain dump and calendar into a single sized, prioritized task list that fits today's actual available hours."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-02
  - QA-01
  - RT-02
difficulty: beginner
tags:
  - daily-planning
  - task-management
  - prioritization
  - time-boxing
updated: "2026-05-12"
related_prompts:
  - domain-productivity/deep-work/deepwork_match_tasks_to_calendar.md
  - domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-productivity/reviews/reviews_time_audit_evidence_based.md
---

# Daily Task List Builder

**Objective:** Convert a raw brain dump of tasks, today's calendar, and yesterday's open loops into one prioritized, realistically sized daily list. Separates what belongs on today's list from what should be deferred or dropped, using the day's actual available hours as the hard constraint.

**When to use:** At the start of the workday or the night before, when you have a pile of open tasks, leftover items from yesterday, and new inputs (messages, requests, commitments) that all want space on today's list. Run this before opening email or messaging apps.

**Audience:** Knowledge workers, students, freelancers, and anyone managing their own daily schedule. Not for coordinating shared team work queues — this is a personal planning tool. Not designed for days with fewer than two hours of discretionary time (a meeting-packed day needs a different approach: pick one MIT and let the rest go).

---

## Inputs Required

1. **Brain dump.** Every task, errand, responsibility, and open loop you're aware of right now — unfiltered, in whatever order it comes out. What makes this useful: cast wide, include things that feel small or embarrassing to admit you haven't done. What makes it less useful: filtering before you dump. A cleaned-up list of 5 items hides the 15 things actually competing for your attention.

2. **Today's calendar.** Every fixed commitment today with approximate start/end times — meetings, calls, appointments, commutes, school pickups, hard deadlines. "Team standup 9–9:30, doctor 2–3pm" is enough. If you have no calendar, estimate hours you expect to lose to non-discretionary demands.

3. **Yesterday's unfinished items.** What were you supposed to do yesterday that didn't happen? One-line per item is fine. If yesterday was clean, say so — that matters too.

4. **Total work window.** The hours you have available today in total (e.g., "8am–6pm"). This is used to calculate discretionary time after meetings.

---

## Instructions

### Step 1 — Calculate Available Work Hours

From the calendar input:
- Total work window in hours
- Subtract: all fixed commitment time (meetings, appointments, commutes)
- Subtract: transition buffer — 10 minutes per discrete meeting or appointment block (this is non-negotiable; transitions cost real time)
- Round down to the nearest half-hour

Call the result **Available Hours**. State it explicitly before building the list.

If Available Hours is under 2 hours, flag this as a meeting-heavy day immediately. Size the list to 1–2 items maximum. Do not build a full list and then note it's tight — size to reality from the start.

Convert Available Hours to **25-minute work blocks** (1 hour ≈ 2 blocks). This is the **Block Budget**.

### Step 2 — Merge and Process the Brain Dump

Combine the brain dump and yesterday's unfinished items into one flat list. Remove duplicates. Mark any item that appears in both with a carryover flag — carryover items have accumulated cost and belong higher in the stack.

For each item, estimate duration in 25-minute blocks:
- Quick task (reply, short decision, single lookup): 1 block
- Medium task (draft, review, prepare, short build): 2–3 blocks
- Large task (deep analysis, complex writing, building something): 4+ blocks

Flag any item estimated at 1 block that sounds like it requires sustained thinking — these are almost always underestimated.

### Step 3 — Sort Into Three Buckets

**Do Today:** Items that are (a) urgent with real external consequences today, (b) carryover items still relevant, or (c) high-importance items that fit within the Block Budget.

**Defer:** Items with no external deadline this week, items blocked on someone else, and any items that would push the Do Today total past the Block Budget. Defer means captured and scheduled — not forgotten.

**Delegate or Drop:** Items that don't require you specifically, items that have become irrelevant, and items that have been deferred more than three times (they are not tasks — they are wishes or anxieties masquerading as tasks).

The sizing rule: if the sum of Do Today blocks exceeds the Block Budget, move the lowest-priority items to Defer until it fits. This is a hard constraint, not a suggestion.

### Step 4 — Identify the MIT

From the Do Today list, name one **Most Important Task (MIT)**: the single item that, if completed, makes the day a success regardless of what else happens.

The MIT should be:
- Owned entirely by you (no blockers waiting on others)
- Completable within today's Available Hours
- The item whose non-completion has the highest downstream cost

The MIT is not automatically the most urgent item. It is the highest-leverage item. State it separately at the top of the output.

### Step 5 — Sequence the Do-Today List

Order Do Today items for execution: MIT first, then hard-deadline items sorted by deadline time, then important items by priority, then quick items (under 1 block) as gap-fillers at the end.

Do not front-load quick wins — that is procrastination wearing a productivity costume.

---

## Constraints

### Must
- State Available Hours and Block Budget explicitly before the list
- Name exactly one MIT
- Show the Do Today block total and confirm it fits within the Block Budget
- Account for every brain dump item in exactly one bucket — nothing is silently dropped
- Include carryover items from yesterday explicitly, with a carryover flag

### Must Not
- Allow the Do Today list to exceed the Block Budget without a specific override reason
- Automatically promote yesterday's unfinished items to today's MIT — carryover items re-compete on merit
- Use vague deferral language ("soon," "later this week") — each deferred item needs either a specific date or an explicit "deprioritized indefinitely" label
- Name multiple MITs — if the user insists everything is equally important, explain that the purpose of the MIT is to force the choice, not document the tie
- Add tasks not present in the brain dump

---

## False-Positive Prevention

1. **The everything-is-urgent trap:** Anxiety makes tasks feel urgent. When urgency clusters across many items, ask for each: "Who is waiting on this today, and what is the specific consequence if it doesn't happen?" If the answer is "nothing external happens," it is not urgent for today's purposes.

2. **The optimistic estimation trap:** Users routinely estimate tasks at half their actual duration. When estimates feel suspiciously round or small — "30 minutes for a complex proposal" — push the block count up. Assume 1.5× for creative and analytical tasks.

3. **The list inflation trap:** A 25-item brain dump does not produce a 25-item daily list. If Do Today has more than 8–10 items, the list has not been sized — it has been copied. Enforce the Block Budget constraint without apology.

4. **The MIT diffusion trap:** Naming 2–3 MITs defeats the exercise. Hold the single-MIT constraint even under user pushback. The act of choosing one is the intervention.

5. **The deferred-means-forgotten trap:** Deferred items must be explicitly captured somewhere. If the user has no system for this, flag it — "defer" without a capture location is just a polite way of dropping the item.

---

## Output Format

```
## Today's Task Plan — [Date]

**Available Hours:** [X hours] → [Y 25-min blocks] (Block Budget)

---

### Most Important Task (MIT)

**[Task name]**
Why: [One sentence — what makes this the highest-leverage item today]
Est. time: [N blocks / ~X min]

---

### Do Today

| # | Task | Blocks | Notes |
|---|------|--------|-------|
| 1 | [MIT — repeated] | [n] | MIT |
| 2 | [Task] | [n] | [Deadline / Carryover / —] |
| 3 | [Task] | [n] | |
| ... | | | |

**Total: [Z] blocks of [Y] available — [fits / OVER by N blocks]**

---

### Defer

- [Task] — [Reason: no deadline / blocked by X / deprioritized indefinitely]
- [Task] — [Review: [specific date]]
- ...

---

### Delegate or Drop

- [Task] — [Delegate to: X / Drop: reason]
- ...
```

---

## Verification

- [ ] Available Hours and Block Budget are stated explicitly
- [ ] Exactly one MIT is named with a rationale
- [ ] Do Today block total is shown and confirmed within budget
- [ ] Every brain dump item appears in exactly one bucket
- [ ] No item silently disappeared from the brain dump
- [ ] Carryover items are flagged (not auto-promoted, not silently dropped)
- [ ] Deferred items have a reason or next-review trigger
