---
title: "Multi-Turn Drift Diagnosis"
category: prompt-engineering/debugging
description: "Locate the turn at which a long conversation's behavior degraded (style drift, rule abandonment, persona slip, format loss)."
techniques:
  - ST-02
  - QA-01
  - PR-01
  - PR-02
  - DC-01
difficulty: advanced
tags:
  - multi_turn
  - drift
  - long_conversation
  - debugging
  - regression
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/debugging/debug_failure_mode_taxonomy.md
  - domain-prompt-engineering/debugging/debug_first_failure_cause_isolator.md
  - domain-prompt-engineering/agent-workflows/
---

## Objective

For a conversation transcript where final-turn behavior is unacceptable, locate the earliest turn at which a measurable behavior metric crossed a threshold and emit the candidate cause.

## When to Use

- Long agent runs that start aligned but end off-spec.
- Persona slip (the model stopped staying in character).
- Format loss after many tool calls.
- Rule abandonment after several user counter-arguments.

## Inputs

- `TRANSCRIPT`: ordered list of turns, each `{ role, content }`.
- `BEHAVIOR_METRICS`: list of named metrics, each with a per-turn measurement function. Examples:
  - `format_valid` (bool)
  - `persona_first_person_count` (int)
  - `rule_R3_violation` (bool)
  - `style_token_set_distance_from_turn_0` (float)
- `THRESHOLDS`: per-metric value at which a turn is "drifted."

## Drift Causes (taxonomy, choose one per metric)

| Code | Cause | Signature |
|------|-------|-----------|
| D1 | Context truncation | A SYSTEM rule visible at turn 0 is no longer in active context window at drift turn. |
| D2 | User pressure | Drift turn is preceded by user input that argues against the rule. |
| D3 | Tool result pollution | A tool result inserted before drift turn contains contradictory style or content. |
| D4 | Self-conditioning | Model's own prior outputs reinforced the off-spec behavior across turns. |
| D5 | Topic shift | Drift turn introduces a new topic the prompt did not cover. |
| D6 | Length pressure | Cumulative tokens approaching context limit; recency-weighted attention. |
| D7 | Sampling noise | No structural cause; isolated turn at high temperature. |

## Constraints

### Must
- Compute every metric for every turn (turn 0 = baseline).
- Locate the earliest turn `t*` where any metric crosses its threshold; report it.
- Emit at least one cause from D1–D7 with cited evidence (specific prior turn(s) or token-count check).
- For each metric, plot the trajectory (text-table form is fine).
- If the threshold is never crossed, output `NO_DRIFT_DETECTED` and stop.

### Must Not
- Combine metrics into a single composite score.
- Re-run the conversation; analyze the existing transcript only.
- Recommend "use a longer context window" without confirming D1.

## Instructions

1. Compute baseline metric values from turn 0.
2. Walk turns; flag the first turn each metric crosses its threshold; record `t*_metric`.
3. For the earliest `t* = min(t*_metric)`:
   - Check D1: locate SYSTEM rule, compute approximate token offset to drift turn, compare to model's known active window.
   - Check D2: scan turns `t*-3..t*-1` for argumentative user content against the violated rule.
   - Check D3: scan tool results in `t*-3..t*` for contradictory content.
   - Check D4: check whether model's own outputs in `0..t*-1` already showed direction toward drift.
   - Check D5: detect topic novelty via term-set comparison.
   - Check D6: cumulative token count at `t*` vs known context length.
   - Check D7: only if D1–D6 all negative.
4. Pick the earliest-applying cause; if multiple, prefer D1 > D3 > D2 > D4 > D5 > D6 > D7.

## Output Format

```
DRIFT_TURN: t*=<n> (out of <T>)
PRIMARY_METRIC_CROSSED: <metric>
THRESHOLD: <value>; OBSERVED_AT_t*: <value>

METRIC_TRAJECTORY
| turn | format_valid | persona_first_person | R3_violation | style_dist |
|------|---------------|----------------------|--------------|------------|
| 0    | true          | 0                    | false        | 0.00       |
| 5    | true          | 1                    | false        | 0.12       |
| 12   | true          | 6                    | true         | 0.41       |  ← t*
| 13+  | …             | …                    | …            | …          |

CAUSE
code: D2
evidence: "User turn 11 said: 'You are too strict; just give me the answer.' Model adopted softer stance from turn 12."

REMEDIATION
- D2 → re-inject SYSTEM rule via developer message between turns; harden rule wording.
- D1 → use rolling summary or sticky system block.
- D3 → add tool-result sanitization rule.
- D4 → periodic self-audit prompt every K turns.
- D6 → trim transcript with summarization at <threshold>.
```

## Verification

- `t*` is the earliest crossing across all metrics? (yes/no)
- Cause cites a specific prior turn or token-count value? (yes/no)
- Re-apply remediation in a fresh run of the same script; confirm `t*` shifts later or disappears.

## Examples

In a 30-turn agent run, format_valid stays true throughout but `R3_violation` flips at turn 18, three turns after a tool result returned plain prose without the schema prefix. Cause: D3.
