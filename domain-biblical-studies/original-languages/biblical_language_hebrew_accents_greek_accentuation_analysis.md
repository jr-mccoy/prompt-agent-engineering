---
title: "Hebrew Cantillation (Te'amim) & Greek Accentuation Analysis — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Help the user read the supralinear/sublinear marking systems of the biblical text — Hebrew cantillation accents (te'amim) as a reading-and-division tradition (disjunctive vs. conjunctive, major pausal breaks) and Greek accent/breathing marks (acute/grave/circumflex, rough/smooth, enclitics, accent-distinguished homographs) — treating every specific accent reading, disjunctive-rank claim, and pausal-division decision as candidate / verify-required against BHS/BHQ and standard grammars, never asserted from memory."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - NE-14
difficulty: advanced
tags:
  - hebrew
  - greek
  - cantillation
  - teamim
  - accentuation
  - anti-fabrication
updated: "2026-06-26"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_masora_and_variants_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md
  - domain-biblical-studies/original-languages/biblical_language_discourse_analysis.md
  - domain-biblical-studies/exegesis-interpretation/biblical_hebrew_poetry_psalms_reading.md
---

# Hebrew Cantillation (Te'amim) & Greek Accentuation Analysis

**Objective:** Take a marked text the user supplies and help them **read the accent/marking system** — for Hebrew, the cantillation accents (*te'amim*) as a combined musical, syntactic, and reading-division tradition (disjunctive vs. conjunctive accents, the hierarchy of pausal breaks); for Greek, the accent and breathing marks (acute/grave/circumflex, rough/smooth breathing, enclitics/proclitics, accent-distinguished homographs) — **without asserting any specific accent reading, disjunctive rank, or pausal-division decision from memory.** The output is a framework-plus-verification scaffold the user populates from BHS/BHQ and standard grammars.

> **STRONG-GUARD prompt.** Accent systems are high-fabrication-risk: models invent which accent stands on a word, misrank the disjunctive hierarchy (which accent makes the major break), assert pausal divisions the te'amim do not support, fabricate Greek accent placements, and over-claim that an accent "proves" a syntactic reading. Here, **every specific accent identification, disjunctive-vs-conjunctive call, pausal-break ranking, and Greek accent/breathing reading is verify-required** against the pointed/accented text (BHS/BHQ; a critical Greek text) and standard reference grammars (e.g., the te'amim systems described in standard Hebrew grammars; Greek accentuation in reference grammars). The model explains the **system**; the user verifies every specific mark.

**When to use:**
- You want to use the Hebrew te'amim to see how the Masoretes divided a verse (major disjunctives, pausal breaks) as a check on clause structure.
- You need to read a Greek word's accent/breathing — including accent-distinguished homographs (e.g., a form that means different things under different accentuation) and enclitic behavior.
- You are reading the text aloud or scanning poetry and need the marking system explained.

**When NOT to use:**
- You want the syntactic analysis of the clause itself — use the Hebrew/Greek syntax prompts (the te'amim can *support* a division, but the syntax prompt does the grammar).
- Your question is the Masorah notes or Qere/Ketiv — use `biblical_language_hebrew_masora_and_variants_analysis.md`.
- Your question is discourse-level clause flow across a paragraph — use `biblical_language_discourse_analysis.md`.
- Your question is the parse of a form — use the parsing helper.

**Audience:** Seminary/academic (A) and pastors (P), including those preparing to read/chant the text, with access to BHS/BHQ and reference grammars.

---

## Inputs / Context

1. **The marked text.** The Hebrew (with te'amim) or Greek (with accents/breathings) word, phrase, or verse — script and reference — pasted by the user; the model references by address and does not supply the accented text from memory.
2. **Which system / focus.** Hebrew te'amim (prose "21 books" system vs. the poetic system of Psalms-Proverbs-Job) or Greek accentuation — and whether the focus is verse division, reading aloud, or a homograph/enclitic question.
3. **Known data (optional).** Any accent identifications or divisions the user already has — supplied so the model organizes and explains, not invents, them.
4. **The question.** "How do the te'amim divide this verse?" / "What's the major pausal break?" / "What does this Greek accent tell me / which homograph is it?" — sets focus.

---

## Constraints

### Must
- Explain the **structure of the relevant system**: for Hebrew, that the te'amim are simultaneously cantillation (musical), accentuation (stress), and a **syntactic division system** (disjunctive accents segment, conjunctive accents join, in a ranked hierarchy of breaks), and that the **poetic books use a different accent system** than the prose books; for Greek, the three accents (acute/grave/circumflex), the two breathings (rough/smooth), enclitic/proclitic behavior, and accent-distinguished homographs.
- Treat every specific accent identification, disjunctive/conjunctive call, pausal-break ranking, and Greek accent/breathing reading as **verify-required** against the accented text and a standard grammar; never assert which accent stands on a word, or its rank, from memory.
- For Hebrew, clarify that the te'amim **reflect the Masoretes' reading of the syntax** — a weighty early witness to how the verse was understood — but are **not infallible** and can be weighed against the grammar, not treated as automatically decisive; route the actual syntactic call to the syntax prompt.
- For Greek, explain how accentuation can **disambiguate** (homographs, enclitic combinations) and flag each specific accent placement as verify-required.
- For any datum, name the *kind* of resource that confirms it (the accented edition, a grammar's te'amim/accentuation section) and **flag specific citations as verify-required.**
- State confidence and the single most important verification step.

### Must Not
- Assert which te'am stands on a word, its disjunctive/conjunctive rank, or the verse's pausal division from memory; never fabricate an accent or a division.
- Treat a te'amim division as automatically settling a disputed syntax/translation when grammar and context bear on it — present it as a weighty witness, not a proof.
- Assert a Greek word's accent/breathing placement, or resolve an accent-distinguished homograph, from memory; flag verify-required.
- Confuse the prose and poetic te'amim systems, or misname accents, without flagging the identification as verify-required.
- Fabricate references to grammars or to the accent literature; name the resource type and flag verify-required.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where the accentual division bears on a contested reading (e.g., a major disjunctive that supports one clause division — and translation — over another, as in classic punctuation cruxes), present the options and attribute the resulting readings to identifiable streams descriptively.
- **Must Not:** privilege the accentual division that favors any tradition's conclusion, or present the Masoretic division as either infallibly decisive or as irrelevant — describe its weight and let the user weigh it against the grammar.

---

## Instructions

### Step 1 — Fix the text and the system
Restate the marked word/phrase/verse and reference. Identify the system (Hebrew prose te'amim / Hebrew poetic te'amim / Greek accentuation) and confirm the focus. Echo any user-supplied accent data as **supplied-by-user**; if the accented text is not pasted, instruct the user to read it from BHS/BHQ or a critical Greek text — do not supply it from memory.

### Step 2 — Explain how this system works
Lay out the relevant framework: for Hebrew, the disjunctive/conjunctive distinction and the ranked hierarchy of breaks (major pausal accents segment the verse into ever-smaller units), noting the prose-vs-poetic system difference; for Greek, the accents, breathings, enclitic/proclitic rules, and how accent distinguishes homographs.

### Step 3 — Candidate reading of the marks (flagged)
For Hebrew: offer a **candidate** account of how the te'amim divide the user's verse — the major disjunctive(s), the resulting segmentation — each flagged **candidate (verify)** against the accented text. For Greek: offer a candidate reading of the accent/breathing and, if relevant, which homograph it selects — flagged candidate (verify).

### Step 4 — Weigh against grammar/context (do not over-claim)
State how the accentual division or accent reading **bears on** the syntax/translation, and route the actual grammatical decision to the syntax prompt. For Hebrew, present the te'amim division as a weighty Masoretic witness that can be weighed against, not as automatically decisive. For Greek, note where the accent genuinely disambiguates vs. where it is merely orthographic.

### Step 5 — Contested-division note
If the accentual reading bears on a contested clause division or translation, present the options and attribute the resulting readings to streams without ruling.

### Step 6 — Confidence + verification map
Give confidence (usually low without direct verification of the marks) and the one verification step that matters most. List the resource *types* to consult, specific citations flagged verify-required.

---

## Output Format

```
# Accents — [word/phrase/verse] in [reference]

## Text & system
- Marked text (supplied): [..] | Reference: [address]
- System: Hebrew prose te'amim | Hebrew poetic te'amim | Greek accentuation
- Focus: verse division | reading aloud | homograph/enclitic | other

## How this system works (framework)
- [Hebrew: disjunctive vs. conjunctive; ranked hierarchy of breaks; prose vs. poetic system]
- [Greek: acute/grave/circumflex; rough/smooth breathing; enclitics; accent-distinguished homographs]

## Candidate reading of the marks (VERIFY against the accented text)
- [Hebrew] Major disjunctive(s): [candidate] — segmentation: [candidate] — VERIFY in BHS/BHQ
- [Greek] Accent/breathing: [candidate] — homograph selected (if any): [candidate] — VERIFY

## Bearing on grammar / translation (not over-claimed)
- Supports division/reading: [..] — route grammatical decision to syntax prompt
- Te'amim weight: weighty Masoretic witness, not automatically decisive
- Greek: genuinely disambiguating | merely orthographic

## Contested-division note (if any)
- [Option A — stream] | [Option B — stream] — described, not adjudicated

## Confidence & verification map
- Confidence: low / moderate (pending verification of the marks)
- Most important next step: [verify accents in BHS/BHQ / critical Greek text]
- Consult (citations verify-required): [accented edition], [grammar's te'amim/accentuation section]
```

---

## Verification

- [ ] The relevant marking system explained at a framework level (Hebrew disjunctive/conjunctive hierarchy + prose/poetic distinction; Greek accents/breathings/enclitics/homographs).
- [ ] Every specific accent identification, disjunctive rank, pausal division, and Greek accent/breathing reading flagged verify-required; none asserted or fabricated from memory.
- [ ] Te'amim presented as a weighty Masoretic witness, not as automatically decisive; grammatical decision routed to the syntax prompt.
- [ ] Prose vs. poetic te'amim systems not confused; Greek homograph resolution flagged verify-required.
- [ ] No grammar or accent-literature reference quoted from memory; resource types named, citations flagged verify.
- [ ] Division-dependent interpretive divergence attributed to streams; confidence + next step stated.

---

## False-Positive Prevention

❌ **DON'T:**
- Assert "the athnach falls here, so the major break is X" or "this word carries a circumflex" from memory — verify the marks in the accented text.
- Treat the Masoretic accentual division as infallibly settling a disputed clause division or translation.
- Resolve a Greek accent-distinguished homograph from memory, or assert an accent placement to anchor a reading.
- Confuse the poetic te'amim system (Psalms-Proverbs-Job) with the prose system.
- Fabricate a grammar's accentuation section to lend authority.

✅ **DO:**
- Explain how the system works so the user can read the marks themselves.
- Flag every accent identification, rank, division, and Greek accent/breathing verify-required against the accented text.
- Present the te'amim as a weighty witness to be weighed against the grammar, and route the syntactic call to the syntax prompt.
- State confidence and the single most decisive verification step; attribute divergent divisions to streams.

---

## Techniques Used

- **ST-01 (Role & Objective Priming):** Frames the model as a guide to *reading the marking system*, not as a source of accent data — setting the verify-required posture before any mark is identified.
- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Fix text → Explain system → Candidate reading → Weigh against grammar → Contested division → Confidence) separates explaining the system from asserting any specific mark.
- **RT-02 (Multi-Dimensional Analysis Framework):** Treats the te'amim as simultaneously musical, accentual, and syntactic, and the Greek marks as accentual, phonological, and disambiguating — analyzing each role without collapsing them.
- **QA-04 (Uncertainty Acknowledgment):** Accent identifications, ranks, and divisions are candidate (verify); the te'amim are a weighty-but-fallible witness; confidence is stated as low without direct verification.
- **NE-14 (Fabrication Prevention):** Bars asserting specific accents, disjunctive ranks, pausal divisions, Greek accent/breathing placements, and grammar citations from memory; each is routed to BHS/BHQ, a critical Greek text, and a named grammar.
