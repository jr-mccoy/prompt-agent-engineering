---
title: "Biblical Studies Literature Review Plan — History of Research, History of Interpretation, and Discipline Databases"
category: biblical-studies/academic-writing
description: "Plan the history-of-research (Forschungsgeschichte) section or chapter for a biblical-studies paper or thesis on a passage, motif, or problem: separate the history of modern research from the history of interpretation, choose the discipline's indexes and source types, build search terms in English, the original language, and other research languages, set inclusion rules and an organising scheme by method or position, and define the extraction record — routing every specific title to the student's own search and verification."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - QA-04
  - OC-12
difficulty: advanced
tags:
  - literature-review
  - history-of-research
  - history-of-interpretation
  - reception-history
  - research-databases
  - academic-writing
  - find-what-scholars-have-said
  - where-to-start-bible-research
updated: "2026-10-03"
related_prompts:
  - domain-research-academic/research_literature_review_plan.md
  - domain-biblical-studies/theology-research/biblical_theological_research_bibliography.md
  - domain-biblical-studies/theology-research/biblical_historical_theology_development.md
---

# Biblical Studies Literature Review Plan

**Objective:** Produce a search-and-synthesis plan for the history-of-research section of a biblical-studies paper or thesis — what to search, where, in which languages, what to include, how to organise it, and what to record from each source — so the student finds the real conversation rather than a model's guess at it.

> **STRONG-GUARD prompt — invented scholarship.** This prompt plans a search; it does not report one. It **never** names a scholar, work, article, or school as part of the literature, never says what "most scholars" or "recent research" hold, and never asserts that a debate has a particular shape. Indexes, edition series, and resource types are named because they are tools; whether your library provides them is **[VERIFY]**. Any work the student already knows is echoed as *user-supplied — VERIFY*.

**When to use:**
- You have a question (or a candidate question) on a biblical text and must write its history of research.
- A supervisor asked "who has said what about this?" and you need a method, not a list.
- You need to test a thesis contribution claim produced by `domain-biblical-studies/academic-writing/biblical_academic_thesis_dissertation_workshop.md`.

**When NOT to use:**
- The review is not on a biblical text or problem, or you need the general literature-review process (screening, PRISMA-style protocols, synthesis types) — use `domain-research-academic/research_literature_review_plan.md`; this prompt adds only what biblical studies requires on top of it.
- You need the *kinds* of sources for a doctrinal question rather than a search plan for a text — use `domain-biblical-studies/theology-research/biblical_theological_research_bibliography.md`.
- You want the history of a doctrine itself traced, not the literature on a text — use `domain-biblical-studies/theology-research/biblical_historical_theology_development.md`.
- You already have sources and need to log and annotate them — use `domain-biblical-studies/academic-writing/biblical_academic_annotated_bibliography_builder.md`.

**Audience:** Seminary and graduate students (A); pastors writing for publication (P).

---

## Inputs / Context

1. **The question** and the passage(s) by address.
2. **Scope.** Paper section (1–3 pages) or thesis chapter (8,000–15,000 words); time available.
3. **Languages.** Reading languages, including original languages and German/French/other modern languages.
4. **Starting points.** Works already read — user-supplied, verify-required.
5. **Library access.** Which indexes and databases the student can reach (confirm with the library).
6. **Declared tradition (optional).** May add a stream of literature to include; never removes others.

---

## Constraints

### Must
- Separate **history of research** (modern critical scholarship on the question) from **history of interpretation / reception** (how communities and readers across periods have read the text). Many papers need both; they are searched differently.
- Name the discipline's **index types**: the ATLA Religion Database, *New Testament Abstracts* / *Old Testament Abstracts*, Index Theologicus, and BiBIL are examples to check against library access [VERIFY]; plus commentary bibliographies, Festschriften, and dictionary/encyclopedia articles as seed sources.
- Build **search terms** in English, in the original language (lemma and key phrase, transliterated and in script), and in other research languages the student reads.
- Set **inclusion rules** (period, method, language, genre) before searching.
- Choose an **organising scheme** — by position, by method, or by period — and say why.
- Define the **extraction record** per source.

### Must Not
- Name works or scholars as members of the literature, or summarise what the literature says.
- Assert a debate's history, phases, or consensus.
- Claim an index covers a period, language, or journal set without a [VERIFY].
- Treat reception history as merely "precritical errors" or modern research as the only serious reading.

### Tradition-neutral stance (Must / Must Not)
- **Must:** include confessional and non-confessional scholarship, and Jewish as well as Christian reception where the text is shared; organise by position, attributing each to its stream.
- **Must Not:** exclude a stream because of its conclusions, or let the organising scheme imply which side is right.

---

## Instructions

### Step 1 — Define the reviewed question
Restate it as the question the literature must answer, plus the sub-questions (meaning, origin, variant, function, reception).

### Step 2 — Split the two histories
Decide whether the paper needs history of research, history of interpretation, or both; allocate pages.

### Step 3 — Seed, then expand
Seed from the bibliographies of the 2–3 most recent technical commentaries the student can access and from dictionary articles; expand by index search and forward citation. Stop rule: when two consecutive search rounds add no new position.

### Step 4 — Search terms
Per sub-question: English terms, original-language lemma/phrase (script and transliteration), modern-language equivalents, passage-address forms (e.g., "Mk 4:12", "Mark 4.10–12", "Mc 4,12").

### Step 5 — Inclusion rules
Period, languages, genres (monograph, article, commentary excursus, dissertation), and how reception sources are read (critical edition or translation — stated).

### Step 6 — Organising scheme and extraction record
Choose the scheme. Extraction record: citation (verified), position on each sub-question, method, evidence used, verse(s) handled, what it answers to, page locations of key claims.

### Step 7 — Plan check
State what would show the plan has missed something (a position cited by others that you have not read; a language you skipped). Uncertainty about coverage is stated, not hidden.

---

## Output Format

```
# Literature Review Plan — [question] — [section | chapter], [pages/words]

## Reviewed question and sub-questions
## Two histories
- History of research: [needed? pages]   - History of interpretation: [needed? periods, pages]

## Seed sources (types; titles user-supplied — VERIFY)
## Indexes and tools to check against library access [VERIFY]
## Search terms
| Sub-question | English | Original language | Other languages | Address forms |

## Inclusion rules
## Organising scheme + reason
## Extraction record fields
## Stop rule and coverage risks
```

---

## Verification

- [ ] No scholar, title, or summary of the literature originated by the model.
- [ ] History of research and history of interpretation are planned separately.
- [ ] Index availability and coverage are marked [VERIFY].
- [ ] Search terms include original-language and other-language forms.
- [ ] Inclusion rules set before searching; stop rule stated.
- [ ] Organising scheme does not presuppose an answer.

---

## False-Positive Prevention

❌ **DON'T:**
- Hand the student a list of "key works" — those are the citations most likely to be invented.
- Organise by "traditional view vs. scholarly view"; that ranks before reviewing.
- Search only in English and conclude a question is open.
- Use the newest commentary's survey as the review; it is a seed, not a substitute.

✅ **DO:**
- Make the student's own search the source of every title.
- Record page locations at extraction so the review's claims can be checked later.

---

## Example Output

```
# Literature Review Plan — Purpose of the parables in Mark 4:10–12 — thesis chapter, ~9,000 words

## Reviewed question and sub-questions
Main: How does the ἵνα clause in 4:12 relate the parables to "those outside"?
(a) Force of ἵνα (purpose, result, or other); (b) Mark's use of Isaiah 6:9–10 and its wording
relative to Hebrew, Greek and Aramaic traditions; (c) relation to Mark's secrecy motif;
(d) reception: how readers have handled the apparent harshness of 4:12.

## Two histories
- Research (≈6,000 words): grammatical, redaction-critical, narrative-critical treatments.
- Interpretation (≈3,000 words): patristic, medieval, Reformation-era, and modern church readings;
  Jewish reception of Isaiah 6:9–10 where relevant to (b).

## Seed sources
- Bibliographies of the 2–3 most recent technical commentaries on Mark you can access (titles: yours — VERIFY).
- Dictionary/encyclopedia articles on "parables" and "messianic secret".
- User-supplied: a monograph on the messianic secret the student has read (VERIFY full citation).

## Indexes and tools [VERIFY each against library access]
ATLA Religion Database; New Testament Abstracts; Index Theologicus (strong for German-language work);
dissertation databases; patristic citation indices for (d).

## Search terms
| (a) | purpose clause, hina, final/consecutive | ἵνα, μήποτε (+ hina, mēpote) | Finalsatz, "damit" | Mk 4:12; Mark 4.10–12; Mc 4,12 |
| (b) | Isaiah 6:9-10 Mark, Targum Isaiah Mark 4:12 | Isa 6:9–10 in Hebrew & LXX forms (you supply text) | Jesajazitat | Isa 6:9–10; Jes 6,9f |
| (c) | messianic secret, secrecy motif | μυστήριον (4:11) | Messiasgeheimnis | — |
| (d) | history of interpretation Mark 4:12; parable theory reception | — | Auslegungsgeschichte | — |

## Inclusion rules
Research: 1900–present; English, German, French; monographs, articles, commentary excursuses.
Interpretation: sources in critical edition or published translation (state which); Latin sources
only in translation (student's competence).

## Organising scheme
By position on (a) — purpose / result / other — with method noted per source; reception by period.
Reason: the chapter's argument is about ἵνα; a period scheme would bury the positions.

## Extraction record
Verified citation · position on (a)–(d) · method · evidence (grammar, Isaiah form, narrative) ·
verses treated · whom it answers · page refs of key claims.

## Stop rule and coverage risks
Stop when two rounds add no new position on (a). Risks: Aramaic-tradition argument under (b) may
need literature you cannot read — note it as a limit. A claim that Mark's wording agrees with one
tradition against another is a frequently discussed proposal: VERIFY from sources; do not assert.
```

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** Question → two histories → seed → terms → rules → scheme → plan check.
- **RT-02 (Multi-Dimensional Analysis Framework):** Research and reception, sub-question by sub-question, language by language.
- **CM-02 (Constraint Specification):** Inclusion rules and a stop rule are fixed before searching.
- **QA-04 (Uncertainty Acknowledgment):** Index coverage and library access are [VERIFY]; coverage risks are stated.
- **OC-12 (External Reference Catalog):** Points to discipline indexes and source types as tools, never to invented entries.

## Related Prompts

- `domain-research-academic/research_literature_review_plan.md` — the discipline-general review process this builds on.
- `domain-biblical-studies/theology-research/biblical_theological_research_bibliography.md` — source types for a doctrinal question.
- `domain-biblical-studies/theology-research/biblical_historical_theology_development.md` — tracing a doctrine across church history.
