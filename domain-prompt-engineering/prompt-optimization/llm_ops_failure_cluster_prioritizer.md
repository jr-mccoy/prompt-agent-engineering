---
title: "Eval Failure Clustering and Fix Prioritiser — From a Pile of Failed Outputs to a Ranked Backlog, by Lever"
category: prompt-engineering/prompt-optimization
description: "Turn one eval run's failures into a ranked fix backlog: open-code each failure by the first thing that went wrong, group the notes into defined clusters, audit for grader and label errors before blaming the prompt, weight clusters by frequency, severity and production share, assign each to its lever (prompt, examples, format, context, tool, model, decomposition, or the eval itself) with a quick probe, and hand only the prompt-shaped clusters to the iteration loop."
techniques:
  - AG-11
  - OC-11
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - error-analysis
  - failure-clustering
  - eval-results
  - open-coding
  - label-errors
  - fix-prioritization
  - too-many-failures-where-to-start
  - is-it-the-prompt-or-the-model
  - eval-score-low-what-now
updated: "2026-10-03"
related_prompts:
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
  - domain-prompt-engineering/prompt-optimization/llm_ops_eval_driven_prompt_iteration.md
  - domain-AI-ML/model-evaluation-validation/mleval_error_analysis_slicing.md
---

# Eval Failure Clustering and Fix Prioritiser

**Objective:** Read an eval run's failures the way an analyst would — case by case,
then in patterns — and produce a short, ranked list of what to fix, with each item
assigned to the lever that can actually fix it, so prompt edits are spent only on
prompt-shaped problems.

**When to Use:**
- An eval run came back with dozens of failures and the next step is unclear.
- The team keeps editing the prompt and the score does not move.
- You suspect some "failures" are the grader's or the expected answer's fault.
- **Not this prompt if** you have **one** bad output to classify — use
  `domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md` (a fixed
  seven-mode taxonomy per output) or `debug_first_failure_cause_isolator.md`. For slicing
  a classical ML model's errors by feature subgroup, use
  `domain-AI-ML/model-evaluation-validation/mleval_error_analysis_slicing.md`; for an
  agent's loop and tool-call failure modes, `domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md`.
  Once the backlog exists, run the prompt items through
  `llm_ops_eval_driven_prompt_iteration.md`.

## Inputs / Context

1. **The eval run**: inputs, outputs, expected answers or rubric, scores, judge notes.
2. **The prompt and configuration** that produced it (and retrieved context or tool
   calls, for RAG or agent systems).
3. **A sample of passes** (10–20%) for the grader audit.
4. **Production mix**: how often each input type occurs in real traffic, if known.
5. **Severity scale** the product owner accepts (e.g. 3 = harmful or wrong action,
   2 = wrong answer, 1 = format or style).

## Method

1. **Sample.** All failures if there are up to ~100; otherwise a random or stratified
   sample of at least 50–100. Add 10–20% of passes for the audit in step 4.
2. **Open coding.** For each failure, write one line naming the *first* thing that went
   wrong, in your own words, before any category list exists. Later errors are often
   consequences of the first.
3. **Group into clusters (AG-11).** Merge the notes into 5–10 clusters, each with a
   definition and an inclusion rule. Recode every failure against them. If "other"
   exceeds ~10%, split or add a cluster.
4. **Audit the grader and the labels (QA-12).** For each failure: is the expected
   answer wrong, the rubric ambiguous, or the judge mistaken? Those go to a separate
   *eval fix* cluster, not the prompt backlog. On the sampled passes, count false passes
   — a lenient judge hides failures.
5. **Weight (DS-06).** `weight = count × severity × (production share ÷ eval share)`.
   Without production data, use severity only and say so.
6. **Assign a lever with a probe.** For each cluster, run a cheap probe on 5–10 cases:
   paste the needed facts into context (passes → context or retrieval lever); give a
   tool or calculator (passes → tool lever); try a stronger model with the same prompt
   (passes only there → model lever); split the task in two (passes → decomposition);
   rewrite the instruction (passes → prompt lever). Format, examples, and refusal
   criteria are prompt-side levers.
7. **Rank the backlog.** By weight, with the lever, the owner, a one-line hypothesis,
   and the protected cases each fix must not break.
8. **Report by pattern (OC-11).** Clusters, not a list of case IDs; each with two
   representative examples quoted.

## Output Format

```
# Failure analysis — [system] run [id]   Cases [n]   Failures [n]   Sampled [n] (+[n] passes)

## Clusters
| Cluster | Definition | Count | Severity | Prod/eval share | Weight | Lever (probe result) |
Other: [n] ([%])

## Eval fixes (not prompt work)
| Issue | Cases | Fix | Owner |
Judge false-pass rate on sampled passes: [n/n]

## Ranked backlog
| Rank | Cluster | Lever | Owner | Hypothesis | Protected cases |

## Representative examples
[cluster]: [input excerpt] → [output excerpt] → first thing wrong: [..]

## Hand-off
To prompt iteration: [clusters] · to retrieval/tools/model owners: [clusters]
```

## Verification

- [ ] Each failure has an open-coded note naming the first thing that went wrong.
- [ ] Clusters have definitions and inclusion rules; "other" is ≤ ~10%.
- [ ] Counts sum to the number of failures analysed.
- [ ] Grader and label errors are separated and a false-pass rate is reported.
- [ ] Weights show count, severity, and the production adjustment (or its absence).
- [ ] Every cluster's lever is supported by a probe, not by opinion.
- [ ] Only prompt-lever clusters are handed to prompt iteration.

## False-Positive Prevention

1. **Categories before reading.** Starting from a fixed list makes every failure fit
   it. Code first, then cluster.
2. **Blaming the prompt for retrieval.** If the answer was not in the context, no
   wording fixes it. The context probe settles it.
3. **Treating label errors as model errors.** Outdated expected answers and ambiguous
   rubrics are common; fixing the eval can move the score more than any prompt edit.
4. **Counting symptoms twice.** A wrong fact that also breaks the citation is one
   failure, coded by its first cause.
5. **Frequency without severity.** Ten formatting slips can matter less than two
   confidently wrong policy answers.
6. **Eval mix as production mix.** A cluster rare in the eval can dominate real
   traffic; reweight when the shares are known.
7. **A lenient judge.** If sampled passes contain wrong answers, the failure count is
   an undercount; report the false-pass rate beside every number.

## Example Output

```
# Failure analysis — HR policy assistant (RAG) run 2026-09-30   Cases 300   Failures 78   Sampled 78 (+20 passes)

## Clusters
| C1 Outdated policy cited | answer drawn from a superseded document | 19 | 3 | 1.0 | 57 | context/retrieval (18/19 pass with current doc pasted) |
| C2 No location caveat    | jurisdiction-dependent policy answered as universal | 14 | 2 | 2.0 (30% prod vs 15% eval) | 56 | prompt (rewritten rule: 6/7 pass) |
| C3 Citation wrong/missing | cites wrong section or none | 12 | 1 | 1.0 | 12 | prompt/format |
| C4 Over-refusal          | refused an answerable question | 9 | 2 | 1.0 | 18 | prompt (refusal criteria) |
| C5 Leave accrual maths   | arithmetic error in accrual | 7 | 3 | 1.0 | 21 | tool (7/7 pass with calculator) |
| C6 Eval error            | see below | 10 | — | — | — | eval fix |
| C7 Other                 | mixed | 7 | — | — | — | — |
Total 19+14+12+9+7+10+7 = 78 ✓   Other: 7 (9%)

## Eval fixes (not prompt work)
| Expected answers from the 2024 handbook | 6 | update to 2026 handbook | Eval owner |
| Rubric demands citation format the spec does not | 4 | align rubric to spec | Eval owner |
Judge false-pass rate on sampled passes: 2/20 (10%) → failures likely undercounted

## Ranked backlog
| 1 | C1 | retrieval: filter on effective_date | RAG lead | superseded docs excluded | refusal set |
| 2 | C2 | prompt: "state when a policy varies by location" | Prompt owner | caveat added where policy varies | single-location answers stay unqualified |
| 3 | C5 | tool: accrual calculator | Platform | maths delegated | — |
| 4 | C4 | prompt: refusal criteria narrowed | Prompt owner | answerable questions answered | protected refusals |
| 5 | C3 | prompt/format: citation contract | Prompt owner | section IDs required | — |

## Hand-off
To prompt iteration: C2, C4, C3 · to RAG lead: C1 · to platform: C5 · to eval owner: C6
```

## Techniques Used

- **AG-11 Taxonomy-Based Classification Systems** — clusters defined from open-coded notes, with inclusion rules.
- **OC-11 Grouped Reporting by Pattern Type** — findings reported by cluster with representative examples.
- **DS-06 Prioritization and Severity Guidance** — count × severity × production share ranks the backlog.
- **QA-12 False Positives Identification** — grader and label errors removed before blaming the prompt.

## Related Prompts

- `domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md` — classifying a single failed output against a fixed taxonomy.
- `domain-prompt-engineering/prompt-optimization/llm_ops_eval_driven_prompt_iteration.md` — working the prompt-lever clusters round by round.
- `domain-AI-ML/model-evaluation-validation/mleval_error_analysis_slicing.md` — slice-based error analysis for classical ML models.
