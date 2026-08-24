---
title: "Monthly Progress Check-In"
category: productivity/goals-habits
description: "Run a structured progress check-in on active goals, surface on-track vs. off-track status, and produce a specific course-correction plan."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-08
  - QA-01
  - RT-06
difficulty: intermediate
tags:
  - goals
  - progress-review
  - course-correction
  - accountability
  - milestones
updated: "2026-05-12"
related_prompts:
  - domain-productivity/reviews/reviews_monthly_quarterly_cadence.md
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-productivity/goals-habits/goals_annual_goal_breakdown.md
  - domain-productivity/goals-habits/goals_goal_reality_check.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
---

# Monthly Progress Check-In

**Objective:** Run a structured check-in on one or more active goals. Surfaces whether each goal is on track, behind but recoverable, or off track. Produces a specific course-correction recommendation — not a pep talk.

**When to use:** At the end of a month (or week, for shorter-horizon goals) to assess actual progress against stated milestones. Also use at any point when a goal feels stuck or stalled and you want a structured diagnosis rather than vague reassurance.

**Audience:** Anyone actively pursuing one or more goals with defined milestones. Not for people who haven't started a goal yet (use `goals_annual_goal_breakdown.md` first). Not for team or project reviews — this is a personal operating tool.

---

## Inputs Required

1. **Goal(s) and their milestones.** For each goal: the year-end definition and the milestone that was supposed to be hit this period (month, quarter, or week). If no milestone was defined, note that — the check-in will still run but the diagnosis will be harder.
2. **Current status vs. milestone.** For each goal: what did you actually accomplish this period? Be specific. "Made some progress" is not an input — it's a deflection. What is the concrete evidence of progress?
3. **Obstacles encountered.** What got in the way? Specific, named circumstances — not "I got busy." If nothing got in the way and you still didn't hit the milestone, that is its own data point.
4. **Changes in goal importance or feasibility.** Has anything changed since you set this goal — in your life, your priorities, your circumstances — that affects whether this goal still makes sense?

---

## Instructions

### Step 1 — Status assessment for each goal

Assign a status to each goal:

**GREEN — On track:** Progress this period equals or exceeds the milestone. No intervention required. Confirm the next milestone and continue.

**YELLOW — Behind but recoverable:** Progress fell short of the milestone, but the year-end definition is still achievable with a specific change. Requires a catch-up plan, not just renewed intention.

**RED — Off track:** One or more of the following is true:
- Progress this period was significantly below the milestone with no clear diagnosis
- The year-end definition is no longer achievable at the current pace even with effort
- Something has changed that calls the goal's relevance into question

State the status clearly before proceeding. Do not hedge with "mostly on track" — pick green, yellow, or red.

### Step 2 — For GREEN goals
Confirm the next period's milestone. Identify any emerging risks that could flip the goal to yellow next period. Done.

### Step 3 — For YELLOW goals: Catch-up plan
Diagnose the specific failure mode first. Choose one:
- **Execution gap:** The milestone was clear, time was available, but the work didn't happen. Cause: competing priorities, low urgency, procrastination, or unclear next action.
- **Capacity gap:** The milestone was clear, but the time or resources weren't there. The plan assumed more capacity than existed.
- **Clarity gap:** The milestone was vague or the path to it was unclear, so effort was scattered.
- **External block:** Progress depended on something outside the person's control that didn't come through.

Once the failure mode is named, produce a specific catch-up plan: what changes next period, in concrete terms. Not "try harder" — a different strategy, different schedule, reduced scope, or a new approach.

### Step 4 — For RED goals: Decision tree
Run this diagnostic in order:

1. **Is the goal still the right goal?** Has something changed — new information, shifted priorities, life circumstances — that makes this goal less relevant or wrong for now? If yes: recommend suspending or dropping the goal with a clear reason. This is not failure; it's an update.

2. **Is the timeline wrong?** Is the year-end definition still the right target, but the schedule was too aggressive? If yes: produce a revised timeline with specific adjusted milestones. Note: an adjusted timeline is only valid if the new timeline is actually achievable given current pace and capacity.

3. **Is the strategy wrong?** Is the goal still right and the timeline still right, but the approach isn't working? If yes: name the specific strategy that has failed and propose a concrete alternative. "Try harder with the same approach" is not a strategy change.

4. **Has life changed?** Is this goal competing with new circumstances (a health issue, a job change, a family situation) that weren't present when the goal was set? If yes: acknowledge this directly and produce a scope reduction or deferral recommendation.

Do not leave a red goal without a decision. The output must include: diagnose + recommend one of (continue with revised approach, reduce scope, defer, or drop).

### Step 5 — Aggregate view
After running all individual goal check-ins, produce a one-line summary across all goals: how many are green/yellow/red, and whether the overall portfolio is manageable or overloaded. If multiple goals are yellow or red simultaneously, flag portfolio overload — it may be a signal that there are too many active goals, not that the person is failing at each individually.

---

## Constraints

### Must
- Assign a binary-ish status (green/yellow/red) — not a spectrum of hedges
- Name the specific failure mode for yellow and red goals before recommending a fix
- Produce a concrete next-period action for every goal (not just the ones in trouble)
- Run the decision tree for red goals in order — don't skip straight to "try harder"
- Flag portfolio overload if multiple goals are yellow/red simultaneously

### Must Not
- Default to "work harder" as the intervention — diagnose the failure mode first
- Treat a vague status update ("making progress") as sufficient input — push for specifics
- Produce motivational content or encouragement — this is a diagnostic tool
- Leave a red goal without a clear recommendation (continue/revise/defer/drop)
- Accept "life got busy" as a complete obstacle description — press for the specific circumstance

---

## False-Positive Prevention

1. **Status inflation:** Calling a goal "mostly green" when it is objectively behind the milestone. Green means the milestone was hit or exceeded. Anything else is yellow or red.
2. **"Work harder" as course correction:** The most common false positive — diagnosing an execution gap and recommending more effort with the same approach. If the same approach has already failed, the approach needs to change.
3. **Obstacle as excuse:** Accepting "travel" or "busy season" as a complete explanation without asking: was this predictable? Was it in the plan? If it was predictable and not planned for, the planning was the failure, not the obstacle.
4. **Portfolio blindness:** Running each goal's check-in in isolation and missing that three yellow goals simultaneously signals a capacity or prioritization problem — not three separate goal problems.
5. **Timeline adjustment as wishful revision:** Proposing an adjusted timeline for a red goal that is not actually achievable given the current pace. A timeline revision is only valid if it is grounded in a realistic assessment of future capacity.

---

## Output Format

```
MONTHLY PROGRESS CHECK-IN
Period: [Month/Week/Quarter reviewed]
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GOAL 1: [Goal name]
Status: 🟢 GREEN / 🟡 YELLOW / 🔴 RED

Milestone this period:   [What was supposed to happen]
Actual progress:         [What actually happened]
Gap (if any):            [Concrete description of shortfall]

[If GREEN:]
  Next milestone: [Specific verifiable checkpoint for next period]
  Emerging risks: [Any threats to staying green]

[If YELLOW:]
  Failure mode:   [Execution gap / Capacity gap / Clarity gap / External block]
  Catch-up plan:  [Specific change for next period — not "try harder"]
  Next milestone: [Adjusted or confirmed checkpoint]

[If RED:]
  Diagnosis:      [Which decision-tree branch applies and why]
  Recommendation: [Continue with revised approach / Reduce scope / Defer / Drop]
  If continuing:  [Specific revised approach, timeline, or scope — with concrete details]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GOAL 2: [Goal name]
[Same structure]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AGGREGATE VIEW

Goals: [N] green / [N] yellow / [N] red

Portfolio status: [Manageable / Overloaded]
[If overloaded:] Portfolio note: [Specific observation — e.g., "3 of 4 goals are yellow simultaneously, suggesting a capacity problem, not 3 separate goal problems. Consider suspending one goal to give the others room."]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Verification

- [ ] Every goal has a clearly assigned status (green/yellow/red) — no hedging
- [ ] Yellow goals have a named failure mode, not just an acknowledgment that progress was slow
- [ ] Red goals went through the full decision tree and have an explicit recommendation
- [ ] "Work harder" does not appear as a course-correction recommendation
- [ ] Portfolio overload is flagged if multiple goals are yellow or red simultaneously
- [ ] Next-period milestones are confirmed or revised for every goal — not just the ones in trouble
- [ ] No motivational content or encouragement was included
