# Expansion Roadmap — `domain-sales-customer/`

**Status as of 2026-09-24:** Wave 1 shipped (coverage roadmap) — 8 prompts across
`sales/` (4), `customer-success/` (2) and `support/` (2), as specified in
[`meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md) §5.

**Filing convention:** one prefix per subfolder — `sales_`, `cs_`, `support_`.
Every prompt carries 3–5 verified technique IDs, exactly three resolving
`related_prompts`, a **When to Use** entry naming the neighbour it is distinct
from, and a False-Positive Prevention list.

## Shipped architecture

```
domain-sales-customer/          8 prompts
├── sales/              4   qualification, outbound strategy, mutual close plan, forecast
├── customer-success/   2   customer QBR, B2B renewal save plan
└── support/            2   ticket triage and routing, escalation reply + handoff
```

## Wave 2 candidates

| Candidate | Notes / distinct from |
|---|---|
| `sales/sales_strategic_account_plan.md` | Multi-year plan for one named key account: whitespace, relationship map, expansion sequence. Distinct from `workflow_cs_account_health` (diagnosis) and `cs_customer_qbr_prep` (one meeting). |
| `support/support_kb_article_from_tickets.md` | Turn a resolved-ticket cluster into a help-centre article with the customer's own symptom language. Distinct from `solo_dev_support_system` (system design). |
| `customer-success/cs_voice_of_customer_synthesis.md` | Only if it is scoped to routing account-level feedback to owners; interview and review-mining synthesis is owned by `skills/marketing/customer-research/` — duplicate-sweep first. |
| Relocate the five `go-to-market/` sales and CS workflows | `workflow_sales_discovery_call_preparation`, `workflow_sales_pipeline_risk_assessment`, `workflow_win_loss_analysis`, `workflow_cs_account_health`, `workflow_customer_success_onboarding_plan` → this domain, recorded in [`meta/REORG_MAP.tsv`](../meta/REORG_MAP.tsv) with tombstones and inbound-reference rewrites. Deferred from Wave 1 because a move changes the relationship-count tests. |

## Explicitly not gaps

Cold-email copy, email sequences, sales collateral and objection docs, lead
scoring and routing, self-serve churn flows, and customer research are owned by
`domain-agentic-resources/skills/marketing/`. The negotiation itself belongs to
`domain-negotiation/`. See the "Not here" table in [`README.md`](README.md).
