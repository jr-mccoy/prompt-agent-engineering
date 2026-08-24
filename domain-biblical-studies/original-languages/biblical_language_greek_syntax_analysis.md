---
title: "Greek Syntax & Grammar Analysis (NT / LXX) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Structure a disciplined syntactic analysis of a Greek clause the user supplies — case functions, tense-aspect/Aktionsart, mood, voice, clause types, participles, and conditional structures — treating every syntactic label as candidate / verify-required, routing to standard reference grammars (flagged verify, no page/section numbers from memory), and attributing syntax-dependent interpretive divergence to streams without ruling."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - greek
  - syntax
  - grammar
  - tense-aspect
  - participles
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_discourse_analysis.md
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md
---

# Greek Syntax & Grammar Analysis (NT / LXX)

**Objective:** Take one Greek clause or sentence the user supplies and structure a disciplined analysis of its syntax — the *functions* of cases, the contribution of tense-form/aspect, the force of mood and voice, clause relationships, participles, and conditional structures — **without asserting syntactic labels as authoritative or fabricating grammar citations.** The output is a labeled analysis scaffold the user verifies against real reference grammars.

> **STRONG-GUARD prompt.** This is among the highest-fabrication-risk prompts in the domain. Models routinely assign confident syntactic labels (a "genitive of source," a "constative aorist," a "first-class condition") and cite grammar sections that are misremembered or invented. Every label here is **candidate / verify-required**, and **specific grammar citations (author, section, page) are flagged verify-required — never asserted from memory.**

**When to use:**
- You want to understand how a Greek clause is constructed and what its syntax contributes to meaning.
- You're weighing how a syntactic choice (a case function, an aspect, a participle's relation) affects interpretation.
- You're preparing the grammatical layer of an exegesis or paper.

**When NOT to use:**
- You need an authoritative grammatical ruling — go to standard reference grammars and a commentary's grammatical notes. This prompt scaffolds and cross-examines; it does not replace them.
- Your question is the *parse* of a single form rather than its function — use `biblical_language_parsing_morphology_helper.md`.
- Your question is clause-flow across a paragraph (prominence, cohesion) rather than syntax within a clause — use `biblical_language_discourse_analysis.md`.

**Audience:** Seminary/academic (A) and pastors (P) with Greek and access to reference grammars.

---

## Inputs / Context

1. **The Greek text.** The clause/sentence (script and/or transliteration) and its verse reference, pasted by the user; the model references by address and does not quote from memory.
2. **Parsing (optional but recommended).** Any parsing the user has confirmed in a tool — supplied so the model analyzes function rather than re-inventing forms.
3. **Translation alongside (optional).** A named translation of the clause, for orientation.
4. **The syntactic question (optional).** A specific focus (e.g., "What is the force of this participle?" "Is this a genitive of source or objective genitive?").
5. **Purpose.** Learning / exegesis / claim-checking — sets depth.

---

## Constraints

### Must
- Treat every syntactic label (case function, aspect/Aktionsart, mood force, voice nuance, clause type, participle relation, conditional class) as **candidate / verify-required** unless the user supplied a verified parse it rests on.
- Distinguish **morphology (the parse)** from **syntax (the function)**: the parse should come from a tool (route to the parsing helper); only function is analyzed here, and even function labels are candidate.
- Where a category is genuinely debated among grammarians (e.g., the meaning of verbal aspect, the legitimacy of certain "case-function" taxonomies), present the competing frameworks descriptively rather than asserting one.
- For any label, name the *kind* of resource that adjudicates it (a standard reference grammar, an intermediate grammar, a syntactical commentary) and **flag specific citations (section/page) as verify-required.**
- State confidence on each syntax-dependent interpretive payoff and what would change it.

### Must Not
- Assert a syntactic label as settled when reasonable analysts could differ, or present a taxonomy category as objective fact.
- Fabricate or assert specific grammar citations (author, section number, page) from memory; name the resource *type* and flag verify-required instead.
- Invent or assert morphology/parsing from memory; route parsing to the parsing helper.
- Quote a grammar or commentary verbatim from memory.
- Use a syntactic choice to smuggle in a contested doctrinal conclusion; misquote the text (reference by address, use supplied forms).

### Tradition-neutral stance (Must / Must Not)
- **Must:** where syntax bears on a contested reading (e.g., a debated genitive, the force of an aorist, subjective vs. objective genitive), lay out the options and attribute the resulting interpretations to identifiable streams descriptively.
- **Must Not:** privilege the syntactic analysis that favors any tradition's conclusion, or present a contested grammatical reading as the plain construction.

---

## Instructions

### Step 1 — Orient and confirm the form base
Restate the clause and reference. Confirm the parse base: echo user-supplied parsing as **supplied-by-user**; if absent, note "parsing not confirmed — verify in a morphological tool first" and route to `biblical_language_parsing_morphology_helper.md`. Function analysis is only as reliable as the parse beneath it.

### Step 2 — Clause structure
Identify the main verb(s) and subject(s); map subordinate and coordinate clauses and how they relate (cause, purpose, result, condition, concession, temporal). Label each relationship **candidate (verify)**.

### Step 3 — Case functions (candidate)
For the key nominals, offer candidate case-function labels (e.g., subjective/objective genitive, dative of means, etc.), each flagged **candidate (verify)** and routed to a reference grammar. Where the function is debated, list the options and what disambiguates them.

### Step 4 — Verb syntax: tense-aspect, mood, voice
Analyze the contribution of the tense-form/aspect (noting that the *meaning* of verbal aspect is itself debated among grammarians — present frameworks, don't rule), the force of the mood, and the nuance of voice. All labels candidate; aspect framework attributed, not asserted.

### Step 5 — Participles and conditionals
For participles, offer candidate relation (adverbial: temporal/causal/concessive/etc.; adjectival; substantival) and tense-aspect contribution, flagged candidate. For conditionals, name the candidate class and the interpretive caution (conditional "classes" are conventional labels, not guarantees of real-world fact).

### Step 6 — Syntax → interpretation
State how the syntax bears on meaning, each payoff tagged **text/grammar-supported (verify)** or **inference (stream)**. Where syntax-dependent readings diverge, attribute them to streams without ruling.

### Step 7 — Confidence + verification map
Give confidence on the central syntactic conclusion and the one verification step that matters most. List the resource *types* to consult, with specific citations flagged verify-required.

---

## Output Format

```
# Greek Syntax — [reference]

## Orientation
- Clause (supplied): [..] | Parse base: [supplied-by-user | unconfirmed — verify first]
- Question: [..]

## Clause structure
- Main verb/subject: [..]
- Subordinate/coordinate relations (candidate, verify): [..]

## Case functions (candidate — VERIFY in a reference grammar)
| Nominal | Candidate function | Alt(s) | Disambiguated by | Verify in |
|---------|--------------------|--------|------------------|-----------|
| [..] | candidate (verify) | [..] | [..] | reference grammar (section flagged verify) |

## Verb syntax
- Tense-aspect/Aktionsart (candidate; aspect framework attributed, not ruled): [..]
- Mood force (candidate): [..]
- Voice nuance (candidate): [..]

## Participles & conditionals
- Participle(s) (candidate relation + aspect): [..]
- Conditional class (candidate label; not a fact-guarantee): [..]

## Syntax → interpretation
- [payoff] — grammar-supported (verify)
- [payoff] — inference ([stream])
- Divergent syntax-dependent readings: [Option A — stream] | [Option B — stream]

## Confidence & verification map
- Central conclusion: [..] (confidence: low/mod/high; would change if ..)
- Consult (specific citations verify-required): [reference grammar], [intermediate grammar], [syntactical commentary]
```

---

## Verification

- [ ] Every syntactic label flagged candidate/verify-required; none asserted as objective fact.
- [ ] Morphology/parsing not invented; function analysis rests on a confirmed or flagged-unconfirmed parse.
- [ ] No specific grammar citation (author/section/page) asserted from memory — resource types named, citations flagged verify.
- [ ] Debated categories (aspect meaning, case taxonomy, conditional classes) presented as frameworks, not rulings.
- [ ] No grammar or commentary quoted from memory; text referenced by address.
- [ ] Syntax-dependent interpretive divergence attributed to streams, not adjudicated.
- [ ] Central conclusion carries confidence + a change condition.

---

## False-Positive Prevention

❌ **DON'T:**
- Hand down a confident case-function or aspect label as if grammarians agree.
- Cite "Wallace, p. ___" or "BDF §___" from memory — these are routinely misremembered or invented.
- Treat conditional "classes" as guarantees about reality, or aspect labels as time-of-action facts.
- Build function analysis on a parse you invented rather than one the user verified.
- Let the genitive (or aspect) reading that supports a doctrine win without naming the alternative.

✅ **DO:**
- Flag every label candidate (verify) and route it to a reference grammar.
- Name the resource *type* and mark any specific citation verify-required.
- Present debated categories as competing frameworks attributed to grammarians/streams.
- Anchor function on a confirmed parse, or flag the parse as unconfirmed first.
- State confidence and the single most decisive verification step.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 7-step sequence (Orient → Clause structure → Case functions → Verb syntax → Participles/conditionals → Interpretation → Confidence) prevents leaping from a recalled label to a doctrinal payoff.
- **RT-02 (Multi-Dimensional Analysis Framework):** Requires analysis across the distinct syntactic dimensions — clause relations, case function, tense-aspect, mood/voice, participles, conditionals — so no single layer is mistaken for the whole.
- **RT-05 (Evidence-Based Reasoning):** Every label is grounded in a named reference-grammar type or flagged unverified; debated categories are presented as competing frameworks rather than settled facts.
- **QA-04 (Uncertainty Acknowledgment):** Labels are flagged candidate (verify); debated taxonomies are surfaced; the central conclusion carries a low/moderate/high confidence with a change condition.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* for each label and explicitly flags specific grammar citations (author/section/page) as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The verification map catalogs the resource types (reference grammar, intermediate grammar, syntactical commentary) needed to validate each syntactic claim.
