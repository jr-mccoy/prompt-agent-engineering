---
title: "Diagnostic for Whether the 'Right Problem' Is Being Solved"
category: prompt-engineering/goal-orientation
description: "Before writing a prompt or delegating a task to AI, verify that the problem the user is about to solve is the problem actually worth solving — separating the stated task from the underlying intent, surfacing assumptions about why it matters, and testing whether solving it as stated will deliver the outcome the user expects."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-09
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - goal-orientation
  - intent-clarity
  - problem-framing
  - diagnostic
  - ai-delegation
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/goal-orientation/goalorientation_constraint_architecture_workshop.md
  - domain-prompt-engineering/delegation/delegation_intent_specification.md
  - domain-personal-development/prompts/agency/agency_project_ownership_converter.md
  - domain-business-strategy/chief-of-staff/cos_clarify_fuzzy_goals.md
---

# Diagnostic for Whether the "Right Problem" Is Being Solved

**Objective:** Before writing the prompt (or running the agent, or kicking off the workflow), test whether the problem the user is about to hand to AI is the *right* problem. Separate the stated task from the outcome the user actually wants. Surface the assumptions that connect the two. Identify where a well-executed answer to the stated problem would still leave the user with the original need unmet. Produce one of three outputs: proceed as framed, reframe, or stop.

**When to use:** You're about to write or run a prompt that will burn meaningful time, compute, or attention. Especially useful before any task that costs >10 minutes of review time downstream, any recurring workflow, or any task where the cost of solving the wrong thing exceeds the cost of pausing to check.

**Audience:** Individuals deciding how to spend AI assistance, team leads shaping AI workflows, anyone about to delegate a multi-step task where rework cost is real. Applicable across coding, writing, analysis, and personal work.

---

## Inputs Required

1. **The task as currently stated.** Verbatim, exactly as the user plans to phrase it to the model.
2. **The outcome the user is hoping for.** One sentence. Not the output format — the change in the user's world the output is supposed to produce.
3. **The cost of solving the wrong problem.** Rough estimate: time to discover, time to redo, cost in other people's attention or trust.
4. **The user's confidence the stated task maps to the outcome.** On a 1–5 scale, honestly. If 5 with no evidence, flag as overconfidence (see false-positive prevention).

Refuse to run the diagnostic on a task where the user can't state the intended outcome. "I want to try something" or "see what the AI comes up with" is not an outcome — it's exploration, and exploration shouldn't be route-checked.

---

## Instructions

### Step 1 — Restate the task and outcome separately

Write both in one line each:

- **Task (what the user will ask the model to do):** [...]
- **Outcome (what the user wants changed when the task is complete):** [...]

Confirm with the user that the outcome statement is the real one. Users often restate the task when asked for the outcome. If the two statements are essentially the same, push for a deeper outcome — what does completing the task *unlock* or *prevent*?

### Step 2 — Surface the assumption bridge

The stated task only produces the outcome *if* certain assumptions hold. Name them. Examples:

- "If the model writes a good draft, it will save me the writing time." (Assumes rewriting a bad draft isn't more expensive than starting from scratch.)
- "If we build this analysis, leadership will make the decision." (Assumes the analysis is what's missing.)
- "If I debug this error, the feature will work." (Assumes the error is the only blocker.)

List 3–6 assumptions. Each should be stated as a conditional the user could check.

### Step 3 — Stress-test each assumption

For each assumption, ask:
- **Have you tested it, or are you guessing?**
- **What would you expect to see if it's false?**
- **What's the cheapest way to check it before committing to the full task?**

Mark each assumption: *tested*, *reasonable guess*, or *untested and load-bearing*.

If any *untested and load-bearing* assumption exists, the "right problem" check is not passing. Either test the assumption or reframe the task so it doesn't depend on that assumption.

### Step 4 — Check for the four common wrong-problem patterns

Run the task against this short checklist. Name any that apply.

- **Solving for output, not outcome.** The task produces an artifact, but the outcome requires a decision, a conversation, a behavior change, or a relationship shift that the artifact alone doesn't deliver.
- **Solving for the visible problem, not the causing problem.** Fixing the symptom leaves the cause in place to re-produce it.
- **Solving for the easy-to-state problem, not the hard-to-state one.** The user has defaulted to the version that's easy to phrase because it's 2 a.m. and the harder framing is, well, harder.
- **Solving the wrong scope.** The task is sized to what the user has time for today, not to what would actually move the outcome. Or the reverse — scoped huge when a narrow test would do.

A task hitting two or more of these is probably the wrong problem.

### Step 5 — Ask the counterfactual

Complete the sentence: "If the model produced a perfect answer to the stated task right now, the user would [describe what they would do next]."

- If the answer is "move on to the outcome" and the path is direct → proceed.
- If the answer is "have to do substantial work before the outcome is reached" → reframe. The right problem is that work.
- If the answer is "still not be sure the outcome followed" → reframe. There's a verification step or a decision that's missing from the task.

This is the single most diagnostic step. A perfect answer to the wrong problem rarely feels like a win.

### Step 6 — Produce one of three verdicts

- **Proceed as framed.** The task maps cleanly to the outcome; assumptions are tested or cheap to check; the counterfactual is a direct path. Move on to writing the actual prompt.
- **Reframe.** The task doesn't map cleanly. Offer a reframed task that better targets the outcome. Specifically name what changed and why.
- **Stop.** The outcome is unclear or the assumption bridge is too thin to commit without testing. Name the one check the user should do before re-running the diagnostic.

Give the verdict in one line, followed by a short explanation.

---

## Constraints

### Must
- Require a stated outcome that is distinct from the stated task.
- Name assumptions explicitly as conditionals.
- Mark each assumption as tested / reasonable guess / untested-and-load-bearing.
- Run the four-pattern checklist and name any that apply.
- Ask the counterfactual explicitly.
- End with one of three verdicts: proceed, reframe, stop.

### Must Not
- Accept an outcome that is a restatement of the task.
- Produce a reframe the user didn't ask for without flagging it as a suggestion to reject.
- Stop a task for aesthetic reasons ("seems like the wrong framing") without naming a specific pattern or untested assumption.
- Run the diagnostic on exploratory tasks. Exploration is not goal-oriented and shouldn't be judged by goal-orientation.
- Route the user through a second prompt when the verdict should be "proceed."

---

## False-Positive Prevention

1. **Over-diagnosing is a real cost.** Not every task needs route-checking. If the task is small, fast, easily rerun, and low-stakes, skip this prompt and just write the prompt. Route-checking a 5-minute task for 10 minutes is anti-leverage.
2. **Confidence without evidence is the biggest flag.** A user rating their task-to-outcome confidence at 5/5 when they haven't tested the assumption bridge is the highest-risk case — these are the tasks that produce perfect answers to the wrong problem.
3. **"Reframe" should be a suggestion, not a mandate.** The user owns the framing. Offer the reframe with the diagnostic reasoning and let them decide.
4. **This prompt can be used defensively.** Someone avoiding a hard task can invoke "right problem?" forever. If the user has been diagnosing the same task more than twice, the diagnostic is itself the avoidance — skip to doing.
5. **Don't confuse lack of certainty with wrong framing.** Many tasks proceed with real uncertainty. Stop-the-press is for load-bearing *untested* assumptions, not for all uncertainty.
6. **Exploratory work shouldn't run through this.** "See what happens when I ask X" is valid. This prompt is for goal-oriented tasks with stated outcomes.
7. **The counterfactual question can be manipulated.** If the user has the wrong outcome in mind, the counterfactual returns "proceed" against a false target. Encourage the user to stress-test the outcome itself when confidence is low.

---

## Output Format

```markdown
## Task (as stated)
[...]

## Outcome (what the user wants changed)
[...]

## Are task and outcome distinct? [yes / no — if no, push for deeper outcome before continuing]

## Assumption bridge
- [Conditional] — [tested / reasonable guess / untested-and-load-bearing]
- [...]

## Wrong-problem patterns present
- [ ] Solving for output, not outcome
- [ ] Solving for visible, not causing, problem
- [ ] Solving for easy-to-state, not hard-to-state, problem
- [ ] Solving the wrong scope

[Any checked: explain in one line each.]

## Counterfactual
If the model produced a perfect answer right now, the user would: [...]
- Direct path to outcome: [yes / no / unclear]

## Verdict
**[Proceed as framed | Reframe | Stop]**

[One paragraph explanation. If reframe, state the proposed reframed task and what changed. If stop, state the one check the user should do before re-running.]
```

---

## Verification

- [ ] Task and outcome are stated distinctly.
- [ ] At least 3 assumptions are listed as conditionals.
- [ ] Each assumption has a tested / guess / untested label.
- [ ] The four-pattern checklist has been run.
- [ ] The counterfactual question is answered.
- [ ] The verdict is exactly one of proceed / reframe / stop.
- [ ] Exploratory tasks were rejected from the diagnostic rather than forced through it.
