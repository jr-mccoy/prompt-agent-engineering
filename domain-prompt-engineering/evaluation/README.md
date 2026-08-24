# Prompt Engineering — Evaluation

**Purpose:** Meta-prompts for evaluating AI output correctness, specification quality, task-difficulty profiling, taste calibration, and adversarial robustness testing.

This folder spans three flat-file groups and four nested subdirectories:

1. **Correctness & evaluation of AI output.** Discovering what "correct" means for a task, translating vague requirements into specs, designing evaluation harnesses at production scale, running pre-mortems, and monitoring outputs for drift.
2. **AI task difficulty.** Profiling tasks across orthogonal axes to decide whether they're AI-shaped, optimizing workflows based on which axes drag hardest, and building calibrated intuition for output quality.
3. **Pre-production stress-testing.** Sweeping runtime configuration (temperature, model version, context length, concurrency) over a fixed challenge set to surface config-sensitivity, latency cliffs, and token-cost spikes before shipping.
4. **Adversarial evaluation.** Red-team test sets, prompt injection probes, persona attacks, data exfiltration attempts, and refusal bypass ladders.
5. **Regression testing.** Golden sets, canary runners, change impact estimation, A/B experiment design, and release-gate scorecards for prompt changes.
6. **Rubric design.** Calibrated score anchors, pairwise vs. pointwise mode selection, inter-rater agreement protocols, and LLM judge design.
7. **Dataset curation.** Production log mining, synthetic generation, difficulty stratification, and holdout split design.

---

## Flat Files (existing)

### Correctness & Evaluation

| File | What it does |
|------|--------------|
| `correctness_discovery_prompt.md` | Convert a fuzzy request into an operational correctness definition — consumer, must-haves, must-nots, refusal conditions, resolved tradeoffs — grounded in real accepted and rejected outputs |
| `correctness_tradeoff_forcer.md` | Surface quality-dimension tensions, screen real vs. apparent, force a dominance + tiebreaker per top tension, evidenced against real outputs |
| `correctness_vague_requirements_translator.md` | Translate a vague quality adjective ("more professional," "more rigorous") into 2–5 observable behaviors with pass/fail rules and real-output anchors |
| `correctness_prompt_specification_audit.md` | Audit an existing prompt against a 10-slot coverage checklist using real past outputs as evidence; returns ranked gaps + diff-sized edits |
| `correctness_pre_mortem.md` | Walk backward from plausible three-month-out failure headlines through a root-cause ladder (output → spec gap → detection gap → recovery gap) to a pre-ship checklist with hard gates |
| `correctness_eval_design_prompt.md` | Design a team/production-scale eval set: 40–150 real cases by category, rubric derived from spec, blinded scoring protocol, thresholds committed in advance, owned and dated |
| `correctness_production_monitoring_setup.md` | Monitor a live AI system for drift across five drift types (input / model / output / consumer / spec), with signals tied to actual telemetry, measured noise bands, and a named response playbook |
| `prompt_lifecycle_assessment.md` | Assess a prompt across its lifecycle; identify maintenance triggers |
| `repository_review_reflection.md` | Reflective review of prompt-repo state |

### AI Task Difficulty

| File | What it does |
|------|--------------|
| `taskdifficulty_decompose_by_axes.md` | Score a candidate task across 8 orthogonal AI-difficulty axes (spec, context, tools, reversibility, stakes, verification cost, ambiguity, horizon); returns proceed / proceed-with-changes / not-yet-AI-shaped |
| `taskdifficulty_workflow_axis_optimizer.md` | Redesign a multi-step workflow based on which step-axis pairs drag hardest; uses six canonical redesign moves |
| `taskdifficulty_calibrated_comparison.md` | Build personal "taste" for AI output quality via blind-scored comparison of spec scores vs. intuition scores, with diagnosis of spec gaps vs. intuition gaps |

### Pre-Production Stress-Testing

| File | What it does |
|------|--------------|
| `stresstest_config_sweep_harness.md` | Sweep runtime config (temperature × model/version × context length × concurrency) over a fixed challenge set; surface config-sensitivity, latency cliffs, and token-cost spikes; output a recommended production config envelope. Orthogonal complement to input-varying evals |

> A planned 5-step pre-production orchestrator (sequencing define → dataset → harness → sweep → gate) is scoped in `_PLANNED_stresstest_orchestrator.md` — a deferred plan, not yet a prompt.

---

## Nested Subdirectories (new)

### adversarial/ — 6 prompts

Red-team test sets, injection probes, persona attacks, and bypass ladders.

| File | What it does |
|------|--------------|
| `adversarial/adv_jailbreak_corpus_builder.md` | Assemble a categorized jailbreak corpus — taxonomy, severity, attack vector, reproduction phrasing |
| `adversarial/adv_prompt_injection_test_set.md` | Direct and indirect injection cases for tool agents, RAG, and multi-turn systems |
| `adversarial/adv_edge_case_generator.md` | Edge inputs from a task spec across boundary, malformed, and hostile axes |
| `adversarial/adv_persona_attack_battery.md` | Graded battery of identity-override attempts ordered by bypass sophistication |
| `adversarial/adv_data_exfil_probe.md` | Probes targeting system prompt content and user data via 6 extraction strategies |
| `adversarial/adv_refusal_bypass_audit.md` | Graded bypass ladder for a specific refusal policy — robust or brittle verdict |

### regression/ — 5 prompts

Regression infrastructure for detecting what prompt changes break.

| File | What it does |
|------|--------------|
| `regression/regression_golden_set_curator.md` | Versioned golden test set with provenance, freeze protocol, and update criteria |
| `regression/regression_change_impact_estimator.md` | Predict which cases a prompt diff affects before running them |
| `regression/regression_ab_test_runner_prompt.md` | A/B experiment design with hypothesis, sample size, blinding, and pre-committed decision rule |
| `regression/regression_canary_set_designer.md` | 5–15-case canary set that runs in <60 seconds to catch major regressions early |
| `regression/regression_release_gate_scorecard.md` | Compare a candidate run against a frozen baseline with noise-floor deltas, per-metric traffic lights, a PASS/SOFT-FAIL/HARD-FAIL roll-up, and a PR-ready scorecard comment |

### rubrics/ — 4 prompts

Rubric design, calibration, agreement measurement, and LLM judge design.

| File | What it does |
|------|--------------|
| `rubrics/rubric_calibrated_anchors.md` | Concrete output examples anchoring each score point (1–5) with boundary rules |
| `rubrics/rubric_pairwise_vs_pointwise.md` | Decision framework and design for pairwise vs. pointwise scoring mode |
| `rubrics/rubric_inter_rater_agreement_protocol.md` | Kappa-based agreement measurement, disagreement diagnosis, and calibration sessions |
| `rubrics/rubric_llm_judge_designer.md` | LLM-as-judge system prompt with CoT, inline rubric, bias controls, and verification |

### eval-datasets/ — 4 prompts

Dataset curation, synthesis, stratification, and holdout splits.

| File | What it does |
|------|--------------|
| `eval-datasets/dataset_case_inventory_from_logs.md` | Mine production logs into a labeled, deduplicated, anonymized test set |
| `eval-datasets/dataset_synthetic_case_generator.md` | Generate synthetic cases with axis-based coverage and quality validation |
| `eval-datasets/dataset_difficulty_stratifier.md` | Score and balance cases across easy/medium/hard difficulty tiers |
| `eval-datasets/dataset_holdout_split_designer.md` | Leakage-free train/dev/test splits with stratification and lockdown protocol |

---

## How the Prompts Fit Together

**For a new AI-delegation decision:**
1. `taskdifficulty_decompose_by_axes.md` — is this task AI-shaped?
2. If ambiguity of correctness ≥2: `correctness_discovery_prompt.md` + `correctness_vague_requirements_translator.md`
3. If reversibility + stakes are both ≥2: `correctness_pre_mortem.md` before running

**For an existing AI-assisted workflow:**
1. `taskdifficulty_workflow_axis_optimizer.md` — where is the drag?
2. `correctness_prompt_specification_audit.md` — audit the prompt for spec gaps
3. `correctness_eval_design_prompt.md` — measure at production scale
4. `correctness_production_monitoring_setup.md` — catch drift over time
5. `taskdifficulty_calibrated_comparison.md` — keep judgment calibrated

**For building evaluation infrastructure:**
1. `eval-datasets/dataset_case_inventory_from_logs.md` or `dataset_synthetic_case_generator.md` — build dataset
2. `eval-datasets/dataset_difficulty_stratifier.md` — balance difficulty
3. `rubrics/rubric_calibrated_anchors.md` → `rubric_pairwise_vs_pointwise.md` → `rubric_llm_judge_designer.md` — design scorer
4. `regression/regression_golden_set_curator.md` — freeze the stable reference set
5. `regression/regression_canary_set_designer.md` — set up CI gate

**For pre-production stress-testing (before a prompt/model ships):**
1. `correctness_eval_design_prompt.md` — build the fixed challenge set + rubric
2. `stresstest_config_sweep_harness.md` — sweep temperature / model / context / load; find the safe config envelope
3. `adversarial/*` — run the input-varying axis alongside the config axis
4. `regression/regression_release_gate_scorecard.md` — judge candidate vs. frozen baseline and gate the merge
5. `correctness_production_monitoring_setup.md` — wire near-cliff configs into live monitoring

**For adversarial hardening:**
1. `adversarial/adv_jailbreak_corpus_builder.md` — broad coverage
2. `adversarial/adv_persona_attack_battery.md` — persona durability
3. `adversarial/adv_data_exfil_probe.md` — extraction resistance
4. `adversarial/adv_refusal_bypass_audit.md` — per-policy hardness

---

## When to Use This Folder vs. Adjacent Folders

- **evaluation/** — measuring or profiling AI output correctness, robustness, and task fit
- **skill-development/** — building the user's durable ability to evaluate and produce correct outputs
- **prompt-improvement/** — rewriting an existing prompt to be better
- **goal-orientation/** — pre-flight on whether the right problem is being solved
