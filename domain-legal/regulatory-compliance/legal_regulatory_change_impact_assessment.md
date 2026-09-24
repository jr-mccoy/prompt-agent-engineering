---
title: "Regulatory Change Impact Assessment — New Rule to Owned Remediation Plan"
category: legal/regulatory-compliance
description: "Map a single new or amended rule, regulation, or agency guidance against a company's current operations: parse the rule into discrete obligations, confirm applicability and effective dates from the supplied text, identify gaps against the current state, rate each gap, and assign remediation owners and dates. Counsel-facing, cross-industry, and anchored to verbatim rule text — never to a remembered version of the rule."
techniques:
  - ST-02
  - RT-02
  - CM-03
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - regulatory-compliance
  - regulatory-change
  - impact-assessment
  - gap-analysis
  - remediation-plan
updated: "2026-09-24"
reasoning:
  styles: [analytic, systematic, decomposition]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [attorney, in_house_counsel, compliance_officer]
related_prompts:
  - domain-legal/research/legal_statutory_interpretation.md
  - domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md
  - domain-legal/in-house-legalops/legal_board_legal_update_brief.md
  - domain-finance/regulatory-compliance/finance_regulatory_requirement_mapper.md
---

# Regulatory Change Impact Assessment

**Objective:** Take one new or amended rule (statute, final rule, regulation, binding guidance, or supervisory expectation) and produce a defensible impact assessment: which parts apply to which business activities, what changes on which date, where current operations fall short, and who closes each gap by when. The deliverable is a decomposed obligation register joined to a remediation plan that a general counsel can hand to business owners and defend to a regulator.

**When to use:**
- A final rule, amendment, or new statute has been published and the company must decide what it has to change before the compliance date.
- A proposed rule is far enough along that counsel wants a provisional impact read (mark the whole output PROVISIONAL).
- A regulator has issued guidance, FAQs, or an enforcement action that shifts how an existing rule is read.

**Distinct from:**
- `domain-finance/regulatory-compliance/finance_regulatory_requirement_mapper.md` and `finance_compliance_gap_analysis.md` — those map a *whole* financial-services regime to activities and controls for a compliance function. This prompt handles the *delta* of one rule, in any industry, and includes the legal-interpretation step.
- `domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md` — evaluates a whole misconduct-risk program (FCPA, AML, sanctions, antitrust) for effectiveness, not a single rule change.
- `domain-software-engineering/analysis/security/security_industry_regulatory_compliance.md` — engineering implementation of controls once counsel has decided what the rule requires.
- `domain-AI-ML/responsible-ai-governance/rai_eu_ai_act_compliance_assessment.md` — use that for an AI-system-specific EU AI Act assessment.

---

## Your Input

- **Jurisdiction(s) and regulator(s):** [e.g., US federal — agency name; State of X; EU / Member State; UK]
- **Rule text (verbatim):** [Paste the operative provisions, definitions section, applicability / scope section, effective and compliance dates, and any transition provisions. Preamble or explanatory memorandum if available.]
- **Citation and publication status:** [Proposed / final / effective; publication citation; date]
- **Company profile:** [Entities, products, business lines, geographies, customer types, headcount, revenue thresholds relevant to the rule's scope triggers]
- **Current state:** [Existing policies, processes, systems, contracts, and controls touching the rule's subject matter; known prior findings]
- **Business owners available:** [Names or roles who can own remediation]
- **Constraints:** [Budget, system freeze windows, board calendar, parallel initiatives]
- **Interpretive positions already taken:** [Any existing memo, trade-association comment, or regulator FAQ the company relies on — supply text]

If the rule text is not supplied, stop at Step 1 and return the list of provisions needed. Do not reconstruct a rule from memory.

---

## Constraints

**Must:**
- Work only from the supplied rule text. Every obligation in the register quotes or pin-cites the provision it comes from (`§ X(b)(2)` style, as it appears in the supplied text).
- Resolve applicability before gaps: scope triggers, thresholds, exemptions, safe harbors, and phase-in tiers decide whether an obligation reaches each entity or activity.
- Separate the **effective date** from the **compliance date(s)** and from any phased or tiered dates; record each as stated in the text.
- Classify each obligation as: new requirement / changed requirement / codification of existing practice / no change.
- Rate each gap on two axes: **legal exposure** (enforcement, private right of action, penalties as stated in the supplied text) and **remediation effort** (people, systems, contracts, time).
- Assign one accountable owner (role, not team) and a target date to every open gap; dates must land before the applicable compliance date with buffer for testing.
- Flag every interpretive question the text leaves open as an **Interpretive Call** with the competing readings and who decides.

**Must Not:**
- Invent statutory or regulatory citations, section numbers, compliance dates, penalty amounts, or regulator FAQs. Use `[CITE: ...]`, `[NEED PIN: ...]`, and `[VERIFY: ...]` placeholders.
- Treat a proposed rule as final, or a preamble statement as binding text.
- Assume the rule applies company-wide because it applies somewhere; apply scope entity by entity.
- Collapse "no current evidence of compliance" into "compliant."
- Add generic "consult counsel" language; the reader is counsel. Replace it with named Interpretive Calls.

---

## Instructions

1. **Confirm the text.** List the provisions supplied and any that are referenced but missing (definitions, cross-referenced rules, appendices). Record publication status and every stated date.
2. **Decompose into obligations.** Break the rule into atomic obligations (one actor, one duty, one trigger). Number them `OB-01`, `OB-02`, … with pin cites.
3. **Resolve applicability.** For each entity / business line, walk the scope triggers, thresholds, and exemptions. Output an applicability matrix (entity × obligation: applies / does not apply / Interpretive Call).
4. **Classify change type.** New / changed / codified / no change, per obligation.
5. **Compare to current state.** For each applicable obligation, record current practice and evidence. Mark Gap / Partial / Met / Unknown. "Unknown" is a gap in evidence and gets an owner.
6. **Rate gaps.** Legal exposure (High / Medium / Low, with the textual reason) × remediation effort (High / Medium / Low). Sort by exposure first, then by lead time.
7. **Build the remediation plan.** For each gap: action, owner, dependencies, target date, evidence of completion. Back-schedule from the compliance date.
8. **List Interpretive Calls.** Each with the question, the competing readings, the downside of each, and the decision owner and deadline.
9. **Draft the executive summary last.** What changes, for whom, by when, the top three exposures, and the decisions needed.

---

## Output Format

```markdown
# Regulatory Change Impact Assessment — {Rule short name}
**Status:** {Final / Proposed — PROVISIONAL} | **Prepared:** {date} | **Privileged & Confidential — Attorney Work Product** {if applicable}

## 1. Executive Summary
- What changed: {2–3 sentences}
- Who is in scope: {entities / lines}
- Key dates: Effective {date as stated} | Compliance {date(s) as stated} | {Phase-in tiers}
- Top exposures: {1–3}
- Decisions needed: {Interpretive Calls with owners and deadlines}

## 2. Source Text Inventory
| Provision | Supplied? | Notes |
|---|---|---|

## 3. Obligation Register
| ID | Obligation (actor / duty / trigger) | Pin cite | Change type |
|---|---|---|---|

## 4. Applicability Matrix
| Obligation | Entity A | Entity B | Business line C | Basis |
|---|---|---|---|---|

## 5. Gap Assessment
| ID | Current state / evidence | Status | Exposure (why) | Effort |
|---|---|---|---|---|

## 6. Remediation Plan
| Gap | Action | Owner (role) | Depends on | Target date | Completion evidence |
|---|---|---|---|---|---|

## 7. Interpretive Calls
| # | Question | Reading A | Reading B | Decision owner | Decide by |
|---|---|---|---|---|---|

## 8. Open Items
- Provisions not supplied: {...}
- Facts to confirm: {...}
- Placeholders to resolve: {[CITE] / [VERIFY] list}
```

---

## Worked Example

**Input (abridged):** A US consumer-lending company with three subsidiaries supplies the verbatim text of a newly finalized state rule requiring (a) written adverse-action explanations within a stated number of days, (b) annual third-party audits of automated underwriting models for lenders above an origination-volume threshold, and (c) record retention of model inputs. The text states an effective date and a later compliance date for the audit requirement. Subsidiary C originates below the threshold.

**Output (excerpt):**

| ID | Obligation | Pin cite | Change type |
|---|---|---|---|
| OB-01 | Lender sends written adverse-action explanation within the stated period after decision | § 4(a) as supplied | Changed (shorter period than current policy) |
| OB-02 | Covered lender commissions annual independent audit of automated underwriting model | § 5(b) as supplied | New |
| OB-03 | Lender retains model inputs for each decision for the stated period | § 6 as supplied | New |

Applicability: OB-02 → Subsidiaries A and B apply; Subsidiary C **Interpretive Call** — the threshold in § 2(d) counts "originations," and the text does not say whether purchased loans count. Reading A (originations only) excludes C; Reading B (all loans held) captures C. Decision owner: GC; decide before audit-vendor RFP issues.

Gap row: OB-03 — current retention is 25 months for application data; model inputs are overwritten on retrain. Status: Gap. Exposure High (text supplies a per-violation penalty; penalty amount `[VERIFY: § 9 penalty amount against official publication]`). Effort High (data-platform change). Owner: VP Data Platform; target date back-scheduled 90 days before the compliance date to allow validation.

---

## Verification

- [ ] Jurisdiction lock: every obligation comes from the supplied text of the named jurisdiction; no borrowing from similar rules elsewhere.
- [ ] Citation discipline: every obligation has a pin cite from the supplied text; no invented section numbers, dates, or penalty figures; placeholders listed in Open Items.
- [ ] Effective date, compliance date(s), and phase-in tiers recorded separately and exactly as stated.
- [ ] Applicability resolved entity by entity before any gap is rated.
- [ ] Every "Unknown" treated as a gap with an owner.
- [ ] Every open gap has one accountable role and a date before the compliance date.
- [ ] Proposed-rule outputs marked PROVISIONAL throughout.
- [ ] Interpretive Calls state both readings and a decision owner.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Reconstructing the rule from memory or from a similarly named rule in another jurisdiction | Use only supplied text; list missing provisions and stop if the operative text is absent |
| Using the effective date as the compliance deadline | Record effective and compliance dates separately; back-schedule from the compliance date |
| Applying the rule company-wide because one entity is covered | Walk scope triggers and exemptions per entity; flag threshold ambiguities as Interpretive Calls |
| Marking an obligation "Met" because a policy exists | Require evidence of operation; a policy without evidence is Partial or Unknown |
| Quoting preamble commentary or regulator FAQs as binding obligations | Label them interpretive aids; obligations come from operative text |
| Stating penalty amounts or private-right-of-action exposure not in the supplied text | Use `[VERIFY: ...]`; rate exposure only on what the text supports |
| Remediation owners assigned to teams or committees | One accountable role per gap |
| Hiding interpretive uncertainty inside a confident gap rating | Surface it as an Interpretive Call with competing readings |
