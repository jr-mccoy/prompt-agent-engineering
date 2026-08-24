---
title: "Stage 5 — Design the Eval Harness (Gate B: two independent gates)"
category: agentic-system-factory/stage-5-eval
description: "Design two independent gates — capability (ABC-valid acceptance suite) and safety (OpenAgentSafety real-tool eval, separate from capability). A system can be capable and unsafe; frontier models show 51–73% unsafe-action rates on safety-vulnerable tasks. Fills EVAL_HARNESS.md and emits both Gate-B markers; missing either is a Gate B failure."
techniques:
  - ST-02
  - QA-01
  - QA-04
difficulty: advanced
tags:
  - gate-b
  - abc-validity
  - openagentsafety
  - capability-vs-safety
updated: "2026-07-02"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_agentic_safety_eval_layer.md
  - domain-AI-ML/agentic-ai-systems/aiagent_evaluation_design.md
  - domain-engineering-workflows/done-definition/done_definition_verification_hardening.md
---

# Stage 5 — Design the Eval Harness (Gate B)

## Objective
Design a capability eval (ABC-valid) **and** a separate real-tool safety eval, record both in `EVAL_HARNESS.md`, and emit both Gate-B markers. An invalid benchmark is worse than none — it manufactures false confidence.

## When to Use
- After Stage 4 gates, before assembly.
- Surgically via `/agent-eval` when you only need the eval harness.

## Inputs / Context
- Success criteria (`ARCHITECTURE.md §1`), the system's real risk surface (from the blast radius + untrusted-content seams), agents/tools.

## Constraints

**Must:**
- Build **both** gates: capability (ABC-valid) and a **separate** safety gate. Missing either ⇒ Gate B FAIL.
- For capability: ensure task validity (solvable iff the agent has the target capability; versions pinned; agent isolated from ground truth; oracle solver), outcome validity (graders robust to semantic equivalents/negation; no success-by-guessing), and reporting with a **trivial-agent baseline** (an empty-response agent must score ~0).
- For safety: evaluate in **real-tool environments** across the **8 OpenAgentSafety categories**; detection = rule-based final-state checks **+ LLM-as-judge**; run benign + adversarial, multi-turn.
- Aim the safety eval at the system's **actual** risk surface, not generic checks.

**Must Not:**
- Waive the safety gate because capability is high.
- Ship a benchmark where an empty/trivial agent scores >0 (the grader is broken).
- Treat stubbed tools as a real-tool safety eval.

## Instructions
1. **Capability suite (Gate B-capability)** — ~20 realistic held-out tasks; task-validity checklist; outcome-validity graders by category; reporting with trivial-agent baseline + dual process/outcome metrics + cost.
2. **Safety suite (Gate B-safety)** — scenarios covering the 8 categories (computer-security compromise, data loss/corruption, privacy breach, unsafe code execution, financial loss, spreading malicious content, legal violations, harmful decision-making); rule-based + LLM-judge detection; adversarial/injection cases on every external-content path.
3. **Sign-off** — capability PASS/FAIL + score; safety PASS/FAIL + worst-category rate. "Production-ready" requires **both**.
4. **Emit both Gate-B markers** (`GATE-B-CAPABILITY: present`, `GATE-B-SAFETY: present`) per [`../templates/BUNDLE_MANIFEST_TEMPLATE.md`](../templates/BUNDLE_MANIFEST_TEMPLATE.md).

## Output Format
Fill `EVAL_HARNESS.md` (both gates) with both markers set.

## Verification Checklist
- [ ] Capability suite is ABC-valid (task validity + outcome validity + trivial-agent baseline).
- [ ] Safety suite covers the 8 categories in real-tool environments with rule + LLM-judge detection.
- [ ] Safety eval targets the actual risk surface; adversarial cases on untrusted-content paths.
- [ ] Both Gate-B markers present.
- [ ] `python3 scripts/check_gate.py --gate B <bundle>` (run from the factory root) returns PASS.

## False-Positive Prevention
- A grader that scores a trivial/empty-response agent above ~0 manufactures a **false Gate-B pass** — the benchmark, not the agent, is broken. Run the trivial-agent baseline before trusting any score.
- Emitting `GATE-B-SAFETY: present` for a stubbed-tool or not-yet-built suite is marker-stuffing: the script checks marker presence, not that the suite exists and ran in real-tool environments. The orchestrator critique must see the 8-category scenario table actually filled before the marker counts.

## References (assembled, not duplicated)
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_agentic_safety_eval_layer.md` — the ABC + OpenAgentSafety layer.
- `domain-AI-ML/agentic-ai-systems/aiagent_evaluation_design.md`; ⭐ `domain-engineering-workflows/done-definition/done_definition_verification_hardening.md`; `domain-AI-ML/model-evaluation-validation/` (general substrate).

## Produces
`EVAL_HARNESS.md` + both Gate-B markers → **Gate B** (the marker the deliberately-incomplete `samples/bundle-fail/` omits).
