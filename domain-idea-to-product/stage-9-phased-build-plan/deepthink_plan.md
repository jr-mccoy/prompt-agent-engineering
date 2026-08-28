---
title: "Deep-Think: Plan / Strategy"
category: deep-analysis/plan
description: "A multi-phase, multi-perspective planning system for working through how to get from here to there with an AI model at a depth that compensates for the absence of a human team. Drives the model through Frame → Decompose into milestones & dependencies → Multi-perspective → Stress-test → Synthesize, using AskUserQuestion at every gate. Terminal artifact: sequenced plan with risks, checkpoints, and abort conditions."
techniques:
  - ST-01
  - ST-02
  - ST-04
  - ST-42
  - RT-02
  - RT-07
  - CM-02
  - QA-01
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - deep-analysis
  - planning
  - strategy
  - multi-perspective
  - dependencies
  - sequencing
  - askuserquestion
  - gated-workflow
updated: "2026-05-08"
related_prompts:
  - domain-deep-analysis/deepthink_problem_analysis.md
  - domain-deep-analysis/deepthink_decision.md
  - domain-deep-analysis/deepthink_design.md
  - domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md
  - domain-presentations/visual-planning/visualplan_cascade_effects_scan.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Deep-Think: Plan / Strategy

**Objective:** Work through *how to get from here to there* at a depth that would normally require a team. Drive the model through five disciplined phases — Frame, Decompose into milestones and dependencies, Multi-perspective analysis, Stress-test, and Synthesize — pausing at each gate to let the user redirect, prune, or go deeper. Produce a sequenced plan with explicit risks, checkpoints, and abort conditions — not a wishlist, not a roadmap stub.

**When to use:** The user has a goal (or has just decided on one) and needs a plan to execute it. Examples: "How do I migrate this codebase?", "What's the 90-day plan for shipping this feature?", "How do I roll out AI tooling across the team?", "How do I exit this job over six months?". Use this when *sequencing the path* is the goal. If the goal hasn't been chosen yet, run `deepthink_decision.md` first. If the question is "what should we build?", run `deepthink_design.md`.

**Audience:** Solo operators, leads, anyone planning execution one-on-one with an AI and trying to compensate for the missing room of co-planners.

---

## Inputs Required

1. **The goal.** One sentence — what does the end state look like? Use observable terms.
2. **The starting point.** Where are things now, in terms relevant to the goal?
3. **Time horizon and hard deadlines.** Is there a date this must hit? Any internal milestones with external dependencies?
4. **Resources.** People, time-per-week, budget, tools, decision authority. Roughly.
5. **Known constraints.** Anything that's not negotiable (regulatory, contractual, capacity, dependencies on other people).
6. **What's already been tried** (if anything). Useful for avoiding rework.

If items 1–4 are missing, ask before starting Phase 1.

---

## Operating Mode

Inherit the shared deep-think operating model from [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md): run the five phases in order, stop at every gate, use `AskUserQuestion` when available, and fall back to a labeled `**GATE:**` block in plain chat. For plans, use in-phase questions for clarifying scope, prioritizing milestones, surfacing dependencies, confirming risk tolerance, and pruning to real capacity.

---

## Instructions

### Phase 1 — Frame

**Goal:** Make sure we're planning for the right end state and the right starting line.

1. **Restate the goal as an observable end state.** Not "improve X" but "X measurably looks like Y by date Z." If the goal can't be made observable, push back: a plan toward an unobservable goal can't be evaluated.
2. **Surface stated vs. revealed goal.** Stated = what the user said. Revealed = what would actually satisfy them when they got there. Name the gap if there is one — "ship the migration" sometimes hides "stop being blocked by the legacy system."
3. **Right-plan check.** Common reframes:
   - "Plan to do X" often hides "Should X actually be the next thing? Is there a smaller test that would reveal whether X is worth doing?"
   - "How do we ship by date Y?" often hides "Is the deadline real, and if so, what scope cuts are on the table?"
   - "How do I get X done in N weeks?" often hides "Does N weeks of capacity actually exist, given current commitments?"
4. **Capacity reality check.** Compare resources to goal. If the goal is implausible given resources within the time horizon, name it now — don't produce a plan the user will fail to execute.
5. **Scope locking.** Are there parts of the goal the user is willing to drop if needed? Hard requirements vs. nice-to-haves vs. desirable-but-cuttable.

**GATE 1:** Confirm framing, observable goal, capacity check, and scope priorities.

Use `AskUserQuestion`:

```
Question: "Is this the right framing of the goal and the realistic capacity before we plan?"
Options:
- "Yes — proceed with this scope and timeframe"
- "Cut scope — I'll specify what's truly required vs. nice-to-have"
- "Extend timeframe — the deadline is more flexible than I said"
- "Stop — capacity reality check failed; this needs rethinking before planning"
```

---

### Phase 2 — Decompose into Milestones and Dependencies

**Goal:** Break the path into milestones, name dependencies, and surface the critical path.

1. **Backwards from the goal.** Start at the end state and walk backwards. What had to be true the week before? The month before? Generate 4–8 milestones, each one observable.
2. **Forward from the start.** Now walk forwards from where things are now. Do the forward and backward chains meet? If not, there's a gap — name it.
3. **Identify dependencies.** For each milestone, what must be true before it can start? Three categories:
   - **Hard dependencies** (sequential — can't start B until A is done).
   - **Soft dependencies** (parallel-possible but easier sequenced).
   - **External dependencies** (other people, vendors, approvals — outside user control).
4. **Surface the critical path.** Which sequence of milestones determines the total timeline? Anything off the critical path can slip without affecting the date.
5. **Name the load-bearing assumptions.** Which assumptions, if false, blow up the plan? Mark as *tested*, *reasonable*, or *untested-and-load-bearing*.
6. **Capacity allocation.** For each milestone, rough effort estimate. Sum them. Compare to time horizon × weekly capacity. If overcommitted, flag.

**GATE 2:** Confirm milestones, dependencies, and capacity allocation.

Use `AskUserQuestion`:

```
Question: "These are the milestones and the critical path. Anything to adjust?"
Options:
- "Looks right — proceed"
- "Reorder / add / remove a milestone"
- "An external dependency I missed — I'll specify"
- "Capacity is overcommitted — let's cut scope or extend timeline"
```

---

### Phase 3 — Multi-perspective Analysis

**Goal:** Run the plan through perspectives the user couldn't easily generate alone.

#### 3a. Run the mandatory roster (always)

Run the Phase 3 mandatory perspective roster defined in [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md): red team, steel-man, blind-spot scan, future-self, naive newcomer, and affected party. For plans, each lens must include its lens statement, its take on the plan, and the single change or flag it would push for.

#### 3b. Propose scope-specific additions

Use the plan/strategy candidate pool in [`BACKBONE.md`](../../domain-deep-analysis/BACKBONE.md) to propose 2–4 additional perspectives tailored to the user's execution context. Confirm the additions with `AskUserQuestion`/`**GATE:**` and run only the perspectives the user picks.

#### 3c. After running all perspectives

Identify:
- **Convergent risks** — risks multiple perspectives flag. These are the risks most worth pre-mitigating.
- **Productive disagreement** — places perspectives genuinely conflict on sequencing or priority.
- **The one change** — if multiple perspectives push for the same revision, that's a signal.

**GATE 3:** Decide depth.

Use `AskUserQuestion`:

```
Question: "Multi-perspective pass is complete. What to stress-test hardest?"
Options:
- "[Specific risk multiple perspectives flagged]"
- "[The critical path under failure of dependency X]"
- "Capacity assumptions specifically"
- "All of them — full stress-test"
```

---

### Phase 4 — Stress-test

**Goal:** Try to break the plan before the user starts executing.

1. **Pre-mortem.** Imagine: at the deadline, the plan failed. What happened? Generate 3–5 specific failure modes. For each: how would the user know they're in that failure mode by week 2 / month 1 / month 3?
2. **Cascade failure scan.** If milestone N slips by two weeks, what downstream slips? If external dependency D doesn't deliver, what's the minimum-pain workaround?
3. **Adversarial check.** What's the strongest objection a smart, experienced critic would raise to this plan? Steel-man it. Does the plan hold, or does it need revision?
4. **Capacity stress-test.** Re-check capacity assuming 30% slippage in productivity (sickness, surprises, hidden coordination cost). Does the plan still fit?
5. **Abort conditions.** Define 2–4 specific observable conditions under which the user should pull the plug. These are different from tripwires — tripwires say "course-correct," abort conditions say "stop the project entirely."
6. **Confidence calibration.** Rate confidence in: hitting the deadline (high/medium/low), achieving the full scope (high/medium/low), avoiding any abort condition firing (high/medium/low).

**GATE 4:** Decide what makes it into the synthesis.

Use `AskUserQuestion`:

```
Question: "Which stress-test findings should be carried into the plan?"
Options:
- "All of them — full risk register and abort conditions in plan"
- "Bake [specific risk] mitigation into the milestone sequence"
- "Cut scope based on the capacity stress-test"
- "Loop back — Phase 2 needs to add a milestone we missed"
```

---

### Phase 5 — Synthesize

**Goal:** Produce a sequenced plan that an executor (the user, or someone they're handing it to) could pick up and run with. Concrete milestones, named dependencies, observable checkpoints, explicit risks, defined abort conditions.

After producing the synthesis:

**FINAL GATE:** Use `AskUserQuestion`:

```
Question: "Plan is on the table. What's next?"
Options:
- "I'm starting execution — done"
- "Convert to a project tracker / task list"
- "Re-run after [first milestone] to update with what we learn"
- "Loop back — [specific phase] needs another pass"
```

---

## Constraints

### Must
- Run all five phases in order. Never skip Phase 1 (Frame) or Phase 4 (Stress-test).
- Stop at every gate and use `AskUserQuestion` (or labeled `**GATE:**`) before proceeding.
- Run the full core roster of six perspectives.
- Produce an observable end-state in Phase 1. If the goal isn't observable, refuse to plan toward it.
- Surface the critical path explicitly in Phase 2.
- Capacity-check both at Phase 1 (rough) and Phase 4 (with 30% slippage).
- Define abort conditions in Phase 4 — distinct from tripwires.
- Make the plan executable in Phase 5 — concrete milestones with owners (even if owner = user) and dates.

### Must Not
- Generate all five phases in one continuous output.
- Produce a plan toward an unobservable goal. Push back in Phase 1.
- Hand-wave implementation. The implementer perspective in Phase 3 should expose any "and then magic happens" steps.
- Treat external dependencies as soft commitments. If a dependency owner has not committed, the plan must have a contingency.
- Assume linear capacity. Real execution is bursty, with surprises. Phase 4's 30%-slippage check exists for this reason.
- Skip abort conditions. A plan without abort conditions is a sunk-cost factory.
- Pad the plan with "if we have time" milestones. Anything past the deadline isn't in the plan.

---

## False-Positive Prevention

1. **The most common failure is overcommitment.** Plans almost always overestimate capacity. The Phase 1 reality check and Phase 4 30%-slippage check exist to fight this. If a plan fits exactly into available capacity, it's already over capacity.
2. **Critical-path thinking can hide diffuse risk.** A plan with a clean critical path but ten parallel soft dependencies often fails not on the critical path but on a parallel that wasn't watched. Phase 2 should name parallel risks too.
3. **External dependencies are usually wishes.** "X will deliver by Y" is a wish unless X has committed and has skin in the game. Phase 3's dependency-owner perspective surfaces this; the plan must have contingencies for any uncommitted external dependency.
4. **Abort conditions are uncomfortable to write but most valuable when written early.** Writing "we abort if X" before starting is much easier than writing it three months in when X has already been quietly fired.
5. **A plan is not a strategy.** If Phase 1's framing reveals the user hasn't decided what they're trying to achieve, stop and run `/deepthink-decision` first. Planning toward an undecided goal produces wasted output.
6. **"How will we know it's working?" should be answerable at every milestone.** If a milestone has no observable signal, it's not really a milestone — it's a deadline-shaped wish.
7. **Re-planning is normal and the original plan should expect it.** Build in a re-planning checkpoint after the first major milestone. The plan that survives contact with execution unchanged is the plan that wasn't really tested by execution.

---

## Output Format

Use this exact structure for the final plan (Phase 5):

```markdown
## Goal (as confirmed in Phase 1)
[One sentence stating the observable end state and deadline.]

## Starting state
[One or two sentences — where things actually are now, in terms relevant to the goal.]

## Plan summary
[3–5 sentences. The shape of the plan in plain language. What it commits to, what it cuts, what's the spine.]

## Sequenced milestones

### Milestone 1: [Name] — by [Date]
- **Observable signal:** [How will we know this is done? Concrete.]
- **Owner:** [Who is on the hook — even if "user."]
- **Effort estimate:** [Rough.]
- **Dependencies:** [What must be true to start. External dependencies named explicitly.]
- **Risk:** [The biggest thing that could derail this milestone, and the mitigation if any.]

### Milestone 2: [Name] — by [Date]
[...]

[Continue for all milestones — typically 4–8.]

## Critical path
[One or two sentences — the chain of milestones that determines the deadline. What can slip without slipping the deadline; what cannot.]

## Risk register (carried from Phase 4)
- **[Risk 1]** — [likelihood: high/medium/low] — [mitigation built into plan: ...]
- **[Risk 2]** — [...]

## Tripwires (course-correct signals)
- [Observable signal 1] — at week/milestone X — would indicate [problem] — response: [...]
- [Observable signal 2] — [...]

## Abort conditions (stop the plan)
- [Observable condition 1] — would indicate [the project is no longer worth completing as scoped]. If hit, abort or re-scope.
- [Observable condition 2] — [...]

## Capacity & confidence
- **Capacity check:** [Total estimated effort vs. available capacity, including 30% slippage buffer.]
- **Confidence in deadline:** [high / medium / low].
- **Confidence in full scope:** [high / medium / low].
- **What would move confidence:** [specific things the user could do.]

## Re-planning checkpoint
[One sentence: at which milestone should the user pause and re-plan based on what's been learned.]

## What this synthesis is *not*
[One sentence. Specifically: this is a plan to execute a goal, not a decision about whether the goal is right (use /deepthink-decision) or a design for what to build (use /deepthink-design).]
```

---

## Verification

Before declaring the plan complete, the model must check:

- [ ] All five phases ran, with a gate after each.
- [ ] Phase 1 produced an observable end state, classified hard vs. nice-to-have scope, and ran a rough capacity check.
- [ ] Phase 2 produced 4–8 milestones with dependencies labeled (hard / soft / external) and surfaced the critical path.
- [ ] Phase 3 ran the full core roster + any user-confirmed additions, including the implementer and abort-condition perspectives.
- [ ] Phase 4 produced pre-mortem failure modes with early warning signs, ran a 30%-slippage capacity test, and defined abort conditions.
- [ ] Phase 5 milestones are observable, owned, and dated. External dependencies have contingencies.
- [ ] Tripwires (course-correct) and abort conditions (stop) are both present and distinct.
- [ ] A re-planning checkpoint is named.
- [ ] The synthesis does not pretend to be a decision or a design.
