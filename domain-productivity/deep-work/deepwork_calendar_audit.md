---
title: "Audit a Calendar for Focus Destruction"
category: productivity/deep-work
description: "Take a week of the user's actual calendar and classify every block against a fixed taxonomy of focus-destruction patterns (fragmentation, swiss-cheese, meeting-pile-up, no-runway, context-thrash) so the user sees which specific pattern is wrecking their week, not a general 'too many meetings' story."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - deep-work
  - focus
  - calendar
  - audit
  - diagnostics
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_focus_parameters_estimator.md
  - domain-productivity/deep-work/deepwork_meeting_cost_estimator.md
  - domain-productivity/deep-work/deepwork_meeting_to_async_converter.md
  - domain-productivity/deep-work/deepwork_match_tasks_to_calendar.md
---

# Audit a Calendar for Focus Destruction

**Objective:** Given a week of the user's actual calendar, identify the specific structural patterns that destroy focus and quantify the damage. Output must name patterns from a fixed taxonomy and tie each one to concrete calendar entries.

**When to use:** The user's week feels unwinnable and they suspect the calendar is the cause. Also before any calendar redesign — you cannot fix a calendar whose failure modes you have not named.

**Audience:** The individual whose calendar this is. Not their assistant, manager, or team-level ops.

---

## Inputs Required

1. **Last week's calendar, as a list of events.** For each: start time, end time, title, who called the meeting, whether attendance was mandatory, and (if known) whether they found it valuable.
2. **A marker on each event the user considers non-negotiable.** A one- or zero-per-event flag.
3. **The user's typed "usable attention span" and "context-reload cost"** from `deepwork_focus_parameters_estimator.md`, or a best-guess if unavailable (flag as guess).
4. **One sentence on the week's top outcome** — the thing that, if shipped, would have made the week worth it.

If no calendar is supplied, ask for it and stop. Do not audit a hypothetical week.

---

## Instructions

1. **Compute free-block inventory.** List every uninterrupted span of ≥ [attention span] minutes between meetings. If none exist on a given day, note that explicitly.

2. **Classify each day against the fixed focus-destruction taxonomy:**
   - **Fragmentation** — many small gaps, none long enough for deep work
   - **Swiss-cheese** — one big block in theory, punched through by 1–2 meetings
   - **Meeting pile-up** — ≥ 3 meetings back-to-back with no recovery gap
   - **No-runway** — the largest free block is before 9am or in the last hour of day (unlikely to be used)
   - **Context-thrash** — adjacent meetings on unrelated topics, forcing reload
   - **Clean** — day contains at least one protected block ≥ 2× attention span

   A day can have multiple labels. Cite the meeting titles that produced each label.

3. **Compute the week's deep-work ceiling.** Sum of free blocks ≥ [attention span] minus ([reload cost] × number of context switches between them). Report as a single number of minutes and as a fraction of the 40-hour work week.

4. **Compare ceiling against top outcome.** Is the ceiling plausibly enough time to ship the top outcome? State yes or no with a one-sentence reason.

5. **Flag the three highest-leverage changes.** Each must be a specific, named calendar entry with a specific change (move, shorten, decline, convert async). Not "fewer meetings."

---

## Output Format

```
## Week at a Glance
- Free blocks ≥ attention span: N
- Deep-work ceiling this week: NN min (N% of a 40-hr week)
- Top outcome: [quoted] — plausible within ceiling? yes/no, because ...

## Day-by-Day Diagnosis
### Monday
Labels: fragmentation, context-thrash
Evidence:
- 9:30 "1:1 with A" then 10:00 "Design review" — unrelated topics, no gap
- Largest free block: 34 min (below attention span)

### Tuesday
... (repeat per day)

## Three Highest-Leverage Changes
1. Decline or shorten [specific meeting, date, time], because [structural reason]. Recovers ~NN min.
2. ...
3. ...

## What This Audit Does Not Cover
- [anything the calendar alone cannot tell you]
```

---

## Constraints

**Must:**
- Cite specific calendar events by title and time.
- Use the labels from the fixed taxonomy exactly.
- Report the deep-work ceiling as a number, not a vibe.
- Tie the three changes to specific events.

**Must not:**
- Give general advice ("block your mornings," "have fewer meetings").
- Judge meeting content quality — this is a structural audit.
- Propose a full redesign. Only the three highest-leverage changes.
- Use adjectives like "packed" or "overwhelming" without a number behind them.

---

## False-Positive Prevention

- **"Too many meetings" bait:** This is the default and least useful conclusion. If the audit ends there, restart — which meetings, in which pattern, is the point.
- **Ideal-week fallacy:** The output is about this calendar, not an ideal one. Do not imagine events that aren't there.
- **Hidden non-negotiables:** A meeting marked non-negotiable should not appear in the three changes unless the user has authority to move it. Check the flag.
- **Attention-span mismatch:** If the user's attention span is short (e.g., 25 min), don't call a 45-min gap "fragmentation." Fragmentation is defined relative to their number.

---

## Self-Verification (before finalizing)

- [ ] Every label cites at least one calendar entry.
- [ ] The deep-work ceiling is computed, not estimated verbally.
- [ ] Each of the three changes names a specific event.
- [ ] No non-negotiable event appears among the three changes.
- [ ] Labels come only from the fixed taxonomy.
- [ ] Top outcome feasibility is answered yes/no.
