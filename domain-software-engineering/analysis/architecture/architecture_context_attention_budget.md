---
title: "Attention Budget Allocation"
category: analysis/architecture
description: "Sort every piece of information an agent handles into four tiers (must-see, must-know-exists, fetch-on-demand, never-read-again) to minimize context window size without breaking behavior."
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
  - context-window
  - cost-optimization
updated: "2026-04-17"
related_prompts: []
---

# Attention Budget Allocation

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me allocate the attention budget for an agentic system. Context window space is finite and expensive. Every token included is a token of attention spent.

Help me sort every piece of information my agent handles into four tiers:

1. **Must see** — In the window for every step, no exceptions
2. **Must know exists** — Referenced in the prompt but content not included; agent knows it can ask for it
3. **Fetch when needed** — Not mentioned until relevant; retrieved on demand
4. **Never read again** — Processed once, compressed or discarded, never re-read in full

For each item, challenge me: "What breaks if this moves down one tier?" If nothing breaks, it should move down.

The goal is a context window that's as small as possible while still producing correct behavior — for cost, coherence, and debuggability.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to build this attention budget. Start now.
```

## Usage Notes

This prompt helps optimize context window usage by forcing rigorous tier classification. The key test for each item: "What breaks if this moves down one tier?" If nothing breaks, it should move down.
