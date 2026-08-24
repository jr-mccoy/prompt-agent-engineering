# AI-Native Rollouts

Prompts for the organizational work of rolling out AI tools and agentic workflows — beyond individual prompting technique. These address the questions teams actually hit once AI moves from experimentation to production: who adopts it and how, how to keep code review signal-to-noise high, how to delegate in the way a competent manager would, how to give projects memory, and how to migrate load-bearing organizational functions safely.

## When to Use This Cluster

- A team is standing up AI tools at organizational scale, not just individual use.
- An AI deployment (code review, delegation practice, project memory) needs redesign because the naive version collapsed into noise or drift.
- Leadership has asked "let's use AI for X" and the team needs a rigorous plan before executing.
- A team is hitting the point where individual AI use patterns diverge and a shared practice is required.

## Prompts

| # | Prompt | Use When |
|---|--------|----------|
| 1 | [`airollout_ambient_code_review.md`](airollout_ambient_code_review.md) | Standing up (or fixing) an AI code-review layer that teams actually accept rather than silently ignore. |
| 2 | [`airollout_tiered_adoption_rollout.md`](airollout_tiered_adoption_rollout.md) | Rolling out AI tools across 10–500 engineers without treating everyone the same — Ignore / Use / Build With. |
| 3 | [`airollout_ship_without_writing_code.md`](airollout_ship_without_writing_code.md) | Runbook for shipping a real PR entirely through AI delegation — a deliberate learning exercise. |
| 4 | [`airollout_delegate_like_parallel_coworker.md`](airollout_delegate_like_parallel_coworker.md) | Designing a reusable delegation brief template calibrated to a specific task class. |
| 5 | [`airollout_long_running_project_memory.md`](airollout_long_running_project_memory.md) | Designing persistent project memory with file layout, update protocol, and decay checks — beyond a stub CLAUDE.md. |
| 6 | [`airollout_bottleneck_migration_plan.md`](airollout_bottleneck_migration_plan.md) | Planning the migration of a load-bearing organizational function to AI — staged, with guardrails, kill switch, and predicted next bottleneck. |

## Cross-References

- AI-augmented development at the individual-workflow level: [`../ai-patterns/`](../ai-patterns/)
- Memory scaffolds at the personal / role level: [`../../domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md`](../../domain-business-strategy/chief-of-staff/cos_memory_scaffold_claude_md.md)
- Agent task design: [`../ai-patterns/ai_pattern_agent_task_first_delegation_spec.md`](../ai-patterns/ai_pattern_agent_task_first_delegation_spec.md)
- Multi-agent architecture: [`../../domain-agentic-resources/commands/multi-agent/`](../../domain-agentic-resources/commands/multi-agent/)
- AI strategy & capability compounding: [`../../domain-business-strategy/ai-strategy/`](../../domain-business-strategy/ai-strategy/)
- Vibe-coding rescue (project-level AI code health): [`../../domain-software-engineering/vibe-coding-rescue/`](../../domain-software-engineering/vibe-coding-rescue/)

## Design Principles

- **Phased, not one-cut.** Every rollout prompt requires staged deployment with exit criteria, not a single-step flip.
- **Tier-aware.** People are not uniformly ready; plans that treat them as such fail predictably. Three tiers (Ignore / Use / Build With) with migration rules in both directions.
- **Signal > noise.** AI systems that post too much get ignored, even when sometimes correct. Caps, confidence requirements, dismiss-rate tracking, and drift reviews prevent signal decay.
- **Human accountability remains named.** Migration of function does not migrate accountability. Every plan keeps a kill switch and a named owner.
- **Memory separated by decay rate.** Constitutional / Architectural / Active / Session-local are different kinds of context with different update cadences.
