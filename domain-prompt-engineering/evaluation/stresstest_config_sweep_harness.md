---
title: "Config-Sweep Stress Harness"
category: prompt-engineering/evaluation
description: "Design a pre-production stress test that varies runtime configuration — temperature, model version, context length, and concurrency/load — rather than inputs, holding a fixed challenge set constant, to surface config-sensitivity, latency cliffs, and token-cost spikes before production does. Distinct from adversarial testing (varies the input) and model robustness testing (perturbs the model or data): this varies the deployment knobs an ops team actually turns."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-06
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - stress-testing
  - evaluation
  - parameter-sweep
  - latency
  - token-cost
  - load-testing
  - prompt-engineering
updated: "2026-07-03"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
  - domain-prompt-engineering/evaluation/correctness_production_monitoring_setup.md
  - domain-prompt-engineering/evaluation/regression/regression_release_gate_scorecard.md
  - domain-prompt-engineering/evaluation/adversarial/adv_edge_case_generator.md
  - domain-prompt-engineering/skill-development/promptcraft_eval_harness.md
---

# Config-Sweep Stress Harness

**Objective:** Design a stress test that holds the prompt and its challenge set constant and sweeps the *runtime configuration* around them — temperature, model/version, context length, and concurrency — to find where the same prompt that passes in staging degrades, gets slow, or gets expensive under a configuration the prompt's authors did not test. The artifact is a runnable sweep matrix, a per-cell metrics table, a set of named failure signatures, and a recommended production config envelope (the safe operating ranges per axis). This is the "run stress scenarios" step of a pre-production pipeline, expressed as a reusable eval.

**When to use:**
- A prompt is moving to production and the ops team can change temperature, swap model versions, or hit it at real concurrency — none of which the prompt was tested against.
- A cost or latency incident is suspected to be config-driven (e.g., an unexplained token-spend spike, or a p95 latency cliff under load) and you need to reproduce it deliberately.
- A model migration is planned and you need to know whether the prompt survives the new version at the same settings.
- You already have a correctness eval (input-varying) and need the orthogonal axis: the same inputs under different runtime settings.

**Audience:** Prompt engineers, ML/platform engineers, and SREs hardening an AI feature for production load. This is the runtime-config complement to input-varying evals — run this *alongside* `correctness_eval_design_prompt.md`, not instead of it.

---

## Inputs Required

1. **The prompt, pinned.** Exact text and version. The sweep varies config, not the prompt — if the prompt changes mid-sweep the results are uninterpretable.
2. **A fixed challenge set.** 20–150 cases that already exercise the prompt's real intents and known edge cases. Reuse the correctness eval set or draw from `dataset_case_inventory_from_logs.md` / `adv_edge_case_generator.md`. The set is frozen for the duration of the sweep.
3. **The production baseline config.** The center of the grid: production temperature, current model + version, typical and maximum context length, and expected steady-state QPS plus known burst QPS.
4. **Cost and latency budgets (SLOs).** Per-call token/cost ceiling, p95/p99 latency targets, and the acceptable error/rate-limit rate. Without budgets the sweep produces numbers with no pass/fail meaning.
5. **The decision the sweep will drive.** One of: certify a config envelope for launch / approve a model migration / reproduce a cost-or-latency incident / set production guardrails. The grid design follows from this.
6. **The CI budget.** Wall-clock and dollar ceiling for the sweep itself (a modest CI runner target is single-digit hours and single-digit dollars). This bounds how many grid cells are affordable.

**Refuse or downscope the sweep if:**
- No fixed challenge set exists — build one first; a sweep over ad-hoc inputs measures the inputs, not the config.
- No SLOs/budgets are supplied — the sweep cannot emit a pass/fail without thresholds; collect them or route to a monitoring dashboard instead.
- The requested grid is full-factorial across four axes at many levels each — this explodes combinatorially; force an OFAT or fractional design (see Step 3) within the CI budget.
- The prompt is not yet correctness-stable — fix correctness at the baseline config first; sweeping an unstable prompt confounds config-sensitivity with prompt bugs.

---

## Instructions

### Step 1 — Anchor the baseline config

Record the production configuration as the grid center: temperature, model + exact version string, context-length regime (typical token count and near-limit token count), and concurrency (steady-state QPS, burst QPS). Every swept cell is interpreted as a delta from this anchor. Run the challenge set once at the anchor to establish baseline correctness, latency, and cost — every other cell is compared against this.

### Step 2 — Define the sweep axes and levels

Pick the axes that matter for the decision and set explicit levels for each. Standard axes:

| Axis | Why it fails | Suggested levels |
|------|--------------|------------------|
| **Temperature** | Under- or over-diversified outputs; determinism collapse | Production value plus one lower and one higher extreme (e.g., 0.2 / 0.7 / 1.0) |
| **Model / version** | Silent behavior shift across versions or on migration | Current pinned version + candidate/next version (+ fallback tier if used) |
| **Context length** | Degradation, truncation, or cost blowup as context grows | Typical / near-limit / at-limit |
| **Concurrency / load** | Latency cliffs, rate-limit backoffs, timeout cascades | 1× (serial) / expected QPS / burst QPS |

Only include an axis if the decision depends on it. Two axes at three levels is a real, affordable sweep; four axes at four levels each is 256 cells and usually is not.

### Step 3 — Choose the grid strategy and cost it

State the strategy explicitly and compute the run count before executing:

- **Full factorial** — every combination. Runs = cases × ∏(levels). Use only for 2 axes / small level counts.
- **One-factor-at-a-time (OFAT)** — sweep each axis independently while holding the others at baseline. Runs = cases × Σ(levels − 1) + baseline. The default; catches single-axis sensitivity cheaply.
- **Fractional / targeted** — full factorial only on the 2 axes most likely to interact (e.g., context length × concurrency for cost/latency), OFAT elsewhere.

Compute expected total calls, wall-clock (accounting for the concurrency axis), and dollar cost. If it exceeds the CI budget, drop levels or axes and say which — never silently sample.

### Step 4 — Instrument metrics per cell

For every grid cell, capture, per case and aggregated:

- **Correctness pass-rate** — scored against the existing rubric. The core question: does correctness hold at this config?
- **Output determinism / variance** — across N repeats at that cell (especially at higher temperature). Report agreement rate or output-distance.
- **Latency** — p50 / p95 / p99, measured warm (discard cold-start calls or report them separately).
- **Token usage** — input and output tokens per call, mean and max. Output-token blowup is the usual hidden cost.
- **Cost** — per-call and per-full-run, derived from measured tokens (not estimated).
- **Reliability** — error rate, rate-limit / 429 count, backoff events, timeouts. These appear only under the concurrency axis.
- **Policy violations** — count of disallowed outputs, if a policy checker is wired in.

Run ≥2 repeats per cell so single-run noise is not read as a config effect.

### Step 5 — Detect failure signatures

Scan the matrix for named signatures rather than eyeballing:

- **Config-sensitivity** — correctness pass-rate moves across a single axis by more than the eval's noise floor. Flag the axis and the level where it breaks.
- **Latency cliff** — a knee in p95/p99 at a specific concurrency or context level (small config change, large latency jump).
- **Token-cost spike** — output tokens (and therefore cost) jump disproportionately at a config change — the class of anomaly where identical work suddenly costs many times more. Flag the triggering cell.
- **Determinism collapse** — output variance crosses a usability threshold as temperature rises.
- **Version regression** — the candidate model version degrades any metric relative to the current version at matched settings.
- **Reliability cliff** — error/backoff rate rises sharply at burst QPS.

Rank flagged signatures by severity (blocks launch / needs guardrail / informational).

### Step 6 — Set the run budget and CI fit

Confirm the final design fits the CI envelope: total calls, wall-clock, and cost. State how the sweep is triggered (on model/version change, on prompt change, nightly/weekly) and where raw per-cell results are logged for later drift comparison. A sweep too expensive to rerun on model changes will not be rerun.

### Step 7 — Recommend a production config envelope

Translate the matrix into an operating recommendation:

- **Safe range per axis** — the levels at which all budgets and correctness thresholds hold.
- **Guardrails** — config values that must never be used in production (red cells), and the metric each would breach.
- **Watch items** — configs that pass but sit near a cliff; wire these into `correctness_production_monitoring_setup.md`.
- **Migration verdict** (if applicable) — go / no-go on the candidate model version, with the evidence cell.

The envelope, not the raw matrix, is the deliverable a launch reviewer reads.

---

## Constraints

### Must
- Hold the prompt and challenge set fixed for the entire sweep; vary only runtime config.
- Compute the run count, wall-clock, and cost before executing, and confirm it fits the CI budget.
- Run ≥2 repeats per cell and report variance, not just a point value.
- Derive cost from measured tokens, never from a pre-run estimate.
- Compare every metric against a supplied SLO/budget and against the baseline cell.
- Report the noise floor and treat sub-noise metric moves as "no change."
- Deliver a recommended config envelope, not just a raw matrix.

### Must Not
- Sweep four axes at full factorial without a stated cost check — force OFAT or fractional within budget.
- Read a single-run difference as a config effect; require repeats.
- Mix cold-start and warm latency into one number.
- Change the prompt mid-sweep to "fix" a failing cell — that ends the sweep and starts a new one.
- Report aggregate pass-rate without the per-axis breakdown that reveals which knob broke it.
- Present a launch envelope that includes a cell breaching a hard budget.

---

## False-Positive Prevention

1. **Seed variance mistaken for config sensitivity.** At higher temperature, two runs at the *same* cell differ. Establish the same-cell variance first; only call a cross-axis move "sensitivity" if it exceeds same-cell noise.
2. **Single run per cell.** One call per cell turns ordinary sampling noise into a false cliff. Require ≥2 repeats; more on the temperature and concurrency axes.
3. **Cold-start latency contamination.** The first call to a cold endpoint is slow for reasons unrelated to config. Discard or separate cold calls before computing p95.
4. **Estimated cost instead of measured.** Token estimates miss the exact failure this test exists to catch — the disproportionate output-token spike. Always measure actual tokens.
5. **Provider-side load read as prompt fragility.** A rate-limit spike at burst QPS may be the provider throttling, not the prompt failing. Distinguish 429/backoff (provider) from wrong-output (prompt) in the reliability metrics.
6. **Combinatorial explosion disguised as thoroughness.** A giant full-factorial grid feels rigorous but blows the budget and rarely gets rerun. OFAT catches most single-axis breaks at a fraction of the cost; reserve factorial for the one axis pair likely to interact.
7. **Correctness confounded with config.** If the prompt isn't correctness-stable at baseline, every cell "fails" for reasons that have nothing to do with config. Stabilize at baseline first.
8. **Noise floor ignored on small challenge sets.** A 3 pp pass-rate move on a 30-case set is usually noise. Compute the floor at the set's actual size before flagging a signature.
9. **Envelope drawn from a lucky run.** A cell that passed once may sit on a cliff edge. Flag near-threshold passing cells as watch items rather than certifying them as safe.

---

## Output Format

```markdown
## Prompt under test
[Name + pinned version.]

## Challenge set
[Reference + size + how frozen.]

## Decision the sweep drives
[certify envelope / approve migration / reproduce incident / set guardrails]

## Baseline config (grid center)
| Axis | Baseline value |
|---|---|
| Temperature | [...] |
| Model + version | [...] |
| Context length | [typical / max tokens] |
| Concurrency | [steady QPS / burst QPS] |

## Baseline metrics
- Correctness: [...] | p95 latency: [...] | tokens/call: [...] | cost/run: [...]

## Sweep design
- Axes + levels: [...]
- Strategy: [full factorial / OFAT / fractional] — rationale: [...]
- Runs: [cases × cells = N] | est. wall-clock: [...] | est. cost: [...]
- Repeats per cell: [N]
- Noise floor: [pp at set size N]

## Per-cell metrics matrix
| Cell (axis=level) | Correctness | Variance | p95 lat | Tokens (mean/max) | Cost | Errors/429 | Policy viol. |
|---|---|---|---|---|---|---|---|
| baseline | ... | ... | ... | ... | ... | ... | ... |
| temp=1.0 | ... |
| ctx=at-limit | ... |
| load=burst | ... |
| model=candidate | ... |

## Failure signatures (ranked)
| Severity | Signature | Triggering cell | Evidence | Blocks launch? |
|---|---|---|---|---|
| [...] | latency cliff | load=burst | p95 X→Y | yes |

## Recommended production config envelope
- Safe temperature range: [...]
- Safe context regime: [...]
- Safe concurrency: [...] (guardrail above: [...])
- Model version verdict: [go / no-go + evidence cell]
- Watch items → monitoring: [...]

## CI fit
- Trigger: [on model change / on prompt change / nightly]
- Result log location: [...]
```

---

## Verification

- [ ] Prompt and challenge set were fixed for the whole sweep.
- [ ] Baseline cell was run and every other cell is compared against it.
- [ ] Run count, wall-clock, and cost were computed before executing and fit the CI budget.
- [ ] ≥2 repeats per cell; same-cell variance established before flagging cross-axis effects.
- [ ] Latency is warm-only (or cold reported separately); cost is from measured tokens.
- [ ] Noise floor computed at the challenge set's actual size.
- [ ] Every metric is compared against a supplied SLO/budget.
- [ ] Failure signatures are named, ranked, and tied to a specific cell.
- [ ] Deliverable includes a config envelope with explicit guardrails, not just the raw matrix.
- [ ] No cell breaching a hard budget appears inside the recommended envelope.
