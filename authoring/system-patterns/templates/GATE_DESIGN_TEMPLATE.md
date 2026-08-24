# GATE DESIGN — `<system name>`

> Fill during Step 4. **Gates are enforced in code/config, never "the agent will remember."** Size every gate to the blast radius from the architecture doc §1. The OWASP-ASI security gate (Gate A) is load-bearing — a design that skips it for its blast radius is not Tier 1.

**System:** `<name>` · **Blast radius:** `<from ARCHITECTURE §1>`

---

## Gate 0 — Justification (already passed in Step 0)
- Written reason an agent beats a workflow: `<paste from ARCHITECTURE §2>`

---

## Gate A — Security (OWASP ASI)

Mark each as: **Enforced (how/where in code)** · **N/A (why)** · **TODO**. N/A must be justified.

| SAFE pattern | ASI | Requirement | Status & enforcement point |
|--------------|-----|-------------|----------------------------|
| SAFE-01 Data/control separation | ASI01 | Untrusted data never drives control flow / tool selection (CaMeL) | |
| SAFE-05 Injection defense | ASI01 | Validate/sanitize all external content; monitor objective drift | |
| SAFE-02 Deterministic policy enforcement | ASI02/05 | Tool allowlist + schema/arg validation + pre-execution check | |
| SAFE-04 Least-privilege tools | ASI02/03 | Minimal tool set/agent; high-privilege ops re-verify intent | |
| SAFE-03 Least-agency scoping | — | No autonomy beyond what the task needs | |
| SAFE-08 Governed identity | ASI03 | Unique identity/agent; attributable; no credential caching | |
| SAFE-06 Memory-poisoning defense | ASI06 | Access control + integrity validation on memory/RAG | |
| SAFE-10 Inter-agent trust | ASI07/10 | Encrypt+authenticate peers; documented trust model | |
| SAFE-07 Cascading-failure breakers | ASI08 | Circuit breakers + blast-radius caps + isolation | |
| (RCE) Sandbox code exec | ASI05 | Sandbox + human review of destructive/unreviewed code | |

**Defense-in-depth (3 layers) — confirm all three exist where untrusted content is processed:**
- [ ] Input-level detection (perplexity/spotlighting/sandwiching) — *reduces attack volume*
- [ ] Model-level instruction hierarchy (system > user > assistant) — *raises the bar*
- [ ] **System/execution-level deterministic policy enforcement** — *hard limits on consequences, regardless of LLM output*

---

## HITL approval gates (SAFE-09)

| Action class | Risk | Gate | Approver | Confidence threshold |
|--------------|------|------|----------|----------------------|
| `<e.g., publish/send/spend>` | high | human approval | `<role>` | `<e.g., <0.9 ⇒ escalate>` |
| `<medium>` | med | log + post-hoc review | | |
| `<read-only>` | low | none | | |

> Use **risk-adaptive authorization** (RBAC + aggregated-risk thresholds), not a confirmation prompt on every action (confirmation fatigue defeats the gate).

---

## Loop bounds & cap-fallbacks

| Loop | Bound | Fallback at cap |
|------|-------|-----------------|
| Main agent loop (`max_turns`) | `<N>` | `<return partial + flag, not silent stop>` |
| Evaluator-optimizer iterations | `<N>` | `<best-so-far + reason>` |
| Handoff chain length | `<N>` | `<halt + escalate>` |
| Sub-agent spawn count | `<N>` | `<reject + alert>` |

---

## Kill switch

- **Mechanism:** `<e.g., config flag `mandate.halt: true` checked before every action-taking step>`
- **Scope when active:** `<stops all action-taking; read/observe may continue>`
- **Who can trip it:** `<operator / automated trigger on X>`
- **Test:** `<how you verify it actually halts>`

---

## Gate C — Production-readiness handoff (detail in DISCLOSURE_MANIFEST)

- [ ] Disclosure manifest complete (6 dimensions)
- [ ] Observability/traces + approval records present
- [ ] Rollback/recovery path for every state-modifying action
- [ ] (Multi-agent) inter-agent trust model documented before rollout
- [ ] Adaptive security benchmark run pre-deploy
