---
title: "Greek Voice & Deponency Analysis — Middle, Passive & the Deponency Debate — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Help the user analyze the voice of a Greek verb form they supply — the interpretive contribution of middle and passive, the active/middle/passive distinctions, and the contested category of 'deponency' (and the newer middle-only / lexical-middle analyses that challenge it) — treating every voice label as candidate / verify-required, presenting the deponency debate as a live debate, and flagging grammar citations verify-required, never asserted from memory."
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
  - voice
  - middle-voice
  - deponency
  - passive
  - anti-fabrication
updated: "2026-06-26"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_greek_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_greek_verbal_aspect_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md
---

# Greek Voice & Deponency Analysis

**Objective:** Take one Greek verb form the user supplies and structure a disciplined analysis of its **voice** — what the middle or passive contributes to meaning, how the active/middle/passive distinctions function, and how to handle a form traditionally called "deponent" — **without asserting voice labels as settled or fabricating grammar citations.** Crucially, the prompt presents the **deponency debate** (traditional deponency vs. the newer view that Greek has a robust middle and "deponent" is often a mislabel for a genuine lexical middle) as a live debate, not a resolved question. The output is an analysis scaffold the user verifies against reference grammars, not a voice verdict.

> **STRONG-GUARD prompt.** Voice analysis is fabrication-prone: models hand down confident voice nuances ("direct middle," "permissive middle"), declare forms "deponent" as if that settles the meaning, assert that a middle/passive form is "really active" without warrant, and cite grammar sections (author/§/page) that are misremembered or invented. Here, **every voice label is candidate / verify-required**, the **deponency question is presented as contested**, and **specific grammar citations are flagged verify-required — never asserted from memory.**

**When to use:**
- You want to know what a middle or passive form contributes to meaning here, and whether the voice choice is doing real interpretive work.
- You hit a "deponent" form and want to know whether to treat it as semantically active, as a genuine middle, or as undecided.
- You are weighing a middle-vs-passive ambiguity (forms that are morphologically ambiguous between middle and passive).

**When NOT to use:**
- You need the *parse* (which voice the form is) — confirm that first in `biblical_language_parsing_morphology_helper.md`, noting that middle/passive can be morphologically ambiguous.
- You want the broader clause syntax (cases, clause relations, participles, conditionals) — use `biblical_language_greek_syntax_analysis.md`.
- Your question is aspect (the tense-form's viewpoint) — use `biblical_language_greek_verbal_aspect_analysis.md`.
- Your question is the verb's lexical meaning/range — use the word-study prompt.

**Audience:** Seminary/academic (A) and pastors (P) with Greek and access to reference grammars.

---

## Inputs / Context

1. **The verb form and clause.** The Greek verb (script and/or transliteration), its clause, and the verse reference — pasted by the user; the model references by address and does not quote from memory.
2. **Confirmed parse (recommended).** The voice (and any morphological middle/passive ambiguity) as verified in a tool — supplied so the analysis rests on the right form.
3. **The verb's lexical profile (optional).** Whether the lexicon lists this verb as middle/passive-only (a "deponent" / middle-only listing) — verify-required, but useful if the user has it.
4. **The question.** "What does the middle add here?" / "Is this 'deponent' meaningfully middle?" / "Middle or passive?" — sets focus.
5. **Purpose.** Learning / checking a voice claim / preparing exegesis — sets depth.

---

## Constraints

### Must
- Distinguish **morphology (which voice-form)** from **semantics (what the voice contributes)**: the parse comes from a tool; only the semantic contribution is analyzed here, and even that is candidate.
- Treat every voice-nuance label (direct/indirect/causative/permissive middle; agentive vs. non-agentive passive; etc.) as **candidate / verify-required**, and flag that many traditional middle "sub-categories" are themselves debated taxonomies.
- Present the **deponency debate** as live: state the traditional view (a "deponent" verb is middle/passive in form but active in meaning) and the newer view (Greek voice is a meaningful system; many "deponents" are genuine lexical middles, so "deponent" can obscure the middle's contribution) — attributed to streams, not adjudicated.
- Handle **middle/passive morphological ambiguity** (esp. certain tense-forms) by surfacing both readings and what would disambiguate them, rather than forcing one.
- For any label, name the *kind* of resource that adjudicates it (a standard reference grammar, an intermediate grammar, a middle-voice study) and **flag specific citations (author/section/page) as verify-required.**
- State confidence on any voice-dependent interpretive payoff and what would change it.

### Must Not
- Declare a form "deponent" as though that settles its meaning, or assert "this middle/passive is really active" without warrant and without flagging the deponency debate.
- Assign a confident middle sub-category (e.g., "this is a permissive middle") as if the morphology guarantees it.
- Force a single voice reading onto a form that is morphologically ambiguous between middle and passive.
- Fabricate or assert specific grammar citations (author, section, page) from memory; name the resource *type* and flag verify-required.
- Invent or assert the parse from memory; route parsing to the parsing helper.
- Quote a grammar or middle-voice study verbatim from memory.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where the voice reading bears on a contested interpretation (e.g., a middle vs. passive choice with theological payoff — "let yourselves be X" vs. "X yourselves" vs. "X happens to you"), present the options and attribute the resulting readings to identifiable streams descriptively.
- **Must Not:** privilege the voice analysis that favors any tradition's conclusion, or let a "deponent — therefore active" move erase a middle nuance that the text may carry.

---

## Instructions

### Step 1 — Orient and confirm the parse base
Restate the verb form, clause, and reference. Echo any user-confirmed parse as **supplied-by-user**, noting explicitly if the form is morphologically ambiguous between middle and passive. If the voice is unconfirmed, route to the parsing helper. Voice semantics rests on the parse beneath it.

### Step 2 — Frame the voice system
Briefly state what active, middle, and passive each do in Greek as a *system* (subject's relation to the action; the middle's subject-affectedness), so the user has the categories before any label.

### Step 3 — Candidate semantic contribution
Offer candidate readings of what the voice contributes here (for a middle: subject-affectedness, self-interest, reflexive/reciprocal nuance, etc.; for a passive: agent expressed/implied, divine passive as a *candidate* reading flagged verify) — each labeled **candidate (verify)** and routed to a reference grammar. Flag that middle sub-category taxonomies are debated.

### Step 4 — The deponency question (if applicable)
If the verb is traditionally called "deponent," present both the traditional analysis and the middle-only/lexical-middle critique, attributed to streams. Ask the load-bearing question: does treating it as a genuine middle change the reading? Frame the answer as options, not a ruling, and route the verb's lexical profile (middle-only listing) to the lexicon as verify-required.

### Step 5 — Middle/passive ambiguity
If the form is morphologically ambiguous, lay out the middle reading and the passive reading side by side, with what would disambiguate (context, agent expression, the verb's attested patterns — itself verify-required), without forcing one.

### Step 6 — Voice → interpretation + confidence
State how the voice reading bears on meaning, each payoff tagged **voice-supported (verify)** or **inference (stream)**. Attribute divergent voice-dependent readings to streams without ruling. Give confidence and the one verification step that matters most, with resource types named and specific citations flagged verify-required.

---

## Output Format

```
# Greek Voice & Deponency — [verb] in [reference]

## Orientation
- Verb / clause (supplied): [..] | Parse base: [supplied-by-user | unconfirmed → parsing helper]
- Morphological middle/passive ambiguity? [yes/no]
- Question: [..]

## Voice system (categories)
- Active / Middle / Passive — what each does (subject's relation; middle subject-affectedness)

## Candidate semantic contribution (VERIFY in a reference grammar)
| Reading | What it contributes | Confidence | Verify in |
|---------|---------------------|-----------|-----------|
| [middle nuance / passive nuance] | [..] | low/mod/high | reference grammar (section flagged verify) |
- ⚠ Middle sub-category taxonomies are debated — labels are conventional, not facts.

## Deponency question (if applicable — debate, not ruled)
- Traditional view: middle/passive form, active meaning — [attributed]
- Middle-only / lexical-middle critique: genuine middle; "deponent" obscures it — [attributed]
- Does reading it as a true middle change the sense? [options, not a verdict]
- Lexical profile (middle-only listing?): VERIFY in lexicon

## Middle/passive ambiguity (if applicable)
- Middle reading: [..] | Passive reading: [..]
- Disambiguated by: [context / agent / attested patterns — VERIFY]

## Voice → interpretation
- [payoff] — voice-supported (verify)
- [payoff] — inference ([stream])
- Divergent voice-dependent readings: [Option A — stream] | [Option B — stream]

## Confidence & verification map
- Central conclusion: [..] (confidence: low/mod/high; would change if ..)
- Consult (specific citations verify-required): [reference grammar], [intermediate grammar], [middle-voice study]
```

---

## Verification

- [ ] Morphology (which voice) distinguished from semantics (what the voice contributes); analysis rests on a confirmed or flagged-unconfirmed parse.
- [ ] Every voice-nuance label flagged candidate/verify-required; middle sub-category taxonomies flagged as debated.
- [ ] The deponency debate presented as live (traditional vs. middle-only/lexical-middle), attributed to streams, not adjudicated; "deponent → active" never used to erase a possible middle nuance.
- [ ] Middle/passive morphological ambiguity surfaced with disambiguating factors, not forced to one reading.
- [ ] No specific grammar/study citation (author/section/page) asserted from memory — resource types named, citations flagged verify.
- [ ] Voice-dependent interpretive divergence attributed to streams; central conclusion carries confidence + a change condition.
- [ ] Lexical "middle-only" profile routed to the lexicon as verify-required, not asserted.

---

## False-Positive Prevention

❌ **DON'T:**
- Declare a form "deponent" and treat that as settling its meaning, or say "this middle is really just active" without warrant.
- Assign "permissive middle" / "direct middle" as if the morphology guarantees the sub-category.
- Force a single reading onto a form that is ambiguous between middle and passive.
- Cite "Wallace, p. ___," "BDF §___," or a middle-voice monograph from memory.
- Let "deponent — therefore active" erase a middle nuance that carries the doctrinal payoff.

✅ **DO:**
- Separate the parse (from a tool) from the semantic contribution (candidate, verify).
- Present the deponency debate as live and ask whether a true-middle reading changes the sense.
- Surface middle/passive ambiguity and name what would disambiguate it.
- Name the resource *type* and flag specific citations verify-required.
- State confidence and the single most decisive verification step; attribute divergent readings to streams.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Orient → Frame system → Candidate contribution → Deponency question → Ambiguity → Interpretation) prevents leaping from a "deponent" label to a settled meaning.
- **RT-02 (Multi-Dimensional Analysis Framework):** Analyzes voice across distinct axes — the system, the candidate nuance, the deponency debate, and the middle/passive ambiguity — so none is mistaken for the whole.
- **RT-05 (Evidence-Based Reasoning):** Every label is grounded in a named reference-grammar type or flagged unverified; the deponency question is presented as competing frameworks attributed to streams rather than a settled fact.
- **QA-04 (Uncertainty Acknowledgment):** Labels are candidate (verify); debated taxonomies and the deponency debate are surfaced; ambiguous forms keep both readings; the central conclusion carries confidence and a change condition.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* for each label and flags specific grammar citations (author/section/page) as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The verification map catalogs the resource types (reference grammar, intermediate grammar, middle-voice study) needed to validate each voice claim.
