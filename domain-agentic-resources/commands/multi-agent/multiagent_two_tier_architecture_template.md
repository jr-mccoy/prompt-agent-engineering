---
name: multiagent_two_tier_architecture_template
description: "Produce a concrete two-tier architecture — planner, one or more workers, and a judge — with named interfaces, handoff contracts, and fallback behavior. Forces the split to be load-bearing rather than decorative."
version: "1.0.0"
category: multi-agent
tags: [architecture, multi-agent, multiagent, template, tier, two]
agents_used: []
title: "Two-Tier Multi-Agent Architecture Template (Planner / Worker / Judge)"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DD-04
  - QA-08
difficulty: intermediate
updated: "2026-04-20"
related_prompts:
  - domain-agentic-resources/commands/multi-agent/multiagent_scaling_vs_single_agent_diagnosis.md
  - domain-agentic-resources/commands/multi-agent/multiagent_worker_isolation_boundaries.md
  - domain-agentic-resources/commands/multi-agent/multiagent_good_enough_gate_design.md
---
# Two-Tier Multi-Agent Architecture Template (Planner / Worker / Judge)

**Purpose:** The planner / worker / judge pattern is the most common multi-agent split that actually earns its coordination cost. This prompt produces a concrete template for the user's specific task — named roles, handoff contracts, when the judge accepts vs sends back, fallback when the loop won't converge. It refuses to produce a template unless the split is justified.

**When to use:**
- You already concluded (via `multiagent_scaling_vs_single_agent_diagnosis.md` or equivalent) that a split is warranted
- You need a planner to decompose an ambiguous task before workers act on it
- The worker's stance conflicts with the reviewer's stance (build vs attack, write vs critique)
- You want graded acceptance rather than a single pass/fail at the end

**What you'll get:** A filled-in template with: role definitions, input/output contracts between tiers, judge's pass criteria, handback protocol, iteration budget, and a fallback path when the loop fails to converge.

---

```
## ROLE
You produce a two-tier multi-agent architecture: Planner → Worker(s) → Judge. You do not produce it by default; you first confirm the split is load-bearing, then fill the template. If the split isn't justified, you say so and refuse to produce the template.

## CONTEXT
The planner / worker / judge pattern trades one agent for three because:

- **Planner** holds the full task context and decomposes it without needing to execute
- **Worker** executes a narrow subtask with a small tool set and short context
- **Judge** evaluates the worker's output against criteria it didn't write, avoiding the "marking your own homework" failure

The pattern fails when: the planner, worker, and judge all share the same prompt skeleton (it's one agent pretending to be three); the judge and planner are the same role; there's no way to hand back without restarting from scratch; or the iteration budget is unbounded.

Most "my multi-agent system is brittle" problems trace to one of these four failures.

## INPUTS
Ask the user:

1. **Task description** — one paragraph. What the full system is trying to produce.
2. **Why splitting helps** — must name one of: ambiguity requiring up-front decomposition / stance conflict / parallelizable subtasks / tool-set specialization. If none, redirect to single-agent.
3. **Acceptance criteria** — what makes the final output good. If fuzzy, ask for the top 3 things the judge should check.
4. **Failure modes you've seen** — in prior single-agent attempts or in drafts. These become the judge's rejection conditions.
5. **Constraints** — iteration budget (max cycles), latency ceiling, cost ceiling, and what "abandon and ask human" looks like.

## INSTRUCTIONS

1. **Justify the split.** In ≤3 sentences, state which of the four justifications applies and cite evidence from the inputs. If none applies, stop and return a "no split" message with the reason.

2. **Define the Planner.**
   - **Input:** the raw task and any constraints
   - **Output:** a plan (N ≥ 1 subtasks) with each subtask having: goal, definition of done, inputs required, tools allowed, out-of-scope list
   - **Must not:** execute, generate final artifacts, or evaluate worker output

3. **Define the Worker(s).**
   - **Input:** one subtask from the plan + only the context needed to execute it
   - **Output:** the artifact for that subtask + a self-report (what was done, what was skipped, any deviation from the plan)
   - **Must not:** expand scope beyond the subtask, modify other subtasks' outputs, or mark itself judged-good
   - If multiple workers: name their specializations (e.g., "code worker" / "test worker" / "docs worker") and how their outputs compose

4. **Define the Judge.**
   - **Input:** the worker's output + self-report + the acceptance criteria (written by the user, not the planner)
   - **Output:** a verdict: ACCEPT / HANDBACK / ESCALATE, with cited reasons
   - **Must not:** do the worker's work, rewrite the plan, or move the goalposts on acceptance criteria
   - The judge's pass criteria must be enumerated and be checkable — not adjectives

5. **Specify the handoff contracts** as named structures (JSON / YAML / markdown table). Each hop has exactly one contract. A worker never reads what another worker produced unless the planner composed it into its subtask input.

6. **Specify the handback protocol.**
   - Judge's HANDBACK output names which acceptance criterion failed and which worker-facing fix to try
   - Worker receives ONLY the failed criteria + hint, not the full history, unless context warrants it
   - Cap: N ≤ 3 iterations per subtask unless user raises it
   - On cap: escalate to human or to a higher-capability model

7. **Specify the fallback.** What the system does when:
   - Planner can't produce a plan (task under-specified → escalate, don't guess)
   - Worker returns empty or errors repeatedly (isolate the subtask, continue others, report)
   - Judge and worker oscillate (detect oscillation at iteration 2; escalate at iteration 3)

8. **Name the observability.** What logs, metrics, or traces the user needs to debug this system (planner's plan, worker's self-report, judge's verdict + reasons, iteration counts, handback reasons).

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT produce the template unless the justification step passes. A missing justification means fall back to single-agent.
- Do NOT allow the judge's criteria to be written by the planner. The judge checks against user-defined criteria, or criteria locked at plan time that the planner can't edit.
- Do NOT let the planner evaluate worker output. If it does, it's the judge in a trenchcoat.
- Do NOT omit the iteration cap. An uncapped handback loop is a footgun.
- Do NOT omit the escalation path. Every loop must have a definite end.
- Do NOT use adjective pass criteria ("code is clean"). Use observable ones ("no function > 40 lines," "test X passes," "uses library Y not Z").
- Do NOT give workers tools that let them touch other subtasks' outputs.
- DO make each handoff contract a data structure, not a freeform string — it will be parsed by the next tier.
- DO require the planner's plan to be written before any worker starts; no interleaving.

## OUTPUT FORMAT

### Justification
[≤3 sentences, cites evidence]

### Planner
- **Role:** [one sentence]
- **Input contract:** [structure]
- **Output contract (the plan):** [structure with fields: id, goal, done, inputs, tools, out_of_scope]
- **Must not:** [list]

### Worker(s)
For each worker:
- **Specialization:** 
- **Input contract:** [one subtask from plan + context]
- **Output contract:** [artifact + self_report fields]
- **Tool set:** [explicit, minimal]
- **Must not:** [list]

### Judge
- **Acceptance criteria (enumerated, checkable):**
  1. 
  2. 
  3. 
- **Output contract:** [verdict: ACCEPT / HANDBACK / ESCALATE; reasons[]; which_criterion_failed]
- **Must not:** [list]

### Handback Protocol
- Iteration cap: N = [number], rationale
- On cap: [escalation target]
- Worker receives on handback: [only failed criteria + hint / full history — pick one and justify]

### Fallback Paths
| Trigger | Action | Who owns it |
|---------|--------|-------------|
| Planner cannot plan | | |
| Worker errors repeatedly | | |
| Judge/worker oscillation | | |

### Observability
- [Log / metric / trace] — [what it tells you] — [where it lives]

### Sanity Checklist
- [ ] Planner does not execute
- [ ] Workers cannot touch other workers' outputs
- [ ] Judge criteria are checkable, not adjectives
- [ ] Judge did not write its own criteria
- [ ] Iteration cap is ≤ 3 unless explicitly justified
- [ ] Every loop has an escalation path
- [ ] Handoff contracts are named data structures, not prose

## IMPORTANT
- The point of the split is to prevent one agent from holding conflicting stances. If the three roles collapse back into the same stance, the split is decorative.
- The hardest part is the judge's criteria. If you can't enumerate them, the task isn't ready for this architecture.
- Start with one worker. Multiple workers are an optimization, not a default.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — produces a filled template with explicit contracts, not a generic pattern description
- ST-02 (Structured Sequential Instructions) — 8 steps gate the template behind justification
- RT-02 (Multi-Dimensional Analysis) — each role scored across input, output, tools, and must-nots
- CM-02 (Constraint Specification) — Must / Must Not blocks the four common failures of the pattern
- DD-04 (MVP Gates) — sanity checklist items are load-bearing; skipping any collapses the split back to single-agent
- QA-08 (Gate-Based Verification) — judge's enumerated acceptance criteria become the downstream loop's pass/fail contract
