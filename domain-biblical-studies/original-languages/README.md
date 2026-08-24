# Original Languages

Prompts for working with the biblical text in Greek, Hebrew, and Aramaic — parsing/morphology, Greek and Hebrew syntax, verbal aspect, voice/deponency, discourse/clause-flow, idiom and figures of speech, semantic domains, OT-in-NT usage, the Septuagint, textual criticism, the Masorah and Qere/Ketiv, cantillation and accentuation, canon/versification, comparative Semitics, documentary/Koine register, and vocabulary building. **This is the highest-fabrication-risk subdirectory in the domain.** Language models routinely invent lemmas, parsing codes, Strong's numbers, semantic ranges, syntactic and aspect labels, frequency counts, grammar-section citations, manuscript/variant data, Masoretic notes, accent placements, cognate forms, papyrus/inscription sigla, and which-textual-tradition claims that sound authoritative and are wrong.

**Everything here is verify-required.** Every prompt is **STRONG-GUARD**: it treats all original-language data as candidate / verify-required unless the user supplied it, never asserts morphology, glosses, syntax/aspect/voice labels, frequencies, apparatus, Masoretic notes, accents, cognates, documentary citations, or versification from memory, never invents Strong's numbers or grammar citations (specific author/section/page references are flagged verify-required, not asserted), references verses by address, and routes every claim to a named real resource (BDAG, HALOT, DCH, LSJ, BDB, Louw-Nida, Moulton-Milligan, reverse interlinears, tagged morphological databases, standard reference grammars, aspect and middle-voice monographs, critical editions and apparatus, the BHS/BHQ Masorah, comparative-Semitic lexica, documentary editions, and Septuagint scholarship). Where a language choice bears on contested interpretation, the options are described and attributed to identifiable streams without ruling.

## Prompts

| Prompt | Focus | Audience | Difficulty |
|---|---|---|---|
| `biblical_language_parsing_morphology_helper.md` | Structure and **verify** the parse/morphology of a supplied form; explain each parsing slot (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_greek_syntax_analysis.md` | Greek syntax/grammar — case functions, tense-aspect, mood/voice, clauses, participles, conditionals (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_hebrew_syntax_analysis.md` | Hebrew/Aramaic syntax — verbal system, waw-consecutive, construct chains, word order, particles (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_greek_verbal_aspect_analysis.md` | Greek verbal aspect vs. "tense"; Aktionsart; competing aspect frameworks described, not ruled (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_greek_voice_deponency_analysis.md` | Greek middle/passive voice semantics and the deponency debate (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_discourse_analysis.md` | Discourse/clause-flow — prominence, cohesion, paragraph/episode boundaries, information structure (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_idiom_and_figures_of_speech_analysis.md` | Original-language idioms and figures of speech where wooden parsing misleads (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_semantic_domains_componential_analysis.md` | Sense disambiguation by semantic-domain/componential method (Louw-Nida/BDAG) (**STRONG-GUARD**) | A, P | intermediate |
| `biblical_language_ot_in_nt_usage.md` | How a NT text uses an OT quotation/allusion; compare MT/LXX/NT wording, classify use (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_septuagint_usage.md` | LXX usage and Masoretic-Text divergences; translation technique (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_textual_criticism_primer.md` | Method + a user-supplied variant: external/internal evidence, positions (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_hebrew_masora_and_variants_analysis.md` | Reading the BHS/BHQ Masorah (Mp/Mm) and Qere/Ketiv (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_hebrew_accents_greek_accentuation_analysis.md` | Hebrew cantillation (te'amim) and Greek accentuation as reading/division traditions (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_aramaic_analysis.md` | Biblical Aramaic syntax, verb stems, noun states, dialect context (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_canon_versification_differences.md` | Canon, ordering, naming, and versification across traditions (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_comparative_semitics_cognate_analysis.md` | Evaluating cognate arguments (Ugaritic/Akkadian/Arabic) with method controls (**STRONG-GUARD**) | A, P | advanced |
| `biblical_language_koine_inscriptions_papyri_register_analysis.md` | Documentary Greek — papyri/inscriptions and Koine register (**STRONG-GUARD**) | A | advanced |
| `biblical_language_greek_hebrew_vocabulary_builder.md` | Frequency-based vocabulary study plan for learners (**STRONG-GUARD**) | A, P | intermediate |

## Which prompt for which question

**Forms, parsing & grammar**
- **"Parse this form / what does this parse mean / is this parse right?"** → `biblical_language_parsing_morphology_helper.md`
- **"What does the Greek syntax do here?"** (case function, clause type, participle, conditional) → `biblical_language_greek_syntax_analysis.md`
- **"What does the Hebrew/Aramaic syntax do here?"** (verb form, construct chain, word order, particle) → `biblical_language_hebrew_syntax_analysis.md`
- **"What does the verbal aspect contribute — is this aorist really 'past'?"** → `biblical_language_greek_verbal_aspect_analysis.md`
- **"What does the middle/passive add — is this form 'deponent'?"** → `biblical_language_greek_voice_deponency_analysis.md`
- **"Analyze a Biblical Aramaic passage."** → `biblical_language_aramaic_analysis.md`

**Meaning, sense & figures**
- **"How do the clauses flow / where are the boundaries / what's foregrounded?"** → `biblical_language_discourse_analysis.md`
- **"Is this phrase an idiom or figure of speech?"** → `biblical_language_idiom_and_figures_of_speech_analysis.md`
- **"Which sense fits here / what distinguishes this word from its synonyms?"** → `biblical_language_semantic_domains_componential_analysis.md`
- **"Does this cognate (Ugaritic/Akkadian/Arabic) argument hold up?"** → `biblical_language_comparative_semitics_cognate_analysis.md`
- **"Is this word formal or everyday — what do the papyri/inscriptions show?"** → `biblical_language_koine_inscriptions_papyri_register_analysis.md`

**Text, transmission & versions**
- **"How does this NT text use the OT, and why does the wording differ from the Hebrew or the Greek?"** → `biblical_language_ot_in_nt_usage.md`
- **"How does the LXX differ from the Masoretic Text here?"** → `biblical_language_septuagint_usage.md`
- **"How would a text critic evaluate this variant?"** → `biblical_language_textual_criticism_primer.md`
- **"What does this Qere/Ketiv or Masoretic note mean?"** → `biblical_language_hebrew_masora_and_variants_analysis.md`
- **"How do the te'amim divide this verse / what does this Greek accent tell me?"** → `biblical_language_hebrew_accents_greek_accentuation_analysis.md`
- **"Is this book in all canons / why is this verse numbered differently?"** → `biblical_language_canon_versification_differences.md`

**Learning**
- **"Build me a frequency-based Greek/Hebrew vocabulary study plan."** → `biblical_language_greek_hebrew_vocabulary_builder.md`

## Related

The **word-study** prompt lives in the sibling `exegesis-interpretation/` subdirectory and is the closest companion to everything here — start there for a term's glosses and semantic range, then use these prompts for the form's parse, its syntax, its aspect/voice, its discourse role, its sense-disambiguation, or its OT-in-NT use:

- `domain-biblical-studies/exegesis-interpretation/biblical_word_study_original_language.md` (Greek/Hebrew word study — **STRONG-GUARD**)
- `domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md` (why translations differ; variant notes — **STRONG-GUARD**)
- `domain-biblical-studies/exegesis-interpretation/biblical_rhetorical_analysis.md` (discourse-level rhetoric, distinct from original-language figures)
- `domain-biblical-studies/exegesis-interpretation/biblical_ane_comparative_context.md` (cultural ANE background, distinct from cognate philology)
- `domain-biblical-studies/exegesis-interpretation/biblical_canonical_intertextual_reading.md` (trace echoes/quotations across Scripture)
- `domain-biblical-studies/exegesis-interpretation/biblical_literary_context_structure.md` (place a passage in its context; map structure)
- `domain-biblical-studies/theology-research/biblical_exegetical_fallacy_detector.md` (catch root fallacy, totality transfer, illegitimate cognate transfer)
