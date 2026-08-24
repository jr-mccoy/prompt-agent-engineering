---
title: "Multi-Agent Scope Design"
category: analysis/architecture
description: "Decide whether and how to split an agentic system into multiple agents. Separates valid splits (planning/execution, verification/generation) from persona-driven anti-patterns."
techniques:
  - ST-01
  - RT-02
  - RT-03
  - CM-02
difficulty: advanced
tags:
  - architecture
  - agentic-systems
  - context-engineering
  - multi-agent
  - scope-design
updated: "2026-04-17"
related_prompts: []
---

# Multi-Agent Scope Design

**Source:** CONTEXT_ENGINEERING_PROMPTS.md
**Category:** Context Engineering / Agentic Systems

## Prompt

```
You are helping me decide whether and how to split my agentic system into multiple agents — and if so, how to handle scope boundaries.

The right question is not "what personas should I create?" but "what work requires a separate context window for clarity or correctness?"

Valid reasons to split:
- **Planning vs execution** — The planner shouldn't see execution noise; the executor shouldn't re-derive the plan
- **Verification vs generation** — The verifier needs a clean window uncorrupted by the generator's reasoning
- **Knowledge management vs action** — One agent curates context; another agent acts on it

Invalid reasons to split:
- "It feels like a different role"
- "I want a PM agent and an engineer agent"
- Anthropomorphizing the architecture

For each potential split, help me answer: "What gets clearer or more correct with separate windows?" If I can't answer that, the split is probably wrong.

Here's my agent: [DESCRIBE YOUR AGENT]

Ask me one question at a time to evaluate whether multi-agent design is warranted. Start now.
```

## Usage Notes

This prompt provides a rigorous framework for deciding when to use multi-agent architecture. The key question: "What gets clearer or more correct with separate windows?" Avoid splits based on anthropomorphizing (PM agent, engineer agent) rather than genuine architectural needs.
