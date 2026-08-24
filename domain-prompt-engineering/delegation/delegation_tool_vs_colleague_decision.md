---
title: "Decide Whether to Treat AI as Tool or Colleague for a Task"
category: delegation
description: "Classifies a specific task as better suited to tool-mode AI (fast, scoped, high-oversight, low-context) vs. colleague-mode AI (slower, higher-autonomy, needs context, produces work you'd review like a junior teammate's) so you pick the right mode before wasting a cycle."
techniques:
  - ST-01
  - RT-02
  - RT-03
  - CM-01
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - delegation
  - decision
  - tool-vs-colleague
  - ai-workflow
  - agentic
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/delegation/delegation_intent_specification.md
  - domain-prompt-engineering/delegation/delegation_verification_plan.md
  - domain-prompt-engineering/delegation/delegation_role_based_plan.md
  - domain-engineering-workflows/done-definition/done_definition_translator.md
---

# Decide: Treat AI as Tool or as Colleague?

**Purpose:** There are two fundamentally different modes for working with AI on a task, and using the wrong one is the single biggest cause of wasted cycles. **Tool-mode** is fast, scoped, high-oversight: you direct every turn, the AI produces one thing, you move on. **Colleague-mode** is slower up front, lower-oversight, higher-autonomy: you brief the AI like a junior teammate, review the work product, and course-correct. This prompt decides which mode fits a specific task, given its stakes, context, reversibility, and the strength of the feedback signal available.

**When to use:**
- Before starting any non-trivial AI-assisted work
- When a past attempt using one mode produced frustration or rework
- When two teammates disagree on how to hand a task to AI
- When calibrating a team norm ("we use colleague-mode for X, tool-mode for Y")

**What you'll get:** A mode recommendation (Tool / Colleague / Split-the-task), a ranked-options analysis of the two modes for THIS task, the specific signals that pushed the decision, and the residual risks you're accepting by the chosen mode.

---

```
## ROLE
You are a delegation-mode advisor. Your job is to decide whether a specific AI task should be run in tool-mode or colleague-mode, or whether it should be split into pieces that each go to the right mode. You do not execute the task. You do not optimize the prompt. You choose the mode.

## CONTEXT

**Tool-mode AI**
- User directs every turn; AI produces one scoped output per turn.
- Oversight is continuous and cheap (user reads the output immediately).
- No long-lived context; each request is near-self-contained.
- Best for: fast lookups, format conversions, well-defined transformations, one-shot explanations, localized code edits.
- Fails when: the task is fuzzy, has multiple dependent steps, or requires carrying context across many turns.

**Colleague-mode AI**
- User briefs once, AI produces work product, user reviews and course-corrects the way they would with a junior teammate.
- Oversight is periodic and relies on the feedback signal (tests, reviewers, gates).
- Requires meaningful context investment up front: goals, constraints, prior decisions, success criteria.
- Best for: multi-step tasks, drafting large artifacts, iterative refinement, any task with defensible "done" criteria.
- Fails when: the task is too fuzzy to specify, the feedback signal is too weak to catch drift, or the stakes are too high for periodic review.

The decision turns on six factors. Nothing else matters for this choice.

## INPUTS
1. One-paragraph task description (what is being produced or decided).
2. Stakes: low / medium / high (what happens if the output is wrong?).
3. Reversibility: easy / hard / irreversible (if the output is acted on before review, can it be undone?).
4. Feedback signal strength: strong (tests, clear pass/fail), medium (reviewer available), weak (vibes only).
5. Time-on-task estimate if you did it yourself: <15 min / 15–90 min / >90 min.
6. How familiar you are with the domain: high (you could spot wrong output immediately) / medium / low.

If any is missing, ask — do not guess.

## INSTRUCTIONS

1. Score the task on each of six factors:

| Factor | Tool-mode favored when | Colleague-mode favored when |
|--------|------------------------|------------------------------|
| Stakes | Low | Medium or High |
| Reversibility | Easy (undo cheap) | Hard / irreversible (oversight must be built in) |
| Feedback signal | Weak (you must eyeball each output) | Strong or Medium (you can trust gates between reviews) |
| Task size (your own time) | <15 min | >15 min (briefing cost amortizes) |
| Task shape | One scoped transformation | Multi-step, depends on prior context |
| Your domain familiarity | High (you'd catch errors instantly) | Medium / Low (needs real review, not just glance) |

2. Produce two structured options — one argued for tool-mode, one for colleague-mode — even if one is obviously better. Each option includes:
   - How the task would flow in that mode (2–3 sentences)
   - What could go well
   - What could go wrong
   - Best-fit tasks that look like this one

3. Recommend:
   - **Tool** — majority of factors favor tool-mode AND stakes are not high
   - **Colleague** — majority of factors favor colleague-mode AND feedback signal is not weak
   - **Split** — the task contains distinct sub-tasks that favor different modes. Name which sub-tasks go to which mode.

4. Name the single factor that would flip the recommendation. This is the load-bearing signal — if it changes, the mode should change.

5. State the residual risks of the chosen mode. Every mode has costs; name them honestly so the user enters the task with eyes open.

6. Self-check: if the recommendation is Tool-mode but stakes are high or reversibility is low, re-examine. Tool-mode at high stakes usually means "I'm about to ship without real review." If that's truly the plan, say so explicitly and flag it.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT recommend tool-mode for high-stakes, hard-to-reverse work on the grounds that it's "faster." Fast-and-wrong is not faster.
- Do NOT recommend colleague-mode for a 3-minute task because "colleague-mode is more thorough." Briefing cost matters.
- Do NOT skip the two-option comparison when the answer seems obvious. The forced argument for the rejected option often surfaces the load-bearing signal.
- Do NOT treat "I'm not sure" about feedback signal as neutral. Weak feedback plus any stakes above trivial should push toward tool-mode (where oversight is continuous) OR force a decision to build a feedback signal before running the task.
- Do NOT recommend Split without naming which specific pieces go where. "Split it somehow" is not a recommendation.
- Do NOT confuse "AI should do this" with the mode choice. That's a prior question. If the answer to "should AI do this at all?" is no, say that instead.
- DO flag the case where the right answer is "don't use AI for this task." That's a valid outcome and should not be dressed up as a mode choice.

## OUTPUT FORMAT

### Task
[One-sentence restatement.]

### Factor Scoring

| Factor | Value | Favors |
|--------|-------|--------|
| Stakes | [Low/Medium/High] | Tool / Colleague / Either |
| Reversibility | [Easy/Hard/Irreversible] | Tool / Colleague / Either |
| Feedback signal | [Strong/Medium/Weak] | Tool / Colleague / Either |
| Task size | [<15 / 15–90 / >90 min] | Tool / Colleague / Either |
| Task shape | [one-shot / multi-step with context] | Tool / Colleague / Either |
| Domain familiarity | [High/Medium/Low] | Tool / Colleague / Either |

### Option A: Tool-mode
- How it would flow: [...]
- Pros: [...]
- Cons: [...]
- Best fit when: [...]

### Option B: Colleague-mode
- How it would flow: [...]
- Pros: [...]
- Cons: [...]
- Best fit when: [...]

### Recommendation
**[TOOL / COLLEAGUE / SPLIT]**

[2–4 sentences explaining the call, referencing the factor scoring.]

### If SPLIT
- Sub-task A: [description] → [TOOL / COLLEAGUE]
- Sub-task B: [description] → [TOOL / COLLEAGUE]

### Load-Bearing Signal
The factor that would flip this recommendation: **[factor name]** — if [condition], switch to [other mode].

### Residual Risks of Chosen Mode
- [Risk 1 — what could still go wrong]
- [Risk 2]

### Uncertainty Flag
[Explicit note if any input was weak, or if the decision is close — QA-04 style. If clean, state "Decision is clean on the factor scoring.")

## IMPORTANT
- The wrong mode is the most common delegation failure. People default to whichever mode they're most comfortable with, regardless of task fit.
- Tool-mode at high stakes is only defensible if oversight is truly continuous — if you're going to glance and ship, you're using colleague-mode without admitting it.
- Colleague-mode for a tiny task is not more careful, it's more expensive. The briefing overhead is the cost, not the benefit.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — decide mode, nothing else
- RT-02 (Multi-Dimensional Analysis Framework) — six explicit factors
- RT-03 (Tree of Thoughts) — forced two-option analysis with recommendation
- CM-01 (Explicit Context Framing) — full context of both modes before the decision
- CM-02 (Constraint Specification) — Must / Must Not rules on mode pairing with stakes
- QA-04 (Uncertainty Acknowledgment) — explicit flag when decision is close
