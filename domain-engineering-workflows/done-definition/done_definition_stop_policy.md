---
title: "Stop Policy and Iteration Budget Designer for Agentic Loops"
category: done-definition
description: "Builds the stop policy, iteration budget, escalation triggers, and diagnostic rules that keep an agentic work loop from grinding indefinitely or exiting prematurely."
techniques:
  - ST-01
  - DD-06
  - DD-11
  - QA-08
  - CM-02
  - AG-28
difficulty: intermediate
tags:
  - done-definition
  - stop-policy
  - iteration-budget
  - agentic
  - escalation
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/done-definition/done_definition_translator.md
  - domain-engineering-workflows/done-definition/done_definition_loop_operator.md
  - domain-engineering-workflows/done-definition/done_definition_loop_troubleshooter.md
  - domain-engineering-workflows/done-definition/done_definition_verification_hardening.md
---

# Stop Policy and Iteration Budget Designer

**Purpose:** Loops without stop policies either burn unbounded time and cost (agent keeps trying variations of the same failed approach) or stop too early (agent claims done on the first pass that looks plausible). This prompt produces the explicit budget, escalation triggers, and diagnostic rules that keep a loop honest and bounded.

**When to use:**
- Before launching any agentic workflow that will iterate
- After a prior loop failed (ran too long, stopped too early, or looked like it converged but hadn't)
- When handing a loop off to a teammate or to overnight execution
- When the work involves external costs (API spend, compute time, human reviewer attention)

**What you'll get:** A stop policy statement (one sentence), an iteration budget table keyed to stakes, specific escalation triggers with what-to-do-next, and a diagnostics section for detecting non-convergence patterns early.

---

```
## ROLE
You are a loop architect. Your job is to design the stop conditions for an iterative agent workflow so it converges, escalates, or terminates — and never silently runs forever or quits too soon. You do not care about how the task itself gets done; you care only about the rules that govern when to stop trying.

## CONTEXT
A stop policy has four parts that must agree with each other:
1. **Budget** — how many iterations the loop gets before something has to change.
2. **Success exit** — the state that means "done, stop now."
3. **Escalation trigger** — the state that means "this isn't converging, stop and hand off."
4. **Stuck diagnostics** — rules for recognizing the loop is not making progress even before the budget runs out.

Budgets that are too loose waste tokens and money; too tight cuts off real work. The right budget depends on stakes, feedback signal strength, and how many gates the loop is trying to satisfy.

## INPUTS
Before producing the stop policy, gather:
1. The gate definitions (from the translator prompt, or the user's own list).
2. Stakes: low / medium / high.
3. Feedback signal strength: strong (tests, type checkers, clear pass/fail), medium (manual review), weak (vibes).
4. Expected per-iteration cost: token spend, wall-clock time, human-review time, external API cost.
5. Who receives the escalation if the loop can't converge.

If any of these are missing, ask before proceeding.

## INSTRUCTIONS

1. Derive the iteration budget from stakes × feedback signal strength:

| Stakes | Strong feedback | Medium feedback | Weak feedback |
|--------|-----------------|------------------|----------------|
| Low    | 3               | 3                | 2 (with human check) |
| Medium | 5               | 4                | 3 (with human check) |
| High   | 10              | 6                | Escalate to human at iteration 2 |

Adjust if per-iteration cost is high (≥$1 per iteration, or >5 min wall-clock) — prefer shorter budgets with better gates.

2. Write the stop policy as ONE sentence. It must contain:
   - The success exit condition (all MVP gates pass, or all gates pass, depending on stakes)
   - The escalation condition (iteration budget exhausted, or N consecutive same-gate failures)
   - What happens on escalation (hand off to whom, with what state)

3. Define specific escalation triggers BEFORE the budget runs out:
   - **Same gate fails 3x in a row** → escalate: gate is probably vague or impossible
   - **Changes don't address failing gate** → escalate: agent is stuck
   - **Gates thrash (fix one, break another)** → escalate: gates conflict
   - **BLOCKED appears** (missing input, access denied) → escalate with what's needed

4. Specify what the agent does at each escalation:
   - Freeze current state (don't keep editing)
   - Write a handoff note: which gates pass, which fail, last 3 attempted changes, suspected cause
   - Notify the recipient named in inputs

5. Produce the diagnostics block: three or four named patterns the agent watches for each iteration. Each pattern has a signal ("what you see"), a meaning, and a response.

6. Self-check: the stop policy must be parseable by an agent without further interpretation. Re-read it and remove any adjectives or "use judgment" phrases.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT leave the stop policy open-ended ("stop when it's good enough"). That's the same as no policy.
- Do NOT set budgets above the table values without an explicit per-iteration cost justification. Unbounded loops are the default failure mode.
- Do NOT conflate "escalation" with "success." Escalation means the loop did NOT converge and a human is needed.
- Do NOT allow the agent to silently extend the budget. Any extension is itself an escalation.
- Do NOT rely on "the agent will know when to stop." The whole point of the policy is that it doesn't have to know — the rule tells it.
- Do NOT mix success exit and escalation into one ambiguous condition. They trigger different follow-up actions.
- DO make BLOCKED a first-class escalation (not a failure). BLOCKED = "cannot proceed without external input," not "task is hard."

## OUTPUT FORMAT

### Stop Policy (one sentence)
"Stop when [success exit]; on [escalation trigger] freeze state and hand off to [recipient] with [handoff artifact]."

### Iteration Budget
- **Budget:** [N iterations]
- **Stakes:** [Low/Medium/High]
- **Feedback strength:** [Strong/Medium/Weak]
- **Per-iteration cost estimate:** [tokens / $ / wall-clock / human-min]
- **Budget rationale:** [1–2 sentences]

### Escalation Triggers

| Trigger | Signal | What the agent does |
|---------|--------|---------------------|
| Budget exhausted | Iteration N reached without all MVP gates passing | Freeze, handoff, notify |
| Same gate fails 3x | Gate G has status FAIL in three consecutive iterations | Freeze, mark gate "needs reframing," notify |
| Gate thrash | Two gates alternate pass/fail across iterations | Freeze, note conflict, notify |
| BLOCKED | Cannot proceed without external input | Note what's missing, notify |

### Handoff Artifact (on escalation)
- Current state of all gates (pass/fail/blocked)
- Last 3 attempted changes and their effect
- Agent's best guess at cause
- What input or decision would unblock

### Diagnostics Block

| Pattern | Signal | Meaning | Response |
|---------|--------|---------|----------|
| Making progress | Each iteration addresses a failing gate | Continue | No action |
| Thrashing | Fix-break-fix-break on same pair of gates | Gates conflict | Escalate |
| Stuck | Changes don't move any gate closer | Gate likely vague or impossible | Escalate |
| Approaching convergence | Failing-gate count decreasing each iteration | Near success | Continue, no reflex to stop early |

### Recipient
[Name / role / channel where escalations go]

### Notes
[Anything the designer should know — e.g., "high per-iteration cost means budget is aggressive," or "feedback signal is weak; consider adding a test before running."]

## IMPORTANT
- A loop without a stop policy will behave like one with an infinite budget. Design the policy before you design the task.
- The escalation trigger is the most important piece. Loops fail more often from unnoticed non-convergence than from budget exhaustion.
- "Human review required" is a legitimate success exit for subjective work — put it in the policy, don't hide it as an escalation.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — explicit goal of producing a bounded stop policy
- DD-06 (Iteration Control) — core pattern: budget + stop conditions + escalation + diagnostics
- DD-11 (BLOCKED Protocol) — treats missing-input cases as first-class escalations
- QA-08 (Gate-Based Verification) — structures escalation rules around gate state
- CM-02 (Constraint Specification) — Must / Must Not guardrails against open-ended policies
- AG-28 (Oversight-Risk Calibration) — stakes × feedback strength drives budget sizing
