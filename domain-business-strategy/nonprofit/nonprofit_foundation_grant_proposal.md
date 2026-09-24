---
title: "Foundation and Government Grant Proposal — Funder-Fit Gate, Then the Narrative"
category: business-strategy/nonprofit
description: "Decide whether a nonprofit should apply to a specific foundation or government program at all — priorities, geography, eligibility, award size, cost-to-apply against odds — and only then draft the proposal sections from the organisation's own logic model, budget and evidence; distinct from the research-grant outliners in domain-science/grants-funding/, which serve a PI writing to NSF, NIH or ERC review criteria."
techniques:
  - QA-08
  - RT-05
  - CM-02
  - ST-03
  - QA-01
difficulty: intermediate
tags:
  - nonprofit
  - grant-writing
  - foundations
  - government-grants
  - fundraising
  - funder-fit
updated: "2026-09-24"
related_prompts:
  - domain-science/grants-funding/science_nsf_proposal_outliner.md
  - domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md
  - domain-business-strategy/nonprofit/nonprofit_operating_budget_restrictions.md
---

# Foundation and Government Grant Proposal

**Objective:** Run a funder-fit gate before a single paragraph is written, then draft
a proposal whose need statement, program design, outcomes, evaluation and budget all
come from the organisation's own documents — so the application is one the funder
can say yes to, and one the organisation can deliver if it does.

**When to Use:**
- A program officer, a board member or a database search has surfaced a funder and
  someone is about to spend thirty hours on an application.
- You have a program, a logic model and a budget, and need them turned into the
  funder's sections without losing internal consistency.
- A government notice of funding opportunity (NOFO) or RFP has arrived and you need
  a compliance matrix before drafting.

**Not this prompt if:**
- You are a researcher writing to NSF, NIH or ERC review criteria — use
  `domain-science/grants-funding/science_nsf_proposal_outliner.md` and its siblings,
  which are organised around intellectual merit and specific aims, not community need.
- You do not yet have a logic model — build it first with
  `domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md`.
  This prompt consumes one; it does not derive one.
- You need the general case for the organisation, not one funder's application —
  `nonprofit_case_for_support.md`.

## Inputs

1. **The funder's own materials:** guidelines, priorities, eligibility, award range,
   deadline, reporting requirements, and — for foundations — the recent grants list
   or public filing that shows who they actually fund.
2. **The program:** its logic model, current participant numbers, staff, and what it
   has measured so far (with source and date for every number).
3. **The program budget**, including other committed and pending funding.
4. **Hours available** to write, and who reviews.
5. **For government grants:** the full NOFO, registration status, match requirement,
   and whether the organisation has a negotiated indirect cost rate.

## Method

1. **Gate 0 — funder fit (QA-08).** Score six criteria before drafting anything:

   | Criterion | Pass means |
   |---|---|
   | Priority match | The program fits a *stated* priority in the funder's words, not by stretching |
   | Geography | The service area is inside theirs |
   | Eligibility | The organisation meets stated eligibility — **confirmed from documents, not asserted** |
   | Award size | The request sits inside the award range and below ~25% of the program budget unless the funder says otherwise |
   | Precedent | Their recent grants include organisations of similar size and type |
   | Burden | Reporting and match requirements are ones you can meet |

   Verdict: **Go**, **Go with conditions** (name them), or **No-go**. Two failed
   criteria is a No-go regardless of how attractive the money is.

2. **Price the application.** Expected value = award × realistic odds. Compare with
   writing hours. If the funder does not publish odds, mark the estimate `[verify]`
   and say where it came from. A low-odds, high-effort application is a decision to
   make deliberately, not by default.

3. **Build the compliance matrix (CM-02).** Every requirement from the guidelines or
   NOFO in one table: section, page or character limit, required attachment, where
   it is answered. Government applications fail on compliance more often than on
   merit.

4. **Draft each section from evidence (RT-05).**
   - **Need:** local data with source and year; one sentence on why *this*
     organisation. No beneficiary story unless one has been supplied with consent.
   - **Program design:** activities, dosage, staffing — taken from the logic model.
   - **Outcomes and evaluation:** the logic model's indicators, the baseline, the
     target, and who measures. Targets must be derivable from past results.
   - **Capacity:** track record with numbers the organisation can document.
   - **Budget and narrative:** every line traceable; indirect costs at the funder's
     cap or the organisation's rate — see `nonprofit_operating_budget_restrictions.md`.
   - **Sustainability:** what funds the program after this grant ends.

5. **Cross-check (QA-01).** Participant counts, costs per participant and targets
   must agree across narrative, budget and logic model.

6. **Flag what needs a qualified reviewer.** Tax-exempt status, fiscal sponsorship,
   lobbying restrictions in the grant agreement, federal registration and cost
   principles are flagged for the executive director, auditor or counsel. The prompt
   drafts; it does not determine eligibility.

## Output Format

```
# Grant proposal — [funder] / [program]

## Gate 0: funder fit
| Criterion | Evidence | Pass / Fail |
Verdict: [Go | Go with conditions | No-go] — [reason]
Application economics: [award] × [odds, source] = [EV] against [hours]

## Compliance matrix
| Requirement | Limit | Answered in | Status |

## Draft sections
### Need  ### Program design  ### Outcomes and evaluation
### Organisational capacity  ### Budget narrative  ### Sustainability

## Consistency check
| Figure | Narrative | Budget | Logic model | Agree? |

## Flags for qualified review
- [item] — [who reviews]
```

## Verification

- [ ] Gate 0 was scored before any section was drafted.
- [ ] Every statistic has a source and a year, or is marked `[verify]`.
- [ ] No outcome target exceeds what past results support.
- [ ] Budget total equals the sum of its lines and the funding sources.
- [ ] Every compliance-matrix row is answered.
- [ ] Eligibility and exempt-status items are flagged, not asserted.

## False-Positive Prevention

1. **"They fund education" is not a fit.** Fit is a stated priority, a geography and
   a precedent grant. Mission adjacency is how organisations write thirty
   applications and win two.
2. **Do not stretch the program to fit the funder.** A program reshaped for one
   grant becomes a second program the organisation cannot staff.
3. **Never invent a statistic or a beneficiary story.** If a number is missing,
   write `[need: local literacy rate, source]`. A fabricated figure discovered at
   a site visit ends the relationship.
4. **Outcomes are not outputs.** "240 tutoring sessions" is an output; "learners
   gain one reading level" is an outcome. Funders read the difference.
5. **Indirect costs are not padding.** Stating them at the allowed rate is correct;
   hiding them in program lines is the error.
6. **Eligibility is a document question.** Confirm status from the organisation's
   records and public registries; do not treat the drafter's belief as proof.
7. **Dual failure:** do not pass a weak fit to be encouraging, and do not reject a
   good fit because odds are unpublished — mark the odds `[verify]` and decide.

## Example Output

```
# Grant proposal — Hartwell Family Foundation / Riverbend Adult Literacy Tutoring

## Gate 0: funder fit
| Criterion | Evidence | Result |
| Priority match | Guidelines list "adult basic education" as priority 2 of 3 | Pass |
| Geography | Serves Marion County; funder area is three counties incl. Marion | Pass |
| Eligibility | Requires public charity status — confirm with determination letter on file | Pass [verify] |
| Award size | Range $25k–$75k; request $55,000 = 63% of $87,400 program budget | Condition |
| Precedent | Recent grants list: 2 literacy orgs with budgets under $600k | Pass |
| Burden | One interim + one final report; no match | Pass |
Verdict: Go with conditions — request is 63% of program cost; the narrative must
show the other $32,400 is committed or pending.
Economics: $55,000 × ~15% (18 grants from ~120 requests, funder's annual report
[verify]) = $8,250 EV against 30 writing hours.

## Compliance matrix
| Requirement | Limit | Answered in | Status |
| Need statement | 500 words | §Need | Drafted |
| Program budget | Funder template | Attachment B | Drafted |
| Board list | — | Attachment C | Needs update |
| Most recent audit or financial statements | — | Attachment D | On file |

## Draft sections (excerpt)
Need: "Marion County's adult basic literacy rate is [need: rate, source, year].
Riverbend's waitlist stood at 64 adults on 1 August 2026 (intake log)."
Outcomes: 80 learners enrolled; 60% (48) gain one reading level on the program's
existing assessment within 9 months — last year's rate was 58% of 72 learners.
Budget narrative: direct costs $76,000 (coordinator 0.75 FTE $42,000 + benefits
$8,400; materials $6,000; assessments $3,600; space $7,200; tutor training $4,800;
evaluation $4,000) + indirect at funder cap 15% ($11,400) = $87,400.
Funding: Hartwell $55,000 (requested); city grant $20,000 (committed); individual
donors $12,400 (budgeted from prior-year giving) = $87,400.
Sustainability: city grant renews annually; donor share rises to $25,000 by year 3.

## Consistency check
| Figure | Narrative | Budget | Logic model | Agree? |
| Learners | 80 | $87,400 / 80 = $1,093 each | 80 | Yes |
| Outcome target | 48 (60%) | — | 60% | Yes |

## Flags for qualified review
- Exempt-status confirmation — executive director, from IRS records
- Grant agreement lobbying clause — board treasurer / counsel before signature
```

## Techniques Used

- **QA-08 Gate-Based Verification:** the funder-fit gate precedes drafting.
- **RT-05 Evidence-Based Reasoning:** every number carries a source or a marker.
- **CM-02 Constraint Specification:** the compliance matrix holds the funder's limits.
- **ST-03 Output Format Specification:** fixed sections that map to funder templates.
- **QA-01 Self-Verification:** the consistency check across narrative, budget and model.

## Related Prompts

- `domain-science/grants-funding/science_nsf_proposal_outliner.md` — research grants, a different review logic
- `domain-education-teaching/program/evaluation-analytics/program_logic_model_designer.md` — the logic model this prompt consumes
- `domain-business-strategy/nonprofit/nonprofit_operating_budget_restrictions.md` — indirect rates and restricted funds
- `domain-business-strategy/nonprofit/nonprofit_case_for_support.md` — the organisation-level case grant sections draw from
