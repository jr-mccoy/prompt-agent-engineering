---
title: "Customer QBR Prep — Outcomes Against Their Goals, Sourced Value, and the Decisions You Need from the Room"
category: sales-customer/customer-success
description: "Prepare a customer-facing quarterly business review for one account: restate the customer's own success criteria, report progress against each with provenance-tagged numbers, surface what is not working before they do, and design the agenda around two or three decisions the executives in the room must make — distinct from an account health assessment, which is the internal diagnosis this meeting draws on, and from an internal company QBR deck."
techniques:
  - RP-02
  - DS-02
  - RT-05
  - NE-23
difficulty: intermediate
tags:
  - customer-success
  - qbr
  - executive-business-review
  - account-management
  - value-realization
  - b2b
updated: "2026-09-24"
related_prompts:
  - domain-sales-customer/customer-success/cs_renewal_risk_and_save_plan.md
  - domain-business-strategy/go-to-market/workflow_cs_account_health.md
  - domain-business-strategy/go-to-market/workflow_customer_success_onboarding_plan.md
---

# Customer QBR Prep

**Objective:** Produce the brief and agenda for a business review that the
customer's executives would choose to attend — because it reports on *their*
goals, is honest about what is off track, and ends with decisions rather than a
roadmap tour.

**When to Use:**
- A QBR or EBR is scheduled and last quarter's deck is the only template.
- The customer's sponsor has stopped attending, or sends a delegate.
- Renewal is 2–3 quarters out and you need the value story on record early.
- Adoption is uneven and you need the customer to make a resourcing decision.
- **Not this prompt if** you need the internal diagnosis of the account's risk —
  use `domain-business-strategy/go-to-market/workflow_cs_account_health.md` first
  and feed its output in here. If renewal is inside 90 days and at risk, use
  `cs_renewal_risk_and_save_plan.md`. For your own company's internal quarterly
  review deck, see `domain-presentations/powerpoint_quarterly_business_review.md`.

## Inputs / Context

1. **The customer's success criteria** as agreed at onboarding or last QBR — in
   their words, with who set them. If none exist, that is the first finding.
2. **Usage and outcome data** for the period, each figure tagged by source.
3. **Support and incident history:** open tickets, escalations, SLA misses.
4. **Attendees on their side** and what each is measured on.
5. **Commitments made last QBR,** by both sides, and their status.
6. **Internal account view:** health score, renewal date, expansion hypotheses.
   Used to plan; most of it is not presented.

## Method

1. **Restate their goals first (RP-02).** The QBR opens on the customer's
   criteria, not your product. If goals were never set, the agenda's first item
   is agreeing them, and the rest of the brief is shorter.

2. **Define each metric before reporting it (DS-02).** For every goal: the
   measure, the baseline, the target, this period's value, and the source. A
   metric without a baseline is activity, not outcome.

3. **Tag provenance on every number (RT-05).** `[their-data]` the customer's
   system or report; `[our-data]` product telemetry; `[estimate]` modelled value
   such as hours saved. Estimated value is shown as an estimate with its
   assumptions, never as a result.

4. **Lead with what is off track.** One slide or section: what is behind, why,
   and what each side will do. The customer already knows; saying it first buys
   the credibility the rest of the meeting needs.

5. **Close the loop on last quarter.** Every commitment from the last review:
   done, late, or dropped — both sides.

6. **Pre-empt the executives' objections (NE-23).** For each senior attendee,
   the strongest question they are likely to ask ("why are only 40% of depots
   using it?") and the honest answer with evidence.

7. **Design the decisions.** Two or three asks the room must decide: resourcing an
   adoption push, confirming next quarter's goals, sponsoring a new use case, a
   reference. Each has a proposed answer and what happens if it is deferred.

8. **Split presented from internal.** Health score, renewal risk, expansion
   targets and discount thinking stay in the internal brief.

## Output Format

```
# QBR prep — [Customer] — [quarter] — meeting [date]

## Their goals (as agreed [date], by [whom])
| Goal | Measure | Baseline | Target | This period | Source tag | Status |

## Off track, said first
| Item | Why | Our action | Their action | By |

## Last quarter's commitments
| Commitment | Owner (side) | Status |

## Anticipated questions
| Attendee (measured on) | Likely question | Honest answer + evidence |

## Decisions for the room
| # | Decision | Proposed answer | If deferred |

## Agenda (minutes)
## Pre-read to send [n] days before
## Internal brief (not presented): health, renewal date, expansion hypothesis, risks
```

## Verification

- [ ] The first content item is the customer's own goals, attributed.
- [ ] Every number carries a source tag; every `[estimate]` shows its assumptions.
- [ ] At least one off-track item appears before any good news — or the brief
      states, with evidence, that none exists.
- [ ] Every prior commitment has a status.
- [ ] The meeting ends on decisions with proposed answers.
- [ ] No internal-only field appears in the presented sections.

## False-Positive Prevention

1. **Logins are not outcomes.** Seat utilisation and feature usage belong in an
   appendix unless the customer's goal was adoption itself.
2. **Modelled ROI is not realised ROI.** "Saved 1,200 hours" computed from an
   assumption is `[estimate]`, and presenting it as a result is the fastest way
   to lose the CFO.
3. **A green QBR with a red support queue is a red QBR.** If escalations are open,
   they are on the agenda whether or not you put them there.
4. **Roadmap is not value.** A feature preview answers "what will you give us,"
   not "what did we get," and reads as deflection when the second is weak.
5. **Goals you set for them are not their goals.** If success criteria came from
   your template and nobody on their side agreed them, re-agree before reporting.
6. **Do not invent quotes or testimonials.** Customer statements appear only
   when a named person said them, with date.
7. **Do not bury the ask.** A QBR without a decision is a status update the
   sponsor will delegate next time.

## Example Output

```
# QBR prep — Bayfield Grocers — Q3 2026 — meeting 2026-10-09

## Their goals (as agreed 2026-04-02 kick-off, by COO D. Varga)
| Goal | Measure | Baseline | Target | Q3 | Source | Status |
| Cut fuel variance | Monthly variance vs budget | 6.1% | 3.0% | 4.2% | [their-data] finance report | Behind |
| Depot adoption | Depots with weekly report use | 0/12 | 12/12 | 5/12 | [our-data] telemetry | Behind |
| Audit-ready reporting | Q3 audit sample passes | — | pass | passed 09-15 | [their-data] audit memo | Met |

## Off track, said first
| Item | Why | Our action | Their action | By |
| 7 depots not using reports | No local owner; login SSO issue at 4 depots (ticket #4471) | Fix SSO, 2 on-site trainings | Name depot owners | 10-31 |

## Last quarter's commitments
| Deliver SSO for all depots | Us | Late — 8/12 done |
| Share fuel-card exports monthly | Them | Done |

## Anticipated questions
| CFO (cost per mile) | "Is 4.2% from you or from fuel prices?" | Variance is vs budget at actual prices; the 5 active depots average 3.1% vs 5.0% for the 7 inactive — [their-data], 3 months, not causal proof |
| COO (on-time delivery) | "Why only 5 depots?" | SSO ticket #4471 and no depot owners; see off-track item |

## Decisions for the room
| 1 | Name an owner at each of the 7 depots | Yes, by 10-31 | Adoption stays 5/12 into renewal |
| 2 | Confirm Q4 target: 9/12 depots, variance ≤3.5% | Yes | Q4 review has no bar |
| 3 | Sponsor a pilot of route-level reporting at 2 depots | Defer to Q4 | None — optional |

## Agenda (45 min)
5 goals recap · 10 off track · 10 results · 5 commitments · 15 decisions

## Pre-read (send 10-06): goals table + off-track item only.

## Internal brief
Health: amber (adoption). Renewal 2027-04-01 (~26 weeks). Expansion hypothesis:
route-level module, only after depot adoption ≥9/12. Risk: CFO attributes gains
to fuel prices — the depot comparison is the only answer, and it is correlational.
```

## Techniques Used

- **RP-02 Audience-Specific Framing** — built around what each executive is measured on.
- **DS-02 Metric Specification** — measure, baseline, target and source per goal.
- **RT-05 Evidence-Based Reasoning** — provenance tags separate their data, ours, and estimates.
- **NE-23 Objection Pre-emption** — the hardest question per attendee, answered honestly.

## Related Prompts

- `domain-business-strategy/go-to-market/workflow_cs_account_health.md` — the
  internal diagnosis to run before this.
- `domain-business-strategy/go-to-market/workflow_customer_success_onboarding_plan.md`
  — where the success criteria should have been set.
- `domain-sales-customer/customer-success/cs_renewal_risk_and_save_plan.md` — when
  the review shows renewal is at risk.
