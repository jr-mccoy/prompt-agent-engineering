---
title: "Annotated Bibliography Builder for Biblical Studies — Verified Entries Only, Annotations From What You Read"
category: biblical-studies/academic-writing
description: "Build an annotated bibliography for a biblical-studies paper or thesis from sources the student has actually located and read: gate every entry on verification status, format citations to the required style from user-supplied details only, draft annotations from the student's own notes (position, method, evidence, verses handled, usefulness), and quarantine any entry that cannot be located — never inventing a source, author, title, date, page number, or quotation."
techniques:
  - QA-05
  - IPC-07
  - IPC-08
  - DP-04
  - OC-12
difficulty: intermediate
tags:
  - annotated-bibliography
  - citation-integrity
  - anti-fabrication
  - source-evaluation
  - sbl-style
  - academic-writing
  - make-annotated-bibliography
  - check-my-sources-are-real
updated: "2026-10-03"
related_prompts:
  - domain-education-teaching/learner/writing/learn_annotated_bibliography_helper.md
  - domain-biblical-studies/theology-research/biblical_commentary_evaluation.md
  - domain-research-academic/research_manuscript_fact_check_reconciler.md
---

# Annotated Bibliography Builder for Biblical Studies

**Objective:** Turn the sources a student has found and read into a correctly formatted, honestly annotated bibliography — and stop any source that cannot be verified from entering it.

> **STRONG-GUARD prompt — never invent a source.** Annotated bibliographies are where fabricated citations do the most damage: they look finished. This prompt **never** creates an entry, author, title, journal, volume, year, publisher, page range, DOI, or quotation, and never fills a missing field by guessing. It **never** annotates a source from memory of what the work "argues"; annotations are drafted only from the student's own notes and supplied excerpts. A field the student has not supplied stays **[VERIFY: missing]**. An entry the student cannot locate in a library catalogue or the publisher's record is moved to **Quarantine** and is not annotated. Sources suggested by any AI tool, including this one, start in Quarantine.

**When to use:**
- An assignment or thesis proposal requires an annotated bibliography on a biblical text or problem.
- You have a pile of sources and notes and need consistent citations and annotations.
- You suspect some of your references came from an AI chat or an unreliable list and need them checked.

**When NOT to use:**
- You want coaching to write the annotations yourself, sentence by sentence, without drafted text (common in high-school and first-year courses) — use `domain-education-teaching/learner/writing/learn_annotated_bibliography_helper.md`.
- You need to decide what *kind* of commentary to use before you have sources — use `domain-biblical-studies/theology-research/biblical_commentary_evaluation.md`.
- You have a finished draft and need every claim checked against its sources — use `domain-research-academic/research_manuscript_fact_check_reconciler.md`.
- You have not searched yet — use `domain-biblical-studies/academic-writing/biblical_academic_literature_review_plan.md` first.

**Audience:** Seminary and graduate students (A); pastors and teachers documenting research (P).

---

## Inputs / Context

1. **The question** the bibliography serves and the passage(s) by address.
2. **Style.** Required style guide and edition (biblical studies commonly uses the *SBL Handbook of Style*; confirm with the instructor), and annotation length.
3. **Entries.** For each source, the bibliographic details exactly as found in the catalogue or on the title page.
4. **Verification status per entry.** Where the student located it (library catalogue, publisher page, database record, physical copy) — or "not located".
5. **The student's notes per entry.** What they read (chapters/pages), the work's position, method, evidence, verses handled; short excerpts with page numbers if they want them quoted.
6. **Academic-integrity rule.** Whether the course permits AI-drafted annotations; if not, the prompt returns structure and questions only.

---

## Constraints

### Must
- Run a **verification gate** on every entry before formatting: located (where) → fields complete → read (what) → annotate.
- Format citations **only from supplied fields**; missing fields are **[VERIFY: missing]**, never inferred.
- Draft annotations **only from the student's notes**, anchoring each claim to the note or excerpt it came from (page numbers as the student gave them).
- Annotate in a fixed shape: position, method, evidence, verses handled, relation to the student's question, limits.
- Record each work's **interpretive stream** where the student identified it, without ranking streams.
- Move unlocatable or AI-suggested entries to **Quarantine** with the check to run.

### Must Not
- Create, complete, or "correct" an entry from memory — including a plausible year, publisher, or page range.
- Summarise a work the student has not read or noted.
- Quote anything the student did not supply verbatim with a page.
- Present a quarantined entry as usable.

### Tradition-neutral stance (Must / Must Not)
- **Must:** describe each source's stance in the student's terms and attribute it; include sources across streams where the student has them.
- **Must Not:** label a source "unreliable" for its conclusions; judge on method and evidence.

---

## Instructions

### Step 1 — Gate
For each entry: located? where? which fields present? read what? Assign **VERIFIED**, **INCOMPLETE** (located, fields missing), or **QUARANTINE** (not located, or AI-suggested and unchecked). Reject, don't repair: an entry with an unconfirmed author or title is not fixed by guessing.

### Step 2 — Format
Format VERIFIED and INCOMPLETE entries to the required style; insert [VERIFY: missing] for absent fields.

### Step 3 — Annotate from notes
Draft each annotation from the notes in the fixed shape. Mark any sentence whose basis is thin ("notes do not say what method — ask").

### Step 4 — Classify
Tag each: type (commentary, monograph, article, reference work, primary source in edition, reception source), stream (as identified by the student), sub-question served.

### Step 5 — Coverage check
Show which sub-questions and streams have no source; route to the literature-review plan.

### Step 6 — Quarantine report
For each quarantined entry: what is missing and the exact check (catalogue search by title, journal table of contents for the claimed volume, publisher record).

---

## Output Format

```
# Annotated Bibliography — [question] — [style + edition]

## Gate summary
VERIFIED [n] · INCOMPLETE [n] · QUARANTINE [n]

## Entries
### [formatted citation — fields as supplied; [VERIFY: missing] where absent]
Status: [VERIFIED | INCOMPLETE] · Located via: [..] · Read: [chapters/pages]
Type / stream / sub-question: [..]
Annotation (from student notes): [position] [method] [evidence] [verses] [relation to question] [limits]

## Coverage gaps
## Quarantine (not annotated)
| Entry as given | Problem | Check to run |
```

---

## Verification

- [ ] No field, entry, or quotation originated by the model.
- [ ] Every annotation sentence traces to a student note or excerpt.
- [ ] Missing fields are [VERIFY: missing], not guessed.
- [ ] AI-suggested and unlocated entries are in Quarantine and not annotated.
- [ ] Streams are attributed as the student identified them, not ranked.

---

## False-Positive Prevention

❌ **DON'T:**
- Complete "Hoover, HTR 1971" into a full citation with pages from memory; ask for the pages from the article's first and last page.
- Annotate a famous work from its reputation.
- Trust a reference because it looks well-formed; fabricated citations usually do.

✅ **DO:**
- Treat a well-formed entry the student cannot locate as more suspicious than a messy one they can.
- Keep the student's notes as the audit trail for every annotation.

---

## Example Output

```
# Annotated Bibliography — The meaning of ἁρπαγμός in Phil 2:6 — SBL style (edition per syllabus)

## Gate summary
VERIFIED 1 · INCOMPLETE 2 · QUARANTINE 2

## Entries
### Martin, Ralph P. Carmen Christi: Philippians ii. 5–11 in Recent Interpretation and in the Setting
of Early Christian Worship. Cambridge: Cambridge University Press, 1967.
Status: VERIFIED · Located via: library catalogue record (user-supplied) · Read: the chapter on 2:6
Type / stream / sub-question: monograph · historical-critical · (a) meaning, (c) history of research
Annotation (from student notes): Surveys interpretations of 2:5–11 up to the time of writing and
treats the passage as an early hymn; the student's notes record a chapter organising readings of
ἁρπαγμός into groups [student to supply page range]. Useful as a map of positions before 1967;
limits: predates later lexical studies, so cannot serve as the current state of the question.

### Hoover, Roy W. "The Harpagmos Enigma: A Philological Solution." Harvard Theological Review 64
(1971): [VERIFY: missing page range].
Status: INCOMPLETE · Located via: database record (user-supplied) · Read: whole article
Annotation (from student notes): Argues from idiom that the phrase concerns not taking advantage of
something already possessed; method: comparison of the expression in Greek authors (student notes
list the passages compared — cite them from the article, not from here). Central for (a).

### Wright, N. T. "ἁρπαγμός and the Meaning of Philippians 2:5–11." Journal of Theological Studies
37 (1986): [VERIFY: missing page range].
Status: INCOMPLETE · Located via: database record (user-supplied) · Read: whole article
Annotation (from student notes): Engages the previous article's proposal and relates the phrase to
the passage's narrative; student notes the article was later revised in a collection
[VERIFY which version you read and cite that one].

## Coverage gaps
No reception source for sub-question (d) patristic use. No non-English source.
→ biblical_academic_literature_review_plan.md, Step 4 search terms.

## Quarantine (not annotated)
| "Smith, J. 'Harpagmos and the Roman Triumph.' NTS 2009." | AI-suggested; not found in catalogue | Check the journal's 2009 tables of contents; if absent, delete. |
| "Blog: 'What harpagmos really means'" | Located, but not scholarly; no author credentials | Keep out of the bibliography; use only to find sources it cites, then verify those. |
```

---

## Techniques Used

- **QA-05 (Citation Requirements):** Every field comes from the student's record of the source; absent fields stay [VERIFY: missing].
- **IPC-07 (Verbatim Source Anchoring):** Each annotation claim is tied to a student note or excerpt with its page, giving an audit trail.
- **IPC-08 (Validation Gate, Reject-Don't-Repair):** The located → complete → read gate runs before formatting; unverifiable entries are quarantined, not repaired.
- **DP-04 (Must-Not Constraints):** Explicit prohibitions on completing, summarising, or quoting from memory.
- **OC-12 (External Reference Catalog):** Routes each check to catalogues, journal tables of contents, and publisher records.

## Related Prompts

- `domain-education-teaching/learner/writing/learn_annotated_bibliography_helper.md` — Socratic coaching when the student must write every annotation sentence.
- `domain-biblical-studies/theology-research/biblical_commentary_evaluation.md` — choosing commentary types before sourcing.
- `domain-research-academic/research_manuscript_fact_check_reconciler.md` — reconciling a finished draft against its sources.
