---
title: "Licensing and IP Terms — Negotiating Scope, Exclusivity, and the Royalty Base"
category: negotiation/contexts
description: "Negotiate the business terms of an IP, technology, content, or brand license from either side, before the lawyers draft: scope (field of use, territory, term), exclusivity and what it must be paid for, the economic structure (upfront, royalty rate and — more importantly — royalty base, minimums, milestones), sublicensing and improvements, and termination. Treats exclusivity as the most valuable and most often underpriced term. Counters the failure this context produces: fighting over the royalty rate while conceding the base, the scope, or exclusivity without performance obligations."
techniques:
  - ST-01
  - RT-02
  - DS-01
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - negotiation
  - licensing
  - intellectual-property
  - royalties
  - deal-structure
updated: "2026-09-24"
reasoning:
  styles: [analytic, strategic, adversarial]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: structured
  user_role: [founder, executive, creator, business_development]
  mode: [plan, decide, rehearse]
related_prompts:
  - domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md
  - domain-negotiation/preparation/negotiation_package_trade_design.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
---

# Licensing and IP Terms — Negotiating Scope, Exclusivity, and the Royalty Base

**Objective:** A license negotiation looks like an argument about a percentage. It is really an argument about **what the percentage applies to** and **what is being granted**. A generous royalty rate on a narrowly defined base, with deductions allowed before it is calculated, can pay less than a modest rate on gross revenue. An exclusive, worldwide, all-fields grant with no minimums can lock an asset into a partner who never commercializes it. And the terms that decide the deal's real value — **field of use, territory, term, exclusivity, sublicensing, improvements, and termination** — are frequently settled quickly while the parties fight over a point of rate.

This prompt negotiates the **business terms** from either side — licensor or licensee — in the order that reflects their value: scope first, exclusivity and its price second, economic structure third, then the governance terms that determine what happens when things change. It treats **exclusivity as the most valuable and most often underpriced term** in a license: it should be paid for, and bounded by performance obligations — minimum royalties, diligence milestones, or reversion to non-exclusive if they are missed.

Drafting the agreement is a legal task — `domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md` — and the position paper that lawyers negotiate from is `legal_negotiation_position_paper.md`. Warranties, indemnities, IP ownership, validity, and infringement risk belong with counsel. This prompt decides what you want the deal to be before those documents are written. `preparation/negotiation_package_trade_design.md` supplies the general method for trading terms of different value to each side.

**When to use:**
- You are licensing out (or in) technology, a patent, software, content, a brand, or a character.
- A term sheet or first draft has arrived and you need to decide what to push on.
- The discussion has stalled on the royalty rate.
- You are being asked for exclusivity and need to decide its price and conditions.

**When NOT to use:**
- You need the agreement drafted or reviewed — `legal_licensing_agreement_drafter.md`.
- The question is open-source license compatibility — `domain-legal/ip/legal_open_source_license_compatibility_review.md`.
- You are selecting a vendor's software licence as a buyer — `contexts/negotiation_vendor_procurement_buyside.md`.
- The dispute is an infringement claim rather than a license negotiation — `domain-legal/`.

**Audience:** Founders, executives, creators, and business-development leads negotiating a license on either side.

---

## Inputs / Context

1. **Your side and the asset.** Licensor or licensee; what exactly is licensed; its stage and proof of value.
2. **The proposal.** Current terms on scope, exclusivity, economics, sublicensing, improvements, term, and termination.
3. **Commercial plans.** How the licensee intends to use the asset, in which products, markets, and timeframes. Tag projections `known / inferred / guessed`.
4. **Alternatives.** Other potential partners or assets, building or developing an alternative, or not licensing at all.
5. **Comparable deals.** Any known terms for similar licenses, with sources and tags. Treat most published royalty "norms" with caution.
6. **Constraints.** Existing licenses, prior grants, funding or regulatory constraints that limit what can be granted.

---

## Constraints

### Must
- Negotiate **scope before price**: field of use, territory, term, and the exact definition of the licensed asset.
- Define the **royalty base** precisely — gross or net, which deductions, which products, at what point of sale — before discussing the rate.
- Price **exclusivity explicitly**, and bound it with **performance obligations**: minimums, diligence milestones, or reversion if they are missed.
- **Steelman the other side**: a licensee takes commercialization risk and cost; a licensor gives up alternative uses. Both are real.
- Model the **economics under several scenarios** — slow, expected, fast — so both sides see what each structure pays.
- Settle **sublicensing, improvements, and termination** as business terms before drafting, not as legal boilerplate.
- Tag every projection and comparable `known / inferred / guessed`.
- Route **warranties, indemnities, ownership, validity, and drafting** to counsel.

### Must Not
- Concede the base, scope, or exclusivity to win a point on the rate.
- Grant or accept exclusivity with no minimums, milestones, or reversion.
- Rely on a single "industry standard" royalty figure as if it settled the question.
- Leave "improvements" or "net sales" undefined for the lawyers to resolve later.
- Overstate the asset's validity, proof of value, or the other party's alternatives.
- Draft legal language or opine on IP validity, infringement, or enforceability.

---

## Instructions

### Step 1 — Define exactly what is licensed
Name the asset, its versions, and what is excluded. Ambiguity here becomes a dispute later about whether a product is covered.

### Step 2 — Set the scope
Field of use, territory, and term. For a licensor, narrow scope preserves other deals; for a licensee, scope must cover the actual plan with reasonable room to grow. Map where the plans and the scope diverge.

### Step 3 — Decide exclusivity and its price
Exclusive, sole, or non-exclusive — and in which fields and territories. If exclusive, attach its price (higher upfront, higher minimums) and its conditions (diligence milestones, reversion to non-exclusive if missed).

### Step 4 — Define the royalty base
Gross or net; which deductions; which products and bundles; when a sale counts. Model two or three definitions to show their effect. Settle the base before the rate.

### Step 5 — Build the economic structure
Combine upfront payment, royalty rate, minimums, milestones, and caps or tiers. Model each structure under slow, expected, and fast scenarios with tagged assumptions. Choose structures that align incentives rather than only maximizing your side's expected value.

### Step 6 — Settle governance terms
Sublicensing (allowed, with consent, revenue share); improvements (who owns, who may use, grant-backs); audit rights; term and renewal; termination triggers and what survives. These determine what happens when circumstances change.

### Step 7 — Design packages
Using `preparation/negotiation_package_trade_design.md`, build two or three equivalent packages — for example, higher royalty with narrower scope versus lower royalty with exclusivity and minimums — and offer them together.

### Step 8 — Hand off to counsel
Summarize the agreed business terms in a term sheet or position paper for the lawyers, and list the legal questions — warranties, indemnities, ownership, validity — for them to resolve.

### Step 9 — Adversarial check
- If the licensee never commercializes, what does the licensor end up with under your terms?
- If the product succeeds far beyond expectations, does the structure still feel fair to both sides — or will one side seek to reopen it?
- Which term did you concede quickly while arguing about the rate?

---

## False-Positive Prevention

1. **Rate fixation.** Negotiating the percentage while the base, scope, or deductions quietly determine what is actually paid.
2. **Free exclusivity.** Granting or accepting exclusivity without paying or charging for it.
3. **Exclusivity without diligence.** No minimums, milestones, or reversion, leaving the asset locked in a partner who does not use it.
4. **Undefined "net."** Leaving deductions and bundling unspecified, which becomes a recurring audit dispute.
5. **Industry-standard anchoring.** Treating a single published royalty figure as settled, when comparables vary widely by field and stage.
6. **Single-scenario modeling.** Evaluating a structure only at the expected case, missing how it behaves in failure or runaway success.
7. **Governance as boilerplate.** Leaving sublicensing, improvements, and termination to the lawyers, where they are settled without business judgment.
8. **Overstated asset or alternatives.** Claims about validity, proof of value, or competing interest that do not survive diligence.

---

## Output Format

```
# License Negotiation Plan — [asset / counterpart]

## Side and asset
[Licensor / licensee] · Asset: [...] · Excluded: [...]

## Scope
| Term | Their proposal | My position | Gap |
|---|---|---|---|
| Field of use | | | |
| Territory | | | |
| Term | | | |

## Exclusivity
Type: [exclusive / sole / non-exclusive] · Where: [...]
Price: [...] · Conditions: [minimums / milestones / reversion]

## Royalty base
| Definition | Deductions | Effect under expected case |
|---|---|---|

## Economic structure
| Structure | Upfront | Rate | Minimums | Milestones | Slow | Expected | Fast |
|---|---|---|---|---|---|---|---|
Assumptions (tagged): [...]

## Governance
Sublicensing: [...] · Improvements / grant-back: [...] · Audit: [...]
Termination triggers and survival: [...]

## Packages (offered together)
A: [...] · B: [...] · C: [...]

## Counsel hand-off
Agreed business terms: [...] · Legal questions: [warranties / indemnities / ownership / validity]

## Adversarial check
- If never commercialized: [...]
- If runaway success: [...]
- Term conceded quickly while arguing rate: [...]
```

---

## Verification

- [ ] Licensed asset defined with exclusions.
- [ ] Scope negotiated before price.
- [ ] Exclusivity priced and bounded by performance obligations.
- [ ] Royalty base defined before the rate, with alternative definitions modeled.
- [ ] Economic structures modeled under slow, expected, and fast scenarios with tagged assumptions.
- [ ] Sublicensing, improvements, audit, and termination settled as business terms.
- [ ] Other side's position steelmanned.
- [ ] Equivalent packages designed and offered together.
- [ ] Legal questions handed to counsel.
- [ ] Adversarial check tests non-commercialization and runaway-success cases.
- [ ] No exclusivity without minimums, milestones, or reversion.
- [ ] No legal drafting or opinion on validity or infringement.
