---
title: "Context View Compilation Design"
category: analysis/architecture
description: "Design the view compilation layer that takes full session state and produces minimal per-step context — context window is computed, not accumulated."
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
  - view-compilation
  - state-management
updated: "2026-04-17"
related_prompts: []
---

# View Compilation Design

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me design the view compilation layer for an agentic system — the component that takes the full session state and produces the minimal context for each step.

The core principle: the context window is computed, not accumulated. The session state is authoritative. The view is small, relevant, and scoped to the current action.

I'm going to describe my agent's workflow. For each step type, help me define:
- What MUST be in the view (the model cannot act without it)
- What SHOULD be in the view (improves quality but isn't essential)
- What should be REFERENCED but not included (the model knows it exists and can fetch it)
- What should be EXCLUDED entirely (irrelevant or distracting)

Challenge me if I'm including too much. The goal is the smallest view that produces correct behavior.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to design this view compiler. Start now.
```

## Usage Notes

This prompt helps design the view compilation layer that produces minimal, relevant context for each step. The key insight is that context should be computed from authoritative state, not accumulated from conversation history.
