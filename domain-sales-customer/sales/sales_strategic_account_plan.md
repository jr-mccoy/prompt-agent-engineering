---
title: "Strategic Account Plan — Whitespace Map, Relationship Coverage, and an Expansion Sequence Gated on Evidence"
category: sales-customer/sales
description: "Build an internal 12–24 month plan for one named key account: the customer's own priorities with provenance, a whitespace matrix of business units against products (owned, in use, open-fit, open-unknown, competitor-held), a relationship map that exposes single-threading, and an expansion sequence in which every play is gated on adoption, value proof or renewal timing, with owners, dated milestones and a pause rule — distinct from the account-health diagnosis (cs_account_health), the one-meeting QBR (cs_customer_qbr_prep) and the renewal save plan."
techniques:
  - RT-12
  - DS-01
  - RT-05
  - AG-08
difficulty: advanced
tags:
  - sales
  - key-account-management
  - account-planning
  - expansion
  - whitespace
  - relationship-mapping
  - b2b
updated: "2026-09-24"
related_prompts:
  - domain-sales-customer/customer-success/cs_account_health.md
  - domain-sales-customer/customer-success/cs_customer_qbr_prep.md
  - domain-sales-customer/customer-success/cs_renewal_risk_and_save_plan.md
---

# Strategic Account Plan

**Objective:** Decide where one key account can grow, who at the customer must be
reached to get there, and in what order — with each expansion move held until the
evidence says the customer is ready for it.

**When to Use:**
- A top account is up for annual planning, a new account owner is taking it over,
  or leadership asks "what's the growth plan for this customer?"
- Expansion has been pitched opportunistically and keeps stalling.
- The relationship rests on one or two people and you want to see it before they leave.
- **Not this prompt if** you need to know how healthy the account is right now —
  `domain-sales-customer/customer-success/cs_account_health.md` is the diagnosis
  this plan starts from (and its expansion indicators feed the whitespace map).
  For one executive meeting, use `cs_customer_qbr_prep.md`. If renewal is at risk
  inside ~180 days, use `cs_renewal_risk_and_save_plan.md` first; a plan built on
  an at-risk renewal is a wish list. For a new logo, use
  `sales_deal_qualification_scorecard.md`.

## Inputs / Context

1. **Account facts:** products owned, ARR, contract and renewal dates, adoption data.
2. **The customer's priorities** in their words — annual report, QBR goals, stated
   initiatives — with who said it and when.
3. **Organisation:** business units, sites, fleets or teams, and which ones you serve.
4. **People:** every contact you know, role, last substantive interaction, stance.
5. **Your portfolio:** products and modules, with list pricing.
6. **Competitive footprint:** incumbents in areas you do not serve, contract ends if known.
7. **Current health signals:** latest health assessment, open incidents, escalations.

Provenance tags as in the rest of this domain: `[their-data]`, `[our-data]`,
`[estimate]`; people and quotes dated and attributed. Gaps are `[ASK]` or
`[NOT PROVIDED]`.

## Method

1. **Anchor on their priorities (RT-05).** List the customer's stated priorities
   first, each with source. A play that serves none of them is parked, however
   good the product fit.

2. **Build the whitespace matrix (DS-01).** Rows: business units or sites. Columns:
   your products. Each cell exactly one state: **Owned** (with adoption level),
   **Open-fit** (evidence of the need from their data or words), **Open-unknown**
   (plausible, no evidence), **Competitor-held** (with contract end if known),
   **N/A**. Dollar-size only Owned gaps and Open-fit cells, as `[estimate]` with the
   pricing basis.

3. **Infer adjacent opportunities, transparently (RT-12).** Where the matrix
   suggests something the account team has not raised — a unit you have never
   contacted, a use that follows from what they already do — list it as
   **inferred** with the reasoning, never as a pipeline number.

4. **Map relationships.** Per person: role in buying (economic, technical, user,
   sponsor, potential blocker), stance, our owner, last substantive contact.
   Flag: single-threading (one contact holds the account), economic buyers never met,
   and units in the whitespace with no known contact.

5. **Sequence the plays behind gates (AG-08).** Each play states:
   the **gate** it must pass (e.g. adoption ≥ a threshold, a success criterion met,
   renewal signed, an introduction made), the evidence that shows it passed, owner,
   target quarter, and `[estimate]` value. Fix adoption and open escalations before
   any expansion; an unsigned renewal comes before any upsell.

6. **Set the pause rule.** One observable condition, with a date, that pauses all
   expansion plays and turns the plan into a retention plan.

7. **Keep it internal.** This document never goes to the customer as written; the
   QBR prep is where customer-facing material is built.

## Output Format

```
# Strategic account plan — [Account] — [period] — owner [..] — as of [date]
ARR $[..] · renewal [date] · health [..] (source)

## Their priorities
| Priority | Source (who, date) | Our relevance |

## Whitespace matrix
| Unit / Product | P1 | P2 | P3 | P4 |
Open-fit value [estimate]: $[..]   Inferred opportunities: [..]

## Relationship map
| Person | Title | Buying role | Stance | Our owner | Last substantive contact | Flag |

## Expansion sequence
| # | Play | Gate | Evidence it passed | Owner | Target | Value |

## Pause rule
## Risks and asks of our side
## Not for the customer
```

## Verification

- [ ] Every priority has a source and date; every play maps to one.
- [ ] Every matrix cell has exactly one state; only Owned gaps and Open-fit cells carry dollars.
- [ ] All dollar values are `[estimate]` with a pricing basis, and they sum correctly.
- [ ] Every play has a gate with observable evidence and a date.
- [ ] The relationship map flags any economic buyer never met.
- [ ] The pause rule is one observable event with a date.

## False-Positive Prevention

1. **Whitespace is not pipeline.** An open cell becomes an opportunity when the
   customer's data or words show the need; until then it is Open-unknown.
2. **Product fit is not their priority.** A module that serves nothing they said
   they care about will be politely declined, then remembered.
3. **Upselling an unhealthy account accelerates churn.** Adoption and escalations
   come first; the gate enforces it.
4. **A sponsor is not a relationship map.** If the COO leaves, who else knows why
   you are there?
5. **Inferred opportunities are labelled, not forecast.** They are questions for
   the next conversation.
6. **A competitor-held cell is not an attack plan.** Without a contract end date
   and a stated dissatisfaction, park it.
7. **No fabricated contacts, quotes or org charts.** Unknown people are `[ASK]`.

## Example Output

```
# Strategic account plan — Bayfield Grocers — Q4 2026–Q4 2027 — owner Priya
# Shah (AM) — as of 2026-09-24
ARR $96,000 [our-data] · renewal 2027-04-01 · health amber — depot adoption 5/12
(QBR prep, 2026-10-09) · Incident C-1 (fuel sync) escalated 09-24, credit pending

## Their priorities
| Cut fuel variance to 3.0% | COO D. Varga, kick-off 2026-04-02 | Core + fuel reconciliation |
| Audit-ready reporting | Audit memo 09-15 [their-data] | Core (met) |
| Grow home delivery 30% in 2027 | Annual report p.4 [their-data] | Van fleet — no contact |

## Whitespace matrix
| Unit / Product | Core analytics | Fuel reconciliation | Route-level reporting | Maintenance scheduling |
| Distribution (12 depots) | Owned — 5/12 adopted | Owned — C-1 open | Open-fit: COO deferred pilot to Q4 (QBR decision 3) | Open-unknown |
| Home delivery (40 vans) | Open-unknown | Open-unknown | Open-unknown | Open-unknown |
| Refrigerated trailers | Competitor-held (incumbent telematics; end date [ASK]) | N/A | N/A | N/A |
Open-fit value [estimate]: route-level at 12 depots × $200/mo = $28,800 ARR.
Inferred: home-delivery vans — a 30% growth goal on a fleet we already analyse
for depots suggests the same fuel-variance problem; no one has asked. Sizing
40 vans × $40/mo = $19,200 [estimate] only after discovery confirms the need.

## Relationship map
| D. Varga | COO | Economic buyer, sponsor | Supportive | Priya Shah | QBR 07-15 | — |
| CFO | Approves spend [ASK: threshold] | Economic buyer | Skeptical: "Is 4.2% from you or fuel prices?" | none | never 1:1 | Never met 1:1 |
| Dana | Ops Director | User lead | Frustrated (C-1, 09-24) | Sam Ortiz | 09-24 | Escalation open |
| IT manager | SSO owner | Technical | Neutral | CSM | ticket #4471 | — |
| Home-delivery lead | [ASK] | Unknown | — | none | — | No contact in growth unit |
Single-threaded on the COO for all commercial decisions.

## Expansion sequence
| 0 | Close C-1 credit; fix SSO #4471 | Credit decided, SSO live | Priya's reply sent; 12/12 SSO | Priya / CSM | Q4 2026 | — |
| 1 | Depot adoption to 9/12 | Named owner at each depot | Telemetry [our-data] | CSM | 2027-01-31 | protects $96,000 |
| 2 | Renew core; 2-year option | Adoption ≥ 9/12 | Signed order form | Priya | 2027-04-01 | $96,000 |
| 3 | Route-level pilot, 2 depots | Renewal signed; pilot success criterion agreed with COO | Criterion in writing | Priya | Q2 2027 | $4,800 one-off [estimate] |
| 4 | Route-level, all depots | Pilot criterion met | Pilot readout | Priya | Q3 2027 | +$28,800 ARR [estimate] |
| 5 | Home-delivery discovery | COO introduces the home-delivery lead | Meeting held | Priya | Q2 2027 | +$19,200 ARR [estimate, inferred] |
| — | Refrigerated trailers | Contract end known + stated dissatisfaction | — | — | parked | — |
Identified expansion: $28,800 + $19,200 = $48,000 ARR [estimate] (+50% on $96,000).

## Pause rule
Depot adoption < 7/12 on 2027-01-31, or C-1 recurs before renewal → pause plays
3–5; move to cs_renewal_risk_and_save_plan.

## Risks and asks of our side
CFO has never met anyone from us: our VP CS requests a CFO meeting via the COO
before 2027-01-15, with the depot comparison (correlational, labelled as such).

## Not for the customer
Internal plan. Customer-facing material is built in cs_customer_qbr_prep.
```

## Techniques Used

- **RT-12 Adjacent Opportunity Inference** — the home-delivery fleet surfaced and labelled as inferred.
- **DS-01 Framework Application** — whitespace matrix with one state per cell.
- **RT-05 Evidence-Based Reasoning** — priorities, stances and open-fit cells cite sources.
- **AG-08 Evidence-Based Decision Gates** — no play starts until its gate shows evidence.

## Related Prompts

- `domain-sales-customer/customer-success/cs_account_health.md` — the health
  diagnosis and expansion indicators this plan starts from.
- `domain-sales-customer/customer-success/cs_customer_qbr_prep.md` — the
  customer-facing meeting where plays are proposed.
- `domain-sales-customer/customer-success/cs_renewal_risk_and_save_plan.md` —
  where the plan goes when the pause rule fires.
