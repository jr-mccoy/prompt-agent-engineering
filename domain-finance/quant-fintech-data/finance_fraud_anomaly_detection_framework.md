---
title: "Transaction Fraud & Anomaly Detection — Feature and Rule Framework"
category: finance/quant-fintech-data
description: "Design a transaction fraud/anomaly-detection framework: engineer behavioral and network features, layer deterministic rules with statistical/ML scoring, and tune the precision–recall tradeoff against false-positive cost, alert capacity, and class imbalance — with validation discipline and fair-lending/bias guardrails built in."
techniques:
  - DT-02
  - DS-02
  - QA-02
  - DS-06
  - QA-04
difficulty: advanced
tags:
  - fraud-detection
  - anomaly-detection
  - feature-engineering
  - precision-recall
  - class-imbalance
  - fintech
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_financial_statement_anomaly_detector.md
  - domain-finance/regulatory-compliance/finance_aml_kyc_program_designer.md
  - domain-finance/quant-fintech-data/finance_time_series_forecast_critique.md
  - domain-finance/field_guide.md
---

**Informational only — not legal, compliance, or model-governance advice. A fraud model influences customer treatment and may carry fair-lending and disparate-impact obligations; deploy only under qualified compliance and model-risk oversight.**

## Objective

Produce a deployable design for detecting fraudulent or anomalous transactions: the feature set, the layered detection logic (rules + statistical/ML scoring), the validation protocol appropriate to a severely imbalanced and adversarial problem, the operating-point selection that trades off false positives against missed fraud given alert capacity, and the bias/fair-treatment guardrails. The deliverable is a framework and methodology — not a trained model and not invented fraud-rate statistics.

## When to Use

- Standing up or overhauling a payments/card/account-takeover fraud system
- Designing the feature and rule layer before a fintech ML build
- Reviewing an existing fraud system for blind spots, alert overload, or bias
- Setting or re-tuning the score threshold / alert operating point
- AML/sanctions transaction-monitoring scenario design (pairs with the AML/KYC prompt)
- Adding anomaly detection to a new product or transaction type

## Inputs / Context Required

```
<fraud_context>
Product / transaction type: [card present/not-present, ACH, P2P, account opening, login]
Fraud typologies of concern: [stolen card, account takeover, synthetic identity, mule, friendly fraud]
Data available per transaction: [amount, time, merchant/MCC, geo, device, IP, velocity history]
Entity & network data: [account age, device-sharing, prior disputes, linked accounts]
Label availability & lag: [confirmed-fraud labels? how delayed? chargeback window]
Volume & base rate context: [approx transactions/day; is fraud rare? — do NOT invent the rate]
Cost asymmetry: [cost of a missed fraud (loss + ops) vs cost of a false positive (friction, churn, review labor)]
Alert/review capacity: [analysts available; max alerts/day they can clear]
Regulatory context: [fair-lending/ECOA exposure? region; explainability requirement]
Decision mode: [block | step-up auth | queue for review | monitor]
</fraud_context>
```

If base rates, fraud losses, or label quality are unknown, treat them as parameters to be measured — never substitute assumed numbers.

## Constraints

### Must
- Engineer features across the standard fraud dimensions (DT-02): **transaction** (amount, MCC, time-of-day), **velocity** (count/sum over rolling windows), **behavioral** (deviation from the entity's own history), **network/graph** (shared device/IP/beneficiary), **device/session**, and **geo** (impossible-travel).
- Define each feature with a precise, computable specification (DS-02) — window, aggregation, and what "anomalous" means for it.
- Use a **layered** architecture: deterministic rules (high-precision, explainable) + statistical anomaly scores (unsupervised, for novel patterns) + supervised model (where labels exist) — and state how their outputs combine.
- Confront **class imbalance** directly: fraud is rare, so accuracy is meaningless. Evaluate on **precision, recall, PR-AUC, and precision@k (k = alert capacity)**, not accuracy or ROC-AUC alone.
- Make the **operating point a cost decision**: tie the threshold to the false-positive vs false-negative cost asymmetry and to analyst capacity. Show the precision/recall tradeoff at candidate thresholds.
- Specify **validation discipline**: out-of-time (not random) splits to respect temporal order and concept drift; guard against label leakage from post-event features (e.g., a chargeback flag is not a usable input).
- Include **bias / fair-treatment guardrails** (QA-02): test for disparate false-positive rates across protected-class proxies; avoid features that are proxies for protected attributes; require explainability where regulation demands it.
- Acknowledge adversarial drift (QA-04): fraudsters adapt; the model decays and needs monitoring and retraining.

### Must Not
- Invent fraud rates, loss figures, precision/recall numbers, or class balances.
- Use accuracy as the headline metric on an imbalanced problem.
- Use post-outcome or leakage features (chargeback status, future dispute) as model inputs.
- Recommend auto-blocking on an opaque score where a regulatory explainability or adverse-action obligation applies, without flagging it.
- Ignore the analyst-capacity constraint — a recall gain that floods the queue beyond capacity is not deployable.

## Instructions

**Step 1 — Map the threat model.**
Enumerate the fraud typologies in scope and, for each, the behavioral signature it tends to leave (e.g., account takeover → new device + password change + high-velocity transfers). This drives feature design.

**Step 2 — Engineer the feature set (DT-02 + DS-02).**

| Dimension | Example feature | Computable spec | Typifies which fraud |
|---|---|---|---|
| Transaction | amount vs entity 90-day mean | (amt − μ₉₀)/σ₉₀ z-score | stolen card |
| Velocity | txns in last 1h / 24h | rolling count & sum | testing, bust-out |
| Behavioral | new merchant category for entity | 0/1 vs MCC history | takeover |
| Network | beneficiary shared with flagged accounts | graph degree to known-fraud | mule rings |
| Device/session | new device fingerprint | 0/1 vs device history | takeover |
| Geo | impossible travel since last txn | distance/Δtime > feasible | stolen credentials |

**Step 3 — Layer the detection logic.**
```
Layer 1 — Rules: high-precision, explainable, fast (e.g., impossible-travel block,
  hard velocity caps). Each rule states precision intent and the action.
Layer 2 — Unsupervised anomaly score: isolation forest / autoencoder / robust z —
  catches novel patterns without labels. Output = anomaly score.
Layer 3 — Supervised model (if labels exist): gradient-boosting/logistic with the
  engineered features. Output = calibrated fraud probability.
Combination: state the policy — e.g., Layer-1 hard rules override; Layers 2–3
  feed a unified score; thresholds map to action (block / step-up / review / monitor).
```

**Step 4 — Evaluate under imbalance (DS-02).**
```
Required metrics (NOT accuracy):
  Precision = TP / (TP+FP)        Recall = TP / (TP+FN)
  PR-AUC (area under precision-recall curve)
  Precision@k where k = daily alert capacity
  Fraud-$ caught vs fraud-$ missed (value-weighted, not count-weighted)
Show the confusion-matrix tradeoff at 2–3 candidate thresholds.
```

**Step 5 — Choose the operating point as a cost decision (DS-06).**
```
Let C_FN = cost of a missed fraud (loss + downstream ops)
    C_FP = cost of a false positive (review labor + customer friction/churn)
Pick threshold minimizing expected cost = C_FN·(missed fraud $) + C_FP·(false alerts),
  subject to alerts/day ≤ analyst capacity.
Report the chosen threshold, its precision/recall, and the resulting alert volume.
```

**Step 6 — Validation & drift protocol.**
- Out-of-time split (train on earlier period, test on later) — never random shuffle.
- Leakage audit: confirm no post-event feature is an input; respect label lag (chargeback window).
- Drift monitoring: track score distribution, precision@k, and fraud-mix over time; define retrain triggers.

**Step 7 — Bias & fairness guardrails (QA-02).**
- Test false-positive-rate parity across protected-class proxies (geography, demographic proxies).
- Remove/penalize features that proxy protected attributes; document the review.
- Ensure adverse-action explainability where ECOA/regulatory obligations apply.
- Disconfirming check: "Which legitimate customer segment looks most like fraud to this model, and what is the harm if we block them?"

## Output Format

```
## Fraud / Anomaly Detection Framework — [Product]
Decision mode: [block/step-up/review] | Prepared: [date] | Data: user-supplied

### 1. Threat Model
[Typologies → behavioral signatures]

### 2. Feature Set
[Step 2 table]

### 3. Layered Detection Architecture
[Rules / unsupervised / supervised + combination policy]

### 4. Evaluation Under Imbalance
[PR-based metrics; threshold tradeoff table — NOT accuracy]

### 5. Operating Point (Cost Decision)
[Chosen threshold, precision/recall, alert volume vs capacity]

### 6. Validation & Drift Protocol
[Out-of-time split, leakage audit, retrain triggers]

### 7. Bias & Fairness Guardrails
[Disparate-FP test, proxy-feature review, explainability]

### Known Limitations
[Label lag, adversarial drift, unmeasured base rates]
```

## Verification

- [ ] Threat model maps each typology to a behavioral signature before feature design.
- [ ] Every feature has a computable specification (window, aggregation, threshold logic).
- [ ] Architecture is layered (rules + unsupervised + supervised) with a stated combination policy.
- [ ] Evaluation uses precision/recall/PR-AUC/precision@k — accuracy is not the headline.
- [ ] Operating point tied to C_FP/C_FN asymmetry and analyst capacity.
- [ ] Validation uses out-of-time splits; leakage/label-lag audit performed.
- [ ] Disparate false-positive-rate test and proxy-feature review included.
- [ ] No fraud rates, losses, or performance metrics invented.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Reporting high accuracy on rare-fraud data | Accuracy is meaningless under imbalance; require precision/recall/PR-AUC and precision@k |
| Random train/test split | Use out-of-time splits; random shuffling leaks future patterns and hides drift |
| Leakage features (chargeback/dispute flags) as inputs | Audit every feature for post-event timing; respect the label-lag window |
| Maximizing recall regardless of queue | Constrain to analyst capacity; an unservable alert volume is not a deployment |
| Ignoring disparate impact | Test FP-rate parity across protected-class proxies; remove proxy features; document |
| Treating the model as static | Fraud adapts; require drift monitoring and retrain triggers, and state expected decay |
