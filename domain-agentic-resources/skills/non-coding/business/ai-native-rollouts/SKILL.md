---
name: ai-native-rollouts
description: Plan and execute team or organization adoption of AI tools and agentic workflows — ambient code review, tiered rollouts, ship-without-coding patterns, parallel coworker delegation, long-running project memory, and bottleneck migration. Use when leading an AI-tooling rollout, when adoption has stalled past early enthusiasts, or when an org's processes haven't kept up with what AI can now do.
metadata:
  tags:
    - ai-adoption
    - team-process
    - change-management
    - agentic-workflows
  updated: "2026-05-05"
---

# AI-Native Rollouts

AI tools land easily on the tech stack and badly on team processes. The skill of rolling them out isn't picking the model — it's redesigning how work flows through the team so AI capabilities are used at the right point and the human review is at the right point. This skill bundles six workflows covering the most common rollout problems.

## When to Use This Skill

- Leading an AI-tooling rollout for a team or org
- Adoption stalled after the early enthusiasts; the rest of the team hasn't moved
- Code reviews have become bottlenecks because more code is being produced
- A senior person has become the bottleneck because they're the only one who can use AI effectively
- The org has AI tools but no policy on what they're for, where they shouldn't be used, and what review is required

## Workflows

This skill routes to six workflows in `domain-engineering-workflows/ai-native-rollouts/`.

### 1. Ambient Code Review (`airollout_ambient_code_review.md`)

**Trigger:** "Code review is the bottleneck and getting worse."

Designs an ambient AI review system that runs continuously on every PR, surfaces specific concerns rather than generic comments, and frees human reviewers to focus on architecture and judgment calls. Includes the policy decisions: what blocks merge, what's advisory, where humans must still weigh in.

Output: rollout plan, integration points, escalation rules.

### 2. Tiered Adoption Rollout (`airollout_tiered_adoption_rollout.md`)

**Trigger:** "Half the team is using AI tools fluently and half isn't."

Designs a tiered rollout — observers, users, advanced users — with clear progression criteria, training, and the work patterns each tier is expected to adopt. Acknowledges that uniform mandates fail and uniform "use AI however you want" produces uneven outcomes.

Output: tier definitions, criteria for moving between tiers, support structure.

### 3. Ship Without Writing Code (`airollout_ship_without_writing_code.md`)

**Trigger:** "Non-engineers want to contribute changes; engineering keeps saying no."

Plans a real, shippable change executed by a non-engineer with AI assistance — copy update, config tweak, small feature flag, dashboard wiring. Names the safety net (review, rollback, scope), the artifact produced (PR), and the lesson the org gets from one successful round.

Output: a candidate change, a step-by-step plan, the safety boundaries.

### 4. Delegate Like a Parallel Coworker (`airollout_delegate_like_parallel_coworker.md`)

**Trigger:** "I'm using AI like a fancy autocomplete and not getting much out of it."

Reframes individual AI use as parallel delegation — running multiple agents on independent subtasks rather than one chat-shaped conversation. Includes the patterns for clean briefs, isolation boundaries, and synthesis of parallel results.

Output: a delegation playbook tied to the user's actual task list.

### 5. Long-Running Project Memory (`airollout_long_running_project_memory.md`)

**Trigger:** "Every AI session starts from zero and re-asks the same questions."

Builds the persistent memory layer for a project — `CLAUDE.md`, decision log, glossary, index of where things live. Names what stays per-session vs. cross-session, what gets compacted, and how memory is updated as the project evolves.

Output: a memory-layer scaffold tailored to the project's domain.

### 6. Bottleneck Migration Plan (`airollout_bottleneck_migration_plan.md`)

**Trigger:** "We have a process bottleneck (review, ops, support) that an AI agent could partially absorb."

Plans the migration of a specific organizational bottleneck from human-only to AI-assisted, with explicit failure modes, escalation triggers, and metrics for whether the migration is working. Treats this as change management, not a tooling decision.

Output: migration plan, risks, success criteria, rollback condition.

## Routing Decision Tree

```
What's the symptom?
│
├── "Code review is the bottleneck"
│   → Workflow 1: Ambient Code Review
│
├── "Adoption is uneven across the team"
│   → Workflow 2: Tiered Adoption Rollout
│
├── "Non-engineers want to contribute"
│   → Workflow 3: Ship Without Writing Code
│
├── "I'm not getting enough leverage from AI personally"
│   → Workflow 4: Delegate Like a Parallel Coworker
│
├── "AI sessions can't accumulate context"
│   → Workflow 5: Long-Running Project Memory
│
└── "An org-wide bottleneck (ops, support, review) needs to move to AI"
    → Workflow 6: Bottleneck Migration Plan
```

## Recommended Sequence for a Full Rollout

If standing up AI practice from scratch:

1. **Long-Running Project Memory** — establishes the memory infrastructure all other workflows depend on
2. **Tiered Adoption Rollout** — sets up who does what, when
3. **Delegate Like a Parallel Coworker** — gives advanced-tier users the leverage pattern
4. **Ambient Code Review** — makes the increased throughput sustainable
5. **Ship Without Writing Code** — extends value beyond engineering
6. **Bottleneck Migration Plan** — apply to specific problem areas as they surface

## Cross-Cutting Considerations

### Policy decisions every rollout must make

- **What's blocked vs. advisory** in AI review? What can a human override?
- **What data can flow to which provider?** PII, customer data, source code visibility
- **Who owns AI-generated artifacts?** PRs need a human author of record
- **What's the rollback story?** When AI ships something wrong, how does it get reverted, and who's accountable?

### Metrics to track

- Time from PR opened to merge (AI review should reduce this)
- Defect escape rate (AI review should not increase this)
- Tier-2/3 adoption rate (proportion of team using AI for delegation, not just autocomplete)
- Bottleneck throughput (for whichever bottleneck is being migrated)
- Memory artifact freshness (when was CLAUDE.md last updated?)

## Companion Skills

- `vibe-coding-rescue` — for projects that adopted AI fast and now need help recovering
- `model-evaluation-harness` (skills/ml-ai/) — if the rollout includes evaluating AI features
- `keyword-cluster-generation` (skills/seo-marketing/) — if the rollout includes content team adoption

## Related Resources

The source prompts live at:
- ../../../domain-engineering-workflows/ai-native-rollouts/airollout_ambient_code_review.md
- ../../../domain-engineering-workflows/ai-native-rollouts/airollout_tiered_adoption_rollout.md
- ../../../domain-engineering-workflows/ai-native-rollouts/airollout_ship_without_writing_code.md
- ../../../domain-engineering-workflows/ai-native-rollouts/airollout_delegate_like_parallel_coworker.md
- ../../../domain-engineering-workflows/ai-native-rollouts/airollout_long_running_project_memory.md
- ../../../domain-engineering-workflows/ai-native-rollouts/airollout_bottleneck_migration_plan.md

These prompts are the executable workflows; this SKILL.md is the routing layer.

## Anti-Patterns to Avoid

- **Mandating uniform adoption** — failure rate is high, resentment compounds
- **No policy on data flow** — PII or customer data ends up in third-party providers, then a compliance fire
- **Ambient review without escalation rules** — every AI nit becomes a blocking comment
- **Long-running memory that nobody updates** — stale context is worse than no context
- **Migrating a bottleneck without success criteria** — you don't know if it worked, and you can't roll back cleanly
- **Skipping tiered design** — putting non-users in the same workflow as advanced users wastes both groups' time
