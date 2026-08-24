---
title: "Unit Economics Designer (LTV / CAC / Payback / Cohort Retention)"
category: idea-to-product/market-research
description: "Build a unit-economics model for a software/platform business by selecting the right formulas for the business model (SaaS, marketplace, transactional, ads, hybrid), surfacing the inputs that must be estimated, computing LTV/CAC/payback/gross margin/cohort retention, and producing a sensitivity-band worksheet that flags which assumptions are load-bearing."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01  # Framework Application
  - DS-02  # Decomposition
  - RT-02  # Multi-Dimensional Analysis
  - QA-01
  - QA-02
difficulty: intermediate
tags:
  - unit-economics
  - ltv-cac
  - cohort-analysis
  - financial-model
  - market-research
updated: "2026-05-19"
related_prompts:
  - domain-idea-to-product/stage-3-market-research/product_market_size_calculator.md
  - domain-idea-to-product/stage-4-business-model/monetization_model_selector.md
  - domain-idea-to-product/stage-4-business-model/monetization_pricing_strategy.md
  - domain-idea-to-product/stage-4-business-model/solo_dev_financial_planning.md
---

# Unit Economics Designer (LTV / CAC / Payback / Cohort Retention)

**Objective:** Given a software/platform business model and a small set of inputs (price, gross margin estimate, expected churn, expected CAC), produce a complete unit-economics worksheet: LTV, CAC, LTV:CAC ratio, payback period, contribution margin, and cohort retention curves — with sensitivity bands showing how the answers shift under pessimistic, base, and optimistic assumptions. Flag which 2-3 assumptions are load-bearing.

## When to Use

- You have a validated problem (stage 2 passed) and a candidate business model (stage 4 in progress).
- You want to know if the math can plausibly work before investing in a PRD.
- You're choosing between business models (e.g., subscription vs. usage-based) and want unit economics side-by-side.

## Inputs

The user must provide:
1. **Business model type** — SaaS subscription / marketplace / transactional / usage-based / ads / freemium-with-upsell / hybrid.
2. **Pricing assumption** — ARPU/month, or transaction take rate, or ad RPM. Single number or a range.
3. **Gross margin estimate** — what % of revenue survives after COGS (hosting, payment processing, content costs, support). If unknown, ask the user to pick a sector default (SaaS: 70-85%, marketplace: 15-30% on take, consumer ads: 50-70%).
4. **Churn estimate** — monthly logo churn % or net revenue retention. Mark as "guess" if no data.
5. **CAC estimate** — fully-loaded cost to acquire one paying customer (paid + sales + content amortized). Mark as "guess" if no data.
6. **Time horizon** — 12 / 24 / 36 / 60 months for LTV calculation.

If a critical input is missing, ask for it OR ask permission to use a sector default (and label the resulting number as "assumed").

## Constraints

**Must:**
- Pick formulas appropriate to the business model. SaaS LTV ≠ marketplace LTV ≠ ads LTV — do not paste a generic formula.
- Show the formula being used (with citation to the model type) before plugging in numbers.
- Produce three scenarios: pessimistic / base / optimistic, with explicit assumption changes per scenario.
- Label every "assumed" number distinctly from every "user-provided" number.
- Surface the 2-3 inputs the answer is most sensitive to (do a quick sensitivity check by perturbing each input ±30% and seeing which moves LTV:CAC most).
- End with a verdict: GREEN (math works at base case) / YELLOW (works under optimistic) / RED (doesn't work even under optimistic).

**Must Not:**
- Invent industry benchmarks without labeling them as "rough sector defaults — verify."
- Treat "blended CAC" as fine for early-stage. Always ask whether the user is computing organic + paid blended (which lies about scalable CAC).
- Produce a 5-year DCF. This is unit economics, not a valuation model.
- Recommend "raising prices" as the answer when the underlying problem is churn. Identify the actual binding constraint.

## Instructions

### Step 1: Confirm the business model and pick the formula set

For each business model, use:

**SaaS subscription:**
- Gross margin per customer = ARPU × GM%
- LTV (simple) = (ARPU × GM%) / monthly churn%
- LTV (cohort) = sum over T months of (ARPU × GM% × retention(t))
- Payback = CAC / (ARPU × GM%)
- Healthy ratio: LTV:CAC ≥ 3, payback ≤ 12 months for SMB, ≤ 24 months for enterprise

**Marketplace:**
- Revenue per transaction = GMV × take rate
- GM per transaction = (GMV × take rate) − payment fees − fraud reserve
- LTV = (avg transactions/year × GM per txn) × expected user lifespan
- CAC must be split: supply-side CAC and demand-side CAC, then summed weighted by liquidity model
- Healthy ratio: same 3:1 but with explicit liquidity threshold

**Transactional (one-shot purchase, may repurchase):**
- LTV = avg order value × GM% × expected repurchase count over horizon
- Watch repurchase rate carefully — most one-shot models fail because LTV ≈ first-purchase margin

**Usage-based:**
- LTV = ∑ (expected monthly usage × price × GM%) × retention(t) over horizon
- ARPU is volatile; use median, not mean, and show distribution if data exists

**Ads:**
- LTV per user = sessions × pages/session × ad load × eCPM × GM% × retention(t)
- Sensitivity to retention curve is extreme; show 30/90/365-day retention separately

**Freemium-with-upsell:**
- Compute LTV only on paid users
- CAC must be divided by free-to-paid conversion rate
- Effective CAC per paid user = (CAC to acquire free user) / (free-to-paid %) + (paid acquisition cost)

**Hybrid:** Decompose into components and compute separately, then weight by revenue share.

### Step 2: Plug in user-provided numbers; explicitly label each as PROVIDED vs ASSUMED

### Step 3: Compute base case (point estimates)

### Step 4: Compute pessimistic and optimistic scenarios
- Pessimistic: churn ×1.5, CAC ×1.5, ARPU ×0.7
- Optimistic: churn ×0.7, CAC ×0.7, ARPU ×1.3
- Show all three side by side.

### Step 5: Sensitivity check
- Perturb each input ±30% one at a time. Record absolute % change in LTV:CAC.
- Rank inputs by sensitivity. Identify the 2-3 that the answer rides on.

### Step 6: Verdict and binding constraint
- Verdict: GREEN / YELLOW / RED.
- Binding constraint: which input has to improve most to move from RED→YELLOW or YELLOW→GREEN.
- Required data to firm up the model: what real measurement would replace the load-bearing assumption.

## Output Format

```
## Unit Economics: [business name / hypothesis]

### Model type: [SaaS subscription | marketplace | ...]
### Formulas used:
[formula set with model-type citation]

### Inputs
| Input | Value | Source |
|-------|-------|--------|
| ARPU/month | $X | PROVIDED |
| Gross margin % | Y% | ASSUMED (sector default) |
| Monthly churn % | Z% | PROVIDED |
| CAC (fully loaded) | $W | ASSUMED |
| Horizon | T months | PROVIDED |

### Base case
- Gross margin per customer/month: $___
- LTV ([formula]): $___
- Payback period: ___ months
- LTV:CAC ratio: ___:1

### Scenarios
| Metric | Pessimistic | Base | Optimistic |
|--------|------------|------|-----------|
| LTV | | | |
| CAC | | | |
| LTV:CAC | | | |
| Payback (months) | | | |

### Sensitivity (top 3)
1. [Input X] — ±30% moves LTV:CAC by ±__%
2. [Input Y] — ±30% moves LTV:CAC by ±__%
3. [Input Z] — ±30% moves LTV:CAC by ±__%

### Verdict: [GREEN | YELLOW | RED]
**Binding constraint:** [the one assumption that must improve]
**Required data:** [what you must actually measure to firm up the model]
**Next stage:** [if GREEN, advance to stage 4; if YELLOW, run stage-4 monetization_pricing_strategy to test price increase or stage-2 to re-test retention; if RED, return to stage 1 reshape]
```

## Verification

- [ ] Formula matches business model type (no generic SaaS formula on a marketplace)
- [ ] Every input labeled PROVIDED or ASSUMED
- [ ] Three scenarios computed
- [ ] Top 3 sensitivities ranked
- [ ] Verdict given (GREEN/YELLOW/RED, not "depends")
- [ ] Binding constraint named

## False-Positive Prevention

- **LTV with monthly churn formula on a high-touch enterprise sale will lie.** Use cohort method when churn varies by tenure.
- **Blended CAC hides paid-channel scalability problems.** Split organic vs. paid; the paid-only CAC is what matters at scale.
- **Marketplace LTV computed on one side only is half the model.** Both sides must clear.
- **Ignoring payback period when LTV:CAC looks fine** kills cash-constrained companies. A 60-month payback at 4:1 LTV:CAC bankrupts a startup before recovery.
- **"We'll improve retention later" is not a model.** If base-case fails, retention improvement must be measurable and within 6-12 months, not aspirational.
