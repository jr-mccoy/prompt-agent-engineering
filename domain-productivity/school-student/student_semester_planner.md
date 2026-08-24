---
title: "Semester Planner"
category: productivity/school-student
description: "Map the full academic semester — major assignments, exams, high-load weeks, and low-intensity windows — so the student can see the terrain and make better time decisions."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-08
  - QA-01
  - OC-06
difficulty: intermediate
tags:
  - semester
  - planning
  - academic-calendar
  - time-management
  - strategic
updated: "2026-05-12"
related_prompts:
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/deep-work/deepwork_chunk_project_to_calendar.md
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-productivity/reviews/reviews_monthly_quarterly_cadence.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Semester Planner

**Objective:** At the start of a semester, build a strategic map of the academic calendar — identifying high-load weeks, dead zones, and the semester's highest-stakes deliverables — so the student can make informed decisions throughout, not panic-driven ones.

**When to use:** Within the first 1–2 weeks of a semester, when syllabi are available. Also useful mid-semester when the student realizes they have lost sight of the full calendar. Not a day-by-day schedule — a strategic terrain map.

**Audience:** Undergraduate and graduate students taking multiple courses simultaneously. Also useful for high school students in AP or honors tracks with significant independent project loads. Not designed for a single-course plan (use `student_study_schedule_builder.md` for that).

---

## Inputs Required

1. **Semester dates.** Start date, end date, and any official breaks (spring break, fall reading week, holidays).

2. **Course list with major deliverables.** For each course, provide:
   - Course name
   - Major assignments with due dates and rough weight (% of grade if known)
   - Exam dates (midterm, final, any additional exams)
   - Weekly or recurring obligations (participation, weekly problem sets, lab reports)

3. **Extracurricular or work commitments.** Regular time blocks consumed by non-academic obligations. Example: "Work 20 hrs/week (Mon/Wed/Fri), club meetings Tuesdays 6–8 PM."

4. **Known personal events.** Trips, family obligations, medical appointments, or any week you know in advance will be disrupted.

---

## Instructions

### Step 1 — Build the full deliverables calendar

Collect every dated deliverable across all courses onto a single timeline. Include:
- Major assignments and their weights
- Exam dates
- Recurring weekly obligations (count their time cost per week, not per instance)

Sort chronologically. Flag any week with 3 or more due dates or exams.

### Step 2 — Identify load levels

Classify each week of the semester into one of three load levels:

- **High load** (red): 3+ major deadlines or exams; OR a single very high-stakes deliverable (final paper, capstone exam) combined with at least one other deadline; OR a week following a break where catch-up is required
- **Medium load** (yellow): 1–2 moderate deadlines; normal weekly obligation volume
- **Low load / recovery** (green): No major deadlines; typically early semester weeks, post-break weeks with nothing due, or late semester after finals

Produce a week-by-week load level table for the entire semester.

### Step 3 — Identify high-load clusters

Flag any stretch of 2+ consecutive high-load weeks. These are danger zones where students are most likely to fall behind, make poor time decisions, or burn out. Name them explicitly: "Weeks 7–9 are a high-load cluster: Econ midterm, History paper, and Bio lab report all land within 10 days."

### Step 4 — Identify work-ahead windows

For each high-load week, identify the preceding low or medium week(s) where the student could front-load work. Name what specifically should be started early:
- Example: "Week 5 (low load) is the ideal time to begin research for the Week 7 History paper."
- Example: "Spring break falls 2 weeks before the Week 11 finals cluster — this is the primary work-ahead window."

### Step 5 — Rank the semester's top deliverables

Identify the 3–5 highest-stakes assignments or exams for the semester, weighted by their grade impact and difficulty. These are the deliverables the student must protect against schedule slippage:
- Rank by: weight × difficulty (self-estimated), not due date
- Label the single most important deliverable clearly

### Step 6 — Produce the semester map

Output the full map using the format below: month-by-month overview, load levels, flagged clusters, work-ahead windows, and top-deliverable ranking.

---

## Constraints

### Must
- Cover the entire semester, not just the next few weeks
- Classify every week with a load level
- Flag high-load clusters (2+ consecutive high-load weeks) explicitly
- Identify work-ahead windows before each high-load week
- Rank the semester's top 3–5 deliverables by stakes, not chronology
- Note official breaks and how they interact with surrounding deadlines

### Must Not
- Produce a day-by-day schedule — this is a strategic map, not a calendar
- Treat all assignments as equal weight regardless of grade percentage
- Ignore recurring weekly obligations when calculating load level
- Flag every week as "high load" — the classification is relative and meaningful only if differentiated
- Add generic time-management advice not grounded in the student's specific calendar

---

## False-Positive Prevention

1. **Load level inflation:** If everything is "high load," the classification is meaningless. A typical semester has 3–5 genuinely high-load weeks, not 12. Weeks with only one small assignment are medium or low.

2. **Break treated as a safe zone without context:** Spring break immediately before a finals cluster is not a recovery period — it is a work-ahead window. Note what is due in the two weeks following any break.

3. **Weight blindness:** A 10% quiz and a 40% final paper are not equally important even if they are due on the same day. Grade weight should influence the stakes ranking in Step 5.

4. **Recurring obligations underestimated:** Weekly problem sets or lab reports that take 2–3 hours each are a constant load that compounds during high-deadline weeks. They must be counted in load-level calculations, not ignored.

5. **No post-map action:** A semester map with no work-ahead recommendations is just a calendar. The value is in identifying what to start early and when — include that explicitly.

---

## Output Format

```
SEMESTER MAP — [Semester] [Year]
[Start date] → [End date]

TOP DELIVERABLES (by stakes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#1 — [Assignment/Exam] — [Course] — Due: [Date] — Weight: [X%] — Difficulty: [H/M/L]
#2 — [Assignment/Exam] — [Course] — Due: [Date] — Weight: [X%]
#3 — ...
#4 — ...
#5 — ...

MONTH-BY-MONTH OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Month]
  Week [N] ([Dates]): [LOAD: HIGH | MEDIUM | LOW]
    Deadlines: [List]
    Notes: [Work-ahead target | High-load cluster | Post-break | etc.]

  Week [N] ([Dates]): [LOAD]
    Deadlines: [List]
    ...

HIGH-LOAD CLUSTERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠ Cluster 1: Weeks [N–N] ([Dates])
  What lands: [List of deadlines]
  Work-ahead window: [Week N — start X by this date]
  Risk: [What breaks down if you don't prepare early]

⚠ Cluster 2: Weeks [N–N]
  ...

BREAK INTERACTION ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Break name] ([Dates]):
  What follows within 2 weeks: [Deadlines]
  Recommended use of break: [Work-ahead on X | Recovery | Both]

WEEK-BY-WEEK LOAD SUMMARY (full semester)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wk 1  [Date range]: [LOW / MEDIUM / HIGH] — [Brief note]
Wk 2  [Date range]: [LOW / MEDIUM / HIGH] — [...]
...
```

---

## Verification

- [ ] Every week of the semester has a load classification
- [ ] Load classifications are differentiated — not all medium or all high
- [ ] High-load clusters (2+ consecutive high weeks) are named and flagged
- [ ] A work-ahead window is identified before each high-load cluster
- [ ] Top 3–5 deliverables are ranked by stakes (weight × difficulty), not due date
- [ ] Official breaks are analyzed in context of surrounding deadlines
- [ ] Recurring weekly obligations are reflected in load-level calculations
- [ ] Output is a strategic map, not a day-by-day schedule
