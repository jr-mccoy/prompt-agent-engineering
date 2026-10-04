# Orchestration Agents

> Specialized agents for AI context management, multi-agent fan-out and gather, repository curation, and intelligent memory systems.

## Available Agents

| Agent | Model | Description |
|-------|-------|-------------|
| [context-manager](context_manager.md) | INHERIT | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory systems. Orchestrates context across multi-agent workflows and enterprise AI systems. |
| [prompt-kit-ingestor](prompt-kit-ingestor.md) | SONNET | Repository curator that absorbs external prompt kits into structured, technique-tagged, indexed repository prompts via the external-prompt-kit-ingestor skill. |
| [task-decomposition-coordinator](task_decomposition_coordinator.md) | OPUS | Splits one concrete task into parallel subtasks with a dependency graph, disjoint write ownership, and per-subtask handoff contracts. Returns a dispatch plan; does not spawn workers. |
| [result-reconciler](result_reconciler.md) | SONNET | Merges parallel worker outputs: contract check, deduplication with stated rules, conflict detection, and a traceable reconciliation log. Flags substantive conflicts instead of picking a winner. |

## Model Assignments

- **INHERIT**: Allows user to choose model based on orchestration complexity and requirements
- **OPUS**: Task decomposition, where a bad split multiplies cost across every worker
- **SONNET**: Structured curation and reconciliation work with clear contracts

## Fan-out / gather pair

`task-decomposition-coordinator` plans the split and writes handoff contracts; the calling session dispatches the workers; `result-reconciler` merges what comes back against those contracts. Design-time questions (whether to go multi-agent, which topology) belong to `commands/multi-agent/` and `domain-AI-ML/agentic-ai-systems/`.

## Related Resources

- [Parent: Agents Overview](../README.md)
- [Skills: Orchestration](./)
