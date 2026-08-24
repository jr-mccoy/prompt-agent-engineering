---
title: "Consumer / SME Underwriting Decision Framework — with Fair-Lending Guardrails"
category: finance/credit-lending
description: "Structured consumer/SME underwriting decision framework scoring ability-to-repay, willingness, and stability from permissible factors, with explicit ECOA/Reg-B fair-lending guardrails, protected-class prohibitions, and proxy-discrimination detection — no invented data."
techniques:
  - RT-02
  - AG-02
  - CM-02
  - DS-02
  - NE-10
difficulty: intermediate
tags:
  - consumer-credit
  - sme-underwriting
  - fair-lending
  - ecoa
  - reg-b
  - disparate-impact
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_five_cs_credit_analysis.md
  - domain-finance/credit-lending/finance_pd_lgd_ead_framing.md
  - domain-finance/credit-lending/finance_watchlist_early_warning.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, lending, or legal/compliance advice. Underwriting decisions and fair-lending compliance must be reviewed by qualified credit and compliance professionals against current law.*

## Objective

Provide a structured underwriting decision framework for consumer or small-business (SME) credit that evaluates ability-to-repay, willingness-to-repay, and stability using only permissible credit factors, and that bakes in fair-lending guardrails: it prohibits the use or inference of protected-class status, flags variables that may act as proxies for protected classes, and prompts a disparate-impact check. Decisions are evidence-based and arithmetic is transparent; no applicant data is invented.

## When to Use

- Designing or documenting a consumer/SME credit decision rule or scorecard logic
- Adjudicating an individual application against a defined policy
- Reviewing an existing decision framework for fair-lending risk
- Building adverse-action reasoning that is specific and permissible
- Auditing whether a model's features include proxy-discrimination risk

## Inputs / Context Required

Provide as much as available; missing items are flagged, not invented. Do NOT provide protected-class attributes.

**Permissible applicant data**
- Income / cash flow, employment or business tenure, existing debt obligations
- Credit bureau data: score, payment history, delinquencies, utilization, derogatories (as permitted)
- For SME: business revenue, time in business, DSCR, cash-flow stability
- Requested amount, purpose, term, collateral (if secured)

**Policy parameters**
- Decision thresholds: minimum score, maximum DTI, minimum income, minimum tenure (supplied or `[ASSUMED]`)
- Pricing tiers / risk-based pricing bands, if applicable
- Adverse-action reason code set

**Compliance framework**
- Jurisdiction (US fair-lending = ECOA / Regulation B; flag other jurisdictions). Verify against current regulations as of [date].
- List of variables used by the model/policy (for proxy screening)

## Constraints

### Must
- Use only permissible, repayment-relevant factors (RT-02): ability, willingness, stability.
- Default to a skeptical, evidence-based stance (AG-02): approval requires the factors to support repayment; thin files are flagged, not assumed favorable.
- Show decision arithmetic (DTI, DSCR, residual income) with formula -> inputs -> result.
- Manage the constraint tension (CM-02) between approval/access and risk — state the trade-off, do not silently tighten.
- Explicitly PROHIBIT use or inference of protected-class status (race, color, religion, national origin, sex, marital status, age (with ECOA exceptions), receipt of public assistance, exercise of CCPA rights).
- Run a PROXY screen: flag any feature (e.g., zip code, name, school, shopping patterns) that could correlate with a protected class, and prompt a disparate-impact check.
- Produce specific, permissible adverse-action reasons tied to actual factors.
- State the framework and "verify against current regulations as of [date]."

### Must Not
- Use, request, or infer any protected-class attribute, directly or by proxy.
- Invent applicant income, scores, or bureau data.
- Approve or decline on impermissible factors or unexplained "judgment."
- Use zip code, neighborhood, or geography as a credit factor without a disparate-impact justification (redlining risk).
- Provide vague adverse-action reasons ("did not meet our standards").
- Treat a fair-lending check as optional.

## Instructions

1. **Confirm permissible-factor scope.** List the factors the decision will use; confirm none is a protected-class attribute. Flag any feature requiring a proxy review (step 5).

2. **Assess ability-to-repay.** Compute the repayment-capacity metrics:
```
DTI = Total Monthly Debt Obligations / Gross Monthly Income
Residual Income = Net Monthly Income - (Debt Obligations + Living Expenses)
For SME: DSCR = Business Cash Flow / Debt Service
Payment-to-Income (new loan) = Proposed Payment / Gross Monthly Income
```

3. **Assess willingness-to-repay.** From bureau payment history: delinquency pattern, derogatories, utilization trend — permissible behavioral factors only.

4. **Assess stability.** Employment/business tenure, income consistency, residential/operating stability (as permissible and non-proxying).

5. **Run the fair-lending proxy screen.** For every feature, ask: could this correlate strongly with a protected class? Flag candidates (zip code, surname, alma mater, certain spending data). For any flagged feature, require a documented business-necessity justification and a disparate-impact test, or remove it.
```
Disparate-impact flag (methodology): compare approval/pricing outcomes across groups
   defined ONLY for testing/monitoring by compliance — never used in the decision itself.
```

6. **Apply the decision rule.** Compare metrics to stated thresholds; produce approve / decline / refer with risk-based pricing tier. State the trade-off where access and risk conflict.

7. **Generate adverse-action reasoning.** If declined or counter-offered, produce specific, permissible reasons tied to the actual factors (e.g., "debt-to-income ratio of X% exceeds policy maximum of Y%"), never to protected status or vague judgment.

## Output Format

### Permissible Factor & Proxy Screen
| Factor Used | Repayment-Relevant? | Proxy Risk? | Action |
|---|---|---|---|
| Income | yes | no | use |
| Credit score | yes | no | use |
| Zip code | — | YES | remove / business-necessity + disparate-impact test |
| Surname | — | YES | not used |

### Ability-to-Repay Arithmetic
```
DTI            = Monthly Debt / Gross Monthly Income = X%
Residual Income = Net Income - (Debt + Living Expenses) = $X
DSCR (SME)     = Business Cash Flow / Debt Service = X.XXx
PTI (new loan) = Proposed Payment / Income = X%
```

### Decision Scorecard
| Dimension | Assessment | Metric vs. Threshold | Permissible? |
|---|---|---|---|
| Ability | ... | DTI X% vs max Y% | yes |
| Willingness | ... | delinquency pattern | yes |
| Stability | ... | tenure X vs min | yes |
| **Decision** | **Approve / Decline / Refer** | pricing tier | |

### Decision Sensitivity (base / downside / severe income)
| Metric | Base | Downside (income -X%) | Severe (income -X%) |
|---|---|---|---|
| DTI | X% | X% | X% |
| Residual Income | $X | $X | $X |
| Decision | | | |

### Fair-Lending Guardrail Summary
- Protected-class attributes used or inferred: **NONE** (verified)
- Proxy variables flagged: [list + disposition]
- Disparate-impact test: [recommended to compliance — methodology only]
- Framework: ECOA / Regulation B (US) — verify against current regulations as of [date]

### Adverse-Action Reasons (if applicable)
| Reason Code | Specific, Permissible Basis |
|---|---|
| ... | "DTI X% exceeds policy max Y%" |

## Verification

- [ ] No protected-class attribute is used, requested, or inferred — directly or by proxy.
- [ ] Every feature passed the proxy screen; flagged ones removed or justified + disparate-impact tested.
- [ ] Ability-to-repay arithmetic (DTI, residual income, DSCR/PTI) shown with formula -> inputs -> result.
- [ ] Decision compares metrics to stated thresholds; trade-off between access and risk stated.
- [ ] Adverse-action reasons are specific, permissible, and tied to actual factors.
- [ ] Geography/zip not used as a factor without business-necessity + disparate-impact justification.
- [ ] No applicant data invented; gaps flagged `[MISSING]` / `[ASSUMED]`.
- [ ] Framework named with "verify against current regulations as of [date]."

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Using a proxy variable (zip, name) that correlates with protected class | Proxy screen flags and removes or requires business-necessity + disparate-impact test |
| Declining with a vague reason | Adverse-action reasons must be specific and tied to actual permissible factors |
| Inferring marital status, age, or national origin from data | Protected-class inference prohibited and verified as NONE used |
| Geography-based pricing creating redlining risk | Geography barred as a factor absent justification and impact testing |
| Approving a thin file as favorable by default | Skeptical stance: missing data flagged, not assumed positive |
| Treating fair-lending as optional polish | Guardrail summary is a required output section |
| Silently tightening access to reduce risk | Access/risk trade-off stated explicitly (CM-02) |
