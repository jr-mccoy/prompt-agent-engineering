---
title: "Interview Bank: Recommendation & Ranking Systems"
category: AI-ML/learning-ai-ml/interview-bank
description: "A bank of recommendation and ranking ML-system-design interview questions, each paired with a junior→staff leveled rubric covering candidate generation, ranking, cold start, feedback-loop bias, and online/offline evaluation."
techniques:
  - DS-01
  - ST-02
  - DS-06
  - RP-01
  - QA-12
difficulty: advanced
tags:
  - interview-prep
  - recommendation
  - ranking
  - system-design
  - rubric
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_ml_system_design_interview.md
  - domain-AI-ML/learning-ai-ml/interview-bank/mllearn_interview_scoring_rubric.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_multi_objective_ranking.md
---

# Interview Bank: Recommendation & Ranking Systems

**Objective:** Produce a usable bank of recommendation/ranking ML-system-design interview questions, each with a leveled rubric (junior / mid / senior / staff) that describes what a strong answer covers at each bar — so a learner can self-quiz, an interviewer can grade consistently, and the operational discriminators (cold start, feedback-loop bias, online/offline eval) that separate seniority levels are explicit, not implied.

**When to Use:**
- A learner is preparing for recommendation/ranking system-design rounds and wants questions + bars.
- An interviewer needs a consistent, level-calibrated rubric for these rounds.
- Self-assessing depth on candidate generation → ranking → serving → eval for recsys.

**When NOT to Use:**
- The learner wants an interactive mock, not a question bank (use `mllearn_ml_system_design_interview.md`).
- The round is concept/coding/stats quizzing (use `mllearn_ml_interview_prep.md`).
- They need the generic cross-topic rubric only (use `mllearn_interview_scoring_rubric.md`).

## Inputs / Context

- **Target level(s)** — which bars matter most (junior, mid, senior, staff).
- **Sub-focus** — feed ranking, e-commerce recs, candidate generation, etc., if narrowing.
- **Use mode** — self-quiz, interviewer grading, or curriculum gap-finding.
- **Number of questions** — how many to generate.

## Constraints

**Must:**
- Pair every question with a leveled rubric whose bars escalate from "names the component" (junior) to "owns the operational lifecycle and second-order effects" (staff).
- Bake the recsys-specific discriminators into the senior/staff bars: cold start, feedback-loop/popularity bias, online vs offline eval mismatch, candidate-generation vs ranking separation, and multi-objective tradeoffs.
- Make "asks requirements and defines success metrics before modeling" a pass condition at every level.

**Must Not:**
- Present these as real, specific company interview questions or attach fabricated "real candidate" scores or hiring-bar facts — they are practice questions and reasoning bars.
- Reward a fluent architecture answer that skips requirements, metrics, or evaluation.
- Treat "we'll use a recommender model" as sufficient without candidate-generation/ranking structure.

**Instructions:**

1. **Confirm scope.** Establish target level(s), any sub-focus, use mode, and question count.

2. **Generate questions across the recsys design surface.** Cover candidate generation, ranking, cold start, real-time vs batch serving, feedback loops/bias, and evaluation — phrased as open design prompts.

3. **For each question, write the leveled rubric.** Four bars (junior/mid/senior/staff). Each bar states what the answer demonstrates; higher bars add operational reality and second-order reasoning.

4. **Embed the discriminators.** Ensure the senior/staff bars require cold-start handling, feedback-loop/bias awareness, online/offline eval reconciliation, and a stated multi-objective tradeoff.

5. **Add a "requirements & metrics gate".** For each question, note the clarifications and success metrics a passing answer must establish before modeling.

6. **Note common failure signals.** For each question, list the answers that look good but should not pass (e.g., jumping to a model, ignoring popularity bias).

7. **Point to deeper study.** Link the recsys practitioner prompts for the concepts a learner must shore up.

**Output Format:**

A markdown question bank:
- **Scope** — levels, focus, mode.
- **Questions** — for each: the design prompt, a Requirements & Metrics Gate, a 4-bar leveled rubric, and Common Failure Signals.
- **Study Pointers** — where to deepen weak areas.

## Verification

- [ ] Every question has a 4-bar (junior→staff) rubric with escalating expectations.
- [ ] Senior/staff bars require cold start, feedback-loop bias, and online/offline eval.
- [ ] Each question has a requirements-and-metrics gate as a pass condition.
- [ ] Questions are framed as practice prompts, not fabricated real company questions.
- [ ] Common failure signals are listed (fluent-but-shallow answers don't pass).

## False-Positive Prevention

❌ **DON'T:**
- Claim these are actual questions asked at named companies, or invent candidate scores.
- Let an answer pass for naming "two-tower model" without requirements, metrics, or eval.
- Omit feedback-loop/popularity bias from the senior bar — it's a core recsys discriminator.
- Score offline metrics as sufficient without addressing online/offline mismatch.

✅ **DO:**
- Frame questions as practice and rubrics as demonstrated-reasoning bars.
- Require requirements + success metrics before any modeling, at every level.
- Put cold start, bias, and online/offline eval in the senior/staff bars.
- List the seductive-but-failing answers explicitly.

## Example Output

```markdown
## Interview Bank — Recommendation & Ranking (levels: mid + senior; mode: self-quiz)

### Q1: Design a home-feed ranking system for a content platform.
**Requirements & Metrics Gate:** scale/QPS, latency budget, the objective (engagement? long-term
retention?), how success is measured online vs offline, content freshness needs.

**Rubric**
- *Junior:* names candidate generation + ranking; picks reasonable features/model; some offline metric.
- *Mid:* separates retrieval from ranking; defines an offline metric AND an online metric; handles
  basic cold start; aware of training/serving data flow.
- *Senior:* reconciles offline/online eval (proxy-metric risk), handles cold start for users AND
  items, identifies the feedback loop (engagement → exposure → more engagement) and its bias,
  states a latency/accuracy tradeoff.
- *Staff:* designs for multi-objective ranking (engagement vs diversity vs creator health),
  anticipates Goodhart on the proxy objective, plans guardrail metrics and a long-term holdout.

**Common Failure Signals:** jumps to "a deep ranking model" before metrics; treats offline AUC as
the goal; ignores popularity bias; no online eval plan.

### Q2: Cold-start a recommender for a brand-new marketplace. …
(Requirements gate, 4-bar rubric, failure signals as above.)

### Study Pointers
Weak on multi-objective tradeoffs → `recsys_multi_objective_ranking.md`. Weak on bias →
`recsys_feedback_loop_bias_audit.md`.
```

**Techniques Used:**
- **DS-01 (Framework Application):** the recsys design surface (gen → rank → serve → eval) structures the bank.
- **ST-02 (Structured Sequential Instructions):** scope → questions → rubrics → gates → failure signals.
- **DS-06 (Prioritization & Severity Guidance):** leveled bars prioritize the discriminators by seniority.
- **RP-01 (Audience/Level Adaptation):** four bars calibrated junior→staff.
- **QA-12 (Rubric-Based Evaluation):** explicit, level-calibrated grading bars per question.

**Related Prompts:**
- `mllearn_ml_system_design_interview.md` — the interactive mock to practice these questions live.
- `interview-bank/mllearn_interview_scoring_rubric.md` — the universal dimension-by-dimension rubric.
- `recsys_multi_objective_ranking.md` — deepen the multi-objective ranking concepts the staff bar requires.
