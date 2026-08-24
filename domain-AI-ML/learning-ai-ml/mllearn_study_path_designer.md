---
title: "ML/AI Study Path Designer"
category: AI-ML/learning-ai-ml
description: "Design a personalized ML/AI study path for a stated goal, current level, and time budget — sequencing prerequisites and projects with checkpoints, not just listing courses."
techniques:
  - ED-01
  - ST-02
  - DS-06
  - RP-01
  - CM-02
difficulty: intermediate
tags:
  - study-plan
  - learning-path
  - sequencing
  - prerequisites
  - personalized
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_portfolio_project_designer.md
  - domain-AI-ML/learning-ai-ml/mllearn_concept_explainer.md
  - domain-AI-ML/learning-ai-ml/mllearn_glossary_builder.md
---

# ML/AI Study Path Designer

**Objective:** Design a personalized, sequenced ML/AI study path for a specific goal, honest current level, and realistic time budget — ordering topics by prerequisite dependency, interleaving projects to cement learning, and inserting checkpoints — so the learner has a path that fits their life and proves progress, not a generic course dump.

**When to Use:**
- A learner wants to learn ML/AI toward a concrete goal but doesn't know what to study in what order.
- An existing plan is a disorganized list with no sequencing or checkpoints.
- Pivoting into ML from an adjacent background and needing a calibrated bridge.

**When NOT to Use:**
- The learner wants one project designed (use `mllearn_portfolio_project_designer.md`).
- They need a single concept explained (use `mllearn_concept_explainer.md`).

## Inputs / Context

- **Goal** — be specific (e.g., "land an ML engineer role," "build a recsys for my app," "understand transformers deeply").
- **Current level** — honest math/coding/ML background; what they can already do.
- **Time budget** — hours/week and target horizon.
- **Constraints/preferences** — learning style, theory vs applied bias, resources available.

## Constraints

**Must:**
- Sequence topics by prerequisite dependency — don't schedule deep learning before the math/ML foundations it needs.
- Tailor scope and pace to the stated level and time budget; a realistic path beats an ambitious one that gets abandoned.
- Interleave hands-on projects and checkpoints so learning is applied and progress is verifiable, not just consumed.

**Must Not:**
- Dump a generic "learn Python → stats → ML → DL" list with no personalization to goal/level/time.
- Recommend an unrealistic pace for the stated time budget, or skip prerequisites to reach exciting topics faster.
- Over-index on courses/videos; balance with doing (projects, exercises) since passive consumption rarely produces skill.

**Instructions:**

1. **Clarify the goal and "done."** Restate the concrete goal and what reaching it looks like (a job-ready skill set, a shipped project, exam readiness). The whole path is reverse-engineered from this.

2. **Assess the starting point.** Map current strengths and gaps against what the goal requires. Be candid about prerequisite gaps (math, programming, ML basics) — these set the entry point.

3. **Derive the topic dependency graph.** List the topics the goal requires and order them by prerequisite (e.g., linear algebra + probability → classical ML → neural nets → the goal-specific area). Mark what can be skipped given the learner's background.

4. **Phase the path to the time budget.** Break into phases sized to weeks-at-the-stated-pace. Each phase: topics, a concrete project/exercise, and a checkpoint that proves the phase landed.

5. **Interleave doing with learning.** For each phase, pair study with a small build/exercise so concepts are applied immediately, and recall is practiced.

6. **Insert checkpoints and adjust-points.** Define how the learner verifies each phase (can implement X, can explain Y, project Z works) and where to re-plan if a phase takes longer.

7. **Right-size resources.** Recommend a small number of high-quality resources per phase (not an overwhelming list), matched to the learner's style and the topic.

**Output Format:**

A markdown study path:
- **Goal & Definition of Done** — the concrete target.
- **Starting Point** — strengths, gaps, entry point.
- **Topic Dependency Order** — sequenced, with skippables marked.
- **Phased Plan** — table per phase: Weeks | Topics | Project/Exercise | Checkpoint.
- **Resources** — a few high-quality picks per phase.
- **Adjust-Points** — where/how to re-plan if pace slips.

## Verification

- [ ] Topics are ordered by prerequisite dependency, not by appeal.
- [ ] Pace and scope fit the stated hours/week and horizon.
- [ ] Each phase pairs study with a concrete project/exercise and a checkpoint.
- [ ] Prerequisite gaps set the entry point; nothing skipped to rush to flashy topics.
- [ ] Resource lists are curated and small, not overwhelming.

## False-Positive Prevention

❌ **DON'T:**
- Hand over a generic roadmap identical regardless of the learner's goal or background.
- Schedule transformers in week 2 for someone without the linear-algebra/ML foundations.
- Plan 30 hours/week of content for someone with 5.
- Fill the path with courses and no building, producing tutorial-watchers who can't ship.

✅ **DO:**
- Reverse-engineer the path from the specific goal and definition of done.
- Let honest prerequisite gaps set the entry point and the order.
- Match weekly load to the real time budget; under-promise and let them accelerate.
- Pair every phase with a build and a checkpoint that proves the skill.

## Example Output

```markdown
## Study Path — Goal: "Become job-ready as an ML engineer" (level: SWE, weak stats; 10 hrs/wk; 6 mo)

### Goal & Definition of Done
Can build, evaluate, and deploy an ML model end-to-end; can pass concept + system-design
rounds; has 2 portfolio projects.

### Starting Point
Strong: Python, software engineering, APIs. Gaps: probability/stats, ML fundamentals, ML
eval rigor. Entry point: stats refresher + classical ML (skip "learn to code").

### Topic Dependency Order
prob/stats → classical ML (regression, trees, eval) → feature eng + leakage → neural nets
basics → one specialization (NLP or recsys) → serving/MLOps. (Skip: intro programming.)

### Phased Plan
| Weeks | Topics | Project | Checkpoint |
|---|---|---|---|
| 1–3 | Prob/stats for ML | Stats exercises on a real dataset | Explain bias-variance, CI |
| 4–8 | Classical ML + eval | Build+evaluate a classifier, no leakage | Clean CV, beats baseline |
| 9–13 | Feature eng + MLOps basics | Deploy the classifier as an API + monitor | Model served + monitored |
| 14–20 | Specialization (recsys) | Build a recommender end-to-end | Portfolio project #1 |
| 21–26 | System design + interview prep | Reproduce a small paper | Mock interviews + project #2 |

### Resources
A few curated picks per phase (one solid course + one applied tutorial), not a 40-link list.

### Adjust-Points
If the stats phase runs long, extend it — don't proceed to ML without it. Re-check pace
at week 8 and week 14.
```

**Techniques Used:**
- **ED-01 (Iterative Scaffolding):** phases build prerequisite-by-prerequisite.
- **ST-02 (Structured Sequential Instructions):** goal → starting point → dependency order → phases.
- **DS-06 (Prioritization & Severity Guidance):** dependency-driven topic sequencing.
- **RP-01 (Audience/Level Adaptation):** scope and pace tuned to level and time budget.
- **CM-02 (Constraint Specification):** time budget and prerequisites as hard constraints.

**Related Prompts:**
- `mllearn_portfolio_project_designer.md` — design the projects this path schedules.
- `mllearn_concept_explainer.md` — explain a topic the path introduces.
- `mllearn_glossary_builder.md` — build a glossary alongside the path.
