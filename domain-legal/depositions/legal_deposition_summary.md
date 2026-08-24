---
title: "Deposition Transcript Summary"
category: legal/depositions
description: "Generate a structured deposition summary with page:line index, topic-organized digest, key admissions, exhibits used, prior-inconsistent-statement flags, and impeachment material — usable by trial team and partner-level reviewers."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - depositions
  - summary
  - transcript-digest
  - trial-prep
updated: "2026-05-08"
related_prompts:
  - domain-legal/depositions/legal_deposition_outline_witness.md
  - domain-legal/litigation/legal_motion_for_summary_judgment.md
  - domain-legal/litigation/legal_case_strategy_assessment.md
---

**Purpose:** Convert a deposition transcript into a working tool for the trial team — page:line index by topic, digest of substantive testimony, list of admissions tied to elements, exhibits used, impeachment hooks, and items reserved for trial use.

**When to use:** After every deposition; supplemented after errata; consolidated into a multi-witness synthesis pre-MSJ or pre-trial.

---

## Your Input

- **Witness:** [Name, role, capacity (fact / 30(b)(6) / expert)]
- **Date and matter:** [...]
- **Transcript:** [Paste the transcript with page and line numbers preserved, or supply with consistent page:line cites]
- **Exhibits used:** [List with descriptions and Bates numbers]
- **Element / theory map:** [The elements of claims and defenses the testimony bears on]
- **Prior statements available for comparison:** [Interrogatory responses, declarations, prior depositions, public statements]
- **Audience:** [Case team / partner brief / settlement memo / MSJ work]
- **Length target:** [Short (1–2 pages digest only) / Standard (page:line index + digest) / Comprehensive (full topic-organized synthesis with element ties)]

---

## Constraints

**Must:**
- Tie every substantive entry to a **page:line range**.
- Organize the digest by **topic**, not chronologically through the transcript.
- For each substantive admission, identify the **element or theory** it bears on.
- Quote operative language verbatim; do not paraphrase admissions.
- Identify **exhibits used** and where in the transcript each was authenticated and discussed.
- Flag **prior inconsistent statements** with the specific prior source and the page:line where the inconsistency was surfaced.
- Identify **objections** that may need ruling pre-trial (deposition designations, motions in limine).
- Note **errata** if any.
- Maintain a separate **personal-capacity vs. 30(b)(6)** column for corporate depositions.

**Must Not:**
- Paraphrase a key admission. Quote.
- Conflate topics; one topic per row in the digest.
- Treat "I don't recall" the same as "no." Track them separately.
- Omit the questioner's name. Same-question impact differs by examiner.
- Generate quotations that are not present in the supplied transcript.
- Lose objection / instruction-not-to-answer events; these often require ruling before designations.

---

## Instructions

1. **Cover sheet.** Witness, date, capacity, matter, examiners, length, exhibits.
2. **Headline admissions and themes.** Five-or-fewer top items, each tied to an element or use.
3. **Page:line index.** Topic → page:line range, in topic order. Cross-references for multi-topic passages.
4. **Topic-organized digest.** For each topic:
   - Topic title and element/theory tie.
   - Page:line range.
   - Substantive summary, with verbatim quotes for admissions.
   - Exhibits used.
   - Prior-statement comparisons.
5. **Exhibits used.** Table: exhibit number, description, Bates, page:line of authentication, page:line of substantive discussion.
6. **Objections and instructions not to answer.** Page:line, basis, ruling needed.
7. **Errata.** Page:line, original, correction, basis.
8. **Trial-use notes.** Designations to consider, impeachment hooks, exhibit predicates, themes.

---

## Output Format

```markdown
# DEPOSITION SUMMARY — {Witness} ({capacity}) — {Date}
**Matter:** {caption}
**Examiners:** {names}
**Length:** {pages, hours}
**Privileged & Confidential — Attorney Work Product**

## Headline Admissions and Themes
1. {Admission} — Element/theory tie: {...} — Page:line: {p:l}.
2. ...

## Page:Line Index by Topic
| Topic | Page:Line | Notes |
|-------|-----------|-------|
| Witness background | 5:1–12:18 | ... |
| Knowledge of {topic} | 24:5–37:22 | ties to element X |
| {topic} | ... | ... |

## Topic Digest

### Topic 1: {Title} — Element/theory: {tie}
- Page:line: {range}
- Summary: {narrative}
- Verbatim admissions:
  - "{quoted Q & A}" (p:l)
  - "{...}" (p:l)
- Exhibits used: Ex. {N} (auth at {p:l}, substantive at {p:l}).
- Prior-statement comparison: Inconsistent with Interrogatory Response No. {N}, dated {date}: {how} (p:l of impeachment).
- Open items: {follow-up needed}.

### Topic 2: {Title}
{...}

## Exhibits Used

| Ex. # | Description | Bates | Auth p:l | Substantive p:l |
|-------|-------------|-------|----------|------------------|

## Objections and Instructions Not to Answer

| p:l | By whom | Basis | Question | Ruling needed |
|-----|---------|-------|----------|----------------|

## Errata

| p:l | Original | Correction | Basis |
|-----|----------|------------|-------|

## Trial-Use Notes
- Designations to consider: {p:l ranges with reason}
- Counter-designations to anticipate: {...}
- Impeachment hooks: {...}
- Exhibit predicates established: {...}
- Themes: {...}
```

---

## Verification

- [ ] Every substantive entry carries a page:line cite.
- [ ] Admissions quoted verbatim; not paraphrased.
- [ ] Digest organized by topic, not by transcript order.
- [ ] Exhibits authenticated and substantively used are both indexed.
- [ ] Prior-inconsistent statements identified with the specific prior source.
- [ ] Objections and instructions not to answer captured for ruling.
- [ ] Errata captured.
- [ ] No quotations introduced that are not in the supplied transcript.
- [ ] "I don't recall" tracked separately from denials.
- [ ] Element/theory ties shown for each admission.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Paraphrasing an admission ("admitted she knew") | Quote verbatim with p:l |
| Treating "I don't recall" as "no" | Track separately; "I don't recall" is impeachable but not a denial |
| Losing the questioner's identity | Capture, especially across cross-noticed depositions |
| Mixing personal-capacity and 30(b)(6) testimony | Mark each segment by capacity |
| Forgetting authentication moments for exhibits | Without the authentication p:l, the exhibit is harder to use |
| Skipping objections that need ruling | These drive motion-in-limine and designation practice |
| Quotations that drift from the transcript | Use only language present in the supplied transcript |
| Ignoring errata | Errata can change the substance of a key admission |
