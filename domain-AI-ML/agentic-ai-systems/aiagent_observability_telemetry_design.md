---
title: "AI Agent Observability & Telemetry Design"
category: AI-ML/agentic-ai-systems
description: "Design the telemetry architecture for an agent system — which events and spans to emit, how to structure trajectory traces, cardinality/sampling/retention, and the dashboards and alerts that turn raw signals into health monitoring and incident diagnosis."
techniques:
  - ST-02
  - DS-02
  - QA-17
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - observability
  - telemetry
  - tracing
  - trajectory
  - alerting
updated: "2026-06-18"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_evaluation_design.md
  - domain-prompt-engineering/agent-workflows/agent_observability_prompt_for_traces.md
  - domain-software-engineering/devops/devops_opentelemetry_instrumentation.md
---

# AI Agent Observability & Telemetry Design

**Objective:** Design what an agent system emits and how it is structured — the event/span schema, the trajectory trace model, cardinality/sampling/retention policy, and the dashboards and alerts — so that operators can see agent health, diagnose a failure from its trace, and attribute cost, rather than discovering problems only when users complain.

**When to Use:**
- An agent is going to production (or already is) and you need to see what it's doing without re-running it.
- Failures are diagnosed by guesswork because traces are missing, unstructured, or too noisy to read.
- You need to alert on agent-specific anomalies (loops, runaway cost, success-rate drops) not just CPU/memory.

**When NOT to Use:**
- You're designing the *offline* evaluation harness that scores quality — use `aiagent_evaluation_design.md` (this prompt is about production telemetry, not graded eval).
- You only need the in-agent prompt that emits structured events — use `domain-prompt-engineering/agent-workflows/agent_observability_prompt_for_traces.md`.
- You need generic OpenTelemetry/service instrumentation — use `domain-software-engineering/devops/devops_opentelemetry_instrumentation.md` and cross-link.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Agent shape** — single vs. multi-agent, loop structure, tools called.
- **What you need to answer from telemetry** — the questions operators will ask (why did this task fail? where did cost go? is it looping?).
- **Volume** — tasks/day and steps/task (drives cardinality, sampling, and cost of telemetry itself).
- **Retention & compliance needs** — how long traces must be kept; whether payloads contain sensitive data.
- **Existing stack** — tracing/metrics backend already in use, if any.

## Constraints

**Must:**
- Define a trace model that reconstructs a full task trajectory: a task-level trace with step/tool spans, decision points, inputs/outputs (or references), and outcome.
- Specify the metric set with explicit dimensions: at minimum success rate, step count, latency, token/cost, tool-error rate, loop/retry rate — each sliceable by task type.
- Set cardinality, sampling, and retention policy so telemetry is affordable and PII-safe (reference, redact, or sample high-volume payloads).
- Define alerts tied to agent-specific failure signals with thresholds and an owner, not just infra metrics.

**Must Not:**
- Log free-form prose with no schema, making traces ungreppable and unaggregatable.
- Emit unbounded-cardinality labels (raw user input, full prompts as metric tags).
- Store raw sensitive payloads in traces without redaction or a retention limit.
- Claim "observable" when there's no way to reconstruct why a specific task failed.

**Instructions:**

1. **List the operator questions.** Write the concrete questions telemetry must answer (failure cause, cost attribution, loop detection, quality drift). Every signal you design must serve one.

2. **Define the trace/span model.** Specify the task-level trace and the spans within it (per step, per tool call, per LLM call), the parent/child structure, and the fields on each span (timestamps, inputs/outputs or references, decision/rationale tag, outcome, token/cost).

3. **Define the metric set and dimensions.** Specify success rate, step count, latency (p50/p95), tokens/cost, tool-error rate, retry/loop rate — each with the slice dimensions (task type, agent role, tool, model). Keep dimension cardinality bounded.

4. **Set sampling and cardinality controls.** Decide which traces are kept in full (errors, slow, expensive → always; happy-path → sampled) and which labels are bounded. Note the telemetry's own cost.

5. **Set retention and sensitivity policy.** Define retention per data class and how sensitive payloads are handled (reference IDs, redaction) — cross-link `aiagent_privacy_data_governance.md`.

6. **Design dashboards.** Specify the health view (rates, latency, cost over time) and the single-trajectory view (drill into one task's full trace) operators use during an incident.

7. **Define alerts.** For each agent-specific failure signal (success-rate drop, cost spike, loop-rate rise, tool-error surge), set a threshold, a window, and an owner/runbook pointer.

8. **State the incident workflow.** Describe how an operator goes from an alert to a root cause using the trace model — proving the telemetry is sufficient.

**Output Format:**

A markdown design doc:
- **Operator Questions** — what telemetry must answer
- **Trace/Span Model** — trace → spans → fields
- **Metric Set** — metric | dimensions | purpose
- **Sampling & Cardinality** — kept-in-full rules + bounded labels
- **Retention & Sensitivity** — per data class + cross-link
- **Dashboards** — health view + trajectory view
- **Alerts** — signal | threshold | window | owner
- **Incident Workflow** — alert → trace → root cause

## Verification

- [ ] The trace model can reconstruct any single task's full trajectory and outcome.
- [ ] Metrics carry bounded-cardinality dimensions and are sliceable by task type.
- [ ] Errors/slow/expensive traces are always retained; high-volume payloads are sampled or referenced.
- [ ] Sensitive payloads are redacted/referenced with a retention limit.
- [ ] Each alert ties to an agent-specific signal with a threshold and an owner.
- [ ] An incident walkthrough shows alert → trace → root cause works end to end.

## False-Positive Prevention

❌ **DON'T:**
- Call the system "observable" because it writes logs, when those logs can't reconstruct a failed trajectory.
- Use raw user input or full prompts as metric labels (cardinality explosion + PII leak).
- Alert only on CPU/memory/latency and miss agent failures like looping or success-rate collapse.
- Keep full raw payloads forever with no redaction or retention policy.

✅ **DO:**
- Design a structured trace that links steps, tool calls, decisions, and outcome for every task.
- Bound label cardinality and reference/redact heavy or sensitive payloads.
- Alert on agent-specific signals (loop rate, cost spike, success drop) with owners and runbooks.
- Validate the design by walking one incident from alert to root cause.

## Example Output

```markdown
## Telemetry Design: Document-Processing Agent (5k tasks/day, ~8 steps each)

### Operator Questions
Why did task X fail? Where did today's cost spike come from? Is any task class looping?

### Trace/Span Model
Trace = task (id, type, outcome). Spans: per step {action, decision_tag, outcome}, per tool call {tool, args_ref, status, latency, cost}, per LLM call {model, tokens_in/out, cost}. Payloads stored by reference (blob id), not inline.

### Metric Set
| Metric | Dimensions | Purpose |
|---|---|---|
| success_rate | task_type | health |
| step_count p95 | task_type | loop detection |
| cost_per_task | task_type, model | cost attribution |
| tool_error_rate | tool | flaky-tool detection |
| retry_rate | task_type | instability |

### Sampling & Cardinality
Keep full traces for: errors, p95+ latency, cost > 2× median. Sample happy-path at 5%. Labels bounded to enums; no raw input as a label.

### Retention & Sensitivity
Traces 30d; payload blobs 7d, PII-redacted at write. See `aiagent_privacy_data_governance.md`.

### Dashboards
Health: success/latency/cost time series by task_type. Trajectory: single-task drill-down (step→tool→LLM spans).

### Alerts
| Signal | Threshold | Window | Owner |
|---|---|---|---|
| success_rate drop | <90% | 15m | on-call |
| cost spike | >2× 7d baseline | 1h | on-call |
| step_count p95 | >2× baseline | 30m | on-call |

### Incident Workflow
Cost-spike alert → filter traces by cost desc → one task_type looping on a flaky tool → tool_error_rate confirms → fix/route around tool.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** questions → trace model → metrics → sampling → alerts → incident flow.
- **DS-02 (Metric Specification):** the metric set and its dimensions are specified, not assumed.
- **QA-17 (Named Scores for Multi-Dimensional Metrics):** health is tracked across success, cost, latency, and stability simultaneously.
- **CM-02 (Constraint Specification):** cardinality, sampling, and retention bound the telemetry's own cost and risk.
- **QA-01 (Self-Verification):** the incident walkthrough proves the telemetry is sufficient.

**Related Prompts:**
- `aiagent_evaluation_design.md` — offline quality scoring (vs. this prompt's production telemetry).
- `domain-prompt-engineering/agent-workflows/agent_observability_prompt_for_traces.md` — the in-agent event-emission prompt.
- `domain-software-engineering/devops/devops_opentelemetry_instrumentation.md` — generic OTel instrumentation to build on.
