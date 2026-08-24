---
title: "Canon & Versification Differences Across Traditions — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Map where a user-specified book or passage appears across canonical traditions (Protestant, Catholic, Orthodox, Ethiopian, Jewish Tanakh ordering), note versification differences (Psalm numbering MT vs. LXX, chapter/verse splits), and identify books present in some canons but not others — treating every canon-inclusion claim and versification datum as verify-required against each tradition's own published canon lists and numbered editions."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - NE-14
difficulty: advanced
tags:
  - original-languages
  - canon
  - versification
  - deuterocanon
  - apocrypha
  - septuagint
  - masoretic-text
  - anti-fabrication
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_septuagint_usage.md
  - domain-biblical-studies/original-languages/biblical_language_ot_in_nt_usage.md
  - domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md
  - domain-biblical-studies/exegesis-interpretation/biblical_canonical_intertextual_reading.md
---

# Canon & Versification Differences Across Traditions

> **STRONG-GUARD prompt.** Canon lists and versification data look like simple facts, but models routinely misremember which books each tradition includes, confuse deuterocanonical/apocryphal classifications across traditions, assert wrong Psalm numbering offsets, fabricate chapter/verse mappings, and conflate distinct canonical traditions (e.g., treating the Greek Orthodox and Ethiopian canons as identical). Here, **every canon-inclusion claim, book ordering, versification mapping, and chapter/verse difference is verify-required** against each tradition's own published canon list and numbered edition. The model explains the **framework** of canonical and versification divergence; the user verifies every specific datum.

**Objective:** Take a user-specified book or passage and map where that content sits across the major canonical traditions — identifying which canons include it, what it is called in each, where it is placed in the ordering, and where versification (chapter/verse numbering) diverges — **without asserting any specific canon-inclusion claim, Psalm-numbering offset, or chapter/verse mapping from memory as authoritative.** The output is a structured comparison scaffold the user populates with verified data from each tradition's own sources.

**When to use:**
- You are studying a book or passage that may not appear in all Christian or Jewish canons and want to understand where it stands in each tradition.
- You encounter a verse reference that does not match between translations (e.g., a Psalm number is off by one, a chapter/verse split differs) and want to understand the versification systems.
- You are preparing teaching, preaching, or academic work that involves multiple traditions and need to map references accurately across them.

**When NOT to use:**
- Your question is about the *content* divergence between MT and LXX in a passage they share (translation differences, Vorlage differences) — use `biblical_language_septuagint_usage.md`.
- You want to trace how the NT uses an OT text across textual traditions — use `biblical_language_ot_in_nt_usage.md`.
- You want to understand why English translations render a verse differently when the underlying text is the same — use `biblical_translation_comparison.md` (in `exegesis-interpretation/`).

**Audience:** Seminary/academic (A) and pastors (P) working across traditions or preparing cross-traditional resources.

---

## Inputs / Context

1. **The book or passage.** The book name (in any tradition's naming convention) and, if applicable, the specific chapter/verse reference the user wants to map.
2. **The naming convention used.** Which tradition's name the user is starting from (e.g., "Sirach" vs. "Ecclesiasticus," "1 Esdras" vs. "3 Esdras") — naming alone varies across traditions and is a major source of confusion.
3. **Traditions to compare.** Which canonical traditions the user wants mapped — default is all five major traditions (Protestant, Roman Catholic, Eastern Orthodox, Ethiopian Orthodox, Jewish Tanakh), but the user may specify a subset.
4. **Known versification data (optional).** Any specific numbering differences the user has already identified — supplied so the model organizes, not invents, them.
5. **The question.** "Is this book in all canons?" / "Why is this Psalm numbered differently?" / "Where does this chapter/verse reference map across traditions?" — sets focus.

---

## Constraints

### Must
- Treat every **canon-inclusion claim** ("tradition X includes/excludes book Y") as **verify-required** against that tradition's own published canon list or conciliar/synodal decision. Never assert inclusion/exclusion from memory as settled.
- Treat every **versification mapping** (Psalm numbering offset, chapter/verse splits, verse-count differences) as **verify-required** against the numbered editions used by each tradition (MT, LXX, Vulgate, etc.).
- Distinguish clearly between **canon** (which books are considered authoritative Scripture), **ordering** (where books are placed in the sequence), and **naming** (what a book is called) — these are three separate questions that often get conflated.
- Explain the **reasons** for divergence at a framework level: the historical processes that led to different canons (Alexandrian vs. Palestinian canon theory, conciliar decisions, Reformation-era debates), different numbering systems (MT vs. LXX Psalm numbering, Vulgate inheritance), and different orderings (Torah-Nevi'im-Ketuvim vs. OT/NT Protestant ordering vs. Catholic ordering).
- Present each tradition's position **on its own terms** — describing what each tradition holds and why, attributed to that tradition, without evaluating whose canon is "correct."
- Flag areas of **genuine scholarly debate** (e.g., whether the Alexandrian canon theory accurately describes Second Temple practice, whether "deuterocanonical" and "apocryphal" map onto the same set of books).

### Must Not
- Assert from memory which specific books a tradition includes or excludes — this must be verified against each tradition's own published lists.
- Assert Psalm numbering offsets (e.g., "MT Psalm 10 = LXX Psalm 9 continued") from memory as authoritative — these mappings are verify-required.
- Assert chapter/verse boundary differences from memory — these are verify-required against the relevant numbered editions.
- Conflate distinct canonical traditions (e.g., treating Greek Orthodox, Russian Orthodox, and Ethiopian Orthodox as having identical canons — they do not).
- Use one tradition's terminology as the default (e.g., calling deuterocanonical books "apocrypha" without noting that this is a tradition-specific label, or vice versa).
- Present the history of canon formation as settled when it is debated — the historical reconstruction of how canons formed is itself a contested scholarly field.
- Fabricate conciliar decisions, synodal decrees, or publication dates for canon lists.

### Tradition-neutral stance (Must / Must Not)
- **Must:** present each tradition's canon as that tradition defines it, using that tradition's own terminology (deuterocanonical, anaginoskomena, apocrypha, etc.) and attribution, describing — not evaluating — the rationale each tradition offers.
- **Must Not:** privilege any tradition's canon as the "real" Bible, frame one tradition's additional or fewer books as the deviation from a norm, or present the historical question of canon formation as having a single correct answer.

---

## Instructions

### Step 1 — Fix the target and the traditions
Restate the book or passage the user has specified and the naming convention they used. Identify the canonical traditions to be compared. Flag immediately if the book name itself differs across traditions (e.g., "1 Esdras" refers to different books in different traditions) — this is a common source of confusion and must be surfaced before any mapping.

### Step 2 — Canon inclusion (verify-required per tradition)
For each tradition the user wants mapped, state whether the book appears in that tradition's canon — **flagged verify-required** against that tradition's own published canon list. Use each tradition's own terminology for the book's status:
- Protestant: canonical / apocryphal (non-canonical but sometimes printed between testaments)
- Roman Catholic: protocanonical / deuterocanonical
- Eastern Orthodox: canonical / anaginoskomena (and note that this category's boundaries vary by Orthodox jurisdiction — verify-required per jurisdiction)
- Ethiopian Orthodox: the broader Ethiopic canon — verify-required against the Ethiopian canon list
- Jewish: in the Tanakh (Torah / Nevi'im / Ketuvim) or not

Each inclusion/exclusion claim is flagged: "VERIFY against [tradition]'s published canon list."

### Step 3 — Ordering and placement
For traditions that include the book, note where it is placed in the ordering — flagged verify-required. Explain the structural logic of each ordering system (e.g., Jewish Tanakh places Daniel in Ketuvim, not among the prophets; Catholic OT includes deuterocanonical books interspersed, not grouped separately). If the user's question is about a specific passage rather than a whole book, note whether the passage's chapter/verse location is affected by ordering differences.

### Step 4 — Versification differences (verify-required)
If the user has specified a passage (not just a book), map where the chapter/verse reference falls across traditions — each mapping flagged **verify-required** against the numbered editions. Cover the major versification systems:
- **Psalm numbering:** MT/Hebrew numbering vs. LXX/Vulgate numbering — explain the framework (which Psalms are combined or split) without asserting specific number offsets from memory; instruct the user to verify the mapping in a Psalm numbering chart.
- **Psalm superscriptions:** Some traditions number superscriptions as verse 1, shifting all subsequent verse numbers — explain the framework and flag as verify-required.
- **Chapter/verse splits:** Some passages have different chapter or verse boundaries across editions (e.g., where one tradition starts a new chapter, another does not) — identify that this class of difference exists for the user's passage and instruct verification.
- **Verse-count differences:** Some passages have additional or fewer verses in certain traditions (e.g., additions to Daniel, additions to Esther) — identify the framework and flag each claim verify-required.

### Step 5 — Naming differences
Map the book's name across traditions (e.g., Sirach / Ecclesiasticus / Ben Sira; 1-2 Esdras / 3-4 Esdras / Ezra-Nehemiah — naming conventions vary significantly). Flag each name as verify-required and warn the user that numbering schemes for books like Esdras are a notorious source of confusion across traditions.

### Step 6 — Framework: why the divergence exists
Explain at a framework level why these canonical and versification differences exist — the historical, theological, and textual-tradition reasons — without asserting a single correct reconstruction. Cover: Second Temple period diversity of practice, the relationship between Hebrew and Greek text traditions, the role of conciliar/synodal decisions (flagging specific decisions as verify-required), Reformation-era canon debates, and the inheritance of different numbering systems from different base texts (MT vs. LXX vs. Vulgate). Present scholarly debate about canon formation as debate, not as settled history.

---

## Output Format

```
# Canon & Versification — [book or passage]

## Target
- Book / passage: [as user specified]
- User's naming convention: [tradition of origin]
- Traditions compared: [list]

## Naming across traditions (VERIFY each)
| Tradition | Name used | VERIFY against |
|-----------|-----------|----------------|
| [..] | [..] — VERIFY | [tradition's published canon/edition] |
⚠ Naming confusion alert: [if applicable — e.g., "1 Esdras" means different books in different traditions]

## Canon inclusion (VERIFY each against tradition's own published list)
| Tradition | Included? | Status term | Verify against |
|-----------|-----------|-------------|----------------|
| Protestant | [VERIFY] | canonical / apocryphal | [canon list] |
| Roman Catholic | [VERIFY] | protocanonical / deuterocanonical | [canon list] |
| Eastern Orthodox | [VERIFY — varies by jurisdiction] | canonical / anaginoskomena | [jurisdiction's list] |
| Ethiopian Orthodox | [VERIFY] | [status term] | [Ethiopian canon list] |
| Jewish (Tanakh) | [VERIFY] | Torah / Nevi'im / Ketuvim / not included | [Tanakh ordering] |

## Ordering and placement (VERIFY)
- [Tradition]: placed in [section] — structural logic: [..] — VERIFY
- [Tradition]: placed in [section] — structural logic: [..] — VERIFY

## Versification mapping (if passage specified — VERIFY every mapping)
| Reference system | Chapter:verse | Verify against |
|------------------|---------------|----------------|
| MT / Hebrew | [VERIFY] | [edition] |
| LXX / Greek | [VERIFY] | [edition] |
| Vulgate | [VERIFY] | [edition] |
| English (follows [MT/Vulgate/varies]) | [VERIFY] | [translation] |

- Psalm numbering: [framework explanation] — specific offsets VERIFY in Psalm numbering chart
- Superscription numbering: [framework explanation] — VERIFY per edition
- Chapter/verse boundary differences: [framework] — VERIFY
- Additional/fewer verses: [framework] — VERIFY

## Why the divergence (framework — historical reconstruction is debated)
- Second Temple diversity: [..]
- Hebrew vs. Greek text traditions: [..]
- Conciliar/synodal decisions: [..] — specific decisions VERIFY
- Reformation-era debates: [..]
- Numbering system inheritance (MT vs. LXX vs. Vulgate): [..]

## Confidence & next steps
- Canon-inclusion confidence: low without verification against each tradition's published list
- Versification confidence: low without verification against numbered editions
- Most important verification step: [..]
```

---

## Verification

- [ ] Every canon-inclusion claim flagged verify-required against the specific tradition's own published canon list; none asserted from memory as settled.
- [ ] Every versification mapping (Psalm numbers, chapter/verse splits, verse counts) flagged verify-required against the relevant numbered editions; none asserted from memory.
- [ ] Book naming differences across traditions surfaced and flagged verify-required; naming-confusion risks identified (e.g., Esdras numbering).
- [ ] Each tradition's canon described using that tradition's own terminology (deuterocanonical, anaginoskomena, apocryphal, etc.) without privileging one label.
- [ ] Distinct canonical traditions not conflated (e.g., Greek Orthodox vs. Ethiopian Orthodox distinguished).
- [ ] Canon-formation history presented as a framework with scholarly debate acknowledged, not as settled narrative.
- [ ] No conciliar decisions, synodal decrees, or canon-list dates fabricated from memory; all flagged verify-required.

---

## False-Positive Prevention

❌ **DON'T:**
- Assert "the Catholic canon includes book X" or "Psalm 10 in the MT is Psalm 9 in the LXX" from memory — these are exactly the claims that require verification against each tradition's own sources.
- Treat one tradition's canon as the baseline and describe other traditions as having "extra" or "missing" books — each tradition defines its own canon on its own terms.
- Conflate Eastern Orthodox jurisdictions (Greek, Russian, Serbian, etc.) into a single canon when their lists may differ at the margins.
- Fabricate a conciliar decision, synodal decree, or canon-list publication date to anchor a claim.

✅ **DO:**
- Explain the framework of why canons and versification diverge (historical, theological, textual-tradition reasons) clearly enough that the user understands the *kind* of difference before looking up the specifics.
- Flag every specific inclusion/exclusion, numbering, and naming claim as verify-required and name the source type (tradition's published canon list, numbered edition, Psalm numbering chart).
- Use each tradition's own terminology and present each tradition's rationale on its own terms, without evaluating whose canon is correct.

---

## Techniques Used

- **ST-01 (Role & Objective Priming):** Frames the model as a comparison-scaffold builder, not a canon authority — the objective is an explicitly verify-required map across traditions, which sets the anti-fabrication posture before any datum is offered.
- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Fix target → Canon inclusion → Ordering → Versification → Naming → Framework) separates the three distinct questions (canon, ordering, naming) that are routinely conflated, and defers every specific datum to verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Forces analysis across the distinct axes of divergence — inclusion, ordering, versification, naming, and historical cause — so no single axis is mistaken for the whole picture.
- **QA-04 (Uncertainty Acknowledgment):** Every canon-inclusion, versification, and naming claim carries a verify-required flag; canon-formation history is presented as scholarly debate, not settled narrative; confidence is stated as low without verification.
- **NE-14 (Fabrication Prevention):** Bars asserting canon lists, Psalm-numbering offsets, chapter/verse mappings, conciliar decisions, and publication dates from memory; each is routed to the tradition's own published canon list or numbered edition.
