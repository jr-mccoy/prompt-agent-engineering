---
title: "Original-Language Idiom & Figures-of-Speech Analysis (Greek / Hebrew / Aramaic) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Help the user identify and interpret idioms, fixed expressions, and figures of speech in an original-language phrase they supply — where a wooden, word-by-word reading misleads (e.g., Hebrew 'lifted up his eyes,' 'heart' as mind/will, anthropomorphism; Greek idiom and Semitic-influenced expressions) — treating every claimed idiom, idiomatic gloss, and figure classification as candidate / verify-required against lexica and reference grammars, and never inventing a cultural or idiomatic claim to explain a phrase."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - idiom
  - figures-of-speech
  - hebraism
  - metaphor
  - metonymy
  - anti-fabrication
updated: "2026-06-26"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/original-languages/biblical_language_semantic_domains_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
  - domain-biblical-studies/exegesis-interpretation/biblical_rhetorical_analysis.md
  - domain-biblical-studies/exegesis-interpretation/biblical_historical_cultural_context.md
---

# Original-Language Idiom & Figures-of-Speech Analysis

**Objective:** Take an original-language phrase the user supplies and help them decide whether it is an **idiom or figure of speech** that a literal, word-by-word rendering would distort — naming the candidate figure (idiom, metaphor, metonymy, synecdoche, hendiadys, anthropomorphism, litotes, euphemism, merism, etc.), explaining what the figure does, and routing every idiomatic claim to a real lexicon or grammar — **without inventing an idiom, a cultural background, or an idiomatic meaning to make a phrase "work."** The output is an interpretive scaffold the user verifies, not an idiom dictionary recited from memory.

> **STRONG-GUARD prompt.** Idiom and figure analysis is high-fabrication-risk: models invent "Hebrew idioms" and "ancient figures of speech" wholesale, assert that a phrase "literally means X in the Hebrew" when it does not, fabricate cultural backstories to license a metaphor, and over-spiritualize ordinary expressions. Here, **every claimed idiom, idiomatic gloss, figure classification, and cultural explanation is candidate / verify-required** against lexica (BDAG, HALOT, DCH, BDB, LSJ), reference grammars, and figure-of-speech reference works; **nothing is asserted from memory as an established idiom**, and a phrase is never declared figurative (or literal) without warrant.

**When to use:**
- A phrase reads oddly when taken word-for-word and you suspect an idiom or figure.
- You want to avoid either flattening a figure into woodenness or over-reading an ordinary expression as a loaded metaphor.
- You are checking a commentary's or translation's claim that a phrase is "a Hebrew/Greek idiom for X."

**When NOT to use:**
- Your question is the semantic range of a single word — use the word-study prompt, or `biblical_language_semantic_domains_analysis.md` for sense-disambiguation method.
- Your question is the *rhetorical strategy* of a passage at the discourse/argument level (English-text rhetoric) rather than a figure in the original-language wording — use `biblical_rhetorical_analysis.md` in `exegesis-interpretation/`.
- Your question is the historical/cultural background behind a practice or image — use `biblical_historical_cultural_context.md`.
- You need the syntax of the clause — use the Greek/Hebrew syntax prompts.

**Audience:** Seminary/academic (A) and pastors (P) with original-language access and lexica.

---

## Inputs / Context

1. **The phrase.** The original-language phrase (script and/or transliteration) and its verse reference, pasted by the user; the model references by address and does not quote from memory.
2. **A literal gloss (optional).** The user's own word-by-word rendering, if they have one — supplied so the model can compare literal vs. idiomatic candidates.
3. **A translation alongside (optional).** How a named translation renders the phrase, which often signals an idiomatic reading.
4. **Any idiomatic claim being checked (optional).** A commentary/translation note asserting "this is an idiom for X" the user wants evaluated rather than trusted.
5. **The question.** "Is this an idiom?" / "What figure is this and what does it do?" / "Is this claim about a Hebrew idiom legitimate?" — sets focus.

---

## Constraints

### Must
- Distinguish **literal**, **idiomatic/figurative**, and **ambiguous** as live options, and require warrant before declaring a phrase figurative *or* insisting it is literal — both are interpretive claims.
- Treat every claimed idiom, idiomatic gloss, and figure classification as **candidate / verify-required** against a named lexicon, reference grammar, or figures-of-speech reference work; the relevant lexicon entry often labels an expression idiomatic — route the user there.
- Name the **candidate figure** precisely (idiom, dead vs. live metaphor, metonymy, synecdoche, merism, hendiadys, anthropomorphism/anthropopathism, litotes, hyperbole, euphemism, irony) and explain *what it does* to meaning, with the limits of the identification.
- Flag the difference between a **conventionalized/dead idiom** (where the figurative sense is the lexicalized meaning — verify in the lexicon) and a **live figure** (an author's fresh image — interpreted from context), since they are evaluated differently.
- Where a figure depends on a **cultural background**, treat that background as **verify-required** (route to the historical-cultural prompt / ANE or Greco-Roman reference works); never supply a cultural backstory from memory to license the reading.
- State confidence on the figurative reading and the single most important verification step.

### Must Not
- Invent an idiom, fixed expression, or cultural practice to explain a phrase; never assert "this is a known Hebrew/Greek idiom for X" from memory.
- Claim a phrase "literally says X in the original" when the literal morphemes do not say that, or use a fabricated literal layer to set up a "but it really means" move.
- Over-spiritualize an ordinary expression into a loaded metaphor without textual or lexical warrant, or flatten a genuine figure into woodenness.
- Fabricate or assert specific lexicon/grammar citations (entry, section, page) from memory; name the resource *type* and flag verify-required.
- Quote a lexicon, grammar, or figure-of-speech reference verbatim from memory.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where the literal-vs-figurative decision bears on a contested reading (e.g., whether a phrase is anthropomorphic figure or literal description, whether an image is metaphor or prediction), present the options and attribute the resulting readings to identifiable streams descriptively.
- **Must Not:** privilege the literal-or-figurative classification that favors any tradition's conclusion, or let a figure-of-speech label (e.g., "this is just anthropomorphism" or "this is literal") settle a doctrinal dispute by fiat.

---

## Instructions

### Step 1 — Fix the phrase and the literal layer
Restate the phrase and reference. Lay out the **defensible** word-by-word sense (only what the morphemes actually carry — route uncertain glosses to the word-study prompt rather than inventing them). Echo any user-supplied literal gloss as **supplied-by-user**. Do not manufacture a literal meaning to contrast with an idiom.

### Step 2 — Is a figure even in play?
Assess whether the phrase plausibly is idiomatic/figurative at all: does the literal sense fit the context, or does it generate oddity, category error, or impossibility (a classic figure trigger)? Mark the result **literal (candidate)**, **figurative (candidate)**, or **ambiguous**, with the trigger named. Resist declaring a figure where the literal sense fits.

### Step 3 — Name the candidate figure(s)
If figurative, name the candidate figure type(s) and explain what each does to meaning. Distinguish a **dead/conventionalized idiom** (verify the lexicalized sense in the lexicon) from a **live figure** (interpret from context). List more than one candidate where the data allow.

### Step 4 — Route the idiomatic claim to verification
For each candidate idiom/figure, name where it is confirmed: the lexicon entry (which often flags idiomatic usage), a reference grammar's discussion of the construction, or a figures-of-speech reference work — with specific citations flagged verify-required. If the user supplied a commentary's idiom claim, evaluate *how* to verify it rather than ratifying it.

### Step 5 — Cultural-background dependency (if any)
If the figure leans on a cultural image or practice, flag that background as **verify-required** and route to the historical-cultural / ANE / Greco-Roman background prompt and reference works. Do not supply the background from memory.

### Step 6 — Figure → interpretation + confidence
State how the figurative (or literal) reading bears on meaning, each payoff tagged **lexically/contextually supported (verify)** or **inference (stream)**. Attribute divergent literal-vs-figurative readings to streams without ruling. Give confidence and the one verification step that matters most.

---

## Output Format

```
# Idiom / Figure — [phrase] in [reference]

## Phrase
- Original (supplied): [..] | Reference: [address]
- Defensible literal layer (only what the morphemes carry): [.. | uncertain glosses → word study]
- Translation alongside (supplied, optional): [..]

## Is a figure in play?
- Verdict: literal (candidate) | figurative (candidate) | ambiguous
- Trigger: [does the literal sense fit, or produce oddity/impossibility?]

## Candidate figure(s) (VERIFY each)
| Candidate figure | What it does to meaning | Dead idiom or live figure? | Verify in |
|------------------|-------------------------|----------------------------|-----------|
| [idiom/metonymy/...] | [..] | [lexicalized → lexicon | live → context] | [lexicon entry / grammar / figures ref — citation VERIFY] |

## Idiomatic-claim check (if user supplied a claim)
- Claim: [..] — how to verify: [lexicon entry / grammar section] — VERIFY (not ratified here)

## Cultural-background dependency
- Background required: [.. | none] — VERIFY in [historical-cultural prompt / ANE / Greco-Roman ref] — not supplied from memory

## Figure → interpretation
- [payoff] — supported (verify)
- [payoff] — inference ([stream])
- Divergent literal-vs-figurative readings: [Option A — stream] | [Option B — stream]

## Confidence & next step
- Figurative-reading confidence: low / moderate / high
- Most important verification step: [..]
```

---

## Verification

- [ ] Literal, figurative, and ambiguous treated as live options; no phrase declared figurative or literal without warrant.
- [ ] No idiom, fixed expression, or cultural practice invented to explain the phrase; no "known Hebrew/Greek idiom for X" asserted from memory.
- [ ] No fabricated literal layer used to set up a "but it really means" move; uncertain glosses routed to word study, not guessed.
- [ ] Dead/conventionalized idiom (lexicon-verified) distinguished from live figure (context-interpreted).
- [ ] Each candidate figure routed to a named lexicon/grammar/figures resource; specific citations flagged verify-required; none quoted from memory.
- [ ] Cultural-background dependencies flagged verify-required and routed out, not supplied from memory.
- [ ] Literal-vs-figurative interpretive divergence attributed to streams, not adjudicated; confidence + next step stated.

---

## False-Positive Prevention

❌ **DON'T:**
- Invent "this is an ancient Hebrew idiom meaning X" or a cultural backstory to make a metaphor land.
- Claim "the Greek/Hebrew literally says X" when the morphemes don't, then pivot to "but it figuratively means Y."
- Over-spiritualize an ordinary phrase into a loaded metaphor, or flatten a real figure into wooden literalism.
- Cite a lexicon entry or "Bullinger, *Figures of Speech*, p. ___" from memory.
- Let "it's just anthropomorphism" or "it's literal" decide a doctrinal dispute by labeling.

✅ **DO:**
- Build only the defensible literal layer, and require a trigger (oddity/impossibility/context-misfit) before reading a figure.
- Name the candidate figure, say what it does, and distinguish a lexicalized idiom from a live image.
- Route every idiom/figure claim to a named lexicon, grammar, or figures reference with citations flagged verify-required.
- Flag cultural-background dependencies as verify-required and route them out.
- State confidence and the single most decisive verification step; attribute divergent readings to streams.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Literal layer → Is a figure in play? → Name figure → Route to verification → Cultural dependency → Interpretation) forces a warrant-before-figure discipline and prevents the "literally says X but means Y" move from inventing its own literal layer.
- **RT-02 (Multi-Dimensional Analysis Framework):** Separates the literal layer, the figure-type, the dead-vs-live distinction, and the cultural-background dependency so each is evaluated on its own evidence.
- **RT-05 (Evidence-Based Reasoning):** Every idiom/figure claim is grounded in a named lexicon/grammar/figures resource or flagged unverified; cultural backgrounds are routed to reference works rather than supplied from memory.
- **QA-04 (Uncertainty Acknowledgment):** Literal/figurative/ambiguous are live verdicts; each figure is candidate (verify); the figurative reading carries a confidence rating and a named next step.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* (lexicon entry, reference grammar, figures-of-speech work) for each claim and flags specific citations as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The output catalogs the specific real resources (lexica, grammars, figures references, background works) needed to validate each idiom/figure claim.
