---
title: "ML Knowledge Distillation Plan (Teacher → Student)"
category: AI-ML/model-optimization-efficiency
description: "Design a teacher→student distillation plan — student capacity, distillation objectives, temperature, transfer data, and evaluation — that pairs the efficiency gain of the smaller student with its measured accuracy cost versus both the teacher and a from-scratch baseline."
techniques:
  - ST-02
  - RT-02
  - QA-12
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - knowledge-distillation
  - teacher-student
  - model-compression
  - soft-labels
  - temperature
  - inference-efficiency
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_compression_tradeoff_analysis.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_quantization_plan.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_pruning_strategy.md
---

# ML Knowledge Distillation Plan (Teacher → Student)

**Objective:** Produce a knowledge distillation plan that takes a large, accurate teacher model and trains a smaller, faster student — specifying student capacity, the distillation loss (soft-label / logit / feature / response matching), temperature, transfer data, and an evaluation protocol — so the student's efficiency gain is reported against both the teacher's accuracy and a from-scratch baseline of the same student.

**When to Use:**
- You have an accurate teacher (or ensemble) that is too large/slow to serve and want to compress its behavior into a smaller student.
- A smaller architecture trained from scratch underperforms, and you want the teacher's "dark knowledge" to close the gap.
- You need an efficiency win that quantization/pruning of the teacher alone cannot reach.

**When NOT to Use:**
- No strong teacher exists, or the teacher itself is unreliable (distillation copies its errors and biases).
- A simpler post-hoc compression of the existing model meets the budget (use `mlopt_quantization_plan.md` / `mlopt_pruning_strategy.md`).
- You want a cross-technique comparison first (use `mlopt_compression_tradeoff_analysis.md`).

## Inputs / Context

Provide what you can; the plan degrades gracefully if some are missing:
- **Target hardware + runtime** — what the student must run on, and the latency/size/memory budget. *Ask the user if unspecified.*
- **Framework + version** — for the distillation training loop and export path.
- **Teacher** — architecture, accuracy on the target metric, calibration quality, known weaknesses/biases.
- **Candidate student(s)** — proposed smaller architecture(s) and their from-scratch accuracy if known.
- **Transfer data** — labeled and/or unlabeled data available for distillation; whether the original training set is accessible.
- **Quality bar** — the metric, the teacher's score, and the maximum acceptable gap for the student.

## Constraints

**Must:**
- Ask for target hardware + runtime and framework + version before fixing the student size; tie efficiency claims to the named target.
- Compare the distilled student against BOTH the teacher (upper bound) and the same student trained from scratch (the value distillation actually adds).
- Pair the efficiency gain (size/latency) with the measured accuracy gap and how it is measured on a held-out set.

**Must Not:**
- Quote specific accuracy or speedup numbers as measured — mark figures as estimates to verify on the user's data/hardware.
- Assume distillation always beats from-scratch training — require the ablation that proves it.
- Ignore that the student inherits the teacher's biases and calibration errors — flag for slice evaluation.

**Instructions:**

1. **Fix the student budget and the quality bar.** Restate the latency/size/memory target on the named hardware, the teacher's accuracy, and the maximum acceptable student gap. This bounds how small the student can be.

2. **Choose the student capacity.** Recommend an architecture/size whose from-scratch accuracy is the floor and whose budget fits the target; note the expected teacher–student capacity gap and its implication for achievable accuracy.

3. **Select the distillation objective.** Choose among response/logit matching (KL on softened logits), feature/intermediate matching (hint layers), and relation-based losses; justify the choice by modality and how much the student can absorb. Specify the weighting between the distillation loss and the hard-label loss.

4. **Set the temperature and loss weights.** Define the softmax temperature (higher reveals more inter-class structure but flattens signal) and the α balance between soft and hard targets; explain the tradeoff and a small search range.

5. **Design the transfer data.** Specify what the student learns from — original train set, unlabeled in-domain data scored by the teacher, or augmented data — and why coverage of the production distribution matters for transfer.

6. **Specify the training loop.** Optimizer, LR schedule, epochs, and whether the teacher is frozen; note compute cost so the up-front investment is visible against the serving savings.

7. **Define the evaluation protocol.** Measure the student's accuracy on a held-out set against teacher and from-scratch baselines, per-slice for inherited bias, calibration (ECE) if probabilities are consumed, and efficiency (size/latency/memory) on the target hardware.

8. **Set accept/reject gates.** Pass = student gap ≤ budget AND efficiency target met AND distillation beats from-scratch by a meaningful margin. Define the fallback (larger student, different objective, or a different compression technique).

**Output Format:**

A markdown plan:
- **Distillation Decision Summary** — table: Decision | Choice | Rationale | Efficiency Gain (est.) | Accuracy Cost vs Teacher (est.) | How Measured
- **Student Capacity Choice** — with from-scratch floor and budget fit
- **Objective & Hyperparameters** — loss type, temperature, α, weights
- **Transfer Data Plan** — sources, coverage, teacher-scoring strategy
- **Training Loop Spec** — optimizer/LR/epochs/compute cost
- **Evaluation Protocol** — teacher vs from-scratch vs distilled, slices, calibration, efficiency
- **Open Questions** — hardware budget, transfer data availability, quality bar

## Verification

- [ ] Target hardware/runtime and framework/version were requested or used.
- [ ] The student is compared against both the teacher and a from-scratch baseline.
- [ ] Efficiency gain is paired with the accuracy gap and a measurement method.
- [ ] Temperature and soft/hard-loss balance are specified with a tradeoff rationale.
- [ ] Per-slice and calibration evaluation are included to catch inherited bias/miscalibration.
- [ ] Accept/reject gates and a fallback exist.

## False-Positive Prevention

❌ **DON'T:**
- Claim distillation "worked" by comparing only to the teacher — a tiny gap is meaningless if from-scratch training reaches the same place.
- Use a temperature tuned on the test set, or report the best of many runs without noting variance.
- Assume the student is fair/calibrated because the teacher was — capacity loss can amplify slice errors and degrade calibration.
- Ignore the up-front training compute, presenting only the serving savings.

✅ **DO:**
- Run the three-way comparison (teacher, from-scratch student, distilled student) on the same held-out set; report the delta distillation adds.
- Tune temperature/α on a validation split and report run-to-run variance or CIs.
- Evaluate per-slice and check ECE when probabilities are consumed downstream.
- Net the one-time distillation cost against projected serving savings so the tradeoff is honest.

## Example Output

```markdown
## Distillation Plan: Sentiment Model (teacher: 12-layer transformer → student: 4-layer)

### Distillation Decision Summary
| Decision | Choice | Rationale | Efficiency Gain (est.) | Accuracy Cost vs Teacher (est.) | How Measured |
|---|---|---|---|---|---|
| Student | 4-layer transformer | Fits 20ms p95 budget on target CPU | ~3x latency, ~3x smaller (verify) | ~1–2 F1 (verify) | macro-F1 held-out |
| Objective | KL on softened logits + 0.5 hard CE | Logits carry class structure | — | reduces gap vs from-scratch | 3-way ablation |
| Temperature | T=3 (search 2–5) | Reveals inter-class similarity | — | tune on val | val F1 |

### Student Capacity Choice
4-layer student scores ~85 F1 from scratch vs teacher's 90. Distillation targets closing ~half that gap. Fits the CPU latency budget.

### Objective & Hyperparameters
L = α·KL(soft_student, soft_teacher; T=3) + (1−α)·CE(student, labels), α=0.7. Temperature searched on val.

### Transfer Data Plan
Full labeled train set + 200k unlabeled in-domain reviews scored by the teacher to broaden coverage.

### Training Loop Spec
AdamW, LR 5e-5 cosine, 5 epochs, teacher frozen. ~6 GPU-hours one-time vs projected serving savings of ~3x compute.

### Evaluation Protocol
- Macro-F1 on held-out for teacher / from-scratch / distilled, 95% CI.
- Per-slice F1 (product category, review length) for inherited bias.
- ECE for downstream thresholding; latency/size on target CPU.

### Accept/Reject Gate
Pass if distilled gap ≤ 2 F1 AND p95 ≤ 20 ms AND distilled beats from-scratch by ≥ 1.5 F1. Else try 6-layer student or feature-matching loss.

### Open Questions
- Confirm CPU latency budget; confirm unlabeled data licensing for transfer.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** budget → student → objective → temperature → data → training → eval.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances size, latency, accuracy, and calibration jointly.
- **QA-12 (False Positives Identification):** central to the teacher-only-comparison and tuned-on-test traps.
- **CM-02 (Constraint Specification):** quality bar + serving budget as governing constraints.
- **DS-02 (Metric Specification):** fixes the three-way comparison metrics and measurement points.

**Related Prompts:**
- `mlopt_compression_tradeoff_analysis.md` — weigh distillation against quantization/pruning.
- `mlopt_quantization_plan.md` — often combined with distillation for a smaller-and-lower-precision student.
- `mlopt_pruning_strategy.md` — an alternative or complement when a teacher is unavailable.
```