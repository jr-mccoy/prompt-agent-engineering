# Expansion Roadmap — `domain-sales-customer/`

**Status as of 2026-09-24:** Wave 1 shipped (coverage roadmap) — 8 prompts across
`sales/` (4), `customer-success/` (2) and `support/` (2), as specified in
[`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md) §5. **Wave 2 shipped** —
the five `go-to-market/` relocations plus four new prompts (17 total). A human-agent
QA scorecard followed in the coverage audit pass (18 total).

**Filing convention:** one prefix per subfolder — `sales_`, `cs_`, `support_`.
Every prompt carries 3–5 verified technique IDs, exactly three resolving
`related_prompts`, a **When to Use** entry naming the neighbour it is distinct
from, and a False-Positive Prevention list.

## Shipped architecture

```
domain-sales-customer/          18 prompts
├── sales/              8   qualification, outbound strategy, mutual close plan, forecast,
│                           strategic account plan; relocated: discovery prep,
│                           pipeline risk, win/loss
├── customer-success/   5   customer QBR, B2B renewal save plan, account feedback
│                           routing loop; relocated: account health, onboarding
└── support/            5   ticket triage and routing, escalation reply + handoff,
                            incident status updates, KB article from tickets,
                            human-agent QA scorecard
```

## Wave 2 — shipped (coverage Wave 2)

| Item | Shipped as | Notes / distinct from |
|---|---|---|
| Strategic account plan | `sales/sales_strategic_account_plan.md` | Whitespace matrix, relationship map, gated expansion sequence; absorbs the expansion/upsell mapping. Distinct from `cs_account_health` (diagnosis) and `cs_customer_qbr_prep` (one meeting). |
| KB article from tickets | `support/support_kb_article_from_tickets.md` | One symptom, customer's verbatim words, fixes counted against confirmed resolutions. Distinct from `solo_dev_support_system` (system design) and `bottleneck_knowledge_base_gap_analysis` (KB-wide audit). |
| Account feedback routing | `customer-success/cs_account_feedback_routing_loop.md` | Shipped in the scoped form the candidate required: one account's items routed to owners and closed with the customer. Cross-account VoC synthesis stays with `skills/marketing/customer-research/`; the candidate name `cs_voice_of_customer_synthesis` was not used. |
| Incident status updates | `support/support_incident_status_update.md` | One-to-many outage communication. Distinct from `support_escalation_response_drafter` (one customer) and the engineering postmortem. |
| Relocate the five `go-to-market/` sales and CS workflows | `sales/` (3), `customer-success/` (2) | Recorded in [`meta/REORG_MAP.tsv`](../meta/REORG_MAP.tsv); old ids resolve as aliases. |

## Audit pass — shipped

| Item | Shipped as | Notes / distinct from |
|---|---|---|
| QA for human support agents | `support/support_agent_interaction_qa_scorecard.md` | Scores a person's call, chat or ticket for coaching, with cause marked agent/process/tool. Distinct from `domain-voice-conversational-ui/analytics/analytics_transcript_qa_rubric.md` (bots) and `domain-professional-writing/content-quality/quality_slop_support_response.md` (one written reply). No prior prompt covered it (duplicate sweep, 2026-09-24). |

## Wave 3 candidates

| Candidate | Notes / distinct from |
|---|---|
| Fold `cs_account_health`'s expansion-opportunity section into a pointer to `sales_strategic_account_plan` | Keeps the health prompt a diagnosis; requires editing a relocated file, so deferred to a maintenance pass. |

## Explicitly not gaps

Cold-email copy, email sequences, sales collateral and objection docs, lead
scoring and routing, self-serve churn flows, and customer research are owned by
`domain-agentic-resources/skills/marketing/`. The negotiation itself belongs to
`domain-negotiation/`. See the "Not here" table in [`README.md`](README.md).
