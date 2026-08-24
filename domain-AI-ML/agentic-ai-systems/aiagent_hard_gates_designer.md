---
title: "AI Agent Hard-Gates Designer (Gate A/B/C + Kill Switch, Code-Not-Trust)"
category: AI-ML/agentic-ai-systems
description: "Compose the OWASP-ASI security, ABC/real-tool evaluation, and governance/disclosure checks into a small set of enforced, code-level gates — Gate A (prerequisite/security), Gate B (mid-execution limits + evaluation), Gate C (terminal/governance unlock) — plus an explicit kill switch, all sized to the system's blast radius and enforced in code, never in prose the agent is trusted to honor."
techniques:
  - ST-02
  - CM-02
  - DS-06
  - AG-09
  - QA-01
difficulty: advanced
tags:
  - hard-gates
  - code-not-trust
  - owasp-asi
  - kill-switch
  - policy-enforcement
updated: "2026-06-20"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_runtime_guardrails_policy.md
  - domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_agentic_threat_model.md
---

# AI Agent Hard-Gates Designer (Gate A/B/C + Kill Switch, Code-Not-Trust)

**Objective:** Turn the scattered security, evaluation, and governance requirements of an agentic system into a **small, enforced gate architecture** — Gate A (prerequisite/security checks that must pass before the system may act), Gate B (mid-execution limits, risk thresholds, and capability/safety eval gates), Gate C (terminal unlock: governance, disclosure, and rollback readiness before "production-ready") — plus an explicit, code-level **kill switch**. Every gate is enforced deterministically in code or config, sized to the system's blast radius, so that a prohibited action is blocked *regardless of what the LLM outputs*. This composes the checks that live in many separate prompts into one reusable Gate A/B/C designer; it does not re-derive each individual control.

**When to Use:**
- A system design exists (topology + tools + agents) and you need to convert its risks into enforced gates before it can act.
- Controls are scattered across guardrail/HITL/threat-model prompts and you need them composed into A/B/C + a kill switch.
- You must decide, for the actual blast radius, which checks are mandatory pre-conditions vs. mid-run limits vs. terminal-release conditions.

**When NOT to Use:**
- No system exists yet — design it first (`aiagent_architecture_design.md`), and gate the agent-vs-workflow question with `aiagent_complexity_ladder_gate.md`.
- You need the *content* of one control in depth (how to defend injection, where to place HITL) — use the specific prompt and feed its output into this composer.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **System summary** — topology, agents, tools, and whether it is single- or multi-agent.
- **Blast radius** — the worst action the system can take, per tool/agent (sends money, deletes data, emails externally, executes code).
- **Trust map** — which inputs/content are untrusted external data; which tools are high-privilege.
- **Existing control designs** — outputs from guardrail/HITL/injection/threat-model/eval prompts, if any.
- **Governance context** — disclosure obligations, jurisdiction/regulatory regime, rollback expectations.
- **Operational limits** — cost/latency/loop ceilings and who can invoke a halt.

## Constraints

**Must:**
- Enforce every gate in **code or config**, not in instructions the agent is asked to follow; a gate that depends on the LLM "remembering" is not a gate.
- Size each gate to the blast radius: high-consequence/irreversible actions get mandatory pre-checks and HITL; routine reversible ones flow.
- Include all four layers: Gate A (security/prerequisite), Gate B (mid-execution limits + eval), Gate C (governance/disclosure unlock), and an explicit kill switch with a defined safe state.

**Must Not:**
- Collapse capability and safety into one eval gate — they are independent; a capable system can be unsafe (real-tool unsafe-action rates run 51–73%).
- Leave any loop unbounded or any cap without a defined fallback behavior.
- Mark a system "production-ready" with Gate C unmet (no disclosure manifest, no rollback path, no audit trail).

**Instructions:**

1. **Inventory actions and rank by blast radius.** List every consequential action (per tool/agent), score reversibility × consequence, and order them. This ranking decides which gate each control belongs to and how strict it is.

2. **Compose Gate A — prerequisite/security (OWASP ASI, before the system may act).** Select the minimum mandatory set for this blast radius, each box deliberate: governed unique identity per agent + attributable actions, no credential caching (ASI03); least privilege per tool with intent re-verification for high-privilege ops (ASI02/03); **data/control separation** so untrusted data never drives control flow or tool selection (CaMeL, ASI01); indirect-injection defense on all external content (ASI01); **deterministic policy enforcement** — tool allowlists + schema/arg validation pre-execution + rate limits (the only layer that blocks regardless of LLM output, ASI02/05); sandboxed code execution with human review of destructive code (ASI05); access-control + integrity validation on memory/RAG (ASI06); encrypted, authenticated inter-agent messages if multi-agent (ASI07). State each as an enforceable rule, not an aspiration.

3. **Compose Gate B — mid-execution limits + evaluation.** Define the runtime envelope the system must stay inside: loop/iteration/tool-call caps each with a **cap-fallback**; cost/latency circuit breakers + blast-radius caps vs. cascading failure (ASI08); risk-adaptive authorization (RBAC + aggregated-risk thresholds, not confirmation fatigue) with HITL approval for high-risk actions (ASI09). Attach the **two independent eval gates** as release pre-conditions: capability (ABC-valid acceptance suite) **and**, separately, real-tool safety (OpenAgentSafety 8 categories) — cross-link `aiagent_agentic_safety_eval_layer.md`, do not re-derive.

4. **Compose Gate C — governance/disclosure terminal unlock.** Define what must be true before "production-ready": disclosure manifest covering the 6 AI Agent Index dimensions (incl. safety evals actually run); audit trail of request + each tool action; documented inter-agent trust model before any multi-agent rollout; rollback/recovery path for failed tool actions; measurable aligned objectives + behavioral monitoring + spawn/resource limits (ASI10); and, for fleets, population-level/emergent-behavior monitoring. Behind a jurisdiction selector, cross-link the relevant `responsible-ai-governance/` regulatory assessments.

5. **Design the kill switch.** Specify an explicit, code-level halt (e.g., a `halt` flag in config the runtime checks before every action) that revokes the system's ability to act, who can trip it, how it propagates to in-flight agents, and the **safe state** it leaves behind (in-flight work checkpointed, no half-completed irreversible action).

6. **Assign each control to exactly one gate and mark enforcement.** For every control: which gate, enforced where (code module / policy engine / config), fail-closed or fail-open, and the observable signal that proves it fired. Anything you cannot point to a code/config location for is not yet a gate — flag it.

7. **Define gate transitions and defaults.** State the default-safe behavior at each boundary: Gate A fails → system never starts; Gate B cap/threshold hit → fallback (hold/abort/escalate), never silent proceed on a risky class; Gate C unmet → not releasable. Risky-action timeouts default to hold/abort, never proceed.

8. **Produce the enforced-gate spec.** Output the gates as a checklist of code-enforced rules with locations, plus the kill-switch spec — the artifact a builder wires directly, and an auditor checks against.

**Output Format:**

A markdown gate spec:
- **Action Blast-Radius Ranking** — table: Action | Reversibility | Consequence | Strictest gate it needs
- **Gate A — Security/Prerequisite** — table: Control | OWASP ASI | Enforced where (code/config) | Fail-closed?
- **Gate B — Limits + Evaluation** — loop/cost/risk caps + cap-fallbacks; capability and safety eval gates (cross-linked)
- **Gate C — Governance/Disclosure Unlock** — disclosure manifest, audit trail, trust model, rollback, monitoring
- **Kill Switch** — mechanism, trigger authority, propagation, safe state
- **Transition Defaults** — default-safe behavior at each gate boundary
- **Enforcement Audit** — any control not yet tied to a code/config location, flagged

## Verification

- [ ] Every gate names a code/config enforcement location; none rely on the LLM honoring prose.
- [ ] Gates are sized to the blast-radius ranking, not applied uniformly.
- [ ] Capability and safety eval gates are present and **separate**, both as Gate B release pre-conditions.
- [ ] Every loop/cap has a defined fallback; risky-action defaults are hold/abort, never silent proceed.
- [ ] A kill switch exists with a trigger authority, propagation path, and defined safe state.
- [ ] Gate C blocks "production-ready" until disclosure, audit trail, rollback, and (if multi-agent) trust model are met.

## False-Positive Prevention

❌ **DON'T:**
- Write "the agent should not exfiltrate data" in the system prompt and call it a gate — the LLM can be talked out of it; only deterministic policy enforcement is a gate.
- Pass capability eval and ship — a capable system is unsafe by default in real-tool settings until the separate safety eval passes.
- Bound a loop with a cap that just stops silently at the limit with no fallback.
- Declare "production-ready" while the disclosure manifest, audit trail, or rollback path is missing.

✅ **DO:**
- Tie every gate to a code/config location an auditor can inspect and a signal that proves it fired.
- Keep capability and safety as two independent gates, both required for release.
- Give every cap an explicit fallback and default risky timeouts to hold/abort.
- Make the kill switch real: a flag the runtime checks before acting, with a checkpointed safe state.

## Example Output

```markdown
## Gate Spec: Autonomous Invoice-Payment Agent (single agent, high blast radius)

### Action Blast-Radius Ranking
| Action | Reversibility | Consequence | Strictest gate |
|---|---|---|---|
| Read invoice | Reversible | none | Gate A allowlist |
| Match to PO | Reversible | low | Gate A + schema validation |
| Schedule payment ≤ $1k | Hard to reverse | medium ($) | Gate B HITL (sampled) |
| Release payment > $1k | Irreversible | high ($) | Gate B HITL pre-approval |

### Gate A — Security/Prerequisite
| Control | ASI | Enforced where | Fail-closed? |
|---|---|---|---|
| Unique service identity, no cached creds | ASI03 | IAM + secrets broker | yes |
| Payment tool allowlist + arg schema validation | ASI02/05 | policy engine (pre-exec) | yes |
| Invoice text treated as untrusted; cannot set payee | ASI01 | CaMeL taint-tracking | yes |

### Gate B — Limits + Evaluation
Loop cap 12 tool calls → fallback: escalate to human. Daily spend circuit breaker $50k → halt.
Risk threshold: any payment > $1k → HITL pre-approval. Eval gates (release pre-conditions):
capability ABC suite ≥ 0.95 on payee-match; **separate** real-tool safety eval (8 cats) — see
`aiagent_agentic_safety_eval_layer.md`. Both must pass.

### Gate C — Governance/Disclosure Unlock
Disclosure manifest (6 dims, incl. safety evals run); audit trail of every payment + tool call;
rollback = payment-reversal runbook; SR 11-7 model-risk assessment (jurisdiction selector). Not
releasable until all present.

### Kill Switch
`config.halt = true` checked before every tool call; tripped by on-call or spend breaker;
propagates to in-flight run → checkpoint, no partial payment release. Safe state = no money moves.

### Transition Defaults
Gate A fail → never starts. Loop cap → escalate. Payment timeout on approval → hold (never auto-release).

### Enforcement Audit
All controls tied to a code/config location. None rely on prompt prose.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** inventory → Gate A → Gate B → Gate C → kill switch → enforcement audit.
- **CM-02 (Constraint Specification):** the must/must-not rules make code-enforcement and separate eval gates non-negotiable.
- **DS-06 (Prioritization and Severity Guidance):** the blast-radius ranking decides each control's gate and strictness.
- **AG-09 (Anti-Pattern & Failure Mode Embedding):** the OWASP-ASI failure modes are embedded as the rules each gate enforces.
- **QA-01 (Chain-of-Verification):** the enforcement audit forces every control back to a code/config location or flags it.

**Related Prompts:**
- `aiagent_runtime_guardrails_policy.md` — the deterministic policy-enforcement layer Gate A composes.
- `aiagent_human_in_the_loop_design.md` — the risk-adaptive HITL thresholds Gate B references.
- `aiagent_agentic_threat_model.md` — the OWASP-ASI threat surface these gates are sized against.
