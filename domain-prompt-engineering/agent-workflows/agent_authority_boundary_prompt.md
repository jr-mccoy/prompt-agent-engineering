---
title: "Define Agent Authority Boundaries"
category: prompt-engineering/agent-workflows
description: "Specify what an agent can do autonomously, what requires confirmation, and what is forbidden — as enforceable prompt rules, not aspirational language."
techniques:
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - authority
  - permissions
  - safety
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_human_in_loop_handoff.md
---

## Objective

Produce three explicit lists — Can Do, Ask First, Never — that govern what an agent may execute, including how it should phrase requests and what it must refuse.

## When to Use

- Granting tool access to an agent
- Setting expectations for an agentic workflow with destructive capabilities
- Preventing the agent from taking irreversible actions without confirmation

## Inputs

1. Agent's task scope
2. Available tools and what each can do (especially destructive ones)
3. Risk tolerance per action class
4. Communication channel for "ask first" requests

## Constraints

**Must:**
- Place every available action into exactly one of: Can Do, Ask First, Never
- For Ask First, define the exact phrasing of the confirmation request
- For Never, define the response when the user requests the action anyway
- Sort by risk (high-risk items in Ask First or Never, never in Can Do)

**Must Not:**
- Leave any action unclassified
- Phrase Never as Ask First (creates pressure to bend the rule)
- Allow ambiguous "be careful" guidance for high-risk actions

## Instructions

1. Inventory every action the agent could take with its tool set.
2. Classify each.
3. For Ask First, write the prompt the agent uses to request confirmation.
4. For Never, write the refusal text.
5. Define what the agent does if the user explicitly orders a Never action.

## Output Format

```
AUTHORITY MATRIX

CAN DO (autonomous)
  - <action>
  - ...

ASK FIRST (require explicit confirmation)
  - <action>
    confirmation phrasing:
      "I'm about to <action>. This will <consequence>. Confirm with 'yes' to proceed."
    on no/silence: <do not proceed; explain>

NEVER (refuse even if requested)
  - <action>
    refusal phrasing:
      "I can't <action>. <one-line reason>. <alternative if any>."

OVERRIDE POLICY
  - User cannot move an item from Never to Can Do mid-session
  - User can move an item from Ask First to Can Do for the rest of the session by saying:
    "Authorize <action> until end of session"
```

## Verification

- Every available action is classified
- Confirmation phrasings are concrete strings
- Refusals are firm but not preachy
- Override policy is explicit
