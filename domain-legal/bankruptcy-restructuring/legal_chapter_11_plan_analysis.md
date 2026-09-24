---
title: "Chapter 11 Plan Confirmability Analysis"
category: legal/bankruptcy-restructuring
description: "Test a proposed Chapter 11 or Subchapter V plan against the confirmation requirements — classification, impairment and voting math, best-interests (liquidation comparison), feasibility, cramdown (unfair discrimination and fair-and-equitable / absolute priority), and priority-claim treatment — producing a requirement-by-requirement scorecard, the objections each constituency will raise, and the plan changes that cure them."
techniques:
  - RT-02
  - DS-01
  - QA-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - bankruptcy
  - chapter-11
  - plan-confirmation
  - cramdown
  - absolute-priority
  - feasibility
updated: "2026-09-24"
reasoning:
  styles: [analytic, adversarial, structural]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: small_team
  output_format: [memo, matrix]
  user_role: [lawyer]
  mode: [audit, assess]
related_prompts:
  - domain-legal/bankruptcy-restructuring/legal_chapter_selection_and_eligibility_analysis.md
  - domain-legal/bankruptcy-restructuring/legal_proof_of_claim_drafter.md
  - domain-finance/valuation/finance_dcf_model_auditor.md
  - domain-finance/credit-lending/finance_workout_restructuring_options.md
---

# Chapter 11 Plan Confirmability Analysis

**Objective:** Score a proposed plan against each confirmation requirement, show the voting arithmetic class by class, run the liquidation comparison and feasibility tests against the supplied projections, and — where an impaired class is expected to reject — test cramdown. The output tells the drafting team which requirements are met, which are contested, what each constituency will argue, and which plan amendments cure the problem at what cost to other classes.

**When to use:**
- Debtor's counsel stress-testing a draft plan before filing it with the disclosure statement.
- Creditor or committee counsel evaluating whether to object or vote against.
- Re-scoring after a plan amendment, a valuation fight, or a class vote result.

**Distinct from:**
- `domain-finance/credit-lending/finance_workout_restructuring_options.md` — out-of-court options; no confirmation standards apply there.
- `domain-finance/valuation/finance_dcf_model_auditor.md` — audits the valuation model itself; this prompt consumes the valuation and asks whether the plan clears legal tests with it.
- `legal_363_sale_strategy_memo.md` (this folder) — a sale outside a plan; flag here if the plan is really a sale in disguise.

**Audience:** Restructuring counsel for debtors, committees, or major creditors.

---

## Your Input

- **Jurisdiction:** [District and circuit — cramdown and classification doctrine vary by circuit]
- **Case type:** [Traditional Chapter 11 / Subchapter V / single-asset real estate / prepackaged]
- **Plan draft:** [Class structure and treatment of each class — paste]
- **Claims register summary:** [By class: number of holders and dollar amounts; disputed claims noted]
- **Liquidation analysis:** [Hypothetical Chapter 7 recovery by class, with assumptions]
- **Projections:** [Plan-period cash flows, capital needs, exit financing commitments]
- **Valuation:** [Enterprise value and collateral values, source and date]
- **Expected votes:** [Which classes will accept, reject, or are uncertain — and why]
- **Equity treatment:** [Old equity retained? New-value contribution? Releases for insiders?]
- **Releases / exculpation / injunction provisions:** [Paste]
- **Controlling authority supplied:** [Cases on classification, new value, third-party releases, cramdown interest rate — or leave blank]

---

## Constraints

### Must
- Walk **every confirmation requirement** the plan must meet, marking Met / Contested / Not Met with the fact that decides it; mark the statutory subsection as `[VERIFY: §1129(a)(_)]` rather than reciting text from memory.
- Show **voting math** per class: acceptance requires thresholds by amount and number of claims actually voting `[VERIFY: §1126(c)]`; identify whether at least one impaired, non-insider class accepts.
- Run **best interests** creditor-by-creditor for impaired dissenting holders: plan recovery vs. hypothetical Chapter 7 recovery, with the liquidation assumptions visible.
- Test **feasibility** against the projections — debt service coverage, exit financing, cushion — and name the assumptions that drive it.
- For each rejecting impaired class, test **cramdown**: unfair discrimination among same-priority classes, and fair-and-equitable (secured: lien retention plus present-value stream or indubitable equivalent; unsecured: absolute priority unless the case is Subchapter V, where a different standard applies `[VERIFY: §1191(b)–(c)]`).
- Flag **classification** used to manufacture an accepting class (gerrymandering) and **artificial impairment**.
- Identify the **objection each constituency will raise** and the cure, with its cost to other classes.

### Must Not
- Invent a cramdown interest rate, discount rate, or valuation; take them from inputs or mark `[NEED: …]`.
- Present third-party release law as settled; it is jurisdiction- and time-sensitive `[NEED HOLDING: current controlling authority]`.
- Apply the absolute priority rule to a Subchapter V plan without noting the separate standard.
- Treat insider-class acceptance as satisfying the impaired-accepting-class requirement.
- Cite cases not supplied; use `[CITE: …]`.

---

## Instructions

1. **Map the plan.** Table of classes: claims included, impaired or not, treatment, expected vote.
2. **Test classification.** Are substantially similar claims placed together? Is any separate classification justified by a legitimate reason other than vote engineering?
3. **Voting math.** For each class, compute acceptance under both thresholds using expected votes; identify at least one impaired, non-insider accepting class or flag its absence as fatal to non-consensual confirmation.
4. **Best interests.** For each impaired class with expected dissenters, compare plan recovery to liquidation recovery. Surface the liquidation assumptions that, if challenged, flip the result.
5. **Feasibility.** Test projections: revenue assumptions against history, capex, working capital, exit financing, balloon payments. Identify the single assumption most likely to be attacked.
6. **Priority and administrative claims.** Confirm the plan pays administrative and priority claims as required, including timing for priority tax claims `[VERIFY: §1129(a)(9)]`.
7. **Cramdown.** For each rejecting class: unfair discrimination test among same-priority classes; fair-and-equitable test (secured / unsecured / equity). Address any new-value argument for retained equity against supplied authority.
8. **Other provisions.** Releases, exculpation, injunctions, good faith, disclosure of insider compensation — flag contested items.
9. **Objection map and cures.** For each constituency, the likely objection, its strength, the cure, and who pays for the cure.
10. **Overall confirmability rating** with the two or three items that decide it.

---

## Output Format

```markdown
# Plan Confirmability Analysis — In re {Debtor} ({district}, Case No. {…})
**Plan version:** {date}  |  **Case type:** {…}  |  **Privileged & Confidential**

## 1. Class Map
| Class | Claims | Amount | Impaired? | Treatment | Expected vote |

## 2. Confirmation Scorecard
| Requirement | Status (Met / Contested / Not Met) | Deciding fact | Authority |
|---|---|---|---|
| Plan complies with applicable provisions | | | [VERIFY: §1129(a)(1)] |
| Best interests | | | [VERIFY] |
| Impaired accepting class (non-insider) | | | [VERIFY] |
| Administrative / priority treatment | | | [VERIFY] |
| Feasibility | | | [VERIFY] |
| {…} | | | |

## 3. Voting Math
| Class | Amount voting | Amount accepting | % | Number voting | Number accepting | % | Result |

## 4. Best-Interests Comparison
| Class | Plan recovery (%) | Ch. 7 recovery (%) | Key liquidation assumption |

## 5. Feasibility
{projection test; most-attackable assumption}

## 6. Cramdown (per rejecting class)
- **Unfair discrimination:** {…}
- **Fair and equitable:** {…}

## 7. Other Contested Provisions
## 8. Objection Map and Cures
| Constituency | Objection | Strength | Cure | Cost of cure / who bears it |

## 9. Confirmability Rating
{Likely / Contested / Unlikely — deciding items}
```

---

## Worked Example

**Input (abridged):** Hotel operator, traditional Chapter 11. Class 1: bank secured $14M (collateral valued $11M by debtor). Class 2: bank deficiency $3M. Class 3: trade GUC $1.2M. Class 4: old equity retains 100% on a $500K new-value contribution. Bank will reject Classes 1 and 2. Trade expected to accept. Plan pays GUC 20%. Liquidation analysis: GUC recovers 4%.

**Output (excerpt):**

> **Classification flag:** Separating the bank's $3M deficiency (Class 2) from trade (Class 3) is the gating issue. If the deficiency were classified with trade, the bank's $3M against $1.2M trade would control that class by amount and defeat acceptance. Separate classification needs a justification other than securing an accepting class `[NEED HOLDING: circuit authority on classification of deficiency claims]`.
>
> **Voting math:** Class 3 accepts (trade) — impaired, non-insider → requirement met *only if* the classification survives.
>
> **Cramdown, Class 2:** Old equity retains property while Class 2 is not paid in full → absolute priority problem. The new-value argument requires the contribution to be new, substantial, in money or money's worth, necessary, and reasonably equivalent to what is retained; retention without market testing of the equity is vulnerable `[NEED HOLDING: controlling authority on new value and market test]`.
>
> **Cure:** Open the equity to competing bids (cost: equity holders may lose control), or pay Class 2 in full over time (cost: feasibility — debt service coverage drops below 1.1x on debtor's own projections).
>
> **Rating:** Contested — turns on classification and the new-value market test.

---

## Verification

- [ ] Jurisdiction lock: circuit stated; classification, release, and cramdown authority limited to supplied or placeholder citations.
- [ ] Every confirmation requirement scored with a deciding fact.
- [ ] Voting math shows both thresholds and excludes insider votes from the impaired-accepting-class test.
- [ ] Best interests compared per impaired class with liquidation assumptions visible.
- [ ] Feasibility tied to specific projection assumptions.
- [ ] Cramdown tested per rejecting class; Subchapter V standard used where applicable.
- [ ] No invented cramdown rates, valuations, or holdings.
- [ ] Each objection paired with a cure and its cost.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Declaring the plan confirmable because "most classes accept" | Non-consensual confirmation needs every rejecting class to pass cramdown and one impaired non-insider accepting class |
| Counting insider acceptance toward the impaired-accepting-class requirement | Exclude insider votes for that requirement |
| Reciting "fair and equitable" without applying it by class type | Secured, unsecured, and equity tests differ; apply the one that fits |
| Applying absolute priority to a Subchapter V plan | Use the Subchapter V standard and its disposable-income requirement |
| Accepting the debtor's liquidation analysis uncritically | Surface the assumptions (forced-sale discounts, Chapter 7 costs) that the objector will attack |
| Treating third-party releases as routinely approvable | Controlling law has shifted; require current authority |
| Picking a cramdown interest rate | Take from inputs or supplied authority; otherwise `[NEED]` |
