---
title: "Bankruptcy Chapter Selection and Eligibility Analysis"
category: legal/bankruptcy-restructuring
description: "Counsel-facing analysis of whether a debtor is eligible for Chapter 7, Chapter 11, Subchapter V, or Chapter 13, and which chapter best serves the debtor's objectives — gating eligibility bars first, then comparing chapters on control, cost, discharge scope, asset retention, timeline, and creditor dynamics, with every dollar threshold and deadline marked for verification against the current Code."
techniques:
  - ST-01
  - RT-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - bankruptcy
  - chapter-selection
  - subchapter-v
  - means-test
  - eligibility
  - restructuring
  - buried-in-debt
updated: "2026-09-24"
reasoning:
  styles: [analytic, comparative, strategic]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: [memo, matrix]
  user_role: [lawyer]
  mode: [assess, decide]
related_prompts:
  - domain-legal/research/legal_statutory_interpretation.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
  - domain-finance/credit-lending/finance_workout_restructuring_options.md
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
---

# Bankruptcy Chapter Selection and Eligibility Analysis

**Objective:** Produce a counsel-grade memo that (1) tests the debtor against every eligibility gate for each candidate chapter before any strategy discussion, (2) compares the eligible chapters on the dimensions that actually decide the choice — who controls the estate, what is discharged, what the debtor keeps, what it costs, how long it takes, and how the creditor body is likely to behave — and (3) recommends a chapter with the facts that would flip the recommendation. Every statutory dollar limit, look-back period, and filing deadline is treated as a moving target and marked `[VERIFY]`.

**When to use:**
- Pre-filing strategy for an individual, sole proprietor, or business debtor where more than one chapter is plausible.
- Re-evaluating chapter choice after a material change (a lawsuit judgment, a lost contract, a secured lender acceleration).
- Evaluating conversion or dismissal risk in a pending case.

**Distinct from:**
- `domain-finance/credit-lending/finance_workout_restructuring_options.md` — the lender's out-of-court workout menu; this prompt is the debtor-side legal eligibility and chapter choice.
- `domain-legal/personal-self-advocacy/` — layperson preparation; this prompt assumes the reader is bankruptcy counsel and produces legal analysis, not self-help.
- `legal_chapter_11_plan_analysis.md` (this folder) — confirmability of a plan once in Chapter 11.

**Audience:** Bankruptcy and restructuring counsel, and supervised associates or paralegals preparing a filing recommendation.

---

## Your Input

- **Jurisdiction:** [District and circuit — local rules and circuit authority on eligibility disputes differ]
- **Debtor type:** [Individual / married joint / sole proprietor / LLC / corporation / partnership]
- **Debt profile:** [Secured, unsecured, priority, contingent, unliquidated, disputed — with amounts; identify consumer vs. business debt share]
- **Income and household (individuals):** [Current monthly income for the look-back, household size, state of residence]
- **Assets:** [Schedule-level list with values, liens, and claimed exemptions under the applicable exemption scheme]
- **Prior filings:** [Chapter, filing date, dismissal/discharge date and reason, for every prior case]
- **Pre-filing events:** [Credit counseling completed? Transfers to insiders, recent payments, pending litigation, foreclosure or repossession dates]
- **Debtor objectives:** [Keep a house or operating business, stop a sale date, shed a guarantee, liquidate cleanly, deal with tax debt]
- **Business facts (entities):** [Operating or not, cash position, DIP-financing prospects, key contracts and leases, affiliate structure]
- **Current thresholds you have verified:** [Subchapter V and Chapter 13 debt limits, median income figures, and effective dates — or leave blank and they will be marked `[VERIFY]`]

---

## Constraints

### Must
- Run **eligibility before strategy.** A chapter the debtor cannot file under is removed from the comparison, with the disqualifying fact stated.
- Test each chapter's gates in the order the Code applies them: who may be a debtor under the chapter, debt limits, prior-filing bars, credit counseling, means-test presumption (Chapter 7 individuals with primarily consumer debt), and bad-faith / cause for dismissal exposure.
- Separate **consumer from business debt** before applying the means test; the characterization drives whether the test applies at all.
- Compare eligible chapters on a fixed set of dimensions (control, discharge scope, asset retention, cost, timeline, creditor voting and objection leverage, co-debtor and guarantor effects, tax consequences).
- State **what would flip the recommendation** — the facts or valuations the answer is sensitive to.
- Mark every dollar threshold, look-back, and deadline `[VERIFY: provision + effective date]` unless the user supplied a verified figure.

### Must Not
- Invent debt limits, median-income figures, exemption amounts, or filing deadlines. Subchapter V and Chapter 13 limits have changed repeatedly and some temporary increases have lapsed.
- Cite case law without supplied authority; use `[CITE: ...]`, `[NEED HOLDING: ...]`.
- Treat Subchapter V as automatically preferable for small businesses without testing its eligibility conditions and the loss of creditor-vote dynamics that cut both ways.
- Ignore prior-filing effects on the automatic stay (shortened or no stay after recent dismissed cases).
- Recommend pre-filing asset transfers or debt-payment sequencing without flagging avoidance and dischargeability exposure.
- Add generic "consult an attorney" boilerplate; the reader is the attorney.

---

## Instructions

1. **Restate objectives and constraints** in one paragraph: what the debtor must achieve, by when (sale date, levy date, hearing), and what it cannot lose.
2. **Characterize the debt.** Classify each debt as secured / priority / general unsecured, consumer / business, and liquidated / contingent / disputed. Note which debts count toward any debt limit and which may be non-dischargeable in which chapter.
3. **Run the eligibility gates per chapter.** For Chapter 7, 11, Subchapter V, and 13: eligible debtor type, debt limits `[VERIFY]`, prior-filing bars and stay-limiting effects, credit counseling, means test where applicable, and any known cause-for-dismissal risk. Output pass / fail / uncertain with the controlling fact.
4. **Drop ineligible chapters.** Record why. If eligibility is uncertain, say what document or valuation resolves it.
5. **Compare eligible chapters** on the fixed dimensions. Be specific to this debtor — e.g., "Chapter 13 lets the debtor cure the mortgage arrears over the plan; Chapter 7 does not stop the foreclosure beyond the stay period."
6. **Stress-test the leading option.** What will the most motivated creditor do (move for stay relief, object to discharge, move to convert or dismiss, vote against a plan)? What does the trustee or U.S. Trustee scrutinize?
7. **Recommend** a chapter, the sequencing (e.g., file before a sale date; complete counseling first), and the facts that would flip the recommendation.
8. **List verification items** — every threshold, deadline, and authority the recommendation depends on.

---

## Output Format

```markdown
# Chapter Selection Memo — {Debtor}
**Jurisdiction:** {district / circuit}  |  **Prepared:** {YYYY-MM-DD}  |  **Privileged & Confidential — Attorney Work Product**

## 1. Objectives and Hard Dates
{paragraph; table of dates: event | date | consequence}

## 2. Debt Characterization
| Creditor | Amount | Secured / Priority / GUC | Consumer / Business | Contingent / Disputed | Dischargeability notes |

## 3. Eligibility Gates
| Gate | Ch. 7 | Ch. 11 | Subch. V | Ch. 13 | Controlling fact / [VERIFY] |
|---|---|---|---|---|---|
| Eligible debtor type | | | | | |
| Debt limit | n/a | n/a | | | [VERIFY: current limit + effective date] |
| Prior-filing bar / stay effect | | | | | |
| Credit counseling | | | | | |
| Means test (Ch. 7 individual) | | n/a | n/a | n/a | |
| Dismissal / conversion exposure | | | | | |
**Removed from comparison:** {chapter — reason}

## 4. Comparison of Eligible Chapters
| Dimension | {Chapter} | {Chapter} |
|---|---|---|
| Control of estate | | |
| Discharge scope | | |
| Assets retained | | |
| Cost and administrative burden | | |
| Timeline | | |
| Creditor leverage (votes, objections) | | |
| Guarantor / co-debtor effects | | |
| Tax consequences | | |

## 5. Adversary Stress-Test
{most motivated creditor; trustee / UST focus}

## 6. Recommendation
- **Chapter:** {…}
- **Sequencing:** {…}
- **Flip conditions:** {facts that would change the answer}

## 7. Verification Items
- [VERIFY: …]  [CITE: …]
```

---

## Worked Example

**Input (abridged):** Single-member LLC operating a two-location bakery in a district with no circuit authority supplied. Debts: $1.9M bank loan secured by equipment and a blanket lien, personally guaranteed by the owner; $140K sales-tax liability; $260K trade debt; landlord claim for $85K arrears. No prior filings. Owner's objective: keep the stronger location open, reject the weaker lease, and cap guarantee exposure. The user did not supply current debt limits.

**Output (excerpt):**

> **3. Eligibility Gates.** Chapter 13 — **fail**: the LLC is not an individual; Chapter 13 is unavailable to the entity (the owner's own eligibility is a separate question — see Flip conditions). Subchapter V — **uncertain**: total noncontingent liquidated debt is roughly $2.4M; eligibility turns on the current limit and the share arising from commercial activities `[VERIFY: current Subchapter V debt limit and effective date — temporary increases have lapsed before]`. Chapter 11 and Chapter 7 — **pass** on debtor type.
>
> **4. Comparison (Subchapter V vs. Chapter 11 vs. Chapter 7).** Subchapter V keeps management in possession with an appointed Subchapter V trustee in a facilitation role `[VERIFY: §1183 duties]`, removes the creditor-committee default, and relaxes plan-confirmation conditions that would otherwise give the bank's large unsecured deficiency claim a veto `[VERIFY: §1191 confirmation standard]`. Chapter 11 offers the same lease-rejection tool at materially higher administrative cost. Chapter 7 ends operations; the owner's guarantee exposure is untouched in either business chapter and is fully crystallized in Chapter 7.
>
> **6. Recommendation.** Subchapter V if the debt limit is confirmed; otherwise traditional Chapter 11 with an early cash-collateral fight expected. **Flip conditions:** (a) the verified limit is below aggregate qualifying debt; (b) the bank's collateral value exceeds its claim (changes the deficiency-claim dynamics); (c) the sales-tax liability is assessed at a higher figure — a priority tax claim must be paid in full under either reorganization chapter under consideration — in Chapter 11 (including Subchapter V), in regular installment payments within 5 years after the order for relief `[VERIFY: §1129(a)(9)(C)]`; in Chapter 13, in full deferred cash payments over the plan unless the holder agrees otherwise `[VERIFY: §1322(a)(2)]` — which raises the required plan payments; Chapter 7 has no plan, so the tax is instead paid from the estate in priority order and, if nondischargeable, survives `[VERIFY: §§507(a)(8), 523(a)(1)]`.

---

## Verification

- [ ] Jurisdiction lock: district and circuit stated; no authority from elsewhere presented as controlling.
- [ ] Eligibility ran before strategy; every removed chapter has a stated disqualifying fact.
- [ ] Consumer vs. business debt characterized before the means test was applied or waived.
- [ ] Every debt limit, median-income figure, exemption amount, and deadline is either user-verified or marked `[VERIFY]`.
- [ ] Prior-filing stay effects addressed.
- [ ] Comparison uses the fixed dimensions and is specific to this debtor.
- [ ] Flip conditions stated.
- [ ] Citation discipline: no case names, holdings, or pinpoints beyond supplied authority.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Stating a Subchapter V or Chapter 13 debt limit from memory | Limits change and temporary increases have sunset; mark `[VERIFY]` with effective date unless supplied |
| Running the means test on a debtor with primarily business debt | Characterize debt first; the presumption applies only where consumer debt predominates |
| Recommending Chapter 13 for an entity | Only individuals (with regular income) qualify; analyze the owner separately |
| Treating the automatic stay as guaranteed | A dismissed case in the prior year can shorten or eliminate the stay; check prior filings |
| Presenting Subchapter V as strictly debtor-favorable | It trades creditor-vote leverage and cost savings against disposable-income commitments and trustee oversight; show both sides |
| Ignoring guarantor exposure | Entity filings do not stay actions against guarantors by default; address separately |
| Comparison that is generic ("Chapter 11 is expensive") | Tie every comparison cell to this debtor's facts and objectives |
