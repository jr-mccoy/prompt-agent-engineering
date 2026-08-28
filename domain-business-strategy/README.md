# Domain: Business Strategy

**Purpose:** Strategy and go-to-market work at the scale of a company — what the
organization should do, how it positions itself, and how it reaches a market.

**Audience scope:** the **org**. This is the outermost of the repository's five
work-domain tracks (see [Which domain does this belong in?](../CLAUDE.md)):

| Track | Domain |
|---|---|
| Self | `domain-personal-development/` |
| Individual execution | `domain-productivity/` |
| Team delivery | `domain-engineering-workflows/` |
| Product | `domain-product-management/` |
| **Org / company** | **this domain** |

---

## Directory Structure

```
domain-business-strategy/
├── ai-strategy/          # Enterprise AI strategy framing and analysis
├── ambition-leverage/    # Leadership ambition and AI-leverage conversations
├── go-to-market/         # Marketing, sales, and customer-success execution
├── research/             # Competitive and market intelligence
├── startup/              # Founder and solo-operator playbook
└── README.md
```

| Subdirectory | Prompts | What it holds |
|---|---|---|
| `ai-strategy/` | 7 | Agent use-case portfolio, build/buy/hybrid, vendor switch cost, capability compounding, context accumulation, moat narrative, board-ready platform brief |
| `ambition-leverage/` | 5 | Leadership audit, experts-to-builders roadmap, expansion vs. savings brief, founder-bottleneck test, insight-to-action workflow |
| `go-to-market/` | 17 | Marketing playbook (10), campaign brief, content performance, sales discovery and pipeline risk, customer-success onboarding and account health, pre-meeting background research |
| `research/` | 9 | Competitor teardown, competitive landscape, company deep dive, industry trends, vendor and tool evaluation, technical due diligence, user-research synthesis, leader pulse |
| `startup/` | 26 | Monetization (7), founder operations (3), positioning diagnostics (3), plus branding, naming, copy, story, and app-store assets (13) |
| **Total** | **64** | |

---

## What moved out, and why

The domain previously held about 102 prompts. Roughly a third of them were not
company strategy, and were re-homed:

| Was | Now | Why |
|---|---|---|
| `analysis/` (20) | [`domain-software-engineering/analysis/business/`](../domain-software-engineering/analysis/business/) | Every one is titled "… for Codebase" and takes a repository as input |
| `chief-of-staff/` (10) | [`domain-productivity/operating-cadence/`](../domain-productivity/operating-cadence/) | Its own README described it as "personal systems… not built for team-wide rollout" |
| `browser-automation/` (4) | [`domain-productivity/automation/`](../domain-productivity/automation/) | Self-described as "per-user, per-small-team… not an infrastructure-level exercise" |
| `organization/` (3) | productivity + engineering-workflows | Knowledge-management and status reporting, not strategy |
| `monetization_play_billing_implementation` | [`domain-software-engineering/mobile/android/implementation/`](../domain-software-engineering/mobile/android/implementation/) | A Kotlin BillingClient coding prompt |
| `solo_dev_tax_strategy`, `solo_dev_financial_planning` | [`domain-finance/`](../domain-finance/) | Money |
| `solo_dev_business_formation`, `solo_dev_contractor_management` | [`domain-legal/`](../domain-legal/) | Entity formation and contracts |
| `solo_dev_roadmap_planner` | [`domain-engineering-workflows/workflows/`](../domain-engineering-workflows/workflows/) | Delivery planning |
| `solo_dev_weekly_operating_rhythm` | [`domain-productivity/reviews/`](../domain-productivity/reviews/) | Personal operating cadence |
| `research_content_research` | [`domain-professional-writing/writing/`](../domain-professional-writing/writing/) | Source material for an article |

`go-to-market/` is new: it consolidates the `startup/` marketing playbook with the
sales, marketing, and customer-success workflows that were filed under
`domain-engineering-workflows/` despite not being engineering.

---

## Exemplar Prompts

| Prompt | Why it's exemplary |
|---|---|
| [`research/competitor_teardown.md`](research/competitor_teardown.md) | Named competitors required; separates fact from inference and flags every claim to verify |
| [`ai-strategy/aistrategy_platform_brief.md`](ai-strategy/aistrategy_platform_brief.md) | Board-ready output with explicit invalidation conditions |
| [`research/research_competitive_landscape.md`](research/research_competitive_landscape.md) | Structured research methodology with verification steps |

---

## When to use this domain

Use these prompts to decide what the company should do: position against
competitors, size and enter a market, set AI strategy, monetize a product, or
build the go-to-market motion.

**Route elsewhere for:**

- Anything whose input is a codebase → [`domain-software-engineering/`](../domain-software-engineering/)
- Your own calendar, focus, or weekly cadence → [`domain-productivity/`](../domain-productivity/)
- PRDs, market sizing for a feature, sprint planning → [`domain-product-management/`](../domain-product-management/)
- Team delivery process and incident practice → [`domain-engineering-workflows/`](../domain-engineering-workflows/)
- An end-to-end idea → shippable product pipeline → [`domain-idea-to-product/`](../domain-idea-to-product/)
