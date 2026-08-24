---
title: "Stage 4 — Screening / Opportunity Finder (Gate A: validated patterns only score)"
category: investment-research/screening
description: "Turn the universe plus dossiers into a ranked watchlist by scoring each candidate on which VALIDATED patterns fire and at what confidence. Enforces Gate A: hypothesis-status patterns appear only as unscored 'paper-only signal' and cannot influence the rank or score. Every ranking carries its evidence trail; missing inputs are queued, never assumed favorable."
techniques:
  - CM-02
  - DS-02
  - QA-04
  - NE-10
  - RT-06
difficulty: advanced
tags:
  - screening
  - opportunity-finder
  - watchlist
  - gate-a
  - ranking
  - validated-patterns
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/prompts/stage-1-universe-data-sourcing.md
  - ai-investment-research-toolkit/prompts/stage-2-deep-research.md
  - ai-investment-research-toolkit/prompts/stage-3-pattern-knowledge-base.md
  - ai-investment-research-toolkit/skills/pattern-knowledge-base/SKILL.md
  - referenced-prompts/domain-reasoning-craft/forecasting/forecasting_signal_vs_noise_filter.md
  - referenced-prompts/domain-finance/quant-fintech-data/finance_signal_decay_monitor.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Convert the Stage 1 universe and the Stage 2 dossiers into a ranked watchlist of opportunities,
scored by which **`validated`** patterns from the knowledge base fire on each candidate and with
what confidence. The load-bearing rule is **Gate A**: only patterns the knowledge base has
promoted to `validated` (out-of-sample, ≥ minimum sample size) may contribute to a candidate's
score or rank. `hypothesis`-status patterns may be *shown* as unscored "paper-only signal" but
can never move a candidate up the list. Every ranking ships with the evidence trail that
produced it; nothing is assumed favorable because data is missing.

## When to Use

- Producing or refreshing `data/output/watchlist.csv` on the research cadence (weekly sweep)
- Ranking which dossiers deserve monitoring (Stage 5) or a paper decision (Stage 6)
- Re-scoring after Stage 3 promotes/retires a pattern or Stage 7 resolves predictions
- Separating real, validated edges from interesting-but-unproven signals

## Inputs / Context Required

**Candidates & evidence**
- The Stage 1 universe (`data/snapshots/<as_of>/universe.csv`)
- The Stage 2 dossiers (`data/output/dossiers/<ticker>.md`)

**Patterns (the scoring rules)**
- `knowledge-base/patterns/PATTERN-*.md` with their `status` and `confidence`
- `knowledge-base/INDEX.md` for the at-a-glance status list
- The `pattern-knowledge-base` skill for what `validated` vs. `hypothesis` means (Gate A)

**Config**
- `config/mandate.yaml` — if `halt: true`, the kill switch stops this action stage
- `config/asset_classes.yaml` — which classes are in scope

## Constraints

### Must
- Count **only `validated` patterns** toward a candidate's score and rank; exclude `hypothesis`
  and `retired` patterns from scoring (CM-02 — this is Gate A enforced).
- Weight each firing pattern by its recorded `confidence`, and define the scoring rule
  explicitly so the ranking is reproducible (DS-02).
- Attach an **evidence trail** to every ranked candidate: which patterns fired, on what dossier
  facts, with what confidence (RT-06).
- Show `hypothesis`-status signals separately and clearly labeled "paper-only signal — unscored."
- Judge whether a firing is signal or noise before trusting it (reuse
  `forecasting_signal_vs_noise_filter.md`); flag patterns flagged as decaying (cross-check
  `finance_signal_decay_monitor.md`) (QA-04).
- **Reconcile records vs. INDEX before any screen (F18):** run
  `python skills/pattern-knowledge-base/scripts/validate_pattern.py --reconcile knowledge-base/patterns --index knowledge-base/INDEX.md`;
  a FAIL (status drift / missing record) **blocks screening** until fixed (route the fix to Stage 3).
- Honor the kill switch: if `halt: true`, do not emit an actionable watchlist (read-only only).

### Must Not
- Let any `hypothesis` (or `retired`) pattern contribute to the score or change the rank order
  (the single most important rule of this stage).
- Invent a pattern firing, a confidence, or a score where the dossier data is `UNAVAILABLE` —
  treat missing data as "cannot score," not as a pass (DS-02, QA-04).
- Produce a point-estimate "this will return X%" — the watchlist ranks opportunity strength, it
  does not forecast returns (NE-10).
- Assign position sizes or place orders (that is Stage 6, behind Gate B / Gate C).
- Quietly upgrade a decaying pattern's weight; respect decay flags.

## Instructions

0. **Reconcile before screening (F18).** Run the reconcile check; a FAIL blocks this stage:

   ```bash
   python skills/pattern-knowledge-base/scripts/validate_pattern.py \
     --reconcile knowledge-base/patterns --index knowledge-base/INDEX.md
   ```

   On FAIL (status drift / missing record), stop and route the fix to Stage 3 — do not screen on a
   stale or inconsistent knowledge base.

1. **Load validated patterns (CM-02 / Gate A).** From `knowledge-base/INDEX.md` and the
   `PATTERN-*.md` records, take only `status: validated` patterns as scoring rules. Note each
   one's `confidence` and `decay_estimate`. Set `hypothesis` patterns aside as unscored signals.

2. **Match patterns to candidates (RT-06).** For each candidate, check its dossier + snapshot
   facts against each validated pattern's `feature_definition`. Record which fired and the exact
   dossier facts that triggered each (the evidence trail). Where the needed fact is `UNAVAILABLE`,
   mark the pattern "cannot score," not "did not fire."

3. **Filter signal from noise (QA-04).** For each firing, apply
   `forecasting_signal_vs_noise_filter.md`; down-weight or drop firings that look like noise.
   Cross-check `finance_signal_decay_monitor.md` flags and respect any decay down-weighting.

4. **Score and rank (DS-02).** Combine the firing validated patterns by their confidence into a
   single, explicitly-defined score per candidate; rank descending. State the scoring formula so
   the result is reproducible. **Use the scorer — Gate A is enforced at ranking time, in code:**

   ```bash
   # firings.json = {"SYMBOL": {"PATTERN-0001": "evidence note", ...}, ...} (your dossier matches).
   # Each fired pattern is run through validate_pattern; ONLY status: validated patterns that PASS
   # count toward the score (weighted by confidence low=1/medium=2/high=3). hypothesis/retired
   # firings are emitted as UNSCORED "paper-only signal" and can never move the rank.
   python skills/pattern-knowledge-base/scripts/screen_rank.py \
     --firings firings.json --patterns-dir knowledge-base/patterns --out data/output/watchlist.csv
   ```

5. **Surface unscored signals separately.** List `hypothesis`-pattern firings as "paper-only
   signal" in a distinct section — visible for monitoring, never affecting the rank.

6. **Write the watchlist.** Save `data/output/watchlist.csv` with rank, score, firing patterns,
   confidence, and an evidence-trail reference. Summarize coverage and what was un-scoreable.

## Output Format

```
## WATCHLIST: as_of [date] | Scored on VALIDATED patterns only (Gate A) | Mode: [live/manual]
```

### Ranked candidates (scored — validated patterns only)
| Rank | Symbol | Class | Score | Validated patterns fired (confidence) | Evidence trail ref |
|---|---|---|---|---|---|
| 1 | … | … | … | PATTERN-00xx (high), … | dossier §… |

### Scoring rule (reproducible)
- Formula: [how pattern confidences combine into the score] (DS-02)
- Signal/noise filter applied: [yes — summary] · Decay flags respected: [list]

### Paper-only signals (UNSCORED — hypothesis-status patterns)
| Symbol | Hypothesis pattern fired | Why not scored |
|---|---|---|
| … | PATTERN-00yy (hypothesis) | Gate A: not validated |

### Coverage & un-scoreable
| Symbol | Pattern | State | Reason |
|---|---|---|---|
| … | PATTERN-00xx | cannot score | dossier field UNAVAILABLE (queued) |

### Gate A statement
- Patterns used for scoring: [only `validated` — count] · Excluded: [hypothesis/retired count]
- Kill switch (`halt`): [false → watchlist emitted / true → read-only]

## Verification

- [ ] `--reconcile` PASSed before screening; a FAIL blocked the stage until fixed (F18).
- [ ] Only `validated` patterns contributed to scores and ranks (Gate A).
- [ ] `hypothesis` firings appear only in the separate, clearly-labeled unscored section.
- [ ] The scoring formula is stated and reproducible; confidences are applied.
- [ ] Every ranked candidate has an evidence trail (patterns + dossier facts).
- [ ] `UNAVAILABLE` data → "cannot score," never a silent pass.
- [ ] Signal/noise filter applied; decay flags respected.
- [ ] No position sizes or orders; no point-estimate return forecasts.
- [ ] Kill switch honored.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| An unproven (hypothesis) pattern inflates a candidate's rank | Gate A: only `validated` patterns score; hypotheses are unscored signals |
| Missing data treated as a passing/favorable result | `UNAVAILABLE` → "cannot score," shown explicitly (DS-02, QA-04) |
| A lucky one-off firing trusted as edge | Apply `forecasting_signal_vs_noise_filter.md` before scoring |
| A decayed edge keeps its old weight | Respect `finance_signal_decay_monitor.md` flags; down-weight/exclude |
| Ranking read as a return forecast | Score ranks opportunity strength only; no point return claims (NE-10) |
| Opaque score nobody can reproduce | Scoring formula stated explicitly (DS-02) |
| Screen drifts into sizing/ordering | Sizing/orders are Stage 6 behind Gate B/C — out of scope here |
