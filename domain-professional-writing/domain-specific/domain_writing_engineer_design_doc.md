---
title: "Engineer Design Doc — Implementation-Level Design, Real Alternatives, Success Criteria That Can Fail"
category: professional-writing/domain-specific
description: "Write a software design doc for the engineers who will build and operate one system: goals and non-goals, data model and contracts, a failure path for every dependency, alternatives stated as their advocates would state them, a phased rollout with a rollback for each phase, tests mapped to risks, and success criteria with baselines. Distinct from an RFC, which asks other teams for a decision and runs a comment period."
techniques:
  - CM-03
  - QA-24
  - DP-07
  - DS-02
  - QA-09
difficulty: intermediate
tags:
  - design-doc
  - software-engineer
  - technical-design
  - system-design-document
  - alternatives-considered
  - rollout-and-rollback
  - write-a-design-doc
updated: "2026-10-06"
related_prompts:
  - domain-professional-writing/domain-specific/domain_writing_engineer_rfc.md
  - domain-agentic-resources/skills/backend-development/architecture-decision-records/SKILL.md
  - domain-deep-analysis/deepthink_design.md
  - domain-professional-writing/business-writing/business_writing_prd_document.md
---

# Engineer Design Doc

**Objective:** Produce a design doc detailed enough that a teammate could start
implementation tickets from it and the on-call engineer could predict how the system
fails, with alternatives and success criteria that a reviewer can genuinely disagree with.

**When to Use:**
- Your team is about to build or substantially change a system it owns, and the work is
  large enough that a wrong data model or rollout would be expensive to undo.
- Reviewers are the engineers who will build, operate and be paged for it, plus the odd
  specialist (DBA, security).
- You have a direction and need the review to find the holes before code does.
- **Not this prompt if** the change requires other teams to change their systems,
  adopt a standard, or accept a new contract, and needs their sign-off within a comment
  period — that is an RFC: `domain-professional-writing/domain-specific/domain_writing_engineer_rfc.md`.
  A decision already made that needs a short permanent record is an ADR
  (`domain-agentic-resources/skills/backend-development/architecture-decision-records/SKILL.md`).
  Exploring what to build from scratch, through multi-perspective passes, is
  `domain-deep-analysis/deepthink_design.md`. Reviewing an existing API surface is
  `domain-software-engineering/api/api_rest_design_review.md`.

**Audience:** Engineers on the owning team, the tech lead, the on-call rotation, and
named specialist reviewers. They need the data model, the contracts, the failure
behaviour and the rollout steps, and they will reject anything vague.

## Inputs / Context

Paste source material inside named tags and refer to it by name, e.g.
`<current_system>…</current_system>`, `<schema>…</schema>`, `<metrics>…</metrics>`.

1. **Problem** — what is broken or limiting, why the current approach does not work,
   with evidence (latency, error rates, incident links, support volume) in `<metrics>`.
2. **Requirements and non-goals** — from the PRD or ticket; what this design explicitly
   does not address.
3. **Current system** `<current_system>` — components, data flow, existing schema
   `<schema>`, and the code path being changed.
4. **Proposed solution** — the author's design: components, data flow, data model, API or
   message contracts, key technologies.
5. **Alternatives considered** — the other approaches and why the author did not choose
   them.
6. **Migration / implementation plan** — phases, flags, backfills, data migrations.
7. **Testing strategy** — what the author intends to test and how.
8. **Success criteria** — how the team will know the problem is solved.
9. **Constraints** — SLOs, load (peak and average), budget, deadline, team skills, what
   the team is on call for.

Write only the technical detail the inputs contain. Where the design needs a decision
the author has not made, write `[OPEN: question]`; where it depends on a library,
service limit or vendor behaviour, write `[VERIFY: claim, source to check]` rather than
supplying one.

## Method

1. **Fix scope first (CM-03).** Goals as outcomes, non-goals as named exclusions, and
   constraints as numbers. If a requirement would force another team to change, mark it
   and recommend splitting that part into an RFC.
2. **Specify the design at implementation level.**
   - Components and who owns each; the data model as fields with types and constraints;
     contracts (endpoints, message schemas, delivery guarantees).
   - The main data flow end to end, then the behaviour under concurrency, retries and
     duplicates (idempotency, ordering, transactions).
3. **Predict failure modes (DP-07).** For every external dependency and every stateful
   step: what happens when it is slow, down, or returns garbage; what the user sees; what
   alerts; how it recovers. Add capacity (peak load, growth) and cost.
4. **Write the alternatives as their advocates would (QA-24).**
   - Include doing nothing (or extending the current system) and the strongest
     competing design.
   - For each: what it is better at than the proposal, and the specific constraint or
     requirement that rules it out. Add when to revisit, if anything would change the
     answer.
5. **Plan the rollout around reversibility (QA-09).**
   - Phases behind flags or traffic percentages; entry criteria for each phase.
   - A rollback step for each phase, including what happens to in-flight data. Name any
     one-way door (destructive migration, contract published to customers) and put it
     last.
6. **Map tests to risks.** Each failure mode from step 3 and each correctness property
   from step 2 gets the test or monitor that would catch it. Test types without a risk
   are dropped.
7. **Define success criteria (DS-02).** Metric, baseline, target, measurement window,
   data source. For each, check that it could fail; a criterion met by shipping is a
   milestone, not a success criterion.
8. **Verify before writing.** Every number traces to `<metrics>` or the constraints, or
   is marked `[measure]`; every component in the overview appears in a data flow; every
   failure mode has a test or alert; every alternative has a constraint-based rejection;
   no technical behaviour is stated that the author did not supply or mark `[VERIFY]`.

## Output Format

```
# Design: [system / change]
Status: Draft | In review | Approved   Author: [..]   Reviewers: [names, roles]
Related: [PRD / ticket / RFC if any]

## Context and problem
[current behaviour, evidence with source]

## Goals / Non-goals / Constraints

## Proposed design
### Overview            [components and ownership]
### Data model          [tables / schemas with types and constraints]
### Contracts           [APIs, messages, delivery guarantees]
### Data flow           [main path, then concurrency / retries / duplicates]
### Failure behaviour   | Dependency or step | Failure | Effect | Detection | Recovery |
### Capacity and cost

## Alternatives considered
| Alternative | Better than proposal at | Ruled out because | Revisit if |

## Rollout and migration
| Phase | Change | Entry criteria | Rollback |
One-way doors: [..]

## Testing strategy
| Risk / property | Test or monitor |

## Operability
[alerts with thresholds, dashboards, runbook entries]

## Success criteria
| Metric | Baseline | Target | Window | Source |

## Open questions
| Question | Owner | Must resolve before |
```

## Verification

- [ ] Non-goals are listed and nothing in the design contradicts them.
- [ ] Data model fields have types and constraints; every contract states its delivery
      or consistency guarantee.
- [ ] Each external dependency has a row in Failure behaviour.
- [ ] Each alternative states what it does better than the proposal and the constraint
      that rules it out.
- [ ] Every rollout phase has a rollback that accounts for in-flight data.
- [ ] Every row in Failure behaviour maps to a test or alert.
- [ ] Every success criterion has a baseline and could be missed.
- [ ] No library, service-limit or vendor claim appears without `[VERIFY]` unless the
      author supplied it.

## False-Positive Prevention

1. **Straw-man alternatives.** "Do nothing" and "rewrite everything" as the only
   alternatives make any proposal look reasonable. Include the competing design a
   strong engineer on the team would actually argue for, describe it so its advocate
   would agree with the description, and reject it on a stated constraint.
2. **Success criteria that cannot fail.** "Improved reliability", "migration complete",
   "webhooks moved to the new service" are all true the day the code ships. A criterion
   needs a baseline, a target and a window over which it could be missed.
3. **A happy-path data flow.** The diagram shows a request succeeding. Reviewers need
   the duplicate message, the crash between commit and publish, the slow downstream —
   that is where designs are wrong.
4. **Invented technical detail.** The model fills gaps with plausible throughput
   figures, library features or configuration values the author never gave. Each gap is
   an `[OPEN]` for the team or a `[VERIFY]` against documentation, not a sentence.
5. **A rollback that ignores in-flight data.** "Flip the flag back" is not a rollback if
   rows written by the new path are orphaned or re-sent by the old one. State what
   happens to work already in progress.
6. **Testing strategy as a list of test types.** "Unit, integration and end-to-end
   tests" says nothing about which risk each test retires. Map each test to a risk.
7. **An RFC hidden inside the design.** A design that quietly changes another team's
   API, schema or on-call burden needs their decision, not their review comments. Split
   that part out.

## Example Output

```
# Design: Transactional outbox for payment webhooks
Status: In review   Author: M. Osei (Payments API)
Reviewers: Payments API engineers; R. Lind (on-call lead); J. Park (DBA)
Related: PAY-2291 (missing webhooks), PRD "Reliable merchant notifications"

## Context and problem
POST /v1/payments sends the merchant webhook inline, inside the request, with a 10 s
timeout. Over the last 14 days p99 latency for that endpoint was 2.4 s, driven by slow
merchant endpoints (<metrics>: APM). In August 0.8% of 1.9M webhook events had no
delivery record — 15,200 events — mostly sends lost when a pod restarted mid-request
(<metrics>: reconciliation script). Support logged 230 "webhook missing" tickets that
month.

## Goals / Non-goals / Constraints
Goals: payment latency independent of merchant endpoints; no event lost without a record.
Non-goals: changing the webhook payload; exactly-once delivery; a merchant redelivery UI.
Constraints: peak 120 events/s; existing Postgres primary; no new infrastructure the
team is not on call for; ship by 15 Dec.

## Proposed design
### Overview
Payments API writes an outbox row in the same transaction as the payment state change.
A delivery worker pool (owned by Payments API, same deploy) claims rows and sends them.
### Data model
webhook_outbox(id bigserial PK, event_id uuid UNIQUE NOT NULL, merchant_id bigint NOT
NULL, payload jsonb NOT NULL, status text CHECK IN ('pending','delivered','dead'),
attempts int NOT NULL DEFAULT 0, next_attempt_at timestamptz NOT NULL, created_at
timestamptz NOT NULL DEFAULT now()); index on (status, next_attempt_at).
### Contracts
At-least-once delivery; every attempt carries the same event_id so merchants can
deduplicate. [VERIFY: public webhook docs already state at-least-once; if not, a docs
change is in scope for Phase 3.] Retries at 1 m, 5 m, 30 m, 2 h, 6 h, 24 h; then 'dead'.
### Data flow
1 Payment transaction commits payment row + outbox row together, or neither.
2 Worker claims a batch of pending rows due now, skipping rows locked by other workers.
3 Worker POSTs with a 5 s timeout; 2xx → 'delivered'; otherwise attempts+1 and
  next_attempt_at from the schedule.
Duplicates: a worker crash after the POST but before the status update re-sends the
event; event_id makes this safe for merchants who deduplicate.
### Failure behaviour
| Dependency/step     | Failure            | Effect                     | Detection               | Recovery |
| Merchant endpoint   | Slow / down        | Retries; that merchant only | Per-merchant failure rate | Schedule; 'dead' after 24 h |
| One slow merchant   | Holds workers      | Other merchants delayed     | Oldest-pending age       | Cap 10 in-flight per merchant |
| Worker pod          | Crash mid-batch    | Locks released; resend      | Pod restarts             | Next claim picks rows up |
| Postgres primary    | Failover           | Claims pause                | DB alerts                | Resume; rows were committed |
### Capacity and cost
120 events/s peak; 8 workers to start; per-worker throughput [measure in load test].
~1.9M rows/month; delivered rows deleted after 30 days [OPEN: retention, see Q1].

## Alternatives considered
| Alternative | Better than proposal at | Ruled out because | Revisit if |
| A Keep inline; 2 s timeout + async thread | Smallest change; no schema | In-memory sends still lost on restart — the 0.8% stays | — |
| B Publish to a queue from the handler after commit | No polling; native retries | Commit-then-publish loses the event when publish fails; fixing it needs an outbox anyway | — |
| C Change data capture on the payments table | No extra writes, no polling query; strongest option | Needs a CDC connector nobody on the team operates or is on call for; payload would mirror internal columns | Platform offers managed CDC |
| D Do nothing | Zero cost | 15,200 lost events and 230 tickets a month | — |

## Rollout and migration
| Phase | Change | Entry criteria | Rollback |
| 0 | Create webhook_outbox (additive) | DBA review | Drop table |
| 1 | Write outbox rows; workers dry-run and log; inline sends continue | Phase 0 deployed | Stop writes; table ignored |
| 2 | Flag on for 5% of merchants: inline off, workers send | Dry-run matches inline sends ≥ 99.99% over 7 days | Flag off for new events; workers keep draining existing rows so none are lost or doubled |
| 3 | 100% of merchants | Success criteria 1–3 holding at 5% for 7 days | As Phase 2 |
| 4 | Delete inline send code | Criteria 1–2 holding for 30 days at 100% | Revert commit |
One-way doors: none. Phase 4 is last because it removes the fast fallback.

## Testing strategy
| Risk / property | Test or monitor |
| Payment and outbox row commit together | Integration test: forced rollback leaves neither row |
| Worker crash loses an event | Kill worker mid-batch; assert every row delivered or pending |
| Retries change event_id | Contract test: all attempts carry the same event_id |
| Slow merchant starves others | Load test: one merchant at 10 s latency; others' p95 to first attempt ≤ 30 s |
| Poll query degrades at peak | Load test at 120 events/s; query p95 [measure] |

## Operability
Page: oldest pending row > 5 min. Ticket: > 100 rows to 'dead' in an hour.
Dashboard: pending count, attempts histogram, dead rows by merchant.
Runbook: re-queue dead rows for one merchant after their endpoint recovers.

## Success criteria
| Metric | Baseline | Target | Window | Source |
| 1 p99 POST /v1/payments latency | 2.4 s | ≤ 400 ms | 14 days at 100% | APM |
| 2 Events with no delivery record after 1 h | 0.8% | 0 | 30 consecutive days | Reconciliation job |
| 3 p95 commit → first attempt | n/a (inline) | ≤ 30 s | 14 days | Outbox timestamps |

## Open questions
| Question | Owner | Must resolve before |
| Q1 Retain delivered rows 30 or 90 days? (data team wants 90) | J. Park | Phase 3 |
| Q2 Does an event that goes 'dead' notify the merchant by email? | Product (A. Ruiz) | Phase 3 |
```

## Techniques Used

- **CM-03 Scope Definition** — goals, named non-goals and numeric constraints fixed before
  the design.
- **QA-24 Dismissed-Candidates Coverage Table** — each alternative with what it does better,
  the constraint that rules it out, and a revisit condition.
- **DP-07 Failure Mode Prediction** — a failure row for every dependency and stateful step.
- **DS-02 Metric Specification** — success criteria with baseline, target, window and
  source.
- **QA-09 Reversibility Assessment** — per-phase rollback including in-flight data, and
  one-way doors placed last.

## Related Prompts

- `domain-professional-writing/domain-specific/domain_writing_engineer_rfc.md` — when the
  change needs other teams' decision and sign-off.
- `domain-agentic-resources/skills/backend-development/architecture-decision-records/SKILL.md`
  — recording the approved design's key decision.
- `domain-deep-analysis/deepthink_design.md` — exploring the design space before there is
  a proposal to write up.
- `domain-professional-writing/business-writing/business_writing_prd_document.md` — the
  product requirements this design implements.
