---
title: "Semantic Domains & Componential Analysis (Louw-Nida / BDAG) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Help the user disambiguate a word's sense in its context using the method of semantic-domain analysis — mapping the term's candidate senses to domains (Louw-Nida for Greek, comparable domain tools for Hebrew), comparing it with near-synonyms and antonyms in the same field, and letting context select the component — while treating every domain assignment, sense, and synonym relationship as candidate / verify-required against the actual lexica, never asserted from memory."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: intermediate
tags:
  - semantic-domains
  - louw-nida
  - componential-analysis
  - lexical-semantics
  - synonyms
  - anti-fabrication
updated: "2026-06-26"
related_prompts:
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
  - domain-biblical-studies/original-languages/biblical_language_idiom_and_figures_of_speech_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_greek_syntax_analysis.md
  - domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md
  - domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md
---

# Semantic Domains & Componential Analysis (Louw-Nida / BDAG)

**Objective:** Take a word in a specific context the user supplies and apply the **method** of semantic-domain analysis to disambiguate its sense — mapping the term's candidate senses to their semantic domains, comparing it with near-synonyms and contrasts in the same field, and showing how the context selects one sense-component — **without asserting domain numbers, sense inventories, or synonym relationships from memory.** This is a *method* prompt: distinct from a word study's breadth-of-senses, it teaches how to move from "the word can mean these things" to "in this context the sense is this," using the structure of the semantic field.

> **STRONG-GUARD prompt.** Semantic-domain work is fabrication-prone: models invent Louw-Nida domain numbers, fabricate sense inventories, assert false synonym/antonym sets, and commit classic word-study fallacies (illegitimate totality transfer — importing every sense into one occurrence; reading an English semantic range back into the Greek/Hebrew). Here, **every domain assignment, sense, gloss, and lexical relationship is candidate / verify-required** against the actual tools (Louw-Nida *Greek-English Lexicon Based on Semantic Domains*, BDAG's sense divisions; for Hebrew, HALOT/DCH and domain-oriented tools), and **specific entry/domain references are flagged verify-required — never asserted from memory.**

**When to use:**
- A word has several possible senses and you want a disciplined way to select the one that fits the context.
- You want to compare a term with its near-synonyms to see what distinguishes them in this field.
- You want to avoid totality transfer and use the semantic-field structure to constrain meaning.

**When NOT to use:**
- You want the full breadth of a term's senses and usage (a word study) — start with `biblical_word_study_original_language.md`; come here for the disambiguation *method*.
- The phrase is idiomatic/figurative rather than a single word's sense — use `biblical_language_idiom_and_figures_of_speech_analysis.md`.
- You want to check whether an interpretation commits a specific exegetical fallacy — use `biblical_exegetical_fallacy_detector.md`.
- You need the syntax that frames the word — use the Greek/Hebrew syntax prompts.

**Audience:** Seminary/academic (A) and pastors (P) with lexical tools (Louw-Nida, BDAG, HALOT, DCH).

---

## Inputs / Context

1. **The word and its context.** The term (script and/or transliteration), the clause/verse it occurs in, and the reference — pasted by the user; the model references by address and does not quote from memory.
2. **Confirmed lemma/parse (recommended).** The verified lemma the senses attach to — supplied so the analysis rests on the right headword (route to the parsing helper if unconfirmed).
3. **Candidate senses (optional).** Any sense inventory or domain data the user already has from the lexica — supplied so the model organizes and reasons over it rather than inventing it.
4. **Near-synonyms to compare (optional).** Terms the user wants set alongside it in the field.
5. **The question.** "Which sense fits here?" / "What distinguishes this term from its synonyms?" / "Am I over-loading the word?" — sets focus.

---

## Constraints

### Must
- Treat every **domain assignment** (e.g., a Louw-Nida domain/sub-domain number), **sense**, **gloss**, and **lexical relationship** (synonym/antonym/hyponym) as **candidate / verify-required** against the actual lexica; route the user to confirm each in Louw-Nida and BDAG (Greek) or HALOT/DCH (Hebrew).
- Teach the **method** explicitly: (1) inventory candidate senses (from the lexica, not memory); (2) map each to its semantic domain; (3) bring in near-synonyms and contrasts that share the domain; (4) identify the *distinguishing components* among them; (5) let the **context** select which sense/component is in play.
- Enforce the **anti-totality-transfer rule**: a word in one occurrence carries *one* contextually-selected sense, not the sum of its possible senses; flag any move that imports multiple senses at once.
- Guard against **English-range back-reading**: the semantic field is the original language's, not the English gloss's; flag reasoning that treats an English synonym set as the Greek/Hebrew field.
- For any datum, name the *kind* of resource that confirms it (the semantic-domain lexicon, BDAG's sense divisions, HALOT/DCH) and **flag specific entry/domain references as verify-required.**
- State confidence on the selected sense and the single most decisive contextual indicator.

### Must Not
- Invent a Louw-Nida domain number, a BDAG sense division, or a sense/gloss; never assert a domain assignment from memory as authoritative.
- Fabricate synonym or antonym sets, or assert that two terms are "synonyms"/"distinguished by X" without routing to the lexica.
- Let the analysis commit totality transfer (stacking all senses into one occurrence) or root-fallacy/etymologizing in place of synchronic field analysis.
- Read an English semantic range back into the original-language field.
- Quote a lexicon verbatim from memory, or assert specific entry numbers/pages from memory.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where the sense selection bears on a contested reading (e.g., a term whose narrower vs. broader sense carries doctrinal weight), present the competing sense selections and attribute the resulting readings to identifiable streams descriptively.
- **Must Not:** privilege the sense that favors any tradition's conclusion, or let a domain/sense choice pre-decide a doctrinal dispute under the appearance of neutral lexical method.

---

## Instructions

### Step 1 — Fix the word, lemma, and context
Restate the term, the confirmed lemma (or flag it unconfirmed → parsing helper), the clause, and the reference. State the question the disambiguation must answer.

### Step 2 — Inventory candidate senses (from the lexica)
List the candidate senses **as the user supplied them or as to be looked up** — each flagged **candidate (verify)** with the resource to confirm it. Do not generate a sense inventory from memory; where none is supplied, mark "look up in Louw-Nida / BDAG / HALOT-DCH" and proceed methodologically.

### Step 3 — Map senses to domains
Place each candidate sense in its semantic domain (Louw-Nida domain/sub-domain for Greek; the comparable field for Hebrew), each assignment flagged **candidate (verify)**. Explain that the domain groups senses by meaning, not by word, so one word's senses can sit in several domains.

### Step 4 — Bring in the field: synonyms and contrasts
Identify near-synonyms and contrasts that share the relevant domain (flagged candidate, routed to the lexica) and the **distinguishing components** that separate them — what does *this* term encode that its neighbors do not? This componential comparison is the heart of the method.

### Step 5 — Let context select the sense (anti-totality-transfer)
Show how the specific context (collocations, syntax, discourse, the author's usage) selects one sense/component. State explicitly that only the selected sense is in play here — not the word's whole range. Flag any tempting over-load.

### Step 6 — Sense → interpretation + confidence
State how the selected sense bears on meaning, tagged **context-selected (verify)** or **inference (stream)**. Attribute divergent sense selections to streams without ruling. Give confidence and the single most decisive contextual indicator, plus the verification step that matters most.

---

## Output Format

```
# Semantic-Domain Analysis — [word] in [reference]

## Word & context
- Term (supplied): [..] | Lemma: [supplied-by-user | unconfirmed → parsing helper]
- Clause / reference: [.. / address]
- Question: [which sense / what distinguishes it / over-loading check]

## Candidate senses (VERIFY in the lexica — not from memory)
| Candidate sense | Domain (candidate) | Verify in |
|-----------------|--------------------|-----------|
| [sense] | [Louw-Nida domain / field] — VERIFY | [Louw-Nida / BDAG / HALOT-DCH] |

## The field: synonyms & contrasts (VERIFY)
| Term in same domain | Shared component | Distinguishing component | Verify in |
|---------------------|------------------|--------------------------|-----------|
| [near-synonym] | [..] | [..] | [lexicon] |

## Context selects the sense (anti-totality-transfer)
- Selecting indicators: [collocation / syntax / discourse / author usage]
- Sense in play here: [one selected sense] — NOT the word's whole range
- ⚠ Over-load check: any senses being imported without warrant?

## Sense → interpretation
- [payoff] — context-selected (verify)
- [payoff] — inference ([stream])
- Divergent sense selections: [Option A — stream] | [Option B — stream]

## Confidence & next step
- Selected-sense confidence: low / moderate / high
- Most decisive contextual indicator: [..]
- Most important verification step: [confirm domains/senses in named lexica]
```

---

## Verification

- [ ] Every domain assignment, sense, gloss, and synonym/antonym relationship flagged candidate/verify-required against named lexica; none asserted or invented from memory.
- [ ] The disambiguation method (inventory → map → compare field → distinguish components → context selects) is taught explicitly, not just applied.
- [ ] Anti-totality-transfer enforced: only the context-selected sense is in play; over-loading flagged.
- [ ] No English semantic range read back into the original-language field; no root/etymology fallacy substituted for synchronic analysis.
- [ ] Near-synonyms and distinguishing components routed to the lexica, not asserted.
- [ ] No lexicon quoted from memory; specific entry/domain references flagged verify-required.
- [ ] Sense-dependent interpretive divergence attributed to streams; confidence + decisive indicator + next step stated.

---

## False-Positive Prevention

❌ **DON'T:**
- Invent a Louw-Nida domain number or a BDAG sense division to anchor the analysis.
- Assert "these two words are synonyms distinguished by X" from memory without routing to the lexica.
- Stack all of a word's possible senses into one occurrence (totality transfer), or argue from the root/etymology in place of synchronic field analysis.
- Treat an English synonym set as if it were the Greek/Hebrew semantic field.
- Let the sense that supports a doctrine win under cover of "neutral lexical method."

✅ **DO:**
- Teach the method (inventory → domain → field comparison → distinguishing components → context selection) and apply it transparently.
- Flag every sense, domain, and relationship candidate (verify) and name the lexicon to confirm it.
- Enforce one context-selected sense per occurrence and run an over-load check.
- Keep the field in the original language, not the English glosses.
- State confidence, the decisive contextual indicator, and the next verification step; attribute divergent selections to streams.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Fix word → Inventory senses → Map domains → Field comparison → Context selects → Interpretation) operationalizes componential method and front-loads the anti-totality-transfer discipline.
- **RT-02 (Multi-Dimensional Analysis Framework):** Analyzes the term across multiple axes — its senses, its domains, its synonym field, and the distinguishing components — so meaning is constrained by structure rather than asserted.
- **RT-05 (Evidence-Based Reasoning):** Every sense, domain, and relationship is grounded in a named lexicon or flagged unverified; the context-selection step grounds the verdict in observable indicators, not intuition.
- **QA-04 (Uncertainty Acknowledgment):** Senses, domains, and relationships are candidate (verify); the selected sense carries a confidence rating and a named decisive indicator.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* (Louw-Nida, BDAG, HALOT/DCH) for each datum and flags specific entry/domain references as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The output catalogs the specific real lexica needed to validate the sense inventory, domain assignments, and synonym field.
