---
title: "AI Agent Cost & Token Budget Design"
category: AI-ML/agentic-ai-systems
description: "Set and enforce token, cost, and latency budgets for an agent with circuit breakers, so a single task or a runaway loop cannot quietly burn money or time."
techniques:
  - ST-02
  - DS-02
  - CM-02
  - DS-06
  - AG-29
difficulty: advanced
tags:
  - cost-budget
  - token-budget
  - latency
  - circuit-breaker
  - runaway-cost
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_evaluation_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md
---

# AI Agent Cost & Token Budget Design

**Objective:** Define an agent's token, dollar, and latency budgets at the right granularities (per-step, per-task, per-session, per-day) and the circuit breakers that enforce them, so that no single loop, retry storm, or traffic spike can run away with cost or time — and so cost is a first-class, monitored property of the agent, not a surprise on the invoice.

**When to Use:**
- Before deploying an agent with an open-ended loop or tool retries that could spiral.
- Costs or latency are unpredictable, spiking, or already over budget.
- You need enforceable ceilings (breakers), not just dashboards, plus alerting thresholds.

**When NOT to Use:**
- A single fixed-cost LLM call with no loop — a simple per-call limit suffices; this is overkill.
- You need the overall loop/stopping design (use `aiagent_architecture_design.md`), of which budget is one input.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Per-call cost model** — model/version pricing (input/output tokens), tool-call costs, and the framework (ask; don't assume).
- **Task profile** — typical and worst-case steps per task, tokens per step, tool calls per task.
- **Volume** — tasks/sessions per day and peak concurrency.
- **Constraints** — acceptable cost per task, monthly spend cap, latency SLA (P50/P95).
- **Current behavior** — observed cost/latency distribution and any runaway incidents.

## Constraints

**Must:**
- Set budgets at multiple granularities (per-step, per-task, per-session, and a global per-day/per-tenant cap) and define the enforcement (breaker) for each.
- Specify breaker behavior on breach: degrade (cheaper model/fewer steps), abort with partial result, or escalate — never silently continue.
- Tie cost/latency to the agent's value: state the per-task cost the outcome justifies, not just a technical ceiling.

**Must Not:**
- Fabricate pricing or token counts — reason from the user's model/version and task profile; mark unknowns as assumptions to measure.
- Rely on monitoring/alerts alone as "enforcement" — alerts notify, breakers stop.
- Leave retries, tool loops, or context growth uncapped (the common runaway sources).

**Instructions:**

1. **Build the per-task cost model.** From per-call pricing × typical/worst-case steps and tokens, estimate per-task token and dollar cost and latency. State assumptions where pricing or step counts are unknown.

2. **Set budgets at each granularity.** Define per-step, per-task, per-session, and global per-day/per-tenant ceilings. Derive them from the task's value and the volume, not from round numbers alone.

3. **Locate the runaway sources.** Identify where cost spirals: unbounded loops, retry storms on tool errors, context-window growth, and recursive sub-agent calls. Each needs a specific cap.

4. **Specify circuit breakers.** For each ceiling, define the breaker: the metric, the threshold, and the action (degrade / abort-with-partial / escalate). Make at least the per-task and global caps hard stops independent of the model's judgment.

5. **Define graceful degradation.** Specify the cheaper fallback path when approaching budget: smaller model, fewer retries, reduced retrieval, or returning best-so-far — so the agent degrades usefully instead of failing hard.

6. **Add monitoring and alert thresholds.** Define what is logged per task (tokens, cost, steps, latency) and alert thresholds *below* the hard breakers (early warning), plus anomaly detection for cost spikes.

7. **Reconcile cost with latency and quality.** Show the tradeoff: a cheaper model or fewer steps cuts cost but may cut success or raise latency variance. State the chosen balance against the agent's value.

8. **Plan for scale.** Apply per-tenant and global daily caps so one user or one bad deploy cannot exhaust the whole budget; define what happens when the global cap is hit.

**Output Format:**

A markdown budget design:
- **Per-Task Cost Model** — assumptions + estimated tokens/$/latency (typical & worst case)
- **Budget Table** — Granularity | Ceiling | Metric | Breaker action
- **Runaway Sources & Caps** — table: source | cap
- **Degradation Path** — fallback steps as budget nears limit
- **Monitoring & Alerts** — logged signals + warning thresholds (below breakers)
- **Cost vs. Latency/Quality Tradeoff** — the chosen balance
- **Scale Caps** — per-tenant + global

## Verification

- [ ] Budgets exist at per-step, per-task, per-session, and global granularities.
- [ ] Every ceiling has an enforced breaker action (degrade/abort/escalate), not just an alert.
- [ ] Per-task and global caps are hard stops independent of the model's judgment.
- [ ] All runaway sources (loops, retries, context growth, recursion) have specific caps.
- [ ] Pricing/token figures are reasoned from the user's model or marked as assumptions.
- [ ] Per-task cost is justified against the outcome's value, and the cost/quality/latency tradeoff is stated.

## False-Positive Prevention

❌ **DON'T:**
- Treat a monitoring dashboard or alert as a budget control — alerts notify after the spend, breakers prevent it.
- Set only a per-call token limit and leave the loop's total step count and retries uncapped.
- Make up model pricing or "tokens per task" from memory — that produces a fictional budget.
- Cap cost by silently truncating output and call it "within budget" when the task actually failed.

✅ **DO:**
- Enforce hard per-task and global breakers that stop the agent regardless of what it "wants" to do next.
- Cap every runaway source: loop steps, retries, context growth, and recursive sub-agent calls.
- Derive budgets from the user's actual model/version pricing and task profile, flagging assumptions.
- Make degradation explicit and useful (best-so-far + flag), so a budget breach is a graceful stop, not a silent bad result.

## Example Output

```markdown
## Budget Design: Data-Enrichment Agent

### Per-Task Cost Model (assumptions stated)
Model X-1.2 @ $3/$15 per M tokens (in/out). Typical: 5 steps, ~4k in + 1k out/step → ~$0.13/task. Worst case (loop near cap): 15 steps → ~$0.39. Assumption: enrichment tool calls are free (internal) — confirm.

### Budget Table
| Granularity | Ceiling | Metric | Breaker action |
|---|---|---|---|
| Per-step | 8k tokens | tokens/step | truncate context, continue |
| Per-task | $0.40 / 15 steps | $ or steps | abort, return partial + flag |
| Per-session | $5 | cumulative $ | escalate to human |
| Global/day | $2,000 | daily $ | queue/throttle new tasks |

### Runaway Sources & Caps
| Source | Cap |
|---|---|
| Reasoning loop | 15 steps + repeated-state detector |
| Tool retries | max 3, exp backoff |
| Context growth | compact at 12k tokens |
| Sub-agent calls | none (single agent) |

### Degradation Path
At 80% per-task budget: stop new tool calls, synthesize from data so far, return best-so-far + "budget-limited" flag.

### Monitoring & Alerts
Log {tokens, $, steps, latency} per task. Alert at $0.30/task (75% of breaker) and at daily $1,500. Anomaly alert on 3σ cost spike.

### Cost vs. Latency/Quality Tradeoff
Could use a cheaper model for classification sub-step (−40% cost, −3% success) — adopted for that step only.

### Scale Caps
Per-tenant $50/day; global $2,000/day hard cap → throttle, not fail open.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** cost model → budgets → runaway caps → breakers → monitoring.
- **DS-02 (Metric Specification):** defines the cost/latency metrics and thresholds precisely.
- **CM-02 (Constraint Specification):** budgets and hard caps are the governing constraints.
- **DS-06 (Prioritization & Severity Guidance):** prioritizes the highest-runaway sources for hard caps.
- **AG-29 (Agent Loop Architecture):** breakers and step caps integrate into the control loop.

**Related Prompts:**
- `aiagent_architecture_design.md` — the loop these budgets are enforced within.
- `aiagent_evaluation_design.md` — uses these budgets as evaluation gates.
- `aiagent_failure_mode_analysis.md` — runaway cost is a primary failure mode these breakers bound.
