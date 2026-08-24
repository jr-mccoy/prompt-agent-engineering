---
title: "Signal vs Noise Filter — Triage New Information Against an Existing Forecast"
category: reasoning-craft/forecasting
description: "Triage a stream of new information items against an existing forecast. Score each: signal or noise? Direction? Magnitude? Cumulative effect on forecast in the period? Recommended forecast adjustment (or none). Counters two failures: ignoring genuine signal and over-updating on noise."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - forecasting
  - signal
  - noise
  - update
  - triage
updated: "2026-05-10"
reasoning:
  styles: [bayesian, triage, calibration]
  stakes: variable
  horizon: variable
  uncertainty: variable
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: triage_table_plus_update
  user_role: [forecaster, analyst, investor, executive]
  mode: [audit, forecast]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md
  - domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
---

# Signal vs Noise Filter

**Objective:** Take an existing forecast and a flow of recent information items (news, data points, expert opinions, market moves). For each item, score: is this signal or noise? Direction? Magnitude? Cumulative effect on the forecast in the period? Recommend a forecast adjustment (or none) and which items to keep monitoring. Counters two failures: ignoring genuine signal and over-updating on noise.

**When to use:**
- Maintaining a forecast across a flow of new information.
- High-information environment (markets, breaking news, fast-moving events).
- After a notable news cycle: was that signal or noise relative to my forecast?
- Periodic review of an open forecast position.

**When NOT to use:**
- Pure ad-hoc reaction to a single item (use `reasoning_bayesian_belief_update.md`).
- No existing forecast to evaluate against (build the forecast first).
- The user wants to react to news without checking against forecast (different mode).

**Audience:** Forecasters, analysts, investors, executives maintaining live forecast positions.

---

## Inputs / Context

1. **Current forecast** (probability or value, with reasoning).
2. **Period** being triaged (last week, last month).
3. **List of new information items** in that period.
4. **Established tripwires** from `forecasting_what_would_change_my_mind.md` if any.

---

## Constraints

### Must
- Per item: classify as **signal** (genuinely diagnostic about the forecast question) or **noise** (correlated with topic but not diagnostic).
- For signal items: direction (up / down on the forecast), magnitude (small / moderate / large update), source quality.
- Check for **chained sources**: 5 articles citing the same study are 1 piece of signal.
- Check against **pre-committed tripwires**: did any trigger?
- Compute **cumulative effect** in the period (multiple small signals can compound; multiple noise items shouldn't).
- Output: recommended forecast adjustment (or none, with reason), items to keep watching.

### Must Not
- Treat every news item as signal (most isn't).
- Treat all signal items as independent (often they're correlated).
- Over-update on a single dramatic item without checking source quality.
- Under-update because "we already knew that" — sometimes the new specific is genuinely diagnostic.
- Skip the cumulative check; small signals can add up.

---

## Instructions

### Step 1 — Restate forecast
Current probability or value, brief reasoning.

### Step 2 — Per-item triage
| # | Item | Source | Signal/noise | Direction | Magnitude | Notes |
|---|------|--------|--------------|-----------|-----------|-------|
| 1 | [...] | [...] | signal | up | moderate | [chained to #3] |
| ... | | | | | | |

Signal vs noise test: would this item update an informed observer's forecast? If no, it's noise (interesting but not diagnostic).

### Step 3 — Chained-source collapse
Group items that cite the same primary source. Treat as one piece of evidence with magnitude of the strongest in the chain.

### Step 4 — Tripwire check
Did any pre-committed tripwire trigger? If yes, that item gets the magnitude assigned to the tripwire.

### Step 5 — Cumulative effect
Sum the directional moves across signal items. Multiple small same-direction signals → moderate cumulative move. Mixed signals → small or zero cumulative.

### Step 6 — Forecast adjustment recommendation
- New probability / value
- Magnitude of change from prior
- Reason: which items drove the change
- If no change: why (cumulative was within noise band, signals offset, etc.)

### Step 7 — Watch list for next period
Items that aren't yet signal but might become so; items that need second-source confirmation.

---

## False-Positive Prevention

1. **News-as-signal.** Most news cycles aren't diagnostic of any specific forecast.
2. **Over-update on dramatic single item.** Source quality matters more than vividness.
3. **Chained-source double-counting.** 5 op-eds citing the same study are 1 signal.
4. **Tripwire blindness.** If you pre-committed and the tripwire fired, honor it.
5. **Cumulative blindness.** Three small same-direction signals can be a moderate update.
6. **No-change theater.** Sometimes no-change is right; document the reasoning rather than skipping it.

---

## Output Format

```
# Signal vs noise — [forecast question, period]

## Current forecast (start of period)
- Probability / value: [...]
- Reasoning: [...]
- Tripwires: [list, status]

## Item triage
| # | Item | Source | Signal/noise | Direction | Magnitude | Chained? |
|---|------|--------|--------------|-----------|-----------|----------|
| 1 | [...] | [...] | signal | up | small | no |
| 2 | [...] | [...] | noise | — | — | — |
| ... | | | | | | |

## Chained-source collapse
- Group A (cite same study): items 3, 5, 7 → one signal of moderate magnitude
- Group B (independent): items 1, 4, 8

## Tripwire check
- [Tripwire X]: [triggered / not] → [implication]

## Cumulative effect
- Net signal direction: [up / down / mixed]
- Net signal magnitude: [small / moderate / large]
- Reasoning: [...]

## Forecast adjustment
- New probability / value: [...]
- Change from prior: [...]
- Driven by: [items]
- If no change: [reason]

## Watch list
- Items to monitor for confirmation: [...]
- Conditions that would convert noise to signal: [...]
```

---

## Verification

- [ ] Per-item signal/noise classification.
- [ ] Direction and magnitude for signals.
- [ ] Chained sources collapsed.
- [ ] Tripwire check performed.
- [ ] Cumulative effect computed, not just per-item.
- [ ] Forecast adjustment (or no-change with reason).
- [ ] Watch list for next period.
- [ ] No news-as-signal default.
