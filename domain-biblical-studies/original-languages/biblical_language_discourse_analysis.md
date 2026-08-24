---
title: "Discourse / Clause-Flow Analysis — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Structure a methodology-forward discourse analysis of a user-supplied text — prominence/foregrounding, cohesion and connectives, paragraph/episode boundaries, and information structure (topic/focus, given/new) — treating every analytical label as candidate / verify-required, routing competing discourse models to named resources without ruling, and never fabricating original-language data, frequencies, or model citations."
techniques:
  - ST-02
  - RT-02
  - RT-05
  - QA-04
  - QA-05
  - OC-12
difficulty: advanced
tags:
  - discourse-analysis
  - clause-flow
  - prominence
  - cohesion
  - information-structure
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_greek_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_hebrew_syntax_analysis.md
  - domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md
  - domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md
  - domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md
---

# Discourse / Clause-Flow Analysis

**Objective:** Take a user-supplied passage and structure a disciplined discourse analysis — how clauses cohere into paragraphs/episodes, what is foregrounded vs. backgrounded, how connectives signal relationships, and how information is packaged (topic/focus, given/new) — **as a method scaffold, not a settled chart.** Every analytical label is candidate; competing discourse models are named, not adjudicated; no original-language data is fabricated.

> **STRONG-GUARD prompt.** Discourse analysis tempts confident, chart-like output that looks objective but rests on contested models and on morphology/syntax the model may misremember. Here, prominence/boundary/information-structure labels are **candidate / verify-required**; discourse *models* are attributed and held open; any original-language datum (verb forms, particles, frequencies) is verify-required and routed to the syntax/parsing prompts — never asserted from memory.

**When to use:**
- You want to see how a passage's clauses flow — what carries the mainline, where the breaks are, what is emphasized.
- You're identifying paragraph/episode boundaries before structuring an exegesis or sermon.
- You're examining how connectives and information structure shape the argument or narrative.

**When NOT to use:**
- You need the *parse* or within-clause *syntax* of specific forms — use `biblical_language_parsing_morphology_helper.md`, `biblical_language_greek_syntax_analysis.md`, or `biblical_language_hebrew_syntax_analysis.md`.
- You only need the passage's literary placement and outline at a higher level — use `biblical_literary_context_structure.md`.
- You want an authoritative, model-specific discourse chart — go to a discourse grammar / discourse-analytical commentary in your tradition of method; this prompt scaffolds, it does not replace them.

**Audience:** Seminary/academic (A) and pastors (P), ideally working from the original-language text or a closely structured translation.

---

## Inputs / Context

1. **The passage.** The text (original language and/or a named translation), pasted by the user with its reference; the model references by address and does not quote from memory.
2. **Confirmed syntactic data (optional but recommended).** Any verified verb forms, connectives, or clause boundaries the user has from a tool — supplied so the model analyzes flow rather than re-inventing forms.
3. **Preferred discourse model (optional).** If the user works within a named discourse framework, the model can foreground its categories but still notes it is one model among several.
4. **The discourse question (optional).** A specific focus (e.g., "Where do the episodes break?" "What's foregrounded in this paragraph?").
5. **Genre.** Narrative vs. discourse/argument vs. poetry — prominence and boundary signals differ by genre.

---

## Constraints

### Must
- Treat every analytical label (prominence/mainline-vs-offline, boundary, cohesion relation, topic/focus, given/new) as **candidate / verify-required**, grounded in features the user can check.
- Anchor claims in **observable features of the supplied text** (connectives, verb-form patterns, repetition, participant reference, word order) — and route any original-language datum to the syntax/parsing prompts rather than asserting it.
- Name the **discourse model** in use and acknowledge that discourse-analytic frameworks differ; present competing models descriptively rather than ruling one correct.
- Adjust signals by **genre** (mainline marking, boundary cues, and information structure work differently in narrative vs. exposition vs. poetry).
- State confidence on the proposed structure (boundaries, prominence) and what textual evidence would confirm or revise it.

### Must Not
- Invent or assert original-language morphology, verb-form distributions, particle inventories, or frequencies from memory; route these to the syntax/parsing prompts and flag verify-required.
- Present a prominence/boundary chart as objective when it depends on a contested model.
- Fabricate or assert specific discourse-model or commentary citations (author/section/page) from memory; name the resource *type* and flag verify-required.
- Quote a discourse grammar or commentary verbatim from memory; misquote the passage (reference by address, use supplied text).

### Tradition-neutral stance (Must / Must Not)
- **Must:** where discourse structure bears on a contested reading (e.g., where the boundary or the foregrounded element changes the interpretation), present the options and attribute the resulting readings to identifiable streams descriptively.
- **Must Not:** privilege the structural analysis that favors any tradition's conclusion, or present a contested boundary/prominence reading as the obvious flow.

---

## Instructions

### Step 1 — Orient: genre, model, data base
Restate the passage, reference, and genre. Name the discourse model being used and note it is one of several. Confirm the data base: echo user-supplied syntactic data as **supplied-by-user**; flag any original-language feature you would otherwise assert as "verify in syntax/parsing tools first."

### Step 2 — Segment into clauses/units
Lay out the text in clause-sized units (using the supplied text). Label each unit's role candidate-ly (mainline vs. supporting/offline), tied to observable features, flagged **candidate (verify)**.

### Step 3 — Boundaries: paragraphs/episodes
Propose paragraph/episode boundaries from observable cues (shifts in participant, time, place, connective, verb-form pattern). Flag each boundary **candidate (verify)** and name the cue it rests on; note where boundaries are debated.

### Step 4 — Cohesion and connectives
Map how units cohere: connectives and their candidate relations (continuity, development, contrast, grounds/result), participant reference chains, repetition/lexical cohesion. Route connective-force claims to the syntax prompts; flag candidate.

### Step 5 — Prominence and information structure
Identify candidate foregrounded/emphasized elements and information packaging (topic/focus, given/new, fronting), tied to features and flagged candidate. Note that prominence judgments are model-dependent.

### Step 6 — Discourse → interpretation
State how the proposed flow bears on meaning, each payoff tagged **feature-supported (verify)** or **inference (stream)**. Where the structure-dependent reading diverges, attribute options to streams without ruling.

### Step 7 — Confidence + verification map
Give confidence on the proposed structure and the one piece of textual evidence that would most confirm or revise it. List resource *types* (discourse grammar, discourse-analytical commentary, the syntax/parsing prompts) with specific citations flagged verify-required.

---

## Output Format

```
# Discourse Analysis — [reference]

## Orientation
- Genre: [..] | Discourse model (one of several): [..]
- Data base: [supplied-by-user | original-language features unconfirmed — verify first]
- Question: [..]

## Clause/unit segmentation (candidate roles — verify)
| Unit | Text (supplied) | Candidate role (mainline/offline) | Feature it rests on |
|------|-----------------|-----------------------------------|---------------------|
| [..] | [..] | candidate (verify) | [..] |

## Boundaries (candidate — name the cue)
- Boundary at [..] — cue: [participant/time/place/connective/verb-form] (verify; debated? [y/n])

## Cohesion & connectives
- Connective relations (candidate, route force to syntax prompt): [..]
- Participant-reference chains / lexical cohesion: [..]

## Prominence & information structure (model-dependent, candidate)
- Foregrounded/emphasized: [..]
- Topic/focus, given/new, fronting: [..]

## Discourse → interpretation
- [payoff] — feature-supported (verify)
- [payoff] — inference ([stream])
- Divergent structure-dependent readings: [Option A — stream] | [Option B — stream]

## Confidence & verification map
- Proposed structure confidence: low / moderate / high
- Most decisive confirming/revising evidence: [..]
- Consult (citations verify-required): [discourse grammar], [discourse-analytical commentary], [syntax/parsing prompts]
```

---

## Verification

- [ ] Every analytical label (prominence/boundary/cohesion/info-structure) flagged candidate/verify-required and tied to an observable feature.
- [ ] No original-language morphology, verb-form distribution, particle inventory, or frequency asserted from memory; routed to syntax/parsing prompts.
- [ ] Discourse model named and acknowledged as one of several; competing models not adjudicated.
- [ ] Genre-appropriate signals used (narrative vs. exposition vs. poetry).
- [ ] No specific model/commentary citation asserted from memory; resource types named, citations flagged verify.
- [ ] Structure-dependent interpretive divergence attributed to streams, not ruled.
- [ ] Proposed structure carries confidence + the most decisive confirming/revising evidence.

---

## False-Positive Prevention

❌ **DON'T:**
- Produce a clean prominence/boundary chart that reads as objective when it rests on a contested model.
- Assert verb-form distributions or particle frequencies from memory to justify a boundary.
- Cite a specific discourse grammar section or commentary page from memory.
- Treat one discourse model's categories as the only valid analysis.
- Let the boundary or foregrounding that supports a doctrine stand without naming the alternative.

✅ **DO:**
- Tie every label to an observable feature of the supplied text and flag it candidate (verify).
- Route original-language claims to the syntax/parsing prompts.
- Name the discourse model and acknowledge competing frameworks.
- Adjust signals by genre and note where boundaries are debated.
- State confidence and the single most decisive piece of confirming/revising evidence.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** The 7-step sequence (Orient → Segment → Boundaries → Cohesion → Prominence → Interpretation → Confidence) imposes a method so the analysis builds from observable features rather than a recalled chart.
- **RT-02 (Multi-Dimensional Analysis Framework):** Requires analysis across the distinct discourse dimensions — segmentation, boundaries, cohesion/connectives, prominence, and information structure — so no single layer is mistaken for the whole flow.
- **RT-05 (Evidence-Based Reasoning):** Every label is anchored in an observable textual feature or flagged unverified; discourse models are presented as competing frameworks rather than settled fact.
- **QA-04 (Uncertainty Acknowledgment):** Labels and boundaries are flagged candidate (verify); model-dependence is named; the proposed structure carries a low/moderate/high confidence and a most-decisive-evidence note.
- **QA-05 (Citation Requirements):** Requires naming the resource *type* for each claim and flags specific discourse-model/commentary citations as verify-required — never asserted from memory.
- **OC-12 (External Reference Catalog):** The verification map catalogs the resource types (discourse grammar, discourse-analytical commentary, the syntax/parsing prompts) needed to validate the proposed structure.
