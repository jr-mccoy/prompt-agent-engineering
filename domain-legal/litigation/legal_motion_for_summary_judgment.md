---
title: "Motion for Summary Judgment — Rule 56 (and State Analogs)"
category: legal/litigation
description: "Draft a motion for summary judgment with statement of undisputed material facts, memorandum of law applying Rule 56 standard count-by-count, citations to record evidence, and proposed order."
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
  - litigation
  - summary-judgment
  - rule-56
  - dispositive-motion
updated: "2026-05-08"
related_prompts:
  - domain-legal/litigation/legal_motion_to_dismiss_12b6.md
  - domain-legal/discovery/legal_document_request_drafter.md
  - domain-legal/depositions/legal_deposition_summary.md
---

**Purpose:** Draft a complete summary-judgment package — Notice of Motion, Statement of Undisputed Material Facts (SUMF), Memorandum of Law, and Proposed Order — applying Rule 56 (or the state analog) to discovery-record evidence the user supplies.

**When to use:** Post-discovery dispositive motion; partial summary judgment on an element or affirmative defense; cross-motions; training/evaluation tasks where the record is bounded.

---

## Your Input

- **Court / venue:** [Federal district / state court]
- **Movant / non-movant:** [Plaintiff or defendant; identify counterparty]
- **Counts targeted:** [All / specific — list]
- **Substantive law for each targeted count:** [Elements; affirmative-defense elements where applicable]
- **Record evidence:** [Deposition excerpts (witness, page:line), declarations, contracts, emails, business records, RFA admissions — supplied verbatim or by clear reference with quoted text]
- **Theory of the motion per count:** [Element fails / affirmative defense established as a matter of law / no genuine dispute on a dispositive fact]
- **Local rules:** [Specific to the court — separate SUMF requirement, page limits, evidentiary objections format]
- **Anticipated non-movant evidence:** [What the other side will likely offer]
- **Tone:** [Aggressive / measured]

---

## Constraints

**Must:**
- Use the **Celotex / Rule 56** framework: movant either (a) produces evidence that no genuine dispute exists as to the element on which it bears the burden, or (b) shows the absence of evidence on an element on which the non-movant bears the burden at trial.
- Draft a **Statement of Undisputed Material Facts**: each fact in a separate numbered paragraph with a citation to specific record evidence (deposition page:line, declaration paragraph, exhibit page).
- Argue **count-by-count** in the memorandum. For each count, state the elements, identify the disputed/undisputed status of each, and apply Rule 56 to each.
- Treat the non-movant's evidence in the light most favorable to the non-movant where the movant has the burden at trial; otherwise apply the appropriate framework.
- Identify and respond to **evidentiary issues** the non-movant will raise (hearsay, authentication, expert admissibility, parol evidence) only if those issues affect what evidence is on the Rule 56 record.
- Where the motion is on an **affirmative defense** the movant will bear at trial, plead and prove every element with record citations.
- Address **partial summary judgment** alternatives if full summary judgment is not warranted.

**Must Not:**
- Treat the SUMF as argument. The SUMF is fact-only with citations; argument lives in the memorandum.
- Cite to evidence not in the supplied record. Use `[NEED CITE: {what evidence}]` placeholders for gaps.
- Weigh witness credibility. That is impermissible at summary judgment.
- Resolve genuine factual disputes by characterization. If the inference cuts both ways, summary judgment fails on that fact.
- Confuse Rule 56 with Rule 12(b)(6); the standards are different and the record is different.
- Use evidence that would be inadmissible at trial without acknowledging the admissibility issue under Rule 56(c)(2).

---

## Instructions

1. **Notice of Motion** — short, names Rule 56, identifies relief (full or partial summary judgment), sets hearing per local rules.
2. **Statement of Undisputed Material Facts (SUMF).** One material fact per numbered paragraph. Each paragraph cites:
   - Witness deposition: "{Witness} Dep. {date} at {page}:{line}–{page}:{line}."
   - Declaration: "Declaration of {Name} ¶ {N}."
   - Document: "Ex. {Letter} at {page}."
   - RFA: "{Party}'s Resp. to RFA No. {N}."
3. **Memorandum — Introduction.** Two short paragraphs: what the case is and why summary judgment is warranted on identified counts.
4. **Memorandum — Procedural Posture.** Brief — discovery completion, prior motion practice.
5. **Memorandum — Legal Standard.** Rule 56 / state analog: genuine dispute, material fact, Celotex burden allocation. Use supplied authority's language with pinpoints.
6. **Memorandum — Argument.**
   - For each targeted count or defense:
     - Caption (e.g., "I. Plaintiff Cannot Establish Reliance on Count II Because the Undisputed Record Shows No Reliance.").
     - Elements.
     - Application: walk SUMF facts through the operative element. Tie each conclusion to specific SUMF paragraph numbers.
     - Address the non-movant's anticipated evidence and explain why it does not create a genuine dispute (or, if it would, why it is not material).
7. **Partial Summary Judgment Alternative.** If full SJ is a stretch, identify what can be granted partially.
8. **Conclusion.** Specific prayer for relief.
9. **Proposed Order** (if locally required).
10. **Local-rule certifications.**

---

## Output Format

```markdown
{COURT CAPTION}

NOTICE OF MOTION AND MOTION FOR SUMMARY JUDGMENT

PLEASE TAKE NOTICE that on {date} at {time}, or as soon thereafter as counsel may be heard, {Movant} will and hereby does move this Court for summary judgment under Federal Rule of Civil Procedure 56 in {Movant}'s favor on Counts {N} of the Complaint. This Motion is supported by the accompanying Memorandum of Law, the Statement of Undisputed Material Facts, the Declaration(s) of {…}, and Exhibits {A–N}.

Dated: {date}                       /s/ {counsel}

---

STATEMENT OF UNDISPUTED MATERIAL FACTS

1. {Fact.} ({citation})
2. {Fact.} ({citation})
{...}

---

MEMORANDUM IN SUPPORT OF MOTION FOR SUMMARY JUDGMENT

INTRODUCTION
{...}

PROCEDURAL POSTURE
{...}

LEGAL STANDARD
{Rule 56; Celotex burden allocation; pinpoints to supplied authority.}

ARGUMENT

I. {Count / Defense / Element} — {Operative Reason}
   A. Elements.
   B. The Undisputed Record Establishes {fact / lack of fact}.
      {Walk SUMF ¶¶ X–Y through the element.}
   C. {Non-movant's evidence does not create a genuine dispute because …}

II. {Count / Defense / Element}
{...}

III. In the Alternative, Partial Summary Judgment Should Be Granted on {…}

CONCLUSION
For the foregoing reasons, {Movant} respectfully requests that this Court grant summary judgment in {Movant}'s favor on Counts {…} of the Complaint, or in the alternative, grant partial summary judgment on {…}.

Dated: {date}                       /s/ {counsel}

---

[PROPOSED ORDER]
[CERTIFICATE OF COMPLIANCE / SERVICE]
```

---

## Verification

- [ ] SUMF contains one material fact per paragraph, each with a record citation.
- [ ] No argumentation in the SUMF.
- [ ] Memorandum applies Rule 56 standard, not 12(b)(6).
- [ ] Each targeted count argued separately with elements and SUMF citations.
- [ ] Non-movant's anticipated evidence acknowledged and addressed.
- [ ] Partial summary judgment alternative considered.
- [ ] No witness-credibility weighing.
- [ ] No evidence cited that is not in the supplied record; gaps flagged with placeholders.
- [ ] Local rules on page limits, separate SUMF, and proposed order met.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Drafting an SUMF that argues rather than recites facts | One fact per paragraph, citation to the record, no characterization |
| Asking the court to weigh credibility | Impermissible at summary judgment; identify the credibility issue and seek trial |
| Conflating "no evidence" with "evidence I don't believe" | Celotex requires either affirmative evidence or a showing the non-movant lacks evidence |
| Treating an immaterial dispute as defeating the motion | A dispute is only fatal if it is material to the element |
| Citing inadmissible evidence (hearsay, unauthenticated) | Acknowledge admissibility under Rule 56(c)(2); identify how it can be presented in admissible form at trial |
| Loading the SUMF with legal conclusions | "Defendant breached the contract" is not a fact; "Defendant did X on Y date" is |
| Mixing Rule 56 with Rule 12(b)(6) standards | Different motions, different records; do not blend |
| Forgetting affirmative-defense elements when the movant has the trial burden | If the movant carries the trial burden, every element must be proved on the Rule 56 record |
| Hiding partial-SJ relief in the conclusion only | If partial SJ is in play, brief it in its own argument heading |
