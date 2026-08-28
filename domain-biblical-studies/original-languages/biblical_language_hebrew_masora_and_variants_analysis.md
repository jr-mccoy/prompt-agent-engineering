---
title: "Hebrew Masorah & Qere/Ketiv Analysis (BHS/BHQ) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Help the user read and interpret the Masoretic apparatus of a Hebrew text they supply — the Masorah parva/magna notes and Qere/Ketiv (written vs. read) divergences — explaining what the system encodes about transmission and reading tradition, while treating every specific Masoretic note, Qere/Ketiv reading, and frequency datum as verify-required against BHS/BHQ and Masoretic reference works, never asserted from memory."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - NE-14
difficulty: advanced
tags:
  - hebrew
  - masorah
  - qere-ketiv
  - masoretic-text
  - bhs
  - anti-fabrication
updated: "2026-06-26"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_textual_criticism_primer.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_greek_accentuation.md
  - domain-biblical-studies/original-languages/biblical_language_septuagint_usage.md
---

# Hebrew Masorah & Qere/Ketiv Analysis (BHS/BHQ)

**Objective:** Take a Hebrew text and its Masoretic notes (or a Qere/Ketiv the user is looking at) and help the user **read the Masoretic system** — what the Masorah parva (Mp), Masorah magna (Mm), and Qere/Ketiv apparatus encode about the transmission and the received reading tradition — **without asserting any specific Masoretic note, Qere/Ketiv reading, or frequency count from memory.** The output is a framework-plus-verification scaffold the user populates from BHS/BHQ and Masoretic reference works, not a reading recited from memory.

> **STRONG-GUARD prompt.** The Masorah is high-fabrication-risk: models invent Masoretic notes, misstate Qere/Ketiv readings, fabricate the hapax/frequency counts the Mp records, mis-explain Masoretic sigla and abbreviations, and confuse Qere/Ketiv with text-critical variants or with vocalization choices. Here, **every Masoretic note, Qere/Ketiv form, frequency datum, and siglum interpretation is verify-required** against BHS/BHQ and Masoretic reference works (e.g., the BHS Masorah, Weil's *Massorah Gedolah*, Yeivin's *Introduction to the Tiberian Masorah*). The model explains the **system**; the user verifies every specific datum.

**When to use:**
- You see a Qere/Ketiv (a *qere* "read" form differing from the *ketiv* "written" consonants) and want to understand what it signals.
- You want to read the small marginal Masoretic notes (Mp) — circellus markers, frequency notes, hapax indicators — and the cross-referencing Masorah magna (Mm).
- You are weighing whether a Masoretic note bears on a text-critical or interpretive decision.

**When NOT to use:**
- Your question is a manuscript variant evaluated by external/internal criteria (apparatus, text-types) — use `biblical_language_textual_criticism_primer.md`; Qere/Ketiv is a feature of the Masoretic reading tradition, not a manuscript apparatus.
- Your question is the cantillation accents (te'amim) and their function — use `biblical_language_hebrew_greek_accentuation.md`.
- Your question is the parse or syntax of a form — use the parsing or Hebrew syntax prompts.
- Your question is MT-vs-LXX divergence in content — use `biblical_language_septuagint_usage.md`.

**Audience:** Seminary/academic (A) and pastors (P) who can read pointed Hebrew and access BHS/BHQ.

---

## Inputs / Context

1. **The text and its notes.** The Hebrew word/phrase (script and/or transliteration), the verse reference, and — pasted by the user — the Masoretic note(s) or the Qere/Ketiv as they appear in BHS/BHQ. The model references by address and does not supply the apparatus from memory.
2. **What the user is looking at.** A Qere/Ketiv, an Mp note, an Mm cross-reference, or a siglum/abbreviation they cannot decode — sets the focus.
3. **Known data (optional).** Any reading, frequency, or note the user has already gathered — supplied so the model organizes and explains, not invents, it.
4. **Edition.** BHS, BHQ (where available), or another — different editions present the Masorah differently.
5. **The question.** "What does this Qere/Ketiv mean?" / "How do I read this Mp note?" / "Does this bear on the text or interpretation?" — sets depth.

---

## Constraints

### Must
- Explain the **structure of the Masoretic system** clearly: the Masorah parva (marginal frequency/usage notes keyed by the circellus), the Masorah magna (the fuller cross-referencing lists), the Masorah finalis, and the Qere/Ketiv mechanism (consonantal *ketiv* preserved in the text, *qere* vocalization/reading supplied in the margin) — so the user can interpret what they see.
- Treat every specific Masoretic note, Qere/Ketiv form, frequency/hapax count, and siglum reading as **verify-required** against BHS/BHQ and Masoretic reference works; never assert a specific note or count from memory.
- Distinguish the **types of Qere/Ketiv** as a framework (ordinary qere, qere perpetuum, *ketiv velo qere* / *qere velo ketiv*, euphemistic *tiqqune sopherim*-adjacent cases) without asserting that the user's instance is a given type — that classification is verify-required.
- Clarify what a Qere/Ketiv **is and is not**: a feature of the received reading tradition, which *may* reflect a variant, a correction, a euphemism, or a grammatical/orthographic convention — not automatically a "better original reading."
- For any datum, name the *kind* of resource that confirms it (the edition's Masorah, a Masoretic handbook, Weil's index for the Mm) and **flag specific citations as verify-required.**
- State confidence and the single most important verification step.

### Must Not
- Assert a specific Mp/Mm note, a Qere/Ketiv reading, or a frequency/hapax count from memory; never fabricate a Masoretic note to support a point.
- Decode a siglum or abbreviation with a confident meaning that is actually verify-required (Masoretic abbreviations are terse and edition-specific).
- Treat a Qere as automatically the "correct" or "original" reading over the Ketiv (or vice versa) — the relationship is interpreted, not assumed.
- Conflate Qere/Ketiv with the manuscript apparatus, with vocalization-only choices, or with *tiqqune/itture sopherim* traditions without flagging the distinctions as verify-required.
- Fabricate references to Yeivin, Weil, Ginsburg, or the BHS/BHQ Masorah; name the resource type and flag verify-required.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where a Qere/Ketiv or Masoretic note bears on a contested reading (e.g., a divine-name vocalization, a euphemistic substitution, a reading with doctrinal payoff), present the options and attribute the resulting readings to identifiable streams descriptively.
- **Must Not:** privilege the Qere or the Ketiv because it favors any tradition's conclusion, or present the Masoretic reading tradition as either uniquely authoritative or as obviously secondary — describe what it is and let the user weigh it.

---

## Instructions

### Step 1 — Fix the text and what the user is seeing
Restate the word/phrase, reference, and edition. Echo the user-supplied note or Qere/Ketiv as **supplied-by-user**. If the user has not pasted the apparatus, instruct them to read it directly from BHS/BHQ — do not supply the note from memory.

### Step 2 — Locate it in the Masoretic system
Identify which part of the apparatus is in view (Mp / Mm / Masorah finalis / Qere-Ketiv margin) and explain that component's function in one or two lines, so the user knows *what kind of note* they are reading.

### Step 3 — If Qere/Ketiv: explain the mechanism and candidate type
Explain the *ketiv* (written consonants) vs. *qere* (read form) relationship and how the vocalization signals it. Offer the **candidate type** of Qere/Ketiv (ordinary, *qere perpetuum*, *ketiv velo qere*, *qere velo ketiv*, euphemistic) — each flagged **candidate (verify)** — and what would confirm it. State plainly that neither member is automatically the better reading.

### Step 4 — If Mp/Mm note: explain how to decode it
Explain how the marginal note works (the circellus keys a word to its note; the Mp records frequencies/usages; the Mm gives the supporting list). Flag the specific count or cross-reference as **verify-required** in the edition's Masorah and, for the Mm, in Weil's index. Decode sigla only as candidate, routed to a Masoretic handbook.

### Step 5 — Bearing on text and interpretation
State whether the note/Qere-Ketiv plausibly bears on a text-critical question (route the actual evaluation to the textual-criticism prompt) or on interpretation. Tag each consequence **reading-dependent** and attribute divergent readings to streams without ruling.

### Step 6 — Confidence + verification map
Give confidence (usually low without direct verification) and the one verification step that matters most. List the resource *types* to consult, specific citations flagged verify-required.

---

## Output Format

```
# Masorah / Qere-Ketiv — [word/phrase] in [reference]

## Text
- Hebrew (supplied): [..] | Reference: [address] | Edition: [BHS | BHQ | other]
- Apparatus element in view: Mp | Mm | Masorah finalis | Qere/Ketiv

## What component this is (function)
- [one- to two-line explanation of the apparatus element]

## If Qere/Ketiv
- Ketiv (written, supplied): [..] | Qere (read, supplied): [..]
- Candidate type (VERIFY): ordinary | qere perpetuum | ketiv velo qere | qere velo ketiv | euphemistic
- Note: neither member is automatically the "original" reading

## If Mp / Mm note
- How to decode: [circellus → Mp note → Mm list]
- Specific count / cross-reference: [supplied-by-user | VERIFY in edition's Masorah / Weil index]
- Sigla decoded (candidate, verify in a Masoretic handbook): [..]

## Bearing on text / interpretation
- Text-critical relevance: [route evaluation to textual-criticism prompt] — VERIFY
- Interpretive consequence: [..] — reading-dependent
- Divergent readings: [Option A — stream] | [Option B — stream]

## Confidence & verification map
- Confidence: low / moderate (pending direct verification)
- Most important next step: [verify in BHS/BHQ Masorah / named handbook]
- Consult (citations verify-required): [edition Masorah], [Yeivin / Weil / Ginsburg — type named]
```

---

## Verification

- [ ] The Masoretic system's components (Mp, Mm, finalis, Qere/Ketiv) explained at a framework level so the user can interpret what they see.
- [ ] Every specific Masoretic note, Qere/Ketiv form, frequency/hapax count, and siglum reading flagged verify-required; none asserted or fabricated from memory.
- [ ] Qere/Ketiv type offered as candidate, not asserted; neither member treated as automatically original.
- [ ] Qere/Ketiv distinguished from the manuscript apparatus, vocalization-only choices, and sopherim traditions, with distinctions flagged verify-required.
- [ ] Text-critical evaluation routed to the textual-criticism prompt rather than resolved here.
- [ ] No reference to Yeivin/Weil/Ginsburg/BHS Masorah quoted from memory; resource types named, citations flagged verify.
- [ ] Reading-dependent interpretive divergence attributed to streams; confidence + next step stated.

---

## False-Positive Prevention

❌ **DON'T:**
- Assert "the Mp here notes this form occurs N times" or "the Qere reads X" from memory — these are exactly the data to verify in BHS/BHQ.
- Decode a Masoretic abbreviation with false confidence — the sigla are terse and edition-specific.
- Treat the Qere as the "correct" reading and the Ketiv as an error (or vice versa) by default.
- Conflate a Qere/Ketiv with a manuscript variant in the apparatus, or with a *tiqqun sopherim*, without flagging the distinction.
- Fabricate a citation to Yeivin's *Introduction* or Weil's *Massorah Gedolah*.

✅ **DO:**
- Explain how the apparatus element works so the user can read it themselves.
- Flag every note, reading, count, and siglum verify-required against the edition's Masorah and a named handbook.
- Offer the Qere/Ketiv type as a candidate and keep both members in play.
- Route the text-critical evaluation to the textual-criticism prompt.
- State confidence and the single most decisive verification step; attribute divergent readings to streams.

---

## Techniques Used

- **ST-01 (Role & Objective Priming):** Frames the model as a guide to *reading the Masoretic system*, not as a source of Masoretic data — setting the verify-required posture before any note is interpreted.
- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Fix text → Locate in system → Qere/Ketiv mechanism → Decode Mp/Mm → Bearing → Confidence) separates explaining the system from asserting any datum.
- **RT-02 (Multi-Dimensional Analysis Framework):** Distinguishes the apparatus components (Mp, Mm, finalis, Qere/Ketiv) and the question types (transmission, reading tradition, text-critical, interpretive) so they are not collapsed.
- **QA-04 (Uncertainty Acknowledgment):** Qere/Ketiv type and siglum decodings are candidate (verify); neither Qere nor Ketiv is privileged by default; confidence is stated as low without direct verification.
- **NE-14 (Fabrication Prevention):** Bars asserting specific Masoretic notes, Qere/Ketiv readings, frequency counts, and reference citations from memory; each is routed to BHS/BHQ and a named Masoretic reference work.
