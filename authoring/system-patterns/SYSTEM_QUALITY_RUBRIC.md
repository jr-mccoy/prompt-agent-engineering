# Agentic System Quality Rubric

**Purpose:** Score an agentic-system design on a 100-point scale before stamping it "production-ready."
**Target score:** 75/100.
**Usage:** Score each category, sum, identify gaps. **Two categories are load-bearing gates (see below) — failing either disqualifies the design regardless of total.**

---

## Scoring Overview

### Score distribution

| # | Category | Points | Load-bearing? |
|---|----------|--------|---------------|
| 1 | Agent justification & complexity-appropriateness | 15 | — |
| 2 | Topology fit & primitive correctness | 15 | — |
| 3 | **Security gate coverage vs OWASP ASI** | **20** | ✅ **GATE** |
| 4 | **Evaluation validity (ABC) + real-tool safety eval** | **20** | ✅ **GATE** |
| 5 | Durability / observability / cost design | 10 | — |
| 6 | Documentation completeness (3-layer + disclosure manifest) | 10 | — |
| 7 | Cross-link hygiene / no duplication / no-fabrication | 10 | — |
| | **Total** | **100** | |

### The two load-bearing gates (analogy: False-Positive Prevention for Tier-1 prompts)

A design can total ≥75 and **still not be Tier 1** if either gate fails:

- **Security gate (Category 3):** score < 14/20 ⇒ **NOT production-ready**, regardless of total. Tools are authority boundaries; a system that skips ASI coverage for its blast radius is a prototype.
- **Evaluation gate (Category 4):** missing *either* an ABC-valid capability suite *or* a separate real-tool safety eval ⇒ "production-ready" is unprovable. Capability ≠ safety.

### Quality tiers

| Score | Tier | Status |
|-------|------|--------|
| 90–100 | Exemplary | Gold standard, reference material |
| 80–89 | Excellent | Production-ready, minor improvements possible |
| 75–79 | Good | Production-ready, meets standards |
| 65–74 | Acceptable | Functional; revise before relying on it |
| 50–64 | Needs work | Significant gaps |
| <50 | Incomplete | Not ready |

> **Override rule:** if either load-bearing gate fails, cap the reported tier at **"Needs work"** until fixed, even if the arithmetic says higher.

---

## Detailed Criteria

### 1. Agent justification & complexity-appropriateness (15 pts)

| Points | Criterion |
|--------|-----------|
| 6 | A written Step-0 justification exists and is honest (names *why* a deterministic workflow can't do it). |
| 5 | The chosen rung is the **lowest** that meets scope (no gratuitous multi-agent). |
| 4 | Cost implications acknowledged (≈4×/15× tokens) and accepted for stated value. |

**Auto-zero this category** if the design jumped to multi-agent without a breadth/parallelism justification, or if a function/prompt/workflow would obviously suffice.

### 2. Topology fit & primitive correctness (15 pts)

| Points | Criterion |
|--------|-----------|
| 6 | Topology matches the three selection variables (control / sequence-parallel-conversation / plan-known-vs-runtime). |
| 5 | Primitives correctly named and scoped (tools, state, memory, handoff, guardrail, HITL, tracing). |
| 4 | The agent loop is bounded with a defined cap-fallback; handoffs/loops can't run unbounded. |

### 3. Security gate coverage vs OWASP ASI (20 pts) — ✅ LOAD-BEARING

Score against the SAFE-01…SAFE-10 patterns, sized to the actual blast radius.

| Points | Criterion |
|--------|-----------|
| 4 | **Data/control separation** (SAFE-01) + **injection defense** (SAFE-05) present wherever untrusted content is read. |
| 4 | **Deterministic policy enforcement** (SAFE-02) — allowlists, schema/arg validation, pre-execution tool-call validation. |
| 3 | **Least-privilege tools** + **least-agency scoping** (SAFE-03/04); high-privilege ops re-verify intent. |
| 3 | **Governed identity** + no credential caching (SAFE-08). |
| 3 | **Circuit breakers / blast-radius caps** (SAFE-07) + a **kill switch** in code. |
| 2 | **HITL approval + confidence scoring** for high-risk actions, risk-adaptive (SAFE-09). |
| 1 | (Multi-agent) **inter-agent trust model** documented (SAFE-10); memory-poisoning defense if memory persists (SAFE-06). |

**Gate fail:** < 14/20.

### 4. Evaluation validity (ABC) + real-tool safety eval (20 pts) — ✅ LOAD-BEARING

| Points | Criterion |
|--------|-----------|
| 5 | **ABC task-validity** (EVAL-01): solvable iff capability present; versions pinned; agent isolated from ground truth; oracle solver. |
| 5 | **ABC outcome-validity** (EVAL-02): graders robust to equivalents/negation; no success-by-guessing; code → unit+fuzz+E2E; LLM-judge validated. |
| 6 | **Separate real-tool safety eval** (EVAL-03): the 8 OpenAgentSafety categories in real-tool environments, benign + adversarial, rule-based + LLM-judge. |
| 2 | **Dual process + outcome metrics** + **trivial-agent baseline** + cost reported (EVAL-04). |
| 2 | Started small (~20 realistic queries), held-out set, human spot-check. |

**Gate fail:** missing the ABC capability suite **or** the separate safety eval.

### 5. Durability / observability / cost design (10 pts)

| Points | Criterion |
|--------|-----------|
| 3 | Context strategy chosen per hop; compaction / notes / sub-agent isolation applied where relevant (CTX-01/02/03). |
| 3 | External state + checkpoint/resume for long-running work (CTX-04). |
| 2 | Observability designed: event/span schema, trajectory traces, dashboards, alerts. |
| 2 | Model right-sizing (cheap models for classify/extract/format); token budget noted. |

### 6. Documentation completeness (10 pts)

| Points | Criterion |
|--------|-----------|
| 4 | Three-layer docs (README + ARCHITECTURE + PIPELINE_OVERVIEW) if shipped as a system (SP-01). |
| 3 | Disclosure manifest covers all 6 AI Agent Index dimensions, incl. safety evals actually run. |
| 3 | Runbook: deployment/rollout (shadow/canary), rollback path, failure-mode catalog. |

### 7. Cross-link hygiene / no duplication / no-fabrication (10 pts)

| Points | Criterion |
|--------|-----------|
| 4 | References existing repo prompts instead of re-authoring them (DRY; reference-don't-move). |
| 3 | No fabricated data/sources/figures; unknowns flagged (`UNAVAILABLE` / "verify against current docs"). |
| 3 | Stack-specific code (if any) stays version-neutral inside the named stack; drifting facts flagged. |

---

## Quick Evaluation Checklist

```
[ ] Step-0 written justification present (Cat 1)
[ ] Lowest-complexity topology chosen (Cat 1/2)
[ ] Every loop bounded + cap-fallback (Cat 2)
[ ] Data/control separation + injection defense for untrusted content (Cat 3 — GATE)
[ ] Deterministic policy enforcement + pre-execution tool validation (Cat 3 — GATE)
[ ] Least privilege + governed identity + kill switch (Cat 3 — GATE)
[ ] HITL for high-risk actions (Cat 3 — GATE)
[ ] ABC-valid capability eval present (Cat 4 — GATE)
[ ] Separate real-tool safety eval present (Cat 4 — GATE)
[ ] Trivial-agent baseline + cost reported (Cat 4)
[ ] Context/durability/observability designed (Cat 5)
[ ] 3-layer docs + disclosure manifest + runbook (Cat 6)
[ ] Cross-links not duplications; no fabrication (Cat 7)
```

---

## Common Deductions

| Issue | Deduct | Category |
|-------|--------|----------|
| Multi-agent with no breadth/parallelism justification | −10 (often auto-zero) | 1 |
| Unbounded loop / no cap-fallback | −6 | 2 |
| Untrusted content read with no injection defense | gate fail | 3 |
| "The agent will check policy itself" (no deterministic enforcement) | gate fail | 3 |
| No kill switch | −3 + flag | 3 |
| Capability eval only, no safety eval | gate fail | 4 |
| Benchmark lets empty/guessed answers pass | −5 + flag invalid | 4 |
| Re-authored a prompt the repo already has | −4 | 7 |
| Asserted API/model/pricing facts from memory | −3 | 7 |

---

## Improvement Guide

- **Below 75 overall:** revise the lowest-scoring non-gate category first, but never ship with a failed gate.
- **Security gate failing:** walk SAFE-01…SAFE-10 against the blast-radius table in [SYSTEM_USE_CASE_LOOKUP.md](SYSTEM_USE_CASE_LOOKUP.md); pull `aiagent_agentic_threat_model` + `aiagent_runtime_guardrails_policy`.
- **Eval gate failing:** if only capability is covered, add the real-tool safety suite (EVAL-03); if the suite is weak, run it against a trivial agent — if the trivial agent scores >0, the benchmark is invalid.
- **Toward Exemplary (90+):** add population-level monitoring for fleets, durable-execution checkpointing, and a fully worked disclosure manifest.

---

**See it applied:** [templates/GOLD_STANDARD_AGENTIC_SYSTEM.md](templates/GOLD_STANDARD_AGENTIC_SYSTEM.md) is scored against this rubric at the end.
