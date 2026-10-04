---
title: "Project Closeout and Lessons Learned — Acceptance, Handover, Commercial Close, a Variance Account That Sums, and Lessons That Change an Artifact"
category: operations/project-delivery
description: "Close a finished non-software project properly: deliverables accepted against the definition of done with a dated snag list, ownership handed to operations with warranties and manuals, every vendor account and open commitment closed, a plan-versus-actual account of schedule and cost whose causes add up to the variance, and lessons learned that are each tied to an owner and to the template, checklist or estimating record they change."
techniques:
  - QA-08
  - RT-05
  - RT-09
  - DS-40
difficulty: intermediate
tags:
  - project-closeout
  - lessons-learned
  - handover
  - punch-list
  - variance-analysis
  - vendor-closeout
  - wrap-up-a-project
  - what-went-wrong-on-the-project
  - loose-ends-after-event
updated: "2026-10-03"
related_prompts:
  - domain-operations/project-delivery/ops_non_software_project_plan.md
  - domain-operations/project-delivery/ops_schedule_recovery_plan.md
  - domain-decision-making/documentation/decisiondoc_after_action_report.md
---

# Project Closeout and Lessons Learned

**Objective:** End a project so nothing is left running, owed, or forgotten — formal
acceptance, a clean handover to whoever owns the result, every account and temporary
service closed — and turn plan-versus-actual into a few lessons that change how the
next project is planned.

**When to Use:**
- A facility move, fit-out, event, installation, or rollout has reached its date and
  the team is about to disperse.
- Vendors still have final invoices, deposits, or disputes open.
- The same overrun keeps recurring across projects and nobody has written down why.
- **Not this prompt if** you need a decision-level after-action report (was the
  *decision* sound, separate from the outcome) — use
  `domain-decision-making/documentation/decisiondoc_after_action_report.md`; after a
  risk event, `domain-risk/risk_after_action_review.md`; after a software incident,
  `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md`; after a
  game ships, `domain-game-development/production/production_project_postmortem.md`.
  A safety event during the project goes to
  `domain-operations/quality-safety/ops_safety_incident_investigation.md`. This prompt
  is the operational close of a physical or organizational project.

## Inputs / Context

1. **The plan**: definition of done, WBS, baseline schedule and budget, RACI (from
   `ops_non_software_project_plan.md`), plus any recovery re-baseline.
2. **Actuals**: milestone dates, final or forecast cost per line, approved change orders.
3. **Acceptance state**: per deliverable, who accepted it, when, and open defects.
4. **Commercial state**: vendor contracts, POs, deposits, retentions, credits, disputes.
5. **Handover material**: manuals, as-built drawings, warranties, keys and access,
   spare parts, data the project created, and the receiving owner for each.
6. **Team input**: a short written note from each party (internal and vendors) on what
   helped and what cost time or money — collected before the debrief.

## Method

1. **Acceptance gate (QA-08).** For each deliverable: accepted by its Accountable with
   evidence, accepted with snags, or not accepted. Snags get an owner and a date. A
   deliverable without acceptance is not closed, whatever the schedule says.
2. **Handover.** Name the receiving owner for every lasting thing: building systems,
   equipment, data, vendor relationships. Build a warranty register (item, start,
   expiry, claim contact) and send maintenance tasks to the site's maintenance plan.
   Data collected for the project gets a retention or deletion date per policy.
3. **Commercial close.** Reconcile each vendor: contract + approved changes − credits =
   final account. Track deposits and retentions with release conditions and dates.
   Close POs, cancel temporary services (rentals, storage, temporary power, subscriptions)
   — these "zombie costs" outlive most projects.
4. **Plan versus actual (RT-05).** Schedule: baseline vs. actual per milestone, with a
   slip account. Cost: budget vs. actual per line. Every variance is attributed to a
   cause with evidence, and the causes **sum to the total**. Scope delivered vs. planned.
5. **Root causes, not symptoms (RT-09).** For the two or three largest variances, ask
   why until you reach something the next project can control (a missing gate, an
   estimating assumption, a contract clause). Separate decision quality from luck:
   favourable weather is not a lesson.
6. **Lessons that change an artifact (DS-40).** Each lesson: observation (evidence) →
   cause → change → owner → **where it lives** (plan template gate, contract checklist,
   vendor scorecard, estimating record). A lesson with no artifact to change is noted,
   not counted. Record actual durations and rates as estimating data.
7. **Outcome check.** Results not measurable at close (adoption, satisfaction, pipeline,
   running cost) get a dated check with an owner, 30–90 days out.
8. **Release.** Release people and spaces, archive the record, and close permits and
   sign-offs. Regulated sign-offs (occupancy, fire, electrical) are confirmed by the
   responsible authority, not by this document.

## Output Format

```
# Closeout — [project]   Closed: [date]   Sponsor: [..]   PM: [..]

## Acceptance
| Deliverable | Accountable | Status (accepted / with snags / not) | Evidence | Snags → owner, date |

## Handover
| Item | Receiving owner | Material handed over | Warranty / retention date |

## Commercial close
| Vendor | Contract | Changes | Credits | Final account | Open (deposit, dispute) | Close by |
Temporary services cancelled: [list, with end dates]

## Plan vs actual
Schedule: | Milestone | Baseline | Actual | Slip | Cause |
Cost:     | Line | Budget | Actual | Variance | Cause |
Variance account: [causes] = [total]  (must sum)
Scope: [delivered vs planned; deferred items and new owner]

## Root causes (top 2–3 variances)
## Lessons
| # | Observation (evidence) | Cause | Change | Owner | Artifact changed |
Keep doing: [...]   Luck, not lesson: [...]
## Estimating data recorded
## Outcome check: [measure] on [date], owner [..]
```

## Verification

- [ ] Every deliverable has an acceptance status from its Accountable, with evidence.
- [ ] Every snag and open commercial item has an owner and a date.
- [ ] Warranties and retentions are registered with dates and a receiving owner.
- [ ] Temporary services are cancelled with end dates.
- [ ] Schedule and cost variance causes sum to the totals.
- [ ] Each counted lesson names the artifact it changes and an owner.
- [ ] Favourable outcomes due to luck are labelled as luck.
- [ ] An outcome check is dated where results are not yet measurable.

## False-Positive Prevention

1. **Date reached = project closed.** Unaccepted deliverables and open accounts mean it
   is not; the cost of an unclosed deposit or a forgotten rental is real money.
2. **Variance explained by adjectives.** "Vendor issues" is not a cause. Name the
   clause, the gate, or the estimate, with the amount it accounts for.
3. **Lessons as a wish list.** "Communicate better" changes nothing. If no template,
   checklist, or contract changes, it is not a lesson learned — it is a lesson noted.
4. **Blame as root cause.** "The AV vendor was slow" usually traces to a late input the
   project gave them. Stop at the controllable condition, not the person.
5. **Outcome bias.** A good result from a risky bet is not validation; a bad result from
   a sound call is not a mistake. Judge the decision on what was known then.
6. **Only the PM's view.** Vendors and the receiving owner see different failures;
   collect their notes before the debrief so the loudest voice does not set the record.
7. **Signing off regulated items here.** Occupancy, fire and electrical sign-offs come
   from the authority or licensed professional; record them, do not grant them.

## Example Output

```
# Closeout — Annual sales conference (420 attendees)   Closed: 24 Oct   Sponsor: CRO

## Acceptance
| Event delivered        | Events lead   | accepted          | run-of-show log, survey n=287 | — |
| Attendee data handover | Marketing ops | accepted with snag| CRM import 96% matched | 17 records → MOps, 31 Oct |

## Handover
| Attendee list + consents | Marketing ops | CRM import, consent flags | delete non-consented records by 24 Apr |
| Survey results, vendor scorecards | Next year's events lead | shared folder, 4 scorecards | — |

## Commercial close
| Venue  | $142,000 | +$8,200 attrition | —       | $150,200 | $5,000 damage deposit | 15 Nov |
| AV     | $46,000  | +$9,800 (2 COs)   | —       | $55,800  | $1,200 overtime disputed | 8 Nov |
| Catering (via venue) | $64,400 | +$5,600 gala no-shows | — | $70,000 | — | closed |
| Shuttles | $12,600 | −$2,200 fewer runs | — | $10,400 | — | closed |
Temporary services cancelled: event app licence (ends 31 Oct), storage unit (ends 30 Nov)

## Plan vs actual
| Agenda final | wk −8 | wk −5 | 3 wk | two keynotes confirmed late; no freeze gate |
| Room block release | wk −4 | wk −4 | 0 | — |
Cost: budget $310,000 (four vendors $265,000 + speakers/print/swag $45,000, on budget)
  → actual $331,400 → +$21,400 (+6.9%)
Variance account: attrition $8,200 + AV change orders $9,800 + gala no-shows $5,600
  − shuttle saving $2,200 = $21,400 ✓

## Root causes
1. AV COs: agenda changed after AV design was locked — no agenda-freeze gate in the plan.
2. Attrition: 600 room-nights sized from last year's 520 in-person registrations; this
   year added a remote option. Pickup 444 vs 480 (80% threshold) → 36 × $228 = $8,208.
3. Gala: guarantee set at 460 = RSVPs, ignoring a 9% historical no-show rate.

## Lessons
| 1 | AV COs $9,800 | no agenda freeze | freeze at wk −8; later changes priced to sponsor | Events lead | plan template gate |
| 2 | attrition $8,200 | block sized without remote shift | block = 75% of forecast; negotiate 70% attrition + release dates | Procurement | venue contract checklist |
| 3 | 40 unused covers | guarantee = RSVPs | guarantee = RSVPs × (1 − no-show rate) | Events lead | estimating record |
Keep doing: shuttle schedule built from flight-arrival data (saved $2,200).
Luck, not lesson: no weather disruption on the outdoor reception.

## Estimating data recorded
Pickup 74% of block; gala no-show 8.7%; AV design lead time 6 weeks.
## Outcome check: pipeline sourced from attendee meetings, 90 days (22 Jan), owner Sales ops
```

## Techniques Used

- **QA-08 Gate-Based Verification** — nothing closes without acceptance evidence from its Accountable.
- **RT-05 Evidence-Based Reasoning** — every variance tied to a document and an amount, summing to the total.
- **RT-09 Root Cause Explanation Pattern** — the top variances taken back to a controllable condition.
- **DS-40 Follow-Up Action Extraction** — snags, open accounts, and lessons each converted to an owned action.

## Related Prompts

- `domain-operations/project-delivery/ops_non_software_project_plan.md` — the plan, definition of done and RACI this closes against.
- `domain-operations/project-delivery/ops_schedule_recovery_plan.md` — the re-baseline whose decisions the variance account explains.
- `domain-decision-making/documentation/decisiondoc_after_action_report.md` — judging the decisions themselves, separate from the outcome.
