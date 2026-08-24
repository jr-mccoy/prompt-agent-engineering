---
title: "Technical Accounting Memo Writer — Issue / Analysis / Conclusion Structure"
category: finance/accounting-controllership
description: "Structure a defensible technical accounting position memo using IRAC discipline (Issue, Facts, Analysis under the standard, Conclusion, financial-statement impact), with authoritative-literature grounding, alternatives considered, GAAP-vs-IFRS flagging, and a strict no-fabricated-citations rule."
techniques:
  - RT-05
  - QA-05
  - DT-02
  - QA-04
  - DS-02
difficulty: advanced
tags:
  - technical-memo
  - accounting-policy
  - irac
  - position-paper
  - authoritative-literature
  - documentation
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_revenue_recognition_asc606_memo.md
  - domain-finance/accounting-controllership/finance_lease_accounting_asc842_analysis.md
  - domain-finance/accounting-controllership/finance_audit_pbc_preparation.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (FASB ASC / IASB IFRS).**

## Objective

Structure a rigorous technical accounting position memo on any accounting question — using IRAC discipline (Issue → Facts → Analysis under the authoritative standard → Conclusion → financial-statement impact) — that grounds the conclusion in the correct accounting literature, considers and rejects alternative treatments with reasons, flags GAAP-vs-IFRS divergence where it matters, and never fabricates citations. The output is an audit-ready position file, not a quick answer.

---

## When to Use

- Documenting management's accounting position on a judgmental or novel transaction (financial instrument, business combination, modification, impairment, consolidation, contingency).
- Creating the support an external auditor expects for a significant judgment (a "white paper" / technical memo).
- Resolving a disagreement between treatments by laying out the analysis and alternatives.
- Building a reusable memo template a team can apply to recurring technical questions.
- **Do not use** to produce a final auditable conclusion without independent technical review, or to generate specific ASC/IFRS paragraph citations you cannot verify — cite by standard and flag exact paragraphs for confirmation.

---

## Inputs / Context Required

```
<memo_context>
Entity / reporting framework: US GAAP | IFRS | dual
Topic / transaction:
Period(s) affected:
Audience: internal policy file | external auditor | audit committee

FACTS:
- The transaction/event and its terms:
- Amounts and timing:
- Relevant agreements, board actions, management intent:
- Any prior accounting / restatement history on this topic:

THE QUESTION:
- Precise accounting issue(s) to resolve (recognition, measurement, classification, presentation, disclosure):

LITERATURE THE USER BELIEVES APPLIES (optional):
- Candidate standards / topics (state by title/number; do not require paragraph numbers):

CONSTRAINTS:
- Materiality:
- Deadline / decision context:
</memo_context>
```

---

## Constraints

### Must
- Use the **IRAC-style structure**: **Issue → Facts → Analysis (under the standard) → Conclusion → Financial-Statement Impact** (plus Alternatives Considered and Open Items).
- State the **Issue** as a precise, answerable accounting question (or a short list).
- Separate **Facts** from assumptions; label every assumption.
- In **Analysis**, identify the governing authoritative literature **by standard title/number** (e.g., "ASC 805 Business Combinations" / "IFRS 3"), apply it to the facts step by step, and reason to a conclusion.
- Present **Alternatives Considered** — the other defensible treatment(s) and why they are rejected (DT-02). A memo with no alternatives considered is weak.
- Flag **GAAP-vs-IFRS divergence** where it changes the answer; if converged, say so.
- State the **Conclusion** explicitly, the **financial-statement impact** (entries, captions, ratios, disclosures), a **confidence level**, and the **key judgments** the conclusion depends on.
- Include the line: *"All paragraph-level references must be verified against current authoritative guidance (FASB ASC / IASB IFRS) as of [date]; this memo cites standards by title/number and flags specific paragraphs for confirmation."*

### Must Not
- Fabricate ASC/IFRS paragraph numbers, sub-paragraph letters, effective dates, or thresholds — cite by standard title/number and mark exact paragraphs `[CONFIRM ¶]`.
- Reach a conclusion without applying the literature to the specific facts.
- Omit the alternatives-considered analysis.
- Present a confident conclusion on a genuinely judgmental matter without disclosing the key judgments and confidence level.
- Apply the wrong framework's standard (e.g., cite ASC for an IFRS-only filer) without flagging.
- Bury the financial-statement impact — it must be explicit (entries, presentation, disclosure).

---

## Instructions

1. **Frame the Issue.** Write the precise accounting question(s). If multiple, order them logically (a recognition question often precedes measurement).

2. **State the Facts.** Summarize the transaction terms and context relevant to the issue; isolate assumptions and label them.

3. **Identify the literature.** Name the governing standard(s) by title/number. If the user proposed candidates, confirm or redirect. Do not assert paragraph numbers you cannot verify — mark them `[CONFIRM ¶]`.

4. **Analyze.** Apply the standard's criteria to the facts step by step. Where the standard requires judgment (probable, reasonably certain, control, fair value), make and document the judgment with reasons.

5. **Consider alternatives (DT-02).** Lay out the competing treatment(s). For each, state the argument for it and the specific reason it is rejected under the facts and literature.

6. **GAAP-vs-IFRS check.** If dual-reporting or framework matters, flag the divergence and its effect; otherwise note convergence.

7. **Conclude.** State the answer to each issue. Provide the financial-statement impact: journal entries, affected captions, ratio/covenant effects, and disclosure requirements.

8. **Disclose judgments & confidence.** List the load-bearing judgments and assign a confidence level; note what would change the conclusion.

9. **Verification (QA-04/QA-05).** Confirm the conclusion follows from the analysis; confirm alternatives are addressed; confirm no fabricated citations (every reference is to a real standard, paragraphs flagged for confirmation).

---

## Output Format

```
## Technical Accounting Memo — [Topic]
Framework: [US GAAP | IFRS | Dual] | Period(s): [__] | Audience: [__]
Prepared: [date] | Status: DRAFT — requires technical review
Confidence: [High / Medium / Low]

### 1. Issue
[Precise accounting question(s).]

### 2. Facts
[Transaction terms and context; assumptions labeled.]

### 3. Analysis
Governing literature: [Standard title/number — e.g., ASC 606 / IFRS 15] [CONFIRM ¶ for specific paragraphs]
[Step-by-step application of the standard's criteria to the facts; judgments documented.]

### 4. Alternatives Considered
| Alternative treatment | Argument for | Reason rejected |
|-----------------------|--------------|-----------------|
| [Treatment B] | [rationale] | [why it fails under facts/literature] |

### 5. GAAP vs IFRS
[Divergence affecting the conclusion, or "Converged — no divergence."]

### 6. Conclusion
[Answer to each issue.]

### 7. Financial-Statement Impact
Entries: [DR/CR]
Presentation / captions: [__]
Disclosures: [__]
Ratio / covenant effects: [__]

### 8. Key Judgments & Confidence
[Load-bearing judgments; confidence; what would change the answer.]

All paragraph-level references verified against current FASB ASC / IASB IFRS as of [date]; standards cited by title/number, specific paragraphs flagged [CONFIRM ¶].
```

---

## Verification

- [ ] Issue stated as a precise, answerable question.
- [ ] Facts separated from labeled assumptions.
- [ ] Governing standard(s) named by title/number; paragraph references flagged `[CONFIRM ¶]`.
- [ ] Standard applied step by step to the specific facts.
- [ ] Alternatives considered, with reasons for rejection.
- [ ] GAAP-vs-IFRS divergence flagged (or convergence stated).
- [ ] Conclusion follows from the analysis.
- [ ] Financial-statement impact explicit (entries, presentation, disclosure).
- [ ] Key judgments and confidence level disclosed.
- [ ] No fabricated citations, thresholds, or effective dates.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Fabricating ASC/IFRS paragraph numbers to look authoritative | Cite standards by title/number; mark specific paragraphs `[CONFIRM ¶]`; never invent references |
| Concluding without applying literature to the facts | Analysis must map the standard's criteria onto the specific transaction |
| Omitting alternatives (one-sided memo) | Alternatives-considered table is mandatory, with reasons for rejection |
| Overstating confidence on a judgmental issue | Disclose key judgments and a calibrated confidence level; state what would change the answer |
| Citing the wrong framework's standard | Confirm the entity's framework; flag any GAAP-vs-IFRS divergence affecting the conclusion |
| Hiding the financial-statement impact | Require explicit entries, presentation, and disclosure effects |
