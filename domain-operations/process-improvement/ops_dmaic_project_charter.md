---
title: "DMAIC Project Charter — Problem Statement, CTQs, Baseline, Scope, and the Measurement-System Check"
category: operations/process-improvement
description: "Charter a Six Sigma DMAIC improvement project before the work starts — a problem statement with no cause or solution in it, CTQs traced to the customer, a baseline with its data source, in/out scope, a goal and benefit estimate labelled as estimates, gate dates, and a measurement-system check that confirms the data can be trusted before Analyze begins."
techniques:
  - DS-01
  - DS-02
  - CM-03
  - QA-04
difficulty: advanced
tags:
  - dmaic
  - six-sigma
  - project-charter
  - ctq
  - baseline
  - measurement-system-analysis
updated: "2026-09-24"
related_prompts:
  - domain-operations/process-improvement/ops_root_cause_a3_report.md
  - domain-operations/process-improvement/ops_process_map_and_waste_scan.md
  - domain-risk/risk_fmea_analysis.md
---

# DMAIC Project Charter

**Objective:** Produce a one-page charter that lets a sponsor approve (or kill) a
DMAIC project on its merits — and that forces the team to prove its baseline data
measures what it claims to before any analysis is done on it.

**When to Use:**
- A process problem is chronic, variable, and multi-causal enough that a single A3
  will not resolve it.
- A sponsor wants a scoped, dated commitment before assigning people.
- Previous improvement efforts stalled because the scope crept or nobody agreed on
  the baseline.
- **Not this prompt if** the problem is narrow and one team can see it end to end —
  use `ops_root_cause_a3_report.md`. If you are assessing what *could* fail rather
  than improving a measured gap, use `domain-risk/risk_fmea_analysis.md` (FMEA is a
  common tool inside Analyze or Improve, not a charter). Software delivery problems
  belong in `domain-engineering-workflows/`.

## Inputs / Context

1. **The pain**, as the customer or the business experiences it.
2. **The process** and its owner.
3. **Existing data**: what is recorded, where, how often, and by whom.
4. **Volume and cost** figures, with source.
5. **Sponsor, team candidates, and available hours.**
6. **Constraints**: systems that cannot change, dates that are fixed, regulations.

## Method

1. **Write the problem statement (DS-02).** What, where, when, how big, and the
   impact — in a number with a unit and a date range. No cause, no solution, no
   blame. Test: could someone who disagrees with your theory still sign it?
2. **Derive CTQs (DS-01).** Voice of customer → need → measurable
   critical-to-quality characteristic with a specification limit or target. Each CTQ
   has an **operational definition**: exactly how it is measured, from which field,
   when the clock starts and stops.
3. **Set the baseline.** Current performance on each CTQ, with source, period, and
   sample size. Show variation (range, or a run chart description), not just the mean.
4. **Scope it (CM-03).** In scope / out of scope as explicit lists — process
   start/end, sites, product lines, systems. Anything not in the in-list is out.
5. **Goal and benefit.** A target on the primary CTQ with a date. The benefit is an
   **estimate**, stated with its assumptions and the name of whoever will validate it
   (usually finance). Include one secondary (guardrail) metric that must not get worse.
6. **Measurement-system check (QA-04).** Before Analyze, confirm:
   - **Validity** — does the field record what the CTQ definition says? Sample
     records against source documents.
   - **Repeatability / agreement** — for attribute data (codes, pass/fail), have
     2–3 people classify the same 20–30 items; report the percentage where all agree.
     A common working threshold is ≥80–90% agreement; below it, fix the definitions
     before trusting any Pareto built on them.
   - For continuous gauge data, a formal gauge R&R study is the standard; note if one
     is needed and who is qualified to run it.
7. **Team, gates, and risks.** Named sponsor, process owner, lead, members with hours.
   D/M/A/I/C gate dates. Top three project risks (not process risks).

## Output Format

```
# DMAIC charter — [project]        Sponsor: [..]  Lead: [..]  Date: [..]

## Problem statement
## CTQs
| Customer need | CTQ | Operational definition | Spec/target |
## Baseline
| CTQ | Current | Period | n | Source | Variation |
## Scope
In: [...]   Out: [...]
## Goal and benefit (estimates)
Primary: [CTQ from X to Y by date]   Guardrail: [metric must not exceed ..]
Benefit estimate: [$ / time] — assumptions: [...] — validated by: [role]
## Measurement-system check
| Check | Method | Result | Pass? | Action |
## Team and gates
| Role | Name | Hours/wk |      Gates: D [..] M [..] A [..] I [..] C [..]
## Project risks
```

## Verification

- [ ] Problem statement contains no cause and no solution.
- [ ] Each CTQ has an operational definition naming the data field and clock rules.
- [ ] Baseline states period, sample size, and source.
- [ ] Scope has explicit in- and out-lists.
- [ ] Benefit is labelled an estimate with named validator.
- [ ] A guardrail metric is named.
- [ ] Measurement-system check is done or scheduled before Analyze, with pass/fail.

## False-Positive Prevention

1. **The solution charter.** "Implement automated invoice matching" is a solution
   seeking a project. Charter the gap; the solution comes out of Analyze.
2. **Trusting the field name.** A field called `paid_date` may hold the batch-created
   date. Validate against source records before baselining.
3. **Pareto on unreliable codes.** If people disagree on how to code a defect, the
   Pareto ranks the coders' habits, not the causes.
4. **Mean-only baselines.** A mean without variation hides whether the problem is a
   shift or a spread — they need different fixes.
5. **Benefit as fact.** Savings projected by the team are a hypothesis; the charter
   says who validates them and when.
6. **Unbounded scope.** "All invoices, all entities" is a program, not a project.
   One process, one boundary, one sponsor.
7. **No guardrail.** Paying invoices on time by skipping three-way match fixes the
   CTQ and creates a control failure.

## Example Output

```
# DMAIC charter — AP late payments     Sponsor: Controller  Lead: AP supervisor

## Problem statement
Jan–Jun: 18% of PO-backed invoices (avg 576 of 3,200/month) were paid after their
due date, incurring $9,400/month in late fees (AP ledger) and supplier holds (4 in Q2).
## CTQs
| Supplier paid on time | Paid ≤ due date | bank release date ≤ invoice due date | ≤5% late |
| Fast approval         | Receipt→approval days | ERP received_ts → approved_ts | ≤5 days |
## Baseline
| Late rate      | 18%     | Jan–Jun | 19,200 | ERP + bank file | monthly 14–23% |
| Receipt→approve| median 9 d | Jun  | 3,150  | ERP             | IQR 4–16 d     |
## Scope
In: PO-backed invoices, US entity, receipt to bank release.
Out: utilities, employee expenses, non-PO invoices, other entities, ERP replacement.
## Goal and benefit (estimates)
Primary: late rate 18% → ≤5% by 31 Mar.   Guardrail: three-way-match exceptions
approved without match stay at 0.
Benefit estimate: late fees fall roughly with late count: $9,400 × (1 − 160/576)
≈ $6,800/month ≈ $81k/yr — assumes fees scale linearly — validated by: FP&A.
## Measurement-system check
| Validity of paid date | 40 invoices vs bank file | 7 of 40 off by 2–4 d (field = batch created) | No | use bank release date |
| Exception-code agreement | 3 clerks × 30 invoices | all 3 agreed on 20 (67%) | No | rewrite codebook, retest before Analyze |
## Team and gates
| Sponsor Controller 1 h | Lead AP supervisor 6 h | 2 AP clerks 3 h | Purchasing rep 2 h | IT analyst 2 h |
Gates: D 10 Oct  M 7 Nov  A 5 Dec  I 30 Jan  C 31 Mar
## Project risks
Month-end close pulls AP staff; bank file access needs IT approval; year-end freeze.
```

## Techniques Used

- **DS-01 Framework Application** — DMAIC charter structure and VOC→CTQ derivation.
- **DS-02 Metric Specification** — operational definitions and baseline with variation.
- **CM-03 Scope Definition** — explicit in/out lists that stop scope creep.
- **QA-04 Uncertainty Acknowledgment** — benefit as estimate; measurement system tested before use.

## Related Prompts

- `ops_root_cause_a3_report.md` — the lighter single-problem alternative.
- `ops_process_map_and_waste_scan.md` — the Measure-phase process map.
- `domain-risk/risk_fmea_analysis.md` — FMEA as an Analyze/Improve tool.
