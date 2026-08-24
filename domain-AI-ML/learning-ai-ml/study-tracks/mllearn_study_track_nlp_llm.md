---
title: "NLP / LLM Specialization Study Track"
category: AI-ML/learning-ai-ml/study-tracks
description: "An instantiated, phased NLP→LLM curriculum — text representation → transformers → fine-tuning → RAG/evaluation — with prerequisite gates, a build per phase, and checkpoints the learner can demonstrate."
techniques:
  - ED-01
  - ST-02
  - DS-06
  - RP-01
  - CM-02
difficulty: intermediate
tags:
  - nlp
  - llm
  - study-track
  - curriculum
  - specialization
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_study_path_designer.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
  - domain-AI-ML/learning-ai-ml/paper-reproductions/README.md
---

# NLP / LLM Specialization Study Track

**Objective:** Give a learner a concrete, phased NLP-to-LLM curriculum — sequenced by prerequisite, anchored to a build and a demonstrable checkpoint per phase, and tuned to their honest starting level and weekly hours — so they reach working LLM-application competence (build, evaluate, and ground an LLM system end-to-end) instead of jumping straight to prompting frameworks without the foundations.

**When to Use:**
- A learner with ML basics wants to specialize in NLP/LLMs and needs the order, not just topics.
- An existing plan skips text fundamentals and starts at "call an API," leaving evaluation gaps.
- Bridging into NLP/LLMs from adjacent ML/SWE work and needing a calibrated entry point.

**When NOT to Use:**
- The learner needs a generic, any-goal study path generator (use `mllearn_study_path_designer.md`).
- They want one LLM system designed, not a curriculum (use `genai_rag_system_design.md`).
- They lack ML/programming foundations entirely — fix that via a general study path first.

## Inputs / Context

- **Current level** — honest math/ML, Python, and any prior NLP/LLM exposure.
- **Goal** — be specific (e.g., "build a RAG assistant for my docs," "land an LLM/AI engineer role," "understand transformers deeply").
- **Time budget** — hours/week and target horizon.
- **Compute/API access** — local GPU, cloud, or hosted-API-only (constrains fine-tuning vs prompting builds).
- **Theory vs applied bias** — how much architecture detail vs shipping.

## Constraints

**Must:**
- Sequence phases by prerequisite — text representation and classical NLP before transformers before fine-tuning before RAG/agentic applications.
- Pair every phase with a build and a checkpoint, and make **evaluation** (a rubric or metric, not vibes) an explicit deliverable — LLM outputs are easy to fool yourself about.
- Treat grounding, hallucination, and eval as first-class topics, not afterthoughts.

**Must Not:**
- Invent specific course names, book titles, model benchmark numbers, or "best model" claims from memory — describe the resource *type* and direct the learner to verify the current one.
- Schedule fine-tuning or RAG before the learner understands tokenization, embeddings, and transformer basics.
- Let "it looks good" substitute for an evaluation method on any LLM build.

**Instructions:**

1. **Pin the goal and "done."** Restate the concrete NLP/LLM goal and what reaching it looks like. Reverse-engineer the track from this.

2. **Assess the entry point.** Map current math/ML/NLP strengths and gaps; name the prerequisite gaps that set where the track starts.

3. **Lay out the phase dependency order.** Present the sequence — text preprocessing/representation → classical NLP (classification, embeddings) → transformer architecture → fine-tuning vs prompting → RAG + retrieval → evaluation/guardrails — marking skippables.

4. **Phase to the time budget.** Size phases in weeks at the stated pace. Each phase: topics, a build, an evaluation method, and a checkpoint.

5. **Make evaluation a deliverable each phase.** Specify how the learner will judge quality (classification metric + baseline for early phases; a rubric / LLM-as-judge with human spot-checks + adversarial cases for LLM phases).

6. **Insert checkpoints and adjust-points.** Define how each phase is proven and where to re-plan if it runs long.

7. **Right-size resources.** Recommend a small number of resource *types* per phase (one structured course + one hands-on build tutorial + one canonical paper), not a long list.

**Output Format:**

A markdown study track:
- **Goal & Definition of Done** — the concrete target.
- **Entry Point** — strengths, gaps, where the track starts.
- **Phase Dependency Order** — sequenced, skippables marked.
- **Phased Plan** — table per phase: Weeks | Topics | Build | Evaluation method | Checkpoint.
- **Evaluation Discipline** — the recurring rubric/metric + grounding/hallucination checks.
- **Resources** — a few resource *types* per phase (verify current canonical picks).
- **Adjust-Points** — where to re-plan if pace slips.

## Verification

- [ ] Phases are ordered by prerequisite dependency (representation → transformers → fine-tune → RAG).
- [ ] Every phase has a build, an explicit evaluation method, and a checkpoint.
- [ ] LLM phases use a rubric/metric with human spot-checks, not "looks good."
- [ ] Pace and builds fit the stated hours/week and compute/API access.
- [ ] No invented course/book/benchmark names — resource *types* only.

## False-Positive Prevention

❌ **DON'T:**
- Start the track at "call the API" and skip tokenization/embeddings/transformer basics.
- Accept "the output looks great" as evaluation on any LLM build.
- Cite specific model benchmark numbers or "the best model is X" from memory.
- Fill the track with reading and no building.
- Treat RAG as just "stuff documents in the prompt" without a retrieval-quality eval.

✅ **DO:**
- Build the foundations before fine-tuning and RAG.
- Require an evaluation method (rubric/metric + human spot-check + adversarial cases) per LLM phase.
- Describe resource *types*; tell the learner to verify the current canonical resource.
- Pair every phase with a build and a checkpoint.
- Make grounding and hallucination checks explicit in the RAG phase.

## Example Output

```markdown
## NLP/LLM Study Track — Goal: "Build a grounded RAG assistant + be LLM-engineer-ready" (level: ML basics, no NLP; 10 hrs/wk; hosted API + small GPU; 5 mo)

### Goal & Definition of Done
Can build and evaluate a RAG system with a retrieval-quality eval and an answer-quality rubric;
understands transformers well enough to read a paper; has 1–2 NLP/LLM portfolio projects.

### Entry Point
Strong: Python, ML basics. Gaps: all NLP. Start at Phase 1 (text representation).

### Phase Dependency Order
text preprocessing/representation → classical NLP (classification, embeddings) → transformer
architecture → fine-tuning vs prompting → RAG + retrieval → evaluation/guardrails.

### Phased Plan
| Weeks | Topics | Build | Evaluation method | Checkpoint |
|---|---|---|---|---|
| 1–3 | Tokenization, embeddings, text classification | Train a text classifier | Macro-F1 vs majority baseline | Beats baseline; no leakage |
| 4–6 | Transformer architecture | Reproduce a small attention model | Loss curve + sanity task | Explains attention from the build |
| 7–9 | Fine-tuning vs prompting | Fine-tune (or PEFT) on a small task | Task metric vs prompted baseline | States when fine-tune is worth it |
| 10–14 | RAG + retrieval | Build a RAG assistant on real docs | Retrieval recall@k + answer rubric | Grounded answers; project #1 |
| 15–20 | Evaluation + guardrails | Add an eval harness + safety checks | LLM-as-judge + human spot-check + adversarial set | Eval catches regressions; project #2 |

### Evaluation Discipline
Early phases: metric + baseline + leakage check. LLM phases: a rubric, LLM-as-judge anchored by
human spot-checks, and an adversarial case set. RAG: separate retrieval-quality from answer-quality.

### Resources
Per phase: one structured course (verify current canonical), one hands-on build tutorial, one
landmark paper to read critically (see the paper-reproductions series).

### Adjust-Points
If transformers don't click, extend that phase — don't fine-tune what you can't explain. Re-check
pace at weeks 6 and 14.
```

**Techniques Used:**
- **ED-01 (Iterative Scaffolding):** phases build prerequisite-by-prerequisite toward LLM-application competence.
- **ST-02 (Structured Sequential Instructions):** goal → entry point → dependency order → phases.
- **DS-06 (Prioritization & Severity Guidance):** dependency-driven sequencing; skippables marked.
- **RP-01 (Audience/Level Adaptation):** scope, pace, and builds tuned to level, time, and compute/API.
- **CM-02 (Constraint Specification):** time budget, access, and prerequisites as hard constraints.

**Related Prompts:**
- `mllearn_study_path_designer.md` — the generic generator this track instantiates for NLP/LLM.
- `genai_rag_system_design.md` — deep reference for the RAG phase.
- `paper-reproductions/README.md` — the landmark-paper reproduction series (Transformer, word2vec) the track points to.
