---
title: "Tax Research Memo"
category: legal/tax
description: "Tax-specific research memo built on the tax authority hierarchy — Code, Treasury regulations (final, temporary, proposed), IRS published guidance, private rulings, and case law by forum — with pinpointed citations or explicit placeholders, a confidence level tied to penalty-protection standards, and currency checks for effective dates and recent legislation."
techniques:
  - ST-03
  - RT-05
  - CM-02
  - QA-04
  - QA-01
difficulty: advanced
tags:
  - legal
  - tax
  - tax-research
  - research-memo
  - treasury-regulations
  - authority-hierarchy
  - penalty-protection
updated: "2026-09-24"
reasoning:
  styles: [analytic, evidential, hierarchical]
  stakes: high
  horizon: days
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: [memo, structured]
  user_role: [lawyer, analyst]
  mode: [synthesize, assess]
related_prompts:
  - domain-legal/research/legal_research_memo_irac.md
  - domain-legal/research/legal_research_plan.md
  - domain-legal/research/legal_statutory_interpretation.md
  - domain-finance/tax-planning/finance_entity_structure_tax_comparison.md
---

# Tax Research Memo

**Objective:** Answer a discrete tax question in a memo that a reviewer can verify line by line: the question and facts, a short answer with a stated confidence level, the governing authorities ranked by weight (statute, regulations by type, published guidance, non-precedential guidance, case law by forum), the analysis applying them, the contrary authority, and the open items. Every citation is either pinpointed from supplied material or a placeholder — the memo never manufactures a Code section, regulation paragraph, ruling number, or case.

**When to use:**
- A discrete federal (or state) tax question arising in a transaction, return position, controversy, or advisory matter.
- Documenting the basis for a return position where penalty protection or disclosure is in play.
- Updating an existing memo after new legislation, regulations, or guidance.

**Distinct from:**
- `domain-legal/research/legal_research_memo_irac.md` — the general IRAC memo; this adds the tax authority hierarchy, regulation-type weighting, forum-specific case law, effective-date discipline, and confidence levels mapped to penalty standards.
- `domain-finance/tax-planning/` — planning and modeling of tax outcomes for decision-makers; this is legal analysis of what the law requires.
- `domain-legal/divorce/legal_divorce_tax_consequences_analysis.md` — the tax consequences of a property settlement in a divorce.

**Audience:** Tax attorneys, tax-controversy counsel, and CPAs or EAs working on legal-analysis memos under supervision.

---

## Your Input

- **Question presented:** [One precise question — split compound questions]
- **Taxpayer and year(s):** [Entity type, tax year(s), filing status — effective dates depend on year]
- **Jurisdiction:** [Federal / state (name) / both; for litigation risk, likely forum: Tax Court, district court, Court of Federal Claims, and circuit of appeal]
- **Facts:** [Operative facts only, with source documents]
- **Authorities in hand:** [Paste statute text, regulation text, rulings, cases — with citations]
- **Purpose of memo:** [Return position / transaction planning / controversy / opinion support]
- **Confidence standard needed:** [e.g., reasonable basis, substantial authority, more likely than not — as defined by your firm's policy and current rules `[VERIFY]`]
- **Research-current date:** [Date through which authorities were checked]

---

## Constraints

### Must
- Rank authorities by **weight**: Code; final regulations; temporary regulations; proposed regulations (generally not binding authority — say so); revenue rulings and procedures; notices and announcements; private letter rulings, TAMs, and chief counsel advice (non-precedential — flag); case law by forum and circuit of appeal.
- Pinpoint every citation to the subsection, paragraph, or page supplied; otherwise use `[CITE: …]`, `[NEED PIN: …]`, or `[NEED HOLDING: …]`.
- Check **effective dates** for each provision against the tax year(s) and flag recent legislation or regulatory changes that could apply `[VERIFY: effective date + transition rule]`.
- Identify the **likely litigation forum** and whether its circuit has ruled; Tax Court follows the law of the circuit to which appeal lies.
- State a **confidence level** and tie it to the standard the user specified; explain what would raise or lower it.
- Present the **strongest contrary authority** and why it is distinguishable or why it controls.
- Separate **facts assumed** from facts established; list facts that would change the answer.

### Must Not
- Invent Code sections, regulation paragraphs, ruling or notice numbers, rates, thresholds, or case names.
- Treat proposed regulations or private letter rulings as binding.
- State a rate, dollar threshold, or phase-out from memory; mark `[VERIFY: amount + year]`.
- Blend federal and state analysis without flagging conformity or decoupling `[VERIFY: state conformity date]`.
- Express confidence without naming the standard it maps to.

---

## Instructions

1. **Question presented and short answer** with confidence level.
2. **Facts** — operative, sourced, with assumptions listed separately.
3. **Authority map** — table ranking each authority by weight, with pinpoint and effective date.
4. **Statutory analysis** — text first; definitions, cross-references, and exceptions.
5. **Regulatory and administrative analysis** — regulation type, deference considerations `[NEED HOLDING: current standard of review for agency interpretations]`, published guidance.
6. **Case law** — by forum; note circuit of appeal.
7. **Contrary authority** — strongest counter-position and response.
8. **Conclusion and confidence** — mapped to the required standard; disclosure considerations if confidence is below the non-disclosure threshold `[VERIFY]`.
9. **Open items and currency** — facts to confirm, pending guidance, legislation to watch, research-current date.

---

## Output Format

```markdown
# Tax Research Memorandum
**To:** {…}  **From:** {…}  **Date:** {…}  **Re:** {question — taxpayer — year(s)}
**Research current through:** {date}  |  **Privileged & Confidential**

## Question Presented
## Short Answer   (Confidence: {level} — maps to {standard})
## Facts
### Assumed facts
## Authority Map
| Rank | Authority | Pinpoint | Type / weight | Effective for year? |
## Analysis
### A. Statute
### B. Regulations and Administrative Guidance
### C. Case Law (forum: {…}; circuit: {…})
### D. Contrary Authority
## Conclusion and Confidence
## Facts That Would Change the Answer
## Open Items and Currency Checks
```

---

## Worked Example

**Input (abridged):** Question: Is a C corporation's $400,000 payment to terminate an unfavorable supply contract deductible currently or capitalized? Tax year 2026. Authorities in hand: user pasted the text of the relevant capitalization regulation and one Tax Court decision. Forum if litigated: Tax Court, appeal to the Ninth Circuit. Standard needed: substantial authority.

**Output (excerpt):**

> **Short answer:** Likely currently deductible, *unless* the termination facilitates the acquisition of a new contract or asset. Confidence: **substantial authority**, not more-likely-than-not, because the facilitation facts are incomplete.
>
> **Authority Map (excerpt).** Rank 1: Code capitalization provision `[CITE: IRC section — user to confirm; not supplied]`. Rank 2: final regulation on intangibles — pasted text; pinpoint to the paragraph addressing termination payments `[NEED PIN: paragraph]`. Rank 5: Tax Court decision (pasted) — precedential in Tax Court; Ninth Circuit has not addressed on these facts `[NEED HOLDING: any Ninth Circuit authority]`.
>
> **Facts that would change the answer:** If the corporation signed a replacement supply contract with a new vendor as part of the same plan, the payment may facilitate that acquisition and be capitalized — confirm sequence and documentation.
>
> **Currency:** confirm no 2025–2026 amendment to the regulation and no intervening guidance `[VERIFY]`.

---

## Verification

- [ ] Jurisdiction lock: federal vs. state stated; forum and circuit of appeal identified.
- [ ] Every citation pinpointed from supplied text or marked with a placeholder.
- [ ] Authority map ranks by weight; proposed regs and PLRs flagged as non-binding.
- [ ] Effective dates checked against the tax year(s).
- [ ] Confidence level named and mapped to the requested standard.
- [ ] Contrary authority presented and answered.
- [ ] No rates, thresholds, or ruling numbers from memory.
- [ ] Research-current date stated.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Citing a Code section or regulation paragraph from memory | Pinpoint only from supplied text; otherwise `[CITE]` / `[NEED PIN]` |
| Treating a PLR or CCA as precedent | Label non-precedential; use only as evidence of IRS position |
| Applying a provision without checking its effective date | Test each authority against the tax year and transition rules |
| Ignoring the Tax Court's circuit-of-appeal rule | Identify the circuit and whether it has ruled |
| Confidence stated as "likely" with no standard | Map to the specific penalty or opinion standard requested |
| Federal answer silently applied to state tax | Flag state conformity or decoupling |
| Burying the facts that flip the answer | List them explicitly after the conclusion |
