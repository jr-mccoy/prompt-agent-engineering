---
title: "Hebrew Syntax & Grammar Analysis (Biblical Hebrew / Aramaic) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Structure a disciplined syntactic analysis of a Biblical Hebrew (or Aramaic) clause the user supplies — the verbal system and aspect/tense debate, waw-consecutive, construct chains, word order and clause types, and particles — treating every syntactic label as candidate / verify-required, routing to standard reference grammars (flagged verify, no section/page numbers from memory), and attributing syntax-dependent interpretive divergence to streams without ruling."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - hebrew
  - aramaic
  - syntax
  - verbal-system
  - construct-chain
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md
  - domain-biblical-studies/original-languages/biblical_language_greek_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_discourse_analysis.md
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md
---

# Hebrew Syntax & Grammar Analysis (Biblical Hebrew / Aramaic)

**Objective:** Take one Biblical Hebrew (or Aramaic) clause the user supplies and structure a disciplined analysis of its syntax — the contribution of the verbal system (with the aspect/tense/sequence debate held open), waw-consecutive forms, construct chains, word order and clause types, and particles — **without asserting syntactic labels as authoritative or fabricating grammar citations.** The output is a labeled analysis scaffold the user verifies against real reference grammars.

> **STRONG-GUARD prompt.** This is among the highest-fabrication-risk prompts in the domain. Models routinely assign confident labels (a "waw-consecutive imperfect = simple past," a "genitive construct of material") and cite grammar sections that are misremembered or invented. Every label here is **candidate / verify-required**, and **specific grammar citations (author, section, page) are flagged verify-required — never asserted from memory.** The Hebrew verbal system in particular is genuinely contested; this prompt presents frameworks, it does not rule.

**When to use:**
- You want to understand how a Hebrew/Aramaic clause is built and what its syntax contributes to meaning.
- You're weighing how a syntactic choice (verb form, construct relation, word order) affects interpretation.
- You're preparing the grammatical layer of an exegesis or paper.

**When NOT to use:**
- You need an authoritative grammatical ruling — go to standard reference grammars and a commentary's grammatical notes. This prompt scaffolds and cross-examines; it does not replace them.
- Your question is the *parse* of a single form rather than its function — use `biblical_language_parsing_morphology_helper.md`.
- Your question is clause-flow across a paragraph (prominence, cohesion, episode boundaries) — use `biblical_language_discourse_analysis.md`.

**Audience:** Seminary/academic (A) and pastors (P) with Hebrew and access to reference grammars.

---

## Inputs / Context

1. **The Hebrew/Aramaic text.** The clause (pointed/unpointed script and/or transliteration) and its verse reference, pasted by the user; the model references by address and does not quote from memory.
2. **Parsing (optional but recommended).** Any parsing the user has confirmed in a tool — supplied so the model analyzes function rather than re-inventing forms (stem/binyan, conjugation, person/gender/number).
3. **Translation alongside (optional).** A named translation, for orientation.
4. **The syntactic question (optional).** A specific focus (e.g., "Is this construct chain genitive of material or of purpose?" "What's the discourse force of this wayyiqtol?").
5. **Language.** Biblical Hebrew or Biblical/Targumic Aramaic — sets the right verbal system.

---

## Constraints

### Must
- Treat every syntactic label (verb-form function, construct relation, word-order significance, clause type, particle force) as **candidate / verify-required** unless it rests on a user-supplied verified parse.
- Distinguish **morphology (the parse)** from **syntax (the function)**: route parsing to the parsing helper; only function is analyzed here, and even function is candidate.
- Hold the **Hebrew verbal system debate open**: present qatal/yiqtol/wayyiqtol/weqatal contributions in terms of competing frameworks (aspect-prominent, tense-prominent, discourse/sequence-prominent) rather than asserting one as the meaning.
- For any label, name the *kind* of resource that adjudicates it (a standard reference grammar, an intermediate Hebrew grammar, a syntactical/discourse grammar, a commentary's grammatical notes) and **flag specific citations (section/page) as verify-required.**
- State confidence on each syntax-dependent interpretive payoff and what would change it.

### Must Not
- Assert a verb-form's force as settled (e.g., "wayyiqtol always = simple past"), or present a construct-chain category as objective fact.
- Fabricate or assert specific grammar citations (author, section, page) from memory; name the resource *type* and flag verify-required instead.
- Invent or assert morphology/parsing or vocalization from memory; route parsing to the parsing helper and treat pointing as data to verify.
- Quote a grammar or commentary verbatim from memory.
- Use a syntactic choice to smuggle in a contested doctrinal conclusion; misquote the text (reference by address, use supplied forms).

### Tradition-neutral stance (Must / Must Not)
- **Must:** where syntax bears on a contested reading, lay out the options and attribute the resulting interpretations to identifiable streams descriptively.
- **Must Not:** privilege the syntactic analysis that favors any tradition's conclusion, or present a contested grammatical reading as the plain construction.

---

## Instructions

### Step 1 — Orient and confirm the form base
Restate the clause and reference. Confirm the parse base: echo user-supplied parsing (stem, conjugation, PGN) as **supplied-by-user**; if absent, note "parsing not confirmed — verify in a morphological tool first" and route to `biblical_language_parsing_morphology_helper.md`. Treat vocalization/pointing as verify-required.

### Step 2 — Clause type and word order
Identify whether the clause is verbal or nominal/verbless; note the word order and whether it is marked (fronting for emphasis/topic) — flagged **candidate (verify)**, since word-order significance is interpreted, not automatic.

### Step 3 — Verbal system (frameworks, not a ruling)
For the finite verb(s), describe the candidate discourse/aspectual/temporal contribution under the competing frameworks, naming the form (qatal/yiqtol/wayyiqtol/weqatal, or Aramaic equivalents) and what each framework would make of it. Do not declare a single "correct" force.

### Step 4 — Construct chains and nominal relations
For construct chains and other nominal relations, offer candidate relation labels (e.g., possessive, material, attributive, objective), each flagged **candidate (verify)**, with what would disambiguate them. Note where the relation is genuinely debated.

### Step 5 — Particles, conjunctions, discourse markers
Analyze candidate force of key particles and conjunctions (waw and its functions, common particles), flagged candidate, routed to a reference grammar; note that many particles are multivalent.

### Step 6 — Syntax → interpretation
State how the syntax bears on meaning, each payoff tagged **text/grammar-supported (verify)** or **inference (stream)**. Where syntax-dependent readings diverge, attribute them to streams without ruling.

### Step 7 — Confidence + verification map
Give confidence on the central syntactic conclusion and the single most important verification step. List resource *types* to consult, with specific citations flagged verify-required.

---

## Output Format

```
# Hebrew/Aramaic Syntax — [reference]

## Orientation
- Clause (supplied): [..] | Parse base: [supplied-by-user | unconfirmed — verify first]
- Language: [Biblical Hebrew | Aramaic] | Question: [..]

## Clause type & word order
- Verbal / nominal(verbless): [..]
- Word order & markedness (candidate, verify): [..]

## Verbal system (competing frameworks — no single ruling)
- Form: [qatal/yiqtol/wayyiqtol/weqatal/Aramaic equiv.]
- Aspect-prominent framework would read: [..]
- Tense-prominent framework would read: [..]
- Discourse/sequence framework would read: [..]

## Construct chains & nominal relations (candidate — VERIFY)
| Relation | Candidate label | Alt(s) | Disambiguated by | Verify in |
|----------|-----------------|--------|------------------|-----------|
| [..] | candidate (verify) | [..] | [..] | reference grammar (section flagged verify) |

## Particles / conjunctions / discourse markers (candidate)
- [particle]: candidate force [..] (multivalent — verify)

## Syntax → interpretation
- [payoff] — grammar-supported (verify)
- [payoff] — inference ([stream])
- Divergent syntax-dependent readings: [Option A — stream] | [Option B — stream]

## Confidence & verification map
- Central conclusion: [..] (confidence: low/mod/high; would change if ..)
- Consult (specific citations verify-required): [reference grammar], [intermediate grammar], [discourse/syntactical grammar], [commentary notes]
```

---

## Verification

- [ ] Every syntactic label flagged candidate/verify-required; none asserted as objective fact.
- [ ] Morphology/parsing/pointing not invented; function analysis rests on a confirmed or flagged-unconfirmed parse.
- [ ] Hebrew verbal system presented as competing frameworks, not a single ruling.
- [ ] No specific grammar citation (author/section/page) asserted from memory — resource types named, citations flagged verify.
- [ ] No grammar or commentary quoted from memory; text referenced by address.
- [ ] Syntax-dependent interpretive divergence attributed to streams, not adjudicated.
- [ ] Central conclusion carries confidence + a change condition.

---

## False-Positive Prevention

❌ **DON'T:**
- Declare "wayyiqtol = simple past" (or any verb form's force) as if the verbal-system debate were closed.
- Cite "GKC §___," "Joüon-Muraoka §___," or "Waltke-O'Connor p. ___" from memory — routinely misremembered or invented.
- Hand down a single construct-chain category as objective fact.
- Build function analysis on parsing or pointing you invented rather than data the user verified.
- Let the verb-form or construct reading that supports a doctrine win without naming the alternative.

✅ **DO:**
- Flag every label candidate (verify) and route it to a reference grammar.
- Present the verbal system under competing frameworks attributed to grammarians/streams.
- Name the resource *type* and mark any specific citation verify-required.
- Anchor function on a confirmed parse, or flag the parse as unconfirmed first.
- State confidence and the single most decisive verification step.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 7-step sequence (Orient → Clause type/order → Verbal system → Construct chains → Particles → Interpretation → Confidence) prevents leaping from a recalled label to a doctrinal payoff.
- **RT-02 (Multi-Dimensional Analysis Framework):** Requires analysis across the distinct syntactic dimensions — clause type, word order, the verbal system, construct/nominal relations, and particles — so no single layer stands in for the whole.
- **RT-05 (Evidence-Based Reasoning):** Every label is grounded in a named reference-grammar type or flagged unverified; the verbal system is presented as competing frameworks rather than a settled fact.
- **QA-04 (Uncertainty Acknowledgment):** Labels are flagged candidate (verify); the verbal-system debate is held open; the central conclusion carries a low/moderate/high confidence with a change condition.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* for each label and explicitly flags specific grammar citations (author/section/page) as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The verification map catalogs the resource types (reference grammar, intermediate grammar, discourse/syntactical grammar, commentary notes) needed to validate each syntactic claim.
