---
title: "Goal Setting and Reflection Loop"
category: personal-development
description: "Regular goal review and adjustment — honestly assess progress, identify what's working and what isn't, celebrate wins, adjust goals based on new information, and produce an updated action plan"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - QA-01
  - QA-20
difficulty: beginner
tags:
  - personal-development
  - goal-setting
  - reflection
  - review
  - accountability
  - habits
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/goals/goals_goal_system_designer.md
  - domain-personal-development/prompts/thinking/thinking_blind_spot_mirror_see_what_im_missing.md
  - domain-personal-development/prompts/agency/agency_weekly_review.md
---

# Goal Setting and Reflection Loop

**Objective:** Run a structured review of your current goals — honestly assess progress, identify what's working and what isn't, adjust goals based on new information, and produce an updated action plan for the next period.

## When to Use

- Use when: you already have an **existing goal system** and need to review/adjust it — weekly (quick 10-minute), monthly (full 30-minute), or quarterly (comprehensive).
- Use when: goals feel stale, you've been avoiding your tracker, or circumstances have changed and the plan needs to flex.
- **Use this over its sibling `goals_goal_system_designer.md` when** goals already exist and the job is *reflect-and-adjust* (the ongoing loop). Use `goals_goal_system_designer.md` instead when you are *creating* the system from scratch — turning raw aspirations into SMART goals, trackers, and rituals for the first time.
- Don't use when: you're decomposing a single skill into a practice path — use `goals_skill_breakdown_blueprint.md` or `goals_decompose_learning_task.md`.

---

## Inputs / Context

1. **Current Goals:** [List your active goals with their metrics and deadlines]
2. **Time Since Last Review:** [When did you last review these goals?]
3. **What Happened:** [Brief summary of progress, setbacks, and surprises since last review]
4. **How You Feel:** [Energized? Overwhelmed? Bored? Guilty? Be honest.]

**Refusal / insufficiency logic:** This prompt reviews goals that already exist — if no current goals are supplied, do not invent them; redirect the user to `goals_goal_system_designer.md` to create the system first. If goals are listed but **without metrics or deadlines** (e.g. "get fit," "grow the business"), flag that they cannot be honestly assessed as on-track/behind, and ask the user to attach a measurable target before producing a progress dashboard. Do not fabricate progress numbers the user did not provide.

---

## Instructions

### Phase 1: Progress Check

For each active goal:

| Goal | Target | Current | On Track? | Blockers |
|------|--------|---------|-----------|----------|
| [Goal 1] | [Metric] | [Where you are] | Yes/Behind/Ahead | [What's in the way] |

### Phase 2: Honest Assessment

Answer these questions without self-judgment:
- **What worked this period?** (Specific actions or habits that moved the needle)
- **What didn't work?** (What you tried that didn't produce results)
- **What did you avoid?** (Tasks you skipped and why — be honest)
- **What surprised you?** (Unexpected progress, setbacks, or insights)
- **What changed?** (New information, shifting priorities, life events)

### Phase 3: Goal Adjustment

For each goal, decide:
- **Keep as-is:** On track, metrics still relevant, motivation intact
- **Adjust:** Change the metric, timeline, or approach based on what you've learned
- **Pause:** Temporarily deprioritize (with a specific resume date)
- **Drop:** Honestly no longer important — remove without guilt

For adjusted goals, specify what changed and why.

### Phase 4: Updated Action Plan

For each active goal (kept or adjusted):
- **Next milestone:** [Specific target for next review period]
- **Key actions this week:** [2-3 specific tasks]
- **Potential blockers:** [What might get in the way]
- **Support needed:** [Help, resources, or accountability]

### Phase 5: Celebrate

Name at least one thing you did well since the last review. Progress is not just hitting targets — showing up and reviewing is itself progress.

---

### False-Positive Prevention

- ❌ Do NOT just add more goals when current ones aren't progressing — diagnose first
- ❌ Do NOT blame yourself for missed goals without examining structural causes
- ❌ Do NOT treat "behind schedule" as failure — circumstances change and timelines should adapt
- ❌ Do NOT skip the celebration step — acknowledging progress prevents burnout
- ❌ Do NOT keep goals you've outgrown out of guilt or sunk cost
- ✅ DO celebrate progress even if incomplete — partial progress is still progress
- ✅ DO adjust goals based on new information — flexibility is strength, not weakness
- ✅ DO examine what you avoided — avoidance patterns reveal important information
- ✅ DO distinguish between "this goal is wrong" and "my approach is wrong"
- ✅ DO set a specific date for the next review before ending this one

---

## Dual-Failure Prevention (QA-20)

Test the review for **both** directions of failure:

❌ **HARMFUL failure (over-optimistic / dishonest):** The review rubber-stamps goals as "on track" to protect the user's feelings, lets a clearly-dead goal linger out of sunk cost, or reframes pure avoidance as "circumstances changed." A useless review tells the user what they want to hear.

❌ **UNHELPFUL failure (harsh / paternalistic):** The review turns into a self-flagellation exercise — moralizing about missed targets, ignoring the celebration step, or demanding the user drop goals they still genuinely want. Excessive "you must be disciplined" hedging makes the user stop running the loop.

✅ **Quality check:** Would a thoughtful coach be comfortable with this review — that it is **honest about what isn't working** (no flattery) AND **non-punitive** (it adjusts structure, names a win, and keeps the user coming back)?

---

## Expected Output

```markdown
# Goal Review: [Date]

## Progress Dashboard
| Goal | Target | Current | Status | Action |
|------|--------|---------|--------|--------|
| ... | ... | ... | On track/Behind/Adjusted/Dropped | ... |

## What I Learned
- Worked: ...
- Didn't work: ...
- Avoided: ...

## Adjusted Goals
- [Goal]: Changed [what] because [why]

## This Week's Focus
1. [Top priority action]
2. [Second action]
3. [Third action]

## Win to Celebrate
[Something you did well]

## Next Review: [Date]
```

---

## Verification

Before delivering the review, confirm each of these. If any fails, fix it before responding:

- [ ] Every supplied goal appears in the progress dashboard with an **honest status** (On track / Behind / Ahead / Adjusted / Dropped) — none are silently dropped or auto-flattered to "on track."
- [ ] Status calls are grounded in the **user's actual metrics/numbers**, not assumed progress.
- [ ] The "What I Learned" section names at least one **avoided** item (avoidance is surfaced, not skipped).
- [ ] Each adjusted goal states **what changed and why** — distinguishing "wrong goal" from "wrong approach."
- [ ] This-week's focus is **≤3 specific actions**, not a re-listing of all goals.
- [ ] The **celebration step is present** (at least one genuine win) and the **next review date is set**.
- [ ] Both dual-failure directions checked: the review is neither flattering nor punitive.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Goal review with adjustment output
- **ST-02** (Structured Sequential Instructions) — Check, assess, adjust, plan, celebrate
- **CM-01** (Explicit Context Framing) — Current goals, progress, and feelings
- **QA-01** (Chain-of-Verification) — Structured review against metrics
- **QA-20** (Dual-Failure Quality Test) — Keeps the review honest about failure without becoming punitive (replaces the prior mislabeled RT-04 "Emotional Intelligence" technique, which no longer maps to this prompt — RT-04 is Analogical Reasoning)

---

## Related Prompts

- [goals_goal_system_designer.md](../goals/goals_goal_system_designer.md) — Sibling: design the initial goal system from raw aspirations (use *before* this loop exists).
- [thinking_blind_spot_mirror_see_what_im_missing.md](../thinking/thinking_blind_spot_mirror_see_what_im_missing.md) — Check what you're missing in your approach.
- [agency_weekly_review.md](../agency/agency_weekly_review.md) — Weekly execution review for agency-focused work (compounding output review).
