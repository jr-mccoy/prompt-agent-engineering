---
title: "AI Multi-Agent Orchestration Decision"
category: AI-ML/agentic-ai-systems
description: "Decide whether a task warrants multiple agents and, if so, how to coordinate them — roles, boundaries, and communication — paying the coordination cost only when a single agent demonstrably can't do the job."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - AG-09
difficulty: advanced
tags:
  - multi-agent
  - orchestration
  - coordination-cost
  - role-boundaries
  - single-vs-multi
updated: "2026-05-29"
related_prompts:
  - domain-agentic-resources/commands/multi-agent/multiagent_scaling_vs_single_agent_diagnosis.md
  - domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
---

# AI Multi-Agent Orchestration Decision

**Objective:** Decide whether a task genuinely needs more than one agent and, if it does, specify the coordination design — roles, scope boundaries, communication, and shared state — while making the single-agent baseline the default and treating multi-agent coordination as a cost to be justified, not a feature to add. This prompt owns the *decision and the ML-engineering framing*; the detailed architectural templates live in `domain-agentic-resources/commands/multi-agent/` and are cross-linked, not duplicated.

**When to Use:**
- You are tempted to split a workflow into multiple agents and want to test whether that's warranted.
- A single agent is overloaded (too many tools, conflated responsibilities) and you suspect decomposition helps.
- You already have multiple agents and coordination is the source of cost, latency, or errors.

**When NOT to Use:**
- You have not yet exhausted a single-agent design (build it first with `aiagent_architecture_design.md`).
- You need the full planner/worker/judge templates — use the multi-agent command set directly (linked below) once this prompt says "split."

## Inputs / Context

Provide what you can; the analysis degrades gracefully if some are missing:
- **Task & sub-tasks** — the work, and whether it decomposes into separable pieces.
- **Single-agent attempt** — what a one-agent design looks like and where it strains (tool count, context size, conflicting objectives).
- **Parallelism opportunity** — sub-tasks that can run independently vs. strictly sequential.
- **Budgets** — cost/latency ceilings; coordination adds overhead to both.
- **Reliability needs** — where isolation/specialization would reduce error or blast radius.

## Constraints

**Must:**
- Default to a single agent; require a concrete, named reason a single agent fails before recommending a split.
- Quantify (or estimate with stated assumptions) the coordination cost a split adds: extra calls, tokens, latency, and new failure modes (handoff loss, deadlock, conflicting actions).
- For any recommended split, define each agent's role, scope boundary, communication contract, and how conflicts/failures are resolved.

**Must Not:**
- Recommend multi-agent because it is fashionable, "more scalable," or mirrors a human org chart, absent a single-agent failure.
- Leave inter-agent communication, shared state, or termination undefined.
- Ignore the new failure modes coordination introduces (one cross-link instead of re-deriving them).

**Instructions:**

1. **Establish the single-agent baseline.** Describe the best single-agent design and where it actually breaks: too many tools to select reliably, context overflow, conflicting objectives, or unsafe mixing of privileges. If it doesn't break, stop — recommend single.

2. **Identify the decomposition axis.** If splitting, name *why*: separable sub-tasks, independent privileges (least-privilege isolation), parallelizable work, or specialization that improves reliability. Map sub-tasks to candidate agents.

3. **Choose a coordination pattern.** Select among orchestrator/worker, planner/executor, pipeline, or peer collaboration — and cross-link the matching template in `domain-agentic-resources/commands/multi-agent/` rather than re-specifying it. Justify the pattern against the decomposition axis.

4. **Define roles and least-privilege boundaries.** Give each agent one responsibility and the minimum tools/scope it needs. Isolation should *reduce* blast radius, not just add boxes.

5. **Specify the communication contract.** Define what each agent passes (structured handoff, not free chat), what shared state exists, and how information loss across handoffs is prevented.

6. **Define termination, conflict, and failure handling.** Specify when the whole system stops, how conflicting agent outputs are reconciled (judge/voter/orchestrator decides), and what happens when one agent fails or loops — so a sub-agent failure doesn't strand the system.

7. **Tally the coordination cost.** Estimate added calls/tokens/latency and the new failure modes; compare against the single-agent baseline on capability, cost, latency, and safety. Recommend only if the split wins net.

8. **State the decision.** Single vs. multi, with the deciding reason, and (if multi) point to the specific command template to implement it.

**Output Format:**

A markdown decision doc:
- **Single-Agent Baseline & Where It Breaks** — explicit failure point or "doesn't break → single"
- **Decomposition Rationale** — the axis justifying a split (if any)
- **Recommended Pattern** — with cross-link to the multi-agent command template
- **Role & Boundary Map** — agent | responsibility | least-privilege scope
- **Communication & State Contract** — handoff format, shared state
- **Termination / Conflict / Failure Handling**
- **Coordination Cost vs. Baseline** — table: capability/cost/latency/safety
- **Decision** — single or multi + deciding reason

## Verification

- [ ] A single-agent baseline is described and its concrete break point named (or it's recommended).
- [ ] Any split has a named decomposition rationale, not "more scalable."
- [ ] Each agent has one responsibility and least-privilege scope.
- [ ] Communication is a structured contract, and termination/conflict/failure handling is defined.
- [ ] Coordination cost (calls/tokens/latency + new failure modes) is tallied vs. the baseline.
- [ ] The implementation template is cross-linked, not re-derived here.

## False-Positive Prevention

❌ **DON'T:**
- Split into agents because the workflow has multiple "steps" — steps are not agents; a single agent runs steps too.
- Mirror a human team structure (researcher/writer/editor) without showing a single agent fails.
- Claim multi-agent is "more reliable" while ignoring handoff loss, deadlock, and conflicting-action failures.
- Recommend a split and leave who-decides-on-conflict and when-does-it-stop unspecified.

✅ **DO:**
- Make the single agent prove insufficient (tool overload, context overflow, privilege conflict) before splitting.
- Use isolation to shrink blast radius and improve reliability, with the gain stated.
- Count the coordination tax in calls, tokens, latency, and new failure modes against the baseline.
- Define handoff contracts, conflict resolution, and global termination explicitly.

## Example Output

```markdown
## Orchestration Decision: Compliance-Document Processing

### Single-Agent Baseline & Where It Breaks
One agent with 14 tools (extract, classify, redact, validate, route). Breaks: tool-selection error rate climbs with 14 tools; redaction needs write-to-PII scope it shouldn't share with the public-summary step.

### Decomposition Rationale
Privilege isolation (redaction handles PII; summarizer must not) + reliability (smaller tool sets per agent).

### Recommended Pattern
Orchestrator + 3 workers (extract/classify, redact, summarize). See
`domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md` for the template.

### Role & Boundary Map
| Agent | Responsibility | Scope |
|---|---|---|
| Orchestrator | route + assemble result | no doc write |
| Redactor | remove PII | read+write PII (isolated creds) |
| Summarizer | public summary | read redacted-only (no PII access) |

### Communication & State Contract
Structured JSON handoffs; summarizer receives only the redacted artifact (enforces isolation). Shared state = doc id + status.

### Termination / Conflict / Failure Handling
Orchestrator stops when all workers report done or any worker errors twice. Redactor failure → halt (never summarize un-redacted). No peer conflict (pipeline).

### Coordination Cost vs. Baseline
| | Capability | Cost | Latency | Safety |
|---|---|---|---|---|
| Single agent | tool-select errors | $0.05 | 9s | PII scope mixed (worse) |
| Multi (chosen) | fewer errors | $0.08 | 13s | PII isolated (better) |

### Decision
Multi-agent — justified by PII privilege isolation, not by step count. Coordination tax accepted for the safety gain.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** baseline → rationale → pattern → boundaries → cost → decision.
- **RT-02 (Multi-Dimensional Analysis Framework):** single vs. multi scored on capability/cost/latency/safety.
- **DS-06 (Prioritization & Severity Guidance):** isolation prioritized by blast radius reduction.
- **CM-02 (Constraint Specification):** least-privilege boundaries and budgets constrain the design.
- **AG-09 (Multi-Agent Coordination):** roles, handoff contract, and conflict handling are the core deliverable.

**Related Prompts:**
- `domain-agentic-resources/commands/multi-agent/multiagent_scaling_vs_single_agent_diagnosis.md` — deeper single-vs-multi diagnosis.
- `domain-agentic-resources/commands/multi-agent/multiagent_two_tier_architecture_template.md` — planner/worker/judge implementation template.
- `aiagent_architecture_design.md` — build and exhaust the single-agent baseline first.
