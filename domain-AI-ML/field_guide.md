# domain-AI-ML — Field Guide

How to author and evaluate prompts in this domain. Read this before adding a prompt.

## What makes an AI/ML prompt Tier-1 here

Beyond the repo-wide Tier-1 bar (clear objective, structured instructions, locked output format, verification, realistic example, technique citations), AI/ML prompts must carry a **domain-specific False-Positive Prevention block**. Generic "be careful" warnings do not count. The block must name the actual ways ML reasoning goes wrong for *that* task.

## The ML failure-mode catalog (source material for FPP blocks)

Use these to write the ❌ DON'T / ✅ DO pairs. Pick the ones that bite for the specific task.

- **Leakage masquerading as skill** — high offline metrics from target/temporal/train-test leakage. ✅ Rule out leakage before trusting any strong result.
- **Bias claims without slice evidence** — calling a model "fair" or "biased" from aggregate numbers. ✅ Require per-group/intersectional slices and a stated fairness definition.
- **Drift claims without a baseline** — declaring drift from a single window. ✅ Require a reference window and a significance/magnitude threshold.
- **Correlation ↔ causation slippage** — feature importance read as causal levers. ✅ Separate predictive from causal claims.
- **Accuracy on imbalanced data** — ✅ demand class-specific metrics and a majority-class baseline.
- **No baseline** — improvement claimed against nothing. ✅ Always compare to random / majority / simple heuristic / prior model.
- **Point estimates without intervals** — ✅ require CIs / significance tests for comparisons.
- **Benchmark/SOTA fabrication** — inventing numbers from memory. ✅ Reason from the user's data; mark unknowns as unknown.
- **Overfitting to the validation set** — repeated tuning against the same holdout. ✅ reserve a true golden set; use nested CV for HPO.
- **Calibration ignored** — using probabilities that aren't calibrated. ✅ check ECE/reliability when probabilities are consumed downstream.
- **Train/serve skew** — features computed differently offline vs online. ✅ verify the same code path / timing.
- **GenAI: ungrounded eval** — LLM-as-judge without a rubric or human anchor. ✅ rubric + spot human calibration + adversarial cases.
- **Agentic: success-rate without cost/safety** — ✅ pair task success with token cost, latency, and failure-mode analysis.

### Vertical-specific failure modes (Wave 3 deeper verticals)

- **Temporal / future-edge leakage** (video, sequential recsys, time-series, graph link-prediction/fraud) — frames from one clip, future interactions, look-ahead features, or test edges visible in the message-passing graph. ✅ Split by the unit that carries leakage (clip, session-time, rolling origin, temporal/inductive graph split) and never on random rows.
- **Aggregate-metric masking** (multilingual, hierarchical forecasting, structured extraction, fraud) — a strong average hiding catastrophic per-language / per-level / per-field / operating-point performance. ✅ Report the disaggregated cut (per-language, per-node, per-field precision/recall, precision@k at review capacity), not just the headline.
- **Interval miscalibration / point-estimate overconfidence** (probabilistic & intermittent forecasting, offline RL OPE) — a nominal 90% interval that covers far less, or a point forecast treated as certainty. ✅ Validate coverage with proper scoring (pinball/CRPS) and report calibration, not just interval width.
- **Reward / objective over-optimization (Goodhart)** (RLHF/RLAIF, multi-objective ranking, bandits) — gaming a proxy reward model or lifting one objective while silently degrading another. ✅ Add guardrail metrics, a KL/anchor penalty, and propensity-corrected off-policy evaluation before trusting a win.

### Cross-cutting & governance failure modes (Wave 4)

- **Regulatory-text / threshold fabrication** (NIST RMF, FDA SaMD, ECOA, GDPR, SR 11-7, EU AI Act) — inventing article/section numbers, statutory text, numeric thresholds, fine amounts, deadlines, or case citations from memory. ✅ Map the system to the framework's *structure* and obligations; have the user confirm classification + version; flag every specific legal fact "verify against the current official source." Not legal advice.
- **Governance / compliance theater** (governance frameworks, risk registers, doc suites, RMF assessments) — a documented control, a "mitigated" risk, or a green checklist with no evidence the control actually reduces residual risk. ✅ Require evidence per control/risk; score *residual* risk after the control, not the existence of the control.
- **Fabricated cost / energy / carbon figures** (cost attribution, budgeting, carbon accounting) — asserting kWh, $/prediction, emissions, PUE, or grid-intensity numbers from memory, or treating chip TDP as measured energy. ✅ Use measured inputs and stated assumptions only; mark unknowns "measure on your data"; never present location- vs market-based Scope 2 cherry-picking as the real number.
- **Documentation drift** (model cards, datasheets, risk registers, doc-suite freshness) — the same fact (a metric, data composition, intended use) stated differently across documents, or a card whose numbers no longer match the deployed model. ✅ Single source of truth, cross-references, and a freshness verdict (current / stale / unverifiable) against live behavior — never assume "still current."
- **Postmortem hindsight & single-root-cause bias** (incident postmortems, runbook libraries) — blaming an individual, declaring one root cause, or judging decisions by what was knowable only in hindsight. ✅ Blameless systems/process root cause, multiple contributing factors, an evidence-reconstructed timeline (gaps marked "unknown / needs investigation"), and judging decisions by what was detectable at the time.

## Authoring conventions

- **Frontmatter (8 fields):** `title`, `category: AI-ML/<subdir>`, `description`, `techniques` (3–5 valid IDs from `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty` (beginner/intermediate/advanced), `tags` (3–6), `updated` (ISO date), `related_prompts` (real paths).
- **Section order:** `# Title` → **Objective** → **When to Use** (incl. when not to) → **Inputs/Context** → **Constraints (Must / Must Not)** → **Instructions** (numbered) → **Output Format** → **Verification** (checklist) → **False-Positive Prevention** (❌/✅) → **Example Output** (realistic, domain-appropriate) → **Techniques Used** → **Related Prompts**.

- **Heading syntax is canonical, not incidental.** Exactly **five** of those sections are `##` headings; the rest are **bold labels**. All 326 prompts follow this, and a check that assumes otherwise will misreport the whole domain.

  | `##` heading | Bold label `**X:**` |
  |---|---|
  | `## Inputs / Context` | `**Objective:**` |
  | `## Constraints` | `**When to Use:**` |
  | `## Verification` | `**When NOT to Use:**` |
  | `## False-Positive Prevention` | `**Instructions:**` |
  | `## Example Output` | `**Output Format:**` |
  | | `**Techniques Used:**` |
  | | `**Related Prompts:**` |

  `**Instructions:**` and `**Output Format:**` sit *inside* `## Constraints`. Inside `## Example Output`, the example's own title is a single `##` and any sub-blocks are `###`, so they do not collide with the prompt's heading level.

  A repo-wide grep for `^## When to Use` reports 0/326 here and 1,321 elsewhere; that is a style split across the repository, not a defect in this domain. Any CI check on section presence must match bold labels as well as headings.

- **Example Output is judged by density, not length** — one coherent scenario carried through every section of the stated Output Format, with later sections referencing earlier ones. See the *Density, not length* criterion in `PROMPT_QUALITY_STANDARDS.md`. Prefer `[measure]` / `[verify]` markers over invented numbers.
- **No-fabrication clause** belongs in Constraints/Must-Not for any prompt that could otherwise invent numbers.
- **Framework neutrality:** ask the user for framework + version; don't hardcode drifting APIs in instructions (examples may show code, clearly framed as illustrative).
- **File naming:** `{prefix}_{function}.md`; prefixes per subdirectory (see README).

## Commonly used technique IDs in this domain

| ID | Name | Typical AI/ML use |
|---|---|---|
| ST-01 | Clear Objective Statement | every prompt |
| ST-02 | Structured Sequential Instructions | pipelines, audits, debugging flows |
| ST-03 | Output Format Specification | reports, model cards, decision matrices |
| RT-02 | Multi-Dimensional Analysis Framework | tradeoff/selection prompts |
| RT-05 | Evidence-Based Reasoning | anchoring claims to data/features |
| RT-09 | Root Cause Explanation | training/production debugging |
| RT-10 | Troubleshooting Decision Tree | "won't converge", "degraded in prod" |
| QA-01 | Self-Verification | every prompt's verification block |
| QA-12 | False Positives Identification | leakage, bias, drift detection |
| QA-17 | Named Scores for Multi-Dimensional Metrics | eval / scorecards |
| DS-01 | Framework Application | governance (EU AI Act, NIST RMF), recsys frameworks |
| DS-02 | Metric Specification | metric selection, monitoring thresholds |
| DS-06 | Prioritization & Severity Guidance | ranked findings / fix queues |
| CM-02 | Constraint Specification | prediction-time boundary, budgets, SLAs |
| RP-02 | Audience-Specific Framing | leadership briefs, jargon translation |
| ED-01/03 | Iterative Scaffolding / Guided Discovery | learner track |
| NE-13 | Technical-to-Business Translation | product-leadership prompts |
| DS-35 | LLM-as-Judge with Rubric | GenAI evaluation |
| AG-29 | Agent Loop Architecture | agentic systems |

## Cross-link map

Before writing a GenAI/LLM-ops/prompt prompt, check whether it already exists in `domain-prompt-engineering/`, `domain-software-engineering/devops/`, `domain-software-engineering/analysis/`, `domain-agentic-resources/skills/`, or `domain-business-strategy/ai-strategy/`. If it does, cross-link via `related_prompts` and the README inventory instead of duplicating. This domain owns the *engineering workflow*; those own the technique reference, ops one-offs, ready-to-run skills, and strategy.
