# Jewish–Christian Dialogue

Prompts for **pastors (P), academic readers (A), group leaders (G), and self-directed learners (S)** who want to read the Bible with Jewish tradition in view and without inherited anti-Jewish habits: how Jewish tradition reads a specific Hebrew Bible text, the Second Temple Jewish context of a New Testament passage, and an anti-Judaism check for teaching on hard New Testament texts. This is the domain's place of **elevated risk of misrepresenting Jewish tradition**, so every prompt here is **STRONG-GUARD**.

## Shared guard contract

- **Never invent Jewish or ancient sources.** No midrash, Talmud, Mishnah, Targum, or medieval commentary is quoted, paraphrased, or located from memory; no tractate and folio, midrash section, or commentary location the user did not supply. Where one is needed, a `[VERIFY: locate in …]` slot names the *kind* of source. Well-known commentators may be named as people; what they say at a verse is always `[VERIFY]`. No invented rabbis, scholars, dates, Dead Sea Scroll sigla, Josephus/Philo references, or archaeological claims.
- **Scripture by address only.** The user supplies the translation — a named Jewish translation, a Christian one, or both.
- **Jewish interpretation in its own terms.** Readings are attributed to identifiable streams — classical rabbinic literature (with its internal debate), medieval commentators, Targumim, philosophical and mystical streams, modern movements, academic Jewish studies — using Jewish terminology (Tanakh, Torah, Akedah) and noting canon-order and versification differences.
- **No supersessionist framing in the prompt's own voice.** Jewish reading is not a "pre-Christian stage" or a foil; Judaism after the first century is a living tradition; "Pharisee" is not a synonym for hypocrite; Second Temple Judaism is not "legalistic works-righteousness". Christian theologies of Israel may be described and attributed as Christian positions, never adopted as the frame or presented as what Jews believe.
- **Tradition-neutral.** Plural positions within Judaism and within Christianity are attributed, not adjudicated. Where stakes are real, each prompt recommends checking with a Jewish dialogue partner, rabbi, or Jewish-studies scholar.

**Audience codes:** L = layperson · G = group leader · P = pastor/preacher · A = seminary/academic · S = self-directed learner · M = ministry-context teacher.

## Prompts

| Prompt | Audience | Difficulty | Guard | What it does |
|---|---|---|---|---|
| `biblical_dialogue_jewish_tradition_text_reading.md` | P, A, S | advanced | **STRONG-GUARD** | Maps Jewish reading streams on one Hebrew Bible text (peshat/derash, rabbinic, Targum, medieval, liturgy, modern movements, academic), with internal disagreement; optional Christian readings side by side; questions for a Jewish dialogue partner |
| `biblical_dialogue_second_temple_context.md` | P, A, G | advanced | **STRONG-GUARD** | Second Temple Jewish context for an NT passage, each claim labelled by confidence and source type; anachronism gate for later rabbinic literature; debates attributed; caricature check on your draft |
| `biblical_dialogue_anti_judaism_teaching_check.md` | P, G, A | intermediate | **STRONG-GUARD** | Element-by-element review of a sermon or lesson on a hard NT text against eight anti-Jewish patterns; severity-rated findings and honest revisions; attributed *Ioudaioi* options; clean-pass valve |

## Which prompt for which question

- **"How do Jews read this passage?"** → `biblical_dialogue_jewish_tradition_text_reading.md`
- **"What was Judaism actually like behind this Gospel or Pauline passage?"** → `biblical_dialogue_second_temple_context.md`
- **"Does my sermon on John 8 / Matthew 23 sound anti-Jewish?"** → `biblical_dialogue_anti_judaism_teaching_check.md`

A typical sequence for teaching a hard NT text: Second Temple context → build the sermon in `sermon-devotional/` → anti-Judaism check on the draft.

## What these prompts are not

- Not a substitute for a Jewish dialogue partner, rabbi, or Jewish-studies scholar — they produce maps and verify lists to take to one.
- Not a source of rabbinic, Targum, or commentary content — every such item is a slot the user fills from a real edition.
- Not a verdict on any theology of Israel — Christian positions are described and attributed, never ranked.
- Not a way to sanitise Scripture — the anti-Judaism check keeps the text's hard edges and changes only the teacher's framing.

## Lives elsewhere — do not duplicate

- **Interfaith dialogue with any religion, topic-level** → `apologetics-engagement/biblical_apologetics_other_religions_dialogue.md`.
- **General historical-cultural background (any period)** → `exegesis-interpretation/biblical_historical_cultural_context.md`; full background brief → `theology-research/biblical_background_research_brief.md`.
- **Competing Christian interpretations of a verse** → `exegesis-interpretation/biblical_multiview_interpretation_map.md`.
- **MT/LXX comparison, OT-in-NT usage, canon order and versification** → `original-languages/` (`biblical_language_septuagint_usage.md`, `biblical_language_ot_in_nt_usage.md`, `biblical_language_canon_versification_differences.md`).
- **Building the sermon itself** → `sermon-devotional/biblical_expository_sermon_prep.md`; **exegetical fallacies** → `theology-research/biblical_exegetical_fallacy_detector.md`.
