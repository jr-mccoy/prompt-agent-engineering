---
title: "Build an Eval Harness for a Personal Workflow"
category: prompt-engineering/skill-development
description: "Produce a lightweight, personal-scale eval harness for a task type the user runs repeatedly with AI — 5–10 representative inputs, a rubric, a scoring protocol, and a baseline. The harness is for skill development and quality tracking, not for production CI. It makes prompt changes measurable instead of felt."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-01
difficulty: advanced
tags:
  - skill-development
  - eval-harness
  - personal-workflow
  - measurement
  - baseline
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/skill-development/promptcraft_specification_defines_done.md
  - domain-prompt-engineering/skill-development/promptcraft_rapid_four_discipline_diagnostic.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Build an Eval Harness for a Personal Workflow

**Objective:** Produce a lightweight eval harness — 5–10 representative inputs, a rubric, a scoring protocol, and a baseline measurement — for a specific task type the user runs repeatedly with AI. When the user changes a prompt, swaps a model, adjusts context, or tries a new approach, they can rerun the harness and see whether the change helped, hurt, or didn't matter. The harness is personal-scale (not production CI) and optimized for being cheap to run manually.

**When to use:** The user runs the same task type 5+ times a month (e.g., weekly memo drafts, code-review summaries, research synthesis, customer-email triage) and can't tell whether prompt tweaks are actually improving things. Or: the user wants to compare two prompts, two models, or two context strategies without relying on "it feels better."

**Audience:** Users who've already built a spec for the task (via `promptcraft_specification_defines_done.md` or similar) and want to measure against it. Not for one-off tasks. Not for users still forming intuition for the task type — they need more reps before an eval harness pays off.

**Personal scale, not production scale.** This harness is designed to run manually in under 30 minutes. It does not need a test runner, a CI pipeline, or a golden-dataset methodology. Users who need those should graduate to `correctness_eval_design_prompt.md` and/or Session 9's upcoming `correctness_prompt_specification_audit.md`.

---

## Inputs Required

1. **A task type the user runs ≥5 times/month.** Named specifically. "Drafting customer follow-up emails after a discovery call" is a task type. "Writing" is not.
2. **The spec for that task type.** Produced by `promptcraft_specification_defines_done.md` or equivalent. If none exists, stop — an eval harness without a spec is scoring against the user's shifting intuition.
3. **At least 10 real past instances of the task.** With their inputs (the situation) and the actual outputs the user accepted. No synthetic examples.
4. **The user's current prompt** for the task.
5. **What the user is actually trying to measure.** One of:
   - Is my new prompt better than my old one?
   - Is model A better than model B?
   - Is my context document helping or hurting?
   - Is quality drifting over time?

Refuse to build a harness on synthetic inputs. A harness scored on invented tasks measures the harness's invention quality, not the user's workflow quality. Also refuse without a spec — without a spec, scoring is subjective and the harness's numbers mean nothing.

---

## Instructions

### Step 1 — Choose 5–10 representative inputs

From the 10+ real past instances, select a representative set:
- Include 2–3 *easy* cases (clear, well-formed input).
- Include 2–3 *edge* cases (ambiguous, thin-input, unusual constraints).
- Include 1–2 *trap* cases (the model historically gets these wrong in a specific way).
- Skip cases that are so idiosyncratic they won't generalize.

Fewer than 5: the harness is too noisy; any single bad run swings the score. More than 10: the harness takes too long to run manually, and users will stop running it.

Anonymize sensitive content before including it in the harness — the harness will be reread often.

### Step 2 — Write the rubric

Import the spec's criteria. Translate them into a rubric:
- **Must-pass criteria → binary (pass / fail).** Any fail = output fails the case.
- **Should-pass criteria → 0 / 0.5 / 1 per criterion.** Summed and normalized per case.
- **Nice-to-have → optional, 0 / 1 bonus.**

Each case yields a tuple: `(must_pass: bool, should_pass_score: 0–1, nice_to_have: 0–N)`. Aggregate across cases: % of cases must-passing, average should-pass score.

If the spec has 5 criteria, each case takes ~1 minute to score. 10 cases × 1 minute = 10 minutes per run. This is the scale the harness is designed for.

### Step 3 — Establish the baseline

Run the *current* prompt against all 5–10 cases. Score each. This is the baseline.

Record:
- % must-passing.
- Average should-pass score.
- Notes: patterns in failures (which criteria fail most often, on which case types).

Users often skip the baseline because "I already know my prompt works" — but without it, later changes can't be compared. The baseline is 80% of the harness's value.

### Step 4 — Write the run protocol

One paragraph, so the user doesn't have to reconstruct the method each time:
- Exact prompt used (copy-paste, don't paraphrase).
- Model + version.
- Any context attached.
- Order of cases (randomize or fixed).
- Time budget per case (usually: accept the model's first output; don't iterate).

Consistency across runs is what lets score changes mean something. A harness where the method drifts is indistinguishable from a harness with no method.

### Step 5 — Decide the change-detection thresholds

Personal-scale harnesses are noisy. Ten cases is a small sample. Decide in advance how big a change has to be to count:
- % must-passing: changes ≥ 20 percentage points are meaningful; smaller could be noise.
- Average should-pass score: changes ≥ 0.15 on a 0–1 scale are meaningful.

Smaller changes should trigger a rerun, not a conclusion. (Sample size really is small.)

### Step 6 — Decide when to rerun

A harness rotted from neglect is worse than no harness (it produces false comparisons). Decide:
- **On prompt change.** Always rerun the full harness before adopting a new prompt.
- **On model version change.** Always rerun.
- **Quarterly.** Even without changes — to catch silent drift.

If the harness becomes costly to rerun, it's too big. Cut cases.

### Step 7 — Build the revision log

Every time the harness is rerun, log:
- Date.
- What changed (prompt / model / context).
- Score before / after.
- Decision (adopt / reject / rerun).

The revision log is the skill-development artifact that survives the harness. Over a year of logs, the user sees what actually moved the needle.

### Step 8 — Name what the harness doesn't measure

Harnesses measure what's in the rubric. They don't measure:
- Latency.
- Cost.
- Whether the task itself was worth running.
- Subjective qualities outside the spec.

Name these explicitly. Users who forget will conclude from harness results that their prompt is good when the harness couldn't have told them it was slow, expensive, or beside the point.

---

## Constraints

### Must
- Use 5–10 real, representative cases.
- Import rubric directly from an existing spec.
- Record a baseline before comparing to anything.
- Document the run protocol so reruns are comparable.
- Log changes and results.

### Must Not
- Be built without a pre-existing spec.
- Use synthetic or invented cases.
- Run with an inconsistent method (drifted prompts, different models, mixed context).
- Over-interpret small score changes on a 10-case sample.
- Grow beyond what the user will actually rerun. If it takes more than 30 minutes, it's over-engineered for personal scale.
- Replace user judgment on what "good" means — the rubric is derived from the user's spec, not from generic best practices.

---

## False-Positive Prevention

1. **Cherry-picked cases.** Users unconsciously pick cases they know their current prompt handles well. Force the mix: 2–3 edges, 1–2 traps.
2. **Unstable rubric.** If the user changes the rubric between runs, scores aren't comparable. Freeze the rubric; revise the spec first if needed, then rerun the baseline before any new comparison.
3. **Scoring drift.** Scoring manually is subjective. To catch drift, score blind: don't look at the prompt/model label when grading. If that's not possible, rescore the baseline cases at the end of each run to check calibration.
4. **Adoption on noise.** Adopting a new prompt on a 10% score bump is probably adopting noise. Require ≥20 pp must-pass change or ≥0.15 should-pass change before adoption.
5. **The harness that replaces the spec.** Harnesses score against the spec; they don't replace it. If the user is grading on "feels better" rather than on rubric hits, the harness isn't doing its job — the spec is.
6. **Using this harness for production CI.** Personal-scale harnesses are not production gates. Don't wire them into deployment pipelines. That's a different tool with different methodology.
7. **Harness rot.** A harness the user hasn't rerun in 6 months may score against an obsolete spec, stale cases, a retired model. Either update or retire.
8. **Comparing across specs.** Comparing prompts on different specs is incoherent. If the spec changed, the comparison starts from a new baseline.

---

## Output Format

```markdown
## Task type
[Named specifically.]

## Spec in use
[Reference / inline version.]

## Cases (5–10)
| # | Label | Category (easy/edge/trap) | Input reference | Accepted past output (for calibration) |
|---|---|---|---|---|
| 1 | [...] | easy | [...] | [...] |
| ... |

## Rubric
- Must-pass criteria (binary):
  - [criterion]
  - [...]
- Should-pass criteria (0 / 0.5 / 1):
  - [...]
- Nice-to-have (0 / 1 bonus):
  - [...]

## Run protocol
- Prompt: [exact text, or link to pinned version]
- Model + version: [...]
- Context attached: [...]
- Order: [fixed / randomized]
- Per-case: accept first output, don't iterate.

## Baseline
- Date: [...]
- % must-passing: [...]
- Avg should-pass score: [...]
- Failure patterns: [...]

## Change-detection thresholds
- Must-pass: ≥ 20 pp to count.
- Should-pass: ≥ 0.15 on 0–1 scale to count.

## Rerun triggers
- On prompt change / model version change / quarterly.

## Revision log
| Date | What changed | Before | After | Decision |
|---|---|---|---|---|

## What this harness doesn't measure
- [...]
```

---

## Verification

- [ ] 5–10 real, labelled cases covering easy / edge / trap.
- [ ] Rubric was imported from an existing spec, not invented.
- [ ] Baseline scored before any comparison.
- [ ] Run protocol documents exact prompt, model, context.
- [ ] Change-detection thresholds are set before running.
- [ ] Revision log is in place.
- [ ] What the harness doesn't measure is stated explicitly.
- [ ] Total manual run time < 30 minutes.
