---
title: "Reproduce-a-Paper Plan"
category: AI-ML/learning-ai-ml
description: "Plan a faithful reproduction of an ML paper — scoping what to reproduce, surfacing ambiguities, defining baselines and success criteria, and budgeting realistically."
techniques:
  - ST-02
  - CM-02
  - DS-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - reproduction
  - research-skills
  - baselines
  - success-criteria
  - rigor
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_paper_digest_generator.md
  - domain-AI-ML/learning-ai-ml/mllearn_paper_reading_guide.md
  - domain-AI-ML/learning-ai-ml/mllearn_portfolio_project_designer.md
---

# Reproduce-a-Paper Plan

**Objective:** Produce a concrete plan to reproduce an ML paper's central result — defining the scope, cataloguing the ambiguities and missing details that will bite, specifying baselines and a success criterion for "reproduced," and budgeting effort/compute realistically — so the reproduction is rigorous and the learner knows in advance where it might diverge.

**When to Use:**
- A learner wants to reproduce a paper to deepen understanding or validate a result.
- Building a portfolio piece or a baseline for new research.
- Assessing whether a published result is trustworthy before building on it.

**When NOT to Use:**
- You just want the paper summarized (use `mllearn_paper_digest_generator.md`).
- You're designing a general portfolio project, not a reproduction (use `mllearn_portfolio_project_designer.md`).

## Inputs / Context

- **The paper** — its method and the specific result to reproduce (provide content/digest, not just title).
- **Available resources** — compute budget, time, datasets accessible, code released (if any).
- **Learner level** — to scope ambition and the amount of scaffolding.
- **Purpose** — understanding, validation, baseline for new work, portfolio.

## Constraints

**Must:**
- Define precisely WHICH result is being reproduced and what numeric tolerance counts as "reproduced" (exact match is rarely realistic).
- Catalogue the under-specified details the paper omits (hyperparameters, seeds, preprocessing, exact data splits) as explicit risks with a plan to resolve each.
- Specify the baselines that must also be implemented to make the comparison meaningful.

**Must Not:**
- Assume the result will reproduce exactly; plan for and document divergence.
- Invent the paper's missing hyperparameters as if known — list them as ambiguities to sweep or infer, not as facts.
- Scope a full-paper reproduction when one core result is the right, achievable target.

**Instructions:**

1. **Pin the reproduction target.** State the single central result (a number in a specific table/figure) to reproduce, and why it's the right target. Reproducing one headline result well beats reproducing everything poorly.

2. **Define "reproduced."** Set a success criterion: the metric, the tolerance band (e.g., within ±X of reported, accounting for seed variance), and how many seeds you'll run to judge it.

3. **Inventory what's specified vs missing.** Catalogue the method details: clearly given, partially given, and absent (common gaps: LR schedule, weight init, exact preprocessing, data split seeds, early-stopping rule). Each absence is a risk.

4. **Plan to resolve ambiguities.** For each missing detail, choose a strategy: use released code, infer from convention, sweep a small grid, or contact authors. Mark assumptions that will affect the result.

5. **Specify baselines and data.** Identify the baselines that must be reimplemented (or sourced) for the comparison to mean anything, and confirm dataset access and exact splits.

6. **Budget effort and compute.** Estimate the work in phases (data → method → baseline → tuning → evaluation) and the compute, as ranges. Flag if the reported result implies a compute budget the learner can't match (and how to scale down honestly).

7. **Define the divergence protocol.** Decide in advance how you'll diagnose a failure to reproduce (is it a bug, a missing detail, or a genuine non-reproduction?) and how you'll report it.

**Output Format:**

A markdown plan:
- **Reproduction Target** — the exact result + why.
- **Success Criterion** — metric, tolerance, seed count.
- **Specification Inventory** — table: Detail | Given/Partial/Missing | Resolution strategy.
- **Baselines & Data** — what must be reimplemented; data/splits confirmed.
- **Phased Plan & Budget** — phases, effort/compute ranges.
- **Divergence Protocol** — how to diagnose and report a non-reproduction.

## Verification

- [ ] A single, specific reproduction target is named.
- [ ] "Reproduced" is defined with a metric, tolerance, and seed count.
- [ ] Missing/under-specified details are catalogued with resolution strategies.
- [ ] Required baselines and exact data splits are specified.
- [ ] A divergence protocol exists; exact-match reproduction is not assumed.

## False-Positive Prevention

❌ **DON'T:**
- Plan to "reproduce the paper" without naming the one result that matters.
- Assume your single run matching the reported number means success — seed variance is real.
- Treat the paper's omitted hyperparameters as if you know them.
- Skip reimplementing the baseline and compare against a number you can't recompute.

✅ **DO:**
- Target one headline result with a tolerance band and multiple seeds.
- Catalogue every missing detail as a risk with a resolution plan.
- Reimplement (or carefully source) the baselines so the comparison is honest.
- Pre-commit to a protocol for diagnosing whether a miss is a bug or a non-reproduction.

## Example Output

```markdown
## Reproduce-a-Paper Plan — "[Method]" Table 2, row "ours @ DatasetA"

### Reproduction Target
Table 2: 88.1 F1 on DatasetA with the proposed method. It's the paper's central claim;
the ablations depend on it.

### Success Criterion
Reproduced = mean F1 within ±0.7 of 88.1 over 5 seeds (paper reports ±0.4 over 5 seeds).
A single run within range is necessary but not sufficient.

### Specification Inventory
| Detail | Status | Resolution |
|---|---|---|
| Architecture | Given | Implement as described |
| LR schedule | Partial (mentions "cosine") | Assume cosine + warmup; sweep warmup len |
| Weight init | Missing | Use framework default; note as assumption |
| Data preprocessing | Partial | Infer from released code if available, else convention |
| Train/val/test split | Given (seed not given) | Use stated ratios; sweep 3 split seeds |

### Baselines & Data
Reimplement the strong supervised baseline (84.3) — the gain is only meaningful relative
to it. DatasetA is public; confirm the exact version/split.

### Phased Plan & Budget
Data+pipeline (1 wk) → method (1–2 wk) → baseline (3–5 d) → tuning/seeds (1 wk, GPU-bound).
Compute: ~5 seeds × method + baseline; fits 1 mid-range GPU over ~3 weeks. If the paper
implies more compute, scale model/data down and report the adjusted target.

### Divergence Protocol
If F1 lands low: first verify the baseline reproduces (isolates pipeline bugs), then sweep
the assumed details (LR warmup, init). If still off after the sweep, report as a probable
non-reproduction with the specific gap, not as "my bug, probably."
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** target → criterion → inventory → baselines → budget.
- **CM-02 (Constraint Specification):** success defined as a tolerance band, not exact match.
- **DS-02 (Metric Specification):** metric, tolerance, and seed count specified up front.
- **RT-05 (Evidence-Based Reasoning):** missing details treated as risks, not assumed facts.
- **QA-01 (Self-Verification):** the divergence protocol is a built-in self-check.

**Related Prompts:**
- `mllearn_paper_digest_generator.md` — digest the paper before planning the reproduction.
- `mllearn_paper_reading_guide.md` — critically read it first to find the ambiguities.
- `mllearn_portfolio_project_designer.md` — turn the reproduction into a portfolio piece.
