---
title: "Organisational Accessibility Program — Maturity Baseline, Policy, Conformance Reports (VPAT/ACR), Risk-Tiered Audit Cadence, Procurement Gates, and Role-Based Training"
category: frontend-development/accessibility
description: "Design or assess an organisation-wide digital accessibility program rather than a single product audit: baseline maturity by dimension, write a policy with a named standard, owners and an exceptions route, produce Accessibility Conformance Reports (VPAT-based) that are backed by test evidence, set audit and regression cadence by risk tier, gate procurement on validated vendor ACRs, train by role, and track metrics that show whether barriers are actually being removed."
techniques:
  - ST-47
  - DS-32
  - DP-05
  - AG-12
difficulty: advanced
tags:
  - accessibility-program
  - vpat
  - accessibility-conformance-report
  - accessibility-policy
  - accessible-procurement
  - accessibility-training
  - wcag
  - customer-asking-for-vpat
  - make-whole-company-accessible
  - accessibility-compliance-plan
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
  - domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md
  - domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md
---

# Organisational Accessibility Program

**Objective:** Turn accessibility from a sequence of one-off audits into an operating
program — with a policy, owners, evidence-backed conformance reports, a testing cadence
sized to risk, procurement that does not buy new barriers, and training matched to roles
— and measure whether it is working.

**When to Use:**
- A customer, tender, or university buyer asks for a VPAT/ACR and the existing one is old,
  unsupported by testing, or does not exist.
- Leadership wants an accessibility plan after a complaint, demand letter, or new
  regulation (e.g. European Accessibility Act, ADA Title II rule, EN 301 549 in public
  tenders).
- Audits keep finding the same defects because nothing upstream changes.
- The organisation buys software for staff or the public without checking accessibility.
- **Not this prompt if** you need to **test one product** against WCAG — use
  `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md`; for the
  documents and slides the organisation publishes, use
  `frontend_accessibility_documents_slides.md`; for a general compliance-program gap
  analysis under a specific legal regime with counsel, use
  `domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md`. Running the
  tender itself is `domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md`
  — this prompt supplies its accessibility requirements and scoring.

## Inputs / Context

1. **Organisation profile**: sector, jurisdictions, customer types (public sector,
   education, consumers), headcount, products and digital channels.
2. **Obligations and pressures**: laws, contracts, tenders, complaints, demand letters.
3. **Current state**: existing policy, ACRs and their dates, last audits and results,
   defect backlog, CI checks, training delivered, procurement practice.
4. **People**: who owns accessibility today, and whether disabled employees or users are
   involved in testing and decisions.
5. **Budget and timeline constraints**.

## Method

1. **Baseline maturity by dimension (ST-47).** Rate each dimension of the W3C
   Accessibility Maturity Model (draft note) — Communications, Knowledge and Skills,
   Support, ICT Development Lifecycle, Personnel, Procurement, Culture — as Inactive,
   Launch, Integrate, or Optimize, citing evidence for each. Tiers are cumulative; aim the
   next 12 months at one level up where stakes are highest, not everywhere at once.
2. **Enumerate obligations (DS-32).** List each law, standard, and contract term with what
   it covers and what it requires (standard and level, reporting, deadlines). Flag every
   legal interpretation for counsel; this prompt does not give legal advice.
3. **Write the policy.** Scope (products, sites, documents, internal tools, procured ICT);
   the standard (normally WCAG 2.2 AA; EN 301 549 where EU public sector applies); roles and
   an executive owner; exceptions process with documented rationale and alternative access;
   a public accessibility statement with a feedback route and response time.
4. **Make conformance reports evidence-backed.** Use the ITI VPAT edition matching the
   buyer (508, EU, WCAG, or INT). Every criterion's conformance level (Supports, Partially
   Supports, Does Not Support, Not Applicable) cites the test: date, method (manual +
   assistive technology + automated), tester, scope, and known issues with remediation
   dates. Re-issue on each major release or at least annually.
5. **Set cadence by risk tier (DP-05).** Tier properties by reach and consequence:
   *Tier 1* (public transactional flows, customer-critical products) — automated checks in
   CI on every merge, expert manual audit each major release and at least annually,
   usability sessions with disabled participants yearly; *Tier 2* — automated in CI,
   manual audit every 1–2 years; *Tier 3* — automated monitoring, audit on change. The
   same tiering sets procurement gates.
6. **Gate procurement.** Require a current ACR for in-scope purchases; validate claims by
   spot-testing 3–5 key tasks for Tier 1 purchases; score accessibility in evaluation;
   put remediation commitments and timelines in the contract.
7. **Train by role.** Designers (contrast, focus, patterns), engineers (semantics, ARIA,
   testing), content authors (headings, alt text, documents), QA (AT testing),
   procurement (reading an ACR), support (handling barrier reports). Measure application
   (defects introduced per role), not attendance alone.
8. **Define metrics and review rhythm (AG-12).** Open barriers by severity and age;
   share of Tier 1 releases passing the gate; ACR currency; share of in-scope purchases
   with a validated ACR; median time to resolve user-reported barriers. Quarterly review
   by the executive owner.

## Output Format

```
# Accessibility program — [organisation]   Standard: [..]   Executive owner: [..]

## Maturity baseline
| Dimension | Level | Evidence | 12-month target |
## Obligations (for counsel review)
| Obligation | Applies to | Requires | Deadline | Status |
## Policy outline
scope · standard · roles · exceptions · statement & feedback route
## Conformance reports
| Product | VPAT edition | Last tested | Evidence basis | Known gaps | Re-issue by |
## Risk tiers and cadence
| Tier | Properties | Automated | Manual audit | User testing | Release gate |
## Procurement gate
## Training plan by role
## Metrics and targets
## 90-day plan
```

## Verification

- [ ] Each maturity rating cites evidence, not opinion.
- [ ] Obligations list names a deadline and is flagged for legal review.
- [ ] Every ACR claim is traceable to a dated test with method and scope.
- [ ] Every property is assigned a tier with a cadence and a release gate.
- [ ] Procurement requires validation for Tier 1 purchases, not only collection of ACRs.
- [ ] Training is role-specific with an applied-outcome measure.
- [ ] Metrics include age and resolution time of barriers, not just counts.

## False-Positive Prevention

1. **ACR as marketing.** "Supports" claimed without testing creates contractual and legal
   exposure when a buyer spot-tests; Partially Supports with a dated plan is safer and true.
2. **Overlays as compliance.** Third-party overlay widgets do not make inaccessible source
   conformant and are not a program.
3. **Automated scores as conformance.** Automated tools catch a minority of WCAG failures;
   a 100 Lighthouse score is not an ACR basis.
4. **Training hours as outcome.** Attendance does not show whether defects fell.
5. **Policy without an owner or exceptions route.** Exceptions then happen silently.
6. **Program built without disabled people.** No participation from disabled users or
   staff leaves the most important evidence out.
7. **Legal conclusions in a program plan.** Applicability and deadlines are counsel's call.

## Example Output

```
# Accessibility program — Tallis Learning (LMS SaaS, 1,200 staff; US universities + EU)
Standard: WCAG 2.2 AA; EN 301 549 for EU public tenders   Executive owner: CPO

Trigger: two university renewals require a current ACR; the 2022 ACR claims "Supports"
on 49 of 50 WCAG 2.1 A/AA criteria; a buyer spot-test found failures on 6 (1.3.1, 1.4.3,
2.1.1, 2.4.7, 3.3.1, 4.1.2).

## Maturity baseline
| Communications | Launch | statement exists, no feedback SLA | Integrate |
| Knowledge & Skills | Launch | one-off dev workshop 2023 | Integrate |
| ICT Dev Lifecycle | Inactive | no CI checks; audits only on request | Integrate |
| Procurement | Inactive | no ACR requested for 41 tools bought in 2025 | Launch |
| Personnel | Launch | 1 specialist, part-time | Integrate |
| Support | Launch | barrier reports routed as general tickets | Integrate |
| Culture | Launch | no disabled-user research | Launch+ (first study) |

## Conformance reports
| Learner app | VPAT INT edition (current ITI release) | re-test Nov 2026 | manual + NVDA/VoiceOver + axe | 6 known
  failures; fixes for 2.1.1 and 4.1.2 in Dec release | interim ACR now, re-issue Jan 2027 |

## Risk tiers and cadence
| 1 | learner app, assessment engine, checkout | axe in CI, blocking on new serious issues |
  expert audit per major + annual | 1 study/yr with 8 disabled participants | yes |
| 2 | admin console, marketing site | CI, non-blocking | every 18 months | — | serious only |
| 3 | internal tools | monthly scan | on change | — | no |

## Procurement gate
Tier 1 purchases (LMS plugins, video platform): current ACR + 5-task spot test + contract
remediation clause (critical issues fixed within 90 days). 3 of 41 existing tools are Tier 1 → test first.

## Training plan by role
Engineers 2×2 h + paired fixes; designers 2 h + contrast/focus review; content authors
1 h + template; procurement 1 h on reading an ACR; support 45 min on barrier triage.

## Metrics and targets (Q2 2027)
Open serious barriers in Tier 1: 64 → ≤15, none older than 90 days. ACR currency: 100% of
Tier 1 products tested within 12 months. Validated ACR for 100% of new Tier 1 purchases.
Median resolution of user-reported barriers: unknown → measured, target ≤30 days.

## 90-day plan
Interim honest ACR to both universities (week 2); CI checks on learner app (week 4);
policy approved (week 6); support triage tag + SLA (week 6); external audit booked (week 8).
```

## Techniques Used

- **ST-47 Capability Maturity Tiering** — maturity rated per dimension with a one-level, stakes-driven target.
- **DS-32 Regulatory Enumeration Pattern** — obligations listed with coverage, requirements, and deadlines for counsel.
- **DP-05 Stakes-Based Gate Policy** — risk tiers set audit cadence, release gates, and procurement validation.
- **AG-12 Quantitative Success Metrics** — barrier age, ACR currency, and resolution time as program health.

## Related Prompts

- `frontend_accessibility_wcag_audit.md` — the product-level audit that produces ACR evidence.
- `domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md` — counsel-led gap analysis against a legal regime.
- `domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md` — running the tender that the procurement gate plugs into.
