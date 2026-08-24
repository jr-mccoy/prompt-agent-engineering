---
title: "Interview Bank: Real-Time & Fraud Detection Systems"
category: AI-ML/learning-ai-ml/interview-bank
description: "A bank of real-time/streaming and fraud-detection ML-system-design interview questions, each paired with a junior→staff leveled rubric covering latency, train/serve skew, label delay, class imbalance, adversarial drift, and human-review loops."
techniques:
  - DS-01
  - ST-02
  - DS-06
  - RP-01
  - QA-12
difficulty: advanced
tags:
  - interview-prep
  - fraud-detection
  - real-time
  - system-design
  - rubric
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_ml_system_design_interview.md
  - domain-AI-ML/learning-ai-ml/interview-bank/mllearn_interview_scoring_rubric.md
  - domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md
---

# Interview Bank: Real-Time & Fraud Detection Systems

**Objective:** Produce a usable bank of real-time/streaming and fraud-detection system-design interview questions, each with a leveled rubric (junior / mid / senior / staff) — so a learner can self-quiz, an interviewer can grade consistently, and the discriminators that separate seniority (latency at scale, train/serve skew, label delay, class imbalance, adversarial drift, human-in-the-loop review) are explicit rather than implied. These rounds are won or lost on operational reality.

**When to Use:**
- A learner is preparing for real-time/fraud/anomaly system-design rounds and wants questions + bars.
- An interviewer needs a consistent, level-calibrated rubric for these rounds.
- Self-assessing depth on low-latency serving, delayed/biased labels, and adversarial settings.

**When NOT to Use:**
- The learner wants an interactive mock (use `mllearn_ml_system_design_interview.md`).
- The round is concept/coding/stats quizzing (use `mllearn_ml_interview_prep.md`).
- They need the generic cross-topic rubric only (use `mllearn_interview_scoring_rubric.md`).

## Inputs / Context

- **Target level(s)** — which bars matter most.
- **Sub-focus** — payment fraud, account-takeover, anomaly detection, real-time abuse, etc.
- **Use mode** — self-quiz, interviewer grading, or curriculum gap-finding.
- **Number of questions** — how many to generate.

## Constraints

**Must:**
- Pair every question with a leveled rubric escalating from "picks a classifier and a metric" (junior) to "owns the operational lifecycle under latency, delayed labels, imbalance, and adversaries" (staff).
- Bake the real-time/fraud discriminators into senior/staff bars: latency budget and fallback, train/serve skew (same feature computation offline/online), label delay and how to evaluate under it, class imbalance and correct metrics (not accuracy), adversarial drift, and a human-review queue with its feedback loop.
- Make "establishes the cost asymmetry (FP vs FN), latency budget, and how success is measured before modeling" a pass condition at every level.

**Must Not:**
- Present these as real, specific company questions or attach fabricated scores/hiring facts.
- Reward "train a gradient-boosted model" without latency, skew, label-delay, or imbalance reasoning.
- Accept "we'll measure accuracy" on an imbalanced fraud problem.

**Instructions:**

1. **Confirm scope.** Establish target level(s), sub-focus, use mode, and question count.

2. **Generate questions across the real-time/fraud design surface.** Cover low-latency serving + fallback, feature freshness/train-serve skew, label delay, class imbalance + metrics, adversarial drift, and human-review loops — as open design prompts.

3. **For each question, write the leveled rubric.** Four bars; higher bars add operational reality and adversarial reasoning.

4. **Embed the discriminators.** Senior/staff bars require latency budget + fallback, train/serve skew handling, evaluation under label delay, imbalance-aware metrics, adversarial drift response, and a human-review feedback loop.

5. **Add a "cost-asymmetry & metrics gate".** For each question, note the FP/FN cost asymmetry, latency budget, and success metrics established before modeling.

6. **Note common failure signals.** List seductive-but-failing answers (accuracy on imbalanced data, ignoring label delay, no skew handling, no fallback).

7. **Point to deeper study.** Link the monitoring/triage prompts for concepts to shore up.

**Output Format:**

A markdown question bank:
- **Scope** — levels, focus, mode.
- **Questions** — for each: the design prompt, a Cost-Asymmetry & Metrics Gate, a 4-bar leveled rubric, and Common Failure Signals.
- **Study Pointers** — where to deepen weak areas.

## Verification

- [ ] Every question has a 4-bar (junior→staff) rubric with escalating expectations.
- [ ] Senior/staff bars require latency+fallback, skew, label-delay eval, imbalance metrics, adversaries, human review.
- [ ] Each question has a cost-asymmetry-and-metrics gate as a pass condition.
- [ ] Questions are framed as practice, not fabricated real company questions.
- [ ] Common failure signals are listed (accuracy on imbalanced data fails).

## False-Positive Prevention

❌ **DON'T:**
- Claim these are actual questions from named companies, or invent scores.
- Pass "a GBM with good accuracy" on an imbalanced fraud problem.
- Omit train/serve skew or label delay from the senior bar.
- Ignore the human-review queue and its label feedback loop.

✅ **DO:**
- Frame questions as practice and rubrics as demonstrated-reasoning bars.
- Require FP/FN cost asymmetry, latency budget, and metrics before modeling.
- Put skew, label delay, imbalance metrics, adversaries, and human review in senior/staff bars.
- List the fluent-but-failing answers explicitly.

## Example Output

```markdown
## Interview Bank — Real-Time & Fraud (levels: senior + staff; mode: interviewer grading)

### Q1: Design a real-time payment-fraud detection system.
**Cost-Asymmetry & Metrics Gate:** cost of a false block vs a missed fraud, latency budget
(synchronous block vs async review), how success is measured (precision at a recall floor;
$ losses), throughput.

**Rubric**
- *Junior:* picks a classifier; names precision/recall; some real-time notion.
- *Mid:* sets a latency budget; chooses imbalance-aware metrics; basic feature pipeline; aware
  labels are delayed.
- *Senior:* designs for train/serve skew (identical feature computation offline/online), evaluates
  under weeks-delayed labels, handles imbalance correctly, designs a human-review queue, plans a
  fallback if the model service is down.
- *Staff:* treats fraud as adversarial (drift as adversaries adapt; retraining cadence + drift
  monitoring), closes the label feedback loop from review without biasing it, and quantifies
  business impact with guardrails.

**Common Failure Signals:** accuracy on imbalanced data; ignores label delay; computes features
differently offline vs online; no fallback; static model in an adversarial setting.

### Q2: Design streaming anomaly detection for service metrics. …

### Study Pointers
Weak on degradation diagnosis → `mlmonitor_performance_degradation_triage.md`.
```

**Techniques Used:**
- **DS-01 (Framework Application):** the real-time/fraud operational surface structures the bank.
- **ST-02 (Structured Sequential Instructions):** scope → questions → rubrics → gates → failure signals.
- **DS-06 (Prioritization & Severity Guidance):** leveled bars order operational discriminators by seniority.
- **RP-01 (Audience/Level Adaptation):** four bars calibrated junior→staff.
- **QA-12 (Rubric-Based Evaluation):** explicit, level-calibrated grading bars per question.

**Related Prompts:**
- `mllearn_ml_system_design_interview.md` — the interactive mock to practice these live.
- `interview-bank/mllearn_interview_scoring_rubric.md` — the universal dimension-by-dimension rubric.
- `mlmonitor_performance_degradation_triage.md` — deepen the drift/degradation concepts the staff bar requires.
