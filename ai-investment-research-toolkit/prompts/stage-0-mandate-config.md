---
title: "Stage 0 — Mandate & Config (validate the rules of engagement before any stage runs)"
category: investment-research/mandate-config
description: "Encode and validate the rules of engagement so every later stage is bounded. Reads config/mandate.yaml, risk_limits.yaml, asset_classes.yaml, and data_sources.yaml; refuses to start the loop if any required field is missing or malformed; surfaces the kill switch (halt) and the Gate C live lock (live_enabled + thresholds) in plain sight; confirms the run is paper-only; and hands off the validated config set to Stage 1. Missing fields are reported as blocking, never assumed or guessed."
techniques:
  - CM-02
  - QA-05
  - DS-02
  - QA-04
difficulty: advanced
tags:
  - mandate
  - config-validation
  - kill-switch
  - gate-c
  - paper-first
  - preflight
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/config/mandate.yaml
  - ai-investment-research-toolkit/config/risk_limits.yaml
  - ai-investment-research-toolkit/config/asset_classes.yaml
  - ai-investment-research-toolkit/config/data_sources.yaml
  - ai-investment-research-toolkit/prompts/stage-1-universe-data-sourcing.md
  - ai-investment-research-toolkit/orchestrator_investment_research.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Make the rules of engagement explicit and **provably complete before any other stage runs**.
Stage 0 is the preflight gate: it reads the four config files, validates that every field a
later stage depends on is present and well-formed, and **refuses to start the loop** if any
required field is missing or malformed — naming exactly which field, in which file, is at fault.
It then surfaces the two highest-stakes switches in plain sight — the **kill switch** (`halt`)
and the **Gate C live lock** (`live_enabled` plus its thresholds) — confirms the run is
paper-only, and hands the validated config set to Stage 1. A missing or ambiguous value is
reported as a blocker; it is never defaulted-in, assumed favorable, or guessed.

## When to Use

- At the start of any cadence pass, before Stage 1 — the orchestrator's first step
- After editing any `config/*.yaml` (or adding a `config/mandate.local.yaml` override)
- Before a `/decide`, `/screen`, or `/monitor` run, to confirm the gates are wired as intended
- Whenever you need a one-screen, auditable statement of the current mandate, caps, scope, and
  data-source modes
- To confirm the kill switch / live lock state before trusting any downstream "paper-only" claim

## Inputs / Context Required

**The four config files (all read; none optional)**
- `config/mandate.yaml` — objective, `capital.simulated_usd` + `capital.currency`, `cadence`
  (`monitor`, `research`), the kill switch `halt`, the Gate C block (`live_enabled`,
  `gate_c.min_resolved_predictions`, `gate_c.max_brier_score`, `gate_c.require_manual_enable`)
- `config/risk_limits.yaml` — `max_position_pct`, `max_asset_class_pct`, `max_deployed_pct`, the
  `per_asset_class` overrides, and the discipline flags (`require_stop_loss`, `reject_if_unsized`,
  `reject_if_no_premortem`)
- `config/asset_classes.yaml` — each class's `active` flag and its `universe_filters`
- `config/data_sources.yaml` — the `implementation` (and `manual_input` / `enabled`) backing each
  adapter seam

**Optional local override**
- `config/mandate.local.yaml` (git-ignored) — if present, its fields override the tracked
  `mandate.yaml`; record which fields were overridden.

Stage 0 reads config only. It writes no snapshot, pulls no market data, and places no order.

## Constraints

### Must
- Read **all four** config files and validate them before declaring the loop runnable (CM-02).
- Treat the following as **required**; their absence or malformation is a **hard blocker**
  (refuse to proceed), reporting file + field by name (CM-02, QA-05):
  - `mandate.yaml`: `capital.simulated_usd` (positive number), `halt` (boolean),
    `live_enabled` (boolean), `gate_c.min_resolved_predictions`, `gate_c.max_brier_score`,
    `gate_c.require_manual_enable`, `cadence.monitor`, `cadence.research`
  - `risk_limits.yaml`: `max_position_pct`, `max_asset_class_pct`, `max_deployed_pct` (each a
    fraction in `(0, 1]`), `require_stop_loss`, `reject_if_unsized`, `reject_if_no_premortem`
  - `asset_classes.yaml`: at least one class with `active: true`, and each active class carries a
    non-empty `universe_filters` block
  - `data_sources.yaml`: every seam Stage 1/2/5/6 relies on has an `implementation`; the
    `LiveBrokerAdapter` carries `enabled: false`
- Surface the **kill switch** (`halt`) and the **Gate C lock** (`live_enabled` + the three
  thresholds) at the top of the output, in plain language, before anything else (QA-04).
- **Cross-check Gate C integrity:** if `live_enabled: true` is found, do **not** silently honor
  it — flag it as out of scope for this build (the `LiveBrokerAdapter` ships disabled; §13 step 7
  is deferred) and treat the effective state as paper-only.
- Validate internal consistency: `per_asset_class` overrides do not exceed the portfolio
  `max_position_pct` (lower wins); active crypto/options classes have the seams they need
  (`OnChainAdapter` for crypto, `OptionsChainAdapter` for options) declared in `data_sources.yaml`.
- Report each seam's **mode** (live provider vs. `stub` → manual-only) so downstream stages know
  whether they run on real or pasted data (DS-02).
- Emit a single explicit **GO / NO-GO** verdict and, on GO, hand the validated config to Stage 1.

### Must Not
- Invent, default-in, or assume any missing config value to let the loop proceed — a missing
  required field is a NO-GO, not a guess (DS-02, QA-05).
- Treat `halt: true` or `live_enabled: false` as something to work around or "temporarily relax."
- Enable, reach, or simulate the `LiveBrokerAdapter`, or report a live path as available.
- Loosen a risk cap, widen a universe filter, or activate a class to make a later stage "fit."
- Pull market data, write a snapshot, or place any order — Stage 0 is config validation only.
- Declare GO while any required field is missing, malformed, or internally inconsistent.

## Instructions

1. **Load config (CM-02).** Read `mandate.yaml`, `risk_limits.yaml`, `asset_classes.yaml`,
   `data_sources.yaml`. If `config/mandate.local.yaml` exists, layer it over `mandate.yaml` and
   note the overridden fields. If a file is missing or unparseable, that is an immediate NO-GO.
   **Preflight that the gates are wired in code before trusting the loop** (all stdlib; the
   `load_config` / `load_data_sources` parsers back this validation):

   ```bash
   python -m unittest discover -s tests                                   # 20 gate tests
   python skills/pattern-knowledge-base/scripts/validate_pattern.py --self-check   # Gate A
   python skills/prediction-journal/scripts/score_brier.py --self-check           # Brier / Gate C
   python skills/paper-trade-executor/scripts/brokers.py --self-check             # Gate B / kill switch
   python skills/data-source-adapter/scripts/adapters.py --self-check             # look-ahead / UNAVAILABLE
   python skills/data-source-adapter/scripts/build_snapshot.py --self-check       # snapshot immutability
   python skills/pattern-knowledge-base/scripts/screen_rank.py --self-check       # Gate A at rank time
   ```

2. **Validate required fields (QA-05).** Check each required field from the Must list for presence
   and type/range. Build a per-file pass/fail table. Any failure → record it as a blocker with the
   exact file and field path; do not substitute a default.

3. **Surface the switches first (QA-04).** Read and report `halt` and the full Gate C block.
   State the plain-language consequence: `halt: true` → Stages 4–6 will not run (research/journaling
   read-only); `live_enabled` → paper-only regardless (the live adapter is disabled in this build).
   If `live_enabled: true`, flag the mismatch and hold the effective state at paper-only.

4. **Check internal consistency.** Confirm: ≥1 active class; each active class has filters; each
   `per_asset_class.max_position_pct` ≤ portfolio `max_position_pct`; caps are fractions in `(0,1]`;
   active crypto/options classes have their required seams declared. Record any inconsistency as a
   blocker.

5. **Report seam modes (DS-02).** For each seam in `data_sources.yaml`, state whether it is a live
   provider or `stub` (manual-only, reading from its `manual_input` path). Confirm
   `LiveBrokerAdapter: enabled: false`.

6. **Emit the verdict.** If there are zero blockers, declare **GO** and hand the validated config
   summary to Stage 1 (`prompts/stage-1-universe-data-sourcing.md`). If any blocker exists, declare
   **NO-GO**, list every blocker, and stop — the loop does not advance until config is fixed.

## Output Format

```
## MANDATE PREFLIGHT: as_of [date] | verdict [GO / NO-GO] | halt=[t/f] | live_enabled=false (paper-only)
```

### Switches (read first)
| Switch | Value | Consequence |
|---|---|---|
| Kill switch (`halt`) | true/false | true → Stages 4–6 dropped (research/journaling read-only) |
| Gate C (`live_enabled`) | false | Paper-only — `LiveBrokerAdapter` disabled (deferred, §13 step 7) |
| Gate C thresholds | ≥… resolved · Brier ≤ … · manual enable [t/f] | Unlock conditions (not met until tracked) |

### Config validation
| File | Required fields present? | Issues (file → field) |
|---|---|---|
| mandate.yaml | yes/no | … |
| risk_limits.yaml | yes/no | … |
| asset_classes.yaml | yes/no | … |
| data_sources.yaml | yes/no | … |

### Effective mandate (on GO)
| Field | Value |
|---|---|
| Simulated capital | $… |
| Cadence | monitor=… · research=… |
| Active classes | [equity/crypto/options] + filters |
| Risk caps | position ≤…% (per-class …) · class ≤…% · deployed ≤…% |
| Discipline flags | require_stop_loss / reject_if_unsized / reject_if_no_premortem |
| Local override applied | [none / list of overridden fields] |

### Seam modes
| Seam | Implementation | Mode |
|---|---|---|
| MarketDataAdapter / FundamentalsAdapter / FilingsAdapter / OnChainAdapter / OptionsChainAdapter | … | live / manual (stub) |
| PaperBrokerAdapter | builtin_simulator | paper |
| LiveBrokerAdapter | stub | DISABLED (enabled:false) |

### Verdict & hand-off
- Blockers: [count] — [list, or "none"]
- Verdict: **GO** → hand validated config to Stage 1 | **NO-GO** → fix listed blockers, do not advance

## Verification

- [ ] All four config files were read and parsed; a missing/unparseable file is a NO-GO.
- [ ] Every required field was checked for presence and type/range; failures name file + field.
- [ ] `halt` and the full Gate C block are surfaced at the top, with their plain-language effect.
- [ ] No missing value was defaulted-in or guessed to allow GO.
- [ ] `LiveBrokerAdapter: enabled: false` confirmed; any `live_enabled: true` is flagged, not honored.
- [ ] Per-class caps ≤ portfolio cap; ≥1 active class with filters; active crypto/options seams present.
- [ ] Each seam's mode (live vs. manual stub) is reported.
- [ ] A single explicit GO / NO-GO verdict was emitted; GO hands off to Stage 1.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| A missing required field is quietly defaulted so the loop runs | Required fields are hard blockers → NO-GO names the exact file + field; nothing is defaulted |
| `live_enabled: true` is taken at face value as a real-money path | This build ships the live adapter disabled; any `live_enabled: true` is flagged and held to paper-only |
| `halt: true` is treated as advisory | `halt: true` is reported first and forces Stages 4–6 to be dropped downstream |
| A per-class cap silently exceeds the portfolio cap | Consistency check rejects any `per_asset_class` cap above the portfolio cap (lower wins) |
| An active crypto/options class lacks its data seam | Consistency check requires the seam (OnChain / OptionsChain) to be declared before GO |
| "Live data" assumed when seams are stubs | Each seam's mode (live vs. manual stub) is reported explicitly |
| GO declared despite unresolved problems | Verdict is GO only at zero blockers; any blocker → NO-GO and the loop does not advance |
