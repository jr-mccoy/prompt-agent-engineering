---
title: "ML Compression Tradeoff Analysis"
category: AI-ML/model-optimization-efficiency
description: "Compare compression options (quantization, pruning, distillation, architecture swap, and their combinations) across the size / latency / accuracy / cost frontier for a stated deployment target, and recommend the option that meets the budget at the least accuracy cost — with every figure flagged for measurement."
techniques:
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - model-compression
  - tradeoff-analysis
  - quantization
  - pruning
  - distillation
  - cost-performance
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_quantization_plan.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_pruning_strategy.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_knowledge_distillation_plan.md
---

# ML Compression Tradeoff Analysis

**Objective:** Given a deployment target and budget, compare the realistic model-compression options — quantization, pruning, knowledge distillation, an efficient-architecture swap, and sensible combinations — across the four-way frontier of size, latency, accuracy, and engineering/serving cost, and recommend the option (or sequence) that meets the hard constraints at the lowest accuracy cost, with every performance/accuracy figure explicitly flagged as an estimate to be measured.

**When to Use:**
- You must shrink/speed up a model and want a principled comparison before committing to one technique.
- Multiple constraints bind at once (size AND latency AND accuracy AND cost) and you need the option that satisfies all.
- A single technique alone won't reach the budget and you need to evaluate combinations.

**When NOT to Use:**
- You have already chosen a technique and need the detailed plan (use the technique-specific prompt: `mlopt_quantization_plan.md`, `mlopt_pruning_strategy.md`, `mlopt_knowledge_distillation_plan.md`).
- The real issue is hardware choice (use `mlopt_hardware_accelerator_selection.md`).

## Inputs / Context

Provide what you can; the analysis degrades gracefully if some are missing:
- **Target hardware + runtime** — what the compressed model runs on and which precisions/sparsity/kernels it accelerates. *Ask the user if unspecified — runtime support determines which techniques actually pay off.*
- **Framework + version** — for technique availability and export path.
- **Hard constraints** — size ceiling, latency SLA, memory ceiling, and the accuracy budget (metric + max drop).
- **Resources** — whether retraining/fine-tuning is feasible (gates QAT, pruning recovery, distillation), data access, and engineering time.
- **Current model** — architecture, size, full-precision accuracy and latency on the target.
- **Cost basis** — to compare serving cost-per-request and the one-time engineering/training cost of each option.

## Constraints

**Must:**
- Evaluate each option against the SAME hard constraints and accuracy budget, so the comparison is apples-to-apples.
- Tie each technique's viability to the target runtime's support (e.g., unstructured pruning needs sparse kernels; int8 needs int8 compute) and to retraining feasibility.
- For every option, pair the efficiency gain with its accuracy cost AND the one-time engineering/training cost, and flag each number as an estimate to be measured.

**Must Not:**
- Quote specific size/latency/accuracy numbers as measured — present them as estimates with the measurement that would confirm them.
- Recommend a combination without noting interaction effects (e.g., prune-then-quantize compounds accuracy loss; order and recovery matter).
- Pick the option with the best single axis while ignoring a violated hard constraint.

**Instructions:**

1. **Fix the constraint set and budget.** Restate the hard ceilings (size, latency, memory), the accuracy budget, and retraining feasibility. These are the pass/fail filters every option faces.

2. **Screen techniques for runtime + resource viability.** Eliminate up front the techniques the runtime can't accelerate (e.g., unstructured pruning on dense hardware) or that retraining infeasibility rules out (QAT, distillation). State why each is in or out.

3. **Characterize each surviving option.** For quantization, pruning, distillation, architecture swap, and key combinations, describe the expected position on each axis (size, latency, accuracy, cost) — as estimates, with the dominant accuracy-cost mechanism named.

4. **Build the tradeoff frontier.** Lay out a comparison table; identify which options are on the Pareto frontier (no other option is better on all axes) and which are dominated and can be dropped.

5. **Analyze combinations and ordering.** Where a single technique misses the budget, evaluate combinations, explicitly noting that accuracy losses compound and that order (e.g., distill → quantize, or prune → fine-tune → quantize) changes the outcome.

6. **Account for total cost.** For each frontier option include one-time cost (engineering + training/fine-tuning compute) and recurring serving cost-per-request, so a cheap-to-run option with a huge build cost is visible.

7. **Recommend with a decision rule.** Pick the option meeting all hard constraints at the least accuracy cost (tie-broken by lowest total cost); state the rule, the runner-up, and the assumption that, if false, flips the choice.

8. **Specify the validation gate.** Define the held-out accuracy metric (and per-slice check), the on-target efficiency measurements, and the go/no-go threshold to confirm the chosen option before shipping.

**Output Format:**

A markdown analysis:
- **Constraints & Budget** — hard ceilings, accuracy budget, retraining feasibility
- **Technique Viability Screen** — table: Technique | Runtime-supported? | Retraining needed? | In/Out + why
- **Tradeoff Frontier** — table: Option | Size (est.) | Latency (est.) | Accuracy cost (est.) | One-time cost | Serving cost | Meets all constraints?
- **Pareto Set & Dominated Options**
- **Combinations & Ordering Notes**
- **Recommendation + Decision Rule + Runner-Up**
- **Validation Gate** — what to measure before shipping
- **Open Questions**

## Verification

- [ ] All options are scored against the same hard constraints and accuracy budget.
- [ ] A viability screen removes runtime-unsupported / retraining-infeasible techniques with reasons.
- [ ] Each option pairs efficiency gain with accuracy cost AND one-time + serving cost.
- [ ] A Pareto frontier is identified and dominated options are dropped.
- [ ] Combination options note compounding accuracy loss and ordering effects.
- [ ] The recommendation states a decision rule, a runner-up, and the assumption-flip condition, with a validation gate.

## False-Positive Prevention

❌ **DON'T:**
- Recommend unstructured pruning for a "5x smaller, 5x faster" claim on hardware with no sparse kernels — size may shrink but latency won't.
- Stack quantization on top of aggressive pruning and assume the accuracy costs simply add — they often compound non-linearly and depend on order.
- Choose the option with the best size or latency while it quietly violates the accuracy budget or memory ceiling.
- Compare options on per-unit speed while ignoring that one requires weeks of QAT/distillation engineering.

✅ **DO:**
- Screen every technique against the target runtime's actual acceleration and the team's retraining feasibility first.
- For combinations, plan the order and a recovery step, and measure the combined accuracy cost end-to-end, not per-technique.
- Filter on all hard constraints before ranking; an option that misses any ceiling is disqualified regardless of its strong axis.
- Include one-time engineering/training cost so build effort is part of the tradeoff, not just runtime savings.

## Example Output

```markdown
## Compression Tradeoff: Object Detector for Cloud Serving (target GPU runtime vX)

### Constraints & Budget
Size ≤ 60 MB, p95 ≤ 30 ms at batch=8, mAP drop ≤ 1.0 pt. Retraining feasible (data + 2 GPUs).

### Technique Viability Screen
| Technique | Runtime-supported? | Retraining needed? | In/Out + why |
|---|---|---|---|
| int8 quantization | Yes (int8 GEMM) | No (PTQ) | In |
| Structured (channel) pruning | Yes (dense) | Yes (recovery) | In |
| Unstructured pruning | No sparse kernels | Yes | Out — no latency win |
| Distillation to smaller backbone | Yes | Yes | In |
| Combo: distill → int8 | Yes | Yes | In |

### Tradeoff Frontier
| Option | Size (est.) | Latency (est.) | Accuracy cost (est.) | One-time cost | Serving cost | Meets all? |
|---|---|---|---|---|---|---|
| int8 PTQ | ~45 MB | ~22 ms | ~0.6 pt | low | low | Yes |
| Channel prune + FT | ~55 MB | ~24 ms | ~0.9 pt | medium | low | Yes (tight) |
| Distill → smaller | ~38 MB | ~18 ms | ~1.3 pt | high | lowest | No (acc) |
| Distill → int8 | ~22 MB | ~15 ms | ~1.1 pt | high | lowest | No (acc, tight) |

### Pareto Set & Dominated
Pareto: int8 PTQ (cheap, safe), distill→int8 (smallest/fastest, costlier + risk). Channel-prune dominated by int8 on cost and accuracy here.

### Combinations & Ordering Notes
distill→int8 compounds loss; distill first, recover, THEN quantize and re-validate — quantizing a freshly distilled student without recovery overshoots the budget.

### Recommendation + Decision Rule + Runner-Up
Recommend int8 PTQ: meets all constraints at least accuracy cost and lowest build effort. Rule: prefer the lowest-accuracy-cost option meeting all ceilings; choose distill→int8 only if a future size ceiling drops below 30 MB. Runner-up: distill→int8 (if accuracy recovery closes the gap). Flips if int8 PTQ fails its accuracy gate.

### Validation Gate
mAP on held-out + per-class slices; size + p95 at batch=8 on target GPU. Ship if mAP drop ≤ 1.0 pt AND p95 ≤ 30 ms AND size ≤ 60 MB.

### Open Questions
- Confirm int8 op coverage for detection head; confirm mAP budget (assumed 1.0 pt).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** constraints → viability screen → characterize → frontier → combinations → cost → recommend → gate.
- **RT-02 (Multi-Dimensional Analysis Framework):** the core size/latency/accuracy/cost four-way comparison.
- **DS-06 (Prioritization & Severity Guidance):** Pareto ranking and the least-accuracy-cost decision rule.
- **CM-02 (Constraint Specification):** hard ceilings and accuracy budget as disqualifying filters.
- **QA-12 (False Positives Identification):** guards against sparsity-without-kernels, compounding-loss, and best-single-axis traps.

**Related Prompts:**
- `mlopt_quantization_plan.md` — detailed plan once quantization is chosen.
- `mlopt_pruning_strategy.md` — detailed plan once pruning is chosen.
- `mlopt_knowledge_distillation_plan.md` — detailed plan once distillation is chosen.
```