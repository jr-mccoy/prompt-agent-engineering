---
title: "LLM Cost & Latency Optimization"
category: AI-ML/genai-llm-engineering
description: "Cut LLM cost and latency without quality loss: model routing, caching, batching, prompt compression, and distillation — each gated by an eval that proves quality held, with cost/latency measured before and after."
techniques:
  - RT-02
  - DS-06
  - DS-02
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - cost-optimization
  - latency
  - model-routing
  - caching
  - distillation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_llm_observability_tracing.md
  - domain-AI-ML/genai-llm-engineering/genai_context_window_strategy.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_evaluation_design.md
---

# LLM Cost & Latency Optimization

**Objective:** Reduce the cost and/or latency of an LLM application — via model routing, caching, batching, prompt compression, and distillation — by ranking the levers against the workload's cost/latency drivers and gating every change behind an eval that proves quality did not regress, with cost and latency measured before and after each change.

**When to Use:**
- LLM spend or response time is too high and you need targeted, quality-safe reductions.
- You're tempted to switch to a cheaper model and want to confirm quality holds first.
- Scaling up and need a cost/latency plan before volume grows.

**When NOT to Use:**
- You lack cost/latency telemetry to target the right lever (set up `genai_llm_observability_tracing.md` first).
- The issue is purely context size (use `genai_context_window_strategy.md`).

## Inputs / Context

State the model(s) + provider + version. Provide what you can:
- **Cost/latency breakdown** — current spend and latency, ideally attributed by step/model/feature (from observability).
- **Workload shape** — request volume, prompt/completion token sizes, repeat-query rate, peak vs steady, tolerance for staleness.
- **Quality bar** — the eval and threshold quality must not drop below (cross-link `genai_llm_evaluation_design.md`).
- **Constraints** — latency SLA, infra (can you batch? self-host a distilled model?), budget target.

## Constraints

**Must:**
- Identify the dominant cost/latency driver before choosing a lever (don't optimize the cheap part).
- Gate every optimization behind the quality eval; report quality before and after, with cost/latency deltas.
- Distinguish cost levers from latency levers (some help one and hurt the other — e.g., batching cuts cost but adds latency).

**Must Not:**
- Switch to a cheaper/smaller model on the assumption quality holds — measure it on the eval set.
- Cache responses without a correctness/staleness policy (a cached wrong or stale answer is worse than a slow right one).
- Fabricate cost/latency savings; require before/after measurement at realistic volume.

**Instructions:**

1. **Attribute the cost/latency.** From telemetry, break down spend and latency by model, feature, prompt component, and step. Find the dominant driver — most savings come from one or two places (often oversized prompts or an over-strong model on easy queries).

2. **Rank candidate levers against the driver.** Map levers to drivers: model routing (use a small model for easy queries, escalate hard ones), caching (high repeat rate), batching (throughput-bound, latency-tolerant), prompt compression / context trimming (oversized prompts — cross-link `genai_context_window_strategy.md`), distillation (high steady volume on a narrow task).

3. **Design model routing.** Define how query difficulty is classified and routed to a cheap vs strong model, with an escalation path and a quality check per tier. Verify each model's cost/latency against current docs.

4. **Design caching.** Specify exact-match and/or semantic caching, the staleness/invalidation policy, and what is unsafe to cache (personalized, time-sensitive, or non-deterministic-critical outputs).

5. **Design batching/streaming.** For latency, consider streaming (time-to-first-token) and parallelism; for cost/throughput, consider request batching — noting the latency tradeoff and SLA limits.

6. **Design prompt/context compression.** Trim non-load-bearing context, shorten system prompts, and reduce few-shot examples to the minimum that holds quality — re-using the context-window strategy.

7. **Consider distillation.** For a narrow high-volume task, evaluate distilling/fine-tuning a smaller model from the strong model's outputs, gated by the same quality eval and the worth-it cost analysis.

8. **Gate, measure, and roll out.** For each lever, run the quality eval (must stay ≥ threshold) and measure cost/latency before/after at realistic volume. Roll out only levers that hold quality; monitor for regression post-launch.

**Output Format:**

A markdown optimization plan:
- **Cost/Latency Attribution** — dominant drivers by model/feature/step
- **Lever Ranking** — table: Lever | Targets cost/latency | Expected impact | Quality risk | Effort
- **Selected Levers** — design per chosen lever (routing/caching/batching/compression/distillation)
- **Quality Gate** — eval + threshold each lever must pass
- **Before/After Measurement Plan** — metrics at realistic volume
- **Rollout & Monitoring** — sequence + regression watch

## Verification

- [ ] The dominant cost/latency driver is identified before levers are chosen.
- [ ] Each lever is gated by the quality eval with before/after quality reported.
- [ ] Cost levers and latency levers are distinguished (batching's latency cost is noted).
- [ ] Caching has an explicit staleness/invalidation policy and unsafe-to-cache list.
- [ ] Model routing has a per-tier quality check and escalation path.
- [ ] Savings are measured at realistic volume, not estimated from memory.

## False-Positive Prevention

❌ **DON'T:**
- Drop to a cheaper model and assume quality is "good enough" without running the eval on hard queries.
- Cache aggressively without an invalidation policy — stale/wrong cached answers erode trust silently.
- Optimize the cheap part of the pipeline because it's easy, while the dominant cost driver is untouched.
- Add batching to cut cost without checking it breaks the latency SLA.

✅ **DO:**
- Attribute cost/latency first and aim the biggest lever at the dominant driver.
- Gate every change behind the quality eval and report quality + cost + latency deltas.
- Define caching staleness/invalidation and exclude unsafe-to-cache outputs.
- Treat cost and latency as separate axes and check each lever's effect on both.

## Example Output

```markdown
## Cost/Latency Plan: Doc Q&A Assistant (models: <provider/model vX>)

### Attribution
80% of cost is the strong model answering simple FAQ-style queries it doesn't need.
Latency dominated by model-call (p95 2.1s); prompts oversized (avg 6k tokens, ~half low-value).

### Lever Ranking
| Lever | Targets | Impact | Quality risk | Effort |
|---|---|---|---|---|
| Routing (small for FAQ) | cost | high | med (gate) | med |
| Prompt/context trim | cost+latency | med | low | low |
| Semantic cache | cost+latency | med | med (staleness) | med |
| Batching | cost | low here (latency-sensitive) | n/a | skip |

### Selected Levers
1. Route: difficulty classifier -> small model for FAQ, escalate low-confidence to strong.
2. Trim context per genai_context_window_strategy (6k -> ~3k).
3. Semantic cache for FAQ answers, 24h TTL, invalidate on doc update; exclude account-specific.

### Quality Gate
All levers must keep correctness ≥ 2.4 (rubric) and faithfulness ≥ 0.95 on the eval set.

### Before/After (at realistic volume)
Routing+trim: cost -52%, p95 2.1s -> 1.3s, correctness 2.5 -> 2.48 (within CI). Cache adds -15% cost.

### Rollout & Monitoring
Ship trim, then routing, then cache. Watch escalation rate and cache hit/staleness weekly.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** levers weighed across cost, latency, quality risk, effort.
- **DS-06 (Prioritization & Severity Guidance):** levers ranked against the dominant driver.
- **DS-02 (Metric Specification):** quality, cost, latency measured before/after at volume.
- **QA-12 (False Positives Identification):** guards against unmeasured cheaper-model and stale-cache wins.
- **CM-02 (Constraint Specification):** SLA and quality threshold bound every lever.

**Related Prompts:**
- `genai_llm_observability_tracing.md` — provides the attribution this plan starts from.
- `genai_context_window_strategy.md` — prompt/context trimming is a primary lever.
- `genai_llm_evaluation_design.md` — the quality gate every cost/latency change must pass. (See also the token-cost optimization one-offs under `domain-software-engineering/devops/`.)
