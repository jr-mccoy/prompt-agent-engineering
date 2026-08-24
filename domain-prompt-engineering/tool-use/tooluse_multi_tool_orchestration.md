---
title: "Multi-Tool Orchestration with Dependency Tracking"
category: prompt-engineering/tool-use
description: "Plan a sequence of tool calls with explicit dependencies, parallelism, and a single retry rule per node."
techniques:
  - ST-02
  - DT-01
  - DD-06
  - QA-01
difficulty: advanced
tags:
  - tool_use
  - orchestration
  - dependency_graph
  - parallelism
  - planner
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_when_to_call_decision_prompt.md
  - domain-prompt-engineering/tool-use/tooluse_failure_recovery_pattern.md
  - domain-prompt-engineering/tool-use/tooluse_dry_run_pattern.md
  - domain-prompt-engineering/agent-workflows/
---

## Objective

Convert a user goal into a directed acyclic plan of tool calls — each node with id, tool, args (concrete or pending from a parent's output), dependencies, parallel-eligible flag, and on-error policy.

## When to Use

- The task requires ≥ 2 tool calls.
- Some calls can run in parallel; others depend on prior output.
- You need a re-runnable plan that survives partial failure.

## Inputs

```
GOAL: <one sentence>
TOOL_REGISTRY: <name, purpose, idempotent, latency_class>
KNOWN_FACTS: <args already known>
COST_BUDGET: <max calls or tokens>
PARALLEL_LIMIT: <max concurrent calls>
```

## Constraints

### Must
- Output a list of nodes. Each node: `id`, `tool`, `args` (values or `{from: "<node_id>.<path>"}`), `depends_on` (list of node ids), `parallel_group` (integer), `on_error` ∈ {`abort`, `retry_once`, `fallback:<tool>`, `ask_user`}, `idempotency_key` (for non-idempotent tools).
- Topologically valid: every `depends_on` id is defined earlier; no cycles.
- A node is `parallel_group=N` only if all its dependencies are in groups ≤ N-1.
- Total nodes ≤ COST_BUDGET; concurrent nodes per group ≤ PARALLEL_LIMIT.
- Mark every destructive node with `confirm_before_run: true`.

### Must Not
- Plan more than one fallback level (no fallback-of-fallback).
- Use the same `id` twice.
- Reference a parent's output field that does not appear in that tool's documented return shape.
- Run destructive nodes in a parallel group with a non-idempotent sibling.

## Instructions

1. Decompose GOAL into the minimum sequence of tool calls. Cut anything not on the critical path.
2. For each node, set args from KNOWN_FACTS or `{from: ...}`.
3. Build the dependency edges. Run a 3-step cycle check.
4. Assign parallel groups via topological sort (Kahn's algorithm). All sources go in group 1.
5. For each node, choose `on_error`:
   - Read-only + idempotent → `retry_once`.
   - Read-only + flaky → `fallback:<sibling>` if a sibling exists.
   - Write/destructive → `abort` and require user confirmation.
6. Emit a renderable run plan + a checkpoint hint per group (where to persist intermediate results).

## Output Format

```yaml
plan:
  - id: n1
    tool: <name>
    args: {<...>}
    depends_on: []
    parallel_group: 1
    on_error: retry_once
    idempotency_key: <stable hash if non-idempotent>
  - id: n2
    tool: <name>
    args: {x: {from: "n1.result.id"}}
    depends_on: [n1]
    parallel_group: 2
    on_error: fallback:<sibling>
    confirm_before_run: false

groups:
  1: [n1, n3]
  2: [n2]

checkpoints:
  - after_group: 1
    persist: [n1.result.id]
```

## Verification

- Every `from` reference targets a node listed in `depends_on`.
- No cycles (run a mental DFS).
- Sum of nodes ≤ COST_BUDGET.
- Every destructive tool node has `confirm_before_run: true` AND `on_error=abort`.
- `parallel_group` numbers are monotonic with dependencies.
