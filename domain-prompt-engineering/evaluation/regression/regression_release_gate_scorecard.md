---
title: "Release-Gate Scorecard"
category: prompt-engineering/evaluation/regression
description: "Turn eval and stress-sweep results into a merge decision: compare a candidate run against a frozen baseline, compute per-metric deltas against noise floors, assign a traffic-light status to each metric, hard-fail on blocker thresholds, and emit a PR-ready scorecard comment. This is the 'analyse and gate releases' artifact — the thing that actually blocks or clears a prompt/model change."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - RT-05
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - release-gate
  - regression_testing
  - scorecard
  - ci-gate
  - baseline-comparison
  - prompt-engineering
updated: "2026-07-03"
related_prompts:
  - domain-prompt-engineering/evaluation/regression/regression_golden_set_curator.md
  - domain-prompt-engineering/evaluation/regression/regression_ab_test_runner_prompt.md
  - domain-prompt-engineering/evaluation/regression/regression_change_impact_estimator.md
  - domain-prompt-engineering/evaluation/stresstest_config_sweep_harness.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Given a candidate evaluation run (from a prompt change, model swap, or config sweep) and a frozen baseline run, produce a release-gate decision: a per-metric delta table judged against pre-committed thresholds and noise floors, a traffic-light status per metric, a single roll-up verdict (PASS / SOFT-FAIL / HARD-FAIL), and a pull-request-ready comment. The scorecard is the artifact that clears or blocks the merge — not a dashboard, not a report. Every scorecard is archived so drift is visible across releases.

## When to Use

- A prompt or model change has been evaluated and someone must decide whether it ships.
- You want the merge gated automatically in CI rather than by whoever reviews last.
- A config sweep (`stresstest_config_sweep_harness.md`) produced metrics that need to be judged against launch budgets.
- You need an auditable record of *why* a release was cleared or blocked, comparable to prior releases.

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `candidate_results` | Yes | Structured results (JSON/CSV) from the candidate run: per-metric values, eval-set version, model+version, config |
| `baseline_results` | Yes | The frozen, pinned last-known-good run to compare against — same eval-set version and rubric |
| `metric_policy` | Yes | Per-metric classification (blocker / guardrail / tracked), threshold, and direction (higher- or lower-is-better) |
| `noise_floors` | Yes | Per-metric minimum meaningful delta, computed at the eval-set's actual size |
| `gate_policy` | Optional | Who may override a SOFT-FAIL, and how an override is logged |

## Constraints

**Must:**
- Verify the baseline is frozen and comparable (same eval-set version and rubric) before computing any delta; abort with a clear message if not.
- Classify every metric as `blocker`, `guardrail`, or `tracked` before judging it.
- Compare each delta against its noise floor and label sub-floor moves as `within-noise`, not as improvement or regression.
- Assign each metric a traffic light: green / yellow / red, by explicit rule (below).
- Roll up to exactly one verdict: `PASS`, `SOFT-FAIL`, or `HARD-FAIL`.
- Emit a PR-ready comment containing the verdict, the metric table with deltas and colors, and the baseline ID.
- State the baseline-promotion rule (when the candidate becomes the new frozen baseline).

**Must Not:**
- Compare a candidate against a baseline scored on a different eval-set version or rubric — that is a category error, not a delta.
- Set or change any threshold after seeing the candidate's numbers.
- Roll up to PASS while any blocker metric is red or any guardrail metric has degraded past noise.
- Report a single aggregate number without the per-metric / per-category breakdown that can hide a regression.
- Allow a HARD-FAIL to be overridden by the gate policy (only SOFT-FAIL is overridable).

## Instructions

**Step 1 — Validate comparability**

Confirm `candidate_results` and `baseline_results` share the same eval-set version and rubric. If they differ, stop: report the mismatch and require a re-baseline. A delta across incompatible runs is meaningless.

**Step 2 — Classify each metric**

| Class | Meaning | Gate effect |
|-------|---------|-------------|
| `blocker` | Hard threshold that must not be crossed (e.g., policy-violation count > 0, correctness below floor) | Red here → HARD-FAIL |
| `guardrail` | A metric that must never degrade past noise even if others improve (usually the highest-severity failure) | Degrade past noise → HARD-FAIL |
| `tracked` | Informational; regressions are surfaced but do not block | Never blocks; may trigger SOFT-FAIL |

**Step 3 — Compute deltas against the noise floor**

For each metric: `delta = candidate − baseline` (oriented by direction). Then label:

| Condition | Label |
|-----------|-------|
| Improvement exceeds noise floor | `improved` |
| \|delta\| ≤ noise floor | `within-noise` |
| Regression exceeds noise floor | `regressed` |

**Step 4 — Assign traffic lights**

| Metric state | Light |
|--------------|-------|
| `improved` or `within-noise` | 🟢 green |
| `tracked` metric `regressed` | 🟡 yellow |
| `guardrail` metric `regressed` | 🔴 red |
| `blocker` threshold crossed | 🔴 red |

**Step 5 — Roll up to a verdict**

- **HARD-FAIL** — any 🔴 red (blocker crossed or guardrail degraded). Blocks merge; not overridable.
- **SOFT-FAIL** — no red, but ≥1 🟡 yellow (a tracked regression). Blocks merge pending a logged manual override per `gate_policy`.
- **PASS** — all 🟢 green.

**Step 6 — Emit the PR scorecard comment**

Produce the comment in the Output Format below: verdict badge, metric table with deltas and lights, an explicit list of regressions with their evidence, the baseline ID, and a link/pointer to raw artifacts.

**Step 7 — Baseline promotion + archival**

State the rule: on merge of a PASS (or overridden SOFT-FAIL), the candidate results become the new frozen baseline, tagged with the commit. Archive every scorecard (pass or fail) so a reviewer can trace the metric's trajectory across releases and detect slow drift that no single gate caught.

## Output Format

```markdown
### 🚦 Release-Gate Scorecard — [VERDICT: PASS | SOFT-FAIL | HARD-FAIL]

**Baseline:** `[baseline_id / commit]`  ·  **Candidate:** `[commit]`
**Eval set:** `[version]`  ·  **Model:** `[name + version]`  ·  **Noise floor basis:** N=[eval size]

| Metric | Class | Baseline | Candidate | Δ | vs noise | Light |
|--------|-------|----------|-----------|---|----------|-------|
| Correctness (primary) | blocker | ... | ... | ... | improved/within-noise/regressed | 🟢/🟡/🔴 |
| Policy violations | blocker | 0 | ... | ... | ... | ... |
| [guardrail metric] | guardrail | ... | ... | ... | ... | ... |
| p95 latency | tracked | ... | ... | ... | ... | ... |
| Cost / run | tracked | ... | ... | ... | ... | ... |

**Regressions requiring attention:**
- [metric]: [baseline → candidate], exceeds noise floor by [X]. Evidence: [link/case IDs].

**Verdict rationale:** [which rule fired — e.g., "guardrail X regressed past noise → HARD-FAIL"]

**Override:** [N/A for HARD-FAIL | required role + logged reason for SOFT-FAIL]

**On merge:** candidate promoted to baseline `[new_id]`. Scorecard archived at `[location]`.
```

## Verification

- [ ] Baseline confirmed frozen and on the same eval-set version + rubric as the candidate.
- [ ] Every metric classified blocker / guardrail / tracked before judging.
- [ ] Every delta compared against a noise floor computed at the actual eval size.
- [ ] Traffic lights assigned by the stated rules, not by judgment call.
- [ ] Exactly one roll-up verdict emitted; no PASS while any red is present.
- [ ] No threshold was set or altered after the candidate numbers were seen.
- [ ] Per-metric breakdown present; no bare aggregate.
- [ ] PR comment includes verdict, table, regressions, baseline ID, and artifact pointer.
- [ ] Baseline-promotion rule and scorecard archival location stated.
