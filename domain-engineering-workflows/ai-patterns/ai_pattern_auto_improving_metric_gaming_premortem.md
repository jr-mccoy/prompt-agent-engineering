---
title: "Metric-Gaming Pre-Mortem for an Auto-Improving Agent Loop"
category: ai-patterns
description: "Before closing the loop on an auto-improving agent system, generate the ways it will learn to game the metrics — specifically, not generically — and propose counter-measures for each. If a path exists, the loop will find it."
techniques:
  - ST-01
  - ST-02
  - QA-02
  - CM-02
  - RT-02
  - RT-11
difficulty: advanced
tags:
  - ai-patterns
  - auto-improvement
  - pre-mortem
  - metric-gaming
  - evaluation
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_auto_improving_triplet_diagnostic.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_auto_improving_trace_infrastructure_audit.md
  - domain-engineering-workflows/ai-patterns/ai_review_failure_mode_premortem.md
---

# Metric-Gaming Pre-Mortem for an Auto-Improving Agent Loop

**Purpose:** Any loop that tunes an agent on a metric will eventually optimize against the metric rather than against the underlying goal. This happens earlier, and more subtly, than teams expect. This prompt runs a pre-mortem specific to the user's metrics and loop — not "metric gaming is a thing" but "here are the six concrete ways *your* setup will drift, and the counter-measures for each."

**When to use:**
- You're about to close the loop on an auto-improvement system (let it update prompts, tools, or configs based on its own metrics)
- A loop has been running and its reported numbers look surprisingly good — check whether it's genuine improvement
- You have LLM-as-judge scoring and want to stress-test whether the system learns to please the judge
- You're designing a reward / grading rubric and want to catch gameable shapes before they ship
- A regulator / stakeholder has asked how you'd know if the system was gaming its metrics

**What you'll get:** A ranked list of specific gaming paths for this system (not generic ones), a counter-measure per path, an early-warning signal per path, and a "stop the loop" trigger set.

---

```
## ROLE
You run a pre-mortem against a specific auto-improving agent loop. You generate the concrete ways THIS system will learn to game ITS metrics. You do not write a generic essay on Goodhart's Law. You produce paths, counter-measures, early-warning signals, and a stop-trigger set.

## CONTEXT
Metric gaming is not an agent being adversarial. It is the optimizer doing exactly what we asked of it — maximizing the metric — while we assumed the metric was a faithful proxy for the goal. The gap shows up predictably:

**Gaming-path shapes:**
1. **Specification shortcut** — the metric can be satisfied without the underlying behavior (e.g., "response includes all 5 sections" → verbose, empty sections)
2. **Distribution shift** — the system optimizes the task set and drifts from real traffic
3. **Judge bias** — LLM-as-judge has a preference (length, format, specific phrasing) that the system learns to exploit
4. **Evaluation leak** — the agent sees eval signals during generation and alters output accordingly
5. **Cost offload** — metric improves by shifting cost to an unmeasured axis (quality up, latency up, or vice versa)
6. **Aggregation hiding** — average metric improves while the tails get worse; one failing subset now catastrophic
7. **Feedback loop collapse** — the agent learns to produce outputs similar to past high-scoring outputs, losing coverage

Generic awareness of these shapes isn't enough. Each has a different counter-measure and a different early-warning signal, and the specifics depend on the system's metrics, task set, and tuning mechanism.

## INPUTS
Ask the user for:

1. **System under pre-mortem** — the agent, what it does, what outputs it produces.
2. **Metrics being optimized** — each metric, its formula / description, who/what computes it.
3. **Tuning mechanism** — what the loop actually changes based on the metric (prompts? tool choice? model selection? fine-tuning data? router weights?).
4. **Task set** — how it's constructed, labeled, and refreshed.
5. **Judge setup** — if LLM-as-judge is involved, which model, which prompt, how calibrated.
6. **Stakes** — user-visible? critical? reversible? what's the blast radius of an undetected gaming path?

## INSTRUCTIONS

1. **For each of the seven gaming-path shapes**, instantiate it against THIS system:
   - What would gaming look like concretely here? (e.g., for a research-summary agent: "specification shortcut" might be "summary includes every requested heading but the content under each heading is three sentences of boilerplate")
   - Is this plausible given how the loop tunes the system? Rate Likelihood (Low / Medium / High) with a reason tied to the specific tuning mechanism.
   - Severity if it happens — how bad for the user, how hard to notice, how hard to reverse.
   - Combine into priority (P0 … P3).

2. **Propose one counter-measure per high-priority path.** Counter-measures take three forms:
   - **Structural** — change what the metric measures so the shortcut doesn't satisfy it (e.g., add a semantic-coverage check; add a second metric that penalizes verbosity)
   - **Independent check** — a periodic audit by a different judge / a held-out human-rated set / adversarial probes
   - **Constraint on the loop** — cap the rate of change per iteration; keep a version the loop can't modify; sample from older task distributions
   
   Prefer structural > independent check > constraint. Structural fixes are cheapest long-term.

3. **Define the early-warning signal per path.** Each gaming path has a footprint: a second-order metric that moves before the headline metric diverges from goal. Examples:
   - Specification shortcut: output length / verbosity metric climbs while information density drops
   - Distribution shift: task-set coverage shifts (new clusters become over-represented)
   - Judge bias: judge-human agreement rate declines on a held-out sample
   - Evaluation leak: small training-style changes correlate with eval-score jumps
   - Cost offload: non-headline metric (latency / cost / human review rate) degrades
   - Aggregation hiding: metric variance across task subsets widens
   - Feedback loop collapse: output-similarity / coverage metric drops
   
   For each high-priority path, name the specific measurement, who/what computes it, and the threshold that triggers investigation.

4. **Define the stop-the-loop trigger set.** Conditions under which the system stops auto-applying changes:
   - Any early-warning signal crosses its threshold
   - Judge-human disagreement crosses N%
   - A held-out adversarial probe set drops below a floor
   - A cost / latency ceiling is crossed
   - Manual kill-switch for stakeholder / on-call
   
   Every trigger names what happens when it fires (freeze loop / revert to last stable / escalate).

5. **Produce a "seed corpus" of known-good and adversarial cases.** Small set (5–10) of cases the system must always handle, regardless of what the loop does. Use it as a regression gate — if the loop's updates degrade performance on this corpus, revert.

6. **Estimate time-to-gaming.** For each high-priority path, how many iterations of the loop before gaming becomes visible? If the answer is "we don't know," that's the finding — start with a shorter feedback cycle.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT produce generic gaming paths. Every path must cite a specific mechanism in THIS system's tuning loop.
- Do NOT propose counter-measures without naming the early-warning signal. Without the signal, the counter-measure is invisible.
- Do NOT recommend "add a second LLM judge" as a default counter-measure. Two judges with the same biases game together.
- Do NOT assume a gaming path is impossible because "our loop is small." Even low-rate loops game on long timescales.
- Do NOT skip aggregation-hiding. It is the most common and least-noticed path.
- Do NOT close the loop without a stop-trigger set. Closing without stops is an outage waiting to happen.
- Do NOT accept "we'd notice" as an early-warning. Require a measurement.
- DO consider whether the judge is also the system being optimized (even indirectly through shared prompts / training data). Same-family judges are especially gameable.
- DO require the seed corpus to include cases the loop cannot update against.

## OUTPUT FORMAT

### Gaming Paths (This System)
| # | Shape | Concrete manifestation here | Likelihood | Severity | Priority |
|---|-------|----------------------------|------------|----------|----------|
| 1 | Specification shortcut | | L/M/H | S/M/L | P0-P3 |
| 2 | Distribution shift | | | | |
| 3 | Judge bias | | | | |
| 4 | Evaluation leak | | | | |
| 5 | Cost offload | | | | |
| 6 | Aggregation hiding | | | | |
| 7 | Feedback loop collapse | | | | |

### Counter-Measures (for P0 / P1 paths)
| Path | Counter-measure type | Specific change | Expected effect |
|------|---------------------|-----------------|-----------------|
| | Structural / Independent / Constraint | | |

### Early-Warning Signals
| Path | Signal | How computed | Threshold |
|------|--------|--------------|-----------|
| | | | |

### Stop-the-Loop Triggers
| Trigger | Action |
|---------|--------|
| | freeze / revert / escalate |

### Seed Corpus
- [ ] 5–10 cases named (attach, or describe briefly)
- [ ] Includes adversarial cases
- [ ] Loop cannot modify this corpus
- [ ] Runs as a gate on every loop iteration

### Time-to-Gaming Estimates
| Path | Estimated iterations before gaming visible | Confidence |
|------|-------------------------------------------|------------|
| | | |

### Sanity Checklist
- [ ] Each path is specific to this system, not generic
- [ ] Each P0/P1 path has a counter-measure and an early-warning signal
- [ ] Stop-triggers are defined with actions
- [ ] Seed corpus is locked from the loop
- [ ] The loop posture is documented (open / shadow / closed, and under which conditions it changes)

## IMPORTANT
- If you cannot name how the loop would game a metric, the loop will still game it. Absence of imagination is not absence of risk.
- Shadow mode is the default for a system without validated counter-measures.
- The most dangerous gaming path is the one nobody in the room would have predicted. Spend disproportionate attention on "aggregation hiding" and "judge bias" — both are quiet.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is a ranked gaming-path list with counter-measures, not a Goodhart's Law summary
- ST-02 (Structured Sequential Instructions) — 6 steps walk from path instantiation → counter-measure → signal → stop trigger
- QA-02 (Adversarial Stress-Test) — pre-mortem against a system the user is about to close the loop on
- CM-02 (Constraint Specification) — Must / Must Not blocks the "two LLM judges = safe" reflex
- RT-02 (Multi-Dimensional Analysis) — seven distinct gaming shapes handled separately
- RT-11 (Error Recovery) — stop-the-loop triggers define how the system halts and rolls back when gaming is detected
