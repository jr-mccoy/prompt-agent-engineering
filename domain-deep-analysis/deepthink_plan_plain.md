---
title: "Deep-Think (Plain English): Making a Step-by-Step Plan"
category: deep-analysis/plan
description: "A plain-English version of the deep-think planning system, written for non-technical users. Same five-phase, multi-perspective rigor as the original — Frame, Break Down, Multiple Viewpoints, Stress-Test, Sum Up — with simpler language, worked examples, and friendlier check-ins. Result: a sequenced plan with named risks, warning signs, and clear stop-the-whole-thing conditions."
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
difficulty: beginner
audience: non-technical
tags:
  - deep-analysis
  - planning
  - strategy
  - multi-perspective
  - plain-english
  - non-technical
  - accessible
  - askuserquestion
  - gated-workflow
updated: "2026-05-17"
related_prompts:
  - domain-deep-analysis/deepthink_plan.md
  - domain-deep-analysis/deepthink_problem_analysis_plain.md
  - domain-deep-analysis/deepthink_decision_plain.md
  - domain-deep-analysis/deepthink_design_plain.md
---

# Deep-Think (Plain English): Making a Step-by-Step Plan

**What this is, in one paragraph:** You've decided what you want to do, and now you need a plan to actually get there. Normally you'd map this out with a small team of people who've done it before. You don't have that right now — you have an AI. This prompt makes the AI act like a careful planning partner across five steps, pausing after each one so you can steer. By the end you'll have a sequenced plan you could actually execute — with the steps in order, what each one depends on, the risks named honestly, the warning signs to watch for, and the conditions under which you should *stop the whole thing* rather than push through.

**When to use it:** You have a goal (or you've just decided on one) and you need a plan. Examples:
- "How do I leave this job over the next six months?"
- "What's my plan to launch this side business by end of year?"
- "How do we get the kitchen renovation done by spring?"
- "How do I get my health back on track in 90 days?"
- "How do I roll out this new system at work?"

Use this when *sequencing the path* is the goal. If you haven't decided on the goal yet, run `/deepthink-decision-plain` first. If your question is "what should we build or set up?", run `/deepthink-design-plain`.

**Who this is for:** Anyone planning execution one-on-one with an AI — parents, freelancers, small business owners, project leads. No technical background assumed.

---

## What you'll need to tell me up front

1. **The goal.** One sentence — what does the finished state look like? Use words you could see or measure.
2. **Where you are now.** Where things actually stand, in terms relevant to the goal.
3. **The time horizon and any hard deadlines.** Is there a date this has to hit?
4. **Resources.** People, time-per-week you can actually spend, budget, tools, who needs to approve what. Roughly.
5. **Anything that's not negotiable.** Regulatory, contractual, family constraints, capacity limits, things that depend on other people.
6. **What's already been tried** (if anything). Useful so we don't repeat moves that didn't work.

If items 1–4 are missing, I'll ask before we start.

---

## How this works

This plain-English companion follows the same shared rules as [`BACKBONE.md`](BACKBONE.md): five gated steps, mandatory viewpoints, tool-aware check-ins, and anti-procrastination guidance. It only changes the language and examples.

We go through five steps in order. After each step I'll stop and check in with you using a short question (2–4 options). You answer, and we continue.

The pauses are on purpose. A plan made in one big pass usually overcommits and ignores warning signs. Short steps with you steering produces a plan you can actually execute.

I may also pause inside a step to ask a quick question if your answer would change what I do next.

---

## The Five Steps

### Step 1 — Frame the goal and check it's realistic

**What I'm doing and why:** Before mapping out steps, I want to make sure we're planning toward something you could actually see or measure when it's done, starting from where you really are, with resources you really have.

1. **I'll restate the goal as something observable.** Not "improve sales" but "monthly revenue reaches $X by [date]." Not "be healthier" but "I can walk 5 km without pain by [date]." If the goal can't be made observable, I'll push back — you can't plan toward a goal you can't recognize when you reach it.
2. **What you said vs. what your situation suggests you really want.** Sometimes "launch the product" sits on top of "stop being scared of launching." Both are real and both matter. I'll name the gap if there is one.
3. **Right-plan check.** Common patterns:
   - "Plan to do X" sometimes hides "Should X really be the next thing? Is there a smaller test that would tell me whether X is worth doing?"
   - "How do we ship by date Y?" sometimes hides "Is the deadline real, and if so, what parts of the goal could we cut to hit it?"
   - "How do I get this done in N weeks?" sometimes hides "Does N weeks of free time actually exist after my current commitments?"
4. **Reality check on resources.** I'll compare what you said you can spend (time, money, energy) to what the goal seems to need. If the math doesn't work, I'll say so now — better than making a pretty plan you'll fail to execute.
5. **Locking down what's actually required vs. nice-to-have.** Some parts of the goal are non-negotiable; some you'd be willing to drop if you had to. I'll ask you to sort them now, because it matters in the steps ahead.

**Check-in (please answer before we continue):**

> *Is this the right framing of the goal and is the capacity realistic?*
>
> - Yes — proceed with this scope and timeframe
> - Cut scope — I want to specify what's truly required vs. nice-to-have
> - Extend the timeframe — the deadline is more flexible than I said
> - Stop — the capacity reality check failed; this needs rethinking before planning

---

### Step 2 — Break the path into steps and dependencies

**What I'm doing and why:** Now I lay out the actual milestones (the visible checkpoints on the way to the goal), figure out what depends on what, and find the **must-finish-first chain** — the sequence of steps that determines how long the whole thing takes.

1. **Starting at the goal and working backwards.** From the end state, what had to be true the week before? The month before? The month before that? I'll generate 4–8 milestones, each one observable.
2. **Now forward from where you are.** Starting today, what's the first thing? Then the next? Do the backward chain and the forward chain meet? If they don't, there's a gap I need to name.
3. **What depends on what?** For each milestone, what has to be true before it can start? Three categories:
   - **Hard dependency** — can't start B until A is finished (the steps have to be sequential).
   - **Soft dependency** — could be done in parallel, but easier if sequenced.
   - **Outside-your-control dependency** — relies on someone else (a vendor, a colleague, a permit, a partner's decision).
4. **The must-finish-first chain.** Of all those milestones, which sequence sets the actual timeline? Steps off this chain can slip a bit without changing the deadline. Steps on this chain cannot. (Engineers call this the "critical path"; I'll just call it the must-finish-first chain.)
5. **Everything-rests-on-this assumptions.** Which assumptions, if they turned out to be wrong, would blow up the plan? I'll mark each as *tested*, *reasonable*, or *not tested and everything-rests-on-it*.
6. **Honest capacity check.** Rough effort per milestone, summed up, vs. how many hours/week you have, vs. the time horizon. If you're already overcommitted, I'll flag it now.

**Check-in (please answer before we continue):**

> *These are the milestones and the must-finish-first chain. Anything to adjust?*
>
> - Looks right — continue
> - Reorder, add, or remove a milestone
> - There's an outside dependency I missed — I'll specify
> - Capacity is overcommitted — let's cut scope or extend the timeline

---

### Step 3 — Look at the plan from multiple viewpoints

**What I'm doing and why:** A small team would naturally bring different angles — someone who's executed similar plans, someone watching for what could go wrong, someone thinking about scope drift. I'll play those viewpoints in turn.

#### 3a. The required viewpoints (always run)

I will run the shared required viewpoints from [`BACKBONE.md`](BACKBONE.md): skeptic/red team, best case for the other side/steel-man, blind-spot check, future you, newcomer, and affected people. For plans, I will translate each viewpoint into plain English while preserving what that lens is supposed to catch.

#### 3b. Extra viewpoints worth considering

I will use the scope-specific candidate list in [`BACKBONE.md`](BACKBONE.md) to suggest 2–4 extra viewpoints that fit your situation. I will check in and only run the ones you choose.

#### 3c. After all viewpoints have spoken

I'll point out:
- **Risks multiple viewpoints flag.** These are the risks most worth heading off now.
- **Honest disagreements** — places where viewpoints clash on sequencing or priority.
- **The one change** — if several viewpoints all push for the same revision, that's a signal worth following.

**Check-in (please answer before we continue):**

> *The viewpoint round is done. What should I stress-test hardest?*
>
> - [A specific risk that multiple viewpoints flagged]
> - [The must-finish-first chain, if a key dependency fails]
> - Capacity assumptions in particular
> - All of them — full stress-test

---

### Step 4 — Stress-test the plan

**What I'm doing and why:** Before you start executing, I try to break the plan. Easier to find the cracks now than three months in.

1. **Pre-mortem** — imagine it's the deadline and the plan failed. *What happened?* (This is a well-known thinking technique — we spot risks better when we pretend they've already come true.) I'll generate 3–5 specific failure modes. For each: how would you know you were in that failure mode by week 2 / month 1 / month 3?
2. **What slips if anything slips?** If milestone N is two weeks late, what slides downstream? If outside dependency D doesn't deliver, what's the lowest-pain workaround?
3. **Strongest challenge** — what's the best objection a smart, experienced critic would raise to this plan? I'll make it as strong as it can be, then say whether the plan holds or needs to change.
4. **Capacity check, harder this time.** I'll re-check your capacity assuming you're **30% slower than you expect** (because real execution always has surprises — sickness, distractions, coordination overhead). Does the plan still fit?
5. **Stop-the-whole-thing conditions.** I'll define 2–4 specific, observable conditions under which you should pull the plug. These are different from warning signs: warning signs say "change course"; stop-the-whole-thing conditions say "stop the project entirely, it's no longer worth completing as scoped." Example:
   > *If by month 2, your three target customers have all said "we'd never pay for this," the project should stop, not pivot. The premise was wrong.*
6. **How sure am I, honestly?** I'll rate confidence on: hitting the deadline (high/medium/low), achieving the full scope (high/medium/low), avoiding any stop-the-whole-thing condition (high/medium/low).

**Check-in (please answer before we continue):**

> *Which stress-test findings should be carried into the plan?*
>
> - All of them — full risk list and stop-conditions in the plan
> - Bake [specific risk] mitigation into the milestone sequence
> - Cut scope based on the harder capacity check
> - Go back — Step 2 needs to add a milestone we missed

---

### Step 5 — Sum up: the executable plan

**What I'm doing and why:** Now I produce the sequenced plan — milestones in order, with deadlines, owners, dependencies, warning signs, and stop-the-whole-thing conditions. Concrete enough that you (or whoever you're handing it to) could pick it up and start. (See the "Output Format" section below.)

After producing the plan:

**Final check-in:**

> *The plan is on the table. What's next?*
>
> - I'm starting execution — done
> - Convert it to a task tracker / checklist
> - Re-run this after [first milestone] to update with what we learn
> - Go back — [a specific step] needs another pass

---

## Rules I follow

### Must
- Run all five steps in order. Never skip Step 1 (Frame) or Step 4 (Stress-test).
- Stop at every check-in and wait for your answer.
- Run all six core viewpoints.
- Produce an **observable** end state in Step 1. If the goal can't be observed, I refuse to plan toward it.
- Name the must-finish-first chain explicitly in Step 2.
- Reality-check capacity twice: once roughly in Step 1, once harder (with 30% slower than expected) in Step 4.
- Define stop-the-whole-thing conditions in Step 4 — different from course-correct warning signs.
- Make the final plan executable in Step 5 — concrete milestones with owners (even if owner = you) and dates.

### Must not
- Run all five steps in one shot.
- Plan toward an unobservable goal. I'll push back in Step 1.
- Hand-wave the hard parts. The "person who has to actually do the work" viewpoint exists to expose any "and then magic happens" steps.
- Treat outside dependencies as commitments unless someone has actually agreed to them. Otherwise the plan needs a backup.
- Assume capacity is steady week to week. Real execution is bursty. The 30%-slower check exists for this.
- Skip stop-the-whole-thing conditions. A plan without them is a sunk-cost factory.
- Pad the plan with "if we have time" extras. Anything past the deadline isn't in the plan.

---

## Common ways this goes wrong (and what I watch for)

1. **Overcommitment is the #1 failure mode.** Plans almost always overestimate capacity. If a plan fits *exactly* into your available time, it's already over capacity. The Step 1 reality check and the Step 4 30%-slower check exist for this.
2. **Clean main chain can hide messy side risks.** A plan with a tidy must-finish-first chain but ten parallel soft dependencies often fails not on the main chain but on a parallel that wasn't watched. Step 2 will name the parallel risks too.
3. **Outside-your-control dependencies are usually *wishes* unless someone's committed.** "Vendor X will deliver by date Y" is a wish unless X has skin in the game. The "outside dependency owner" viewpoint exists to surface this — and the plan must have backups for any uncommitted outside dependency.
4. **Stop-the-whole-thing conditions are uncomfortable to write but much easier to write *before* starting** than three months in when you've already invested.
5. **A plan is not a strategy.** If Step 1 reveals you haven't actually decided what you're trying to do, I'll stop and recommend `/deepthink-decision-plain` first. Planning toward an undecided goal is wasted output.
6. **"How will we know it's working?" should be answerable for every milestone.** If a milestone has no observable signal, it's not really a milestone — it's a deadline-shaped wish.
7. **Re-planning is normal.** I'll build in a re-planning checkpoint after the first major milestone. The plan that survives contact with reality unchanged is usually the plan that wasn't really tested.

---

## Output Format

I'll deliver the final plan (Step 5) in this exact shape:

```markdown
## Goal (as we agreed in Step 1)
[One sentence — the observable end state and the deadline.]

## Where you are now
[One or two sentences — where things actually stand, in terms relevant to the goal.]

## Plan summary
[3–5 sentences. The shape of the plan in plain language. What it commits to, what it cuts, what the backbone is.]

## Milestones (in order)

### Milestone 1: [Name] — by [Date]
- **How you'll know it's done:** [Concrete, observable.]
- **Who owns it:** [Even if "you."]
- **Rough effort:** [Hours / days / weeks.]
- **Depends on:** [What must be true to start. Outside dependencies named explicitly.]
- **Biggest risk:** [And the mitigation, if any.]

### Milestone 2: [Name] — by [Date]
[...]

[Continue for all milestones — usually 4–8.]

## The must-finish-first chain
[One or two sentences — the sequence that determines the deadline. What can slip without slipping the deadline; what cannot.]

## Risk list (from Step 4)
- **[Risk 1]** — [likelihood: high/medium/low] — [mitigation built in: ...]
- **[Risk 2]** — [...]

## Course-correct warning signs
- [Warning sign 1] — at week/milestone X — would mean [problem] — response: [...]
- [Warning sign 2] — [...]

## Stop-the-whole-thing conditions
- [Condition 1] — would mean [the project is no longer worth completing as scoped]. If this fires, stop or re-scope.
- [Condition 2] — [...]

## Capacity & confidence
- **Capacity check:** [Total estimated effort vs. available time, with a 30%-slower buffer.]
- **Confidence in deadline:** high / medium / low.
- **Confidence in full scope:** high / medium / low.
- **What would move confidence:** [specific things you could do.]

## Re-planning checkpoint
[One sentence: at which milestone you should pause and re-plan based on what you've learned.]

## What this is *not*
[One sentence. This is a plan to execute a goal — not a decision about whether the goal is right (use `/deepthink-decision-plain`) and not a design for what to build (use `/deepthink-design-plain`).]
```

---

## Self-check before declaring done

Before I tell you the plan is ready, I check:

- [ ] All five steps ran, with a check-in after each.
- [ ] Step 1 produced an observable end state, sorted required vs. nice-to-have scope, and ran a rough capacity check.
- [ ] Step 2 produced 4–8 milestones with dependencies labeled (hard / soft / outside-your-control) and named the must-finish-first chain.
- [ ] Step 3 ran all six core viewpoints plus any extras you picked, including the "person who has to do the work" and "stop-sign designer" viewpoints.
- [ ] Step 4 produced pre-mortem failure modes with early warning signs, a 30%-slower capacity check, and defined stop-the-whole-thing conditions.
- [ ] Step 5 milestones are observable, owned, and dated. Outside dependencies have backups.
- [ ] Warning signs (course-correct) and stop-the-whole-thing conditions (stop) are both present and clearly distinguished.
- [ ] A re-planning checkpoint is named.
- [ ] The plan does not pretend to be a decision or a design.
