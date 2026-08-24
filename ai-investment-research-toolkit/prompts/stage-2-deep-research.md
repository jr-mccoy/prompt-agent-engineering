---
title: "Stage 2 — Deep Research (per-candidate dossier, asset-class aware)"
category: investment-research/deep-research
description: "Produce a structured, falsifiable dossier per candidate by orchestrating the existing domain-finance research prompts and branching by asset class (equity / crypto / options). Output is a thesis with a variant view, a valuation range, dated catalysts, ranked risks, a pre-committed disconfirming test, and per-asset-class specifics — built only from the Stage 1 snapshot, with unknowns queued."
techniques:
  - RT-05
  - NE-10
  - QA-02
  - DS-02
  - QA-04
difficulty: advanced
tags:
  - deep-research
  - investment-thesis
  - dossier
  - asset-class
  - valuation-range
  - disconfirming-test
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/prompts/stage-1-universe-data-sourcing.md
  - ai-investment-research-toolkit/prompts/stage-4-screening.md
  - referenced-prompts/domain-finance/investing-research/finance_investment_thesis_builder.md
  - referenced-prompts/domain-finance/investing-research/finance_competitive_moat_analyzer.md
  - referenced-prompts/domain-finance/investing-research/finance_catalyst_map_builder.md
  - referenced-prompts/domain-finance/investing-research/finance_short_thesis_constructor.md
  - referenced-prompts/domain-finance/valuation/finance_reverse_dcf_expectations.md
  - referenced-prompts/domain-finance/crypto/finance_token_valuation_framework.md
  - referenced-prompts/domain-finance/crypto/finance_onchain_metrics_analysis.md
  - referenced-prompts/domain-finance/crypto/finance_smart_contract_risk_review.md
  - referenced-prompts/domain-finance/options/finance_options_structure_selector.md
  - referenced-prompts/domain-finance/options/finance_implied_vol_greeks_analysis.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Turn one candidate's Stage 1 snapshot into a structured, falsifiable dossier that Stage 4 can
score and Stage 6 (later) could act on — on paper. This stage does not rebuild analytical
method; it **orchestrates the existing `domain-finance` prompts** (referenced by path) and adds
the asset-class depth each candidate needs. Every dossier carries an explicit variant view
versus consensus, a valuation *range* (not a point), dated catalysts, ranked risks, and a
pre-committed disconfirming test that becomes the prediction's tripwire in Stage 7. It is built
strictly from the snapshot; anything not in the snapshot is queued, not invented.

## When to Use

- Building or refreshing a dossier for a candidate that cleared the Stage 1 universe
- Adding asset-class specifics (tokenomics/on-chain/contract risk; IV/Greeks/structure)
- Preparing the falsifiable claim + disconfirming test that Stage 7 will journal and score
- Re-researching a name when a new snapshot or a resolved prediction changes the picture

## Inputs / Context Required

**From Stage 1**
- The candidate's point-in-time data under `data/snapshots/<as_of>/` (prices/volume,
  fundamentals, filings; on-chain for tokens; chains/IV for options) — with provenance and any
  `UNAVAILABLE` fields already queued
- The candidate's asset class

**Reused analytical prompts (referenced by path, not copied)**
- Equity / general: `finance_investment_thesis_builder.md`, `finance_competitive_moat_analyzer.md`,
  `finance_catalyst_map_builder.md`, `finance_reverse_dcf_expectations.md`,
  `finance_short_thesis_constructor.md` (for short/bear framing)
- Crypto: `finance_token_valuation_framework.md`, `finance_onchain_metrics_analysis.md`,
  `finance_smart_contract_risk_review.md`
- Options: `finance_options_structure_selector.md`, `finance_implied_vol_greeks_analysis.md`

**Config**
- `config/asset_classes.yaml` (which specifics apply); `config/mandate.yaml` (halt switch)

## Constraints

### Must
- Build only from the Stage 1 snapshot; cite the snapshot date as the information cutoff (QA-05,
  via Stage 1 provenance). Treat the dossier as point-in-time.
- State an explicit **variant view**: what you believe that consensus does not, and why (RT-05).
- Express valuation as a **range with scenarios** (bear / base / bull), never a single number
  (NE-10).
- Include dated catalysts and a ranked risk list; for each candidate, pre-commit a **disconfirming
  test** ("what would change my mind") that Stage 7 will track (QA-02).
- Branch by asset class and complete the class-specific section (crypto tokenomics/on-chain/
  contract risk; options structure/IV/Greeks) (DS-02).
- Carry forward `UNAVAILABLE` fields as open items; mark conclusions that depend on missing data
  as provisional (QA-04).
- **Flag single-source theses low-confidence (SECURITY §4a):** a thesis resting on a SINGLE untrusted
  document (one filing / news item / token memo) is marked **low-confidence** until corroborated.
- **Egress scan before persisting (SECURITY §4d):** run
  `python skills/output-guard/scripts/egress_check.py --scan data/output/dossiers/<ticker>.md`; redact
  any finding before the dossier is written/committed.

### Must Not
- Introduce any figure not in the snapshot (no fresh web pulls mid-dossier; new data → back to
  Stage 1). Unknowns stay queued, never guessed (DS-02).
- Present a one-sided thesis with no disconfirming test or no bear case.
- Collapse the valuation range to a point estimate or imply false precision.
- Let a missing class-specific input (e.g. no contract audit data) be silently treated as "fine."
- Assign a pattern status or a position size here — that is Stage 3 and Stage 6, respectively.

## Instructions

1. **Frame from the snapshot (RT-05).** Summarize the candidate from its Stage 1 data only; state
   the snapshot `as_of` as the cutoff. Note which fields are `UNAVAILABLE`.

2. **Build the core thesis.** Run `finance_investment_thesis_builder.md` for the variant view,
   catalysts, and exit criteria; add moat/durability via `finance_competitive_moat_analyzer.md`;
   map dated catalysts with `finance_catalyst_map_builder.md`. For a short/bear candidate, use
   `finance_short_thesis_constructor.md`.

3. **Establish the valuation range (NE-10).** Use `finance_reverse_dcf_expectations.md` to read
   what the current price implies, then frame bear/base/bull scenarios with probabilities. For
   tokens, use `finance_token_valuation_framework.md` instead of/alongside DCF.

4. **Add asset-class specifics (DS-02).**
   - **Crypto:** tokenomics + value accrual (`finance_token_valuation_framework.md`); on-chain
     read (`finance_onchain_metrics_analysis.md`); protocol/contract risk
     (`finance_smart_contract_risk_review.md`).
   - **Options:** structure selection for the thesis (`finance_options_structure_selector.md`);
     IV/skew/term + Greeks (`finance_implied_vol_greeks_analysis.md`); note expiry/assignment risk.
   - **Equity:** ensure microcap liquidity/manipulation risk is addressed.

5. **Rank risks and pre-commit the disconfirming test (QA-02).** Produce a ranked risk list and a
   single, observable "what would change my mind" condition. This becomes the Stage 7 tripwire.

6. **Write the dossier.** Save to `data/output/dossiers/<ticker>.md` with all sections below.
   Keep `UNAVAILABLE` items visible and mark dependent conclusions provisional (QA-04). Before persisting,
   run the egress scan (above) and redact any finding; flag the thesis low-confidence if it rests on a
   single untrusted source (SECURITY §4a).

## Output Format

```
## DOSSIER: <TICKER> | Class: [equity/crypto/options] | Snapshot as_of [date]
```

### Thesis & variant view
- One-line thesis · Variant view vs. consensus · Why the market may be wrong (RT-05)

### Valuation range (scenarios)
| Scenario | Probability | Value / target | Key assumptions |
|---|---|---|---|
| Bear | … | … | … |
| Base | … | … | … |
| Bull | … | … | … |

### Catalysts (dated)
| Date / window | Catalyst | Direction | Confidence |
|---|---|---|---|

### Ranked risks
| Rank | Risk | Severity | Evidence / status |
|---|---|---|---|

### Asset-class specifics
- **Crypto:** tokenomics & value accrual · on-chain read · contract/protocol risk
- **Options:** chosen structure · breakeven/payoff · IV (level/skew/term) · key Greeks · expiry/assignment
- **Equity:** liquidity/manipulation/data-sparsity notes (esp. microcap)

### Disconfirming test (→ Stage 7 tripwire)
- Pre-committed "what would change my mind": [single observable condition]

### Open items (queued, not guessed)
- `UNAVAILABLE` fields carried from Stage 1 + conclusions marked provisional because of them

## Verification

- [ ] Built only from the Stage 1 snapshot; cutoff `as_of` stated; no fresh mid-dossier pulls.
- [ ] Explicit variant view vs. consensus is present.
- [ ] Valuation is a bear/base/bull range with probabilities, not a point.
- [ ] Dated catalysts and a ranked risk list are included.
- [ ] A single, observable disconfirming test is pre-committed for Stage 7.
- [ ] The correct asset-class section is completed (crypto / options / equity).
- [ ] `UNAVAILABLE` items remain visible; dependent conclusions are flagged provisional.
- [ ] A single-untrusted-source thesis is flagged low-confidence (SECURITY §4a).
- [ ] Egress scan run on the dossier; any finding redacted before persisting (SECURITY §4d).
- [ ] No pattern status or position size assigned here.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Confident thesis built on missing data | Carry `UNAVAILABLE` forward; mark dependent conclusions provisional (QA-04) |
| Point-estimate target implies false precision | Require bear/base/bull range with probabilities (NE-10) |
| One-sided bull case with no falsifier | Mandatory ranked risks + pre-committed disconfirming test (QA-02) |
| New numbers sneak in after the snapshot | No mid-dossier pulls; new data routes back to Stage 1 |
| Crypto/options specifics skipped | Asset-class section is required and class-gated (DS-02) |
| Dossier drifts into sizing/decisioning | Sizing is Stage 6; pattern status is Stage 3 — out of scope here |
