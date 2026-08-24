---
name: emit-stack-code
description: "Surgical Stage-7 run: transform the Gate-C-passed agnostic bundle into stack-specific scaffolding for any of the six supported stacks (Claude Agent SDK, LangGraph, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, LlamaIndex). Refuses if Gate C is unmet — surgical jumps between gates, never through one."
version: "1.0.0"
category: orchestration
tags: [agentic-system, code-gen, stage-7, surgical]
agents_used: [system-architect]
---

# /emit-stack-code — Stage 7 (surgical, gated)

## Context
Transform the agnostic bundle into runnable scaffolding for a committed stack. **Hard precondition: Gate C must pass and a stack must be committed.** The command runs Gate C first and refuses on failure.

## Requirements
- A Gate-C-passed bundle + a committed stack (one of: `claude-agent-sdk` | `langgraph` | `openai-agents-sdk` | `google-adk` | `microsoft-agent-framework` | `llamaindex`).

## Stages routed & gates enforced
- Stage 7; runs Gate C as a precondition and refuses if it fails (no routing through Gate C).

## Scripts this command runs
```bash
python3 scripts/validate_bundle.py ./bundle && \
python3 scripts/check_gate.py --gate C ./bundle && \
python3 scripts/score_rubric.py ./bundle    # all must exit 0 before any code is emitted
```

## Hand-off
Stage prompt: `prompts/stage-7-codegen.md`; then the committed stack's transform guide in `stacks/` (six available: `claude-agent-sdk`, `langgraph`, `openai-agents-sdk`, `google-adk`, `microsoft-agent-framework`, `llamaindex`).

## Output Format
Stack scaffolding (transform of the agnostic bundle), version-sensitive facts flagged "verify against current docs."
