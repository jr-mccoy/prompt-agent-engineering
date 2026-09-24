---
title: "Voluntary Self-Disclosure Decision Memo"
category: legal/regulatory-compliance
description: "Draft a privileged decision memo on whether, when, to whom, and how to voluntarily self-disclose potential misconduct to an enforcement authority: facts established versus open, the disclosure policy text the user supplies, the credit available and its conditions, exposure under disclose and do-not-disclose scenarios, detection likelihood, collateral consequences, timing, and structure. Frames the decision for the board; does not predict charging outcomes."
techniques:
  - RT-02
  - NE-10
  - QA-04
  - QA-02
  - QA-05
difficulty: advanced
tags:
  - legal
  - regulatory-compliance
  - voluntary-disclosure
  - self-reporting
  - cooperation-credit
  - white-collar
  - decision-memo
  - found-wrongdoing
updated: "2026-09-24"
reasoning:
  styles: [strategic, evaluative, probabilistic]
  stakes: high
  horizon: weeks
  uncertainty: deep
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: structured
  user_role: [attorney, in_house_counsel, board_member]
related_prompts:
  - domain-legal/regulatory-compliance/legal_internal_investigation_plan.md
  - domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md
  - domain-legal/in-house-legalops/legal_matter_summary_for_executive.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
---

# Voluntary Self-Disclosure Decision Memo

**Objective:** Give a board, special committee, or general counsel a decision-ready memo on voluntary self-disclosure of potential misconduct. The memo separates established facts from open questions, applies the relevant authority's disclosure policy as supplied (conditions, credit, exclusions), compares exposure under disclose-now, disclose-later, and do-not-disclose scenarios with explicit probability language, weighs collateral consequences across other authorities and jurisdictions, and recommends a timing and structure — while being candid about what cannot be known.

**When to use:**
- An internal investigation has surfaced credible evidence of potential violations (e.g., bribery, sanctions or export-control breaches, fraud, antitrust conduct, regulatory reporting failures).
- A whistleblower may already have gone to a regulator, creating a race-to-disclose question.
- An acquirer has found pre-closing misconduct at a target and must decide within a policy window.

**Distinct from:**
- `domain-legal/regulatory-compliance/legal_internal_investigation_plan.md` — plans the fact-finding that feeds this memo.
- `domain-legal/litigation/legal_case_strategy_assessment.md` — strategy for pending litigation, not a pre-enforcement disclosure decision.
- `domain-finance/regulatory-compliance/` — financial-services regulatory filings (e.g., routine regulatory reports); this memo is a discretionary enforcement-exposure decision made under privilege.

---

## Your Input

- **Potential violation(s):** [Conduct, time period, business unit, countries]
- **Facts established vs open:** [What the investigation has confirmed, with evidence; what remains unknown]
- **Candidate authorities:** [Each enforcer that could have jurisdiction — domestic and foreign]
- **Disclosure policy text:** [Paste each authority's current self-disclosure / cooperation policy text with its title and version date. If not supplied, the memo marks each policy element `[VERIFY]` and does not characterize credit.]
- **Detection indicators:** [Whistleblower risk, ongoing government inquiries into the industry, counterparty investigations, audit findings, media interest]
- **Company posture:** [Prior resolutions or history, compliance program state, remediation to date, discipline taken, cooperation capacity]
- **Collateral considerations:** [Debarment / exclusion risk, licensing, securities disclosure, lender and insurer notice, civil litigation, employees' individual exposure]
- **Transaction context:** [If M&A: closing date and any policy window for acquirer disclosure `[VERIFY]`]

---

## Constraints

**Must:**
- Separate facts into **Established** (with evidence), **Probable**, and **Open**; state how each open fact could change the recommendation.
- Apply each authority's policy only from supplied text: eligibility conditions (voluntariness, timeliness, full cooperation, remediation, disgorgement), available credit, and exclusions (aggravating circumstances). Quote the condition.
- Run a **mandatory-reporting screen** before modelling scenarios `[VERIFY each obligation against supplied text]`: e.g., government-contractor mandatory disclosure, bank suspicious-activity reporting, sanctions and export-control reporting, securities disclosure duties, auditor communications, licensing or regulator notification conditions. If any obligation applies, "do not disclose" is removed as an option for that authority and the memo addresses only timing, scope, and form.
- Model at least three scenarios — disclose now, disclose after further investigation, do not disclose (unless removed by the mandatory-reporting screen) — each with exposure elements (penalty range only if the user supplies a basis; otherwise qualitative), probability language (likely / possible / unlikely with the reason), and consequences across other authorities.
- Stress-test the recommendation: state the strongest argument against it and what fact would flip it.
- Address multi-authority coordination: disclosing to one authority can trigger another's interest; state sequencing.
- Address individuals: the policy's expectations about identifying individuals, and the need for separate counsel.
- End with a recommendation, a timing proposal, a disclosure structure (oral proffer, written submission, attorney proffer; scope), and the decisions the board must take.

**Must Not:**
- Invent policy terms, credit percentages, declination presumptions, disclosure windows, penalty amounts, or example resolutions. Use `[CITE: ...]`, `[VERIFY: ...]`, `[NEED PIN: ...]`.
- Predict that an authority *will* decline, or quantify a penalty without a supplied basis.
- Present non-disclosure as risk-free because detection seems unlikely; include the whistleblower and counterparty channels.
- Ignore that a disclosure is effectively irreversible.
- Use generic "consult counsel" boilerplate.

---

## Instructions

1. **Decision framing.** One sentence: what decision, by whom, by when.
2. **Fact status.** Established / Probable / Open table with evidence and the investigative step that would close each open item.
3. **Mandatory-reporting screen `[VERIFY]`.** Before treating disclosure as voluntary, test whether any obligation already requires a report: government-contractor mandatory disclosure, bank suspicious-activity reporting, sanctions or export-control reporting, securities disclosure duties, auditor communications, licence or regulator notification conditions, and contractual reporting clauses. For each: applies / does not apply / unknown, trigger, and deadline `[VERIFY]`. If any obligation applies, remove "do not disclose" as an option for that authority; the remaining question is timing, scope, and form.
4. **Authority map.** For each candidate authority: jurisdictional hook, policy supplied (Y/N), key conditions (quoted), exclusions.
5. **Detection analysis.** Channels by which authorities could learn independently; likelihood and timing for each.
6. **Scenario comparison.** Disclose now / disclose after further investigation / do not disclose: benefits, costs, exposure, collateral effects, reversibility.
7. **Stress test.** Strongest counter-argument; the flip facts.
8. **Recommendation.** Decision, timing, structure, sequencing across authorities, individual-counsel arrangements, remediation to complete before or alongside disclosure.
9. **Board resolutions needed.** Decisions and authorizations.

---

## Output Format

```markdown
# MEMORANDUM — PRIVILEGED & CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION / WORK PRODUCT
**To:** {Board / Special Committee / GC} **From:** {Counsel} **Date:** {date}
**Re:** Voluntary Self-Disclosure Decision — {Matter code name}

## 1. Decision Required
## 2. Summary Recommendation
## 3. Facts — Established, Probable, Open
| Fact | Status | Evidence | Step to close | Effect on decision if different |
|---|---|---|---|---|
## 4. Authorities and Disclosure Policies (as supplied)
| Authority | Hook | Policy (title, version) | Conditions (quoted) | Exclusions |
|---|---|---|---|---|
**Mandatory-reporting screen [VERIFY]**
| Obligation | Applies? (Y / N / Unknown) | Trigger and deadline [VERIFY] | Effect: "do not disclose" removed? |
|---|---|---|---|
## 5. Independent-Detection Analysis
## 6. Scenario Comparison
| Dimension | Disclose now | Disclose after further investigation | Do not disclose |
|---|---|---|---|
## 7. Stress Test — Strongest Case Against the Recommendation
## 8. Recommended Timing, Structure, and Sequencing
## 9. Individuals and Separate Counsel
## 10. Board Actions Required
## 11. Open Items and Placeholders
```

---

## Worked Example

**Input (abridged):** A US-listed industrial company's investigation has confirmed that a foreign subsidiary made four payments through a consultant to an employee of a state-owned customer; the purpose of two further payments is open. A former subsidiary employee who left on bad terms has threatened to "go to the authorities." The user pasted the relevant prosecutor's corporate self-disclosure policy text and version date; no foreign-authority policy text was supplied.

**Output (excerpt):**
- **Facts:** Four payments — Established (bank records, consultant invoices, emails referencing "the customer's contact"). Two payments — Open (next step: consultant's bank-statement production under contract audit rights).
- **Mandatory-reporting screen:** US-listed → securities disclosure duties and auditor communications about the investigation must be assessed before any "do not disclose" option is modelled `[VERIFY: periodic-report disclosure and auditor-communication obligations]`; no government-contract or bank-reporting hook on the facts supplied.
- **Detection:** Former employee → **likely** channel within months; the policy supplied conditions credit on disclosure "prior to an imminent threat of disclosure" (quoted from supplied text), so waiting risks losing voluntariness.
- **Scenario:** Disclose after further investigation — resolves the two open payments but, given the former employee, **possible** loss of voluntariness credit; not reversible if the employee reports first.
- **Stress test:** Strongest case against disclosing now — disclosure before the open payments are understood may expand scope. Flip fact: if the consultant's records show the open payments were legitimate services, scope risk falls.
- **Recommendation:** Initial attorney proffer within a short, stated window, with a commitment to supplement; foreign authority's policy `[VERIFY: current self-reporting policy and any coordination practice]` before sequencing.

---

## Verification

- [ ] Jurisdiction and authority lock: every policy condition quoted from supplied text; unsupplied policies marked `[VERIFY]` and not characterized.
- [ ] Citation discipline: no invented credit levels, windows, penalty figures, or example resolutions.
- [ ] Facts separated into Established / Probable / Open with evidence.
- [ ] Mandatory-reporting screen run before the scenarios; "do not disclose" removed wherever an obligation applies.
- [ ] Three scenarios compared (or fewer, if the screen removed "do not disclose"), including reversibility.
- [ ] Probability language used with reasons; no outcome predictions.
- [ ] Stress test names the strongest counter-argument and flip facts.
- [ ] Multi-authority sequencing and individuals addressed.
- [ ] Board decisions listed.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Quoting a credit percentage or declination presumption from memory | Use only supplied policy text; otherwise `[VERIFY]` and describe the element qualitatively |
| "The authority will decline" | Replace with conditional probability language tied to specific policy conditions |
| Treating low detection likelihood as a reason to stay silent without modelling whistleblower and counterparty channels | Detection analysis covers every channel with timing |
| Recommending disclosure without considering other authorities that learn of it | Map every authority and sequence disclosures |
| Presenting open facts as established to support a clean recommendation | Status column is mandatory; open facts carry flip analysis |
| Ignoring that disclosure cannot be undone | Reversibility is a required scenario dimension |
| Omitting individual exposure and separate counsel | Section 9 is mandatory |
