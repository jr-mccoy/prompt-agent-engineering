---
title: "Summarization Schema Design"
category: analysis/architecture
description: "Design a safe summarization schema that preserves causal steps, active constraints, and decision justifications so summarization doesn't silently destroy agent-critical information."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
difficulty: advanced
tags:
  - architecture
  - agentic-systems
  - context-engineering
  - summarization
  - compression
updated: "2026-04-17"
related_prompts: []
---

# Summarization Schema Design

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me design a safe summarization schema for an agentic system.

The problem: summarization destroys information. Most teams summarize "to save space" without specifying what must be preserved. Then the agent fails at step 47 because a critical constraint was compressed away.

Before I summarize anything, I need a schema that specifies:
- **Causal steps** — The chain of decisions and why they were made
- **Active constraints** — Rules, limits, and requirements still in effect
- **Failures and dead ends** — What was tried and didn't work (to prevent loops)
- **Open commitments** — Promises made that haven't been fulfilled
- **Key entities** — Names, IDs, references that must remain resolvable

Help me define this schema for my agent. For each field, ask me: "If this were lost, what would go wrong?" If I can't answer, the field is probably unnecessary. If I can answer, the field is mandatory.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to build this summarization schema. Start now.
```

## Usage Notes

This prompt prevents the common failure mode of summarizing away critical information. The schema approach forces explicit decisions about what must be preserved, rather than hoping the model will "know" what matters.
