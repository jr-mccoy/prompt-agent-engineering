---
title: "Annual Goal Breakdown"
category: productivity/goals-habits
description: "Decompose annual goals into quarterly milestones, monthly targets, and weekly minimum viable actions."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-02
  - QA-01
  - QA-19
difficulty: intermediate
tags:
  - goals
  - planning
  - annual-review
  - milestones
  - time-horizons
updated: "2026-05-12"
related_prompts:
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-productivity/reviews/reviews_monthly_quarterly_cadence.md
  - domain-productivity/goals-habits/goals_monthly_progress_check_in.md
  - domain-productivity/goals-habits/goals_goal_reality_check.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
---

# Annual Goal Breakdown

**Objective:** Take a set of annual goals and break each one into quarterly milestones, a monthly commitment for the current month, and a weekly minimum viable action. Converts aspirational statements into a structure that can survive contact with a real calendar.

**When to use:** At the start of a year, quarter, or any time you have a list of annual goals that feel real in your head but have no concrete plan attached to them. Also useful mid-year when goals have drifted.

**Audience:** Individuals with 1–5 active annual goals who want to move from intention to scheduled action. Not for project managers tracking team OKRs (use a project management tool). Not for anyone who has more than 5 goals — the first task will be cutting the list.

---

## Inputs Required

1. **Your annual goals (up to 5).** List each goal in one sentence. If you have more than 5, you must cut before proceeding — this prompt will not process more than 5. More than 5 goals is a planning failure, not a planning strategy.
2. **What "done by year-end" looks like for each goal.** Not a feeling — a concrete observable outcome. "I feel healthier" is not acceptable. "I run a 5K in under 30 minutes by December 31" is.
3. **Known obstacles or risks for each goal.** What has blocked this goal before, or what predictably will? Travel, busy seasons, financial constraints, dependencies on others.
4. **Resources available.** For each goal: how many hours per week you can realistically allocate, any budget, and who (if anyone) is supporting you.
5. **Current month and quarter.** So milestones can be anchored to actual calendar dates.

---

## Instructions

### Step 1 — Gate: Cut goals above 5
If the user lists more than 5 goals, stop and present this: "You have listed [N] goals. Pursuing more than 5 annual goals simultaneously is statistically correlated with completing zero. Which 5 matter most this year? Drop the rest — not forever, just from this year's plan."

Do not proceed until the list is 5 or fewer.

### Step 2 — Gate: Challenge vague year-end definitions
For any goal where the year-end definition is vague (feelings, directions, qualities rather than observable outcomes), issue a direct challenge before proceeding:

"Your year-end definition for '[goal]' is vague: '[their definition]'. Vague definitions can't be milestoned. Complete this sentence: By December 31, I will have [specific observable output or behavior]. What is it?"

Do not generate milestones for a goal until it has a concrete year-end definition.

### Step 3 — Conflict check
Before building the breakdown, scan all goals together for conflicts:
- **Time/energy competition:** Which goals compete for the same hours or mental bandwidth?
- **Sequencing requirements:** Does goal B depend on goal A being partially complete first?
- **Identity conflicts:** Do any goals require contradictory lifestyle or behavioral patterns?

Flag any conflicts explicitly. Do not suppress them to appear agreeable.

### Step 4 — Build the breakdown for each goal
For each goal, produce:

**Q1/Q2/Q3/Q4 milestones:** Each milestone is a specific, verifiable checkpoint — not "make progress." It should be falsifiable: either you hit it or you didn't. Milestones should be proportional to the actual work curve of the goal (if most of the work happens in Q3, the Q3 milestone should reflect that — don't space milestones evenly if the work isn't evenly spaced).

**Monthly commitment (current month only):** One specific, concrete action for this month. Not a mindset. Not a category of activity. One action with a defined output.

**Weekly minimum viable action (MVA):** The smallest action that still counts as progress — the floor, not the ceiling. This is what gets done even in a bad week. It should take no more than 30 minutes. If you can't define a 30-minute weekly action, the goal lacks a clear next step and needs to be re-examined.

### Step 5 — Surface the tradeoffs
After building all breakdowns, add a Conflicts and Tradeoffs section. For each conflict identified in Step 3, state clearly what the user is choosing between and what the practical implication is. Do not resolve the conflict for them — present it so they can make an informed choice.

---

## Constraints

### Must
- Challenge vague year-end definitions before proceeding
- Refuse to process more than 5 goals without the user cutting
- Flag goal conflicts explicitly
- Produce milestones that are verifiable, not directional
- Distinguish between the monthly commitment (current month, specific) and the MVA (weekly floor, always available)

### Must Not
- Generate milestones that are equally spaced if the work isn't equally distributed
- Accept "make progress on X" as a milestone
- Produce more than one monthly commitment per goal (the point is focus)
- Offer motivational commentary — be a planning tool, not a coach

---

## False-Positive Prevention

1. **Evenly spaced milestones that don't reflect actual work curves:** A goal with a learning curve up front and execution later will have light Q1 milestones and heavy Q3 milestones — that's correct. Don't smooth this out artificially.
2. **Milestone inflation:** A Q2 milestone that says "have been doing X consistently for 6 weeks" is not a milestone — it's a habit. Milestones are outputs, not processes.
3. **MVA that requires a good week:** If the minimum viable action requires motivation, energy, or more than 30 minutes, it's not the minimum — it's the standard. Force it lower.
4. **Conflict suppression:** If two goals genuinely compete for the same 10 hours of discretionary time per week, this is a real problem. Don't paper over it with "it'll be challenging but doable."
5. **Year-end definition drift:** If the user gives a vague definition and then gives a concrete answer when challenged, use the concrete answer — don't keep both.

---

## Output Format

```
ANNUAL GOAL BREAKDOWN — [Year]
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GOAL 1: [Goal title]
Year-end definition: [Concrete observable outcome]
Resources: [Hours/week] hrs/week | Budget: [Amount or none] | Support: [Names or none]

MILESTONES
  Q1 (by [Date]): [Specific verifiable checkpoint]
  Q2 (by [Date]): [Specific verifiable checkpoint]
  Q3 (by [Date]): [Specific verifiable checkpoint]
  Q4 (by [Date]): [Year-end definition — same as above]

THIS MONTH ([Month Year])
  Commitment: [One specific action with defined output]

WEEKLY MINIMUM VIABLE ACTION
  MVA: [Specific action, ≤30 min, executable even in a bad week]

Known risks: [Obstacles flagged by user]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

GOAL 2: [Goal title]
[Same structure]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONFLICTS AND TRADEOFFS

[Conflict 1 — e.g., Goals 1 and 3 compete for evenings]
  What's at stake: [Description of the tension]
  Decision required: [What the user must choose between]

[Conflict 2 — if any]
  ...

No conflicts detected: [If none, say so explicitly]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Verification

- [ ] All goals have a concrete, falsifiable year-end definition (not a feeling or direction)
- [ ] No more than 5 goals were processed without cutting
- [ ] Each Q milestone is verifiable — it either happened or it didn't
- [ ] Milestones reflect the actual work distribution of the goal, not equal spacing
- [ ] Each goal has exactly one monthly commitment for the current month
- [ ] Each MVA is executable in ≤30 minutes during a bad week
- [ ] All conflicts between goals are surfaced, not suppressed
- [ ] No motivational commentary or coaching was added
