---
title: "Specify a Task for a Sub-Agent with Scope and Verification"
category: business-strategy/chief-of-staff
description: "Write a complete task brief for a sub-agent (AI, EA, junior, contractor) with intent, scope, constraints, deliverable shape, and a verification plan — tight enough that the return is evaluable without re-doing the work yourself."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - ST-03
difficulty: intermediate
tags:
  - chief-of-staff
  - delegation
  - subagent
  - scoping
  - verification
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/delegation/delegation_intent_specification.md
  - domain-prompt-engineering/delegation/delegation_verification_plan.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-prompt-engineering/delegation/delegation_tool_vs_colleague_decision.md
---

# Specify a Task for a Sub-Agent with Scope and Verification

**Objective:** Produce a single task brief for a sub-agent (AI agent, executive assistant, junior teammate, contractor) that specifies intent, scope limits, inputs, deliverable shape, and a verification plan the user can execute in under 10 minutes. The brief should be tight enough that a reasonable sub-agent cannot return obviously wrong work and call it done.

**When to use:** Before handing off any task that will take more than 15 minutes of someone else's time. When past hand-offs keep returning subtly wrong or incomplete. When delegating to an AI agent that will execute multi-step work without checkpoints.

**Audience:** Individual knowledge worker or executive managing delegation to sub-agents. Not limited to AI — the brief structure is the same for a human EA, a vendor, or a Claude subagent.

---

## Inputs Required

1. **The task in the user's words, before specification.** One or two sentences.
2. **Who the sub-agent is.** Specifically: AI (which model / which tool access), or a named human role. This affects what context must be included and what the sub-agent will miss by default.
3. **The sub-agent's known failure modes**, if the user has delegated to them before. Generic if new.
4. **How the user will know it's done.** Their current plan, even if rough.
5. **The deadline and the consequence of missing it.**

Refuse to produce a brief if the user cannot answer input 4. Verification is the non-negotiable half of delegation.

---

## Instructions

### Step 1 — State the intent, not the mechanics

Write one sentence in this shape:

> The outcome I want is [observable end state], so that [downstream action / decision].

No verbs about how the sub-agent should work. No tool names. If the user wrote mechanics ("use X tool to do Y"), lift out the outcome and flag that the mechanics may be user preference, not requirement.

### Step 2 — Draw scope boundaries

Three bullets:
- **In scope:** what counts as part of this task.
- **Out of scope:** adjacent work that might look related but is not this task.
- **If you find something out of scope,** what the sub-agent should do — flag it, ignore it, or escalate. Pick one explicitly.

### Step 3 — Inventory inputs the sub-agent will need

List:
- Documents, links, access credentials.
- Prior context the sub-agent does not know.
- People they may need to contact, and whether they're allowed to.

For an AI sub-agent: name the tools and external systems it is allowed to call, and which it is not. For a human sub-agent: name what authority they have for this task.

### Step 4 — Define the deliverable shape

Write the deliverable as a structural description, not a free-text ask:
- Format (doc, email, spreadsheet, code diff, slide deck).
- Required sections or fields.
- Length bounds.
- What "good" looks like with one example if the user has one.
- What must not appear (false claims, invented data, placeholder lorem, executive summary more than N words).

### Step 5 — Specify the verification plan

Three items, written for the user (not the sub-agent):
- **Automatic checks.** What the user can verify in under 2 minutes without re-doing the work (spot-check a fact, count items, open a link, read the summary).
- **Red-flag signals.** Specific patterns that mean the output is probably wrong even if it looks right. Generic examples: unfamiliar stats with no source; numbered lists that all sum to round numbers; confident claims on topics the user has not briefed.
- **Failure recovery.** If the output fails verification, does the user re-prompt, fix in place, or reassign? Decide in advance.

### Step 6 — Define stop conditions for the sub-agent

For AI sub-agents especially, name when the sub-agent must stop and ask rather than continue:
- Required input is missing.
- A fact the sub-agent cannot verify would materially change the deliverable.
- A decision outside the sub-agent's authority is needed.
- The budget (time, tool calls, dollars) is exceeded.

---

## Constraints

### Must
- Produce intent as an outcome sentence, not a method sentence.
- Draw all three scope boundaries.
- Specify verification in terms the user will actually execute.
- Name at least one red-flag signal specific to this task.
- Name stop conditions for the sub-agent.

### Must Not
- Write the task itself for the sub-agent. This is a brief, not a finished deliverable.
- Assume the sub-agent shares the user's context.
- Leave the verification step as "I'll review the output." That's not a plan.
- Over-specify mechanics the sub-agent doesn't need. Outcomes bind; methods don't.
- Hide the deadline or consequence of missing it.

---

## False-Positive Prevention

1. **Don't confuse effort with specification.** A three-page brief with no verification plan is worse than a one-page brief with a real one.
2. **Don't specify a deliverable that only looks good on delivery.** Red-flag signals are the defense against plausible-wrong output — name them.
3. **Don't conflate authority with access.** A sub-agent may have access to a system and still not have authority to act in it. State both.
4. **Don't skip stop conditions for AI sub-agents.** Without them, the agent will guess, and its guesses are usually confident.
5. **If the brief is over a page,** the task is probably too big to delegate in one shot. Chunk it.

---

## Output Format

```
# Task brief: [short label] — [sub-agent]

## Intent (outcome)
The outcome I want is [end state], so that [downstream use].

## Scope
- In scope: [bullets]
- Out of scope: [bullets]
- If out-of-scope is found: [flag / ignore / escalate]

## Inputs provided
- [Doc/link/credential] — [what it's for]
- [Prior context the sub-agent won't have] — [one-line]

## Authority / tools
[What the sub-agent is allowed to do and call.]

## Deliverable
- Format: [doc/email/etc.]
- Required sections: [list]
- Length: [bounds]
- Must include: [list]
- Must not include: [list]
- Example of good (if available): [link or inline]

## Verification plan (for me)
- Automatic checks (<2 min): [bullets]
- Red-flag signals: [bullets]
- If it fails: [re-prompt / fix / reassign]

## Stop conditions (for sub-agent)
- [Condition] → [ask, don't proceed]

## Deadline
[Date/time] — consequence of missing: [specific].
```

---

## Verification

- [ ] Intent is an outcome, not a method.
- [ ] Scope has all three boundaries and a found-out-of-scope rule.
- [ ] At least one red-flag signal is specific to this task.
- [ ] Verification plan takes under 10 minutes.
- [ ] Stop conditions exist for an AI sub-agent.
- [ ] Brief fits on one page.
