---
title: "Comparative Semitics & Cognate Analysis (Hebrew / Aramaic) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Help the user evaluate a comparative-Semitic / cognate argument about a Hebrew or Aramaic word or construction — weighing evidence from Ugaritic, Akkadian, Arabic, and other Semitic languages — while teaching the method's controls (attestation, semantic plausibility, illegitimate totality/cognate transfer) and treating every cognate form, gloss, and attestation claim as candidate / verify-required against the comparative lexica, never asserted from memory."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - comparative-semitics
  - cognates
  - ugaritic
  - akkadian
  - hebrew
  - anti-fabrication
updated: "2026-06-26"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/original-languages/biblical_language_semantic_domains_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_aramaic_analysis.md
  - domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md
  - domain-biblical-studies/exegesis-interpretation/biblical_ane_comparative_context.md
---

# Comparative Semitics & Cognate Analysis (Hebrew / Aramaic)

**Objective:** Take a Hebrew or Aramaic word, root, or construction the user is investigating with a **comparative-Semitic / cognate argument** (appeal to Ugaritic, Akkadian, Arabic, Aramaic, Phoenician, etc.) and help them evaluate that argument's strength — teaching the methodological controls and weighing the evidence — **without asserting any cognate form, gloss, attestation, or etymology from memory.** This is a *method-and-evaluation* prompt: it disciplines a notoriously abused move (illegitimate cognate transfer) and treats every comparative datum as candidate / verify-required against the comparative lexica.

> **STRONG-GUARD prompt.** Comparative Semitics is among the most fabrication-prone areas in biblical studies: models invent Ugaritic/Akkadian/Arabic cognates, fabricate glosses and attestations, assert etymologies and proto-Semitic roots with false confidence, and license "the Hebrew really means X because the Arabic cognate means X" — a textbook illegitimate transfer. Here, **every cognate form, gloss, attestation, and etymological claim is candidate / verify-required** against the comparative lexica (HALOT and DCH for Hebrew with cognate notes; CAD/AHw for Akkadian; DUL for Ugaritic; comparative-Semitic reference works), and **the method's controls are taught so the user can judge whether the cognate argument is sound or speculative.**

**When to use:**
- A commentary, lexicon note, or article argues a Hebrew/Aramaic word's meaning from a cognate in another Semitic language and you want to assess the argument.
- You are weighing whether a cognate appeal genuinely illuminates a word (esp. a rare word or hapax) or is overreaching.
- You want the methodological controls (attestation, semantic fit, directionality) before trusting a cognate claim.

**When NOT to use:**
- You want the word's senses and usage *within* Biblical Hebrew/Aramaic — start with `biblical_word_study_original_language.md` or `biblical_language_semantic_domains_analysis.md`; come here for the *cross-language* cognate evaluation.
- Your question is the cultural/ANE background of a practice or image (not the linguistics) — use `biblical_ane_comparative_context.md`.
- You want to check whether an interpretation commits an exegetical fallacy in general — use `biblical_exegetical_fallacy_detector.md` (this prompt is the cognate-specific deep dive).
- Your question is the Aramaic grammar of a passage — use `biblical_language_aramaic_analysis.md`.

**Audience:** Seminary/academic (A) primarily, and pastors (P) assessing a major study, with access to comparative-Semitic lexica.

---

## Inputs / Context

1. **The Hebrew/Aramaic word and the cognate claim.** The word/root (script and/or transliteration), the reference, and the comparative argument being evaluated (which language's cognate, what it is claimed to mean) — pasted by the user; the model references by address and does not supply cognates from memory.
2. **The source of the claim (optional).** Where the user encountered it (commentary, lexicon note, article) — supplied so the model evaluates the argument rather than ratifying it.
3. **Within-language data (optional).** The word's attested Hebrew/Aramaic senses, so cognate evidence is weighed *against* internal evidence, not in place of it.
4. **Why it matters.** Whether the word is rare/hapax (where cognate evidence carries more weight) or well-attested internally (where it carries less) — sets the evidential bar.
5. **The question.** "Is this cognate argument sound?" / "Does the Ugaritic/Akkadian really support this?" / "Am I over-reading the cognate?" — sets focus.

---

## Constraints

### Must
- Teach the **methodological controls** explicitly: (1) **attestation** — is the cognate actually attested, where, and how often (verify in the comparative lexicon)?; (2) **semantic plausibility** — is the proposed semantic link motivated, or a stretch?; (3) **internal-evidence priority** — within-language usage outweighs cognate evidence except where the word is rare/obscure; (4) **directionality and borrowing** — is this inheritance, areal borrowing, or a loanword, and does that change the inference?; (5) **the illegitimate-transfer guard** — a cognate's meaning is *evidence about*, not a *definition of*, the Hebrew/Aramaic word.
- Treat every cognate form, gloss, attestation, and etymological/proto-Semitic claim as **candidate / verify-required** against the comparative lexica; never assert a cognate or its meaning from memory.
- Weigh the cognate argument against the **internal Hebrew/Aramaic evidence**, and state the evidential bar (higher cognate weight for hapax/rare words, lower for well-attested ones).
- Rate the argument's strength (strong / plausible / speculative) **conditional on verification** — strong typically requires real attestation + clear semantic motivation + corroboration across more than one cognate or with context; Arabic-only or single-attestation appeals are flagged as weaker.
- For any datum, name the *kind* of resource that confirms it (HALOT/DCH cognate notes, CAD/AHw, DUL, comparative-Semitic reference works) and **flag specific citations as verify-required.**
- State confidence and the single most decisive verification step.

### Must Not
- Invent a cognate, its gloss, or its attestation in any Semitic language; never assert "the Ugaritic/Akkadian/Arabic cognate means X" from memory.
- Assert an etymology or a reconstructed proto-Semitic root as established; flag reconstructions verify-required and note that reconstruction is inferential.
- Commit or endorse illegitimate cognate transfer — importing a cognate's sense into the Hebrew/Aramaic word as if it defines it — or root-fallacy reasoning.
- Let cognate evidence override solid internal usage for a well-attested word.
- Fabricate or assert specific lexicon citations (entry, volume, page) from memory; name the resource *type* and flag verify-required.
- Quote a comparative lexicon or reference work verbatim from memory.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where the cognate-based reading bears on a contested interpretation, present the options and attribute the resulting readings to identifiable streams descriptively, distinguishing what the *linguistic* evidence (if verified) would support from what is interpretive inference.
- **Must Not:** privilege the cognate reading that favors any tradition's conclusion, or let a speculative cognate appeal carry doctrinal weight under the appearance of philological rigor.

---

## Instructions

### Step 1 — Fix the word and the cognate claim
Restate the Hebrew/Aramaic word/root, reference, and the exact cognate argument being evaluated (language, claimed cognate, claimed meaning). Echo any user-supplied data as **supplied-by-user**. If the cognate data is not supplied, instruct the user to gather it from the comparative lexica — do not supply cognates from memory.

### Step 2 — Establish the internal baseline and the evidential bar
Summarize the word's attested Hebrew/Aramaic usage (from the user's data or routed to the word-study prompt) and set the bar: is this a hapax/rare word (cognate evidence weighs more) or well-attested (cognate evidence weighs less)?

### Step 3 — Apply the attestation control
For the proposed cognate, ask: is it actually attested? Where, in what corpus, how often? Flag each attestation claim **verify-required** in the relevant comparative lexicon. An unverified or single-attestation cognate is flagged as weak evidence.

### Step 4 — Apply the semantic-plausibility and directionality controls
Assess whether the proposed semantic link is motivated or a stretch, and whether the relationship is inheritance, borrowing, or loanword — each affects the inference. Flag reconstructions and proto-Semitic roots as inferential and verify-required.

### Step 5 — Guard against illegitimate transfer
State explicitly that the cognate's meaning is evidence *about* the Hebrew/Aramaic word, not a substitute definition. Flag any move that imports the cognate sense wholesale, or that argues from a shared root to a shared meaning (root fallacy).

### Step 6 — Rate strength + interpretation + confidence
Rate the argument strong / plausible / speculative **conditional on verification**, weighing cognate vs. internal evidence. State how the (verified) reading would bear on meaning, tagged **linguistically supported (verify)** or **inference (stream)**, attributing divergent readings to streams. Give confidence and the single most decisive verification step.

---

## Output Format

```
# Comparative Semitics — [Hebrew/Aramaic word] in [reference]

## Word & cognate claim
- Word/root (supplied): [..] | Reference: [address]
- Cognate argument: [language] cognate [form] claimed to mean [..] — source: [..]
- Cognate data: [supplied-by-user | not gathered — look up in comparative lexica]

## Internal baseline & evidential bar
- Attested Hebrew/Aramaic usage: [.. | route to word study]
- Bar: hapax/rare (cognate weighs more) | well-attested (cognate weighs less)

## Control 1 — Attestation (VERIFY)
- Cognate attested? where / how often: [VERIFY in CAD/AHw | DUL | HALOT-DCH notes | ...]
- Single-attestation / unverified → weak evidence

## Control 2 — Semantic plausibility & directionality
- Semantic link: motivated | a stretch
- Relationship: inheritance | areal borrowing | loanword — affects inference
- Etymology / proto-Semitic root (if invoked): inferential — VERIFY

## Control 3 — Illegitimate-transfer guard
- Cognate meaning is evidence ABOUT, not a definition OF, the word
- ⚠ Any wholesale import of the cognate sense / root-fallacy move?

## Strength rating (conditional on verification)
- Rating: strong | plausible | speculative — because [attestation + semantic fit + corroboration]
- Cognate vs. internal evidence: [which weighs more here]

## Cognate reading → interpretation
- [payoff] — linguistically supported (verify) | inference ([stream])
- Divergent readings: [Option A — stream] | [Option B — stream]

## Confidence & next step
- Confidence: low / moderate / high (conditional on verification)
- Most decisive verification step: [confirm attestation/gloss in named comparative lexicon]
```

---

## Verification

- [ ] The methodological controls (attestation, semantic plausibility, internal-evidence priority, directionality, illegitimate-transfer guard) taught explicitly, not just applied.
- [ ] Every cognate form, gloss, attestation, and etymology/proto-Semitic claim flagged candidate/verify-required; none asserted or invented from memory.
- [ ] Internal Hebrew/Aramaic evidence weighed against cognate evidence; evidential bar set by the word's attestation level.
- [ ] Illegitimate cognate transfer and root fallacy explicitly guarded against, not committed or endorsed.
- [ ] Argument strength rated conditional on verification, with the basis (attestation + semantic fit + corroboration) stated; single-source/Arabic-only appeals flagged weaker.
- [ ] No comparative lexicon quoted from memory; resource types named, specific citations flagged verify-required.
- [ ] Cognate-dependent interpretive divergence attributed to streams; confidence + decisive step stated.

---

## False-Positive Prevention

❌ **DON'T:**
- Invent "the Ugaritic/Akkadian/Arabic cognate is [form] meaning [X]" or fabricate its attestation.
- Assert a proto-Semitic root or etymology as established fact.
- Import a cognate's meaning into the Hebrew/Aramaic word as a definition, or argue from a shared root to a shared meaning.
- Let a cognate override solid internal usage for a well-attested word.
- Cite "HALOT, p. ___," "CAD vol. ___," or "DUL, p. ___" from memory.

✅ **DO:**
- Teach and apply the controls (attestation, semantic plausibility, internal priority, directionality, transfer guard).
- Flag every cognate form, gloss, attestation, and etymology verify-required against named comparative lexica.
- Weigh cognate evidence against internal evidence and set the bar by attestation level.
- Rate the argument's strength conditionally and name the most decisive verification step.
- Attribute divergent cognate-dependent readings to streams without ruling.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Fix claim → Internal baseline → Attestation → Semantic plausibility/directionality → Transfer guard → Strength rating) operationalizes comparative-Semitic method and front-loads the controls that prevent illegitimate transfer.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates the cognate argument across distinct axes — attestation, semantic plausibility, directionality, internal-vs-external weight — so a stretch on any axis is exposed.
- **RT-05 (Evidence-Based Reasoning):** Every cognate datum is grounded in a named comparative lexicon or flagged unverified; argument strength is tied to verifiable attestation and semantic fit, not assertion.
- **QA-04 (Uncertainty Acknowledgment):** Cognates, glosses, attestations, and reconstructions are candidate (verify); strength is rated conditional on verification; the central reading carries a confidence rating and a decisive step.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* (HALOT/DCH, CAD/AHw, DUL, comparative-Semitic works) for each datum and flags specific citations as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The output catalogs the specific real comparative lexica needed to validate every cognate form, gloss, and attestation.
