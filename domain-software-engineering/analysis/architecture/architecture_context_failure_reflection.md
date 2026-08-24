---
title: "Failure Reflection System Design"
category: analysis/architecture
description: "Design a structured failure reflection system for an agent: feedback capture, memory delta format, replay strategy, and brittleness guardrails so agents neither ignore failures nor over-correct."
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
  - failure-handling
  - learning
updated: "2026-04-17"
related_prompts: []
---

# Failure Reflection System

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me design a failure reflection system for an agentic agent — how mistakes get captured and integrated into future behavior.

The problem: most agents either ignore failures (and repeat them) or over-correct (and become brittle). I need a structured approach.

Help me design:
- **Feedback capture** — How does the agent know something went wrong? (explicit error, user correction, verification failure, timeout)
- **Memory delta format** — What gets written to memory? (not a narrative, but a structured record: what was attempted, what failed, what to do differently)
- **Integration rules** — When does this feedback enter the context? (always? only when similar situations arise? only when explicitly retrieved?)
- **Decay and revision** — When does old failure memory get updated or removed?

The goal is an agent that learns from mistakes without accumulating an ever-growing list of warnings that crowds out useful context.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to design this reflection system. Start now.
```

## Usage Notes

This prompt helps design a balanced failure reflection system that avoids both ignoring failures (leading to repetition) and over-correcting (leading to brittleness). The structured approach ensures failures are captured, integrated, and eventually decayed appropriately.
