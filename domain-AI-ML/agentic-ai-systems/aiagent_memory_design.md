---
title: "AI Agent Memory Design"
category: AI-ML/agentic-ai-systems
description: "Design an agent's short- and long-term memory — what is stored, retrieved, summarized, and forgotten — and pre-empt its failure modes: staleness, pollution, unbounded growth, and cross-task leakage."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - QA-12
  - AG-32
difficulty: advanced
tags:
  - agent-memory
  - retrieval
  - summarization
  - forgetting
  - context-management
updated: "2026-06-25"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_project_continuity_memory_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_cost_token_budget_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md
---

# AI Agent Memory Design

**Objective:** Design what an agent remembers within a task and across tasks — the storage tiers, retrieval policy, summarization, and forgetting rules — and surface the failure modes memory introduces (stale facts, polluted stores, unbounded context growth, cross-task leakage), so memory improves reliability instead of silently degrading it.

**When to Use:**
- Designing an agent that must recall state within a long task or across tasks.
- An agent forgets mid-task, repeats work, acts on stale facts, or its context cost grows unbounded.
- You are deciding whether long-term/persistent memory is justified at all.

**When NOT to Use:**
- The task is stateless and each invocation is independent — memory adds cost and failure surface for no benefit; say so.
- You need a portable, repo-local **project continuity memory** system for humans, sessions, agents, tools, and devices — use `aiagent_project_continuity_memory_design.md`. This prompt designs an agent's memory tiers; project continuity memory needs typed project records, handoffs, decisions, failed attempts, status/supersession, and interop.
- You only need the overall control loop (use `aiagent_architecture_design.md`) or budget enforcement (use `aiagent_cost_token_budget_design.md`).

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Task shape** — single-turn, long-running, or recurring across sessions; how long state must persist.
- **What must be remembered** — facts, decisions, tool results, user preferences, prior outcomes — and for how long each stays valid.
- **Retrieval needs** — how the agent will look memory up (by recency, semantic similarity, key).
- **Continuity scope** — whether memory serves only the agent run, recurring agent tasks, or a project-shared memory layer that should route to `aiagent_project_continuity_memory_design.md`.
- **Multi-tenancy / isolation** — whether memory is per-user/per-session and must not cross boundaries.
- **Budget** — context window, token/cost ceiling, and latency tolerance for retrieval.

## Constraints

**Must:**
- Justify each memory tier (in-context, short-term scratch, long-term store) against a concrete need; default to the least memory the task requires.
- Specify the retrieval policy, the summarization/compaction trigger, and an explicit forgetting/expiry rule for every persistent item.
- Pair memory capability with its cost: tokens consumed, retrieval latency, and the risk if the memory is wrong.

**Must Not:**
- Add a persistent vector store or long-term memory without a task that needs cross-task recall.
- Let any store grow unbounded with no compaction or eviction policy.
- Allow memory to cross tenant/session boundaries unless explicitly required and isolated.
- Treat project memory as merely a bigger agent memory store; project continuity needs its own record taxonomy, status rules, and read/write protocol.

**Instructions:**

1. **Decide what truly must persist.** List candidate memories and, for each, the minimum lifetime it needs (this turn / this task / across sessions) and its validity window. Drop anything that does not need to survive the current step.

2. **Classify the memory scope.** If the memory exists mainly to help future humans or different agents resume a project, route or cross-link to `aiagent_project_continuity_memory_design.md`; do not bury project decisions, failed attempts, handoffs, or traps in an agent-only memory store.

3. **Choose storage tiers by need.** Map each surviving item to the lightest tier: in-context, short-term scratchpad, or durable long-term store. Justify any long-term store with a concrete cross-task recall need.

4. **Define the retrieval policy.** Specify how items are fetched (recency, semantic similarity, exact key), how many, and how relevance is bounded so retrieval does not flood context or surface stale/irrelevant entries.

5. **Specify summarization / compaction.** Define when and how the agent compresses history (token threshold, step count) and what is preserved vs. discarded. State how compaction avoids silently dropping load-bearing facts.

6. **Define forgetting and expiry.** Give every persistent item a TTL or eviction rule. Specify how stale facts are invalidated (e.g., a fact superseded by a newer tool result) so the agent does not act on outdated state.

7. **Enforce isolation and provenance.** Ensure per-user/session boundaries are not crossed, and tag stored items with source and timestamp so the agent can judge trust and recency.

8. **Trace the memory failure modes.** For staleness, pollution (bad data written), unbounded growth, and cross-task leakage, show what your design does to prevent or detect each. Cross-link `aiagent_failure_mode_analysis.md`.

9. **Account for cost.** Estimate per-task token cost of carrying/retrieving memory and retrieval latency; state how it stays within the budget under the worst case.

**Output Format:**

A markdown memory design:
- **Memory Scope Decision** — agent-run memory vs recurring agent memory vs project continuity memory; route if needed
- **Memory Inventory** — table: Item | Lifetime | Validity window | Tier | Why it persists
- **Storage Tiers** — in-context / short-term / long-term, each with rationale
- **Retrieval Policy** — method, top-k, relevance bounding
- **Summarization & Forgetting Rules** — compaction triggers + TTL/eviction per item
- **Isolation & Provenance** — boundaries + tagging
- **Failure-Mode Mitigations** — table: Failure | Prevention/Detection
- **Cost & Latency** — per-task memory cost estimate

## Verification

- [ ] The memory scope is classified; project continuity memory is routed/cross-linked rather than folded into agent-only memory.
- [ ] Every persistent item has a justified tier and an explicit expiry/eviction rule.
- [ ] No long-term store exists without a stated cross-task recall need.
- [ ] Retrieval is bounded (top-k / relevance) so it cannot flood context.
- [ ] Summarization preserves load-bearing facts and the rule is stated.
- [ ] Tenant/session isolation is specified where required.
- [ ] Each of the four memory failure modes has a prevention or detection mechanism.
- [ ] Memory token cost and retrieval latency are estimated against the budget.

## False-Positive Prevention

❌ **DON'T:**
- Add a vector database because "agents need memory," without a cross-task recall need that justifies it.
- Treat stored facts as permanently true — agents acting on stale memory fail silently.
- Let summarization drop facts without checking which were load-bearing for the task.
- Assume the store is small "for now" and skip an eviction policy.
- Put project-wide decisions, failed attempts, and handoffs into opaque agent memory when they should be human-readable project records.

✅ **DO:**
- Start stateless and add the lightest memory tier a concrete need demands.
- Tag every memory with source and timestamp and define how it goes stale.
- Bound retrieval (top-k, relevance) and compaction so context cost stays in budget.
- Enforce per-tenant isolation and verify it explicitly, since leakage here is a safety/privacy failure.
- Use project continuity memory when the durable state must outlive one agent/runtime and remain portable across tools.

## Example Output

```markdown
## Memory Design: Personal Travel-Planning Agent

### Memory Scope Decision
Agent memory, not project continuity memory. The durable data is per-user preference recall for future travel tasks, not a repo-local record of decisions/attempts/handoffs.

### Memory Inventory
| Item | Lifetime | Validity | Tier | Why |
|---|---|---|---|---|
| Current itinerary draft | This task | until task end | In-context | active working state |
| Tool results (flight quotes) | This task | 10 min (prices stale) | Short-term scratch | reused across steps |
| User home airport / seat pref | Across sessions | until user changes | Long-term store | recurring personalization |
| Raw search transcripts | This task | discard on summarize | none (compacted) | not load-bearing |

### Storage Tiers
- In-context: itinerary + last 3 observations.
- Short-term: scratchpad of quotes with timestamps.
- Long-term: per-user preference record (home airport, seat, loyalty IDs) — justified by recurring use.

### Retrieval Policy
Long-term: exact key by user_id (no semantic search needed). Short-term: most-recent quote per route.

### Summarization & Forgetting
Compact transcript at 12k tokens → keep decisions + chosen options, drop raw search text. Flight quotes expire after 10 min (re-fetch). Preferences persist until user edits.

### Isolation & Provenance
Long-term store partitioned by user_id; every item tagged {source, ts}. No cross-user retrieval path exists.

### Failure-Mode Mitigations
| Failure | Mitigation |
|---|---|
| Stale prices | 10-min TTL + re-fetch before booking step |
| Pollution | preferences write-validated; quotes never promoted to long-term |
| Unbounded growth | transcript compaction at 12k tokens |
| Cross-task leakage | user_id partition + tests |

### Cost & Latency
~2k tokens carried per step; key-lookup retrieval < 20ms. Within 8k/step budget.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** persist → scope → tier → retrieve → summarize → forget → isolate.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs recall benefit against cost, latency, and staleness risk.
- **CM-02 (Constraint Specification):** TTLs, budget, and isolation are governing constraints.
- **QA-12 (False Positives Identification):** separates needed persistence from memory-maximalism.
- **AG-32 (Agent Memory & State Management):** the storage/retrieval/forgetting design is the core deliverable.

**Related Prompts:**
- `aiagent_project_continuity_memory_design.md` — portable repo-local project memory across humans, sessions, agents, and tools.
- `aiagent_architecture_design.md` — names the state the loop depends on; this designs it.
- `aiagent_cost_token_budget_design.md` — bounds the token cost memory consumes.
- `aiagent_failure_mode_analysis.md` — stale/polluted/leaked memory are agent failure modes.
