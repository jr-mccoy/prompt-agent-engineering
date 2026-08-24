# Tool Use

**Purpose:** Patterns for designing, selecting, invoking, and recovering tool calls — from naming conventions to dry-run protocols for irreversible actions.

## When to use this subdirectory

- Adding tools to an agent or LLM application.
- Misrouting between tools, fabricated arguments, missing confirmations, or unbounded retries.
- Designing multi-tool workflows with dependencies, parallelism, and failure recovery.

## Prompts

| File | Description |
|------|-------------|
| `tooluse_tool_description_writer.md` | Write tool descriptions with explicit "use when / do not use when" so routing works on first try. |
| `tooluse_when_to_call_decision_prompt.md` | Force a typed route — `call_tool`, `answer_directly`, or `ask_user` — with confidence and freshness checks. |
| `tooluse_argument_extraction_prompt.md` | Extract typed args from messy text with `evidence_span`, confidence, and `__missing[]`. |
| `tooluse_multi_tool_orchestration.md` | Plan a DAG of tool calls with dependencies, parallel groups, and per-node `on_error`. |
| `tooluse_tool_result_interpretation.md` | Turn raw tool output into a grounded user-facing answer; cite fields; surface errors faithfully. |
| `tooluse_failure_recovery_pattern.md` | Classify a tool error and choose retry / fallback / ask / escalate from a typed table. |
| `tooluse_disambiguation_pattern.md` | Detect ambiguity before destructive tool calls; emit one targeted question with candidates. |
| `tooluse_tool_set_minimization.md` | Find the smallest tool set that covers a task class; flag merges and deletions. |
| `tooluse_tool_naming_convention.md` | `<verb>_<object>[_<qualifier>]` pattern with allowed verb set, scope qualifiers, migration table. |
| `tooluse_dry_run_pattern.md` | Propose → confirm → execute protocol with idempotency keys for irreversible actions. |

## How they compose

- **Design tools**: `tooluse_tool_naming_convention` + `tooluse_tool_description_writer` + `tooluse_tool_set_minimization`.
- **Per-call decision flow**: `tooluse_when_to_call_decision_prompt` → `tooluse_argument_extraction_prompt` → `tooluse_disambiguation_pattern` → `tooluse_dry_run_pattern` (if destructive) → call → `tooluse_tool_result_interpretation`.
- **When things break**: `tooluse_failure_recovery_pattern` decides retry vs fallback vs escalate; `tooluse_multi_tool_orchestration` carries it across multiple nodes.
