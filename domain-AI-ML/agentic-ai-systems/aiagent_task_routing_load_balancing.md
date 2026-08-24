---
title: "AI Agent Task Routing & Load Balancing Design"
category: AI-ML/agentic-ai-systems
description: "Design how work is allocated across a pool of agents — routing by skill/cost/latency, pool sizing and spawn/deprovision rules, queue backpressure, and the retry-vs-escalate decision — so a fleet stays responsive under load instead of melting down or starving."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - task-routing
  - load-balancing
  - agent-pool
  - backpressure
  - retry-escalate
updated: "2026-06-18"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_orchestration_topology_selection.md
  - domain-AI-ML/agentic-ai-systems/aiagent_deployment_serving_architecture.md
  - domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md
---

# AI Agent Task Routing & Load Balancing Design

**Objective:** Design the work-allocation layer for a fleet of agents — how an incoming task is routed to the right agent, how the pool is sized and scaled, how the queue applies backpressure when overloaded, and when a stuck task is retried vs. escalated — so the system degrades predictably under load rather than stalling, starving, or blowing its budget.

**When to Use:**
- You have multiple agents (or many instances of one agent) and tasks arrive faster than any single worker can serve.
- Tasks differ in skill, cost, or urgency and need to reach the right worker.
- The system stalls under bursts, or one slow task blocks everything behind it.

**When NOT to Use:**
- A single agent handles one task at a time with no queue — routing is unnecessary.
- You are deciding the coordination *shape* of a fixed set of agents — use `aiagent_orchestration_topology_selection.md`.
- You are designing the serving/runtime substrate itself — use `aiagent_deployment_serving_architecture.md` (this prompt assumes that substrate exists and designs allocation policy on top).

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Task taxonomy** — the classes of tasks, their differing skill needs, cost, and urgency.
- **Agent pool** — what worker types exist and what each is good/cheap/fast at.
- **Load profile** — arrival rate, burstiness, and acceptable end-to-end latency / SLA.
- **Budgets** — cost ceiling for the fleet; cost of spinning up vs. keeping workers warm.
- **Failure tolerance** — how long a task may retry before a human or fallback must take it.

## Constraints

**Must:**
- Define a routing rule that maps task class → eligible worker(s) using a stated objective (skill match, lowest cost, lowest latency, or a weighted blend).
- Specify pool-sizing and scaling rules: minimum/maximum workers, spawn trigger, idle-deprovision rule.
- Define queue backpressure: what happens when the queue exceeds a threshold (shed, throttle, reject-with-retry-after) — never an unbounded queue.
- Define the retry-vs-escalate boundary: max attempts, backoff, and the escalation target when retries are exhausted.

**Must Not:**
- Route purely round-robin when tasks have materially different skill or cost profiles.
- Allow an unbounded queue or unbounded worker spawn (cost/latency blow-up).
- Retry a deterministically-failing task indefinitely instead of escalating.
- Fabricate throughput, latency, or cost numbers; reason from the user's load profile and mark assumptions.

**Instructions:**

1. **Classify the tasks and the pool.** State the task classes and the worker types, with each worker's relative skill, cost, and latency. Routing needs this map.

2. **Choose the routing objective.** Decide what routing optimizes — best-fit skill, cheapest capable worker, lowest latency, or a weighted blend — and state the rule (and tie-breakers).

3. **Size and scale the pool.** Set min/max workers, the spawn trigger (queue depth or latency SLA breach), and the idle-deprovision rule. Note warm-vs-cold-start cost tradeoff.

4. **Design backpressure.** Define the queue bound and the overflow policy (shed lowest-priority, throttle intake, reject with retry-after). Ensure overload degrades gracefully, not catastrophically.

5. **Handle stragglers and stuck tasks.** Set per-task timeouts, the retry policy (attempts + backoff), and the boundary at which a task escalates to a fallback worker or a human (cross-link `aiagent_human_in_the_loop_design.md`).

6. **Prevent starvation.** Ensure low-priority or expensive task classes still make progress (aging, reserved capacity) so routing doesn't permanently starve them.

7. **Define fleet-level observability hooks.** Name the signals to watch (queue depth, per-class latency, worker utilization, retry rate) so the policy can be tuned — cross-link `aiagent_observability_telemetry_design.md`.

8. **State the cost envelope.** Tie pool size and retry policy back to the fleet cost ceiling; cross-link `aiagent_fleet_cost_attribution_optimization.md`.

**Output Format:**

A markdown design doc:
- **Task Classes & Worker Pool** — capability/cost/latency map
- **Routing Rule** — objective + mapping + tie-breakers
- **Pool Sizing & Scaling** — min/max, spawn trigger, deprovision
- **Backpressure** — queue bound + overflow policy
- **Stragglers & Retry/Escalate** — timeout, attempts, backoff, escalation target
- **Starvation Prevention**
- **Observability Signals**
- **Cost Envelope**

## Verification

- [ ] Routing optimizes a stated objective, not blind round-robin, when tasks differ.
- [ ] The queue is bounded and has an explicit overflow policy.
- [ ] Worker spawn and idle-deprovision rules are defined with min/max bounds.
- [ ] Retries are capped with backoff and a defined escalation target.
- [ ] Low-priority/expensive classes have a starvation-prevention mechanism.
- [ ] Fleet signals and the cost envelope are specified and cross-linked.

## False-Positive Prevention

❌ **DON'T:**
- Call routing "fair" because it's round-robin while one task class needs a specialist or costs 10× more.
- Leave the queue unbounded and assume bursts are rare.
- Retry a failing task on a loop without a cap or an escalation path.
- Size the pool by "max" alone, ignoring idle cost and cold-start latency.

✅ **DO:**
- Route to a stated objective (skill/cost/latency blend) with explicit tie-breakers.
- Bound the queue and define how overload sheds or throttles load.
- Cap retries with backoff and route exhausted tasks to a fallback or human.
- Set min/max pool bounds and reason about warm-vs-cold-start cost.

## Example Output

```markdown
## Routing Design: Mixed Support-Automation Fleet

### Task Classes & Worker Pool
| Class | Skill need | Worker | Cost | Latency |
|---|---|---|---|---|
| FAQ lookup | low | cheap-model worker | $ | fast |
| Refund action | high (write scope) | guarded worker | $$$ | med |
| Escalation triage | med | router worker | $$ | fast |

### Routing Rule
Objective = cheapest capable worker that meets the class SLA. FAQ → cheap worker; refund → guarded worker only (write scope); tie-break by lowest current queue depth.

### Pool Sizing & Scaling
Cheap workers: min 2 / max 20, spawn when queue depth > 50 or p95 latency > SLA, deprovision after 60s idle. Guarded workers: fixed 3 (scarce write credentials).

### Backpressure
Queue bound 500. Overflow: shed FAQ (cheap to retry) first, then throttle intake with retry-after; never shed refund tasks.

### Stragglers & Retry/Escalate
Per-task timeout 30s. Retries: 2 with exp backoff. Exhausted → human queue (see `aiagent_human_in_the_loop_design.md`).

### Starvation Prevention
Refund class has 1 reserved guarded worker so a FAQ burst can't starve refunds.

### Observability Signals
queue_depth/class, p95 latency/class, worker utilization, retry_rate. See `aiagent_observability_telemetry_design.md`.

### Cost Envelope
Max 20 cheap + 3 guarded ≈ ceiling $X/hr; see `aiagent_fleet_cost_attribution_optimization.md`.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** classify → route → scale → backpressure → retry/escalate.
- **RT-02 (Multi-Dimensional Analysis Framework):** routing weighs skill, cost, and latency together.
- **DS-06 (Prioritization & Severity Guidance):** backpressure and starvation rules prioritize by task class.
- **CM-02 (Constraint Specification):** queue bounds, pool limits, and the cost ceiling govern the design.
- **QA-01 (Self-Verification):** the checklist enforces bounded queues and capped retries.

**Related Prompts:**
- `aiagent_orchestration_topology_selection.md` — the coordination shape this routing layer serves.
- `aiagent_deployment_serving_architecture.md` — the runtime substrate routing runs on.
- `aiagent_human_in_the_loop_design.md` — the escalation target when retries are exhausted.
