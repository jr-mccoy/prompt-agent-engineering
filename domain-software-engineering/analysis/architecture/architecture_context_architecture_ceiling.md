---
title: "Architecture Ceiling Test (Bitter Lesson Check)"
category: analysis/architecture
description: "Run the Bitter Lesson check on an agentic system: if you swapped in a more capable model tomorrow, would your system scale or is the architecture the bottleneck?"
techniques:
  - ST-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - architecture
  - agentic-systems
  - context-engineering
  - scalability
updated: "2026-04-17"
related_prompts: []
---

# Architecture Ceiling Test

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me run the Bitter Lesson check on my agentic system architecture.

The question: if I swapped in a more capable model tomorrow, would my system's capabilities increase proportionally — or is my architecture the bottleneck?

Signs the architecture is the bottleneck:
- Hard-coded decision trees that a smarter model could handle dynamically
- Aggressive summarization that throws away information a smarter model could use
- Rigid tool schemas that prevent flexible tool use
- Multi-agent splits that exist because the model "couldn't handle it" rather than for genuine clarity

Signs the architecture scales with model capability:
- The model sees all relevant information and decides what matters
- Constraints are expressed as goals, not as hard-coded rules
- The system would benefit from better reasoning with no code changes

Help me audit my design for artificial ceilings.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to identify where my architecture might be the bottleneck. Start now.
```

## Usage Notes

This prompt helps identify architectural decisions that artificially limit system capabilities. Based on the "Bitter Lesson" principle: architectures that scale with model capability will outperform those with hard-coded limitations as models improve.
