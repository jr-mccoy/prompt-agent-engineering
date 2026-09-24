# Specialized Professional Fields: Real Estate, Trades, and Licensed-Field Guidance

> Part of the [Non-Coding Quick Start](../NON_CODING_QUICK_START.md) system.

This domain holds **seven decision prompts for working real-estate and trades
professionals** — and for serious individual buyers and small investors — plus the
cross-field guidance, disclaimers and templates below for any field with licensing,
liability or jurisdiction constraints.

The prompts sit on the **commercial, non-legal side** of the work: what a house is
worth, what an offer exposes a buyer to, whether a rental pays, what an inspection
report means, whether to bid, what the bid is, and how to price a change. They do
not draft contracts, give title opinions, or make code, structural, legal, tax or
licensing determinations; those are routed to the licensed professional and, for
legal drafting, to [`domain-legal/`](../domain-legal/).

> **Moved (coverage Wave 2):** the domain's two earlier prompts now live in their
> subject home — `ip/patent_landscape_scan.md` →
> [`domain-legal/ip/legal_patent_landscape_scan.md`](../domain-legal/ip/legal_patent_landscape_scan.md);
> `legal/legal_research_plan.md` →
> [`domain-legal/research/legal_research_plan.md`](../domain-legal/research/legal_research_plan.md).
> Field-specific *writing* prompts (24 `domain_writing_*.md` files) stay in
> [`domain-professional-writing/domain-specific/`](../domain-professional-writing/domain-specific/).

## The prompts

### [`real-estate/`](real-estate/README.md) (4) — prefix `realestate_`
| File | Use |
|---|---|
| [`realestate_comparative_market_analysis.md`](real-estate/realestate_comparative_market_analysis.md) | Comp screen, adjustment grid with net/gross limits, weighted value range — from sales the user supplies |
| [`realestate_buyer_offer_strategy.md`](real-estate/realestate_buyer_offer_strategy.md) | Offer packages priced in worst-case cash: escalation cap, appraisal gap, contingencies, reserve floor |
| [`realestate_rental_property_underwriting.md`](real-estate/realestate_rental_property_underwriting.md) | NOI, cap rate, DSCR, cash-on-cash, reserves and a stress test with a traffic-light verdict |
| [`realestate_inspection_report_triage.md`](real-estate/realestate_inspection_report_triage.md) | Safety / material defect / maintenance / not inspected, routed to licensed specialists inside the contingency window |

### [`trades/`](trades/README.md) (3) — prefix `trades_`
| File | Use |
|---|---|
| [`trades_bid_no_bid_decision.md`](trades/trades_bid_no_bid_decision.md) | Gates (license, capacity, cash on real days-to-pay), anchored scores, expected value, kill signal |
| [`trades_bid_estimate_with_contingency.md`](trades/trades_bid_estimate_with_contingency.md) | Takeoff, allowances, unknowns register, contingency sized to named unknowns |
| [`trades_change_order_pricing_notice.md`](trades/trades_change_order_pricing_notice.md) | Price a mid-job change under the contract's terms and ask the owner for a dated decision |

### Quick routing

| You're saying | Use |
|---|---|
| "What's this house worth?" / "where should we list?" | `real-estate/realestate_comparative_market_analysis.md` |
| "Multiple offers — should we escalate or waive the appraisal?" | `real-estate/realestate_buyer_offer_strategy.md` |
| "Does this duplex actually cash-flow?" | `real-estate/realestate_rental_property_underwriting.md` |
| "The inspection report is 40 pages and the clock is running" | `real-estate/realestate_inspection_report_triage.md` |
| "Should we even bid this job?" | `trades/trades_bid_no_bid_decision.md` |
| "What's my number, and how much contingency?" | `trades/trades_bid_estimate_with_contingency.md` |
| "We opened the floor and found rot" / "the owner wants one more thing" | `trades/trades_change_order_pricing_notice.md` |

---

## When This Domain Applies

### Trigger Phrases

Route to this domain when the request mentions:

| Category | Trigger Phrases |
|----------|----------------|
| **Real Estate (non-legal)** | "comps", "CMA", "list price", "offer", "escalation clause", "appraisal gap", "cap rate", "rental property", "inspection report" |
| **Trades/Construction** | "bid", "estimate", "takeoff", "contingency", "allowance", "change order", "should we bid" |
| **Legal** | Route to [`domain-legal/`](../domain-legal/) — contracts, purchase agreements, title, zoning, leases |
| **Finance** | Route to [`domain-finance/`](../domain-finance/) — its own top-level domain |
| **Marketing/Sales** | Route out: deals, pipeline, customer accounts and support → [`domain-sales-customer/`](../domain-sales-customer/); marketing strategy → [`domain-business-strategy/go-to-market/`](../domain-business-strategy/go-to-market/); copy and campaigns → `domain-agentic-resources/skills/marketing/` |
| **Other Professional** | Field-specific writing → [`domain-professional-writing/domain-specific/`](../domain-professional-writing/domain-specific/); guidance below |

### User Personas

| Persona | Typical Needs |
|---------|--------------|
| **Real Estate Agents** | CMAs, offer strategy for buyer clients, inspection-response planning |
| **Buyers and Small Investors** | Offer packages they can afford to have go wrong; rental underwriting |
| **Contractors and Trade Subs** | Bid/no-bid, estimates with defensible contingency, change orders |
| **Other licensed professionals** | The disclaimers, document framework and templates below |

### Out of Scope

- **Actual legal, tax, appraisal or licensing determinations** — these prompts
  structure decisions and route the licensed questions
- **Contract drafting, title opinions, zoning analysis** → `domain-legal/`
- **Clinical healthcare** → domain-healthcare-clinical
- **Academic research** → domain-research-academic

---

## Domain-Specific Considerations

### What Makes Specialized Fields Unique

Specialized field prompts operate in environments where:

1. **Regulatory Requirements** - Documents must meet legal/professional standards
2. **Professional Liability** - Errors can create legal or financial exposure
3. **Industry Terminology** - Precise language with specific meanings
4. **Client Communication** - Translating expertise for non-specialists
5. **Documentation Standards** - Specific formats required
6. **Ethical Constraints** - Professional codes of conduct apply
7. **Licensing Implications** - Some advice can only come from licensed professionals

### The Professional Field Difference

| Dimension | General Content | Professional Field Content |
|-----------|-----------------|---------------------------|
| **Language** | Accessible | Precise, sometimes technical |
| **Format** | Flexible | Often standardized/required |
| **Liability** | Low stakes | Professional exposure |
| **Review** | Optional | Often mandatory |
| **Compliance** | N/A | Regulatory requirements |
| **Authority** | N/A | Licensed professional must verify |

### Critical Success Factors

1. **Know the Limits** - AI assists but doesn't replace licensed professionals
2. **Use Correct Terminology** - Industry terms have precise meanings
3. **Follow Standards** - Required formats exist for good reasons
4. **Document Clearly** - Ambiguity creates liability
5. **Disclaim Appropriately** - Clear about what this is and isn't
6. **Stay Current** - Regulations change; verify against current requirements

### Common Failure Modes

| Failure | Example | Prevention |
|---------|---------|------------|
| **Overstepping scope** | Providing actual legal advice | Frame as document assistance |
| **Wrong terminology** | Mixing up legal/financial terms | Field-specific glossary check |
| **Outdated information** | Referencing old regulations | Note need to verify currency |
| **Missing disclaimers** | No "not legal advice" note | Include appropriate disclaimers |
| **Generic templates** | Same format for all fields | Field-specific customization |
| **Ignoring jurisdiction** | US advice for UK situation | Specify jurisdiction limitations |

---

## Universal Principles for Specialized Fields

### The Professional Document Framework

**Every specialized field document should:**

1. **State Its Purpose Clearly**
   - What this document is for
   - What decisions it supports
   - What it does NOT constitute (e.g., "not legal advice")

2. **Use Appropriate Terminology**
   - Industry-standard terms
   - Defined when necessary for non-specialists
   - Consistent throughout

3. **Follow Field Standards**
   - Required format elements
   - Regulatory compliance
   - Professional conventions

4. **Include Appropriate Caveats**
   - Limitations of the analysis
   - Need for professional verification
   - Jurisdiction/context limitations

5. **Enable Action**
   - Clear next steps
   - Who needs to do what
   - Timeline if relevant

### Confidence and Disclaimers

```markdown
## Standard Disclaimers by Field

**Legal Documents:**
"This document is for informational purposes only and does not constitute legal advice.
Please consult with a licensed attorney in your jurisdiction before taking action based
on this information."

**Financial Analysis:**
"This analysis is for informational purposes only and does not constitute investment
advice or a recommendation to buy, sell, or hold any security. Past performance does
not guarantee future results. Consult a licensed financial advisor for personal advice."

**Real Estate:**
"This information is believed to be accurate but is not guaranteed. Property
conditions, market data, and regulations may change. Work with a licensed real
estate professional and conduct appropriate due diligence."

**Construction/Trades:**
"This estimate is preliminary and subject to change based on site conditions,
material costs, and project specifications. A formal contract with detailed
scope of work should be executed before work begins."

**Accounting/Tax:**
"This information is general in nature and does not constitute tax or accounting
advice. Tax laws vary by jurisdiction and individual circumstances. Consult a
licensed CPA or tax professional for advice specific to your situation."
```

---

## Field-Specific Guidance

### Quick Reference by Field

| Field | Key Considerations | Sample Prompts |
|-------|-------------------|----------------|
| **Legal** | Jurisdiction matters, attorney review required, precise terminology | `domain_writing_attorney_discovery.md` |
| **Finance** | Not investment advice, individual circumstances vary, disclosures required | `domain_writing_financial_advisor_report.md`, `domain_writing_cpa_tax_strategy.md` |
| **Trades/Construction** | Site conditions can change estimates, permits may be required, contingency sized to named unknowns | This domain: `trades/`; writing: `domain_writing_contractor_remodel.md`, `domain_writing_hvac_estimate.md`, `domain_writing_electrician_panel.md` |
| **Real Estate** | Market data changes rapidly, state regulations vary, due diligence required | This domain: `real-estate/`; writing: `domain_writing_realtor_listing.md` |
| **Marketing/Sales** | Audience targeting, conversion metrics, campaign tracking | `domain_writing_marketing_campaign.md`, `domain_writing_sales_strategy.md` |
| **Healthcare-Adjacent** | Not medical advice, professional oversight required | `domain_writing_veterinarian_surgery.md`, `domain_writing_dentist_treatment_plan.md` |

> **Note:** `domain_writing_*` prompts are in `domain-professional-writing/domain-specific/`; `real-estate/` and `trades/` are in this domain.

---

## Field Guides

Comprehensive domain-specific prompt engineering guides:

| Field Guide | Location | Purpose |
|-------------|----------|---------|
| Finance & Economics | [`../domain-finance/field_guide.md`](../domain-finance/field_guide.md) | Financial analysis, investment, risk assessment (now its own top-level domain) |
| Psychology & Behavioral Science | [`../domain-psychology/field_guide.md`](../domain-psychology/field_guide.md) | Clinical research, assessment, therapeutic techniques (now its own top-level domain) |

---

## Prompts in This Repository

The seven prompts are listed under [The prompts](#the-prompts) above. The field
writing prompts (24) live in
[`domain-professional-writing/domain-specific/`](../domain-professional-writing/domain-specific/)
as `domain_writing_{field}.md` — e.g. `domain_writing_contractor_remodel.md`,
`domain_writing_hvac_estimate.md`, `domain_writing_realtor_listing.md` — and are
the document-writing step after the decisions made here.

---

## Templates

### Template 1: Professional Services Proposal

```markdown
# [Service Type] Proposal

**Prepared for:** [Client Name]
**Prepared by:** [Professional Name, Credentials]
**Date:** [Date]
**Valid Until:** [Expiration Date]

---

## Scope of Services

### Services Included

1. **[Service 1]**
   - Description: [What's included]
   - Deliverables: [Specific outputs]
   - Timeline: [When completed]

2. **[Service 2]**
   - Description: [What's included]
   - Deliverables: [Specific outputs]
   - Timeline: [When completed]

[Continue for all services]

### Services NOT Included

The following are explicitly excluded from this engagement:
- [Exclusion 1]
- [Exclusion 2]

---

## Investment

| Service | Fee |
|---------|-----|
| [Service 1] | $[Amount] |
| [Service 2] | $[Amount] |
| **Total** | **$[Amount]** |

**Payment Terms:**
- [Deposit requirements]
- [Payment schedule]
- [Accepted methods]

**Additional Costs (if applicable):**
- [Expense category]: [How billed]

---

## Timeline

| Phase | Activities | Duration | Completion |
|-------|------------|----------|------------|
| [Phase 1] | [Activities] | [Time] | [Date] |
| [Phase 2] | [Activities] | [Time] | [Date] |

---

## Client Responsibilities

To complete this engagement, we require:
- [Item/information 1]
- [Item/information 2]
- [Access/approval/decision by date]

---

## Terms and Conditions

[Standard terms or reference to separate document]

---

## Authorization

To proceed, please sign below:

Client Signature: ___________________________ Date: ___________
Print Name: ___________________________

---

## Disclaimer

[Appropriate professional disclaimer for the field]
```

### Template 2: Client Communication (Technical to Non-Technical)

```markdown
# [Topic Summary]

**To:** [Client Name]
**From:** [Professional Name]
**Date:** [Date]
**Re:** [Subject]

---

## The Bottom Line

[One paragraph summary: what happened, what it means for them, what they need to do]

---

## What This Means for You

**In Plain Terms:**
[Explanation without jargon - what the client actually cares about]

**Specifically:**
- [Implication 1 for them]
- [Implication 2 for them]

---

## What You Need to Do

1. **[Action 1]** - by [Date]
   - [Details if needed]

2. **[Action 2]** - by [Date]
   - [Details if needed]

---

## The Details (For Reference)

[Technical details for those who want them - can be skipped]

### [Technical Section 1]
[Explanation]

### [Technical Section 2]
[Explanation]

---

## Questions?

[How to reach you]
[Offer to explain further]

---

*[Appropriate professional disclaimer]*
```

### Template 3: Estimate/Quote

```markdown
# [Service/Project] Estimate

**Estimate #:** [Number]
**Prepared for:** [Client Name]
**Prepared by:** [Company/Professional]
**Date:** [Date]
**Valid for:** [Days] days

---

## Project Overview

**Description:**
[Brief description of the work]

**Location/Scope:**
[Where/what the work covers]

---

## Cost Breakdown

### Labor

| Task | Hours | Rate | Amount |
|------|-------|------|--------|
| [Task 1] | [Hrs] | $[Rate] | $[Amount] |
| [Task 2] | [Hrs] | $[Rate] | $[Amount] |
| **Labor Subtotal** | | | **$[Amount]** |

### Materials

| Item | Quantity | Unit Price | Amount |
|------|----------|------------|--------|
| [Material 1] | [Qty] | $[Price] | $[Amount] |
| [Material 2] | [Qty] | $[Price] | $[Amount] |
| **Materials Subtotal** | | | **$[Amount]** |

### Other Costs

| Item | Amount |
|------|--------|
| [Permits/fees] | $[Amount] |
| [Equipment rental] | $[Amount] |
| **Other Subtotal** | **$[Amount]** |

---

## Total Estimate

| Category | Amount |
|----------|--------|
| Labor | $[Amount] |
| Materials | $[Amount] |
| Other Costs | $[Amount] |
| **Subtotal** | **$[Amount]** |
| [Tax if applicable] | $[Amount] |
| **TOTAL** | **$[Amount]** |

---

## Assumptions and Conditions

This estimate is based on:
- [Assumption 1 - e.g., normal site conditions]
- [Assumption 2 - e.g., specified materials available]
- [Assumption 3 - e.g., client provides access]

This estimate does NOT include:
- [Exclusion 1]
- [Exclusion 2]

---

## Timeline

**Estimated Start:** [Date or "Upon approval"]
**Estimated Completion:** [Duration or date]
**Schedule depends on:** [Factors - weather, permits, etc.]

---

## Payment Terms

[Deposit]: $[Amount] due upon acceptance
[Progress payments]: [Schedule]
[Final payment]: Due upon completion

---

## To Accept This Estimate

[Acceptance instructions]

Client Signature: ___________________________ Date: ___________

---

*This estimate is valid for [X] days. Prices may change after expiration. This estimate does not constitute a contract. A formal agreement will be provided upon acceptance.*
```

---

## Worked Example

### Scenario: Contractor Creating Project Estimate

**User says:** "I need to create an estimate for a kitchen renovation project"

**Step 1: Classification**

- Task Type: CREATE
- Domain: Specialized Fields (Trades/Construction)
- Specific Type: Project estimate

**Step 2: Context Gathering**

**Need to understand:**
- Scope of renovation (full gut? cosmetic update?)
- Location (affects permits, labor rates)
- Materials (client preferences, budget level)
- Timeline requirements
- Access to site (has assessment been done?)

**Step 3: Build Professional Estimate Prompt**

```markdown
# Kitchen Renovation Estimate

**Objective:** Create a professional estimate for kitchen renovation

## Project Context

**Client:** [Name]
**Property:** [Address]
**Site Visit Date:** [Date]

**Scope:**
- [ ] Full gut renovation
- [ ] Cabinet replacement only
- [ ] Countertop/appliance update
- [ ] Cosmetic refresh (paint, hardware, fixtures)

**Kitchen Details:**
- Square footage: [Size]
- Current condition: [Description]
- Layout changes: [Yes/No - if yes, describe]

## Materials Specification

**Cabinets:**
- Style: [Stock / Semi-custom / Custom]
- Material: [Laminate / Wood / etc.]
- Linear feet: [Amount]

**Countertops:**
- Material: [Laminate / Granite / Quartz / etc.]
- Square feet: [Amount]
- Edge profile: [Standard / Upgraded]

**Appliances:**
- [ ] Client providing
- [ ] Contractor providing - Budget: $[Amount]
- List: [Appliances to be installed]

**Fixtures:**
- Sink: [Type, material]
- Faucet: [Type]
- Lighting: [Fixtures needed]

**Flooring (if included):**
- Material: [Type]
- Square feet: [Amount]

## Labor Components

**Demo:**
- Removal of existing cabinets, counters, flooring
- Estimated hours: [Hours]

**Rough Work (if layout changes):**
- Electrical: [Scope]
- Plumbing: [Scope]
- Permit required: [Yes/No]

**Installation:**
- Cabinets: [Hours estimate]
- Countertops: [Installation method]
- Appliances: [Hook-up requirements]

**Finishing:**
- Painting: [Scope]
- Trim/molding: [Scope]
- Final touches: [Scope]

## Estimate Requirements

**Include:**
- Detailed line-item breakdown (labor and materials separate)
- Assumptions clearly stated
- Timeline with milestones
- Payment schedule
- What's NOT included
- Professional disclaimer

**Format:**
- Client-friendly summary at top
- Detailed breakdown available
- Signature/acceptance section

**Output should be suitable for:**
- Presenting to homeowner
- Converting to contract after acceptance
- Complying with [state] contractor requirements

## Quality Criteria

- [ ] All major cost categories covered
- [ ] Contingency/buffer included (typically 10-15%)
- [ ] Timeline realistic for scope
- [ ] Assumptions stated (so changes trigger change orders)
- [ ] Professional formatting
- [ ] Appropriate disclaimer
```

---

## Anti-Patterns for Specialized Fields

### Mistake 1: Providing Actual Professional Advice

**Problem:** Crossing from document assistance to professional advice

**Bad:**
```
"You should definitely include that clause in your contract because it will protect you from..."
(This is legal advice, not document assistance)
```

**Good:**
```
"Here's a draft clause addressing that concern. Have your attorney review this and advise whether it's appropriate for your specific situation and jurisdiction."
(This is document assistance with appropriate caveat)
```

---

### Mistake 2: Using Wrong Terminology

**Problem:** Mixing up industry-specific terms

**Bad:**
```
"The income statement shows the company's worth..."
(Income statement shows profit/loss, not worth - that's the balance sheet)
```

**Good:**
```
"The balance sheet reflects the company's net worth (assets minus liabilities), while the income statement shows profitability over a period..."
(Correct terminology)
```

---

### Mistake 3: Missing Jurisdiction/Context

**Problem:** Ignoring geographic or situational variations

**Bad:**
```
"For your real estate transaction, you'll need to..."
(Without knowing state/country, requirements vary dramatically)
```

**Good:**
```
"Real estate transaction requirements vary significantly by state. In [State], typical requirements include... Please verify these requirements with a licensed real estate attorney in your jurisdiction."
(Acknowledges variation, suggests verification)
```

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════════════════╗
║           SPECIALIZED FIELDS QUICK REFERENCE                               ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  ALWAYS INCLUDE:                                                          ║
║  □ Appropriate professional disclaimer                                    ║
║  □ Recommendation to verify with licensed professional                   ║
║  □ Jurisdiction/context limitations                                       ║
║  □ "For informational purposes" framing                                  ║
║                                                                           ║
║  PROFESSIONAL BOUNDARIES:                                                 ║
║  ✓ DO: Assist with document drafting and formatting                      ║
║  ✓ DO: Explain general concepts and terminology                          ║
║  ✓ DO: Provide templates and structures                                  ║
║  ✗ DON'T: Provide legal, financial, or medical advice                   ║
║  ✗ DON'T: Guarantee outcomes or compliance                               ║
║  ✗ DON'T: Replace licensed professional review                          ║
║                                                                           ║
║  BY FIELD:                                                                ║
║                                                                           ║
║  LEGAL:                                                                   ║
║  • Precise terminology matters                                            ║
║  • Jurisdiction critical                                                  ║
║  • Attorney review required for anything binding                         ║
║                                                                           ║
║  FINANCE:                                                                 ║
║  • Not investment advice                                                  ║
║  • Past performance ≠ future results                                     ║
║  • Individual circumstances vary                                          ║
║                                                                           ║
║  TRADES/CONSTRUCTION:                                                     ║
║  • Site conditions can change estimates                                   ║
║  • Permits may be required                                                ║
║  • Include contingency buffer                                             ║
║                                                                           ║
║  REAL ESTATE:                                                             ║
║  • Market data changes rapidly                                            ║
║  • State regulations vary significantly                                   ║
║  • Due diligence always required                                          ║
║                                                                           ║
║  PROMPTS AVAILABLE:                                                       ║
║  real-estate/ (4) · trades/ (3) in this domain                            ║
║  domain-professional-writing/domain-specific/ (24 professional guides)   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [NON_CODING_QUICK_START.md](../NON_CODING_QUICK_START.md) | Universal non-coding principles |
| [domain-professional-writing/domain-specific/](../domain-professional-writing/domain-specific/) | 24 professional field prompts |
| [domain-product-management/](../domain-product-management/) | General business documents |
| [PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) | Quality tier definitions |
| [domain-legal/](../domain-legal/) | Contracts, real-estate legal drafting, research |
| [client-services-studio/](../client-services-studio/README.md) | Engagement pipeline for trades and services, with trade verticals |

---

*Document Version: 2.0*
*Created: 2026-01-26 · Rebuilt around real-estate and trades prompts: 2026-09-24*
*Domain: Specialized Professional Fields*
