---
title: "Personal Tracking Dashboard"
category: productivity/goals-habits
description: "Design a minimal tracking system for goals and habits — produces a simple template and weekly review protocol adaptable to any tool."
techniques:
  - ST-01
  - DS-01
  - DS-02
  - CM-02
  - QA-01
  - OC-06
difficulty: beginner
tags:
  - tracking
  - habits
  - goals
  - weekly-review
  - system-design
updated: "2026-05-12"
related_prompts:
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-productivity/goals-habits/goals_habit_stack_designer.md
  - domain-productivity/goals-habits/goals_monthly_progress_check_in.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
---

# Personal Tracking Dashboard

**Objective:** Design a minimal, tool-agnostic tracking system for monitoring progress on goals and habits. Produces a specific tracking template (rows, columns, and what goes in each) plus a weekly review protocol that takes 10 minutes or less. The deliverable is the system design — not a recommendation to buy software.

**When to use:** When someone wants to track goals or habits but doesn't have a working system, or when a previous tracking system collapsed under its own complexity. Also useful when someone is starting `goals_annual_goal_breakdown.md` or `goals_habit_stack_designer.md` and needs a lightweight way to track the results.

**Audience:** Anyone who wants a simple, sustainable tracking system they can actually maintain. Not for teams or shared project tracking. Not for people who need sophisticated analytics or data integration — this is a personal, minimal system designed for human use.

---

## Inputs Required

1. **What you want to track.** List up to 7 items: goals (progress milestones), habits (did-it-or-didn't), or metrics (a number to record). If more than 7 are listed, you will be asked to cut. More than 7 items is a tracking failure, not a tracking strategy.
2. **Preferred format.** Paper (notebook, bullet journal, printed sheet), digital spreadsheet, a notes app, or no preference. This affects the template design.
3. **Time budget for tracking per week.** How many minutes are you willing to spend on tracking and review — 5 minutes, 10 minutes, or 20 minutes? The system will be sized to fit the stated budget.
4. **Previous tracking systems you've tried and why they abandoned them.** What collapsed? Too many fields? Too complex to maintain during travel? Required opening too many apps? Daily check-ins that turned into weekly catch-up sessions that then stopped entirely? This history directly shapes the constraints for the new system.

---

## Instructions

### Step 1 — Gate: Cut items above 7
If more than 7 tracking items are listed, stop: "You have listed [N] items. Tracking more than 7 simultaneously collapses most systems. Which 7 matter most right now? Drop the rest — you can add them later if the system proves sustainable."

Do not proceed until the list is 7 or fewer.

### Step 2 — Categorize items
Sort the submitted tracking items into three types:

- **Habit (binary):** Did it happen or not? Yes/No, checkmark, or dot. These need no more than a cell or box per day.
- **Goal progress (milestone):** A periodic check-in — not daily. Weekly or monthly, depending on the goal's pace.
- **Metric (number):** A specific number to record — weight, pages written, minutes exercised, revenue. These need a number field, not a checkbox.

Different item types have different tracking frequencies. Not everything should be tracked daily. Milestones should be checked weekly or monthly; daily metric tracking is only justified if the metric changes daily and daily data is actually useful.

### Step 3 — Design the tracking template

Produce a specific template structure:

**Format constraints:**
- One view (one page, one sheet, one note) — not a system of linked views
- Review must be completable within the stated time budget
- The design must be simpler than whatever the user abandoned previously

**Template structure:**
- Rows: the items being tracked (habits, goals, metrics)
- Columns: the time periods (days of the week for habits, weeks for goals/milestones)
- Intersections: what gets recorded (checkmark, number, brief text)

For paper format: specify physical layout, page orientation (landscape often works better), and whether to print or hand-draw.

For digital format: specify the exact grid structure — number of columns, column headers, what each cell holds. Keep it simple enough to enter in under 30 seconds per item per day.

### Step 4 — Design the weekly review protocol
Produce 3–4 questions to answer from the tracking data at the end of each week. These replace a generic "weekly review" with specific, data-grounded questions. The review should take the stated time budget or less.

The questions must be answerable from the data in the template — not from memory or additional review. If the template doesn't capture data needed to answer a question, revise the template.

Standard question structure:
1. **Completion rate:** Which habits ran this week? What was the hit rate for each?
2. **Progress signal:** For goal milestones, am I on track for the period milestone?
3. **Friction flag:** What was hardest to do, or what did I skip most? Is this a data point or a pattern?
4. **One forward-looking decision:** Based on the data, is there anything to change, drop, or add next week?

### Step 5 — Anti-complexity check
Before finalizing the design, check it against the constraints derived from the user's stated failure history:

- If they abandoned a previous system because it was too many fields: count the fields in the new design. If it has more fields than what they abandoned, redesign.
- If they abandoned it because daily entry became a catch-up burden: ensure the new design allows for a missed day without requiring backfill — binary habits can be left blank for a missed day without the system breaking.
- If they abandoned it because it required too many tools or app-opens: count the number of tools required. The new design should require one (a notebook or one app).

---

## Constraints

### Must
- Require cutting the item list to 7 or fewer before proceeding
- Produce a concrete template (rows × columns × cell contents) — not a description of a template
- Size the system to fit the stated time budget
- Make the new system demonstrably simpler than whatever the user abandoned
- Include a weekly review protocol with questions answerable from the template data

### Must Not
- Recommend a specific app or software as the deliverable — the deliverable is the system design
- Design a system that requires daily entry for milestone-tracked goals (milestones don't change daily)
- Include more tracking fields than what the user had in their last abandoned system
- Produce a "template" that is actually a description of what to think about rather than a concrete grid
- Suggest adding items to the tracker beyond what the user listed — the goal is minimal, not comprehensive

---

## False-Positive Prevention

1. **Template that is a description, not a template:** A common failure — producing paragraphs about what to track rather than an actual fillable structure. The output must include a literal grid or table the user can copy and use immediately.
2. **App recommendation as the answer:** The question is system design, not tool selection. Recommending Notion or Habitica is not a deliverable — the user needs the design they would implement in any tool.
3. **Daily check-in for milestone goals:** Milestones don't change daily. Requiring daily entry for a quarterly goal creates friction and empty fields that signal failure — both cause system abandonment. Match tracking frequency to the pace of change.
4. **Complexity creep:** Designing a system with 12 items when the user asked for 7, or adding a monthly view when the user said they want 5 minutes a week. The design must stay within stated constraints.
5. **History-ignorant design:** Producing a daily entry system for someone who said their last system failed because daily entry became a catch-up burden. The design must explicitly address the failure mode from the user's history.

---

## Output Format

```
PERSONAL TRACKING DASHBOARD DESIGN
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRACKING ITEMS ([N] total)

  Habits (binary, daily):
    - [Habit 1]
    - [Habit 2]

  Goal milestones (check weekly or monthly):
    - [Goal 1] — check: [weekly / monthly]

  Metrics (record a number):
    - [Metric 1] — frequency: [daily / weekly]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TEMPLATE DESIGN
Format: [Paper / Spreadsheet / Notes app]
Time budget: [N] min/week

WEEKLY HABIT TRACKER (copy this grid)

         | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Hit Rate
---------|-----|-----|-----|-----|-----|-----|-----|----------
[Habit 1]|     |     |     |     |     |     |     |  /7
[Habit 2]|     |     |     |     |     |     |     |  /7
[Metric] |     |     |     |     |     |     |     | avg:

GOAL MILESTONE CHECK (check [weekly/monthly])

| Goal            | Milestone Due | On Track? | Notes |
|-----------------|---------------|-----------|-------|
| [Goal 1]        | [Date]        | Y / N     |       |

Instructions:
- [Format-specific instructions — e.g., for paper: "Use landscape orientation, one page per week, 
  draw the grid in 2 minutes on Sunday night"]
- [For digital: "One tab or one note — do not create separate sheets per goal"]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEEKLY REVIEW PROTOCOL ([N] min)

Answer these 4 questions from your tracking data — not from memory:

  1. Completion: Which habits ran ≥5/7 days? Which ran <5/7?
  2. Progress: For each goal, is milestone tracking on schedule? (Y/N — no narrative needed)
  3. Friction: What did I skip most or find hardest to enter? One pattern only.
  4. Adjustment: Based on the data, is there one thing to change, drop, or add next week?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPLEXITY CHECK

Previous system abandoned because: [User's stated reason]
This design addresses that by: [Specific design decision that prevents the same failure]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Verification

- [ ] Item list was cut to 7 or fewer before proceeding
- [ ] Template is a concrete fillable structure (grid/table), not a description
- [ ] Tracking frequency matches the pace of change for each item type (habits daily, milestones weekly/monthly)
- [ ] Weekly review protocol contains questions answerable directly from the template data
- [ ] Review time fits within stated time budget
- [ ] The design is demonstrably simpler than whatever the user previously abandoned
- [ ] No specific app or software was recommended as the primary deliverable
- [ ] No items were added to the tracker beyond what the user listed
