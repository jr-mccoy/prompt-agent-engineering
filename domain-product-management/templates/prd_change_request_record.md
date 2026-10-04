---
title: "PRD Change Request Record — A Mid-Build Scope Change Stated as a Delta, Priced, Decided by the Right Person, and Written Back Into the Spec"
category: product-management/templates
description: "Handle a request to add, change or remove a requirement after the PRD is agreed: state the change as a delta against the spec version and its acceptance criteria, estimate its effect on effort, date, outcome metric, other teams and reversibility, lay out accept-and-move, accept-and-trade, defer and reject options, route the decision by a pre-agreed authority rule, and record a versioned PRD amendment with a notify list and a cumulative-churn check that triggers a re-plan."
techniques:
  - DD-10
  - RT-07
  - QA-09
  - CM-09
difficulty: intermediate
tags:
  - scope-change
  - change-request
  - prd-amendment
  - scope-creep
  - trade-off
  - change-control
  - someone-wants-to-add-a-feature
  - requirements-changed-mid-sprint
  - stop-scope-creep
updated: "2026-10-03"
related_prompts:
  - domain-product-management/templates/prd_one_pager_with_acceptance_criteria.md
  - domain-decision-making/documentation/decisiondoc_log_entry.md
  - domain-product-management/prompts/product_delivery_sprint_planner.md
---

# PRD Change Request Record

**Objective:** When the spec is agreed and someone wants it changed, produce one
record that says exactly what would change, what it costs in days and in the outcome,
who has the authority to say yes, what was decided, and how the PRD now reads — so
scope moves on purpose rather than by accumulation.

**When to Use:**
- A stakeholder asks for an addition or change after the PRD or one-pager is agreed and
  build has started.
- A non-goal is being challenged ("just add round-robin while you're in there").
- Several small "quick asks" have landed in one sprint and nobody has added them up.
- **Not this prompt if** you are logging a decision of any kind for institutional
  memory — use `domain-decision-making/documentation/decisiondoc_log_entry.md`, which is
  the general append-only log (this record is a change-control instrument against a
  versioned spec, with impact and authority). If the change is to a **client
  engagement's** contracted scope, use the client-services pipeline
  (`client-services-studio/`). If the whole plan needs rebuilding, re-plan with
  `domain-product-management/prompts/product_delivery_sprint_planner.md`; if the
  question is whether to remove a shipped feature, use
  `domain-product-management/prompts/product_feature_sunset_decision.md`.

## Inputs / Context

1. **The agreed spec**, with its version and acceptance-criteria IDs.
2. **The request**: who asked, the wording they used, and the reason given.
3. **Evidence behind it**: a customer, a deal, a defect, a regulation, a preference.
4. **Current delivery state**: remaining estimate, capacity, buffer, work already built.
5. **The authority rule**, if one exists: who may approve which size of change.
6. **Changes already approved** since the spec was agreed (for the churn check).

## Method

1. **State it as a delta.** Spec version, section, and acceptance criteria added,
   changed, or removed. Classify: *addition*, *modification*, *removal*, or
   *clarification*. A clarification changes no criterion — check that it truly does not.
2. **Separate new information from preference.** A defect, a regulation, or a
   measured customer need is new information; "it would be nice" is preference. Both can
   be accepted, but they are argued differently.
3. **Impact (RT-07).** Effort delta with its source; date impact against remaining
   capacity and buffer; acceptance criteria and tests affected; other teams touched;
   effect on the outcome metric (does it move it, or only please the requester?); work
   already built that is thrown away (noted, not decisive).
4. **Reversibility (QA-09).** Can it ship behind the flag and be removed? Does it create
   data, promises, or contracts that persist? Irreversible changes go to the full PRD.
5. **Options.** Always at least: *accept and move the date*; *accept and trade out
   scope of equal or larger size* (name the item); *defer to a follow-up* (with a
   target); *reject* (with the reason). Add *clarify only* where it applies.
6. **Route by authority (CM-09).** Apply the rule — e.g. PM decides changes within the
   buffer that move no date; the sponsor decides any date move or a trade that touches a
   customer commitment; legal or compliance are consulted on anything they own. No rule?
   Propose one with this record.
7. **Record the decision and amend the spec (DD-10).** Version bump, sections changed,
   one-line changelog, tickets updated, and who is told (engineering, design, QA,
   support, sales if customer-facing). The requester hears the decision and the reason.
8. **Cumulative churn check.** Sum approved change effort since the baseline. If it
   exceeds a threshold (e.g. 20% of the original estimate, or three changes in one
   sprint), stop processing change requests one at a time and re-plan.

## Output Format

```
# CR-[nnn] — [short name]       Spec: [name] v[x.y]   Raised by: [..]   Date: [..]

## Change (delta)
Type: [addition | modification | removal | clarification]
Sections / ACs: [+ADDED] [~CHANGED] [−REMOVED]
Reason: [..]   Basis: [new information: ... | preference]

## Impact
| Dimension | Effect | Source |
| Effort | +[n] team-days | [estimate by] |
| Date | [none | +n days] vs buffer [..] |
| Acceptance criteria / tests | [...] |
| Other teams | [...] |
| Outcome metric | [moves it | neutral | distracts] |
| Work discarded | [...] |
Reversible: [yes — how | no — why]

## Options
| Option | Date | Scope effect | Risk | Who it serves |

## Authority
Rule: [..] → decider: [..]   Consulted: [..]

## Decision: [option] — [decider], [date]. Reason: [..]

## Spec amendment
v[x.y] → v[x.y+1] · sections: [...] · changelog: "[...]"
Notified: [...]   Tickets: [...]

## Churn since baseline
Approved CRs: [n] · added effort [n] of [baseline] ([%]) · threshold [..] → [OK | re-plan]
```

## Verification

- [ ] The change is stated against a spec version and named acceptance criteria.
- [ ] Basis is labelled new information or preference.
- [ ] Effort, date, metric, other-team, and discarded-work effects are each stated.
- [ ] Reversibility is assessed; irreversible changes are routed to the full PRD.
- [ ] At least four options, including a named trade and a defer target.
- [ ] The decider follows the authority rule (or one is proposed).
- [ ] The spec version, changelog, tickets, and notify list are updated.
- [ ] Cumulative churn is computed against a stated threshold.

## False-Positive Prevention

1. **"It's just small."** Small changes are approved one at a time and add up to a
   missed date. The churn check exists to see the sum.
2. **Trades that are not equal.** Dropping a 1-day item to absorb a 5-day one does not
   balance. Compare estimates from the same estimator.
3. **The loudest requester decides.** A large deal does not change who has authority;
   it changes the evidence the decider weighs.
4. **Clarifications that are additions.** "Clarify that reassign also handles closed
   tickets" may add work and criteria. Check the acceptance criteria, not the label.
5. **Sunk cost steering.** Work already built is a fact to report, not a reason to keep
   or kill a change.
6. **Decided but not written down.** If the PRD still reads as before, the team builds
   the old version. Amend the spec, bump the version, notify.

## Example Output

```
# CR-007 — Round-robin reassign        Spec: Bulk reassign tickets v1.0   Raised by: Sales (Lee)   Date: 9 Oct

## Change (delta)
Type: addition — challenges a stated non-goal
Sections / ACs: +US-3 "reassign selected tickets across 2–5 agents evenly";
  +AC3.1–3.4 (even split, skip agents at capacity, remainder rule, audit log);
  −Non-goal "round-robin across several agents"
Reason: prospect (Northwind, 240 seats) lists it as a must-have for contract signature
  on 20 Nov. Basis: new information (named deal, written requirement in RFP §4.2)

## Impact
| Effort | +5 team-days | eng lead estimate, same estimator as v1.0 (8 days) |
| Date | Sprint 42 has 2 days buffer → +3 days over; Sprint 42 date slips 1 sprint if accepted in-sprint |
| ACs / tests | 4 new ACs; AC1.3 summary text changes for multi-agent case |
| Other teams | none (no routing-engine change) |
| Outcome metric | neutral for leads' reassign time; serves a sales outcome |
| Work discarded | none |
Reversible: yes — separate option behind the same flag

## Options
| A Accept, move v1 to Sprint 43     | +2 wks | all of v1 later | 3 pilot teams wait | Northwind |
| B Accept, trade out AC2.1 digest   | none   | agents get 37 alerts | guardrail risk | Northwind only |
| C Defer: v1 in S42, round-robin S43| none   | US-3 ships 1 Nov | low | both |
| D Reject                           | none   | — | deal risk | pilot teams |

## Authority
Rule: PM decides when no committed date moves; sponsor (VP Product) if a date moves.
→ Option C is within PM authority. Consulted: Sales (Lee), Support ops.

## Decision: C — Dana (PM), 10 Oct. Reason: meets the 20 Nov deal date without delaying
the pilot; option B breaks the agent-notification behaviour v1 promised.

## Spec amendment
v1.0 → v1.1 · sections: Non-goals, Stories (US-3 added as "Sprint 43 follow-up")
changelog: "Round-robin moved from non-goal to S43 follow-up (CR-007)"
Notified: eng, design, QA, support ops, Sales (Lee)   Tickets: TKT-881–884 created in S43

## Churn since baseline
Approved CRs: 2 (CR-006 clarification 0 d; CR-007 deferred, 0 d in S42) · added effort
in v1 scope 0 of 8 days (0%) · threshold 20% → OK
```

## Techniques Used

- **DD-10 Change Log Iteration** — version bump, changelog line, and cumulative churn per change.
- **RT-07 Cascade Effect Analysis** — effort to date, criteria, tests, other teams, and the metric.
- **QA-09 Reversibility Assessment** — whether the change can be removed behind the flag.
- **CM-09 Authority Boundary Specification** — who may approve which size of change.

## Related Prompts

- `domain-product-management/templates/prd_one_pager_with_acceptance_criteria.md` — the agreed spec this record amends.
- `domain-decision-making/documentation/decisiondoc_log_entry.md` — the general decision log, for decisions that are not spec changes.
- `domain-product-management/prompts/product_delivery_sprint_planner.md` — re-planning when churn passes the threshold.
