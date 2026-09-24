---
title: "Petition for Review Drafter — Certiorari or State Supreme Court Discretionary Review"
category: legal/appellate
description: "Draft a petition for a writ of certiorari or a petition for discretionary review in a state high court, tied to the court's own grant criteria: question(s) presented, reasons for granting (conflict, importance, error, vehicle), record-cited statement, and a grant-worthiness self-assessment — with no invented splits, holdings, deadlines, or rule text."
techniques:
  - ST-01
  - ST-03
  - DS-01
  - RT-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - appellate
  - certiorari
  - petition-for-review
  - discretionary-review
  - questions-presented
  - lost-on-appeal
updated: "2026-09-24"
related_prompts:
  - domain-legal/research/legal_jurisdiction_split_analysis.md
  - domain-legal/appellate/legal_issue_selection_memo.md
  - domain-legal/appellate/legal_amicus_brief_strategy_memo.md
  - domain-legal/research/legal_precedent_comparison_table.md
---

**Objective:** Produce a petition for discretionary review that is organized around the reviewing court's grant criteria rather than the merits alone: a precise question presented, a statement tied to the record, and reasons for granting that show a genuine conflict or important question, a clean vehicle, and (secondarily) error below — plus an internal grant-worthiness assessment that tells counsel candidly whether the petition is worth filing.

> **Scope guard — attorney-facing only.** For licensed appellate counsel (or counsel for a prospective amicus). If the person running it appears to be an unrepresented party, stop and route them to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` (appellate pro bono programs, law-school appellate clinics, legal aid) rather than producing strategy. This guard is not a disclaimer; the ban on "consult an attorney" boilerplate below still applies.

**When to Use:** After an adverse decision from an intermediate appellate court or federal court of appeals; when evaluating whether to seek review at all; when converting an appellate brief into a petition; when responding to a petition (brief in opposition posture — the same criteria inverted).

**Distinct from:**
- `domain-legal/research/legal_jurisdiction_split_analysis.md` — maps a split and assesses review prospects as research; this prompt drafts the petition that uses that map.
- `domain-legal/appellate/legal_issue_selection_memo.md` — selects issues for an appeal as of right; discretionary review usually supports one or two questions.
- `domain-legal/appellate/legal_amicus_brief_strategy_memo.md` — non-party support at the petition or merits stage.

---

## Your Input

- **Reviewing court:** [U.S. Supreme Court / named state supreme court — required]
- **Grant criteria text:** [For the U.S. Supreme Court, Rule 10 considerations; for a state court, its rule or statute — supply text; otherwise `[NEED TEXT]`]
- **Decision below:** [Opinion text, date, court; any rehearing ruling and date]
- **Filing deadline and format rules:** [As the user has verified — word limits, required sections, appendix contents]
- **Posture:** [Petitioner / respondent (brief in opposition)]
- **Split or conflict authority:** [Cases on each side with holdings as verified — or the output of a split analysis]
- **Preservation record:** [Where the question was raised and decided below, with cites]
- **Importance evidence:** [Frequency of the issue, affected parties, government interest, economic impact — with sources]

---

## Constraints

**Must:**
- Organize "Reasons for Granting" around the **supplied grant criteria**, not a merits outline: conflict/split, importance, conflict with the reviewing court's precedent, and vehicle; error below is argued as support, not as the lead.
- Draft the **question presented** as a neutral-sounding, one-sentence (or short) question that frames the conflict and fits the vehicle; offer two to three alternatives with trade-offs.
- Show the **vehicle**: the question was pressed and passed upon below (record cites), is outcome-determinative, and is free of alternative grounds, jurisdictional defects, or factual disputes that would prevent resolution.
- Distinguish a **true split** (different rules) from different applications of the same rule.
- Use the grant criteria of the named court only; do not apply federal criteria to a state court or vice versa.
- Produce an **internal grant-worthiness assessment**: strengths, weaknesses, likely brief-in-opposition arguments, and a candid composite.

**Must Not:**
- Invent or overstate a split, count, or "deepening" trend; every member of a camp needs a supplied case.
- Invent deadlines, word limits, rule text, or the content of the decision below.
- Present the petition as a request for error correction when the criteria disfavor it.
- Cite a case for a holding the user has not verified; use `[NEED HOLDING]`.
- Add "consult an attorney" boilerplate.

---

## Method

1. **Criteria lock.** Quote or summarize the supplied grant criteria; list the elements the petition must satisfy.
2. **Vehicle screen.** Preservation, outcome-determinativeness, alternative grounds, jurisdiction, record clarity. If the vehicle fails, say so first.
3. **Conflict map.** Camps, members, rule of each (from supplied authority), and where the decision below sits.
4. **Question presented.** Draft alternatives; pick one with reasons.
5. **Draft the petition.** Sections as required by the named court's rules (as supplied): question(s) presented, parties, table of contents/authorities, opinions below, jurisdiction, provisions involved, statement, reasons for granting, conclusion, appendix list.
6. **Opposition stress test.** Draft the three strongest brief-in-opposition arguments (e.g., shallow split, poor vehicle, interlocutory posture) and the reply line for each.
7. **Grant-worthiness assessment (internal).**

---

## Output Format

```markdown
# PETITION FOR {WRIT OF CERTIORARI / REVIEW} — {Case}

## Questions Presented
{Selected QP}

## Opinions Below
{Citations/appendix pages as supplied}

## Jurisdiction
{Basis and dates — [VERIFY] any unsupplied date or statute}

## Provisions Involved
{Verbatim text as supplied}

## Statement
{Record-cited facts and proceedings; how the question was raised and decided below}

## Reasons for Granting the Petition
### I. {Courts are divided on the question presented}
### II. {The question is important and recurring}
### III. {This case is an ideal vehicle}
### IV. {The decision below is wrong}

## Conclusion

---
# INTERNAL
## QP Alternatives
| QP | Strength | Risk |
## Opposition Stress Test
| BIO argument | Reply |
## Grant-Worthiness Assessment
| Criterion | Assessment | Evidence |
**Composite:** {Strong / Moderate / Weak} — {reason}
## Open Items
- {Every [CITE]/[VERIFY]/[NEED TEXT]}
```

---

## Worked Example (abbreviated)

**Input:** State supreme court; petitioner lost in the intermediate court on whether a statute of limitations is tolled during a pending administrative claim. The state court's review rule (supplied) lists conflict among intermediate courts and issues of statewide importance. User supplies two intermediate-court decisions holding tolling applies and the decision below holding it does not.

**Output excerpt:**
- Criteria lock: conflict among districts; statewide importance (per supplied rule text).
- Vehicle: raised in opposition to the motion to dismiss (CT 44–51) and decided as the sole ground (Opinion at 6); no alternative ground → clean.
- QP (selected): "Whether the limitations period for a claim under [statute] is tolled while a statutorily required administrative claim is pending."
- Reason I: the decision below expressly disagrees with the two supplied district decisions (Opinion at 8) — a true split on the rule, not an application difference.
- Reason II: importance supported only by supplied data on the number of administrative claims filed annually; no invented figures.
- Stress test: "Split is shallow (2–1)" → reply: the supplied rule does not require depth, and the conflict leaves trial courts statewide without a controlling rule.
- Composite: Moderate-to-Strong, contingent on `[VERIFY: whether any other district has ruled since]`.

---

## Verification

- [ ] Reviewing court and its grant criteria locked; no cross-application of federal and state criteria.
- [ ] Vehicle screened and preservation cited to the record.
- [ ] Split members each supported by supplied authority; true vs. application split distinguished.
- [ ] QP is short, precise, and matches the vehicle.
- [ ] Error correction is secondary to criteria-driven reasons.
- [ ] Opposition stress test completed.
- [ ] No invented deadlines, rule text, holdings, or statistics.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Writing a merits brief with a new caption | Lead with conflict, importance, and vehicle per the supplied criteria |
| Manufacturing a split from dicta or distinguishable facts | Each camp member must state a different rule in a holding |
| Burying a vehicle problem | Screen vehicle first and report defects candidly in the internal assessment |
| A multi-clause, argumentative QP | One question, framed so the answer resolves the conflict |
| Using Supreme Court Rule 10 for a state petition | Use the named court's supplied criteria |
| Stating a filing deadline from memory | Use the user's verified date or `[VERIFY]` |
| Overstating importance with unsourced numbers | Use only supplied data; otherwise argue importance qualitatively |
