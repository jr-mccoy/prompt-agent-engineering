---
title: "AI Multi-Agent Orchestration Topology Selection"
category: AI-ML/agentic-ai-systems
description: "Given that a task warrants more than one agent, select the coordination topology — manager-worker, pipeline, parallel fan-out/gather, debate/ensemble, blackboard, or market/bidding — using a scorecard on capability, cost, latency, reliability, and complexity instead of defaulting to a hierarchy."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - AG-09
  - QA-01
difficulty: advanced
tags:
  - multi-agent
  - topology
  - orchestration
  - coordination-pattern
  - fan-out
updated: "2026-06-18"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_multi_agent_orchestration.md
  - domain-AI-ML/agentic-ai-systems/aiagent_inter_agent_communication_protocol.md
  - domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md
---

# AI Multi-Agent Orchestration Topology Selection

**Objective:** Once a split into multiple agents is justified, choose the coordination topology that fits the decomposition — and only that topology — by scoring the candidates (manager-worker, sequential pipeline, parallel fan-out/gather, debate/ensemble, blackboard, market/bidding) on capability, cost, latency, reliability, and coordination complexity, rather than defaulting to a manager-worker hierarchy because it mirrors an org chart.

**When to Use:**
- `aiagent_multi_agent_orchestration.md` has already concluded the task needs multiple agents, and you must pick *how* they coordinate.
- An existing multi-agent system uses a topology that fights the work (e.g., a pipeline where steps actually need to negotiate, or a debate where a pipeline would do).
- You need to justify a topology choice to reviewers with explicit tradeoffs.

**When NOT to Use:**
- You have not yet established that a single agent fails — run `aiagent_multi_agent_orchestration.md` first.
- You need the concrete planner/worker/judge contract template — use `domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md`.
- You are designing the message protocol between agents — use `aiagent_inter_agent_communication_protocol.md`.

## Inputs / Context

Provide what you can; the analysis degrades gracefully if some are missing:
- **Decomposition** — the sub-tasks and how they relate (independent, sequential, mutually dependent, or competing).
- **Parallelism** — which sub-tasks can run concurrently vs. strictly ordered.
- **Quality model** — whether quality comes from a single best answer, from aggregating diverse answers, or from adversarial critique.
- **Budgets** — cost/latency ceilings; some topologies (debate, fan-out) multiply token cost.
- **Reliability needs** — tolerance for a single agent's failure stalling the whole system.

## Constraints

**Must:**
- Map the decomposition's structure to the topology — the topology must be implied by how sub-tasks relate, not by preference.
- Score every serious candidate on the same axes (capability, cost, latency, reliability, coordination complexity) and pick the one that wins net.
- For the chosen topology, name its dominant failure mode (e.g., manager bottleneck, pipeline stall, fan-out cost blow-up, debate non-convergence) and how the design contains it.

**Must Not:**
- Default to manager-worker because it resembles a human team.
- Choose debate/ensemble or fan-out without showing the quality or recall gain that justifies the multiplied cost.
- Leave the conflict-resolution authority (who decides when agents disagree) and global termination unspecified.
- Invent cost/latency multipliers; estimate from the user's call counts and mark assumptions.

**Instructions:**

1. **Restate the decomposition and relation type.** Classify how the sub-tasks relate: independent, sequential, interdependent (need shared state), or competing (need a winner). This relation is the primary topology signal.

2. **Enumerate candidate topologies.** From the relation type, list the plausible topologies and immediately exclude obviously unfit ones with a one-line reason.

3. **Score candidates on the common axes.** Build a scorecard: capability fit, cost, latency, reliability, coordination complexity. Use the user's parallelism and quality model to fill it; mark estimates as estimates.

4. **Identify the dominant failure mode per finalist.** Manager-worker → manager bottleneck/single point of failure; pipeline → stall propagation; fan-out/gather → cost multiplication + straggler latency; debate/ensemble → non-convergence + cost; blackboard → race conditions on shared state; market/bidding → starvation/gaming.

5. **Select and justify.** Choose the net winner; state why each rejected topology lost on the scorecard.

6. **Specify conflict resolution and termination.** Name who arbitrates disagreement (orchestrator, judge, vote) and the global stop condition; ensure one agent's failure can't strand the system.

7. **Cross-link the implementation template.** Point to the matching template in `domain-agentic-resources/commands/multi-agent/` and the protocol prompt rather than re-specifying contracts here.

**Output Format:**

A markdown decision doc:
- **Decomposition & Relation Type**
- **Candidate Topologies** — with quick exclusions
- **Scorecard** — table: Topology | Capability | Cost | Latency | Reliability | Complexity
- **Dominant Failure Mode (finalists)** — and containment
- **Decision** — chosen topology + why others lost
- **Conflict Resolution & Termination**
- **Implementation Cross-Links**

## Verification

- [ ] The relation type between sub-tasks is stated and drives the topology choice.
- [ ] Every serious candidate is scored on the same axes; the winner wins net, not by default.
- [ ] Cost-multiplying topologies (fan-out, debate) are justified by a stated quality/recall gain.
- [ ] The chosen topology's dominant failure mode is named and contained.
- [ ] Conflict-resolution authority and global termination are specified.
- [ ] The implementation template and protocol prompt are cross-linked, not re-derived.

## False-Positive Prevention

❌ **DON'T:**
- Pick manager-worker because it mirrors how a human team would split the work.
- Use debate or fan-out for the perceived "thoroughness" without quantifying the gain over a single strong agent.
- Score only the favored topology and skip the alternatives.
- Recommend a topology while leaving who-decides-on-conflict and when-does-it-stop open.

✅ **DO:**
- Derive the topology from how the sub-tasks actually relate.
- Justify any cost-multiplying topology with a concrete quality or recall improvement.
- Score all serious candidates on identical axes and show the loser's deficit.
- Pin down conflict arbitration and a global stop condition for the chosen topology.

## Example Output

```markdown
## Topology Selection: Research-Brief Generation from 30 Sources

### Decomposition & Relation Type
Sub-tasks: read/extract per source (independent), synthesize (depends on all extracts), fact-check synthesis (adversarial). Mixed: independent fan-out → dependent join → competing check.

### Candidate Topologies
- Pipeline — excluded as sole pattern: extraction is embarrassingly parallel, a pipeline serializes it.
- Manager-worker fan-out/gather — fits the extraction phase.
- Debate — candidate for the fact-check phase only.
- Blackboard — overkill: extracts don't need shared mutable state.

### Scorecard
| Topology | Capability | Cost | Latency | Reliability | Complexity |
|---|---|---|---|---|---|
| Pipeline (only) | low (serial) | low | high | med | low |
| Fan-out/gather + judge | high | med (30×) | low | high | med |
| Full debate | high | high (N× rounds) | high | med | high |

### Dominant Failure Mode (finalists)
Fan-out/gather → straggler latency + cost multiplication (30 parallel reads). Containment: per-worker token cap + timeout; drop/retry stragglers.

### Decision
**Fan-out/gather (extraction) → single synthesizer → judge fact-check.** Full debate rejected: non-convergence risk and round-multiplied cost without a shown accuracy gain over one judge pass.

### Conflict Resolution & Termination
Judge arbitrates synthesis vs. source conflicts. Stop when judge passes or after 2 synthesis revisions → escalate to human.

### Implementation Cross-Links
See `commands/multi-agent/multiagent_two_tier_architecture_template.md` and `aiagent_inter_agent_communication_protocol.md`.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** decomposition → candidates → scorecard → decision → termination.
- **RT-02 (Multi-Dimensional Analysis Framework):** topologies scored on five axes simultaneously.
- **DS-06 (Prioritization & Severity Guidance):** the dominant failure mode per finalist ranks containment effort.
- **AG-09 (Multi-Agent Coordination):** topology, conflict authority, and termination are the core deliverable.
- **QA-01 (Self-Verification):** the checklist enforces same-axes scoring and a non-default choice.

**Related Prompts:**
- `aiagent_multi_agent_orchestration.md` — the prior whether-to-split decision.
- `aiagent_inter_agent_communication_protocol.md` — design the messages once the topology is chosen.
- `domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md` — concrete planner/worker/judge contract template.
