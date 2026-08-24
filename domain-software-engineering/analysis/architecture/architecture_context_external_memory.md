---
title: "External Memory Architecture"
category: analysis/architecture
description: "Decide what belongs in the context window (semantic memory as compact summaries) versus external storage (procedural memory: artifacts, code, logs, plans) for an agentic system."
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
  - memory-design
updated: "2026-04-17"
related_prompts: []
---

# External Memory Architecture

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me decide what belongs in the context window versus external memory (files, databases, scratchpads) for an agentic system.

The principle: semantic memory (what things mean) belongs in the window as compact summaries. Procedural memory (artifacts, code, logs, outputs, plans) belongs in external storage, referenced but not loaded until needed.

For my agent, help me draw this line clearly:
- What should be summarized into bullets or sentences and kept in-context?
- What should be written to files and only loaded on demand?
- What needs a structured store (database, vector store) for retrieval?
- What's intermediate work product that should be checkpointed but rarely re-read?

The goal is an agent that can operate over large bodies of work without drowning in its own output.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to design this external memory architecture. Start now.
```

## Usage Notes

This prompt helps distinguish between semantic memory (kept in-context as summaries) and procedural memory (stored externally). The goal is an agent that can scale to large projects without context window overflow.
