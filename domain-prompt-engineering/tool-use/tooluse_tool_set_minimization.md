---
title: "Tool Set Minimization for a Task Class"
category: prompt-engineering/tool-use
description: "Find the smallest tool set that fully covers a task class, ranked by per-tool routing confusion and cost."
techniques:
  - ST-02
  - DT-04
  - CM-03
  - NE-09
difficulty: advanced
tags:
  - tool_use
  - minimization
  - tool_set
  - routing
  - cost
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/tool-use/tooluse_tool_description_writer.md
  - domain-prompt-engineering/tool-use/tooluse_tool_naming_convention.md
  - domain-prompt-engineering/agent-workflows/
---

## Objective

For a defined task class and a candidate tool catalog, return the minimum subset of tools that covers all task instances, plus removed tools and the routing improvement expected.

## When to Use

- An agent has 20+ tools and routing accuracy has dropped.
- Several tools have overlapping verbs ("get", "fetch", "list").
- You suspect dead tools that were added "just in case".

## Inputs

```
TASK_CLASS: <description + 5-10 representative user messages>
TOOL_CATALOG: <each tool with name, description, args, return shape>
USAGE_LOGS: <optional: per-tool call count over last N days>
COST_PER_CALL: <per tool>
ROUTING_FAILURES: <optional: examples where wrong tool was picked>
```

## Constraints

### Must
- Output `keep[]`, `remove[]`, `merge[]`. Every TOOL_CATALOG entry appears in exactly one list.
- For every task instance in TASK_CLASS, at least one `keep` tool covers it; document the mapping.
- A tool is `remove` only if (a) zero task instances need it, OR (b) `USAGE_LOGS` show < 1% of calls AND another `keep` tool covers its capability.
- A `merge` proposes combining two tools; both originals appear under `merge` with a target name and migration note.
- Justify each `remove` with one of: `unused`, `redundant_with:<keep_tool>`, `out_of_scope`.

### Must Not
- Remove a tool used for an irreversible action (audit trail, undo) without explicit replacement.
- Merge tools with different idempotency or destructive flags.
- Keep two tools whose descriptions differ by < 10 words and whose args overlap > 80%.

## Instructions

1. Build a coverage matrix: rows = task instances, columns = tools, cells = `covers / partial / no`.
2. Run greedy set cover: pick the tool that covers the most uncovered tasks; repeat until all covered.
3. For each unpicked tool, classify as `remove` or `merge` candidate.
4. Compute confusion score per kept-tool pair: shared verbs + arg-overlap + description-bigram-overlap. Flag pairs with score > threshold for renaming or merging.
5. Estimate routing improvement: assume confusion → misroute rate. Report `(catalog_size_before, catalog_size_after, expected_misroute_drop)`.

## Output Format

```yaml
keep:
  - name: <tool>
    covers: [<task_ids>]
    rationale: <one line>
remove:
  - name: <tool>
    reason: unused | redundant_with:<keep> | out_of_scope
merge:
  - from: [<tool_a>, <tool_b>]
    into: <new_name>
    migration_note: <one line>
coverage_check:
  uncovered_tasks: []   # must be empty
confusion_pairs:
  - [<a>, <b>]: score=<n>; action=rename|merge
expected_routing_improvement:
  catalog_before: <n>
  catalog_after: <n>
  misroute_drop_estimate: <n>%
```

## Verification

- `uncovered_tasks` is empty.
- Sum of |keep| + |remove| + nodes in |merge| = |TOOL_CATALOG|.
- No tool appears in two lists.
- Every `remove` has a stated reason from the allowed set.
- No merged pair has differing destructive or idempotency flags.
