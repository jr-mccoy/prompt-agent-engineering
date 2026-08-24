---
title: "Technical Due Diligence Plan — Audit Technology, Team, Code, IP, Data, and Infrastructure Before You Commit"
category: business-strategy/research
description: "Build a technical due diligence plan for an acquisition, investment, partnership, or major procurement. Covers technology and architecture, team and knowledge concentration, code quality and operational signals, IP ownership and license exposure, data and regulatory risk, and infrastructure and lock-in — ending with a risk-prioritized remediation plan and a deliverable checklist. Counters the failure of a demo-driven yes that misses the debt, the key-person risk, and the IP landmines."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - due-diligence
  - technical-audit
  - acquisition
  - risk-assessment
  - investment
updated: "2026-06-18"
reasoning:
  styles: [analytic, structural, adversarial, risk_weighted]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: [structured, checklist]
  user_role: [investor, executive, founder, analyst, engineering_leader]
  mode: [audit, diagnose, plan]
related_prompts:
  - domain-business-strategy/research/competitor_teardown.md
  - domain-specialized-fields/ip/patent_landscape_scan.md
  - domain-business-strategy/research/research_company_deep_dive.md
---

# Technical Due Diligence Plan

**Objective:** Produce a technical due diligence plan for a high-stakes commitment — acquisition, investment, partnership, or major procurement — that audits the six dimensions where technical risk hides: technology and architecture, team and knowledge concentration, code quality and operations, IP, data and regulatory exposure, and infrastructure. The plan defines what to examine, what evidence to demand, what good and bad look like, and ends with a risk-prioritized remediation plan and a deliverable checklist. The aim is to replace a demo-driven impression with an evidence-driven verdict and a costed list of what you'd inherit.

**When to use:**
- Evaluating a target for acquisition or an investment with material technical risk.
- Vetting a partner whose technology you will depend on or integrate.
- A major procurement where vendor lock-in, scalability, or security determines viability.
- Pre-LOI scoping (what to ask for) or post-LOI deep diligence (what to verify).

**When NOT to use:**
- The deal is non-technical and technology is incidental.
- You need IP landscape analysis specifically — use `patent_landscape_scan.md` for FTO/whitespace; this plan covers IP only at the diligence level.
- You need a market or competitive read rather than a technical audit — use `competitor_teardown.md` or `research_company_deep_dive.md`.

**Audience:** Investors, corp-dev and M&A leads, CTOs and engineering leaders advising on deals, procurement leads, and founders evaluating a technical partner or acquisition.

---

## Inputs / Context

1. **The transaction.** Acquisition / investment / partnership / procurement, and the value at stake.
2. **The thesis.** Why this is attractive — the technical claim the deal rests on (scalable platform, proprietary tech, team, data asset).
3. **Access level.** What you can examine: code, repos, dashboards, contracts, people, or only management representations.
4. **Stage and scale.** Company maturity, user/revenue scale, regulatory environment.
5. **Deal-breakers.** Risks that, if found, kill or reprice the deal.
6. **Timeline.** How long you have to complete diligence.

---

## Constraints

### Must
- Audit all six dimensions: **technology/architecture, team, code quality, IP, data, infrastructure** — and tie each finding back to the deal thesis.
- For each dimension, specify the **evidence to demand** (artifact, access, or demonstration), not just questions to ask. A representation is not evidence.
- Distinguish **what was verified** from **what was represented** from **what could not be examined.** The unexaminable list is itself a risk finding.
- Surface **knowledge concentration / key-person risk** explicitly: who, if they left, would take undocumented critical knowledge.
- Assess **IP ownership chain**: who actually owns the code (contractors, prior employers, open-source obligations) and what license obligations attach.
- Assess **data risk**: PII inventory, retention, consent basis, regulatory exposure (GDPR/CCPA/sector rules), and whether the data asset is legally usable post-deal.
- Identify **single points of failure** and **vendor lock-in** in infrastructure, with the cost and time to remediate.
- End with a **risk-prioritized remediation plan**: each material finding scored by likelihood, impact, and cost-to-fix, with deal implications (proceed / reprice / condition / walk).

### Must Not
- Accept a demo or management representation as verification of an underlying technical claim.
- Score technology in the abstract; always relative to the thesis and the scale it must support.
- Treat "the code works" as "the code is maintainable, secure, and ownable" — these are separate findings.
- Ignore the team dimension because the technology looks good; key-person risk routinely outweighs code risk.
- Skip the IP and license audit because the product ships — license obligations and ownership gaps surface after close.
- Produce findings without remediation cost and deal implication; an unscored finding does not inform the decision.

---

## Instructions

1. **Anchor on the thesis and deal-breakers.** Restate the technical claim the deal rests on and the findings that would kill or reprice it. Diligence depth follows the thesis: spend most effort where the value and the risk concentrate.
2. **Plan the technology and architecture audit.** Examine architecture (coupling, scalability headroom, single points of failure), technical debt (where, how deep, what it blocks), and security posture (auth, data handling, known vulnerabilities, audit history). Evidence to demand: architecture docs, a code/repo walkthrough, recent security assessments, scalability test results.
3. **Plan the team audit.** Map key people, their roles, and knowledge concentration. Identify who holds undocumented critical knowledge, retention/flight risk (vesting, comp, tenure, sentiment), and the bus-factor for each critical system. Evidence: org chart, contribution history (commit/ownership data), retention terms, candid 1:1s where access allows.
4. **Plan the code quality and operations audit.** Assess test coverage, CI/CD and deploy frequency, incident history and MTTR, code review practice, and dependency health. Evidence: coverage reports, deploy logs, incident postmortems, repo metrics — not just a tour of the codebase.
5. **Plan the IP audit.** Trace ownership: was code written by employees (assigned), contractors (assignment clause?), or carried from prior employers? Inventory open-source dependencies and their license obligations (copyleft exposure, attribution, distribution triggers). Identify any patent exposure (infringement risk; for offensive IP value, route to `patent_landscape_scan.md`). Evidence: IP assignment agreements, contractor contracts, SBOM/license scan, OSS compliance records.
6. **Plan the data audit.** Inventory data assets, classify PII/sensitive data, document retention and deletion practice, identify the legal basis for collection and use (consent, contract, legitimate interest), and map regulatory exposure (GDPR, CCPA, HIPAA, sector rules). Determine whether the data asset is legally usable after the transaction. Evidence: data maps, privacy policies, processing records, DPA inventory.
7. **Plan the infrastructure audit.** Assess cloud architecture and spend, vendor lock-in (proprietary services, migration cost), single points of failure, disaster recovery and backups, and scaling cost curve. Evidence: cloud bills, infra-as-code, architecture diagrams, DR test records.
8. **Score and prioritize findings.** For each material finding: likelihood, impact, and cost-and-time to remediate. Separate verified findings from represented-but-unverified and from unexaminable. Rank by risk-weighted severity.
9. **Render deal implications.** For the top findings, state the implication: proceed as-is, reprice by [amount], condition close on [remediation], or walk. Summarize the residual risk you'd be accepting if you proceed.

---

## False-Positive Prevention

1. **Demo-as-verification.** Concluding the technology is sound because the demo worked. A demo shows the happy path; demand architecture, code, and operational evidence.
2. **Representation-as-evidence.** Recording management claims as findings. Tag every item verified / represented / unexaminable.
3. **Thesis-free scoring.** Rating "good architecture" in the abstract rather than against the scale and load the thesis requires.
4. **Code-works fallacy.** Treating a functioning product as proof of maintainability, security, and clean ownership. These are independent audits.
5. **Team-dimension neglect.** Passing the technology while missing that one undocumented engineer holds the critical system. Bus-factor is a first-class finding.
6. **IP-ownership assumption.** Assuming the company owns its code without tracing contractor assignments and prior-employer carryover, and without an OSS license scan.
7. **Copyleft blindness.** Missing a copyleft (e.g., GPL/AGPL) dependency whose obligations conflict with the intended business model.
8. **Data-usability gap.** Valuing a data asset without confirming the legal basis to use it post-transaction; consent collected for one purpose may not transfer.
9. **Lock-in underestimate.** Treating vendor lock-in as a footnote without costing the migration. Lock-in is a priced liability.
10. **Unscored findings.** Listing risks without likelihood, impact, remediation cost, and deal implication — leaving the decision-maker no basis to act.

---

## Output Format

```
# TECHNICAL DUE DILIGENCE PLAN — [target / counterparty]
Transaction: [acquisition / investment / partnership / procurement] | Value at stake: [...]
Thesis (technical claim deal rests on): [...]
Deal-breakers: [...]
Access level: [code / dashboards / contracts / people / representations only]

## Diligence by dimension
| Dimension | What to examine | Evidence to demand | Good looks like | Bad looks like |
|-----------|-----------------|--------------------|-----------------|----------------|
| Technology/architecture | [...] | [...] | [...] | [...] |
| Team / knowledge concentration | [...] | [...] | [...] | [...] |
| Code quality / operations | [...] | [...] | [...] | [...] |
| IP / licenses | [...] | [...] | [...] | [...] |
| Data / regulatory | [...] | [...] | [...] | [...] |
| Infrastructure / lock-in | [...] | [...] | [...] | [...] |

## Findings register
| # | Dimension | Finding | Status | Likelihood | Impact | Remediation cost/time | Deal implication |
|---|-----------|---------|--------|------------|--------|-----------------------|------------------|
| 1 | [...]     | [...]   | verified / represented / unexaminable | [...] | [...] | [...] | proceed / reprice / condition / walk |

## Unexaminable list (itself a risk)
- [what could not be verified, and why it matters]

## Risk-prioritized remediation plan
| Priority | Finding | Remediation | Owner | Cost | Time | Condition of close? |
|----------|---------|-------------|-------|------|------|---------------------|
| P1       | [...]   | [...]       | [...] | [...]| [...]| y/n                 |

## Deal verdict
- Recommendation: [proceed / reprice by X / condition on Y / walk]
- Residual risk if proceeding: [...]

## Deliverable checklist
- [ ] Architecture + scalability assessment
- [ ] Security posture + vuln review
- [ ] Team map + bus-factor + retention read
- [ ] Code quality + operational metrics
- [ ] IP ownership chain + OSS license scan
- [ ] Data inventory + regulatory usability opinion
- [ ] Infrastructure + lock-in + DR review
- [ ] Findings register scored
- [ ] Remediation plan with costs
- [ ] Deal implication per material finding
```

---

## Verification

- [ ] All six dimensions planned, each tied to the deal thesis.
- [ ] Evidence-to-demand specified per dimension (artifacts/access, not just questions).
- [ ] Every finding tagged verified / represented / unexaminable.
- [ ] Key-person / bus-factor risk surfaced.
- [ ] IP ownership chain and OSS license obligations audited.
- [ ] Data usability post-transaction assessed against regulatory exposure.
- [ ] Single points of failure and vendor lock-in costed.
- [ ] Findings scored on likelihood, impact, and remediation cost/time.
- [ ] Deal implication stated per material finding.
- [ ] Deliverable checklist included.
- [ ] No demo or representation accepted as verification.
- [ ] No unscored findings.
