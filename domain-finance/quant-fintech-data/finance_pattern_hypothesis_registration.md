---
title: "Pattern Hypothesis Registration — Pre-Commit the Claim Before Inspecting Outcomes"
category: finance/quant-fintech-data
description: "Pre-register a candidate trading/investing pattern as a falsifiable hypothesis BEFORE looking at outcomes: a precise, reproducible feature definition, the sample frame, the base rate it must beat, the expected effect and direction, and how many features were screened — so the later test cannot become a post-hoc story. Produces a registration record ready for an out-of-sample validation protocol."
techniques:
  - QA-02
  - CM-02
  - DS-02
  - NE-11
  - QA-04
difficulty: advanced
tags:
  - pre-registration
  - hypothesis
  - overfitting
  - base-rate
  - feature-definition
  - research-discipline
updated: "2026-06-18"
related_prompts:
  - domain-finance/quant-fintech-data/finance_out_of_sample_validation_protocol.md
  - domain-finance/quant-fintech-data/finance_backtest_design_critique.md
  - domain-reasoning-craft/forecasting/forecasting_base_rate_establishment.md
  - ai-investment-research-toolkit/skills/pattern-knowledge-base/SKILL.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Pre-registration reduces self-deception but does not make a pattern profitable. All outputs require independent verification before any capital is committed.**

## Objective

Lock down the claim before the data can talk you into a story. This prompt produces a
pre-registration record for a candidate pattern: a precise, reproducible feature definition, the
population and date range it applies to, the base rate it must beat, the expected effect and
direction, and an honest count of how many features were screened to surface this one. Registering
*before* inspecting outcomes is what separates a testable hypothesis from a post-hoc narrative —
it is the entry condition for the out-of-sample validation protocol and for Gate A in the
investment-research toolkit's pattern knowledge base.

## When to Use

- Before testing any candidate pattern/signal for predictive value
- Registering a pattern in the toolkit's knowledge base (`pattern-knowledge-base` skill, Stage 3)
- Converting a vague "I think X tends to precede Y" hunch into a falsifiable, testable claim
- Documenting the multiple-comparisons context (how many ideas were tried) before validation

## Inputs / Context Required

**The candidate claim**
- The hunch in plain language (what signal, what outcome, what population, what horizon)
- Asset class(es) in scope

**For a reproducible registration**
- A precise definition of how the signal is computed (data fields, thresholds, timing)
- The sample frame: universe + date range; how failures/delistings are handled (survivorship)
- The outcome definition and horizon (what counts as success/failure, measured how)
- How many features/ideas were screened in the search that produced this one
- Any input not yet known → mark `UNAVAILABLE` and queue it (DS-02)

## Constraints

### Must
- Register BEFORE inspecting outcomes; set the registration date and state explicitly that
  outcomes have not been examined (or, if they have, declare it and require a fresh holdout)
  (QA-02, CM-02).
- Make the feature definition precise enough to recompute identically by someone else (DS-02).
- State the base rate the pattern must beat — the outcome frequency in the sample frame WITHOUT
  the signal (NE-11; reuse `forecasting_base_rate_establishment.md`).
- Pre-commit the expected effect, direction, and a minimum effect size worth caring about (CM-02).
- Record the number of features screened (multiple-comparisons context) (QA-02).
- Handle survivorship in the sample-frame definition (keep delisted/failed names) (QA-04).

### Must Not
- Inspect or peek at outcomes before completing the registration.
- Leave the feature definition vague ("strong momentum", "cheap") — it must be computable.
- Set the base rate after seeing results, or omit it.
- Hide how many variants were tried to find this pattern.
- Invent a base rate, sample size, or effect figure — queue unknowns (DS-02).

## Instructions

1. **State the falsifiable hypothesis (CM-02).** One sentence: "<signal> predicts <outcome> over
   <horizon> in <population>, with effect <direction/size>." If it cannot be falsified, sharpen it.

2. **Define the feature precisely (DS-02).** Specify the exact computation: data fields, lookback,
   thresholds, timing (point-in-time, no look-ahead). Someone else must be able to reproduce it.

3. **Define the sample frame and outcome (QA-04).** Universe + date range; outcome definition and
   measurement; horizon. Explicitly keep failures/delistings (survivorship). Note any split you
   intend (train vs. reserved holdout) for the validation step.

4. **Establish the base rate (NE-11).** Compute (or queue) the outcome frequency in the sample
   frame absent the signal — the bar the pattern must clear. Reuse
   `forecasting_base_rate_establishment.md`.

5. **Pre-commit effect & multiple comparisons (QA-02).** Record expected direction, a minimum
   effect size worth acting on, and how many features/ideas were screened. The more screened, the
   higher the out-of-sample bar the validation protocol will require.

6. **Freeze the registration (CM-02).** Stamp the registration date; confirm outcomes were not
   inspected. Output the record in the schema the knowledge base expects.

## Output Format

```
## PATTERN REGISTRATION: [working title] | registered_on [date] | Outcomes inspected? [NO / declared]
```

### Hypothesis
- Falsifiable claim: "<signal> predicts <outcome> over <horizon> in <population>, effect <dir/size>."

### Feature definition (reproducible)
| Element | Specification |
|---|---|
| Data fields | … |
| Computation / thresholds | … |
| Timing (point-in-time) | … |

### Sample frame, outcome & base rate
| Field | Value |
|---|---|
| Universe + date range | … |
| Survivorship handling | keep delisted/failed: yes |
| Outcome definition + horizon | … |
| Base rate (no signal) | … (or queued) |
| Planned train/holdout split | … |

### Pre-committed effect & multiple comparisons
- Expected direction · minimum effect size · features screened (count)

### Open items (queued, not guessed)
- `UNAVAILABLE` fields awaiting data

## Verification

- [ ] Registration completed before outcome inspection (or fresh holdout reserved if not).
- [ ] Feature definition is precise and reproducible (no vague terms).
- [ ] Sample frame stated; survivorship handled (failures retained).
- [ ] Base rate stated (or explicitly queued) as the bar to beat.
- [ ] Expected direction, minimum effect, and features-screened count recorded.
- [ ] Registration date stamped; no invented figures (unknowns queued).

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Post-hoc story sold as a hypothesis | Register before inspecting outcomes; declare + reserve holdout if peeked (QA-02) |
| Vague feature can't be retested | Require computable, point-in-time feature definition (DS-02) |
| No bar to beat | Mandatory base rate before testing (NE-11) |
| Multiple comparisons hidden | Record features-screened count up front (QA-02) |
| Survivorship inflates the sample | Sample frame keeps delisted/failed names (QA-04) |
| Missing inputs filled with guesses | `UNAVAILABLE` + queue (DS-02) |
