---
title: "ML Competition Strategy"
category: AI-ML/learning-ai-ml
description: "Build a disciplined strategy for an ML competition — trustworthy validation, EDA, modeling, ensembling, and leaderboard discipline — that avoids the overfitting traps that sink competitors."
techniques:
  - ST-02
  - DS-02
  - QA-04
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - competition
  - kaggle
  - validation
  - ensembling
  - leaderboard-discipline
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_portfolio_project_designer.md
  - domain-AI-ML/learning-ai-ml/mllearn_study_path_designer.md
  - domain-AI-ML/learning-ai-ml/mllearn_paper_digest_generator.md
---

# ML Competition Strategy

**Objective:** Build a structured strategy for an ML competition that prioritizes a trustworthy local validation scheme, disciplined EDA-to-modeling, sound ensembling, and leaderboard discipline — so the learner climbs on genuine signal rather than overfitting the public leaderboard and collapsing on the private split.

**When to Use:**
- A learner is entering a Kaggle-style competition and wants a plan, not just "train a model."
- Improving competition results that look good on public LB but rank poorly privately.
- Using a competition as a focused learning vehicle for modeling and validation skills.

**When NOT to Use:**
- The goal is a portfolio piece for hiring (use `mllearn_portfolio_project_designer.md`).
- The learner needs a broad study plan (use `mllearn_study_path_designer.md`).

## Inputs / Context

- **The competition** — task type (tabular/CV/NLP), metric, dataset size, public/private split structure.
- **Constraints** — time, compute, team or solo, submission limits.
- **Learner level** — to scope ambition (single strong model vs heavy ensembling).
- **Goal** — learn, medal, or just a respectable finish.

## Constraints

**Must:**
- Establish a trustworthy local cross-validation scheme that matches the competition's split structure (grouped/time/stratified) BEFORE any modeling — this is the single biggest determinant of a good private finish.
- Treat the public leaderboard as a noisy, partial signal; trust local CV over public LB when they disagree.
- Optimize for the exact competition metric, not a convenient proxy.

**Must Not:**
- Tune against the public leaderboard repeatedly (probing) — that overfits the public split and collapses privately.
- Build complex ensembles before a single trustworthy validated model exists.
- Invent expected scores or rankings; reason about approach, and let local CV produce the numbers.

**Instructions:**

1. **Decode the competition.** Restate the task, the exact metric, the dataset structure, and — critically — how the public/private split appears to work. The split structure dictates the validation scheme.

2. **Build a trustworthy CV scheme first.** Choose the validation matching the data (GroupKFold for grouped entities, time-based for temporal, stratified for imbalance). Verify local CV correlates with public LB on a couple of submissions; if it doesn't, fix the CV before anything else.

3. **Run targeted EDA.** Understand the target distribution, leakage risks, key features, and any train/test distribution shift. Let EDA generate hypotheses, not just plots.

4. **Establish a baseline and iterate.** Get a simple validated model submitted early to anchor the metric and confirm the pipeline. Then improve features and model deliberately, measuring each change against local CV.

5. **Engineer features and guard against leakage.** Pursue the feature ideas EDA suggested; check every engineered feature for leakage and for being computable on test the same way (no train/serve-style skew).

6. **Ensemble only on a solid base.** Once you have a few genuinely different strong models (different algorithms/features/seeds), combine them (blending/stacking) validated through the same CV — diversity, not just more models, drives ensemble gains.

7. **Exercise leaderboard discipline.** Limit public-LB probing, choose final submissions by local CV (typically your best CV model + one robust ensemble), and avoid chasing a public-LB jump that local CV doesn't support.

**Output Format:**

A markdown strategy:
- **Competition Decode** — task, metric, split structure.
- **Validation Scheme** — the CV design and the local-vs-public correlation check.
- **EDA Focus** — what to investigate and the leakage risks.
- **Modeling Plan** — baseline → iteration, measured on CV.
- **Feature & Leakage Plan** — feature ideas + leakage guards.
- **Ensembling Plan** — when and how, emphasizing diversity.
- **Leaderboard Discipline** — probing limits + final-submission selection rule.

## Verification

- [ ] A CV scheme matching the split structure is established before modeling.
- [ ] Local CV vs public LB correlation is checked, and CV is trusted over LB on disagreement.
- [ ] Modeling optimizes the exact competition metric.
- [ ] Leakage guards are specified for engineered features.
- [ ] Ensembling follows a solid base and emphasizes model diversity.
- [ ] A final-submission selection rule based on CV (not LB chasing) is stated.

## False-Positive Prevention

❌ **DON'T:**
- Skip validation design and tune by submitting to the public leaderboard.
- Trust a public-LB jump that your local CV doesn't reflect — that's overfitting the public split.
- Stack ten near-identical models and expect an ensemble gain (no diversity, no benefit).
- Optimize a proxy metric (accuracy) when the competition scores something else (e.g., AUC, logloss).

✅ **DO:**
- Build a split-matching CV scheme first and confirm it tracks the public LB.
- Treat the public LB as noisy; let local CV pick your moves and final submissions.
- Ensemble only genuinely diverse strong models, validated through the same CV.
- Optimize exactly the competition metric throughout.

## Example Output

```markdown
## Competition Strategy — Tabular, metric: AUC, grouped by customer, solo, 3 weeks

### Competition Decode
Binary classification, AUC. Each customer has multiple rows; public/private split appears
to be by customer → grouped leakage risk if rows from one customer span folds.

### Validation Scheme
GroupKFold on customer_id (5 folds). After baseline, submit twice to confirm local CV-AUC
tracks public LB. If a feature spikes CV but not LB (or vice versa) → investigate before trusting.

### EDA Focus
Target rate per customer, feature drift train vs test, and any feature that's suspiciously
predictive (possible leakage — check timing).

### Modeling Plan
Baseline: logistic regression on raw features (anchor the pipeline + metric). Then
gradient-boosted trees; measure every change on GroupKFold AUC, not on the LB.

### Feature & Leakage Plan
Aggregate per-customer history features — compute strictly from past rows (no future
leakage). Verify each engineered feature is reproducible on test identically.

### Ensembling Plan
Once GBM + a neural net + a different-feature GBM each validate well and disagree on
different cases, blend by CV-optimized weights. Diversity first.

### Leaderboard Discipline
Cap public-LB probes (it's a fraction of test, noisy). Final 2 submissions: best CV single
model + best CV ensemble — never a high-LB/low-CV gamble.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** decode → validate → EDA → model → ensemble → discipline.
- **DS-02 (Metric Specification):** optimize the exact competition metric; CV defined precisely.
- **QA-04 (Overfitting/Validity Check):** CV-vs-LB discipline guards against public-split overfitting.
- **RT-05 (Evidence-Based Reasoning):** moves driven by local CV evidence, not LB noise.
- **DS-06 (Prioritization & Severity Guidance):** validation-first sequencing of effort.

**Related Prompts:**
- `mllearn_portfolio_project_designer.md` — turn a competition into a portfolio narrative.
- `mllearn_study_path_designer.md` — where competition practice fits in a learning plan.
- `mllearn_paper_digest_generator.md` — digest a technique paper a competition inspires.
