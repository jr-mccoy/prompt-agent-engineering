---
title: "Match Today's Tasks to Today's Calendar"
category: productivity/deep-work
description: "Take today's actual task list and today's actual calendar and produce a schedule that only keeps tasks the calendar can support — surfacing which tasks will not happen today so the user can reschedule or drop them before the day starts, not at 9 pm."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - OC-01
  - QA-01
difficulty: beginner
tags:
  - deep-work
  - planning
  - calendar
  - daily-plan
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Match Today's Tasks to Today's Calendar

**Objective:** Given today's task list and today's calendar, produce a schedule that only contains tasks the day can physically support. Surface which tasks will not happen today and why, before the day starts.

**When to use:** Morning planning. Also any time the user writes a daily list longer than the day can hold — which is most days.

**Audience:** The individual planning their own day, not a manager assigning work.

---

## Inputs Required

1. **Today's task list.** 3–20 items, as the user wrote them.
2. **Today's calendar.** Meetings, commitments, and protected blocks with start/end times.
3. **Per-task expected minutes.** If missing, user must estimate — you may not guess.
4. **Which tasks are hard-committed today** (external deadline, promise made, follow-through on yesterday's block). Flag each.
5. **The user's context-reload cost.** Used to price switching between blocks.

---

## Instructions

1. **Compute free-block inventory for today.** List each free block: start, end, length.

2. **Reject blocks too short to use.** Any free block < reload cost + 10 min is unusable; list but do not schedule into them.

3. **Sort tasks by "today-fit":** hard-committed → size-fits-today → size-doesn't-fit. Do not sort by importance alone — importance unmoored from fit is the problem this prompt addresses.

4. **Place tasks into blocks greedily**, largest task into largest block. Between two same-project tasks, no reload charge. Between two different-project tasks in the same block, apply reload cost.

5. **Stop placing when blocks are full.** The remaining tasks become the "won't happen today" list. Do not stretch the day to fit.

6. **For each task in "won't happen today," write one of four dispositions:**
   - Move to a specific later day
   - Delegate (name the target)
   - Drop
   - Accept this is slipping (if hard-committed but no block exists, surface the conflict)

7. **Produce a one-line "truth statement" for the day.** Example: "Today will ship A and half of B; C and D are not happening." Most users will not accept this sentence. That resistance is what makes it useful.

---

## Output Format

```
## Free Blocks Today
| Block | Length | Usable? |
|---|---|---|
| 09:00–10:30 | 90 min | yes |
| ... |

## Scheduled
| Block | Task | Est min | Project | Reload? |
|---|---|---|---|---|
| 09:00–10:30 | ... | ... | ... | — |
| ... |

## Won't Happen Today
| Task | Disposition |
|---|---|
| ... | Move to Thu |
| ... | Delegate to [name] |
| ... | Drop |
| ... | Hard-committed but no block — conflict |

## Truth Statement
[One sentence describing what today will actually ship.]
```

---

## Constraints

**Must:**
- Use real calendar blocks from input 2.
- Price reload cost between different-project tasks in the same block.
- Produce a "won't happen today" list with a disposition per item.
- Include a truth statement even when uncomfortable.

**Must not:**
- Stretch blocks to fit tasks. If a task is 90 min and no 90-min block exists, it doesn't happen.
- Schedule into "work through lunch" or "stay late." The calendar is the constraint.
- Promote a task to today just because it's important if no block supports it.
- Produce encouraging language. This is a matching tool, not a motivator.

---

## False-Positive Prevention

- **Heroic scheduling:** The default failure is a schedule that only works if the user is superhuman. Reality-check block usage — if total scheduled time > 80% of free-block time, cut.
- **Priority override:** "This is too important to drop" does not create calendar time. If a task is truly that important, something else must be dropped today; name which.
- **Estimate optimism:** Self-estimates run low. If input 3 looks uniformly optimistic (all tasks neatly fit), inflate by 25% and rerun placement. Flag that you did.
- **Task-list inflation:** A 20-item list is a wish list, not a plan. Show which 6–8 items are plausible; the rest is acknowledged as deferred.

---

## Self-Verification (before finalizing)

- [ ] Every scheduled task fits inside its block with reload buffer.
- [ ] "Won't happen today" list has a disposition per item.
- [ ] Hard-committed conflicts are surfaced, not hidden.
- [ ] Truth statement is present and concrete.
- [ ] Total scheduled time ≤ 80% of free-block time.
- [ ] No encouraging or motivational language.
