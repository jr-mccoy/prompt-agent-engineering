---
title: "Computer Vision Specialization Study Track"
category: AI-ML/learning-ai-ml/study-tracks
description: "An instantiated, phased computer-vision curriculum — image classification → detection/segmentation → modern architectures → deployment — with prerequisite gates, a build per phase, and checkpoints the learner can demonstrate."
techniques:
  - ED-01
  - ST-02
  - DS-06
  - RP-01
  - CM-02
difficulty: intermediate
tags:
  - computer-vision
  - study-track
  - curriculum
  - specialization
  - sequencing
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_study_path_designer.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/learning-ai-ml/mllearn_portfolio_project_designer.md
---

# Computer Vision Specialization Study Track

**Objective:** Give a learner a concrete, phased computer-vision curriculum — sequenced by prerequisite, anchored to a build and a demonstrable checkpoint per phase, and tuned to their honest starting level and weekly hours — so they reach working CV competence (train, evaluate, and deploy a vision model end-to-end) instead of accumulating disconnected tutorials.

**When to Use:**
- A learner with ML basics wants to specialize in computer vision and needs the order, not just the topics.
- An existing CV plan is a link dump with no sequencing, builds, or checkpoints.
- Bridging into CV from adjacent ML/SWE work and needing a calibrated entry point.

**When NOT to Use:**
- The learner needs a generic, any-goal study path generator (use `mllearn_study_path_designer.md`).
- They want one CV project designed, not a curriculum (use `mllearn_portfolio_project_designer.md`).
- They lack ML/math foundations entirely — fix that first via a general study path.

## Inputs / Context

- **Current level** — honest math (linear algebra, calculus, probability), Python/ML, and any prior CV exposure.
- **Goal** — be specific (e.g., "ship a defect-detection model," "land a CV engineer role," "understand modern vision architectures").
- **Time budget** — hours/week and target horizon.
- **Compute access** — local GPU, cloud, or CPU-only (this constrains which builds are realistic).
- **Theory vs applied bias** — how much derivation the learner wants vs shipping.

## Constraints

**Must:**
- Sequence phases by prerequisite dependency — classification fundamentals before detection/segmentation before modern transformer-based vision.
- Pair every phase with a concrete build on a real dataset and a checkpoint the learner can demonstrate, not just consume.
- Make evaluation rigor (correct metric per task — accuracy vs mAP vs IoU, a baseline, no leakage) an explicit, recurring deliverable.

**Must Not:**
- Invent specific course names, book titles, author names, paper accuracy figures, or "best model" claims from memory — describe the *type* of resource and direct the learner to verify the current canonical one.
- Schedule advanced architectures before the learner can train and honestly evaluate a basic classifier.
- Recommend a pace that ignores the stated hours/week or a build that ignores the stated compute.

**Instructions:**

1. **Pin the goal and "done."** Restate the concrete CV goal and what reaching it looks like (a deployed model, a portfolio of CV projects, role-readiness). Reverse-engineer the track from this.

2. **Assess the entry point.** Map current math/ML/CV strengths and gaps. Name the prerequisite gaps that set where the track starts (e.g., "comfortable with CNNs already → skip to detection").

3. **Lay out the phase dependency order.** Present the CV topic sequence — image data + augmentation → classification/transfer learning → object detection → segmentation → modern architectures (ViT etc.) → deployment/serving — and mark what the learner can skip given their background.

4. **Phase to the time budget.** Size each phase in weeks at the stated pace. Each phase lists: topics, a build on a real/public dataset, the correct evaluation metric, and a checkpoint.

5. **Make evaluation a deliverable each phase.** Specify the right metric per task and require a baseline + a leakage check (e.g., no near-duplicate images across train/test, no test-set augmentation tuning).

6. **Insert checkpoints and adjust-points.** Define how the learner proves each phase landed (can train X to beat baseline, can compute mAP correctly) and where to re-plan if a phase runs long.

7. **Right-size resources.** Recommend a small number of resource *types* per phase (one structured course + one hands-on tutorial + one canonical paper to read), not an overwhelming list.

**Output Format:**

A markdown study track:
- **Goal & Definition of Done** — the concrete target.
- **Entry Point** — strengths, gaps, where the track starts.
- **Phase Dependency Order** — sequenced, skippables marked.
- **Phased Plan** — table per phase: Weeks | Topics | Build (dataset) | Metric + baseline | Checkpoint.
- **Evaluation Discipline** — the metric-per-task + leakage checks that recur.
- **Resources** — a few resource *types* per phase (verify current canonical picks).
- **Adjust-Points** — where to re-plan if pace slips.

## Verification

- [ ] Phases are ordered by prerequisite dependency, not appeal.
- [ ] Every phase has a build on real data, the correct metric, a baseline, and a checkpoint.
- [ ] Pace and builds fit the stated hours/week and compute.
- [ ] Leakage and metric-mismatch are addressed as recurring checks.
- [ ] No invented course/book/paper names or accuracy figures — resource *types* only.

## False-Positive Prevention

❌ **DON'T:**
- Hand over a generic CV roadmap identical regardless of goal, level, or compute.
- Schedule object detection or ViTs before the learner can train and evaluate a classifier.
- Cite specific accuracy numbers or "the best model is X" from memory.
- Fill the track with courses and papers and no building.
- Let the learner report accuracy on a detection task or ignore train/test image leakage.

✅ **DO:**
- Reverse-engineer the phases from the specific goal and definition of done.
- Gate each phase behind a checkpoint the learner can demonstrate.
- Describe resource *types*; tell the learner to verify the current canonical resource.
- Pair every phase with a build and the correct evaluation metric + baseline.
- Make a leakage check part of every phase that trains a model.

## Example Output

```markdown
## CV Study Track — Goal: "Become a job-ready CV engineer" (level: ML basics, weak on detection; 8 hrs/wk; cloud GPU; 5 mo)

### Goal & Definition of Done
Can train, evaluate (correct metric, baseline, no leakage), and deploy a classification AND a
detection model; has 2 CV portfolio projects; can read a modern vision paper.

### Entry Point
Strong: Python, CNN basics, can train a classifier. Gaps: detection/segmentation, modern
architectures, deployment. Start at Phase 2 (skip image-data/classification fundamentals).

### Phase Dependency Order
image data + augmentation → classification/transfer learning → object detection → segmentation
→ modern architectures (ViT) → deployment. (Skip: phases 0–1 given background.)

### Phased Plan
| Weeks | Topics | Build (dataset) | Metric + baseline | Checkpoint |
|---|---|---|---|---|
| 1–2 | Transfer learning, augmentation done right | Fine-tune a classifier on a public dataset | Top-1 acc vs from-scratch baseline | Beats baseline; no train/test image leakage |
| 3–6 | Object detection | Train a detector on a public detection set | mAP@IoU vs naive baseline | Computes mAP correctly; portfolio project #1 |
| 7–9 | Segmentation | Semantic seg on a public set | mIoU vs threshold baseline | Reports IoU per class |
| 10–13 | Modern architectures (ViT) | Compare a CNN vs a transformer backbone | Same metric, matched compute | Explains the tradeoff with evidence |
| 14–20 | Deployment | Serve the detector behind an API | Latency + correctness smoke test | Model served; portfolio project #2 |

### Evaluation Discipline
Classification → top-1/k + a baseline. Detection → mAP@IoU (never accuracy). Segmentation →
mIoU. Every phase: check for near-duplicate images across splits; never tune on the test set.

### Resources
Per phase: one structured course (verify current canonical), one hands-on tutorial, one
landmark paper to read critically. Not a 30-link list.

### Adjust-Points
If detection runs long, extend it — don't move to ViTs without a working detector. Re-check
pace at weeks 6 and 13.
```

**Techniques Used:**
- **ED-01 (Iterative Scaffolding):** phases build prerequisite-by-prerequisite toward CV competence.
- **ST-02 (Structured Sequential Instructions):** goal → entry point → dependency order → phases.
- **DS-06 (Prioritization & Severity Guidance):** dependency-driven topic sequencing; skippables marked.
- **RP-01 (Audience/Level Adaptation):** scope, pace, and builds tuned to level, time, and compute.
- **CM-02 (Constraint Specification):** time budget, compute, and prerequisites as hard constraints.

**Related Prompts:**
- `mllearn_study_path_designer.md` — the generic generator this track instantiates for CV.
- `cv_task_framing.md` — frame the specific CV task each build targets.
- `mllearn_portfolio_project_designer.md` — design the CV projects this track schedules.
