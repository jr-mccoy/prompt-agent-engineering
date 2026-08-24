---
title: "Goal Reality Check"
category: productivity/goals-habits
description: "Test a goal against available time, existing commitments, and competing priorities before committing to it — produces a pursue/scale/defer/drop recommendation."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-01
  - QA-19
  - RT-09
difficulty: intermediate
tags:
  - goals
  - feasibility
  - planning
  - tradeoffs
  - prioritization
updated: "2026-05-12"
related_prompts:
  - domain-productivity/goals-habits/goals_annual_goal_breakdown.md
  - domain-productivity/goals-habits/goals_monthly_progress_check_in.md
  - domain-productivity/bottlenecks/bottleneck_locator.md
  - domain-productivity/bottlenecks/bottleneck_perfectionism_ship_threshold.md
  - domain-personal-development/prompts/identity/identity_purpose_reignition.md
---

# Goal Reality Check

**Objective:** Before committing to a goal, run it through a structured feasibility test. Compares the goal's real time requirements against available capacity, identifies what gets displaced, and returns one of four outputs: pursue as-stated, pursue a scaled version, defer, or drop with reason.

**When to use:** Before adding a new goal to an already-active list, or when a goal that felt exciting in your head starts feeling impossible when you look at your actual week. Also useful when someone else has assigned you a goal and you need an honest read on whether it's achievable.

**Audience:** Anyone considering committing to a significant new goal — career, creative, health, financial, or personal. Not for trivial tasks or short-duration projects under two weeks. Not for team goal-setting or organizational planning — this is a personal capacity tool.

---

## Inputs Required

1. **The goal.** State it in one sentence. If it takes more than one sentence, it may be multiple goals — in which case, pick the most important one and run this prompt for each separately.
2. **Why it matters now.** What is the specific reason this goal has priority at this moment? If the answer is vague ("I've always wanted to do this") or social pressure ("I feel like I should"), that's relevant to the feasibility assessment.
3. **What "done" looks like in concrete terms.** An observable, falsifiable end state. Not a feeling, not a direction. If you can't define done, stop here — the goal isn't ready to be assessed.
4. **Estimated time required per week.** Your estimate. This will be challenged.
5. **Current weekly discretionary hours.** Total hours in a typical week that are not already committed to: work, sleep, family obligations, existing commitments, and maintenance activities (commuting, meals, errands). Be honest — this number is almost always smaller than people think.
6. **What would have to give.** If this goal is added, what currently gets less time, money, or attention? Be specific. "Something would have to give" is not an answer.

---

## Instructions

### Step 1 — Gate: Verify "done" is concrete
If the goal's definition of done is vague (a feeling, a quality, a direction), stop: "Before assessing feasibility, I need a concrete definition of done. By [target date], what specific, observable thing will be true that is not true today?"

Do not proceed until done is concrete and falsifiable.

### Step 2 — Challenge the time estimate
Apply a 2–3x adjustment to the user's stated time estimate. Research on planning and self-assessment consistently shows people underestimate effort for novel goals. State this directly:

"Your estimate is [X] hours/week. Based on consistent patterns of underestimation, the realistic range is [2X–3X] hours/week. Does [2X] hours/week feel impossible, challenging but feasible, or comfortable?"

If the user confirms a higher number, use that. If they insist on the original lower estimate without reasoning, note the disagreement in the output and run the analysis on both the stated estimate and the adjusted estimate.

### Step 3 — Assess available capacity
Compare the adjusted time estimate to stated discretionary hours:

- **Surplus (adjusted estimate ≤ 80% of discretionary hours):** Time is available. Proceed to displacement check.
- **Tight (adjusted estimate = 80–100% of discretionary hours):** Technically possible, but zero buffer. Any disruption (illness, urgent work, family demands) breaks the goal. Flag this explicitly.
- **Over capacity (adjusted estimate > discretionary hours):** The goal cannot be pursued as-stated at the current time. Do not proceed without addressing this.

### Step 4 — Displacement check
Ask: what currently happens in those hours? What gets less time, focus, or attention if this goal is added? Force a specific answer. Acceptable answers: "I reduce time spent on [specific activity]" or "I stop doing [specific commitment]." Not acceptable: "I'll find the time."

If the displacement is a previously committed goal or a relationship, flag this as a significant tradeoff — not just a scheduling preference.

### Step 5 — Return a recommendation
Based on Steps 2–4, return exactly one of the following:

**PURSUE AS-STATED:** Time is available, displacement is acceptable, definition of done is clear. Recommend proceeding and moving to `goals_annual_goal_breakdown.md` for milestone planning.

**PURSUE SCALED VERSION:** The goal is right but the scope or timeline is too aggressive for current capacity. Produce a specific scaled version: reduced scope, extended timeline, or reduced weekly commitment. The scaled version must be specific — not "do less of it" but "complete [specific deliverable] by [date] at [X hours/week]."

**DEFER:** The goal is right, the scope is right, but this is the wrong time — either existing commitments take priority, or a near-term change (project ending, schedule shift) will free capacity. Recommend a specific future trigger for revisiting: "Revisit this goal when [specific condition] — estimate [timeframe]."

**DROP:** The goal is either not achievable at any realistic scope given life circumstances, or the "why it matters now" doesn't hold up under scrutiny. State the specific reason for dropping. Dropping is not failure — it is accurate prioritization.

---

## Constraints

### Must
- Challenge every stated time estimate — accept the user's higher number if they revise, but never accept an unchallenged low estimate
- Force specificity on the displacement question — "I'll find the time" is not an answer
- Return exactly one of the four recommendations (pursue/scale/defer/drop)
- If scaling is recommended, provide a concrete scaled version, not a vague directive
- If deferring, name a specific trigger condition, not just "later"

### Must Not
- Validate every goal just because the user wants it — the purpose of this prompt is honest friction
- Accept a vague definition of done and proceed anyway
- Return a hedged recommendation ("it depends" or "maybe try it and see")
- Motivate or encourage — return an accurate feasibility assessment, not a pep talk
- Suggest the user "just prioritize better" without specifying what gets deprioritized

---

## False-Positive Prevention

1. **Underestimate acceptance:** The most common false positive — accepting the user's stated time estimate without challenge, leading to a feasibility assessment that is optimistic by 2–3x. Always apply the adjustment and state it explicitly.
2. **Aspirational displacement:** Accepting "I'll watch less TV" as displacement without asking: is that actually where the time is going? If the user is already watching minimal TV, this isn't real capacity.
3. **False surplus:** A stated discretionary hours budget that doesn't account for recovery time, family demands, or irregular but frequent obligations (quarterly tax prep, seasonal work spikes, recurring medical appointments). Push for a realistic weekly number, not a best-case-week number.
4. **Vague scaled version:** Recommending "a scaled version" without specifying what it is. A scale recommendation must name the exact scope, deliverable, and timeline — otherwise it provides no actionable guidance.
5. **Deferred without trigger:** Recommending deferral without a specific trigger condition is not a deferral — it is a polite way of not deciding. Every deferral must have a named trigger.

---

## Output Format

```
GOAL REALITY CHECK
Goal: [Stated goal]
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FEASIBILITY ANALYSIS

Definition of done:     [Concrete observable end state]
Why it matters now:     [User's stated reason — and whether it holds up]

Time estimate (stated): [X] hrs/week
Time estimate (adjusted, 2–3x): [Y–Z] hrs/week
Discretionary hours available: [N] hrs/week
Capacity status: [Surplus / Tight / Over capacity]

What gets displaced:    [Specific named activities or commitments]
Displacement severity:  [Minor (low-stakes activity) / Significant (committed goal or relationship)]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMMENDATION

▶ [PURSUE AS-STATED / PURSUE SCALED VERSION / DEFER / DROP]

Reason: [Specific rationale — not generic]

[If PURSUE AS-STATED:]
  Next step: Run goals_annual_goal_breakdown.md to build milestones.

[If PURSUE SCALED VERSION:]
  Scaled version: [Specific reduced scope, deliverable, and timeline]
  Commitment required: [X] hrs/week

[If DEFER:]
  Trigger condition: [Specific named event or circumstance to revisit]
  Estimated revisit window: [Timeframe]

[If DROP:]
  Specific reason: [Why this goal doesn't hold up — not-achievable / wrong-time / wrong-goal]
  Optional: [What this goal would need before it becomes viable, if anything]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Verification

- [ ] Definition of done is concrete and falsifiable before proceeding
- [ ] Time estimate was challenged and adjusted — not accepted at face value
- [ ] Capacity assessment compares adjusted (not stated) estimate to available hours
- [ ] Displacement is specific — named activities, not "I'll find the time"
- [ ] Exactly one recommendation is returned (not hedged)
- [ ] Scaled versions are concrete: specific scope, deliverable, and timeline
- [ ] Deferrals name a specific trigger condition
- [ ] No motivational content or encouragement in the output
