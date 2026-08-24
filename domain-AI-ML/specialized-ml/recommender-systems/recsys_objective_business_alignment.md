---
title: "Recommender Objective ↔ Business Alignment"
category: AI-ML/specialized-ml/recommender-systems
description: "Align a recommender's training objective with the actual business objective — exposing proxy-metric risk where optimizing the trainable label (clicks, watch-time) quietly degrades the goal it's supposed to serve (retention, revenue, satisfaction)."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - recommender-systems
  - objective-alignment
  - proxy-metrics
  - multi-objective
  - goodhart
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_candidate_ranking_design.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_feedback_loop_bias_audit.md
  - domain-AI-ML/specialized-ml/recommender-systems/recsys_offline_evaluation.md
---

# Recommender Objective ↔ Business Alignment

**Objective:** Examine the gap between what a recommender is *trained* to optimize (the trainable proxy label — clicks, watch-time, add-to-cart) and what the business *actually* wants (retention, lifetime value, satisfaction, trust), surfacing where the proxy and the goal diverge, and recommending objective design (label choice, multi-objective weighting, guardrails) that resists Goodhart-style degradation.

**When to Use:**
- Engagement metrics are up but retention/revenue/satisfaction is flat or declining (classic proxy divergence).
- Choosing the training label and objective for a new ranker.
- Suspected clickbait/dark-pattern amplification: the model optimizes a short-term signal that erodes long-term value.

**When NOT to Use:**
- For the mechanical retrieval+ranking design (use `recsys_candidate_ranking_design.md`).
- For systemic exposure/feedback bias (use `recsys_feedback_loop_bias_audit.md`).
- For offline metric mechanics (use `recsys_offline_evaluation.md`).

## Inputs / Context

Provide what you can:
- **Business objective** — the true north (retention, LTV, conversion quality, trust/safety), and how it's measured.
- **Current training label** — what the ranker actually optimizes (CTR, watch-time, dwell, purchases).
- **Observed symptoms** — any divergence (engagement up, retention down; complaints; regret signals).
- **Available long-term signals** — can you observe downstream outcomes (return visits, refunds, unsubscribes) to validate the proxy?
- **Guardrail tolerance** — what the business will accept trading off short-term engagement for long-term value.
- **Constraints** — label sparsity/delay (long-term signals are sparse and lagged), multi-stakeholder objectives.

## Constraints

**Must:**
- Distinguish the trainable proxy from the true objective and characterize *how* they correlate and *where* they diverge.
- Reason about Goodhart's law: once the proxy becomes the target, the model finds ways to lift it that may not serve the goal.
- Propose an objective design (single label, multi-objective weighting, guardrail metrics) with the divergence risk each carries.

**Must Not:**
- Assume the proxy is a faithful stand-in for the goal without evidence of their correlation (and its breakdown points).
- Recommend optimizing a long-term objective directly without addressing its sparsity/delay/attribution problems.
- Fabricate correlation strengths or lift numbers; reason from the user's signals and mark unknowns.

**Instructions:**

1. **State the true objective and the trainable proxy.** Write both explicitly. The proxy is what the loss function sees; the objective is what the business is paid for. Naming the gap is the whole point.

2. **Map proxy↔objective correlation.** Characterize where the proxy tracks the goal (often the common case) and where it diverges (clickbait lifts CTR but erodes trust; autoplay lifts watch-time but erodes satisfaction). Use any downstream signal the user has to ground this.

3. **Diagnose Goodhart failure modes.** Identify how an optimizer could lift the proxy in goal-harming ways: sensationalism, addictive loops, low-quality-but-clickable items, gaming by content producers.

4. **Choose the objective design.** Decide between: a better single label, a multi-objective combination (engagement + a long-term/quality term), or engagement-with-guardrails. State the weighting principle and how it's tuned.

5. **Handle long-term signal sparsity.** Long-term outcomes (retention, LTV) are delayed and sparse. Specify how to incorporate them — surrogate labels, delayed-reward modeling, or guardrail constraints — rather than naively training on them.

6. **Define guardrails and counter-metrics.** Specify metrics that must *not* regress (satisfaction proxies, diversity, complaint rate, unsubscribes) so a proxy win that harms the goal is caught.

7. **Specify validation.** State how to confirm the chosen objective actually serves the goal — A/B on the long-term metric with engagement as a guardrail (not the other way around), and ongoing monitoring of the proxy↔goal gap.

**Output Format:**

A markdown alignment analysis:
- **Objective vs Proxy** — the true goal and the trainable label, side by side.
- **Correlation & Divergence Map** — table: Scenario | Proxy moves | Goal moves | Aligned?
- **Goodhart Failure Modes** — how the proxy could be lifted while harming the goal.
- **Recommended Objective Design** — label/weighting/guardrails with rationale.
- **Long-Term Signal Handling** — surrogates / delayed reward / constraints.
- **Validation & Counter-Metrics** — A/B plan and the metrics that must not regress.

## Verification

- [ ] The true objective and the trainable proxy are both stated explicitly and distinguished.
- [ ] At least one concrete divergence scenario (proxy up, goal down) is identified with reasoning.
- [ ] Goodhart failure modes specific to this recommender are named, not generic.
- [ ] The objective design proposal includes guardrail/counter-metrics that must not regress.
- [ ] Long-term signal sparsity/delay is addressed rather than ignored.
- [ ] No fabricated correlation strengths or lift numbers.

## False-Positive Prevention

❌ **DON'T:**
- Assume CTR (or watch-time, or add-to-cart) is a safe proxy for the business goal — they correlate until the optimizer finds the divergence.
- Optimize a long-term metric (retention) directly without confronting its sparsity, delay, and attribution noise.
- Celebrate an engagement lift in an A/B without checking the goal metric and counter-metrics moved the right way.
- Recommend a multi-objective blend without saying how the weights are chosen or validated.

✅ **DO:**
- Separate the trainable proxy from the true objective and treat their gap as the central risk.
- Ground proxy↔goal correlation in observed downstream signals where they exist; mark it unknown where they don't.
- Use guardrail/counter-metrics so a proxy win that harms the goal is caught in the A/B.
- Run the A/B with the long-term goal as primary and engagement as a guardrail when divergence is the concern.

## Example Output

```markdown
## Objective Alignment: Video Recommendations

### Objective vs Proxy
- True objective: 90-day user retention + reported satisfaction (and ad LTV downstream).
- Trainable proxy: per-session watch-time (dense, immediate, what the ranker's loss sees).

### Correlation & Divergence Map
| Scenario | Proxy (watch-time) | Goal (retention/sat) | Aligned? |
|---|---|---|---|
| Genuinely engaging content | ↑ | ↑ | Yes |
| Autoplay rabbit-holes / outrage bait | ↑ | ↓ (regret, churn) | No |
| Long but low-quality filler | ↑ | flat/↓ | No |
| Satisfying short content | flat/↓ | ↑ | No (proxy understates) |

### Goodhart Failure Modes
Optimizer learns to surface sensational/cliffhanger content and long autoplay chains — watch-time rises, but post-session satisfaction surveys drop and 30-day return rate softens. Creators adapt by making more such content (a producer-side loop).

### Recommended Objective Design
Multi-objective ranking label: watch-time × completion-quality, with a satisfaction surrogate (survey-derived) as a re-rank guardrail. Weighting tuned to hold satisfaction flat-or-up while permitting watch-time gains. Not pure watch-time.

### Long-Term Signal Handling
Retention is sparse/delayed → not a direct training label. Use a satisfaction surrogate (predicted from short-horizon signals validated against survey data) plus a retention guardrail in the A/B.

### Validation & Counter-Metrics
A/B primary: 30-day retention. Guardrails that must not regress: satisfaction survey score, report/complaint rate, diversity of consumed creators. Reject a variant that lifts watch-time but regresses any guardrail.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** objective → correlation → Goodhart → design → long-term handling → validation.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances engagement, quality, satisfaction, and retention.
- **DS-02 (Metric Specification):** defines proxy labels, goal metrics, and guardrail counter-metrics.
- **CM-02 (Constraint Specification):** guardrails as hard constraints the objective must respect.
- **QA-12 (False Positives Identification):** catches the "engagement up = success" false positive when the goal regresses.

**Related Prompts:**
- `recsys_candidate_ranking_design.md` — where the chosen label and objective are implemented.
- `recsys_feedback_loop_bias_audit.md` — proxy-chasing amplifies producer-side feedback loops.
- `recsys_offline_evaluation.md` — choosing the online metric this objective must serve.
