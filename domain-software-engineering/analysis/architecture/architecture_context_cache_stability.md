---
title: "KV Cache Stability Optimization"
category: analysis/architecture
description: "Audit agentic prompt structure for KV cache reuse — classify content as stable-prefix, semi-stable, or volatile, and reorder to maximize cache hit rate for cost and latency savings."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - architecture
  - agentic-systems
  - context-engineering
  - kv-cache
  - performance
updated: "2026-04-17"
related_prompts: []
---

# Cache Stability Optimization

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me optimize KV cache reuse for an agentic system. This is where real cost and latency savings come from.

The principle: tokens that remain identical across steps can reuse cached key-value computations. Tokens that change invalidate the cache from that point forward.

Help me audit my prompt structure:
- **Stable prefix** — System prompt, instructions, and context that never changes mid-session
- **Semi-stable sections** — Content that changes occasionally (e.g., phase transitions)
- **Volatile sections** — Content that changes every step (should be at the END of the prompt)

For each component, ask me:
- Does this actually need to change between steps?
- Can I move volatile information later in the prompt?
- Am I introducing non-determinism (timestamps, random IDs) that kills cache hits?

The goal is a prompt structure where 70%+ of tokens are cache-stable across consecutive steps.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to optimize cache stability. Start now.
```

## Usage Notes

This prompt helps optimize for KV cache reuse, which provides significant cost and latency savings. The key is structuring prompts so stable content comes first and volatile content comes last, maximizing cache hits across consecutive steps.
