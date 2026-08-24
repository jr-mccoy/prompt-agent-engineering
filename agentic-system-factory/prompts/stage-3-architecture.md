---
title: "Stage 3 — Design the Architecture (+ stack-selection sub-step)"
category: agentic-system-factory/stage-3-architecture
description: "Turn the chosen topology into a concrete design: agents and seams (one AGENT_SPEC each), tools as an Agent-Computer Interface (one TOOL_SPEC each), context/durability strategy, and cost/model right-sizing. Includes the stack-selection sub-step that decides whether Stage 7 code-gen will run (commit to a stack now, or defer and stop at the agnostic bundle)."
techniques:
  - ST-01
  - ST-02
  - CM-02
difficulty: advanced
tags:
  - architecture
  - tool-design
  - context-engineering
  - stack-selection
updated: "2026-07-02"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_tool_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_context_engineering_at_scale.md
---

# Stage 3 — Design the Architecture

## Objective
Make the topology concrete. Fill `ARCHITECTURE.md §4`, one `AGENT_SPEC` per agent, one `TOOL_SPEC` per tool, and decide the **stack-selection** question that gates Stage 7.

## When to Use
- After Stage 2 topology selection.

## Inputs / Context
- Topology + primitives (`ARCHITECTURE.md §3`), blast radius (`§1`).
- Whether the user already knows their target stack.

## Constraints

**Must:**
- Produce one `AGENT_SPEC` (from [`../templates/AGENT_SPEC_TEMPLATE.md`](../templates/AGENT_SPEC_TEMPLATE.md)) per agent, including the authority boundary (Can-Do / Ask-First / Never) and a minimized tool set.
- Produce one `TOOL_SPEC` (from [`../templates/TOOL_SPEC_TEMPLATE.md`](../templates/TOOL_SPEC_TEMPLATE.md)) per tool: built around a high-impact workflow (not an API endpoint), errors-as-guidance, idempotency + dry-run for destructive calls.
- Choose a per-hop context strategy and apply long-horizon techniques where relevant.
- Right-size models per agent (cheap for classify/extract/format; strong for reasoning/synthesis).
- Record the **stack-selection decision**: `none` (defer; stop at the agnostic bundle) or a committed stack — any of the six Stage-7 targets: `claude-agent-sdk` | `langgraph` | `openai-agents-sdk` | `google-adk` | `microsoft-agent-framework` | `llamaindex` (transform guides in [`../stacks/`](../stacks/)).

**Must Not:**
- Add tools that don't serve a workflow ("more tools ≠ better").
- Persist raw context where a condensed summary suffices (sub-agent isolation).
- Commit to a stack the user hasn't chosen — defer is a valid, common outcome.

## Instructions
1. **Component / agent map** — draw the topology (`§4.1`); for each agent fill an `AGENT_SPEC`.
2. **Tools (ACI)** — for each tool fill a `TOOL_SPEC`. Consolidate multi-call flows; namespace related tools; return semantic identifiers; make error messages actionable guidance.
3. **Seams** (`§4.2`) — every boundary where control/data crosses, with the validation applied there (especially untrusted-content seams → data/control separation).
4. **Context / durability** (`§4.3`) — per-hop full-raw vs summary vs fresh-instruction-only; apply compaction / agentic note-taking / sub-agent isolation; persist state externally for resumable work.
5. **Cost / model right-sizing** (`§4.4`) — model per agent + expected tokens/run.
6. **System-prompt altitude** (`§4.5`) — note where prompts are intentionally heuristic vs prescriptive.
7. **Stack-selection sub-step** — ask whether the user commits to a stack now. Record the decision in `BUNDLE_MANIFEST.md` (`Stack committed`). If `none`, the bundle terminates at Stage 6; if committed, Stage 7 becomes available **after Gate C passes**.

## Output Format
`ARCHITECTURE.md §4`, the `agents/*.md` specs, the `tools/*.md` specs, and the recorded stack-selection decision.

## Verification Checklist
- [ ] Each agent has a spec with an authority boundary and minimized tools.
- [ ] Each tool has a spec (workflow-shaped, errors-as-guidance, idempotency/dry-run where destructive).
- [ ] Seams list the validation at each boundary.
- [ ] Context strategy + state persistence chosen; long-horizon techniques applied where relevant.
- [ ] Models are right-sized per agent.
- [ ] Stack-selection decision recorded (`none` or a committed stack).

## False-Positive Prevention
- An `AGENT_SPEC`/`TOOL_SPEC` that restates the template headings with generic text is a false spec — each must be implementable as written: an authority boundary with concrete Never items, tool errors that tell the model what to do next, real schemas. If a downstream coding agent would have to guess, the spec isn't done.
- Recording a stack the *author* prefers as "committed" is a false commitment — only the user commits a stack, and `none` (defer to the agnostic bundle) is the default outcome, not a failure.

## References (assembled, not duplicated)
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md`; `aiagent_tool_design.md`; `aiagent_memory_design.md`; `aiagent_cost_token_budget_design.md`; `aiagent_context_engineering_at_scale.md`; `aiagent_failure_mode_analysis.md`.
- `domain-AI-ML/genai-llm-engineering/` — RAG/retrieval when memory is retrieval-backed.

## Produces
`ARCHITECTURE.md §4` + `agents/*` + `tools/*` + stack-selection decision → feeds Stage 4 (gates) and (if committed) Stage 7.
