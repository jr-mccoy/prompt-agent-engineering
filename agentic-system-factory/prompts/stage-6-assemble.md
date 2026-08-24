---
title: "Stage 6 — Assemble, Validate, Document (Gate C)"
category: agentic-system-factory/stage-6-assemble
description: "Emit the framework-agnostic terminal bundle (system design, agent/tool specs, gate spec, eval harness, observability plan, disclosure manifest, runbook, optional rules file), complete the disclosure manifest's six dimensions, score against the 100-pt rubric (≥75, with load-bearing minimums), and pass Gate C. This is the always-produced source-of-truth output; Stage 7 code-gen is a transform of it."
techniques:
  - ST-02
  - ST-03
  - QA-01
difficulty: advanced
tags:
  - gate-c
  - disclosure-manifest
  - rubric-scoring
  - terminal-bundle
updated: "2026-07-02"
related_prompts:
  - domain-engineering-workflows/done-definition/done_definition_loop_operator.md
  - domain-AI-ML/responsible-ai-governance/rai_documentation_suite_orchestrator.md
  - authoring/system-patterns/SYSTEM_QUALITY_RUBRIC.md
---

# Stage 6 — Assemble, Validate, Document (Gate C)

## Objective
Produce the complete agnostic design bundle, complete the disclosure manifest (all six dimensions), score it (≥75 with load-bearing minimums), and pass Gate C. The bundle is the source of truth; any later code-gen is a transform of it.

## When to Use
- After Gate A (Stage 4) and Gate B (Stage 5) both pass.

## Inputs / Context
- All prior artifacts: `ARCHITECTURE.md`, `agents/*`, `tools/*`, `GATE_DESIGN.md`, `EVAL_HARNESS.md`.

## Constraints

**Must:**
- Emit all required bundle artifacts (see [`../templates/BUNDLE_MANIFEST_TEMPLATE.md`](../templates/BUNDLE_MANIFEST_TEMPLATE.md) §1): `OBSERVABILITY.md`, `DISCLOSURE_MANIFEST.md`, `RUNBOOK.md`, `BUNDLE_MANIFEST.md`, `RUBRIC_SCORE.md`.
- Complete **all six** disclosure dimensions — especially #6 (Safety, Evaluation & Impact), the most-skipped — reporting evals **actually run**, not aspirational.
- Provide a **rollback path** for every state-modifying action in the runbook.
- Score against the rubric; total **≥75** AND `cat3_security ≥ 14` AND Gate B passing. A design that fails a load-bearing gate is not Tier 1 regardless of total.

**Must Not:**
- Mark the bundle deployable with a blank safety dimension or no rollback path.
- Fabricate eval results; report what was actually run.

## Instructions
1. **Observability plan** (`OBSERVABILITY.md`) — event/span schema, trajectory traces, dashboards, alerts.
2. **Disclosure manifest** (`DISCLOSURE_MANIFEST.md`) — fill all six AI Agent Index dimensions; emit `DISCLOSURE-DIM-1..6: complete` markers.
3. **Runbook** (`RUNBOOK.md`) — deployment/rollout (shadow/canary), rollback path (emit `ROLLBACK: present`), failure-mode catalog.
4. **Rules file** (optional `CLAUDE.md`/`AGENTS.md`) — if a coding agent will build the system.
5. **Bundle index** (`BUNDLE_MANIFEST.md`) — fill the artifact table + gate status + stack-selection.
6. **Score** (`RUBRIC_SCORE.md`) — fill the seven-category `<!-- RUBRIC ... -->` block.
7. **Validate** — run `validate_bundle.py`, `check_gate.py --gate {0,A,B,C}`, `score_rubric.py`; all must PASS.

## Output Format
The complete bundle directory + the rubric block. The orchestrator runs the scripts and refuses to mark the bundle production-ready on any nonzero exit.

## Verification Checklist
- [ ] All required artifacts present (`validate_bundle.py` PASS).
- [ ] Six disclosure dimensions complete; #6 reports evals actually run.
- [ ] Rollback path present for every state-modifying action.
- [ ] Rubric ≥75, `cat3_security ≥14`, Gate B passing.
- [ ] `python3 scripts/check_gate.py --gate C <bundle>` and `python3 scripts/score_rubric.py <bundle>` (run from the factory root) both PASS.

## False-Positive Prevention
- Disclosure dimension 6 filled with *planned* evals reads as complete to the script — a false Gate-C pass. Only evals actually run belong there; if a suite hasn't run, the dimension says so and Gate C waits.
- The rubric is **self-scored**: the script enforces the caps and load-bearing minimums, not the truth of the numbers. A category score that can't be traced to a bundle artifact is inflation — the orchestrator critique must be able to point at the evidence behind each score before "production-ready" is declared.

## References (assembled, not duplicated)
- ⭐ `domain-engineering-workflows/done-definition/done_definition_loop_operator.md` — the run loop; `done_definition_stop_policy.md`.
- `domain-AI-ML/agentic-ai-systems/aiagent_observability_telemetry_design.md`; `aiagent_durable_execution_state_persistence.md`; `aiagent_deployment_serving_architecture.md`.
- `domain-AI-ML/production-monitoring/` runbooks; ⭐ `domain-AI-ML/responsible-ai-governance/rai_documentation_suite_orchestrator.md` (disclosure).

## Produces
The complete agnostic bundle + `DISCLOSURE_MANIFEST.md` + `RUBRIC_SCORE.md` → **Gate C**. Stage 7 unlocks only after Gate C passes **and** a stack is committed.
