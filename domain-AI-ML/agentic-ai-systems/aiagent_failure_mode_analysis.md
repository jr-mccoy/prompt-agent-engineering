---
title: "AI Agent Failure-Mode Analysis"
category: AI-ML/agentic-ai-systems
description: "Enumerate, prioritize, and mitigate the ways an agent fails — loops, hallucinated tool calls, runaway cost, stalls, and unsafe actions — with detection signals and bounded recovery for each."
techniques:
  - ST-02
  - RT-09
  - RT-10
  - DS-06
  - QA-12
difficulty: advanced
tags:
  - failure-modes
  - loops
  - hallucinated-tool-calls
  - runaway-cost
  - unsafe-actions
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_safety_sandboxing.md
  - domain-AI-ML/agentic-ai-systems/aiagent_cost_token_budget_design.md
---

# AI Agent Failure-Mode Analysis

**Objective:** Produce a prioritized failure-mode catalog for a specific agent — the concrete ways it can loop, hallucinate tool calls, stall, overspend, or take unsafe actions — each with a detection signal, a severity (likelihood × consequence), and a bounded mitigation, so the agent fails safely and cheaply rather than dramatically.

**When to Use:**
- Before shipping an agent, to harden it against the failures that don't appear in the happy-path demo.
- After an incident (a loop, a runaway bill, an unsafe action) to systematize what else could go wrong.
- As input to the evaluation harness (`aiagent_evaluation_design.md`) and safety design.

**When NOT to Use:**
- You have no agent design yet (start with `aiagent_architecture_design.md`).
- You only need runtime sandboxing/permissioning (use `aiagent_safety_sandboxing.md`) — though this analysis feeds it.

## Inputs / Context

Provide what you can; the analysis degrades gracefully if some are missing:
- **Agent design** — planning approach, tools, memory, control loop, stopping conditions.
- **Action surface** — which actions are read-only vs. state-changing/irreversible.
- **Budgets** — cost/latency/step ceilings and what currently enforces them.
- **History** — any observed failures, loops, or near-misses.
- **Environment** — autonomy level, human availability, monitoring in place.

## Constraints

**Must:**
- Anchor each failure mode to a specific component of this agent (a named tool, the loop, a memory tier) — no generic "agents can fail" list.
- Give each failure a detection signal, a severity rating, and a bounded mitigation (cap, breaker, gate, or escalation).
- Treat unsafe/irreversible actions as a distinct, highest-priority class regardless of likelihood.

**Must Not:**
- List failure modes that this agent's design cannot exhibit (e.g., memory pollution for a stateless agent) without marking them N/A and why.
- Propose mitigations that themselves have no bound (e.g., "retry until it works").
- Score "success rate" as adequate evidence of safety — low-probability catastrophic actions still gate.

**Instructions:**

1. **Map the agent's surface.** From the design, list the loop, each tool, each memory tier, and each external action. These are the sites where failures originate.

2. **Enumerate loop & progress failures.** Identify infinite loops, oscillation between states, no-progress repetition, and premature stopping. State the detection signal (repeated state, step count, no observable progress) and the bound (step cap, repeated-state detector).

3. **Enumerate tool-interaction failures.** Hallucinated/invented tool calls, malformed arguments, mishandled errors, retry-after-success, and acting on a tool error as if it succeeded. Tie each to a tool's error contract or schema.

4. **Enumerate cost & latency failures.** Runaway token/dollar spend, context-window exhaustion, and latency blowouts. State the circuit breaker and the degrade/abort behavior (cross-link `aiagent_cost_token_budget_design.md`).

5. **Enumerate safety & action failures.** Irreversible or out-of-scope actions, privilege misuse, prompt-injection-driven actions, and data exfiltration. These are highest priority; map each to a gate, sandbox, or human approval (cross-link `aiagent_safety_sandboxing.md`).

6. **Enumerate correctness & grounding failures.** Confidently wrong outputs, ungrounded claims, and acting on stale memory. Distinguish "wrong but harmless" from "wrong and acted upon."

7. **Rank by severity and assign mitigations.** Score each failure by likelihood × consequence; for each, give a bounded mitigation and how it's verified. Surface residual risk that no mitigation fully closes.

8. **Define monitoring & alerts.** State which signals to log in production and which thresholds trigger an alert or auto-abort, so failures are caught early, not in the bill or the incident review.

**Output Format:**

A markdown failure analysis:
- **Surface Map** — loop, tools, memory, actions
- **Failure-Mode Register** — table: Failure | Origin | Detection signal | Likelihood | Consequence | Severity | Mitigation (bounded) | Residual risk
- **Highest-Priority (Unsafe) Actions** — called out separately with gates
- **Monitoring & Alert Thresholds** — signals + trigger points
- **Residual Risk Summary** — what remains and why it's acceptable (or not)

## Verification

- [ ] Every failure mode is tied to a named component of this agent, not generic.
- [ ] Failure modes impossible for this design are marked N/A with a reason.
- [ ] Each failure has a detection signal and a *bounded* mitigation.
- [ ] Unsafe/irreversible actions are the top priority regardless of likelihood.
- [ ] Severity = likelihood × consequence is assigned and used to rank.
- [ ] Monitoring signals and alert/abort thresholds are specified.

## False-Positive Prevention

❌ **DON'T:**
- Down-rank an unsafe action because it is "unlikely" — consequence dominates for irreversible actions.
- List generic agent failures the design can't actually produce, padding the register.
- Propose "retry" or "add a check" without a bound (max retries, who reviews, when it aborts).
- Conclude an agent is safe because it passed the happy-path runs.

✅ **DO:**
- Rank by likelihood × consequence and let catastrophic-but-rare actions gate the release.
- Trace each failure to a specific tool, loop step, or memory tier so the mitigation lands somewhere real.
- Bound every mitigation (cap, breaker, gate, escalation) and state how it's verified.
- Define production monitoring so loops, cost spikes, and unsafe attempts are caught in flight.

## Example Output

```markdown
## Failure-Mode Analysis: Codebase-Refactor Agent

### Surface Map
Loop: react, 15-step cap. Tools: read_file (R), search (R), write_file (W), run_tests (exec). Memory: in-task scratchpad. Actions: file writes (reversible via git), test execution (sandboxed).

### Failure-Mode Register
| Failure | Origin | Detection | Likelihood | Consequence | Severity | Mitigation | Residual |
|---|---|---|---|---|---|---|---|
| Edit/test oscillation | loop | same file edited >3x no test progress | Med | wasted cost | High | repeated-state detector → abort+report | low |
| Hallucinated file path in write_file | write_file | path not in repo index | Med | corrupt write | High | schema validates against index; reject | low |
| Runaway tokens on large repo | loop+read_file | tokens > 60k | Med | $ spend | High | breaker aborts at 60k, returns partial | low |
| Deletes/overwrites unrelated file | write_file | write outside target dir | Low | data loss | **Critical** | scope to target dir + git checkpoint + human approve on >10 files | medium |
| Acts on failing test as if passing | run_tests | exit code ignored | Low | bad merge | High | structured result; loop branches on pass/fail | low |

### Highest-Priority (Unsafe) Actions
write_file outside target dir → blocked by least-privilege scope + human gate; never auto-merges.

### Monitoring & Alert Thresholds
Alert: any run > 12 steps or > 50k tokens. Auto-abort: write outside scope, or 3 identical edits.

### Residual Risk Summary
Within-target logical-but-wrong refactors remain (caught by test gate + human review of diff). Accepted given reversibility via git.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** surface map → loop → tools → cost → safety → ranking.
- **RT-09 (Root Cause Explanation):** each failure is traced to its originating component.
- **RT-10 (Troubleshooting Decision Tree):** detection signals route each failure to a bounded response.
- **DS-06 (Prioritization & Severity Guidance):** likelihood × consequence ranks the register.
- **QA-12 (False Positives Identification):** prunes failures the design can't exhibit and unbounded "mitigations."

**Related Prompts:**
- `aiagent_architecture_design.md` — the design whose components this analysis stresses.
- `aiagent_safety_sandboxing.md` — where the unsafe-action mitigations are enforced at runtime.
- `aiagent_cost_token_budget_design.md` — the breakers that bound the cost/latency failures.
