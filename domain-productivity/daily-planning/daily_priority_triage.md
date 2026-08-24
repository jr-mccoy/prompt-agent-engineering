---
title: "Daily Priority Triage"
category: productivity/daily-planning
description: "Triage an existing task list using urgency and importance to produce four quadrant assignments and a single concrete start-here recommendation."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - RT-06
  - AG-11
difficulty: intermediate
tags:
  - prioritization
  - triage
  - urgency
  - eisenhower
  - daily-planning
updated: "2026-05-12"
related_prompts:
  - domain-productivity/bottlenecks/bottleneck_locator.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-productivity/daily-planning/daily_task_list_builder.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Daily Priority Triage

**Objective:** Take an existing task list of 10–20 items and classify every item into urgency-importance quadrants, then produce a single concrete start-here recommendation with an explicit reason.

**When to use:** When you have a list already built but feel stuck, overwhelmed, or unsure what to actually start. Most useful between 8–10am when the list feels like a wall. Also useful after an interruption-heavy morning when you've lost your original plan and need to reorient.

**Audience:** Anyone with a task list in front of them that feels unworkable. Not for building a list from scratch — use the Daily Task List Builder for that. Not useful when the list has fewer than 5 items; in that case, just pick the most time-sensitive one and start.

---

## Inputs Required

1. **Task list.** Paste your current task list exactly as it stands — do not pre-sort or filter. A good input is raw and complete, including tasks you're avoiding. A bad input is a pre-filtered "best of" list that hides the real backlog.

2. **Deadlines.** For any item with a deadline today or tomorrow, note it next to the task. Be specific: "due by 5pm" beats "due soon." If you don't know the deadline for an item, say so — unknown deadlines are treated as non-urgent unless stated otherwise.

3. **Who's waiting.** Any tasks where another person is blocked on you specifically. Include their name and approximate urgency: "Maria needs the contract draft by noon" is useful. "The team generally expects this at some point" is not.

4. **Current time and remaining work window.** What time is it now, and how many hours do you have left today? This determines whether a multi-block task is still feasible and affects the sequence recommendation.

---

## Instructions

### Step 1 — Classify Every Item

Assign each task to exactly one quadrant. Do not leave any item unclassified.

- **Q1 — Urgent + Important:** Real external deadline today or tomorrow, or someone is concretely blocked on you right now. Significant consequence if missed today.
- **Q2 — Not Urgent + Important:** No pressing deadline, but advances a meaningful goal. High-value work that rarely feels urgent — which is why it never gets done.
- **Q3 — Urgent + Not Important:** Has a deadline or someone wants it fast, but the consequence of missing it is low, or it serves someone else's priority rather than yours.
- **Q4 — Neither:** No real deadline, no meaningful outcome. Often filler tasks that feel like productivity.

### Step 2 — Challenge the Urgency Claims

After initial classification, review every item assigned to Q1 and Q3. For each one, ask: "Is this deadline external — imposed by another person or a hard system constraint — or is it self-imposed?"

Self-imposed urgency does not count as Q1 urgency unless the consequence of slipping is real and specific. Reclassify items that fail this test.

Also check: does any Q1 item have a deadline that is actually tomorrow or later? If slipping it to tomorrow has no real consequence, move it to Q2.

### Step 3 — Build the Start-Here Recommendation

From Q1 items, select the single task with the hardest external deadline or the most visible concrete blocker. This is the **Start Here** task.

State three things about it:
1. The task name
2. The specific reason (exact deadline or exact person blocked)
3. The first physical action to begin (open the file, call X, write the first sentence)

If Q1 is empty, select the single Q2 item with the most downstream leverage — completing it unblocks the most other work, or advances the most important ongoing goal. Apply the same three-item format.

If everything is Q3 or Q4, flag this explicitly: the list is filled with other people's urgencies while the user's own priorities are absent. This is a structural problem, not a triage problem.

### Step 4 — Sequence the Rest of Q1

After the Start Here task, list remaining Q1 items in deadline order. This is today's must-do stack. If the stack exceeds remaining work hours, flag the overflow — something will not get done, and it is better to name that now than discover it at 5pm.

### Step 5 — Flag Q2 for Scheduling

Q2 items do not get done by triage — they disappear into the background. For each Q2 item, recommend a specific time block today (if discretionary time remains) or flag it for tomorrow's planning session. Do not leave Q2 items as floating intentions.

---

## Constraints

### Must
- Classify every item in the input list — no miscellaneous or unassigned bucket
- Produce exactly one Start Here task with a named, specific reason
- Challenge urgency claims by distinguishing external vs. self-imposed deadlines
- Flag Q2 items with a scheduled time, not just a classification
- Name the specific first physical action for the Start Here task

### Must Not
- Produce a top-3 or top-5 "priorities" list in place of a single Start Here task
- Accept "everything is urgent" as a terminal state — probe for the hardest external constraint
- Move Q4 items into Q2 to make the list look more substantive
- Recommend the Start Here task based on ease ("start with the quick win") rather than consequence
- Treat vague deadline language ("soon," "when you can") as evidence of urgency

---

## False-Positive Prevention

1. **The urgency inflation problem:** When users feel overwhelmed, everything gets labeled urgent. If more than half the list lands in Q1, challenge each item: "If you told the requester this would be one day late, what is the actual consequence?" Real Q1 items survive this question. Self-imposed urgency does not.

2. **The easy-first trap:** Starting with quick wins feels productive but often means spending the morning on Q3/Q4 items while real Q1 deadlines close in. The Start Here recommendation must be driven by consequence, not effort level or time-to-completion.

3. **Q2 neglect:** Triage naturally fills Q1 while Q2 accumulates invisibly. If Q2 has more than 5 items with no scheduled time, flag this as a structural problem — the user is running on crisis mode and important non-urgent work is being quietly abandoned.

4. **Deadline vagueness as fake urgency:** "Needs to be done soon" is not a deadline. If the user cannot give a specific time, treat the item as non-urgent for today's triage. Vague urgency language must not bump items into Q1.

5. **Borrowed urgency:** "The team generally expects this" is not the same as "Maria is blocked and cannot proceed." Only concrete, named blockers and specific deadlines count as external urgency. Ambient team expectations belong in Q2 at best.

---

## Output Format

```
## Priority Triage — [Date, Time]

**START HERE:** [Task name]
- Reason: [Specific deadline / Specific person blocked / Specific consequence]
- First action: [Exact physical step — open the file, call X, write the first line]

---

### Q1 — Urgent + Important (do today, in deadline order)

| # | Task | Deadline | Blocker |
|---|------|----------|---------|
| 1 | [START HERE task] | [Time] | [Who / what] |
| 2 | [Next Q1 task] | [Time] | |
| ... | | | |

[If Q1 total exceeds remaining work hours: flag overflow here — "Items 3+ will not fit today. Communicate now if needed."]

---

### Q2 — Important, Not Urgent (schedule or lose)

| Task | Scheduled time block |
|------|---------------------|
| [Task] | [Today 3–4pm / Tomorrow 9–10am / Protected block this week] |
| ... | |

---

### Q3 — Urgent, Not Important (fast-handle or delegate)

- [Task] — [Do in < 10 min or delegate to: X]
- ...

---

### Q4 — Neither (drop or indefinitely defer)

- [Task] — [Drop / Move to someday list]
- ...

---

**Urgency reclassifications:** [Any items moved out of Q1 after challenge, with reason]
**Q2 alert:** [If Q2 has 5+ items with no scheduled block: flag "Q2 accumulation detected — schedule protection needed"]
```

---

## Verification

- [ ] Every item from the input list appears in exactly one quadrant
- [ ] Start Here is a single task with a specific external reason, not a general priority
- [ ] First physical action is stated for the Start Here task
- [ ] At least one urgency claim was challenged (even if it survived)
- [ ] Q2 items each have a recommended time block, not just a quadrant label
- [ ] No item is in Q1 solely because the user feels anxious about it
- [ ] Overflow in Q1 is flagged if it exceeds remaining work hours
