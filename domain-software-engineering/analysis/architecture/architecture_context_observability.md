---
title: "Context Observability Audit"
category: analysis/architecture
description: "Design observability for an agentic system so you can answer 'what does the agent know right now, and why?' — covers context contents inspection, provenance tracing, and decision audit."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
difficulty: advanced
tags:
  - architecture
  - agentic-systems
  - context-engineering
  - observability
  - debugging
updated: "2026-04-17"
related_prompts: []
---

# Context Observability Audit

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me build context observability for an agentic system — the ability to answer "what does the agent actually know right now, and why?"

This is the litmus test of production readiness. If I can't trace what's in the context and why, I can't debug failures, I can't audit decisions, and I can't trust the system.

Help me design observability for:
- **Context contents** — At any step, can I inspect exactly what's in the window?
- **Provenance** — For each piece of context, can I trace where it came from? (user input, tool output, memory retrieval, summarization)
- **Inclusion rationale** — Why was this included? What triggered its retrieval or retention?
- **Exclusion log** — What was available but not included, and why?

The goal is a system where I can replay any decision, see exactly what the model saw, and understand why it saw that.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to design this observability layer. Start now.
```

## Usage Notes

This prompt helps design context observability, which is essential for production-ready agentic systems. Without the ability to trace what's in context and why, debugging, auditing, and trust are impossible.
