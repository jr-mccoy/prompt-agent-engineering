---
title: "Regulatory Requirement Mapper — Map Applicable Regulations to Business Activities"
category: finance/regulatory-compliance
description: "Map applicable regulations and regulatory bodies (SEC, FINRA, Basel/BIS, Dodd-Frank, MiFID II, FinCEN, OFAC, etc.) to specific business activities, products, and entities — producing a defensible requirement-to-activity matrix with jurisdiction flags, owner assignment, and verify-against-current-source guardrails."
techniques:
  - DT-02
  - ST-02
  - CM-02
  - QA-05
  - DS-06
difficulty: advanced
tags:
  - regulatory-mapping
  - compliance
  - jurisdiction
  - regulatory-inventory
  - applicability
updated: "2026-06-08"
related_prompts:
  - domain-finance/regulatory-compliance/finance_compliance_gap_analysis.md
  - domain-finance/regulatory-compliance/finance_regulatory_filing_calendar.md
  - domain-finance/risk-management/finance_enterprise_risk_register.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not legal or compliance advice. Regulations change and vary by jurisdiction; confirm all requirements against current official sources (SEC, FINRA, Basel/BIS, FinCEN, OFAC, EU/ESMA, and applicable local regulators) and qualified counsel before relying on any output.**

## Objective

Produce a structured regulatory-requirement inventory that maps each material business activity, product, and legal entity to the regulations and regulatory bodies that plausibly apply — with jurisdiction flags, an applicability rationale, an owner, and explicit instructions to verify every cited rule, threshold, and effective date against the current official source. This is a scoping-and-organizing tool that frames *what likely applies and where to confirm it* — not a legal determination of applicability.

## When to Use

- Standing up a compliance program for a new entity, product line, or geography
- Pre-launch regulatory scoping for a new financial product or service
- Building or refreshing a regulatory inventory / obligations library
- Preparing the applicability baseline that feeds a gap analysis (see companion prompt)
- M&A integration: mapping the target's regulatory footprint onto the acquirer's framework

## Inputs / Context Required

```
<regulatory_mapping_context>
ENTITY / BUSINESS:
- Legal entity name(s) and structure (bank holding co, broker-dealer, RIA, fund, fintech, etc.)
- Charter / license types held and pending
- Primary and functional regulators known to oversee the entity

ACTIVITIES & PRODUCTS (list each):
- Activity / product description (e.g., deposit-taking, securities brokerage, investment advice,
  payments / money transmission, lending, custody, market-making, crypto-asset services)
- Customer types served (retail, institutional, qualified/accredited, government)
- Channels (in-person, online, cross-border)

JURISDICTIONS:
- Countries / states / regions where each activity is conducted or marketed
- Home regulator and host regulators
- Cross-border / passporting considerations

KNOWN REGULATORY UNIVERSE (user-supplied or to be researched against official sources):
- Regulations the user already believes apply
- Recent regulatory changes flagged by the user

CONSTRAINTS:
- Materiality threshold for inclusion
- Date of this mapping exercise: __________
</regulatory_mapping_context>
```

## Constraints

### Must
- State the **jurisdiction and applicable regulator(s)** for every mapped requirement.
- For every regulation, citation, section number, threshold, or effective date referenced, mark it as **"[verify against current [regulation] text]"** and require confirmation against the official source. Do not assert specific rule numbers, dollar/percentage thresholds, or deadlines from memory as authoritative.
- Name regulatory bodies and frameworks **generically and correctly** (e.g., "SEC registration and reporting obligations for investment advisers," "Basel III capital framework as implemented by the local prudential regulator") rather than inventing rule numbers.
- Provide an **applicability rationale** for each mapping (why this activity triggers this regulation), and an explicit triggering threshold/condition marked for verification.
- Assign each requirement a **provisional owner** (function/role) and a **confidence flag** (High / Medium / Low applicability certainty).
- Prioritize requirements by **enforcement severity and likelihood** (DS-06).
- Flag activities where applicability is genuinely uncertain and route to counsel.
- Include a **completeness self-audit** that asks which activities, products, jurisdictions, or regulator types may have been omitted.

### Must Not
- Fabricate or assert specific regulatory citations, section numbers, thresholds, or filing deadlines as authoritative.
- Treat the map as a legal determination of applicability — it is a scoping aid.
- Assume that prior-year or another-entity mapping carries over unchanged (over-reliance on prior mapping is a named pitfall).
- Omit cross-border, host-regulator, or marketing-into-jurisdiction obligations.
- Present a "clean" map without naming the activities/jurisdictions that were out of scope or unverified.

## Instructions

**Step 1 — Inventory activities, products, and entities (ST-02).**
List every material activity/product per legal entity. Note customer types and channels, since these often drive applicability (e.g., retail vs. institutional).

**Step 2 — Establish the jurisdiction lattice.**
For each activity, list every jurisdiction where it is conducted *or marketed*. Mark home vs. host regulator and any cross-border trigger. Marketing into a jurisdiction can trigger obligations even without a local entity — verify per jurisdiction.

**Step 3 — Map regulatory bodies and frameworks to each activity (DT-02).**
For each activity × jurisdiction, identify the plausibly applicable regulator(s) and framework(s). Use generic-but-correct framing. Common mappings to consider (confirm applicability per facts):

| Activity (example) | Regulator(s) to consider | Framework area (verify current text) |
|---|---|---|
| Securities offering / public reporting | SEC (US); ESMA / national competent authority (EU) | Registration, periodic & current reporting |
| Broker-dealer activity | SEC + FINRA (US) | Net capital, conduct, supervision, books & records |
| Investment advice | SEC or state (US, by AUM); local regulator | Adviser registration, fiduciary/conduct duties |
| Banking / deposit-taking | Prudential + conduct regulators | Capital (Basel III as locally implemented), liquidity, consumer protection |
| Derivatives / swaps | CFTC / SEC (US); EMIR regime (EU) | Clearing, reporting, margin |
| AML / sanctions | FinCEN, OFAC (US); national FIUs | BSA-type program, CDD, screening |
| Payments / money transmission | State regulators + FinCEN (US); local PSD-type regime (EU) | Licensing, safeguarding, conduct |
| Markets / trading conduct | SEC/FINRA; ESMA under MiFID II | Best execution, transparency, market abuse |

Mark each referenced rule/threshold as "[verify against current [regulation] text]."

**Step 4 — Record the applicability rationale and triggering condition.**
For each mapping, state *why* it applies (activity → trigger) and the threshold/condition that governs (e.g., "registration required above [AUM threshold — verify]"). Where the trigger is fact-dependent or unclear, mark confidence Low and route to counsel.

**Step 5 — Assign owners and prioritize (DS-06).**
Assign a provisional owner function. Rank each requirement by a composite of enforcement severity and likelihood:
- **Tier 1 (Critical):** Core licensing/registration; AML/sanctions; capital/liquidity; mandatory periodic filings.
- **Tier 2 (High):** Conduct, disclosure, recordkeeping, supervision obligations.
- **Tier 3 (Monitor):** Lower-severity or facts-uncertain obligations pending confirmation.

**Step 6 — Completeness self-audit (NE-06 / QA-02).**
Explicitly answer: Which activities/products were not mapped? Which jurisdictions (especially marketing-only or cross-border) might be missed? Which regulator *types* (prudential, conduct, AML, tax, data/privacy, market-infrastructure) were not considered? Did any mapping rely on prior-year or another-entity assumptions without re-verification?

**Step 7 — Verify-against-current instruction block.**
Output an explicit instruction that the user/professional must confirm each cited rule, threshold, and effective date against the official regulator source **as of the mapping date**, and that regulatory change since the cited source date invalidates the mapping.

## Output Format

### Regulatory Requirement Map
| # | Entity | Activity / Product | Jurisdiction | Regulator(s) | Framework / Obligation area | Triggering condition (verify) | Owner | Applicability confidence | Priority tier |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | [verify against current text] | | High/Med/Low | T1/T2/T3 |

### Applicability Rationale Log
| # | Why it applies (activity → trigger) | Threshold / condition | Source to verify | Counsel review needed? |
|---|---|---|---|---|

### Jurisdiction Coverage Summary
| Jurisdiction | Home/Host | Activities in scope | Marketing-only triggers? | Key regulators |
|---|---|---|---|---|

### Completeness Self-Audit
- Activities not yet mapped: …
- Jurisdictions possibly omitted (incl. marketing-only): …
- Regulator types not considered (prudential / conduct / AML / tax / privacy / market infra): …
- Mappings carried over from prior year/entity without re-verification: …

### Verify-Against-Current Instruction
> Confirm every cited regulation, section, threshold, and effective date against the current official source for the relevant regulator **as of [mapping date]**. Regulatory amendments since the source date may add, remove, or change obligations. Route all applicability determinations and legal interpretation to qualified compliance/legal counsel.

## Verification
- [ ] Every mapped requirement has a jurisdiction and named regulator(s).
- [ ] Every cited rule/threshold/date is marked "[verify against current text]" — none asserted as authoritative.
- [ ] Frameworks named generically and correctly; no invented rule numbers.
- [ ] Each mapping has an applicability rationale and a triggering condition.
- [ ] Owners assigned and requirements prioritized by severity × likelihood.
- [ ] Cross-border / marketing-only obligations explicitly considered.
- [ ] Completeness self-audit lists out-of-scope and unverified items.
- [ ] Low-confidence applicability items routed to counsel.

## False-Positive Prevention
| Overclaim risk | Guardrail |
|---|---|
| Asserting a specific rule number or threshold as fact | All citations/thresholds marked "[verify against current text]"; user must confirm against official source |
| Presenting the map as a legal applicability determination | Stated as scoping aid; legal interpretation routed to counsel; Low-confidence items flagged |
| Checkbox-compliance illusion (map looks complete = compliant) | Completeness self-audit forces naming of unmapped activities, jurisdictions, and regulator types |
| Over-reliance on prior-year / another-entity mapping | Must flag any carried-over mapping and re-verify against current facts and rule text |
| Scope omission of marketing-only or cross-border obligations | Jurisdiction lattice explicitly includes "marketed into" jurisdictions and host regulators |
| Treating one regulator as the whole picture | Regulator-type checklist (prudential/conduct/AML/tax/privacy/market infra) required in self-audit |
