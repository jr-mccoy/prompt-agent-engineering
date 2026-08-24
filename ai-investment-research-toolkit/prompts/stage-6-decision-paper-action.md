---
title: "Stage 6 — Decision & Action (paper-first; Gate B sizes, Gate C locks live)"
category: investment-research/decision-paper-action
description: "Convert a high-conviction watchlist/alert into a trade memo, size it, pre-mortem it, and route it to the PAPER broker — never real money. Enforces Gate B (no order without sizing + pre-mortem + a passing risk-limit check) and Gate C (the live adapter stays disabled). Emits a PRED-* prediction that hands off to the Stage 7 journal. Missing inputs are queued, never assumed favorable."
techniques:
  - CM-02
  - DS-02
  - QA-04
  - NE-10
  - RT-06
difficulty: advanced
tags:
  - decision
  - paper-trading
  - position-sizing
  - pre-mortem
  - gate-b
  - gate-c
updated: "2026-06-18"
related_prompts:
  - ai-investment-research-toolkit/prompts/stage-5-monitoring-tripwires.md
  - ai-investment-research-toolkit/prompts/stage-7-journaling-calibration.md
  - ai-investment-research-toolkit/skills/paper-trade-executor/SKILL.md
  - ai-investment-research-toolkit/skills/paper-trade-executor/references/risk_gate_enforcement.md
  - ai-investment-research-toolkit/skills/paper-trade-executor/references/order_schema.md
  - referenced-prompts/domain-finance/investing-research/finance_position_sizing_framework.md
  - referenced-prompts/domain-finance/quant-fintech-data/finance_trading_strategy_premortem.md
---

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades. All outputs require independent verification.*

## Objective

Convert a high-conviction candidate (a Stage 4 watchlist entry or a Stage 5 alert) into an order —
**on paper**. Draft a complete trade memo, size the position, run a pre-mortem, and route the order
to the `PaperBrokerAdapter` via the `paper-trade-executor` skill. Two gates are load-bearing.
**Gate B**: no order — even a paper one — is placed without a position-sizing output, a pre-mortem,
AND a passing risk-limit check (≤ 2% per position, ≤ 20% per asset class, ≤ 60% deployed, with
tighter per-class caps), enforced at order time. **Gate C**: the `LiveBrokerAdapter` is present but
**disabled** and cannot be reached here — real money stays locked until ≥ 100 resolved predictions,
Brier ≤ 0.18, and a manual `live_enabled`. Every decision (taken or consciously declined) emits a
`PRED-*` prediction with a probability stated **up front**, handed to Stage 7 to journal and later
Brier-score. Where an input is missing, it is queued — never assumed favorable to justify the trade.

## When to Use

- Acting on a Stage 5 alert or a top-ranked Stage 4 watchlist name with a real, validated edge
- Producing a paper trade memo + order for `data/output/orders/<date>.md`
- Adjusting or closing an existing paper position when a tripwire fires
- Recording the prediction (probability + horizon + tripwires) that Stage 7 will resolve

## Inputs / Context Required

**The candidate**
- The watchlist entry (`data/output/watchlist.csv`) or Stage 5 alert (`data/output/alerts/<date>.md`)
- Its dossier (`data/output/dossiers/<ticker>.md`) — thesis, valuation range, dated catalysts,
  ranked risks, and the pre-committed disconfirming test
- The `validated` `PATTERN-*` ids that scored it in Stage 4 (Gate A) — for `patterns_fired`

**The account & limits**
- `config/mandate.yaml` — `capital.simulated_usd`, the kill switch `halt`, and the Gate C block
- `config/risk_limits.yaml` — the three caps, per-class overrides, and the discipline flags
- The current paper ledger (`data/output/portfolio.json`) for live exposure
- The `paper-trade-executor` skill (`PaperBrokerAdapter` active; `LiveBrokerAdapter` disabled)

## Constraints

### Must
- Draft a complete **trade memo** before any order: ticker, asset_class, direction, entry, stop /
  exit, thesis (1–2 lines), and the ranked key risks (RT-06).
- Produce an explicit **position-sizing** output (reuse `finance_position_sizing_framework.md`) and
  a **pre-mortem** (reuse `finance_trading_strategy_premortem.md`); both are Gate B prerequisites
  (CM-02).
- Run the **Gate B** risk-limit check via the skill at order time: reject if no stop, no sizing, or
  no pre-mortem, or if any cap is breached (≤ 2% position with per-class override, ≤ 20% class,
  ≤ 60% deployed) (CM-02 — this is Gate B enforced).
- Route the order to the **`PaperBrokerAdapter`** only; record the resulting `Fill`
  (FILLED / REJECTED / HALTED) with its reasons.
- Emit a `PRED-*` block with `probability` stated up front, mapped to the §6 schema, for Stage 7
  (RT-06).
- **Require corroborated, multi-source snapshot fields (SECURITY §4a):** an order resting on a SINGLE
  untrusted document (one filing / news item / token memo) is flagged low-confidence and does not place
  — the thesis behind an order needs corroboration across sources.
- **Egress scan before persisting (SECURITY §4d):** run
  `python skills/output-guard/scripts/egress_check.py --scan data/output/orders/<as_of>.md` before the
  order/PRED file is written/committed; redact any finding first.
- Honor the kill switch: if `halt: true`, place no order; log the no-action decision.

### Must Not
- Reach, enable, or simulate the `LiveBrokerAdapter`, or treat `live_enabled: false` as something to
  work around (Gate C — the single most important rule of this stage).
- Place any order that lacks a stop, a sizing output, or a pre-mortem, or that breaches a cap —
  loosening or hardcoding a limit to force a fill is forbidden (CM-02).
- Invent a fill, a price, or a favorable input where data is `UNAVAILABLE` — a missing input is
  queued, and an order that cannot be sized is not placed (DS-02, QA-04).
- State a point-estimate return ("this returns X%"); the prediction is a calibrated probability over
  a defined outcome, not a forecasted return (NE-10).
- Count any `hypothesis`-status pattern toward the decision — only `validated` patterns (Gate A)
  reached this stage.
- Place an order on a single-untrusted-source thesis (flag it low-confidence), or persist an order/PRED
  file before the egress scan clears (SECURITY §4a/§4d).

## Instructions

1. **Draft the trade memo (RT-06).** From the watchlist/alert + dossier, write the memo: ticker,
   asset_class, direction (long/short), entry, stop/exit, a 1–2 line thesis, and ranked key risks.
   Where a needed fact is `UNAVAILABLE`, queue it — do not fill the gap with a favorable guess.

2. **Size the position (CM-02).** Reuse `finance_position_sizing_framework.md` against
   `capital.simulated_usd` and current exposure (`data/output/portfolio.json`). Produce an explicit
   quantity/notional with its rationale; this is the `sizing_ref` Gate B requires.

3. **Run the pre-mortem (CM-02).** Reuse `finance_trading_strategy_premortem.md`: assume the trade
   failed and enumerate why, then the disconfirming tripwires to watch. This is the `premortem_ref`
   Gate B requires.

4. **Enforce Gate B at order time, in code (CM-02).** Route the drafted order (with `stop`,
   `sizing_ref`, `premortem_ref`) through the implemented simulator — the kill switch and Gate B run
   before any fill. A `REJECTED`/`HALTED` Fill is not placed and never mutates the ledger; record the
   breached reasons and stop — do not adjust a cap to pass. (See
   `paper-trade-executor/references/risk_gate_enforcement.md`.)

   ```bash
   # --config config loads the tracked risk_limits.yaml + mandate.yaml (caps + kill switch).
   # Output: FILLED (ledger updated) | REJECTED (with reasons) | HALTED. Live money is unreachable.
   python skills/paper-trade-executor/scripts/brokers.py \
     --symbol <SYMBOL> --asset-class <equity|crypto|options> --side buy \
     --quantity <Q> --price <P> --stop <STOP> \
     --sizing-ref data/output/orders/<as_of>.md#sizing \
     --premortem-ref data/output/orders/<as_of>.md#premortem \
     --config config --portfolio data/output/portfolio.json
   ```

5. **Route to paper (Gate C).** A passing order fills deterministically against the
   `PaperBrokerAdapter` and updates `data/output/portfolio.json` (above). The `LiveBrokerAdapter` is
   disabled and is never reached. Honor the kill switch (`halt: true` → no order, log no-action; pass
   `--halt` to confirm the HALTED path). Read current paper exposure vs the caps, read-only:

   ```bash
   python skills/paper-trade-executor/scripts/brokers.py --report --config config \
     --portfolio data/output/portfolio.json
   ```

6. **Emit the prediction (RT-06).** Write a `PRED-*` block mapping to the §6 schema (asset,
   direction, `probability` up front, `thesis_ref`, `patterns_fired` = validated patterns, horizon,
   tripwires); leave `resolution`/`brier_component` null. Save the memo, sizing, pre-mortem summary,
   Gate B result, fill, decision-log entry, and the `PRED-*` block to `data/output/orders/<as_of>.md`.
   Before persisting, run the egress scan (above) and redact any finding (SECURITY §4d); confirm the
   thesis is corroborated across sources, not a single untrusted document (SECURITY §4a).

## Output Format

```
## ORDER & DECISION: as_of [date] | [SYMBOL] [direction] | Venue: PaperBrokerAdapter | Mode: [live/manual]
```

### Trade memo
| Field | Value |
|---|---|
| Symbol / class | … / equity\|crypto\|options |
| Direction / entry / stop | long / … / … |
| Thesis (1–2 lines) | … |
| Key risks (ranked) | 1) … 2) … |

### Sizing & pre-mortem (Gate B prerequisites)
- Position sizing: [quantity / notional / % of capital] — rationale (`finance_position_sizing_framework.md`)
- Pre-mortem: [top failure modes + the tripwires they imply] (`finance_trading_strategy_premortem.md`)

### Gate B / Gate C statement
- Gate B check: [PASS / REJECTED] · Reasons: [breached caps/flags, or "none"]
- Caps at order time: position [x.xx% ≤ cap] · class [x.xx% ≤ 20%] · deployed [x.xx% ≤ 60%]
- Gate C: `LiveBrokerAdapter` disabled (live_enabled=false) — paper only
- Kill switch (`halt`): [false → order routed / true → no action logged]

### Paper fill / decision log
| order_id | status | filled_qty | fill_price | venue | notes |
|---|---|---|---|---|---|
| ORD-… | FILLED/REJECTED/HALTED | … | … | PaperBrokerAdapter | … |

### Prediction handoff to Stage 7 (PRED-*)
```yaml
asset: "SYMBOL"
direction: long            # long | short | neutral
probability: 0.NN          # stated UP FRONT (0–1), used for Brier — never edited later
thesis_ref: "data/output/dossiers/SYMBOL.md"
patterns_fired: [PATTERN-00xx]   # validated patterns only (Gate A)
horizon: "90 days"
tripwires: ["thesis-break: …", "stop at -15%"]
resolution: null
brier_component: null
```

## Verification

- [ ] A complete trade memo, a sizing output, and a pre-mortem exist before the order.
- [ ] Gate B ran at order time; any REJECTED order shows its breached reasons and was not placed.
- [ ] All three caps were checked against `risk_limits.yaml` (position with per-class override, class, deployed).
- [ ] The order routed only to `PaperBrokerAdapter`; `LiveBrokerAdapter` was never reached (Gate C).
- [ ] No cap was loosened or hardcoded to force a fill; `UNAVAILABLE` inputs were queued, not assumed.
- [ ] A `PRED-*` block with an up-front `probability` and only `validated` `patterns_fired` was emitted for Stage 7.
- [ ] No point-estimate return claim; the prediction is a probability over a defined outcome.
- [ ] The order's thesis is corroborated across sources (single-untrusted-source → low-confidence, no place) (SECURITY §4a).
- [ ] Egress scan run on the order/PRED file; any finding redacted before persisting (SECURITY §4d).
- [ ] Kill switch honored (`halt: true` → no order, no-action logged).

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| An order slips through without sizing or a pre-mortem | Gate B rejects on `reject_if_unsized` / `reject_if_no_premortem` at order time (CM-02) |
| A position quietly exceeds a risk cap | Gate B checks position/class/deployed caps; lower-of per-class wins; REJECTED names the breach |
| The live adapter gets reached "just this once" | `LiveBrokerAdapter` disabled (Gate C); its `place_order` raises — paper only |
| A missing input is read as favorable to justify the trade | `UNAVAILABLE` → queued; an unsizable order is not placed (DS-02, QA-04) |
| A simulated fill is reported when the order was blocked | A REJECTED/HALTED Fill never mutates the portfolio; status + reasons recorded |
| The decision is sold as a return forecast | Prediction is a calibrated probability over a defined outcome, not a point return (NE-10) |
| A hypothesis pattern is used to justify sizing | Only `validated` patterns (Gate A) reach this stage and `patterns_fired` |
| `probability` is tweaked after the fact to look calibrated | Stated up front in the `PRED-*` block; Stage 7 never edits it |
