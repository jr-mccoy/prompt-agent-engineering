---
title: "Human-in-the-Loop Handoff"
category: prompt-engineering/agent-workflows
description: "Define when and how an agent pauses to request human input, with the format of the request and the resume protocol."
techniques:
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - human-in-loop
  - handoff
  - pause-resume
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_authority_boundary_prompt.md
---

## Objective

Specify the conditions under which an agent must pause for human input, the structure of the request, the timeout behavior, and how the agent resumes once human input arrives.

## When to Use

- Agents take destructive or sensitive actions
- Confidence-based gating routes uncertain cases to humans
- A workflow requires human signoff at named milestones

## Inputs

1. Pause triggers (per category: authority, uncertainty, milestone, error)
2. Communication channel (Slack, email, queue)
3. Timeout behavior if human does not respond
4. Resume condition shape

## Constraints

**Must:**
- Make pause triggers falsifiable
- Format the human-facing request to fit the channel and answerable in one reply
- Define timeout: best-effort proceed, escalate, or stay paused
- On resume, validate that human input addresses the question

**Must Not:**
- Pause for vague reasons ("seems risky")
- Send long context dumps to humans; send the decision and the alternatives
- Resume on input that did not answer the question

## Instructions

1. Enumerate pause triggers.
2. Write the human-facing request template (concise: question + alternatives + default).
3. Define timeout behavior per trigger.
4. Define how the agent verifies the human's answer is interpretable.
5. Define resume payload.

## Output Format

```
PAUSE TRIGGERS

[authority]
  - action in <Ask First> set
[uncertainty]
  - confidence < <threshold>
  - judge fails after retry cap
[milestone]
  - reached <named gate>
[error]
  - error class <X>
  - tool denial

HUMAN REQUEST TEMPLATE
  TO: <human>
  CONTEXT: <≤2 sentences>
  QUESTION: <one sentence>
  OPTIONS:
    A. <option>
    B. <option>
    C. (other; reply with text)
  IF NO REPLY BY <timeout>: <default behavior>

INPUT VALIDATION
  Accept: A | B | free text matching <pattern>
  Reject: silence (apply default) | unrelated text (re-ask once)

RESUME PAYLOAD
  {
    "human_decision": <A | B | free text>,
    "received_at": <ts>,
    "applied_to_iteration": <n>
  }

TIMEOUT BEHAVIOR (per trigger)
  authority: stay paused (do not proceed without consent)
  uncertainty: escalate to default policy
  milestone: stay paused (gate is gating)
  error: escalate
```

## Verification

- Triggers are falsifiable
- Request fits one screen (≤200 tokens)
- Timeout behavior is per-trigger, not global
- Resume validates input before continuing
