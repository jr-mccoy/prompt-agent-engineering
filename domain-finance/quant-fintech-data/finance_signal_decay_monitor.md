---
title: "Signal Decay Monitor — Detect a Fading Edge and Trigger Pattern Retirement"
category: finance/quant-fintech-data
description: "Monitor a validated pattern for edge decay: track rolling lift over the base rate, test for regime sensitivity and crowding, distinguish a real decline from normal sampling noise, and emit a keep / watch / retire verdict with a pre-committed retirement trigger. Closes the loop on the pattern lifecycle so decayed edges are retired honestly rather than ridden into losses."
techniques:
  - QA-02
  - NE-11
  - NE-10
  - DS-02
  - QA-04
difficulty: advanced
tags:
  - signal-decay
  - edge-decay
  - regime-change
  - crowding
  - pattern-retirement
  - monitoring
updated: "2026-06-18"
related_prompts:
  - domain-finance/quant-fintech-data/finance_out_of_sample_validation_protocol.md
  - domain-finance/quant-fintech-data/finance_pattern_hypothesis_registration.md
  - domain-reasoning-craft/forecasting/forecasting_signal_vs_noise_filter.md
  - ai-investment-research-toolkit/prompts/stage-3-pattern-knowledge-base.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Edges decay, often silently and faster once crowded; detecting decay does not recover losses already taken. All outputs require independent verification before any capital is committed.**

## Objective

Tell whether a previously-validated pattern still works — and retire it before it quietly turns
into a losing bet. The monitor tracks the pattern's rolling lift over its base rate, tests whether
a decline reflects a regime change or crowding rather than noise, and returns a **keep / watch /
retire** verdict against a pre-committed retirement trigger. It is the lifecycle counterpart to
the validation protocol: validation earns a pattern the right to drive decisions; this monitor
takes that right away when the edge is gone.

## When to Use

- Re-reviewing `validated` patterns on a cadence as new resolved outcomes arrive (Stage 3/7 loop)
- Deciding whether a recent run of misses is decay or normal variance
- Setting or checking a pattern's pre-committed retirement trigger
- Diagnosing whether crowding or a regime shift has eroded an edge

## Inputs / Context Required

**The pattern & its history**
- The pattern's registration + validation record (feature definition, base rate, original
  out-of-sample lift, minimum sample size)
- A time series of outcomes since validation (ideally resolved predictions from the journal),
  enough to compute rolling lift
- The pre-committed retirement trigger if one exists (e.g. "retire if rolling lift ≤ 0 over N
  resolved outcomes")

**Context**
- Regime markers over the window (volatility regime, rates, sector/asset-class conditions)
- Evidence of crowding (capacity pressure, popularity of the signal)
- Any input unavailable → mark `UNAVAILABLE` and queue (DS-02)

## Constraints

### Must
- Track rolling lift over the base rate through time and compare it to the original validated lift,
  with embedded computation (NE-11).
- Distinguish genuine decay from sampling noise before declaring decline (reuse
  `forecasting_signal_vs_noise_filter.md`) (QA-04).
- Test regime sensitivity and crowding as explanations for a decline (QA-02).
- Compare against a pre-committed retirement trigger; if none exists, define one now (DS-02).
- Emit a keep / watch / retire verdict with a dated reason; on retire, write the status change back
  to the knowledge base (DS-02).
- Present the rolling lift with an uncertainty band, not a single point (NE-10).

### Must Not
- Retire (or keep) on a single window of outcomes without a noise check.
- Attribute decay to "the market changed" without examining regime/crowding evidence.
- Move the retirement trigger after seeing results to avoid retiring (trigger discipline).
- Keep relying on a pattern whose rolling lift has fallen below its base rate over a sufficient
  sample.
- Invent rolling-lift figures or regime data — queue unknowns (DS-02).

## Instructions

1. **Recompute rolling lift (NE-11).** Over a rolling window of resolved outcomes, compute lift
   over the base rate: `rolling_lift = rate_with_signal(window) − base_rate`. Plot/tabulate the
   trajectory vs. the original validated lift.

2. **Noise check (QA-04).** Apply `forecasting_signal_vs_noise_filter.md`: is the decline larger
   and more persistent than expected sampling variation given the window size? Present the band.

3. **Explain the decline (QA-02).** Test regime sensitivity (does the edge concentrate in certain
   volatility/rate/sector regimes that have now changed?) and crowding (capacity pressure, the
   signal becoming widely known). Distinguish "temporarily out of regime" from "structurally gone."

4. **Compare to the trigger (DS-02).** Evaluate against the pre-committed retirement trigger. If no
   trigger exists, define one (e.g. rolling lift ≤ 0 over N resolved outcomes, or band fully below
   the original lift) and record it.

5. **Verdict and write-back (DS-02, NE-10).** Emit keep / watch / retire with a dated reason citing
   rolling lift, sample size, and the trigger. On `retire`, update the pattern's `status` (and the
   knowledge-base index) and stop it from driving decisions. List queued unknowns.

## Output Format

```
## DECAY REVIEW: [pattern] | as_of [date] | Verdict: [KEEP / WATCH / RETIRE]
```

### Rolling lift trajectory
| Window | n | Rolling lift vs. base rate | vs. original validated lift |
|---|---|---|---|
| … | … | … (band: …) | … |

### Decline diagnosis
| Explanation | Evidence | Verdict |
|---|---|---|
| Sampling noise | … | … |
| Regime change | … | … |
| Crowding / capacity | … | … |

### Trigger & verdict
- Pre-committed retirement trigger: … (defined now if absent)
- **[KEEP / WATCH / RETIRE]** — dated reason citing rolling lift, n, and trigger
- Write-back: status set to `[validated / watch / retired]`; index updated: [yes/no]

### Open items (queued, not guessed)
- `UNAVAILABLE` inputs

## Verification

- [ ] Rolling lift over base rate computed across windows and compared to the original lift.
- [ ] Decline tested against sampling noise before any verdict (band shown).
- [ ] Regime sensitivity and crowding examined as explanations.
- [ ] Verdict compared to a pre-committed retirement trigger (defined if absent).
- [ ] On retire, status written back and the pattern stopped from driving decisions.
- [ ] No invented figures; unknowns queued.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Retiring on one unlucky window | Mandatory noise check with band before verdict (QA-04) |
| "Market changed" asserted without evidence | Require regime + crowding diagnosis (QA-02) |
| Trigger moved to avoid retiring | Trigger discipline: pre-committed, not adjusted post-hoc |
| Dead edge ridden into losses | Retire when rolling lift falls below base rate over sufficient n |
| Decay called from a point estimate | Present rolling lift with an uncertainty band (NE-10) |
| Missing outcome/regime data guessed | `UNAVAILABLE` + queue (DS-02) |
