---
title: "Financial Affidavit and Disclosure Builder"
category: legal/divorce
description: "Build a complete divorce financial disclosure: a sworn income-and-expense declaration (financial affidavit) plus a schedule of assets and debts, organized to the controlling state's mandatory-disclosure rules, with income computation from all sources, monthly expense budget tied to the marital standard of living, asset/debt characterization columns, and a documentation/exhibit checklist."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - divorce
  - family-law
  - financial-affidavit
  - disclosure
  - assets-and-debts
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_marital_property_characterization_analysis.md
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_divorce_discovery_plan_and_requests.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/custody/legal_child_support_calculation_framework.md
---

**Purpose:** Produce the mandatory financial disclosure a divorce court requires — a sworn income-and-expense statement and a complete asset/debt schedule — organized so it satisfies the state's disclosure rule, supports support and division analysis, and is backed by documentation. Output is a structured, sworn disclosure and a supporting-documents checklist, not advice.

**When to use:** Preparing mandatory initial/final disclosures; preparing for a temporary-orders or support hearing; responding to the other party's disclosure; assembling inputs for support and property-division analysis.

---

## Your Input

- **Jurisdiction:** [State; county; court; the state's mandatory-disclosure rule and official form name, if any]
- **Property regime:** [Community / equitable distribution]
- **Disclosing party:** [Name; filing posture; deadline for disclosure]
- **Income sources:** [Wages, self-employment, bonus/commission, K-1/business distributions, rental, investment, benefits, support received, perquisites]
- **Monthly expenses:** [Housing, utilities, food, transportation, insurance, children's expenses, debt service, health, other]
- **Assets:** [Real property, retirement/pension, financial accounts, business interests, vehicles, valuables, receivables; title and acquisition date for each]
- **Debts:** [Mortgages, loans, cards, taxes owed; whose name; when incurred]
- **Separate-property claims:** [Items asserted separate, with basis — premarital, gift, inheritance]
- **Documentation available:** [Pay stubs, tax returns, account statements, deeds, loan docs, appraisals]
- **Marital standard of living:** [Lifestyle facts relevant to support]

---

## Constraints

**Must:**
- Conform to the **state's mandatory-disclosure rule and official form** where one exists `[NEED FORM: …]`; do not substitute another state's schedule.
- Compute **income from all sources**, including non-wage income (self-employment net, K-1 distributions, perquisites, recurring gifts) per the state's income definition `[CITE: …]`.
- Build a **monthly expense budget** tied to the marital standard of living and consistent across the document.
- Provide **asset and debt schedules** with columns for value/balance, title/holder, acquisition date, and **provisional characterization** (marital/community vs. separate).
- Note where a value requires **appraisal or statement** (real property, business, pension) and mark `[NEED VALUATION: …]`.
- Include a **documentation/exhibit checklist** mapping each line to supporting records.
- Include the **sworn declaration** language the state requires (under penalty of perjury) and note the duty to supplement.
- Use placeholders `[CITE: ...]`, `[NEED FORM: ...]`, `[NEED VALUATION: ...]`, `[NEED: ...]` for unsupplied authority, forms, values, or facts.

**Must Not:**
- Invent income figures, account balances, valuations, the state's income definition, or the disclosure rule.
- Omit known income sources, assets, or debts, or understate them — disclosure must be complete and the failure to disclose carries serious consequences (sanctions, set-aside of judgment).
- Characterize property as separate without a stated basis.
- Treat estimates as appraised values without flagging.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Identify the rule and form.** Name the state's mandatory-disclosure rule and official form; note the deadline and the duty to supplement.
2. **Income computation.** List every income source; compute monthly gross and net per the state's definition; treat self-employment and K-1 income carefully (add-backs, perquisites) `[CITE: …]`.
3. **Expense budget.** Build a monthly expense schedule by category, consistent with the marital standard of living; separate the children's expenses where the form requires.
4. **Asset schedule.** List each asset with value, title, acquisition date, characterization, and valuation source; mark items needing appraisal.
5. **Debt schedule.** List each debt with balance, holder, date incurred, and characterization.
6. **Separate-property notes.** For each asserted-separate item, state the basis and the tracing/documentation needed.
7. **Documentation checklist.** Map each line to its supporting document; flag gaps.
8. **Declaration.** Insert the sworn declaration and duty-to-supplement statement.

---

## Output Format

```markdown
# FINANCIAL DISCLOSURE — {Disclosing Party} — Case No. {____}
**State rule / form:** {rule} [NEED FORM: …]   **Deadline:** {date}   **Regime:** {community/equitable}

## A. INCOME (monthly)
| Source | Gross/mo | Net/mo | Basis / notes | Doc |
|---|---|---|---|---|
| Wages | {$} | {$} | {pay stub} | Ex. {} |
| Self-employment/K-1 | {$} | {$} | {net + add-backs [CITE]} | Ex. {} |
| {Other} | {$} | {$} | {…} | {} |
| **Total** | {$} | {$} | | |

## B. MONTHLY EXPENSES
| Category | Amount | Notes | Doc |
|---|---|---|---|
| Housing / mortgage | {$} | {…} | {} |
| {…} | {$} | {…} | {} |
| Children's expenses | {$} | {…} | {} |
| **Total** | {$} | | |

## C. ASSETS
| Asset | Value | Title/holder | Acquired | Characterization | Valuation source | Doc |
|---|---|---|---|---|---|---|
| {Real property} | {$ / [NEED VALUATION]} | {whose} | {date} | Marital/Separate/Mixed | {appraisal} | {} |

## D. DEBTS
| Debt | Balance | Holder | Incurred | Characterization | Doc |
|---|---|---|---|---|---|
| {…} | {$} | {whose} | {date} | Marital/Separate | {} |

## E. SEPARATE-PROPERTY CLAIMS
- {Item} — basis: {premarital / gift / inheritance}; tracing/docs needed: {…}

## F. DOCUMENTATION CHECKLIST
- [ ] {Tax returns (years)} ; [ ] {Pay stubs} ; [ ] {Account statements} ; [ ] {Deeds/loan docs} ; [ ] {Appraisals/valuations}

## G. DECLARATION
I, {name}, declare under penalty of perjury under the laws of {State} that the foregoing is true and complete to the best of my knowledge, and I acknowledge a continuing duty to supplement. {Date / signature}.
```

---

## Verification

- [ ] State's mandatory-disclosure rule and official form identified; deadline and duty to supplement noted.
- [ ] Income computed from all sources, including self-employment/K-1 and perquisites, per the state's definition.
- [ ] Monthly expense budget complete and consistent with the marital standard of living.
- [ ] Asset and debt schedules include value, title, acquisition date, and provisional characterization.
- [ ] Items needing appraisal/valuation flagged [NEED VALUATION].
- [ ] Separate-property claims state a basis and the tracing required.
- [ ] Documentation checklist maps each line to supporting records; gaps flagged.
- [ ] Sworn declaration included.
- [ ] No invented figures, balances, valuations, or rules.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Counting only W-2 wages and omitting self-employment, K-1, or perquisite income | Compute income from all sources per the state's definition [CITE]; address add-backs |
| Presenting estimated values as appraised | Flag [NEED VALUATION] for real property, business, and pension values |
| Characterizing assets as separate with no basis | State premarital/gift/inheritance basis and the tracing needed |
| Omitting a known asset or debt | Disclosure must be complete; nondisclosure risks sanctions and set-aside |
| Using another state's disclosure schedule | Conform to the controlling state's mandatory form [NEED FORM] |
| Inconsistent expense figures across sections | Reconcile the expense budget across the document |
| Forgetting the duty to supplement | State the continuing duty to update disclosure |
| Inventing income figures or balances | Use placeholders and tie each figure to a document |
| Mixing the children's expenses into general expenses where the form separates them | Break out children's expenses as the form requires |
| Omitting the sworn declaration | Include the state's penalty-of-perjury declaration |
