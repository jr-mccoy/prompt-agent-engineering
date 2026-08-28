---
title: "ML Paper Reading Guide"
category: AI-ML/learning-ai-ml
description: "Guide a structured, critical read of an ML paper — what to extract, in what order, and how to interrogate claims — building the learner's ability to read papers independently."
techniques:
  - ED-01
  - ED-03
  - ST-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - paper-reading
  - critical-reading
  - research-skills
  - scaffolding
  - method
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_paper_digest_generator.md
  - domain-AI-ML/learning-ai-ml/mllearn_reproduce_paper_plan.md
  - domain-AI-ML/learning-ai-ml/mllearn_concept_explainer.md
---

# ML Paper Reading Guide

**Objective:** Teach a learner to read an ML paper efficiently and critically — by guiding them through a staged reading order, telling them what to extract at each stage and what questions to ask — so they build the durable skill of reading papers independently, not just understanding one paper.

**When to Use:**
- A learner is intimidated by or inefficient at reading research papers.
- Building the skill of critically evaluating ML literature.
- Preparing to read a specific paper and wanting a method, not just a summary.

**When NOT to Use:**
- The learner wants the paper summarized for them (use `mllearn_paper_digest_generator.md`).
- They want to reproduce the paper's results (use `mllearn_reproduce_paper_plan.md`).

## Inputs / Context

- **The paper** (title/topic, or the paper itself) and why the learner is reading it.
- **Learner level** — first papers vs experienced; familiarity with the subfield.
- **Goal** — understand the method, evaluate the claims, find a baseline, prep a presentation.
- **Time budget** — a triage skim vs a deep read.

## Constraints

**Must:**
- Teach the reading *method* (staged passes, what to extract, what to question) — the learner does the reading; the guide coaches.
- Adapt the depth of guidance to the learner's level and the stated goal/time budget.
- Build critical-reading habits: every claim is read against its evidence, baselines, and limitations.

**Must Not:**
- Read the paper *for* the learner or hand them a finished summary — that defeats the skill-building purpose (that's the digest prompt's job).
- Encourage uncritical acceptance — train the learner to ask where results could be misleading (cherry-picked baselines, no ablation, weak significance).
- Assume subfield knowledge; offer to clarify prerequisite concepts when the learner needs them.

**Instructions:**

1. **Set the reading goal and strategy.** Clarify why the learner is reading this and how deep to go. Recommend a multi-pass strategy (skim for structure → targeted read → deep read) sized to the time budget.

2. **Coach the triage pass.** Guide the learner to read title, abstract, figures, and conclusions first, and to write the paper's claimed contribution in their own words. Ask them to predict what the method must do.

3. **Coach the structure pass.** Direct attention to the problem setup, the core method, and the main results table — and prompt the learner to identify the baselines and the headline metric before reading the prose.

4. **Coach the critical pass.** Have the learner interrogate: Is the baseline fair and strong? Are there ablations isolating what actually helps? Are results significant or single-run? What do the authors admit in limitations? Where might the result not transfer?

5. **Coach extraction.** Guide the learner to record the contribution, the method in 3–5 sentences, the key result with its baseline, the limitations, and its relevance to their work — in their own words.

6. **Surface confusions as learning.** When the learner is stuck on a concept, point them to (or briefly explain) the prerequisite, rather than glossing over it.

7. **Reflect on the read.** Prompt the learner to state what they'd still want to verify, whether they believe the central claim and why, and one question they'd ask the authors.

**Output Format:**

A markdown coaching guide:
- **Your Reading Goal & Strategy** — passes sized to the budget.
- **Pass 1: Triage** — what to read, what to extract, a prediction to make.
- **Pass 2: Structure** — what to read, the baseline/metric to find first.
- **Pass 3: Critical** — the interrogation questions to apply.
- **Extraction Template** — fields for the learner to fill in their own words.
- **Reflection Prompts** — belief in the claim, open questions, one question for the authors.

## Verification

- [ ] The guide coaches a reading method; it does not summarize the paper for the learner.
- [ ] Guidance depth matches the learner's level and time budget.
- [ ] Critical-reading questions (baselines, ablations, significance, limitations) are included.
- [ ] Extraction asks the learner to write in their own words.
- [ ] Prerequisite confusions are handled by pointing/explaining, not skipping.

## False-Positive Prevention

❌ **DON'T:**
- Produce the paper's summary and call it a reading guide — that removes the skill being built.
- Let the learner accept the headline result without checking the baseline's strength.
- Treat a single-run improvement as a robust result.
- Skip over a concept the learner doesn't grasp, leaving a hole in their reading.

✅ **DO:**
- Coach the passes and the questions; keep the learner doing the reading.
- Train the habit of finding and judging the baseline before trusting the gain.
- Push for ablation/significance scrutiny on every headline claim.
- Pause to shore up a missing prerequisite so the read is genuine.

## Example Output

```markdown
## Reading Guide — "[Attention-based method] for [task]" (level: 2nd-year, goal: understand method, ~90 min)

### Your Reading Goal & Strategy
Goal: understand the method well enough to explain it. Three passes: 10-min triage,
40-min structure, 40-min critical.

### Pass 1: Triage (10 min)
Read abstract, all figures + captions, conclusion. Then write — in your own words —
"What do the authors claim is new?" Predict: what must their method DO to achieve that?

### Pass 2: Structure (40 min)
Read problem setup + method section. BEFORE reading the results prose, find the main
results table: What are the baselines? What's the headline metric? Note the numbers yourself.

### Pass 3: Critical (40 min)
Ask: Is the strongest existing method used as a baseline, or a weak one? Is there an
ablation showing WHICH part of the method helps? Single run or multiple seeds / CIs?
What do the Limitations say — and what do they NOT admit?

### Extraction Template (fill in your words)
- Contribution: ___  - Method in 3–5 sentences: ___  - Key result + its baseline: ___
- Limitations (theirs + yours): ___  - Relevance to my work: ___

### Reflection Prompts
Do you believe the central claim? Why / why not? What would you still verify? What's
the one question you'd ask the authors?
```

**Techniques Used:**
- **ED-01 (Iterative Scaffolding):** staged passes scaffold the reading skill.
- **ED-03 (Guided Discovery):** the learner predicts, finds, and judges rather than being told.
- **ST-02 (Structured Sequential Instructions):** fixed triage → structure → critical sequence.
- **RT-05 (Evidence-Based Reasoning):** claims read against baselines and evidence.
- **QA-01 (Self-Verification):** reflection prompts make the learner check their own belief.

**Related Prompts:**
- `mllearn_paper_digest_generator.md` — when a structured summary (not skill-building) is wanted.
- `mllearn_reproduce_paper_plan.md` — the next step after a critical read.
- `mllearn_concept_explainer.md` — to shore up a prerequisite the paper assumes.
