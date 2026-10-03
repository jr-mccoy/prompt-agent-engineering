---
title: "Grant Post-Award Compliance Review — Allowable Costs, Reporting Calendar, Subrecipient Monitoring, and Audit Readiness for a Government Award"
category: policy/public-administration
description: "Review a government grant after award from the recipient's side: read the award terms and the governing cost rules (the US Uniform Guidance at 2 CFR 200 as the worked example, other jurisdictions' equivalents where they apply), test charged costs against allowability, allocability, reasonableness and documentation, build the financial and performance reporting calendar, classify each pass-through as subrecipient or contractor and size monitoring to risk, and score audit readiness with a traffic-light verdict — distinct from writing the proposal (nonprofit_foundation_grant_proposal, science grant drafters), which is pre-award."
techniques:
  - DS-32
  - DS-33
  - DP-28
  - RT-05
difficulty: advanced
tags:
  - grant-compliance
  - post-award-management
  - uniform-guidance
  - allowable-costs
  - subrecipient-monitoring
  - single-audit-readiness
  - spend-grant-money-correctly
  - prepare-for-grant-audit
  - grant-reporting-deadlines
updated: "2026-10-03"
reasoning:
  styles: [rule_application, analytic, evaluative, systematic]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: team
  output_format: [structured, matrix]
  user_role: [grants_manager, finance_officer, program_director, compliance_officer]
  mode: [evaluate, document]
related_prompts:
  - domain-business-strategy/nonprofit/nonprofit_foundation_grant_proposal.md
  - domain-science/grants-funding/science_grant_budget_justification_drafter.md
  - domain-policy/policy_program_evaluation_design.md
---

# Grant Post-Award Compliance Review

**Objective:** Tell a grant recipient, before the funder or auditor does, which
costs would not survive review, which reports are due when, which pass-through
partners need monitoring and how much, and how ready the file is for audit — with
each finding tied to the award term or rule it rests on.

**Audience:** Grants managers and finance officers at local governments, state
agencies, nonprofits, universities and tribes that receive government awards; and
program directors who spend the money.

**When to Use:**
- A new government award has been signed and you need the compliance plan before
  the first drawdown.
- A quarterly review or an upcoming site visit, desk review or single audit.
- You are passing funds to partner organisations and must decide whether each is a
  subrecipient or a contractor.
- A charge has been questioned and you need to know whether it is defensible.
- **Not this prompt if** you are still **applying** —
  `domain-business-strategy/nonprofit/nonprofit_foundation_grant_proposal.md` (proposal
  and funder fit) and
  `domain-science/grants-funding/science_grant_budget_justification_drafter.md` (research
  budget justification) are pre-award. Measuring whether the funded program worked is
  `domain-policy/policy_program_evaluation_design.md`. A disallowance appeal or fraud
  question goes to counsel.

## Inputs / Context

1. **The award**: notice of award, terms and conditions, approved budget and budget
   narrative, period of performance, cost-share or match requirement, and any
   special conditions.
2. **Governing rules**: for US federal awards, 2 CFR 200 (Uniform Guidance) plus the
   agency's supplement and program statute; for other funders, their grant
   agreement, cost principles and audit regime. State which applies.
3. **The ledger**: expenditures charged to the award by cost category, with
   supporting documentation status.
4. **Payroll charging**: how time and effort are documented for staff charged to
   the award.
5. **Pass-through agreements**: each partner, its role, amount, and agreement type.
6. **Prior findings**: past audit or monitoring findings and corrective actions.

Rule citations come from the user's award and the current published rules; a
section number the user has not supplied is marked `[verify current text]`. This
review flags; the funder's grants officer and the recipient's auditor decide.

## Method

1. **Enumerate the obligations (DS-32).** From the award and rules: allowable
   activities, budget categories and rebudgeting limits (when prior approval is
   needed), match, program income, procurement standards, equipment and property
   rules, reporting, record retention, and closeout.
2. **Set the jurisdiction (DS-33).** Apply the regime that governs this award. In US
   federal practice: cost principles in 2 CFR 200 Subpart E, subrecipient rules at
   200.331–200.332, and a single audit when federal expenditures cross the
   threshold in force for the fiscal year [verify current threshold]. Elsewhere, map
   the funder's equivalents and say where none exists.
3. **Test each cost category (RT-05).** For each: **allowable** (permitted by the
   rules and the award), **allocable** (benefits this award in proportion charged),
   **reasonable** (what a prudent person would pay), **consistently treated**, and
   **documented** (invoice, approval, proof of payment, time records). Unallowable
   classes to check explicitly: entertainment, alcohol, lobbying, fundraising, bad
   debts, fines, and costs outside the period of performance.
4. **Check payroll charging.** Charges must reflect actual effort, not budgeted
   percentages left unadjusted; flag estimates never reconciled to actual.
5. **Classify pass-throughs.** Subrecipient (carries out part of the program,
   makes programmatic decisions, has performance measured against objectives) versus
   contractor (provides goods or services in the normal course of business). Then
   rate each subrecipient's risk (size, experience, prior findings, systems) and set
   monitoring: reports reviewed, desk review, site visit, audit follow-up.
6. **Build the reporting calendar.** Financial reports, performance reports,
   drawdown reconciliations, match documentation, and closeout, each with due date,
   owner and source data.
7. **Verdict (DP-28).** Green / yellow / red per area with stated criteria; the
   questioned-cost total; the corrective actions with owners and dates.

## Output Format

```
# Post-award compliance review — [award ID / program]   Funder: [..]
Period of performance: [..]   Award $[..]   Match [..]   Rules: [..]

## 1. Obligations map
| Area | Requirement | Source (term / rule) | Owner |
## 2. Cost testing
| Category | Charged $ | Allowable | Allocable | Reasonable | Documented | Questioned $ | Note |
## 3. Payroll charging
## 4. Pass-through classification and monitoring
| Partner | Subrecipient / contractor | Why | Risk | Monitoring |
## 5. Reporting calendar
| Report | Period | Due | Owner | Data source |
## 6. Audit readiness (green / yellow / red, with criteria)
## 7. Corrective actions
| Finding | Action | Owner | Due |
Not a legal opinion; funder and auditor determinations govern.
```

## Verification

- [ ] The governing regime is named; no rule section is cited without `[verify]` unless supplied.
- [ ] Every cost category is tested on all five attributes.
- [ ] Questioned costs are totalled and traced to specific transactions.
- [ ] Each pass-through has a reasoned subrecipient/contractor call.
- [ ] Subrecipient monitoring scales with assessed risk.
- [ ] Reporting calendar has a date and an owner for every report.
- [ ] Traffic-light criteria are stated before the verdicts.

## False-Positive Prevention

1. **"It's in the budget, so it's allowable."** The approved budget does not make
   an unallowable cost allowable.
2. **Budgeted effort as actual effort.** Charging 50% of a salary because the
   budget says 50% fails if the person worked 20% on the award.
3. **Calling a subrecipient a vendor.** Labelling avoids monitoring duties only if
   the relationship is genuinely a procurement; the substance decides.
4. **Period-of-performance blind spot.** Costs incurred before the start date or
   after the end date (other than closeout costs) need specific authority.
5. **Over-flagging.** A missing signature on a small purchase is a documentation
   gap with a fix, not a fraud finding. Severity is proportionate.
6. **US rules as universal.** Other jurisdictions and private funders differ; say
   which rules you applied.

## Example Output

```
# Post-award compliance review — Workforce Pathways (federal pass-through via state)
Funder: State Workforce Agency (federal funds)   Period: 1 Jul 2026 – 30 Jun 2028
Award $1,200,000   Match 10% ($120,000)   Rules: 2 CFR 200 + award terms [verify current]
Review date: month 3; charged to date $186,400

## 2. Cost testing
| Personnel     | 112,000 | Y | Partly | Y | Partly | 9,800  | 2 case managers at 100% also run a city-funded program |
| Fringe        | 33,600  | Y | Follows personnel | Y | Y | 2,940 | Follows the personnel adjustment |
| Training (ITA)| 24,000  | Y | Y | Y | Y | 0      | Provider on state eligible list |
| Supplies      | 6,300   | Y | Y | Y | Partly | 0      | 2 invoices lack approval — fixable |
| Meals/event   | 1,900   | Partly | Y | ? | Y | 640 | $640 alcohol at partner reception — unallowable |
| Subaward      | 8,600   | Y | Y | Y | N | 8,600 | No invoice detail from Northside CBO |
Questioned: $21,980 (11.8% of charged)

## 3. Payroll charging
3 staff charged from budget percentages; no after-the-fact reconciliation yet.
Case managers' timesheets show 70% on award → reduce charge by $9,800 + fringe $2,940.

## 4. Pass-throughs
| Northside CBO | Subrecipient | Enrols and serves participants; outcomes measured | High (new, no prior federal award) | Monthly invoice detail, desk review Q2, site visit Q3 |
| TechSkills LLC | Contractor | Sells a standard course to the public at catalog price | Low | Procurement file only |

## 5. Reporting calendar
| Quarterly financial | Q1 | 30 Oct | Finance | GL + drawdowns |
| Quarterly performance | Q1 | 30 Oct | Program | case-management system |
| Match certification | Q1 | 30 Oct | Finance | in-kind log |
| Subrecipient monitoring note | Q2 | 15 Jan | Grants mgr | desk review |

## 6. Audit readiness
Costs: YELLOW (questioned < 15%, all correctable). Payroll: RED (no reconciliation
method). Subrecipient: RED (no risk assessment on file, no invoice detail).
Reporting: GREEN (calendar set, owners named). Match: YELLOW (in-kind not valued yet).

## 7. Corrective actions
| Payroll reconciliation each quarter | Finance lead | 15 Oct |
| Reverse alcohol $640 to unrestricted funds | Accountant | 10 Oct |
| Northside risk assessment + agreement amendment for invoice detail | Grants mgr | 20 Oct |
Not a legal opinion; funder and auditor determinations govern.
```

## Techniques Used

- **DS-32 Regulatory Enumeration Pattern** — the obligations map built from the award terms and cost rules.
- **DS-33 Jurisdiction-Adaptive Output** — US Uniform Guidance as worked example; other regimes mapped, not assumed.
- **DP-28 Traffic-Light Verdict System** — readiness by area against stated criteria.
- **RT-05 Evidence-Based Reasoning** — each questioned cost traced to transactions and documents.

## Related Prompts

- `domain-business-strategy/nonprofit/nonprofit_foundation_grant_proposal.md` — the pre-award proposal this compliance plan follows.
- `domain-science/grants-funding/science_grant_budget_justification_drafter.md` — the research budget justification written at application.
- `domain-policy/policy_program_evaluation_design.md` — whether the funded program achieved its outcomes.
