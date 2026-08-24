# PLAN (not a prompt): Pre-Production Stress-Test Orchestrator

> **Status:** Planned / deferred. This is an implementation plan, **not** a runnable prompt.
> The leading underscore + this banner keep it out of prompt-index generation and curator scans.
> Delete or convert this file when the orchestrator is authored.

**Source:** `PromptKit_Stress_Testing_Prompts_Before_Production.pdf` (5-step framework), assessed 2026-07-03.
**Sibling prompts already built from the same source:**
- `stresstest_config_sweep_harness.md` (Step 4 — runtime-config sweep)
- `regression/regression_release_gate_scorecard.md` (Step 5 — analyse & gate)

---

## 1. What this would be

A single top-level orchestrator prompt — "**stress-test this prompt before it ships**" — that sequences the five pre-production steps into one CI-integrated workflow, delegating each step to the prompt the repo already has. It is a *convenience/entry-point* asset, not net-new methodology: every step already exists as a standalone prompt. Value is in the sequencing, the hard gates between steps, and a single command a team can point at a prompt-about-to-ship.

Model it on the repo's existing multi-stage orchestrators (`domain-idea-to-product/orchestrator_idea_to_product.md`, `childrens-book-studio/orchestrator_childrens_book.md`, `agentic-system-factory/orchestrator_agentic_system.md`): guided / manual / surgical modes, gate enforcement via orchestrator critique, ≤3 recommended next prompts per step.

## 2. Step → existing-prompt wiring

| PDF step | Delegates to |
|----------|--------------|
| 1. Define success/failure | `correctness_discovery_prompt.md` → `correctness_vague_requirements_translator.md` → `correctness_tradeoff_forcer.md` |
| 2. Build challenge dataset | `eval-datasets/dataset_case_inventory_from_logs.md` + `adversarial/adv_edge_case_generator.md` (+ other `adversarial/` probes) |
| 3. Automate the harness | `correctness_eval_design_prompt.md` (team scale) or `skill-development/promptcraft_eval_harness.md` (personal scale) |
| 4. Run stress scenarios | `stresstest_config_sweep_harness.md` (config axis) + `adversarial/` (input axis) |
| 5. Analyse & gate releases | `regression/regression_release_gate_scorecard.md` + `regression/regression_golden_set_curator.md`; hand drift to `correctness_production_monitoring_setup.md` |
| Checklist / feedback loop | `regression_golden_set_curator.md` + `correctness_pre_mortem.md`; pipe incidents back into Step 2 |

## 3. Hard gates to enforce (orchestrator critique, not scripts)

- **Gate 1→2:** a correctness spec exists (consumer, must-haves, must-nots, refusal conditions, ≥1 resolved tradeoff). No spec → cannot proceed; the eval would score against drifting intuition.
- **Gate 2→3:** challenge set covers every declared intent + known incident cases; ≥85% real inputs (synthetic labeled).
- **Gate 3→4:** harness is reproducible (pinned prompt, model+version, committed thresholds) and baseline established.
- **Gate 4→5:** both stress axes run — config sweep (Step 4 sibling) **and** adversarial inputs — with budgets attached.
- **Gate before ship:** release-gate scorecard returns PASS (or logged SOFT-FAIL override); no HARD-FAIL bypass.
- **Feedback loop (not a gate):** each production incident becomes a Step-2 case. Make this an explicit output, since it is the checklist item teams most often skip.

## 4. Authoring specifics

- **Location:** `domain-prompt-engineering/evaluation/stresstest_preproduction_orchestrator.md`.
- **Frontmatter techniques:** ST-02 (sequential), DT-01 (task decomposition), NE-02 (dialogue-based phases — orchestrators interview), CM-02 (constraints/gates), OC-06 (output contract), QA-01 (verification). Confirm each against `techniques/MASTER_TECHNIQUE_INDEX.md` at authoring time.
- **Modes:** guided (interview → classify entry step → recommend ≤3 prompts → critique each output against that step's verification block → enforce the gate) / manual (walk the table above) / surgical (jump to one step).
- **Do NOT duplicate** any delegated prompt's content — reference in place, mirroring how `domain-idea-to-product` and `childrens-book-studio` cite upstream prompts rather than copying them.
- **Difficulty:** advanced. **Audience:** prompt/ML/platform engineers shipping an AI feature into CI.

## 5. Ship checklist when implemented

- [ ] Author `stresstest_preproduction_orchestrator.md` per §4.
- [ ] Add the three stress-test prompts (2 built + this orchestrator) to `PROMPT_INDEX.json` and `PROMPT_INDEX.md`.
- [ ] Add a "Stress-testing prompts before production" row group to `domain-prompt-engineering/evaluation/README.md`.
- [ ] Add a CLAUDE.md Quick-Reference row: "Stress-test a prompt before production" → orchestrator.
- [ ] Leave a back-pointer in the source PDF's companion notes (or a NOTES file) recording what was ingested.
- [ ] Delete this `_PLANNED_` file.

## 6. Decision

Optional. The two built prompts close the only *net-new methodology* gaps. This orchestrator is pure convenience — build it if/when a team wants one-command pre-production hardening; skip it otherwise with no loss of coverage.
