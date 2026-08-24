---
title: "AI Agent Evaluation Design"
category: AI-ML/agentic-ai-systems
description: "Design a reproducible agent evaluation that scores task success alongside cost, latency, safety, and trajectory quality — not success rate in isolation."
techniques:
  - ST-02
  - DS-02
  - QA-20
  - RT-05
  - DS-35
difficulty: advanced
tags:
  - agent-evaluation
  - trajectory-quality
  - cost-safety
  - reproducibility
  - llm-as-judge
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md
  - domain-AI-ML/agentic-ai-systems/aiagent_cost_token_budget_design.md
---

# AI Agent Evaluation Design

**Objective:** Design an evaluation harness for an agent that measures, on a fixed and reproducible task set, not just whether it succeeded but at what cost, latency, and safety, and with what trajectory quality — so a "high success rate" can never hide an agent that is expensive, slow, unsafe, or right-by-luck.

**When to Use:**
- Before trusting any agent success number, or before comparing two agent designs / model versions.
- An agent passes demos but you have no way to detect regressions across cost, latency, or unsafe actions.
- You need a golden task set and scoring rubric a team can re-run reproducibly.

**When NOT to Use:**
- You only need to evaluate a single non-agentic LLM output (use a GenAI eval prompt in `domain-prompt-engineering/evaluation/`).
- You are designing the agent itself (use `aiagent_architecture_design.md`); evaluation comes after a spec exists.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Agent spec** — its goal, tools, and what "done" means as an observable artifact.
- **Task population** — the real distribution of tasks (easy/typical/hard/adversarial), or examples to sample from.
- **Success definition** — programmatic check, rubric, or human judgment; and who/what adjudicates.
- **Budgets** — cost/latency/failure ceilings the agent must respect (from `aiagent_cost_token_budget_design.md`).
- **Safety boundary** — actions that must never happen (irreversible/out-of-scope), and how they are detected.

## Constraints

**Must:**
- Score every run on four axes at minimum: task success, cost (tokens/$), latency, and safety; add trajectory quality for multi-step agents.
- Make the task set fixed, versioned, and reproducible (frozen inputs, fixed seeds where possible, recorded environment/tool versions).
- Report success with intervals or counts, never as a bare point estimate, and against a baseline (no-agent / simple-heuristic / prior version).

**Must Not:**
- Fabricate benchmark numbers or cite SOTA figures from memory — reason only from runs on the user's task set.
- Use an LLM judge without a rubric and a human-calibration sample.
- Let a single happy-path demo stand in for evaluation.

**Instructions:**

1. **Define the success criterion precisely.** State the checkable artifact or state change that counts as success, and the adjudication method (code check / rubric / human). Resolve partial success explicitly (graded or binary).

2. **Build a representative, versioned task set.** Sample tasks across difficulty and include adversarial/edge cases (ambiguous input, tool failures, traps). Freeze inputs and record environment so the set is reproducible and re-runnable.

3. **Instrument the four core axes.** For each run capture: success outcome, total tokens/cost, end-to-end latency, and any safety-boundary violation (attempted or completed unsafe action). Log enough to recompute later.

4. **Score trajectory quality (multi-step agents).** Beyond the final answer, assess the path: redundant steps, unnecessary tool calls, loops, recovery from errors. A correct answer reached by a wasteful or unsafe path is a partial failure.

5. **Set up adjudication and judge calibration.** If using an LLM-as-judge, give it a rubric and validate it against a human-labeled sample; report judge agreement. Keep adversarial cases where judges are known to be weak.

6. **Anchor to baselines and report uncertainty.** Compare against no-agent / simple heuristic / prior version. Report per-axis results with counts or confidence intervals and per-slice breakdowns (by difficulty/category).

7. **Define pass/fail gates and regression triggers.** State the thresholds on each axis that gate a release, and what change (success drop, cost spike, new safety violation) triggers investigation.

8. **Specify reproducibility metadata.** Record model/version, tool versions, task-set version, seeds, and date so a result can be reproduced or contested.

**Output Format:**

A markdown eval design:
- **Success Criterion & Adjudication** — checkable definition + method
- **Task Set Spec** — composition table (difficulty × category × count), reproducibility metadata
- **Scorecard** — table: Axis | Metric | Baseline | Gate threshold
- **Trajectory Quality Rubric** — dimensions + scoring
- **Judge Calibration Plan** — rubric + human-sample agreement (if LLM judge)
- **Reporting Template** — per-axis results with intervals + per-slice breakdown + regression triggers

## Verification

- [ ] Success, cost, latency, and safety are all instrumented; trajectory quality covered for multi-step agents.
- [ ] The task set is fixed, versioned, and includes adversarial/edge cases.
- [ ] Results are reported against a baseline with counts/intervals, never as a bare success rate.
- [ ] Any LLM judge has a rubric and a stated human-agreement figure.
- [ ] Pass/fail gates and regression triggers are defined per axis.
- [ ] Reproducibility metadata (versions, seeds, date) is recorded.

## False-Positive Prevention

❌ **DON'T:**
- Report "92% success" without cost, latency, safety, and the baseline it beats.
- Treat a correct final answer as a pass when the trajectory looped, over-called tools, or attempted an unsafe action.
- Trust an LLM judge's score without checking it against human labels on a sample.
- Re-run on a task set that quietly changed between versions and call the comparison fair.

✅ **DO:**
- Force every success number to travel with its cost, latency, safety, and baseline.
- Grade the path, not only the destination, for multi-step agents.
- Calibrate judges and keep adversarial cases where they fail.
- Freeze and version the task set so comparisons are apples-to-apples and reproducible.

## Example Output

```markdown
## Eval Design: Research-Summarizer Agent v2 vs v1

### Success Criterion & Adjudication
Success = summary covers all 5 required facts (rubric) AND cites only retrieved sources (code check). Partial = 3–4 facts (graded 0.5).

### Task Set Spec
| Difficulty | Category | Count |
|---|---|---|
| Easy | single-source | 30 |
| Typical | multi-source | 40 |
| Hard | conflicting sources | 20 |
| Adversarial | no answer exists / trap source | 10 |
Reproducibility: task-set v2.1 (frozen), model X-1.2, retrieval tool v3, seed 7, run 2026-05-28.

### Scorecard
| Axis | Metric | Baseline (v1) | Gate |
|---|---|---|---|
| Success | graded pass rate | 0.74 | ≥ 0.80 |
| Cost | tokens/task (mean) | 18k | ≤ 20k |
| Latency | p95 | 31s | ≤ 35s |
| Safety | citation-fabrication rate | 4% | 0% |

### Trajectory Quality Rubric
Redundant retrieval calls (−), recovered from tool error (+), looped (fail), stayed within step cap.

### Judge Calibration Plan
Rubric-based LLM judge; agreement with 50 human labels = 0.89 Cohen's κ. Conflicting-source cases double-scored by human.

### Reporting Template
v2: success 0.83 [0.78–0.88], 17k tokens, p95 28s, fabrication 0% — passes all gates; investigate 2 hard-slice regressions vs v1.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** criterion → task set → instrumentation → judging → gates.
- **DS-02 (Metric Specification):** defines the four axes and their measurement precisely.
- **QA-20 (Comprehensive Evaluation Coverage):** forces multi-axis, multi-slice, adversarial coverage.
- **RT-05 (Evidence-Based Reasoning):** results are reasoned from runs, never fabricated benchmarks.
- **DS-35 (LLM-as-Judge with Rubric):** governs calibrated, rubric-anchored adjudication.

**Related Prompts:**
- `aiagent_architecture_design.md` — the spec this evaluation tests.
- `aiagent_failure_mode_analysis.md` — the failure modes the safety/trajectory axes detect.
- `aiagent_cost_token_budget_design.md` — source of the cost/latency budgets used as gates.
