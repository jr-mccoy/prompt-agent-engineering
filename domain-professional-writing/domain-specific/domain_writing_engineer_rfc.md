---
title: "Engineer RFC — Cross-Team Decision Request, Comment Period, Sign-Off, and Recorded Dissent"
category: professional-writing/domain-specific
description: "Write a principal or senior engineer's RFC that asks several teams for one technical decision: the decision in a sentence, a non-engineer summary with cost and what slips, what each affected team must do, real alternatives, known objections with responses, open questions split by whether they block the decision, and a comment period with named approvers and a dissent record. Distinct from a design doc, which details how one team builds a system it owns."
techniques:
  - CM-09
  - NE-23
  - NE-14
  - QA-09
  - NE-27
difficulty: advanced
tags:
  - rfc
  - request-for-comments
  - principal-engineer
  - cross-team-decision
  - technical-proposal
  - sign-off
  - disagree-and-commit
updated: "2026-10-06"
related_prompts:
  - domain-professional-writing/domain-specific/domain_writing_engineer_design_doc.md
  - domain-agentic-resources/skills/backend-development/architecture-decision-records/SKILL.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-professional-writing/domain-specific/domain_writing_cto_strategy_memo.md
---

# Engineer RFC

**Objective:** Produce an RFC that names one technical decision, shows every affected
team what it costs them, runs a defined comment period, and ends in a recorded outcome
in which approvals were given explicitly and dissent was kept.

**When to Use:**
- A technical change crosses team boundaries: a shared contract, a data-ownership
  boundary, a platform standard, a deprecation others must migrate off.
- You need named people to approve, not only engineers to comment.
- Product leadership needs to understand the cost and what slips without reading the
  technical sections.
- The decision will be argued about later, and a record of who agreed to what will
  matter.
- **Not this prompt if** your team owns the whole change and needs its implementation
  reviewed by the engineers who will build and operate it — that is a design doc:
  `domain-professional-writing/domain-specific/domain_writing_engineer_design_doc.md`
  (each affected team typically writes one after the RFC is accepted). To record a
  decision already made, use the ADR skill at
  `domain-agentic-resources/skills/backend-development/architecture-decision-records/SKILL.md`.
  A business or product choice with no technical proposal is
  `domain-decision-making/documentation/decisiondoc_options_memo.md`.

**Audience:** Engineers and tech leads on every affected team, who will challenge the
proposal and must estimate their own work; the approvers who sign; product leadership,
who read the summary for cost, risk and roadmap impact.

## Inputs / Context

Paste source material inside named tags and refer to it by name, e.g.
`<current_system>…</current_system>`, `<incidents>…</incidents>`,
`<rfc_process>…</rfc_process>`, `<team_estimates>…</team_estimates>`.

1. **Problem statement** — what is broken or limiting now, with evidence.
2. **Current system** `<current_system>` — how it works today and why that is the problem.
3. **Proposed solution** — the technical approach, at the level of contracts,
   boundaries and obligations.
4. **Trade-offs and alternatives** — what is gained, what is given up, the other
   approaches including any competing proposal by name.
5. **Implementation plan** — migration approach, timeline, risks.
6. **Affected teams** — each team, what it would have to do, and its effort estimate in
   `<team_estimates>` (or a note that the estimate is the author's, not the team's).
7. **Decision process** `<rfc_process>` — your organisation's RFC rules: comment-period
   length, who decides, what counts as a blocking objection, escalation path. If none
   exist, say so and the RFC will propose one for this decision only.
8. **Known objections** — raised in earlier conversations, with who raised them.

Represent the author's thinking; do not add technical detail not present in the inputs.
Gaps go in Open Questions; unverified technical claims are marked `[VERIFY: …]`.

## Method

1. **State the decision and its reversibility (QA-09).**
   - One sentence a reader could answer yes or no to.
   - Classify: reversible cheaply, reversible at cost, or one-way (published contracts,
     data deletion, customer-visible changes). The class sets how much evidence and how
     long a comment period the RFC needs; say which part is one-way.
2. **Map authority (CM-09).**
   - Decider (one person or body), approvers whose explicit sign-off is required (each
     team whose system, roadmap or on-call load changes), consulted, informed.
   - Use `<rfc_process>` for the rules. Where it is silent, propose the rule and label it
     as proposed.
3. **Write the summary for non-engineers (NE-14).** Decision, why now, total cost in
   engineer-weeks with who bears it, what slips, the deadline, and the risk of the
   change — no acronyms the product reader would need to look up.
4. **Price inaction (NE-27).** What continues to happen if the RFC is rejected —
   incidents, blocked work, hours — from the evidence, not adjectives.
5. **Describe the proposal at decision level.** Contracts, boundaries, compatibility
   guarantees, deprecation dates and exceptions. Defer implementation detail to the
   design docs each team will write.
6. **Tabulate obligations by team.** Each affected team: what it must do, by when, its
   own estimate (or the author's, flagged), and its approver.
7. **Pre-empt objections (NE-23).** For each known objection: who raised it, the
   strongest form of it, the response, and whether it is resolved, partly resolved, or
   still open. Unresolved ones stay visible.
8. **Split open questions.** Those that must be answered before the decision (if any
   are open, the RFC is not ready for approval) and those that can wait for
   implementation, each with an owner.
9. **Set the decision process.** Comment window dates, where comments go, how a
   blocking objection is raised and resolved, how dissent is recorded (name, reason,
   whether they commit), and what the RFC's possible end states are.
10. **Verify before circulating.** Team estimates sum to the total in the summary;
    every team in the obligations table has a sign-off row; dates in the summary, the
    process and the timeline agree; no technical claim exceeds the inputs.

## Output Format

```
# RFC-[n]: [title]
Author: [..]   Status: Draft | In review | Accepted | Rejected | Withdrawn
Comment period: [open] – [close]   Decider: [..]   Approvers: [..]

## Summary for non-engineers
[decision, why now, cost and who bears it, what slips, deadline, main risk]

## Decision requested
[one sentence] — Reversibility: [class; which part is one-way]

## Problem and current system
[evidence]   Cost of inaction: [..]

## Proposal
[contracts, boundaries, guarantees, deprecation dates, exceptions]

## What each team must do
| Team | Change | By | Estimate (source) | Approver |

## Alternatives considered
| Alternative | Strength | Why not |

## Known objections
| Raised by | Objection (strongest form) | Response | Status |

## Open questions
| Question | Owner | Blocks decision? |

## Timeline and success metrics

## Decision process
[window, where comments go, blocking objections, escalation, dissent rule]
| Approver | Team | Position | Conditions | Date |

## Decision record   (completed at close)
[outcome, conditions, dissent recorded, ADR link]
```

## Verification

- [ ] The decision is one sentence that can be accepted or rejected.
- [ ] The reversibility class is stated and the one-way part named.
- [ ] Every team in "What each team must do" has an approver row in the sign-off table.
- [ ] Each estimate says whether the team or the author produced it; the summary total
      equals their sum.
- [ ] No decision-blocking open question remains if the status is Accepted.
- [ ] Each known objection names who raised it and has a status.
- [ ] The summary can be read by a product leader without the rest of the document.
- [ ] Dissent at close is recorded by name with reason and commit/no-commit.

## False-Positive Prevention

1. **A design doc wearing an RFC header.** If nothing in the document can be accepted
   or rejected, and no one is named to approve, it is informational. An RFC exists to
   get a decision; name it in one sentence or change the document type.
2. **Silence counted as sign-off.** "No objections received by the close date" from a
   team that was never tagged is not approval. Teams whose systems or roadmaps change
   sign explicitly; absence is chased, not assumed.
3. **Work assigned to other teams without their estimate.** "Consumers migrate to the
   new API" with the author's guess at their effort understates cost and invites the
   objection later. Use each team's number or flag it as the author's estimate pending
   theirs.
4. **The decision itself listed as an open question.** If "which consistency model" or
   "who owns the data" is still open, the RFC is not ready for approval. Separate
   decision-blocking questions from implementation-time ones.
5. **Dissent rewritten as consensus.** The closing version marks every objection
   "resolved" because the author answered it. Record who still disagrees, why, and
   whether they commit; that record is what the next engineer to revisit this needs.
6. **A summary only engineers can read.** "Revoke direct schema grants in favour of a
   versioned read API" tells a product leader nothing. Say what it costs, what slips,
   and what risk goes away.
7. **Benchmarks and versions the author did not provide.** RFCs attract invented
   specifics — latency numbers, library versions, vendor limits — that make the
   proposal look finished. Keep to the author's inputs and list the gaps.

## Example Output

```
# RFC-042: Billing data is read through the Billing Read API, not the billing schema
Author: S. Adeyemi (Principal Engineer, Billing)   Status: Accepted
Comment period: Tue 6 Oct – Tue 20 Oct 2026 (10 business days, per <rfc_process>)
Decider: Architecture Council (chair P. Raman)
Approvers: tech leads of Billing, Reporting, Notifications, Collections, Support Tools

## Summary for non-engineers
Five teams read the billing database directly, so any billing change can break their
products; it did twice this year. We propose that they read billing data through an
interface Billing maintains, and that direct access ends on 31 Mar 2027. Cost: 20
engineer-weeks across five teams in Q4–Q1. What slips: Reporting's scheduled-exports
feature moves from Q1 to Q2. Risk removed: billing changes stop causing outages
elsewhere, and three blocked billing changes can ship.

## Decision requested
Adopt the Billing Read API v1 as the only read path to billing data for the five
consuming teams, and revoke direct read access on 31 Mar 2027.
Reversibility: grant revocation is cheaply reversible; the API v1 contract is reversible
only at cost once four teams depend on it — the contract shape is the one-way part.

## Problem and current system
Reporting, Notifications, Collections and Support Tools query billing tables directly
(<current_system>). Billing schema changes in March and June caused Sev2 incidents in
Reporting and Notifications (<incidents>). Three billing changes (multi-currency
invoices, credit notes, tax breakdown) are blocked on coordinating five teams.
Cost of inaction: each billing schema change needs five-team coordination; three
roadmap items stay blocked; incident risk continues with every billing release.

## Proposal
- Billing publishes Read API v1: invoices, line items, payments, credit balances;
  versioned, with 12 months' support for any version after its successor ships.
- Bulk export endpoint for Reporting's batch jobs.
- Exception: the data platform's replica-based analytics extract continues, owned by
  Data Platform, not covered by this RFC.
- Direct read grants for the four consuming teams revoked 31 Mar 2027.
- Implementation detail goes in each team's design doc after acceptance.

## What each team must do
| Team          | Change                                   | By      | Estimate (source)      | Approver   |
| Billing       | Build and operate Read API v1 + bulk export | 15 Jan | 10 eng-wk (team)       | S. Adeyemi |
| Reporting     | Move batch jobs to bulk export           | 15 Mar  | 4 eng-wk (team)        | L. Chen    |
| Notifications | Move invoice lookups to API              | 28 Feb  | 2 eng-wk (team)        | D. Moreau  |
| Collections   | Move dunning queries to API              | 15 Mar  | 3 eng-wk (author's; team confirmed 13 Oct) | K. Iyer |
| Support Tools | Move account view to API                 | 28 Feb  | 1 eng-wk (team)        | F. Haddad  |
Check: 10 + 4 + 2 + 3 + 1 = 20 eng-wk

## Alternatives considered
| Alternative | Strength | Why not |
| Status quo + 30-day schema-change notice | No build cost | Notice existed in June; the Sev2 happened anyway |
| Database views as the contract | Cheapest for consumers; SQL unchanged | Billing still cannot see or limit consumer query load; views tie consumers to the database engine |
| Events only; consumers build their own copies | Fully decoupled | Support Tools needs a read immediately after a write; four teams would each build a projection |

## Known objections
| Raised by | Objection (strongest form) | Response | Status |
| L. Chen (Reporting) | Row-by-row API reads would turn a 20-minute nightly job into hours | Bulk export endpoint added to v1 for this case | Resolved |
| L. Chen (Reporting) | 15 Mar is too early given Q1 commitments | Scheduled exports moves to Q2 to make room | Partly — see dissent |
| K. Iyer (Collections) | Collections also needs to write payment plans | Writes are out of scope; separate RFC if pursued | Open, not blocking |

## Open questions
| Question | Owner | Blocks decision? |
| Collections' own estimate | K. Iyer | No — adjusts total only; closed 13 Oct (3 eng-wk) |
| API rate limits per consumer | S. Adeyemi | No — Billing design doc |
| Writes for Collections | K. Iyer | No — out of scope |

## Timeline and success metrics
API v1 15 Jan; consumers migrated by 15 Mar; grants revoked 31 Mar 2027.
Metrics: zero Sev1/Sev2 in consuming teams caused by billing changes in the two
quarters after revocation (baseline: 2 in 2026); three blocked billing changes shipped
by end of Q2 2027.

## Decision process
Comments in the RFC doc; blocking objections must cite a requirement the proposal
breaks and are raised in #arch-council by 20 Oct; unresolved blocking objections go to
the Council. Dissent is recorded by name and reason; dissenters state whether they
commit. Approvers sign below; a missing row is chased, not assumed.
| Approver   | Team          | Position             | Conditions                         | Date   |
| S. Adeyemi | Billing       | Approve              | —                                  | 14 Oct |
| L. Chen    | Reporting     | Disagree and commit  | Bulk export live before 15 Feb     | 19 Oct |
| D. Moreau  | Notifications | Approve              | —                                  | 15 Oct |
| K. Iyer    | Collections   | Approve with condition | Team estimate replaces author's  | 16 Oct |
| F. Haddad  | Support Tools | Approve              | —                                  | 13 Oct |

## Decision record (closed 20 Oct 2026)
Accepted by the Architecture Council with two conditions: bulk export live before
15 Feb; Collections' estimate replaces the author's (received 13 Oct: 3 eng-wk,
unchanged). Dissent: L. Chen disagrees with the 15 Mar migration date because of
Reporting's Q1 load; commits. Recorded as ADR-0057.
```

## Techniques Used

- **CM-09 Authority Boundary Specification** — decider, required approvers, consulted and
  informed, with a sign-off row per affected team.
- **NE-23 Objection Pre-emption** — known objections in their strongest form, with response
  and status kept visible.
- **NE-14 Multi-Audience Documentation Targeting** — a summary product leadership can act
  on above technical sections engineers can challenge.
- **QA-09 Reversibility Assessment** — the decision classed by reversibility, with the
  one-way part named.
- **NE-27 Cost of Inaction Framing** — what continues if the RFC is rejected, from the
  incident and blocked-work evidence.

## Related Prompts

- `domain-professional-writing/domain-specific/domain_writing_engineer_design_doc.md` — the
  per-team implementation design once the RFC is accepted.
- `domain-agentic-resources/skills/backend-development/architecture-decision-records/SKILL.md`
  — the short permanent record the decision record points to.
- `domain-decision-making/documentation/decisiondoc_options_memo.md` — non-technical
  multi-option decisions.
- `domain-professional-writing/domain-specific/domain_writing_cto_strategy_memo.md` — the
  strategy an RFC often implements.
