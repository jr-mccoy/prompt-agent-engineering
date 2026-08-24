---
title: "ML Feedback Loop Detection"
category: AI-ML/production-monitoring
description: "Detect and break harmful feedback loops where a model's own outputs contaminate the data it later trains on — runaway bias, popularity collapse, and self-fulfilling labels — with evidence and counterfactual checks."
techniques:
  - RT-09
  - RT-10
  - ST-02
  - RT-05
  - QA-12
difficulty: advanced
tags:
  - feedback-loops
  - exposure-bias
  - self-fulfilling-labels
  - data-contamination
  - causality
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_retraining_trigger_strategy.md
  - domain-AI-ML/production-monitoring/mlmonitor_data_pipeline_health_audit.md
  - domain-AI-ML/production-monitoring/mlmonitor_drift_detection_design.md
---

# ML Feedback Loop Detection

**Objective:** Detect feedback loops in which a deployed model's outputs influence the future data used to train or evaluate it — causing exposure bias, self-fulfilling labels, popularity runaways, or degenerate narrowing — and design the interventions that break the loop, anchoring every claim of a loop to a mechanism and a counterfactual rather than a correlation that merely looks self-reinforcing.

**When to Use:**
- A model's behavior is narrowing or amplifying over successive retrains (recommendations get more uniform, a fraud model stops seeing patterns it blocks, a ranker entrenches early winners).
- Designing a retraining pipeline where outputs become future training data and you want to prevent contamination up front.
- Investigating why offline metrics improve while real-world diversity/quality erodes.

**When NOT to Use:**
- For ordinary input drift unrelated to the model's own actions (use `mlmonitor_drift_detection_design.md`).
- To design the retraining triggers/guardrails broadly (use `mlmonitor_retraining_trigger_strategy.md`).
- For non-self-referential data-quality issues (use `mlmonitor_data_pipeline_health_audit.md`).

## Inputs / Context

Provide what you can:
- **Decision-data coupling** — how the model's outputs affect what data is collected (what gets shown, blocked, approved, surfaced).
- **Label provenance** — where training labels come from, and whether they are generated downstream of the model's decisions.
- **Retraining flow** — does the model train on logs of its own outputs/served items? With what frequency?
- **Observed symptoms** — narrowing diversity, popularity concentration, vanishing categories, metric/reality divergence.
- **Exploration** — any randomized/exploration traffic, holdouts, or counterfactual logging in place.
- **Timeframe** — how behavior changed across versions/retrains.

## Constraints

**Must:**
- Identify the specific mechanism by which outputs re-enter training/eval data before naming a "feedback loop" — name the path, not the vibe.
- Distinguish a true self-reinforcing loop from independent external drift or a one-off shift, using a counterfactual or exploration-based check.
- Separate the loop *type* (exposure/selection bias, self-fulfilling labels, popularity runaway, degenerate narrowing) because the break differs by type.

**Must Not:**
- Declare a feedback loop from a trend alone (e.g., "popularity is concentrating") without showing the model's decisions cause the data shift.
- Recommend retraining as the fix — retraining on contaminated data *amplifies* the loop.
- Assume exploration data exists; if there is no counterfactual signal, say the loop is *suspected* and specify what to instrument.

**Instructions:**

1. **Map the output-to-data path.** Trace exactly how predictions influence future data: what gets shown/hidden, approved/blocked, ranked, and how labels are generated from those decisions. If outputs never re-enter the data, there is no loop — say so.

2. **Classify the loop type.** Exposure/selection bias (only acted-on items get labels), self-fulfilling labels (the decision creates the outcome it predicted), popularity/rich-get-richer runaway (surfaced items get more interaction → surfaced more), degenerate narrowing (diversity collapses over retrains). State which apply.

3. **Gather evidence of self-reinforcement.** Look for monotonic narrowing/amplification across retrains, divergence between offline metrics and real-world diversity/quality, and unobserved regions the model stopped collecting data on (the "things it never shows" blind spot).

4. **Run the counterfactual test.** Use exploration/randomized traffic or a holdout that bypasses the model to estimate what the data/outcomes would be absent the model's steering. A gap between observed and counterfactual is the loop's signature; without such data, mark the loop suspected and specify the instrumentation needed.

5. **Quantify the harm.** Estimate the loop's cost: lost diversity, entrenched bias against a group, missed fraud patterns the model now blocks unseen, or eval metrics that flatter a degrading system.

6. **Design the loop-break interventions.** Match to type: hold out randomized exploration traffic and over-weight it in training; inverse-propensity / counterfactual reweighting to de-bias logged data; quarantine model-influenced labels from training; inject diversity/anti-concentration constraints; collect ground truth on blocked/unshown items.

7. **Design ongoing monitoring.** Specify signals that catch a loop forming: diversity/concentration metrics over time, offline-vs-counterfactual metric gap, and coverage of the action space — so the loop is caught early next time.

8. **Re-validate without contamination.** Specify how to evaluate the model on uncontaminated (exploration/holdout) data so the fix's effect is measured honestly, not on the loop's own self-confirming logs.

**Output Format:**

A markdown analysis:
- **Output→Data Path** — the mechanism, or a statement that no loop exists
- **Loop Type(s) Identified** — with the path each follows
- **Evidence of Self-Reinforcement** — trends + offline-vs-reality divergence
- **Counterfactual Check** — observed vs counterfactual, or what to instrument if absent
- **Harm Estimate** — what the loop is costing
- **Loop-Break Interventions** — matched to type, ranked
- **Ongoing Monitoring & Uncontaminated Re-Validation**
- **INSUFFICIENT EVIDENCE** — the correct conclusion when no counterfactual or exploration data exists. Logged outcomes are generated under the model's own choices, so they cannot on their own separate a self-reinforcing loop from a real shift in behaviour. Name the unblocking datum: an exploration slice or a held-out unpersonalized arm, and the period it must cover.

## Verification

- [ ] The specific output-to-data mechanism is named (or absence of a loop is stated).
- [ ] The loop is classified by type, since the fix depends on type.
- [ ] Self-reinforcement is supported by a trend AND an offline-vs-reality or counterfactual signal.
- [ ] Counterfactual/exploration evidence is used, or the loop is marked suspected with instrumentation specified.
- [ ] Retraining is not proposed as the fix on contaminated data.
- [ ] Interventions include collecting data on unshown/blocked items where relevant.
- [ ] Absent counterfactual or exploration data, the loop verdict is INSUFFICIENT EVIDENCE with the exploration slice named — logged outcomes alone do not establish a loop.

## False-Positive Prevention

❌ **DON'T:**
- Call concentration a feedback loop when an external trend (a viral event, seasonality) drives it.
- Infer a loop from a self-confirming metric computed only on the model's own served logs.
- Recommend "just retrain" — that trains on the contaminated logs and tightens the loop.
- Ignore the blind spot: items the model never shows generate no data, so the logs look fine.

✅ **DO:**
- Trace the concrete output→data path and require a counterfactual gap before declaring a loop.
- Evaluate on exploration/holdout data that bypasses the model's steering.
- Break the loop with reweighting/exploration/label-quarantine, then retrain on de-biased data.
- Monitor diversity/coverage and the offline-vs-counterfactual gap over time.

## Example Output

```markdown
## Feedback Loop Analysis: News Recommender v5

### Output→Data Path
- Model ranks articles → top-ranked get impressions → only impressed articles get click labels → next retrain trains on those clicks. Unshown articles get zero labels.

### Loop Type(s) Identified
- Exposure/selection bias (labels only for shown items) + popularity runaway (clicked items rank higher → shown more).

### Evidence of Self-Reinforcement
- Catalog coverage in served slates fell 41% → 12% of articles over 6 retrains. Offline CTR rose each retrain while editorial-measured topic diversity dropped. Bottom 80% of articles now receive ~0 impressions.

### Counterfactual Check
- 2% randomized-exposure holdout shows clicked-through rate on currently-suppressed articles is only 9% below top articles — far less than their ~0 impression share implies. Gap = loop signature, not genuine quality difference.

### Harm Estimate
- Long-tail starvation; new/niche content never surfaces; CTR metric flatters a narrowing system. Editorial diversity SLO breached.

### Loop-Break Interventions (ranked)
1. Over-weight the 2% exploration traffic in training; add inverse-propensity weighting to logged clicks.
2. Quarantine pure-exploitation logs from being the sole training signal.
3. Add an anti-concentration / diversity constraint to ranking.
4. Increase exploration share to 5% temporarily to rebuild coverage.

### Ongoing Monitoring & Uncontaminated Re-Validation
- Track served-catalog coverage + Gini concentration per retrain; alert on monotonic narrowing.
- Re-validate CTR/diversity on the exploration holdout only — never on exploitation logs.
```

**Techniques Used:**
- **RT-09 (Root Cause Explanation):** the loop is explained as a concrete output→data mechanism.
- **RT-10 (Troubleshooting Decision Tree):** classify-then-test branches by loop type.
- **ST-02 (Structured Sequential Instructions):** path → type → evidence → counterfactual → break sequence.
- **RT-05 (Evidence-Based Reasoning):** requires counterfactual/exploration evidence, not trend-alone.
- **QA-12 (False Positives Identification):** separates true loops from external drift and self-confirming-log artifacts.

**Related Prompts:**
- `mlmonitor_retraining_trigger_strategy.md` — the guardrails that keep retraining off contaminated data.
- `mlmonitor_data_pipeline_health_audit.md` — audit label provenance feeding the loop.
- `mlmonitor_drift_detection_design.md` — distinguish self-reinforcing loops from external drift.
```