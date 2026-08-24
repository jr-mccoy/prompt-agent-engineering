---
title: "AI Agent Safety & Sandboxing Design"
category: AI-ML/agentic-ai-systems
description: "Design sandboxing, permissioning, and oversight for an agent that takes real-world actions, so its blast radius is bounded by construction rather than by the model's good behavior."
techniques:
  - ST-02
  - CM-02
  - DS-06
  - AG-13
  - QA-12
difficulty: advanced
tags:
  - agent-safety
  - sandboxing
  - least-privilege
  - oversight
  - blast-radius
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_tool_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md
---

# AI Agent Safety & Sandboxing Design

**Objective:** Design the containment around an agent that can affect the real world — its sandbox, permission scopes, action allow/deny lists, oversight, and kill switch — so that the worst thing it can do is bounded by the system's construction, not by trusting the model to behave or to resist prompt injection.

**When to Use:**
- The agent can take state-changing or external actions (writes, payments, emails, deploys, file/network access).
- The agent processes untrusted input (web content, user files) and could be steered by prompt injection.
- Before granting an agent any production credential or autonomy.

**When NOT to Use:**
- The agent is strictly read-only with no external side effects and no untrusted input — sandboxing is still good hygiene but this prompt is overkill; note the read-only conclusion.
- You only need approval-gate calibration (use `aiagent_human_in_the_loop_design.md`) or per-tool contracts (use `aiagent_tool_design.md`).

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Action inventory** — every action the agent can take and its reversibility / blast radius.
- **Credentials & scopes** — what the agent authenticates as and what those credentials can touch.
- **Untrusted input sources** — web, user uploads, third-party tool outputs that could carry injection.
- **Environment** — where it runs (container, VM, prod vs. staging), network egress, filesystem access.
- **Oversight available** — human approvers, monitoring, logging, rate of operation.

## Constraints

**Must:**
- Bound the blast radius structurally: least-privilege credentials, allow-listed actions/targets, resource and rate limits — independent of the model's outputs.
- Treat all untrusted input as potentially adversarial; assume prompt injection will be attempted and ensure it cannot escalate privilege or trigger irreversible actions.
- Provide a kill switch and an audit log; every state-changing action must be attributable and (where possible) reversible.

**Must Not:**
- Rely on prompt instructions ("do not delete files") as a safety control — instructions are not a sandbox.
- Grant production write/payment/deploy scope when staging or a draft/queue would suffice.
- Allow an irreversible action to occur without a gate, a confirmation token, or a human approval.

**Instructions:**

1. **Inventory actions by blast radius.** List every action and classify it: read-only, reversible-write, irreversible/external. The most dangerous action sets the containment bar for the whole system.

2. **Apply least privilege to credentials.** Scope each credential to the minimum resources/targets needed; prefer separate narrow credentials per tool over one broad one. Default to read-only; grant write only where a task requires it.

3. **Define allow/deny lists for actions and targets.** Enumerate permitted operations and permitted targets (paths, recipients, accounts). Deny by default; an action outside the list is blocked, not warned.

4. **Contain the runtime.** Specify execution isolation (container/VM), filesystem scope, network egress allow-list, and resource limits (CPU/memory/time). Untrusted code or content runs with no path to credentials or the host.

5. **Harden against prompt injection.** Treat tool outputs and fetched content as data, not instructions; ensure injected text cannot widen scope, invoke privileged tools, or bypass gates. State the boundary between trusted policy and untrusted content.

6. **Route irreversible actions through oversight.** For each irreversible/high-blast action, require a confirmation token, a human approval gate, or a reversible proxy (draft/queue). Cross-link `aiagent_human_in_the_loop_design.md` for thresholds.

7. **Add a kill switch, rate limits, and audit logging.** Provide a way to halt the agent immediately, cap operation rate (e.g., N writes/min), and log every action with inputs, decision, and actor for attribution and rollback.

8. **Pair safety with cost & latency impact.** Note where containment adds latency or cost (approval waits, sandboxing overhead) so safety tradeoffs are explicit, not discovered later.

**Output Format:**

A markdown safety design:
- **Action Blast-Radius Inventory** — table: Action | Class | Worst case | Containment
- **Credential & Privilege Map** — scope per credential, read vs. write
- **Allow/Deny Lists** — permitted actions + targets; default-deny stated
- **Runtime Containment** — isolation, filesystem, egress, resource limits
- **Injection Hardening** — trusted/untrusted boundary
- **Oversight & Controls** — gates, kill switch, rate limits, audit log
- **Safety vs. Cost/Latency Notes** — explicit tradeoffs

## Verification

- [ ] Blast radius is bounded by construction (scopes, allow-lists, limits), not by model instructions.
- [ ] Every credential is least-privilege; production write/payment/deploy scope is justified or avoided.
- [ ] Untrusted input is treated as data; injection cannot escalate privilege or trigger irreversible actions.
- [ ] Every irreversible action has a gate, token, or reversible proxy.
- [ ] A kill switch, rate limit, and per-action audit log exist.
- [ ] Latency/cost added by containment is stated.

## False-Positive Prevention

❌ **DON'T:**
- Treat a system-prompt rule ("never email customers") as a control — the model can be injected or simply err past it.
- Assume the agent won't be prompt-injected because the demo wasn't; design for the adversarial input.
- Grant broad prod credentials "to avoid friction" and rely on the agent to use them narrowly.
- Call an action reversible without verifying a concrete rollback path exists.

✅ **DO:**
- Enforce limits in the runtime/credentials/allow-lists so an unsafe instruction simply cannot execute.
- Assume injection will be attempted and verify it cannot reach privileged tools or widen scope.
- Default-deny actions and targets; add only what a task requires.
- Provide a real kill switch and audit trail, and confirm rollback paths for "reversible" actions.

## Example Output

```markdown
## Safety Design: DevOps Deploy-Assist Agent

### Action Blast-Radius Inventory
| Action | Class | Worst case | Containment |
|---|---|---|---|
| read logs/metrics | Read-only | none | read creds only |
| open PR | Reversible | bad diff | PR requires human merge |
| deploy to staging | Reversible | staging breakage | allowed, rate-limited |
| deploy to prod | Irreversible | outage | NOT granted; human runs after approval |

### Credential & Privilege Map
- `obs-read` (logs/metrics): read-only. `repo-pr`: create PR only, no merge, no force-push. No prod-deploy credential issued to the agent.

### Allow/Deny Lists
Permitted: read obs, create PR on allow-listed repos, deploy to `staging-*`. Default-deny everything else, incl. prod targets and secret reads.

### Runtime Containment
Runs in ephemeral container; filesystem limited to checkout dir; egress allow-list (git host, obs API); 5-min CPU cap.

### Injection Hardening
Fetched logs/issue text treated as data; cannot invoke tools or alter the policy block. Tool dispatch is from a fixed registry, not from model-emitted code.

### Oversight & Controls
Kill switch halts loop + revokes session token. Rate limit: 3 staging deploys/10 min. Audit log: every action {tool, args, decision, ts, run_id}.

### Safety vs. Cost/Latency Notes
Human merge gate adds ~minutes of latency to prod path — accepted for an irreversible action. Container spin-up adds ~2s/run.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** inventory → privilege → allow-lists → runtime → injection → oversight.
- **CM-02 (Constraint Specification):** scopes, allow-lists, and limits are the governing constraints.
- **DS-06 (Prioritization & Severity Guidance):** the worst-blast action sets the containment bar.
- **AG-13 (Agent Safety & Guardrails):** structural containment and kill switch are the core deliverable.
- **QA-12 (False Positives Identification):** distinguishes real controls from instruction-only "safety."

**Related Prompts:**
- `aiagent_tool_design.md` — the per-tool scopes this design enforces at runtime.
- `aiagent_human_in_the_loop_design.md` — calibrate the approval gates referenced here.
- `aiagent_failure_mode_analysis.md` — the unsafe-action failures this containment bounds.
