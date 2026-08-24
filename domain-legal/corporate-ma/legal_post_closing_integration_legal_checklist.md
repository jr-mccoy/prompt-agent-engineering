---
title: "Post-Closing Legal Integration Checklist (30/60/90-Day)"
category: legal/corporate-ma
description: "Build a phased post-closing legal integration plan for the buyer: 30/60/90-day tasks across assignments, third-party consents, employment, IP, regulatory filings (HSR / CFIUS / foreign), entity housekeeping, IT/privacy, and contract migration, each with owner, dependency, and dependency-on-deal-structure trigger."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - m-and-a
  - corporate
  - post-closing
  - integration
  - regulatory
updated: "2026-05-11"
related_prompts:
  - domain-legal/corporate-ma/legal_board_resolution_drafter.md
  - domain-legal/corporate-ma/legal_due_diligence_findings_memo.md
  - domain-legal/corporate-ma/legal_disclosure_schedule_drafter.md
  - domain-legal/contracts-transactional/legal_msa_drafter.md
---

**Purpose:** Translate the closing checklist into a 30/60/90-day post-closing legal integration plan. Each task has an owner, dependencies, deal-structure trigger (asset vs. stock vs. merger), and target completion date. Output drives status tracking through the integration period and surfaces any items missed at closing.

**When to use:** Buyer's first integration meeting after signing; closing-week prep; week-one post-closing legal kickoff; mid-integration status review.

---

## Your Input

- **Deal structure:** [Asset / stock / forward merger / reverse triangular merger / 338(h)(10) / 336(e) / F-reorg / drop-down]
- **Governing law of definitive agreement:** [Default: Delaware]
- **Acquired entity state of formation/incorporation:** [State]
- **Industry:** [Industry — drives regulatory filings, licensing transfers]
- **Posture:** Buyer
- **Closing date:** [Date]
- **Target legal name pre-close, post-close (if renamed):** [Names]
- **Jurisdictions of operation:** [States, foreign countries]
- **Material consents procured pre-close vs. deferred to post-close:** [Inventory]
- **Outstanding HSR / CFIUS / foreign-investment / industry-regulator filings or post-close notices:** [List with deadlines]
- **Employee transition mechanic:** [Continuation of employment (stock deal / merger) / termination + rehire (typical for asset deal) / TUPE-style transfer in applicable foreign jurisdictions]
- **Equity treatment at closing:** [Cash-out / acceleration / rollover / replacement awards]
- **D&O tail bound:** [Yes / no, term, carrier]
- **R&W insurance bound:** [Yes / no]
- **Transition services agreement in place:** [Yes / no, term, scope]
- **Known open items from closing checklist:** [List]

---

## Constraints

**Must:**
- Organize by **Day 1 (closing day)**, **Days 2–30**, **Days 31–60**, **Days 61–90**, **>90 days**.
- Each task includes: owner (legal, HR, finance, IT, ops, external counsel), dependency (predecessor task), deal-structure trigger (when does this task apply?), and target completion date.
- Address the full integration legal scope: (a) entity housekeeping, (b) third-party consents and assignment completions, (c) employment transitions, (d) benefits and equity, (e) IP transfers and recordations, (f) regulatory filings and notices, (g) IT / privacy / cybersecurity, (h) real estate, (i) contracts migration, (j) banking and treasury, (k) insurance, (l) tax filings, (m) D&O / E&O / R&W policy administration, (n) earnout governance (if applicable).
- Differentiate **asset deal** tasks (assignments-and-consents, bulk-sale notices, sales-tax clearance certificates, IP recordations, employee termination + rehire) from **stock deal / merger** tasks (officer/director changes, charter/bylaws updates, consents triggered by change-of-control, employee continuity).
- Cite specific regulatory frameworks and post-closing windows where applicable: HSR Item 4(c)/(d) closing certifications, CFIUS post-clearance reporting under 31 C.F.R. Part 800 [CITE: confirm], FCC / FERC / state insurance / banking transfer filings, foreign-investment notifications (e.g., UK NSI Act, EU FSR, Germany AWG), GDPR data-controller updates, HIPAA BAA updates.
- Address D&O tail policy issuance and runoff coverage administration.
- Address R&W insurance policy administration: notice-of-claim procedures, retention erosion tracking, exclusion catalog.
- Surface earnout governance: agreed acceleration triggers, accounting methodology, dispute mechanism activation.
- For asset deals, address successor-liability mitigations: bulk-sales notices where required, sales-tax clearance certificates, environmental Phase I update if needed for warranty triggers.

**Must Not:**
- Invent regulatory deadlines, statutory provisions, or post-closing notice requirements. Use `[CITE: confirm]` and `[NEED: confirm jurisdiction-specific deadline]` placeholders.
- Treat asset and stock deals as interchangeable. Many tasks are deal-structure-specific (assignment-and-consent inventory is core to asset deals; rarely needed for reverse triangular mergers).
- Omit Day-1 tasks (banking signatory changes, insurance certificate updates, authorized-officer changes).
- Use a generic "complete consents" task without itemizing the inventory.
- Insert "consult counsel" disclaimers — substantive guardrails only.
- Skip dependencies — a task that depends on charter amendment cannot precede the filing.

---

## Instructions

1. **Header.** Project name, target, buyer, deal structure, closing date, integration plan version.
2. **Day 1 (closing day) tasks.** What must be done on closing day or by end of closing week: banking signatories, insurance updates, authorized officers, board composition, secretary's certificate, IRS notifications (e.g., §338(h)(10) elections), HSR closing certifications if applicable, employee communications.
3. **Days 2–30 tasks.** Immediate post-closing: open assignment-and-consent items, payroll/benefits transition, IT cutover or integration, equity plan administration, charter/bylaws amendments, foreign qualification filings, IP recordations.
4. **Days 31–60 tasks.** Material contract migration, customer notification waves, vendor consents, sales-tax registrations in new states, real-estate landlord consents, regulatory transfer applications.
5. **Days 61–90 tasks.** Long-tail regulatory filings, post-closing audits, equity grant integration, restrictive-covenant integration, integration of compliance programs (FCPA, OFAC, privacy), TSA exit planning.
6. **>90 days.** Long-tail items: §338(h)(10) tax return filings, R&W policy retention erosion review, earnout governance through measurement period, indemnity claim windows tracking, post-integration audits, dissolution of acquired-entity shell if collapsed.
7. **Owner and dependency table** for the full inventory.

---

## Output Format

```markdown
# Post-Closing Legal Integration Plan
**Project:** [CODE NAME]   **Buyer:** [BUYER]   **Target:** [TARGET]
**Deal Structure:** [Structure]   **Closing Date:** [Date]
**Plan Version:** 1.0   **Date Issued:** [Date]

## Summary by Phase
| Phase | # Tasks | Critical Path Items |
|---|---|---|
| Day 1 | [N] | Banking signatories, authorized officers, D&O tail bind confirmation, payroll cutover, HSR / CFIUS post-close notices |
| Days 2–30 | [N] | Material consents not procured pre-close, equity plan administration, IT cutover |
| Days 31–60 | [N] | Customer/vendor notifications, foreign qualifications, sales-tax registrations |
| Days 61–90 | [N] | Regulatory transfer approvals, restrictive-covenant integration, TSA exit |
| >90 days | [N] | §338(h)(10) returns, earnout measurement, indemnity windows |

---

## Day 1 (Closing Day)
| Task | Owner | Trigger | Dependency | Target |
|---|---|---|---|---|
| File certificate of merger with Secretary of State of [Delaware] | External counsel | Merger | Closing | Day 1 |
| Confirm D&O tail policy bound — receive binder and policy | Buyer GC + broker | All | D&O tail purchase resolution | Day 1 |
| Confirm R&W policy bound — receive binder, retention, exclusions | Buyer GC + broker | If R&W | Pre-bind underwriting | Day 1 |
| Change banking signatories at target's banks; revoke prior; add new | Buyer treasury | Stock / merger | Closing; resolutions adopted | Day 1 |
| File §338(h)(10) election Form 8023 [CITE: confirm filing deadline — generally 8.5 months after acquisition] | Tax counsel | 338(h)(10) | Closing | Per IRS deadline |
| Confirm HSR closing certification, if required | Outside antitrust counsel | HSR-cleared deal | Closing | Within HSR window |
| Issue closing communication to employees | HR + GC | All | Final closing notice | Day 1 |
| Issue closing notice to top [N] customers / suppliers per contract requirements | Commercial team + GC | All; tailor for COC vs. assignment notices | Closing | Day 1 |
| Update authorized-officer records and corporate registers | GC / corporate secretary | All | Resolutions | Day 1 |
| Confirm payroll cutover (continuation vs. new employer) | HR | Asset deal triggers cutover; stock deal continues existing payroll | Closing | Day 1 |
| Issue insurance certificates naming buyer as insured | Risk management | All | Closing | Day 1–7 |

## Days 2–30
| Task | Owner | Trigger | Dependency | Target |
|---|---|---|---|---|
| Complete and record open assignment-and-consent items | GC + commercial | Asset deal — primary; stock deal — for COC-triggered consents | Inventory from disclosure schedule | Day 30 |
| Record IP assignments (patents — USPTO; trademarks — USPTO; copyrights — USCO; domains — registrar transfers) | IP counsel | Asset deal; some stock-deal recordations | Closing IP assignments executed | Day 30 |
| File foreign qualifications for surviving entity in states where it does business | Corporate counsel | All | Closing | Day 30 |
| Update EIN where new entity formed; or notify IRS of name change if applicable | Tax | Depends on structure | Closing | Day 30 |
| Equity plan: cancel cashed-out awards; issue replacement / rollover awards; file Form 3921/3922 if applicable; update §16 filings for public buyer | HR + securities counsel | All | Closing | Day 30 |
| §83(b) elections for new restricted stock grants issued in rollover | Tax + HR | If rollover with restricted stock | Grant date | 30 days post-grant |
| Update privacy notices and data-processing addenda to reflect new controller | Privacy counsel | All | Closing | Day 30 |
| HIPAA BAAs (if applicable industry) updated to reflect new covered entity / business associate | Healthcare counsel | Healthcare industry | Closing | Day 30 |
| Update OFAC / sanctions screening to integrate target customer/vendor base | Compliance | All | Closing | Day 30 |
| Bulk-sale notices to taxing authorities where required (asset deals in jurisdictions with bulk-sales tax laws) | Tax | Asset deal in applicable states | Closing | Per jurisdiction deadline (often pre-close in some states) |
| Apply for sales-tax clearance certificates from selling jurisdictions | Tax | Asset deal | Closing | Day 30 |

## Days 31–60
| Task | Owner | Trigger | Dependency | Target |
|---|---|---|---|---|
| Customer notification wave 2 — non-top-tier accounts | Commercial | All | Day 1 wave completed | Day 45 |
| Vendor consents and contract migrations (anti-assignment clauses) | Procurement + GC | Asset deal primarily | Inventory | Day 60 |
| Sales-tax registrations in new states (post-Wayfair nexus inherited) | Tax | All | Closing | Day 60 |
| Real estate: landlord consents to assignment (asset deal) or change-of-control notices (stock deal) | Real estate counsel | All | Lease inventory | Day 60 |
| Regulatory license transfer applications (FDA, FCC, state insurance / banking, DEA, ITAR registration, FERC) | Regulatory counsel | Industry-specific | Closing | Per regulator timeline |
| CFIUS post-closing reporting if required under 31 C.F.R. §800.502 / §800.503 [CITE: confirm] | CFIUS counsel | CFIUS-cleared deal | Closing | Per CFIUS clearance order |
| Foreign investment notifications (UK NSI, EU FSR, Germany AWG, etc.) post-closing if mandated | Foreign counsel | International deal | Closing | Per jurisdiction |
| Restrictive-covenant integration — confirm enforceability by state for transferred employees; update where state law (CA, MA, others) restricts non-competes | Employment counsel | All | Employee transition | Day 60 |
| Update FCPA / anti-corruption training and policies for acquired workforce | Compliance | All | Closing | Day 60 |

## Days 61–90
| Task | Owner | Trigger | Dependency | Target |
|---|---|---|---|---|
| Complete regulatory transfer approvals (long-tail) | Regulatory counsel | Industry-specific | Day 31–60 applications | Day 90 |
| Integrate compliance programs (FCPA, OFAC, privacy, antitrust) | Compliance | All | Day 31–60 policy work | Day 90 |
| TSA exit planning — confirm in-house capability for each service | Buyer ops + GC | TSA in place | TSA term | Day 90 |
| Employment classification audit on acquired workforce (FLSA exempt/non-exempt, IC vs. employee) | Employment counsel | All | Day 31–60 integration | Day 90 |
| Wage-and-hour audit for state-law compliance (CA, NY, etc.) | Employment counsel | All | Day 31–60 integration | Day 90 |
| Update / file §16 ownership reports if public buyer; record beneficial ownership changes | Securities counsel | Public buyer | Closing | Per Section 16 deadlines |
| Earnout: confirm accounting and measurement protocols established | Finance + GC | If earnout | Closing | Day 90 |

## >90 Days (Long-Tail)
| Task | Owner | Trigger | Dependency | Target |
|---|---|---|---|---|
| §338(h)(10) joint election Form 8023 filed | Tax | 338(h)(10) | Closing | Per IRS deadline (~8.5 months post-acquisition) |
| Earnout measurement-period management; financial statement delivery; objection windows | Finance + GC | If earnout | Closing | Per agreement |
| Indemnity claim windows — calendar by survival period (fundamental, general, tax, IP, fraud) | GC | All | Closing | Calendar through last survival date |
| R&W insurance: retention erosion tracking; claim notice procedure if loss arises | GC + broker | If R&W | Closing | Through policy term (typically 6 years for fundamentals) |
| Dissolution of acquired-entity shell if collapsed into buyer | Corporate counsel | If consolidation | All consents and transfers complete | Per integration plan |
| Final TSA termination; bring all services in-house | Buyer ops | If TSA | TSA term end | Per TSA |
| Post-integration audit — confirm all consents, assignments, regulatory filings completed | GC | All | All prior tasks | One-year mark |

---

## Owner / Dependency Summary Table
| Workstream | Lead Owner | Days 1–30 Tasks | Days 31–90 Tasks | Long-Tail |
|---|---|---|---|---|
| Entity housekeeping | Corporate counsel | [count] | [count] | [count] |
| Assignments & consents | GC + commercial | | | |
| Employment & benefits | HR + employment counsel | | | |
| Equity administration | HR + securities counsel | | | |
| IP transfers and recordations | IP counsel | | | |
| Regulatory filings | Regulatory counsel | | | |
| IT / privacy | Privacy + IT | | | |
| Real estate | Real estate counsel | | | |
| Tax | Tax counsel | | | |
| Insurance | Risk management + broker | | | |
| Earnout governance | Finance + GC | | | |
| Indemnity tracking | GC | | | |

---

## Open Items from Closing Checklist
| # | Item | Status | Resolution Plan |
|---|---|---|---|
```

---

## Verification

- [ ] Tasks organized by Day 1, 2–30, 31–60, 61–90, >90.
- [ ] Each task has owner, deal-structure trigger, dependency, target date.
- [ ] All 14 workstream categories addressed (entity, consents, employment, benefits, IP, regulatory, IT/privacy, real estate, contracts, banking, insurance, tax, D&O/R&W, earnout).
- [ ] Asset-deal-specific tasks (assignment recordations, bulk-sales notices, sales-tax clearance, employee termination/rehire) distinguished from stock/merger-specific tasks (officer/director changes, COC-triggered consents).
- [ ] §338(h)(10) and other tax elections with explicit deadlines flagged.
- [ ] HSR / CFIUS / foreign-investment post-closing obligations addressed.
- [ ] D&O tail and R&W policy administration captured.
- [ ] Earnout governance and indemnity-window calendaring addressed.
- [ ] Restrictive-covenant enforceability by state addressed.
- [ ] Long-tail items extending past Day 90 captured.
- [ ] No invented regulatory deadlines or statutory provisions; placeholders used.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating asset and stock deals as interchangeable in the consent inventory | Asset deals require affirmative assignment + counterparty consent for anti-assignment clauses; stock deals only require consent where contract has a change-of-control trigger — different inventory, different timing |
| Missing bulk-sales notices and sales-tax clearance certificates in asset deals | Several states still maintain bulk-sales statutes; failure to follow can transfer tax liability to buyer; check each jurisdiction at signing, not after closing |
| Treating restrictive covenants as portable across states | Non-competes invalid in CA absent narrow exceptions; restricted in MA, MN, IL, OK, others; assignability and choice-of-law are jurisdictionally limited; rewrite for each state during integration |
| Ignoring §16 reporting for public buyer | Officers and directors acquiring beneficial ownership in connection with the deal trigger §16(a) reporting; calendar Form 4 deadlines |
| Treating CFIUS clearance as "done at closing" | CFIUS mitigation agreements impose ongoing reporting and audit obligations under 31 C.F.R. Part 800; track in long-tail section |
| Missing §338(h)(10) Form 8023 deadline | Filing deadline is approximately 8.5 months after acquisition date [CITE: confirm exact regulation]; calendar at closing |
| Skipping IP recordation post-closing | Failure to record assignments at USPTO / USCO can expose buyer to bona fide purchaser claims by later assignees; record all IP assignments within 90 days |
| Treating customer notification as a one-and-done | Wave customer notifications: top tier on Day 1 with personal outreach; middle tier within 30 days; long tail within 60 days |
| Missing data-controller / privacy notice update | Under GDPR / CCPA, change of data controller may trigger notification obligations and updated privacy notices; calendar within 30 days |
| Treating D&O tail as "in place" without verifying binder receipt | Confirm binder and policy delivery on Day 1; verify run-off term (typically 6 years), aggregate cap, and prior-acts coverage |
| R&W claim windows not calendared | Survival periods for fundamental reps (typically 6 years or statute of limitations), general reps (12–24 months), tax (statute of limitations + 60 days), and IP (often extended) must be calendared at closing |
| Not tracking retention erosion under R&W policy | First-dollar losses erode the retention; failure to log can complicate later claim acceptance |
| Earnout dispute mechanism activated only at deadline | Establish accounting and access protocols on Day 1 to avoid disputes about methodology mid-measurement |
| Treating employees as automatically transferred in asset deals | Asset deals typically require termination by seller and rehire by buyer; employment is not assignable absent statutory transfer mechanism (TUPE-style); plan WARN notices and benefits transitions accordingly |
| Skipping wage-and-hour compliance review post-closing | High-litigation area; conduct exempt/non-exempt and IC classification audit within 90 days to surface inherited exposure |
