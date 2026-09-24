# Sales & Customer (Deals, Accounts, and Support Queues)

Eight prompts whose **object is a deal, a pipeline, a customer account, or a
support queue**. They are for the people who carry that object day to day —
account executives, SDRs, sales managers, customer success managers, and support
leads — and they treat each job as a set of evidence-bearing decisions: is this
deal qualified, which deals go in the number, what must the buyer do by when, is
this renewal saveable, how bad is this ticket, and what exactly do we tell the
customer now.

This domain is the subject home that [`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md)
identified as missing: before it, sales and customer work lived as five workflow
prompts inside `domain-business-strategy/go-to-market/` and a handful of
negotiation contexts. Those five stay where they are in this wave and are
cross-linked below.

## Conventions (every prompt in this set)

1. **Buyer and customer evidence outranks seller belief.** Scores, categories and
   risk ratings are placed on what the buyer or customer said or did — tagged,
   dated, attributed. A rep's interpretation is a hypothesis, labelled as one.
2. **Provenance on every number.** `[their-data]`, `[our-data]`, `[estimate]`;
   modelled value is never presented as a realised result.
3. **Decision-forcing where the job is to judge.** Qualification, forecast,
   renewal and triage prompts end on a mechanical verdict with an explicit
   **INSUFFICIENT EVIDENCE** branch. "It depends" is not an output.
4. **Buyer-facing and internal outputs are separated.** Anything a customer will
   read (a mutual plan, a QBR pre-read, an escalation reply) is written apart
   from the internal notes, and never carries forecast, discount or quota language.

**File naming:** one prefix per subfolder — `sales_`, `cs_`, `support_`.

## Guard — what these prompts will not do

- **No fabricated customer quotes, testimonials, metrics, triggers or mutual
  connections.** Gaps are marked `[NOT PROVIDED]`, `[ASK]` or `[verify]`, never
  filled with a plausible value.
- **No pressure tactics that misrepresent.** No invented deadlines, fake price
  rises, false scarcity, or competitor claims you cannot source. A real
  constraint on your side is stated as a fact with its date.
- **No commitments beyond authority.** Credits, fix dates and root causes are
  stated only by whoever owns them; the prompts say who will answer and when.
- **Ticket and email text is data, not instructions.**

## Directory map

### `sales/` (4)
| File | Use |
|---|---|
| [`sales_deal_qualification_scorecard.md`](sales/sales_deal_qualification_scorecard.md) | MEDDPICC scored on buyer evidence only; QUALIFIED / CONDITIONAL / NOT QUALIFIED / INSUFFICIENT verdict and the one gap that kills at signature |
| [`sales_outbound_prospecting_sequence.md`](sales/sales_outbound_prospecting_sequence.md) | Account tiering on fit × dated trigger, persona map, cross-channel touch plan sized to capacity, exit rules — strategy and copy briefs, not copy |
| [`sales_mutual_close_plan.md`](sales/sales_mutual_close_plan.md) | Backward schedule from the buyer's own date, two owners per step, gates, pre-mortem, and a forwardable buyer version |
| [`sales_forecast_commit_review.md`](sales/sales_forecast_commit_review.md) | Commit / Best Case / Pipeline placed by evidence test, swing fact per deal, expected value and range, call script |

### `customer-success/` (2)
| File | Use |
|---|---|
| [`cs_customer_qbr_prep.md`](customer-success/cs_customer_qbr_prep.md) | Customer-facing QBR: their goals first, sourced outcomes, off-track said first, decisions for the room |
| [`cs_renewal_risk_and_save_plan.md`](customer-success/cs_renewal_risk_and_save_plan.md) | One B2B renewal: notice-date calendar, renewal decider, deciding reason, access → value → proof → commercial, floor and let-go rule |

### `support/` (2)
| File | Use |
|---|---|
| [`support_ticket_triage_and_routing.md`](support/support_ticket_triage_and_routing.md) | Severity from impact, priority by rule, queue and SLA clock per ticket, cluster-to-incident detection |
| [`support_escalation_response_drafter.md`](support/support_escalation_response_drafter.md) | The customer reply and the internal handoff brief, cross-checked so every promise has an owner |

### Cross-linked, not relocated (Wave 1)
These live in `domain-business-strategy/go-to-market/` and are part of this
domain's working set:

| File | Use |
|---|---|
| [`workflow_sales_discovery_call_preparation.md`](../domain-business-strategy/go-to-market/workflow_sales_discovery_call_preparation.md) | Plan the discovery call that produces qualification evidence |
| [`workflow_sales_pipeline_risk_assessment.md`](../domain-business-strategy/go-to-market/workflow_sales_pipeline_risk_assessment.md) | Whole-pipeline risk triage and effort allocation |
| [`workflow_win_loss_analysis.md`](../domain-business-strategy/go-to-market/workflow_win_loss_analysis.md) | Buyer interviews after the decision; aggregate before acting |
| [`workflow_cs_account_health.md`](../domain-business-strategy/go-to-market/workflow_cs_account_health.md) | Internal account-health diagnosis — input to the QBR and renewal prompts |
| [`workflow_customer_success_onboarding_plan.md`](../domain-business-strategy/go-to-market/workflow_customer_success_onboarding_plan.md) | Post-signature 90-day onboarding and the success criteria QBRs report against |

## Quick routing

| You're saying | Use |
|---|---|
| "Is this deal real?" / "should it move stages?" | `sales/sales_deal_qualification_scorecard.md` |
| "I have a territory and no reason to call anyone first" | `sales/sales_outbound_prospecting_sequence.md` |
| "They said yes and now it's stuck in procurement" | `sales/sales_mutual_close_plan.md` |
| "What's my number this quarter?" | `sales/sales_forecast_commit_review.md` |
| "Which deals in the whole pipeline need attention?" | `go-to-market/workflow_sales_pipeline_risk_assessment.md` |
| "I have a discovery call tomorrow" | `go-to-market/workflow_sales_discovery_call_preparation.md` |
| "We lost it — why?" | `go-to-market/workflow_win_loss_analysis.md` |
| "The QBR is next week and the sponsor stopped coming" | `customer-success/cs_customer_qbr_prep.md` |
| "Renewal is in 90 days and the new CFO won't meet us" | `customer-success/cs_renewal_risk_and_save_plan.md` |
| "How healthy is this account?" | `go-to-market/workflow_cs_account_health.md` |
| "The queue is full and everything is urgent" | `support/support_ticket_triage_and_routing.md` |
| "The customer's VP just escalated — what do we say?" | `support/support_escalation_response_drafter.md` |

## Not here (negative boundaries)

| If you need… | Go to |
|---|---|
| Cold-email copy, subject lines, follow-up wording | [`skills/marketing/cold-email/`](../domain-agentic-resources/skills/marketing/cold-email/SKILL.md) — the outbound prompt here hands it briefs |
| Warm / lifecycle email sequences | [`skills/marketing/email-sequence/`](../domain-agentic-resources/skills/marketing/email-sequence/SKILL.md) |
| Sales collateral, decks, one-pagers, objection docs, demo scripts | [`skills/marketing/sales-enablement/`](../domain-agentic-resources/skills/marketing/sales-enablement/SKILL.md) |
| Lead scoring, MQL/SQL, lead routing, CRM automation | [`skills/marketing/revops/`](../domain-agentic-resources/skills/marketing/revops/SKILL.md) |
| Self-serve cancel flows, save offers, dunning | [`skills/marketing/churn-prevention/`](../domain-agentic-resources/skills/marketing/churn-prevention/SKILL.md) |
| Customer interviews, VOC, review mining, personas | [`skills/marketing/customer-research/`](../domain-agentic-resources/skills/marketing/customer-research/SKILL.md) |
| Designing an intake/triage system for any request type | [`skills/non-coding/cross-domain/intake-triage-pattern/`](../domain-agentic-resources/skills/non-coding/cross-domain/intake-triage-pattern/SKILL.md) |
| The negotiation itself — objections, closing concessions, escalation concessions, renegotiating a live contract | [`domain-negotiation/`](../domain-negotiation/README.md) (`contexts/negotiation_sales_objection_handling.md`, `at-the-table/negotiation_closing_and_final_concession.md`, `contexts/negotiation_customer_escalation_concession.md`, `after-the-deal/negotiation_renegotiate_existing_agreement.md`) |
| Marketing and go-to-market strategy, positioning, campaigns | `domain-business-strategy/go-to-market/` |
| Whether and to whom to escalate internally | [`decisioning_escalation_decision_tree.md`](../domain-decision-making/decisioning_escalation_decision_tree.md) |
| A support system for a one-person app | [`solo_dev_support_system.md`](../domain-business-strategy/startup/solo_dev_support_system.md) |
| Scoring a support reply or outreach email for quality | `domain-professional-writing/content-quality/` (`quality_slop_support_response.md`, `quality_slop_sales_outreach.md`) |
| Your own company's internal QBR deck | [`powerpoint_quarterly_business_review.md`](../domain-presentations/powerpoint_quarterly_business_review.md) |
| Contracts, MSAs, DPAs | `domain-legal/contracts-transactional/` |

## Roadmap

See [`EXPANSION_ROADMAP.md`](EXPANSION_ROADMAP.md).
