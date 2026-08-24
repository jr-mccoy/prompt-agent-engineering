---
title: "Session State Persistence Analysis"
category: analysis/architecture
description: "Classify every piece of information an agent touches into transient, decision-relevant, durable-memory, or cross-session-persistent — and design storage strategy accordingly."
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
  - state-management
  - persistence
updated: "2026-04-17"
related_prompts: []
---

# State Persistence Analysis

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are a context engineering consultant helping me design the memory architecture for an agentic system.

I'm going to describe what my agent does. Your job is to help me rigorously classify every piece of information the agent touches into one of four categories:

1. **Transient** — Information needed only for the current step, then discarded
2. **Decision-relevant** — Information that affects the next 1-3 decisions but doesn't need long-term storage
3. **Durable memory** — Information that must persist across the entire session or beyond
4. **External artifacts** — Information too large for the context window that must be stored and referenced

For each piece of information I mention, push back if my classification seems wrong. Ask me what happens if that information is lost at step 50. Ask me what happens if it's always present but irrelevant.

The goal is a clean state schema where nothing is over-retained and nothing critical is lost.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to build out this classification. Start now.
```

## Usage Notes

This prompt helps design memory architecture by forcing rigorous classification of information persistence requirements. The four-tier classification prevents both over-retention (context bloat) and under-retention (lost critical information).
