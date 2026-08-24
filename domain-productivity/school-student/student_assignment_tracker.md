---
title: "Assignment Tracker and Weekly Action Plan"
category: productivity/school-student
description: "Turn a list of simultaneous assignments into a prioritized this-week action plan that accounts for deadlines, effort, dependencies, and progress."
techniques:
  - ST-01
  - DS-01
  - DS-02
  - CM-02
  - QA-01
  - RT-09
difficulty: intermediate
tags:
  - assignments
  - prioritization
  - planning
  - deadlines
  - academic
updated: "2026-05-12"
related_prompts:
  - domain-productivity/daily-planning/daily_task_list_builder.md
  - domain-productivity/daily-planning/daily_priority_triage.md
  - domain-productivity/deep-work/deepwork_decompose_complex_task.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Assignment Tracker and Weekly Action Plan

**Objective:** Given a student's current assignments across all subjects, produce a prioritized action plan for the next 7 days — accounting for deadlines, effort, work already done, and dependencies — not just a sorted due-date list.

**When to use:** When a student has three or more simultaneous assignments and is unsure what to work on first, or is at risk of missing something because competing deadlines are obscuring priorities.

**Audience:** High school and college students managing multiple simultaneous assignments. Not designed for semester-level planning (use `student_semester_planner.md`) or single-subject exam prep (use `student_study_schedule_builder.md`).

---

## Inputs Required

1. **Current assignment list.** For each assignment, provide:
   - Subject/course name
   - Assignment description (what it is)
   - Due date (specific — "next Thursday" is acceptable if today's date is known; avoid "soon")
   - Effort estimate: Small (< 1 hr), Medium (1–3 hrs), Large (> 3 hrs), or best-guess hours
   - Start state: Not started | In progress (with % complete if possible) | Waiting on something
   - Any dependencies: "Can't write essay until I finish the research" or "Waiting for group partner's section"

2. **Available work time this week.** Specific windows per day (not "evenings"). Example: "Mon/Wed/Fri afternoons 2–5 PM, Tue/Thu evenings 7–9 PM, Sunday all day."

3. **Any hard constraints.** Obligations that block specific days or windows. Example: "Thursday is blocked — family event."

---

## Instructions

### Step 1 — Parse and normalize the assignment list

Convert all due dates to specific dates. Flag any assignment with a vague due date ("whenever") — assume end of current week for planning purposes and note the assumption.

For each assignment, compute a **urgency score** using this simple model:
- Days until due: ≤ 2 = High, 3–5 = Medium, 6+ = Low
- Effort: Large = +1 urgency tier, Small = -1 urgency tier
- Start state: Not started = +1 urgency tier, In progress = 0, Waiting on external = deprioritize and flag

Final urgency: Critical | High | Medium | Low

### Step 2 — Identify at-risk assignments

Flag any assignment that meets at least one of these conditions:
- Due within 4 days AND Large effort AND not yet started
- Due within 2 days AND Medium effort AND less than 50% complete
- Has a dependency that has not yet been met and the dependency-resolution deadline is unclear

For each at-risk assignment, state: what makes it at-risk, what needs to happen first, and what the consequence is if it slips.

### Step 3 — Map dependencies

List any assignment that cannot be started or completed until something else happens. For each:
- Name the blocker (internal: "I need to finish the outline before drafting" or external: "waiting for group member")
- Determine whether the blocker can be resolved this week
- If external and unresolved: flag it as a risk, schedule a follow-up action (e.g., "Send a reminder to group member by Tuesday noon")

### Step 4 — Build the 7-day action plan

Distribute work across available windows. Sequence rules:
1. Critical-urgency first — protect at least one work session for each Critical item in the first 48 hours
2. Larger assignments get split across multiple sessions (do not jam a Large assignment into one block)
3. Assignments with unmet internal dependencies: schedule the dependency first, then the dependent work
4. Waiting-on-external items: schedule a check-in action (not the work itself)
5. Do not schedule more hours than the available window allows, with a 20% buffer for friction

Output each day's plan as a session list with assignment, activity, and estimated duration.

### Step 5 — Recommend the next 3-day sequence

Distill the 7-day plan into a tighter recommendation: "Here is what to work on today, tomorrow, and the day after — in this order." This is the actionable core for a student who is overwhelmed and needs to start now.

---

## Constraints

### Must
- Assign specific assignments to specific days — not a generic "work on assignments daily"
- Flag at-risk items before the action plan, not buried in it
- Separate assignments waiting on external dependencies from those the student can act on now
- Respect stated available time windows; do not schedule sessions that exceed daily capacity
- State the recommended next-3-days sequence separately from the full 7-day plan

### Must Not
- Sort assignments only by due date and present that as a "priority order" — effort and start-state must influence sequence
- Schedule a Large unstarted assignment due in 2 days without flagging it as at-risk
- Treat a waiting-on-external assignment as workable when it genuinely cannot proceed
- Add academic advice ("talk to your professor"), emotional support, or productivity tips not requested

---

## False-Positive Prevention

1. **Due-date-only sorting:** An assignment due in 5 days that is Large and not started is higher priority than an assignment due in 3 days that is Small and 80% done. Effort and start-state must adjust the sort order.

2. **Overscheduling:** Students typically have less usable time than their stated windows suggest. Apply a 20% friction buffer (a 3-hour window yields ~2.5 hours of actual work). Do not fill every minute.

3. **Dependency ignored:** If an essay cannot be written until research is complete, scheduling "write essay" before "complete research" is a planning error — even if the essay is due first. Map dependencies before sequencing.

4. **Waiting-for-external treated as actionable:** If an assignment is blocked on a group member, professor approval, or external source, the student cannot work on it. Schedule a follow-up action (send a message, check email) instead of the assignment itself.

5. **Large assignment in a single block:** Scheduling 6 hours of a single assignment in one day for a student who said they can work in 2-hour windows is unrealistic. Split it across days.

---

## Output Format

```
ASSIGNMENT TRACKER — Week of [Start date]

FULL ASSIGNMENT LIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Assignment             | Subject | Due      | Effort | Status        | Urgency
-----------------------|---------|----------|--------|---------------|--------
[Assignment name]      | [Subj]  | [Date]   | [S/M/L]| [Not started] | [CRITICAL]
[Assignment name]      | [Subj]  | [Date]   | [S/M/L]| [In progress] | [HIGH]
...

AT-RISK FLAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠ [Assignment name]: [Why at-risk] — [What needs to happen first]
⚠ [Assignment name]: [Why at-risk] — [What needs to happen first]

DEPENDENCY MAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Assignment A] requires [Action/Assignment B] first
  → [B] is: [complete | in progress | blocked on: X]
  → Action needed: [...]

7-DAY ACTION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Day, Date] — Available: [Start–End time]
  Session 1: [Assignment name] — [Specific activity] — [Est. duration]
  Session 2: [Assignment name] — [Specific activity] — [Est. duration]

[Day, Date] — [BLOCKED: reason]
  Follow-up only: [e.g., "Check for group partner's section by 5 PM"]

...

NEXT 3 DAYS — START HERE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Today:    [Assignment] — [Specific activity] — [Duration]
Tomorrow: [Assignment] — [Specific activity] — [Duration]
Day 3:    [Assignment] — [Specific activity] — [Duration]
```

---

## Verification

- [ ] Every assignment has an urgency score based on due date + effort + start state (not due date alone)
- [ ] At-risk assignments are listed before the action plan
- [ ] Assignments with unmet dependencies are sequenced correctly (dependency first)
- [ ] Waiting-on-external assignments have a follow-up action, not a work session
- [ ] Daily sessions do not exceed available window time minus 20% buffer
- [ ] Next-3-days summary is present and actionable as a standalone list
- [ ] No Large unstarted assignment due within 2 days is treated as non-urgent
