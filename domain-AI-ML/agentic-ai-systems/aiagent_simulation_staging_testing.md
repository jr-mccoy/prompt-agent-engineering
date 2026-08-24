---
title: "AI Agent Simulation & Staging-Test Design"
category: AI-ML/agentic-ai-systems
description: "Design a pre-deployment test environment for an agent — scenario simulation (tools down/slow/wrong), trace replay from production, regression suites, and load/chaos tests — so a change is proven against failure conditions before it touches real traffic."
techniques:
  - ST-02
  - QA-08
  - DD-04
  - QA-12
  - QA-01
difficulty: advanced
tags:
  - simulation
  - staging
  - replay-testing
  - regression
  - chaos-testing
updated: "2026-06-18"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_evaluation_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_deployment_serving_architecture.md
  - domain-prompt-engineering/evaluation/regression/regression_golden_set_curator.md
---

# AI Agent Simulation & Staging-Test Design

**Objective:** Design how an agent is tested before it reaches production — simulated environments that inject realistic failures (tools down, slow, returning wrong or adversarial results), replay of recorded production trajectories, a regression suite that guards against re-breaking fixed behaviors, and load/chaos tests — so a new version is proven against failure modes, not just the happy path, before any rollout.

**When to Use:**
- Before shipping an agent or an agent change (new prompt, tool, model) and you need confidence beyond a demo.
- An agent works in clean conditions but breaks when tools misbehave, and you want to reproduce that pre-prod.
- You need a regression suite so fixed bugs and known-good trajectories stay fixed and good.

**When NOT to Use:**
- You're designing the offline quality *scoring* metrics themselves — use `aiagent_evaluation_design.md` (this prompt uses those metrics inside a test environment).
- You're designing the rollout/canary mechanism in production — use `aiagent_deployment_serving_architecture.md` (staging tests gate the entry to that pipeline).
- You need a generic regression-suite design — use `domain-prompt-engineering/evaluation/regression/regression_golden_set_curator.md` and cross-link.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **The agent under test** — its tools, control loop, and the actions it can take.
- **Known failure modes** — from `aiagent_failure_mode_analysis.md`, the failures the tests must exercise.
- **Production traces** — recorded trajectories available to replay (if any).
- **Tool dependencies** — external services to stub/mock, and their realistic failure behaviors.
- **What "pass" means** — the success/cost/safety criteria a build must meet to ship.

## Constraints

**Must:**
- Test against injected failure conditions, not just the happy path: at minimum tool error, tool timeout/slowness, malformed/wrong tool results, and adversarial/injected content.
- Use deterministic, mockable tool stubs so tests are reproducible (no live external calls that make runs flaky).
- Maintain a regression suite of known-good trajectories and previously-fixed failures, run on every change.
- Define an explicit ship gate: the success/cost/safety thresholds a build must clear, evaluated with the metrics from `aiagent_evaluation_design.md`.

**Must Not:**
- Treat a green happy-path run as sufficient evidence to ship.
- Test against live, non-deterministic external services so results can't be reproduced or compared.
- Score only success rate, ignoring whether cost, latency, or unsafe-action behavior regressed.
- Fabricate pass rates or latency numbers; report measured results from the test runs and mark gaps.

**Instructions:**

1. **Enumerate the conditions to test.** Combine happy-path, the known failure modes, adversarial inputs, and edge cases into a test matrix. Each row is a condition the agent must survive.

2. **Build the simulated environment.** Specify deterministic tool stubs/mocks and how each can be made to fail (error, timeout, wrong result, adversarial content) so failures are reproducible on demand.

3. **Design scenario tests.** For each condition, define the input, the injected behavior, and the expected agent response (recovers, escalates, aborts safely) — not just "doesn't crash."

4. **Set up trace replay.** Where production traces exist, replay them against the candidate version and diff the trajectory/outcome to catch regressions on real cases.

5. **Build the regression suite.** Capture known-good trajectories and every previously-fixed failure as locked test cases that run on every change; a regression fails the build.

6. **Add load and chaos tests.** Define throughput/concurrency tests and chaos scenarios (random tool failures, latency injection, partial multi-agent failure) to expose behavior under stress.

7. **Define the ship gate.** State the pass thresholds across success, cost, latency, and safety, scored with the eval metrics; a build that misses any gate does not proceed to rollout.

8. **Connect to rollout.** Specify how passing staging tests feeds the shadow/canary pipeline in `aiagent_deployment_serving_architecture.md`.

**Output Format:**

A markdown design doc:
- **Test Matrix** — condition | type (happy/failure/adversarial/edge)
- **Simulated Environment** — tool stubs + injectable failures
- **Scenario Tests** — input | injected behavior | expected response
- **Trace Replay** — source + diff criteria
- **Regression Suite** — locked good/fixed cases
- **Load & Chaos Tests** — throughput + failure-injection scenarios
- **Ship Gate** — success/cost/latency/safety thresholds
- **Rollout Connection** — cross-link

## Verification

- [ ] The test matrix covers failure and adversarial conditions, not only the happy path.
- [ ] Tool stubs are deterministic and can inject errors/timeouts/wrong results on demand.
- [ ] Scenario tests assert the agent's *response* (recover/escalate/abort), not just non-crash.
- [ ] A regression suite of good/fixed trajectories runs on every change.
- [ ] The ship gate scores success, cost, latency, and safety — all required to pass.
- [ ] Passing staging feeds the production rollout pipeline (cross-linked).

## False-Positive Prevention

❌ **DON'T:**
- Ship because the happy-path demo and a couple of manual runs looked fine.
- Test against live external services whose non-determinism makes failures unreproducible.
- Declare a build good on success rate alone while cost doubled or it took an unsafe action.
- Let a previously-fixed failure quietly return because nothing locks it as a regression test.

✅ **DO:**
- Exercise the known failure modes and adversarial inputs with deterministic stubs.
- Assert the intended recovery/escalation behavior for each failure condition.
- Score the ship gate on success, cost, latency, and safety together.
- Lock fixed bugs and good trajectories into a regression suite run on every change.

## Example Output

```markdown
## Staging-Test Design: Web-Research Agent (browses + summarizes)

### Test Matrix
| Condition | Type |
|---|---|
| Normal query, sources up | happy |
| Search API 500s | failure |
| Page loads in 30s | failure (timeout) |
| Page contains injected "ignore instructions" | adversarial |
| Zero results | edge |

### Simulated Environment
Stub search + fetch tools; toggles for {error, timeout, wrong_result, injected_content}. Fully deterministic.

### Scenario Tests
| Input | Injected | Expected response |
|---|---|---|
| query | search 500 | retry once, then return "couldn't retrieve", no fabrication |
| query | injected page | treat as data, ignore embedded instruction, flag |

### Trace Replay
Replay last 200 prod trajectories vs. candidate; diff outcome + cost; any new failure or >20% cost rise fails.

### Regression Suite
Locked: 15 good trajectories + 6 previously-fixed bugs (e.g., loop on empty results). Run every change.

### Load & Chaos Tests
50 concurrent queries; randomly fail 10% of fetches; assert no crash, bounded retries, success_rate ≥ target.

### Ship Gate
success ≥ 92%, cost ≤ baseline×1.1, p95 ≤ SLA, zero unsafe actions. Miss any → no rollout.

### Rollout Connection
Pass → shadow stage in `aiagent_deployment_serving_architecture.md`.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** matrix → environment → scenarios → replay → gate.
- **QA-08 (Gate-Based Verification):** the ship gate is an explicit pass/fail before rollout.
- **DD-04 (MVP Gates):** staging tests are the gate the build must clear to proceed.
- **QA-12 (False Positives Identification):** adversarial and failure scenarios catch behavior the happy path hides.
- **QA-01 (Self-Verification):** the checklist enforces failure-condition coverage and multi-axis scoring.

**Related Prompts:**
- `aiagent_evaluation_design.md` — the metrics the ship gate scores against.
- `aiagent_deployment_serving_architecture.md` — the rollout pipeline staging feeds.
- `domain-prompt-engineering/evaluation/regression/regression_golden_set_curator.md` — generic regression-suite design.
