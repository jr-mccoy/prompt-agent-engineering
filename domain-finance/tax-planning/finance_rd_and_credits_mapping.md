---
title: "R&D and Tax-Credit Mapping — Qualifying-Activity Analysis for Credits and Incentives"
category: finance/tax-planning
description: "Map R&D and other tax credits/incentives to qualifying activities and expenditures — applying the four-part test for the research credit, separating QREs (wages/supplies/contract research), and screening employment/energy/investment incentives — as analysis only, routing claims and substantiation to a tax professional."
techniques:
  - NE-11
  - DT-02
  - QA-02
  - DS-02
  - QA-05
difficulty: intermediate
tags:
  - rd-credit
  - tax-credits
  - incentives
  - qre
  - four-part-test
  - section-174
updated: "2026-06-08"
related_prompts:
  - domain-finance/tax-planning/finance_state_nexus_apportionment_mapper.md
  - domain-finance/tax-planning/finance_entity_structure_tax_comparison.md
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not tax, legal, or accounting advice. Credit eligibility, qualification, computation method, and substantiation are fact-intensive, change frequently, and must be determined and claimed by a qualified tax professional (CPA/EA/tax attorney). Verify every credit's rules, rates, base-calculation method, and documentation requirements against current federal and state law as of the analysis date and the applicable jurisdiction.**

## Objective

Produce an auditable mapping that (1) screens candidate activities against credit eligibility tests (notably the four-part test for the research credit), (2) classifies expenditures into qualifying buckets (QREs and others), (3) identifies additional employment/energy/investment incentives that may apply, and (4) surfaces documentation and substantiation gaps — so the user and their tax professional can pursue a defensible claim. This prompt maps and analyzes; it does not compute a final claimable credit or file.

## When to Use

- A company building/improving products, software, or processes wants to scope a potential research credit.
- Year-end planning to identify which projects and costs may qualify before documentation is lost.
- Diligence on a target's claimed credits and the strength of its substantiation.
- Screening for additional incentives (hiring credits, energy/efficiency credits, state-specific programs).
- Building a documentation checklist to support a future credit study.

## Inputs / Context Required

```
<credits_context>
Jurisdiction: Federal + State(s) [name] (many states have their own R&D credit with different rules)
Entity type: C-corp | S-corp | partnership | sole prop (credit flow-through and payroll-offset eligibility vary)
Gross receipts history (for base calc / startup payroll-offset eligibility): [user-supplied by year]
Qualified-small-business / startup status (for payroll-tax offset election): yes | no | unknown

CANDIDATE PROJECTS (repeat per project):
  Project name / description:
  Technical objective (what new/improved functionality?):
  Uncertainty at outset (could the design/method/capability be achieved? how?):
  Process used (experimentation? iterations/prototypes/testing?):
  Field (engineering, software, hard sciences, etc. — note: must be technological in nature):

EXPENDITURES (per project, user-supplied):
  Wages of employees performing/supervising/supporting qualified research: $
  Supplies consumed in research (non-depreciable): $
  Contract research (third-party) cost: $ (note statutory inclusion %)
  Cloud/computer rental for research: $
  Excluded items present? (post-commercial-production, market research, foreign research,
     funded research, reverse engineering, routine data collection, aesthetic/style changes)

OTHER INCENTIVES TO SCREEN:
  Hiring in targeted groups / zones?  Energy efficiency / renewable investment?
  Investment in equipment? State enterprise-zone / job-creation programs?
</credits_context>
```

## Constraints

### Must
- Apply the **four-part test** to each candidate project (DT-02), and require evidence (QA-05) for each part:
  1. **Permitted purpose** — new or improved business component (function, performance, reliability, quality).
  2. **Technological in nature** — relies on hard sciences (engineering, physics, chemistry, computer science, biology).
  3. **Elimination of uncertainty** — uncertainty existed at outset regarding capability, method, or design.
  4. **Process of experimentation** — systematic evaluation of alternatives (modeling, simulation, trial-and-error, testing).
- Screen out **statutory exclusions** explicitly: research after commercial production, adaptation/duplication, surveys/studies, market research, foreign research, funded research (paid for by another and not at the taxpayer's risk / IP retained), routine data, aesthetic/style changes, and certain internal-use-software hurdles.
- Classify expenditures into **QRE buckets** with formula → inputs (NE-11):
  - Qualified wages (often time-tracked or estimated by qualified %),
  - Qualified supplies (consumed, non-depreciable, non-land),
  - Contract research (include only the statutory percentage of third-party cost; non-at-risk arrangements excluded),
  - Qualified cloud/computer rental.
- Note the **§174 capitalization** interaction: research/experimental expenditures may require capitalization and amortization for income-tax purposes even where a credit applies — flag this as a separate, professional-determined item `[verify current §174 treatment]`.
- Present **base-calculation method** as a user/professional choice: regular credit (base-amount method) vs the simplified/alternative method — do NOT pick one; show that the method materially changes the result.
- Flag the **payroll-tax-offset election** availability for qualified small businesses (startups) as a possibility to verify, not a conclusion.
- Screen additional incentives (DS-02) and rank by likely materiality.

### Must Not
- Assert a specific claimable credit amount or current-year rate/limit from memory — require user input or mark `[input/verify]`.
- Conclude a project "qualifies" — output a four-part-test assessment with confidence (likely/uncertain/unlikely); qualification routes to the professional.
- Include excluded categories (market research, post-production, funded, foreign, aesthetic) in QREs.
- Pick a base-calculation method or present a single credit number as definitive.
- Ignore the §174 capitalization interaction when describing the cash benefit.

## Instructions

**Step 1 — Four-part test per project (DT-02, QA-05).**

| Project | Permitted purpose | Technological | Uncertainty | Experimentation | Exclusions present? | Qualification confidence |
|---|---|---|---|---|---|---|
| | evidence | evidence | evidence | evidence | list | Likely/Uncertain/Unlikely |

**Step 2 — Exclusion screen.**
```
For each project, check and document any: post-commercial-production work, funded research,
   foreign research, market/efficiency surveys, routine data collection, duplication/reverse-engineering,
   aesthetic/style changes, internal-use-software high-threshold issues.
Any exclusion narrows or removes the associated QREs — note which costs are carved out.
```

**Step 3 — QRE classification (NE-11).**
```
Qualified wages   = Σ (employee wage × qualified-time %)         [require a basis for the %]
Qualified supplies= Σ supplies consumed in research (non-depreciable)
Contract research = third-party cost × statutory inclusion %      [verify current %]
Cloud/computer    = qualified rental for research
Total QRE (illustrative) = sum of the above   [pre-base, pre-method]
```

**Step 4 — Base-method illustration (do not select).**
```
Show that credit ≈ rate × (QRE − base amount), where:
  - Regular method base depends on a historical fixed-base % × average gross receipts, and
  - Alternative/simplified method uses a % of prior-years' QRE.
Present BOTH as ranges with [verify rate/percentages] and state the method choice is the professional's.
```

**Step 5 — §174 and benefit-timing flag.**
```
Note: even qualifying R&E costs may require capitalization/amortization under §174 for income-tax purposes.
The CREDIT (offset) and the DEDUCTION TIMING (§174) are separate questions — flag both; quantify neither without [verify].
```

**Step 6 — Other-incentive screen (DS-02).**

| Incentive | Trigger present? | Illustrative basis | Likely materiality | Documentation needed |
|---|---|---|---|---|

**Step 7 — Adversarial stress-test (QA-02).**
- Is "uncertainty" genuine technological uncertainty, or just business/economic uncertainty (which does not qualify)?
- Are wage qualified-% estimates defensible under audit, or anchored optimistically without contemporaneous records?
- Is any "R&D" actually funded research (customer-paid, taxpayer not at risk) and therefore excluded?
- Does foreign-performed research dilute the claim?
- Does §174 capitalization reduce the near-term cash benefit the user is anticipating?
- Substantiation: is there contemporaneous project documentation, or will the claim rest on after-the-fact reconstruction (audit risk)?

## Output Format

```
## R&D and Credit Mapping
Jurisdiction: Federal + State [name] | Entity: [type] | As of: [date] | Figures: user-supplied/verify

### Four-Part Test by Project
[Step 1 table with evidence and confidence]

### Exclusion Screen
[Step 2 carve-outs]

### QRE Classification
[Step 3 buckets with formula → inputs → illustrative total]

### Base-Method Illustration (range; method is the professional's choice)
[Step 4 both methods with verify flags]

### §174 / Benefit-Timing Flag
[Step 5]

### Other Incentives
[Step 6 ranked table]

### Stress-Test Findings
[Step 7 — qualification, substantiation, funded/foreign, §174]

### Items to route to your tax professional
[final qualification, method selection, payroll-offset election, §174 treatment, documentation study]
```

## Verification

- [ ] Four-part test applied to every project with evidence cited for each part.
- [ ] Statutory exclusions screened and documented per project.
- [ ] QREs classified into wages/supplies/contract/cloud with formula → inputs.
- [ ] Contract-research statutory inclusion % marked verify; non-at-risk arrangements excluded.
- [ ] Base method shown as a choice (both methods), not a single selected number.
- [ ] §174 capitalization interaction flagged separately from the credit.
- [ ] Payroll-tax-offset eligibility flagged as to-verify, not concluded.
- [ ] Other incentives screened and ranked.
- [ ] No claimable amount or current-year rate asserted from memory.
- [ ] Output frames qualification confidence, not a filed credit.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Calling a project "qualified" | Output is a four-part-test confidence rating; qualification routes to the professional |
| Counting business uncertainty as research uncertainty | Stress-test distinguishes technological uncertainty from economic/market uncertainty |
| Including funded or foreign research in QREs | Exclusion screen explicitly carves these out before QRE totals |
| Presenting one credit number as definitive | Show both base methods as ranges; method choice and final number are the professional's |
| Ignoring §174 capitalization on cash benefit | §174 flagged as a separate timing question; do not net it silently |
| Optimistic wage qualified-% without records | Require a stated basis; stress-test flags reconstruction/audit risk |
| Asserting rates/inclusion %s/limits | All marked `[input/verify]` against current law |
