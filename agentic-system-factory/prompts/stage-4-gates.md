---
title: "Stage 4 — Design the Gates (Gate A: code-not-trust)"
category: agentic-system-factory/stage-4-gates
description: "Design the security/HITL/loop-bound/kill-switch gates, sized to the blast radius from Stage 1, and enforced in code/config — never 'the agent will remember.' The OWASP-ASI security gate (Gate A) is to this system what False-Positive Prevention is to a Tier-1 prompt: the load-bearing differentiator. Fills GATE_DESIGN.md and emits the Gate-A markers."
techniques:
  - ST-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - gate-a
  - owasp-asi
  - hitl
  - kill-switch
  - code-not-trust
updated: "2026-07-02"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_hard_gates_designer.md
  - domain-AI-ML/agentic-ai-systems/aiagent_prompt_injection_untrusted_content_defense.md
  - domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md
---

# Stage 4 — Design the Gates (Gate A)

## Objective
Design four gate layers sized to the blast radius, enforced in code/config, and record them in `GATE_DESIGN.md`. Emit the Gate-A markers.

## When to Use
- After Stage 3 architecture, before the eval harness.

## Inputs / Context
- Blast radius (`ARCHITECTURE.md §1`), tools and their permissions (`tools/*`), agents and authority boundaries (`agents/*`).

## Constraints

**Must:**
- Enforce every gate in **code/config**, never as an instruction the LLM is trusted to follow.
- Satisfy the OWASP-ASI minimum for the actual blast radius — at minimum **data/control separation (SAFE-01)** and **deterministic policy enforcement (SAFE-02)** are non-waivable.
- Provide **defense-in-depth (3 layers)** wherever untrusted content is processed: input detection + model instruction hierarchy + deterministic policy enforcement (the only layer that blocks prohibited actions regardless of LLM output).
- Bound **every** loop with a defined cap-fallback (not a silent stop).
- Include an explicit **kill switch** in code.

**Must Not:**
- Mark SAFE-01 or SAFE-02 as `na`.
- Rely on confirmation-on-every-action (confirmation fatigue defeats the gate) — use risk-adaptive authorization.
- Treat a read-only blast radius as exempt from the injection / data-control gate when inputs are untrusted.

## Instructions
1. **Gate 0** — paste the written justification from `ARCHITECTURE.md §2`.
2. **Gate A (security)** — fill the SAFE table in `GATE_DESIGN.md`, marking each pattern Enforced (how/where) · N/A (justified) · TODO. Confirm the three defense-in-depth layers where untrusted content flows.
3. **HITL approval gates** — map action classes → risk → gate → approver → confidence threshold, using risk-adaptive authorization.
4. **Loop bounds + cap-fallbacks** — bound the main loop, evaluator iterations, handoff chain length, sub-agent spawn count; define what happens at each cap.
5. **Kill switch** — mechanism (e.g., a `halt` config flag checked before every action), scope when active, who can trip it, and how it's tested.
6. **Emit the Gate-A markers** with the exact machine-checked values — `SAFE-01: enforced`, `SAFE-02: enforced`, `SAFE-04: enforced` (or `na: <reason>`), `DEFENSE-IN-DEPTH: 3-layers`, `KILL-SWITCH: present` — per [`../templates/BUNDLE_MANIFEST_TEMPLATE.md`](../templates/BUNDLE_MANIFEST_TEMPLATE.md). Values are exact strings (`yes` / `Enforced` fail); markers must be live text outside any code fence; never leave two same-name markers with different values (the gate fails closed). Note these five are the only *machine-checked* rows — the full SAFE table (SAFE-03/05/06/07/08/10 + RCE) must still be filled; the orchestrator critique enforces those.

## Output Format
Fill `GATE_DESIGN.md` (Gate A + HITL + loop bounds + kill switch) with markers set.

## Verification Checklist
- [ ] SAFE-01 and SAFE-02 are `enforced` (not `na`); SAFE-04 enforced or justified-na.
- [ ] Defense-in-depth has all three layers on untrusted-content paths.
- [ ] Every loop is bounded with a defined cap-fallback.
- [ ] A kill switch exists in code with a stated test.
- [ ] Every SAFE row in the table is filled (not just the five machine-checked ones).
- [ ] `python3 scripts/check_gate.py --gate A <bundle>` (run from the factory root) returns PASS.

## False-Positive Prevention
- **Marker-stuffing is the failure mode the script cannot see:** `SAFE-01: enforced` with no named enforcement point in the table is a false Gate-A pass. Every `enforced` must point at *where in code/config* the rule is applied — the script checks the marker; the orchestrator critique checks the substance.
- Only 5 rows are machine-checked (SAFE-01/02/04 + DEFENSE-IN-DEPTH + KILL-SWITCH). Filling only those and leaving SAFE-03/05/06/07/08/10 blank passes the script but is not a passing Gate-A design — the critique must reject it.

## References (assembled, not duplicated)
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_hard_gates_designer.md` — composes A/B/C + kill switch.
- `domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md`; `aiagent_runtime_guardrails_policy.md`; `aiagent_prompt_injection_untrusted_content_defense.md`; `aiagent_agentic_threat_model.md`; `aiagent_least_agency_scoping.md`; `aiagent_zero_trust_maturity_assessment.md`.

## Produces
`GATE_DESIGN.md` + Gate-A markers → **Gate A**.
