---
title: "Textual Criticism Primer (Method + User-Supplied Variant) — Structured, Anti-Fabrication"
category: biblical-studies/original-languages
description: "Walk a user through how textual criticism evaluates a specific variant they supply — external evidence (manuscript families, dates, geographic distribution), internal evidence (lectio difficilior, scribal tendencies, harmonization) — presenting the method and major text-critical positions while treating every manuscript attribution, apparatus datum, and reading as verify-required against NA28/UBS5/BHS apparatus."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-04
  - NE-14
difficulty: advanced
tags:
  - original-languages
  - textual-criticism
  - manuscripts
  - variants
  - apparatus
  - anti-fabrication
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/original-languages/biblical_language_parsing_morphology_helper.md
  - domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md
  - domain-biblical-studies/exegesis-interpretation/biblical_multiview_interpretation_map.md
  - domain-biblical-studies/original-languages/biblical_language_septuagint_usage.md
---

# Textual Criticism Primer (Method + User-Supplied Variant)

> **STRONG-GUARD prompt.** Textual criticism is the single highest-fabrication-risk area in biblical studies for a language model. Models routinely invent which manuscripts contain which readings, fabricate apparatus data, misattribute manuscript sigla (P46, Sinaiticus, Vaticanus, etc.), assert date ranges and text-type classifications from memory, and present contested text-critical judgments as settled. Here, **every manuscript attribution, apparatus datum, reading, date, text-type classification, and text-critical verdict is verify-required** against the critical apparatus of NA28/UBS5 (NT) or BHS/BHQA (OT). The model explains the **method** — not the data. The user supplies and verifies all specific textual evidence.

**Objective:** Take a specific textual variant the user identifies and walk through how textual criticism evaluates it — explaining external and internal evidence criteria, showing how those criteria would apply to this variant, and presenting the major text-critical positions — **without asserting any manuscript data, apparatus readings, or text-critical verdicts from memory.** The output is a method scaffold the user populates with verified data from a critical apparatus.

**When to use:**
- You encounter a textual variant (footnoted in a Bible translation, noted in a commentary, or found in an apparatus) and want to understand how scholars evaluate it.
- You want to learn the method of textual criticism — external and internal evidence criteria — applied to a concrete case you supply.
- You are preparing an exegesis or sermon and need to assess how a variant affects interpretation, with the text-critical reasoning made transparent.

**When NOT to use:**
- You want the parsing or morphology of a specific form — use `biblical_language_parsing_morphology_helper.md`.
- Your question is why English translations differ but the underlying text is not in dispute — use `biblical_translation_comparison.md` (in `exegesis-interpretation/`).
- You want a settled verdict on which reading is original — no prompt can provide that; the prompt scaffolds the evaluation, the user weighs the evidence from the apparatus. Go to a textual commentary (Metzger's *Textual Commentary*, Tov's *Textual Criticism of the Hebrew Bible*) for published evaluations.

**Audience:** Seminary/academic (A) and pastors (P) who can access a critical apparatus (NA28/UBS5 for NT; BHS/BHQA for OT).

---

## Inputs / Context

1. **The passage.** Book, chapter, verse — and the specific variant unit (which word or phrase is in question).
2. **The variant readings (user-supplied).** The two or more readings as the user has them from a translation footnote, commentary, or apparatus — pasted by the user. The model does not supply readings from memory.
3. **Known apparatus data (optional but recommended).** Any manuscript sigla, ratings (e.g., UBS certainty rating A/B/C/D), or apparatus notes the user has already gathered — supplied so the model organizes and explains, not invents, them.
4. **Testament and text tradition.** NT (NA28/UBS5 tradition) or OT (BHS/BHQA/DSS tradition) — sets the appropriate manuscript families and method conventions.
5. **The question.** "How would a text critic evaluate this?" / "Which criteria apply here?" / "What are the positions?" — sets focus.

---

## Constraints

### Must
- Explain the **method** of textual criticism (external and internal evidence criteria) clearly enough that the user can apply it to their variant — this is the prompt's primary value.
- Treat every specific manuscript attribution ("P46 reads X," "Sinaiticus has Y"), apparatus datum, reading, date range, text-type classification, and text-critical verdict as **verify-required** against the critical apparatus, never asserted from memory.
- Present the **criteria** for evaluating variants (external: manuscript age, text-type, geographic distribution, quantity vs. weight; internal: lectio difficilior, lectio brevior, scribal tendencies, harmonization, style/vocabulary of the author) with clear definitions so the user understands what each criterion means and how it operates.
- When applying criteria to the user's variant, frame applications as "if the apparatus shows X, then criterion Y would weigh toward reading Z" — conditional on verified data, not assertions.
- Present major **text-critical positions** on the variant (where they exist) attributed to identifiable schools or published evaluations, with specific attributions flagged verify-required.
- State the **interpretive stakes** — what changes in meaning depending on which reading is adopted — without adjudicating which reading is original.

### Must Not
- Assert which manuscripts contain which reading from memory — this is exactly the data that must come from the apparatus.
- Fabricate or assert apparatus sigla, dating, text-type classifications, or UBS certainty ratings from memory.
- Present a text-critical verdict ("the original reading is X") as the prompt's conclusion; the prompt explains how to evaluate, not what to conclude.
- Quote a textual commentary (Metzger, Tov, etc.) from memory; name the resource type and flag citations as verify-required.
- Assert the date, provenance, or text-type of a specific manuscript from memory (e.g., "P46 dates to ca. 200 CE" or "Vaticanus is Alexandrian") — these are verify-required claims about specific manuscripts.
- Invent or reconstruct a reading that is not among those the user supplied.
- Collapse genuinely contested text-critical questions into a simple answer.

### Tradition-neutral stance (Must / Must Not)
- **Must:** where the variant bears on a doctrinally significant reading (e.g., Christological titles, Trinitarian formulas, soteriological language), present the text-critical arguments for each reading and attribute doctrinal implications to identifiable streams, without ruling.
- **Must Not:** privilege the reading that favors any tradition's doctrinal conclusion, or present a text-critical judgment as driven by the evidence when it is actually driven by theological preference.

---

## Instructions

### Step 1 — Fix the variant unit and the readings
Restate the passage, the specific variant unit (which word/phrase), and each reading the user has supplied. Echo any apparatus data the user provided as **supplied-by-user**. If the user has not supplied the readings or apparatus data, instruct them to gather this from a critical apparatus before proceeding — do not supply readings from memory. Confirm testament (NT or OT) to set the appropriate text-critical framework.

### Step 2 — Explain external evidence criteria
Define and explain the external evidence criteria that apply:
- **Manuscript age:** Older manuscripts are generally (not always) closer to the original; explain why "generally" and the exceptions.
- **Text-type / manuscript family:** Explain what text-types are (e.g., for NT: Alexandrian, Western, Byzantine — with the caveat that these classifications are themselves debated and verify-required for specific manuscripts). For OT, explain the relevant traditions (MT, LXX Vorlage, Samaritan Pentateuch, DSS).
- **Geographic distribution:** Readings attested across geographically independent traditions carry more weight; explain why.
- **Quantity vs. quality:** Why a reading in fewer but earlier/more reliable manuscripts may outweigh one in many later manuscripts.
Instruct the user: "To apply these criteria, you need the apparatus — which manuscripts support each reading, their dates, and their text-type classifications. Gather this from NA28/UBS5 (NT) or BHS/BHQA (OT)."

### Step 3 — Explain internal evidence criteria
Define and explain the internal evidence criteria:
- **Lectio difficilior (harder reading):** Scribes tend to smooth, clarify, and simplify — so the more difficult reading is often earlier. Explain the limits of this criterion (a reading can be hard because it is a scribal error, not because it is original).
- **Lectio brevior (shorter reading):** Scribes tend to add rather than omit — so shorter readings may be earlier. Explain the limits (scribes also omit by homoioteleuton or parablepsis).
- **Scribal tendencies:** Harmonization (making one passage match a parallel), theological modification, liturgical expansion, grammatical improvement. Define each with the caveat that identifying a scribal tendency is itself an interpretive judgment.
- **Author's style and vocabulary:** The reading that fits the author's known patterns may be original — but "known patterns" must be established independently, not circularly.
- **Transcriptional probability:** Which reading best explains the origin of the others? The reading from which the other variants most plausibly arose is likely original.
Show how these criteria would apply to the user's variant — framed conditionally ("if the harder reading is X, then lectio difficilior would weigh toward X").

### Step 4 — Apply criteria to the user's variant (conditionally)
Walk through each reading the user supplied and show which criteria would favor it — framed as "if the apparatus confirms [condition], then [criterion] favors [reading]." Do not assert the condition; the user verifies it. Identify where criteria conflict (e.g., external evidence favors one reading but internal evidence favors another) and explain that this tension is normal and is what makes text-critical judgment necessary.

### Step 5 — Present major text-critical positions (attributed, not ruled)
If the variant is well-known enough to have published text-critical discussions, name the positions and attribute them to schools or published evaluations — with every specific attribution flagged verify-required. If the variant is not widely discussed, say so and note that the user's own application of the criteria (Steps 2-4) is the evaluation. Present the positions without adjudicating.

### Step 6 — Interpretive stakes and confidence
State what is at stake interpretively — how meaning changes depending on which reading is adopted. Tag each interpretive claim as **reading-dependent** and, where relevant, attribute doctrinal implications to identifiable traditions. State overall confidence on the evaluation (which will usually be low to moderate without apparatus verification) and the single most important next step (typically: "verify the apparatus data for this variant in [NA28/UBS5 or BHS]").

---

## Output Format

```
# Textual Criticism — [passage], variant: [brief description]

## Variant unit
- Passage: [reference]
- Variant location: [which word/phrase]
- Testament / text tradition: NT (NA28/UBS5) | OT (BHS/BHQA)

## Readings (user-supplied)
- Reading A: [as supplied] — apparatus data: [supplied-by-user | not yet gathered]
- Reading B: [as supplied] — apparatus data: [supplied-by-user | not yet gathered]
- [Reading C, etc., if applicable]

## External evidence criteria (method explanation)
- Manuscript age: [definition + how to apply]
- Text-type / family: [definition + how to apply] — text-type classifications VERIFY
- Geographic distribution: [definition + how to apply]
- Quantity vs. quality: [definition + how to apply]
→ To apply: gather apparatus data from [NA28/UBS5 | BHS/BHQA]

## Internal evidence criteria (method explanation)
- Lectio difficilior: [definition + limits + conditional application to this variant]
- Lectio brevior: [definition + limits + conditional application]
- Scribal tendencies: [harmonization / theological modification / etc. + conditional application]
- Author's style: [definition + limits + conditional application]
- Transcriptional probability: [which reading explains the others?]

## Criteria applied to this variant (conditional on apparatus verification)
| Criterion | Favors | Condition (VERIFY) |
|-----------|--------|--------------------|
| [criterion] | Reading [A/B] | "If apparatus shows [X]..." |
| [..] | [..] | [..] |
- Criteria in tension: [where external and internal conflict, if applicable]

## Text-critical positions (attributed, verify-required)
- [Position A]: [attributed to school/evaluation] — VERIFY attribution
- [Position B]: [attributed to school/evaluation] — VERIFY attribution
- [Or: "No widely published discussion found — apply the criteria above with verified data"]

## Interpretive stakes
- If Reading A: [interpretive consequence] — reading-dependent
- If Reading B: [interpretive consequence] — reading-dependent
- Doctrinal significance (if any): [attributed to traditions, not ruled]

## Confidence & next step
- Evaluation confidence: low / moderate (pending apparatus verification)
- Most important next step: [verify apparatus data in specific resource]
```

---

## Verification

- [ ] All readings used are user-supplied; none fabricated or recalled from memory.
- [ ] No manuscript attribution (which manuscripts support which reading) asserted from memory; all apparatus data either supplied-by-user or flagged "not yet gathered."
- [ ] No manuscript date, text-type classification, or UBS certainty rating asserted from memory; all verify-required.
- [ ] External and internal evidence criteria defined clearly enough for the user to apply independently.
- [ ] Criteria applied conditionally ("if the apparatus shows X, then..."), not as assertions about what the apparatus contains.
- [ ] Text-critical positions attributed to schools/evaluations with attributions flagged verify-required.
- [ ] Interpretive stakes stated without adjudicating which reading is original.
- [ ] No textual commentary quoted from memory; resource types named, specific citations flagged verify-required.

---

## False-Positive Prevention

❌ **DON'T:**
- Assert "P46 and Sinaiticus read X" or "the Alexandrian text-type supports reading A" from memory — these are exactly the claims that require apparatus verification.
- Present the text-critical verdict of one school or commentary as the settled answer — even widely accepted judgments rest on weighing contested evidence.
- Fabricate a UBS certainty rating (A/B/C/D) or a Metzger commentary quotation to lend authority to the evaluation.
- Assert a manuscript's date, provenance, or text-type (e.g., "P46 dates to ca. 200 CE," "Vaticanus is Alexandrian") from memory.

✅ **DO:**
- Explain the method (criteria and how they work) clearly enough that the user can evaluate the variant independently once they have the apparatus data.
- Frame every application of criteria as conditional on apparatus verification: "if X, then criterion Y favors reading Z."
- Present competing text-critical positions as positions, not as correct vs. incorrect answers, and require the user to verify every specific attribution.

---

## Techniques Used

- **ST-01 (Role & Objective Priming):** Frames the model as a method-scaffold builder rather than a text-critical oracle — the objective is to explain how a variant is evaluated, with every datum verify-required, which sets the anti-fabrication posture before any apparatus claim.
- **ST-02 (Structured Sequential Instructions):** The 6-step sequence (Fix the variant → External criteria → Internal criteria → Apply conditionally → Positions → Stakes/confidence) separates teaching the method from asserting apparatus data, and keeps criteria-application conditional on verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Requires weighing external evidence (age, text-type, distribution, quantity vs. quality) and internal evidence (lectio difficilior/brevior, scribal tendencies, author's style, transcriptional probability) as distinct dimensions, so no single criterion is mistaken for the whole judgment.
- **QA-04 (Uncertainty Acknowledgment):** Every manuscript attribution, dating, text-type, and certainty rating is verify-required; criteria are applied conditionally; the evaluation carries a low/moderate confidence rating and the readings are not adjudicated.
- **NE-14 (Fabrication Prevention):** Bars asserting which manuscripts read what, apparatus sigla, datings, text-type classifications, UBS ratings, and commentary quotations from memory; all readings are user-supplied and every datum is routed to the critical apparatus (NA28/UBS5; BHS/BHQA).
