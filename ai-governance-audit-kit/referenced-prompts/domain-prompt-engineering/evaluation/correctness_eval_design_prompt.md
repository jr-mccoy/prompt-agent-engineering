---
title: "Design an Evaluation Set for Correctness"
category: prompt-engineering/evaluation
description: "Design a production-scale evaluation set for an AI task: case coverage by category, a rubric that imports the correctness spec, a scoring protocol that two graders can apply consistently, thresholds that separate signal from noise, and an operating cadence. Output is a runnable eval, not a slideware plan. Distinct from a personal eval harness — this is for tasks where the eval itself must be auditable and rerunnable by a team."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - OC-06
  - QA-01
difficulty: advanced
tags:
  - correctness
  - evaluation
  - eval-set
  - rubric
  - production
  - prompt-engineering
updated: "2026-04-21"
related_prompts:
  - domain-prompt-engineering/evaluation/correctness_discovery_prompt.md
  - domain-prompt-engineering/evaluation/correctness_prompt_specification_audit.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
  - domain-prompt-engineering/evaluation/correctness_production_monitoring_setup.md
  - domain-prompt-engineering/skill-development/promptcraft_eval_harness.md
---

# Design an Evaluation Set for Correctness

**Objective:** Design an evaluation set for an AI task that is large enough to produce meaningful signal, small enough to rerun on a sensible cadence, auditable enough to survive a reviewer asking "how did we pick these cases?" and tied directly to the correctness spec. The artifact includes the case inventory, the rubric, the scoring protocol, the metrics and thresholds, and the operating cadence. The eval is runnable, not aspirational.

**When to use:**
- A prompt or AI feature is moving from personal use to a team-owned or production-owned asset.
- Changes to the prompt, model, or context need to be decided by evidence rather than by whoever shouted last.
- A compliance, safety, or reviewer stakeholder requires a documented evaluation methodology.

**Audience:** Prompt engineers, ML engineers, and developers shipping AI-powered features who need an eval set their team can run, not a personal harness. For personal scale (single operator, <30-minute run, skill-development focus), use `promptcraft_eval_harness.md` instead — they are different tools with different methodologies.

---

## Inputs Required

1. **The correctness spec.** Produced by `correctness_discovery_prompt.md` or equivalent. Must include consumer, must-haves, must-nots, refusal conditions, and at least one resolved tradeoff. An eval without a spec scores against graders' drifting intuition.
2. **The task's real input distribution.** The mix of inputs the prompt sees in production, in rough proportions. Volumes are nice but not required; proportions matter.
3. **20+ real past inputs with their outputs.** The eval draws cases from real inputs; synthetic cases are used only to extend specific under-represented categories, and only when labeled as synthetic.
4. **Who will run and score the eval.** Named: self-service, one owner, rotating, external annotator pool. Scoring methodology depends on this.
5. **The decision the eval will drive.** One of: adopt prompt change / swap model / change context / hold release / report to stakeholder. Different decisions need different thresholds.
6. **The operating cadence the eval must fit.** On-change only, weekly, monthly, quarterly. An eval too expensive for its cadence will rot.

**Refuse the design if:**
- No correctness spec exists.
- Fewer than 20 real past inputs are available. Smaller pools cannot cover the case categories an auditable eval needs.
- The eval is meant to make a decision the user hasn't named. Rubric and thresholds follow from the decision.
- The user wants an eval purely for reassurance with no decision attached. That is not an eval; it's a ritual. Refuse or route to a dashboard.

---

## Instructions

### Step 1 — Build the case inventory by category

Divide the eval set into 5–8 categories that together cover the prompt's real input distribution. Typical categories:

- **Canonical cases.** Representative of the high-frequency middle of the distribution. ~40% of eval volume.
- **Edge cases.** Real low-frequency but plausible inputs. ~20%.
- **Adversarial cases.** Inputs designed to probe known failure modes (from `correctness_pre_mortem.md`). ~15%.
- **Ambiguous cases.** Inputs where the correctness spec's refusal condition is in play. ~10%.
- **Regression cases.** Specific past-incident inputs that must continue to pass. ~10%.
- **Out-of-scope cases.** Inputs the system should refuse. ~5%.

Draw cases from the 20+ real input pool. Label each case with its category, its source (real / synthetic), and a unique ID. Target eval-set size: 40–150 cases. Smaller and the category-level signal is too noisy; larger and the cadence breaks.

### Step 2 — Translate the spec into a rubric

From the correctness spec, derive the rubric:

- **Must-haves → binary (pass / fail) criteria.** Each must-have is one rubric item. Any must-have failing = case fails.
- **Must-nots → binary (pass / fail) criteria.** Same structure.
- **Refusal conditions → binary on applicable cases.** Only scored on inputs where refusal is the correct response.
- **Tradeoff policy → directional criterion.** Score whether the dominant dimension was protected; treat violation as a fail on the policy criterion.
- **Nice-to-haves → optional graded (0 / 1).** Not counted toward pass/fail; tracked for drift.

Each rubric item must be applicable by two graders independently without needing the spec's author. If it isn't, revise the spec or revise the rubric item until it is.

### Step 3 — Set the scoring protocol

Name:

- **Grader(s).** Self / team / external. Named roles, not named people.
- **Blinding.** Whether the grader sees the prompt version / model / input order.
- **Inter-rater policy.** At what frequency are cases double-scored, and how are disagreements resolved.
- **Per-case scoring budget.** A grader's average time per case. The eval set's total run cost is cases × per-case budget.
- **Calibration protocol.** How new graders are onboarded against a set of anchor cases so scoring is consistent across cohorts.

A scoring protocol that doesn't name inter-rater policy accepts drift as a methodology choice.

### Step 4 — Define metrics and thresholds

Derive metrics from the rubric:

- **Primary metric.** Share of cases passing all must-haves and must-nots. One number that summarizes whether the system is meeting spec.
- **Category-breakdown metrics.** Pass rate per category. Important because aggregate numbers hide category-specific regressions.
- **Guardrail metric.** A specific must-not or refusal-condition rate that should never degrade, even if the primary metric improves. Usually tied to the highest-severity failure from the pre-mortem.
- **Noise floor.** Below what change in primary metric (absolute percentage points) is a difference indistinguishable from sampling noise at this eval size. Compute using the eval's actual size, not a rule of thumb.

Thresholds follow from the decision:

- **Adopt.** Primary metric improves by more than the noise floor, no category regresses by more than the noise floor, guardrail metric does not degrade.
- **Reject.** Any of the above fails.
- **Rerun.** Borderline changes — rerun at 2× sample before deciding.

The thresholds are committed in advance. Deciding after the fact invites motivated thresholds.

### Step 5 — Write the run protocol

One page. The team must be able to run the eval end-to-end using only this document. Include:

- Exact prompt text used (copy-paste, pinned version).
- Model and model version.
- Any tool / context configuration.
- Case execution order (fixed ID order, or randomized with seed).
- Output capture format.
- Grading environment (blinded, what the grader sees).
- Who scores, in what time window.
- Where raw outputs and scores are logged.

Reproducibility is non-negotiable. An eval whose method isn't documented produces numbers that can't be compared across runs.

### Step 6 — Set the operating cadence and ownership

Name:

- **Cadence.** On-change-only, or periodic (weekly / monthly / quarterly), or both.
- **Owner.** One named role responsible for the eval's health. Not a committee.
- **Revision policy.** When and how the eval set itself is updated — which cases can be retired, which added, how the spec-to-rubric mapping is re-verified.
- **Decommissioning condition.** What would cause the eval to be retired (task retired, spec materially changed, model migrated away from the evaluated behavior).

An eval without an owner rots. An eval whose revision policy is "whenever" drifts silently.

### Step 7 — Pilot the eval

Before adopting the eval as the team's decision instrument, run it once against the current prompt:

- Establish the baseline primary and guardrail metrics.
- Confirm two graders produce consistent scores on a 10-case subset.
- Flag cases where the rubric was ambiguous — either fix the rubric or retire the case.
- Time the run end-to-end; confirm it fits the cadence.

An eval that hasn't been piloted is a design, not a tool.

### Step 8 — Write the eval dossier

Final artifact: a dossier containing everything a reviewer needs to understand, audit, and rerun the eval. Case inventory, rubric, protocol, metrics, thresholds, baseline, ownership. If any of these are missing, the eval is not audit-ready.

---

## Constraints

### Must
- Derive the rubric directly from the correctness spec.
- Draw cases from real past inputs for at least 85% of the set; label synthetic cases as such.
- Name the grader role, blinding, and inter-rater policy before running.
- Commit metrics and thresholds in advance of any decision.
- Pilot the eval and establish a baseline before using it as a decision instrument.
- Name an owner, cadence, and decommissioning condition.

### Must Not
- Use an eval set the same person who authored the prompt scored without blinding.
- Decide thresholds after seeing the result.
- Replace the correctness spec with the eval — the eval scores against the spec, not the other way around.
- Grow the eval beyond what fits the operating cadence. An eval that rots is worse than no eval.
- Present aggregate metrics without category breakdowns.
- Use synthetic cases to plug gaps in categories where real inputs exist — collect more real inputs instead.

---

## False-Positive Prevention

1. **Rubric drift from spec.** The rubric starts aligned to the spec, then slowly absorbs graders' intuitions. Re-verify the spec-to-rubric mapping on every revision; name divergences as spec changes or rubric bugs, not as improvements.
2. **Threshold motivated reasoning.** Thresholds set after the fact always seem to support the decision the author wanted. Commit thresholds in the dossier before running; changing them requires a revision and explanation.
3. **Aggregate metric hiding category regression.** Primary metric up, a specific category down. This is the most common failure of aggregate reporting. Category breakdowns are mandatory, not optional.
4. **Noise floor ignored.** A 3 pp change on a 50-case eval is usually noise. Claiming a decision on noise is the main way evals produce wrong conclusions. Compute the noise floor using the eval's actual size.
5. **Inter-rater drift.** Two graders often disagree by 10%+ on subjective rubrics. Without a double-scoring policy, the eval reports scoring drift as prompt drift.
6. **Grader-author conflict.** The prompt author scoring their own prompt produces generous scores. Blinding and rotated graders are protections, not luxuries.
7. **Eval rot.** Quarterly evals that take 8 hours to run will be skipped. Size the eval to the cadence, not the cadence to the eval.
8. **Synthetic case over-use.** Synthetic cases are cheap and drift away from real inputs. A synthetic-heavy eval measures the eval's imagination, not the prompt's production behavior. Cap synthetic at ~15% and label it.
9. **Eval as dashboard.** Evals drive decisions; dashboards display state. Running an eval weekly "just to watch" is expensive and low-signal. If the user wants a dashboard, route them to `correctness_production_monitoring_setup.md`.
10. **Calibration skipped.** New graders onboarded without a calibration set produce baselines that don't compare across cohorts. Always calibrate.

---

## Output Format

```markdown
## Task under evaluation
[Prompt / system.]

## Spec in use
[Reference + inline summary.]

## Decision the eval will drive
[One of: adopt / reject / hold / report.]

## Case inventory (40–150)
| Category | Target % | Actual count | Source (real/synthetic) | IDs |
|---|---|---|---|---|
| Canonical | 40% | [...] | real | [...] |
| Edge | 20% | [...] | real | [...] |
| Adversarial | 15% | [...] | real + synthetic | [...] |
| Ambiguous / refusal | 10% | [...] | real | [...] |
| Regression | 10% | [...] | real | [...] |
| Out-of-scope | 5% | [...] | real | [...] |

## Rubric
| # | Criterion | Type (pass-fail / directional / graded) | Source (must-have / must-not / refusal / tradeoff / nice-to-have) |
|---|---|---|---|
| 1 | [...] | [...] | [...] |
| ... |

## Scoring protocol
- Grader role: [...]
- Blinding: [...]
- Inter-rater: [% double-scored, disagreement policy]
- Per-case budget: [min]
- Calibration protocol: [...]

## Metrics and thresholds (committed in advance)
- Primary: [metric] — adopt at ≥ [threshold] improvement above noise floor
- Category breakdowns: [no category may regress by more than noise floor]
- Guardrail: [metric] — never degrade
- Noise floor: [pp, computed at eval size N]

## Run protocol (reproducible)
- Prompt version: [pinned]
- Model + version: [...]
- Context / tool config: [...]
- Case order: [fixed / randomized-seeded]
- Output capture: [...]
- Score log location: [...]

## Cadence + ownership
- Cadence: [on-change / periodic]
- Owner: [role]
- Revision policy: [...]
- Decommissioning condition: [...]

## Pilot + baseline
- Date: [...]
- Baseline primary: [...]
- Baseline category breakdowns: [...]
- Baseline guardrail: [...]
- Inter-rater agreement on 10-case subset: [%]
- Run time: [min]

## Dossier checklist
- [ ] Case inventory complete
- [ ] Rubric derived from spec
- [ ] Protocol documented
- [ ] Thresholds committed
- [ ] Pilot run + baseline recorded
- [ ] Owner named
- [ ] Cadence fits run time
```

---

## Verification

- [ ] Spec is in hand and dated.
- [ ] Eval size is 40–150 cases.
- [ ] ≥85% of cases are from real inputs; synthetic cases are labeled.
- [ ] Rubric items map to spec elements; no rubric item lacks a spec source.
- [ ] Thresholds are committed before the first decision run.
- [ ] Noise floor is computed for the eval's actual size.
- [ ] Category breakdowns are reported alongside aggregate metrics.
- [ ] Inter-rater policy is documented and piloted.
- [ ] Cadence × run time is sustainable.
- [ ] Owner role is named (not a committee).
