---
title: "Stage 7 — Stack-Specific Code-Gen (OPTIONAL, gated)"
category: agentic-system-factory/stage-7-codegen
description: "Optional. Transform the framework-agnostic design bundle into runnable scaffolding for a committed stack (any of the six supported: Claude Agent SDK, LangGraph, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, LlamaIndex), keeping the agnostic bundle as the source of truth. Output is scaffolding + specs + harness, not a deployed service. Stack code stays version-neutral inside the named stack; drifting facts (API signatures, model IDs, pricing) are flagged 'verify against current docs.'"
techniques:
  - ST-02
  - ST-03
  - CM-02
difficulty: advanced
tags:
  - code-gen
  - multi-stack
  - stack-scaffolding
  - version-neutrality
updated: "2026-07-02"
related_prompts:
  - agentic-system-factory/stacks/claude-agent-sdk.md
  - agentic-system-factory/stacks/langgraph.md
  - agentic-system-factory/stacks/openai-agents-sdk.md
  - agentic-system-factory/stacks/google-adk.md
  - agentic-system-factory/stacks/microsoft-agent-framework.md
  - agentic-system-factory/stacks/llamaindex.md
  - domain-AI-ML/learning-ai-ml/notebook-to-production/mllearn_n2p_01_refactor_notebook_to_package.md
---

# Stage 7 — Stack-Specific Code-Gen (optional, gated)

## Objective
Transform the agnostic bundle into runnable scaffolding for a committed stack. This stage **only runs when Gate C has passed and a stack is committed** (`BUNDLE_MANIFEST.md → Stack committed`).

## When to Use
- The user named/committed to a stack (in Stage 3 or now), and Gate C passed.
- Surgically via `/emit-stack-code` — which refuses if Gate C is unmet.

## Inputs / Context
- The complete, Gate-C-passed bundle.
- The committed stack — one of the six supported: `claude-agent-sdk`, `langgraph`, `openai-agents-sdk`, `google-adk`, `microsoft-agent-framework`, `llamaindex` (the agnostic bundle ships first regardless; MCP is the assumed tool-interop layer across all six).

## Constraints

**Must:**
- Treat the agnostic bundle as the **source of truth**; code-gen is a transform, never a replacement.
- Keep stack code **version-neutral inside the named stack**; flag drifting facts (API signatures, model IDs, pricing, quotas) as **"verify against current docs,"** never assert them from memory.
- Emit **scaffolding + specs + harness** (agent definitions, tool/function stubs with the designed schemas, the guardrail/policy layer, the topology wiring, the eval-harness scaffold, a runbook), not a finished deployed service.
- Carry the gates into code: the deterministic policy/allowlist becomes a pre-tool-call hook; loop bounds become `max_turns`/recursion limits; the kill switch becomes a config flag checked before action.

**Must Not:**
- Run before Gate C passes or without a committed stack.
- Invent version-specific API details; defer them to "verify against current docs."
- Drop any gate when translating to code (a hijacked agent must still be bounded by the deterministic layer).

## Instructions
1. **Confirm preconditions** — Gate C PASS + a committed stack. If either is missing, stop and route back (to Stage 6, or ask the user to commit a stack).
2. **Open the stack guide** for the committed stack (`../stacks/{claude-agent-sdk,langgraph,openai-agents-sdk,google-adk,microsoft-agent-framework,llamaindex}.md`) — for the transform map (agnostic primitive → stack construct).
3. **Translate** agents, tools, topology wiring, the guardrail/policy layer (deterministic allowlist as a hook), loop bounds, and the kill switch.
4. **Scaffold the eval harness** in the stack's idiom (capability + safety suites).
5. **Emit the runbook + a rules file** (`CLAUDE.md`/`AGENTS.md`) so a downstream coding agent can complete and deploy it.
6. **Flag every drifting fact** with "verify against current docs."

## Output Format
A stack scaffolding directory + a transform note mapping each agnostic artifact to its stack construct, with version-sensitive facts flagged.

## Verification Checklist
- [ ] Gate C passed and a stack was committed before this stage ran.
- [ ] Every gate (deterministic policy, loop bounds, kill switch) is present in the scaffolding.
- [ ] Drifting facts are flagged "verify against current docs," not asserted.
- [ ] Output is scaffolding + specs + harness, traceable back to the agnostic bundle.

## False-Positive Prevention
- An **unflagged** version-specific fact (API signature, model ID, price, quota) that happens to be stale is worse than a flagged one — it reads as verified. When in doubt, flag "verify against current docs."
- Scaffolding that compiles but drops a gate in translation (no pre-tool-call policy hook, an unbounded loop, no kill-switch flag) is a false transform — parity with `GATE_DESIGN.md` is the acceptance test, not "it runs."

## References (assembled, not duplicated)
- `agentic-system-factory/stacks/{claude-agent-sdk,langgraph,openai-agents-sdk,google-adk,microsoft-agent-framework,llamaindex}.md` — the six per-stack transform guides.
- `domain-AI-ML/learning-ai-ml/notebook-to-production/mllearn_n2p_01..04` — package → pipeline → serve → deploy/monitor scaffold.

## Produces
Stack scaffolding (transform of the agnostic bundle). The agnostic bundle remains the source of truth.
