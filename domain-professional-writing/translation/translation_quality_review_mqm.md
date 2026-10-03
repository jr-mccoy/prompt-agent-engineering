---
title: "Translation Quality Review — MQM Error Typology, Severity Weights, and a Pass/Fail Score Agreed Before Reading"
category: professional-writing/translation
description: "Review a finished human translation with an MQM-style (Multidimensional Quality Metrics) method: agree the error categories, severity weights, and pass threshold before reading; annotate each error with its span, category (terminology, accuracy, linguistic conventions, style, locale conventions, audience appropriateness, design), severity, and a fix; exclude preferential changes and source defects; compute a normalised penalty score per 1,000 words with named sub-scores; fail on any critical error regardless of score; and return actionable feedback the translator can learn from."
techniques:
  - AG-11
  - DP-03
  - NE-11
  - QA-17
  - QA-12
difficulty: advanced
tags:
  - human-translation
  - translation-quality
  - mqm
  - error-typology
  - revision
  - severity-scoring
  - check-translation-quality
  - is-this-translation-good
  - grade-a-translator
updated: "2026-10-02"
related_prompts:
  - domain-professional-writing/translation/translation_project_brief_and_glossary.md
  - domain-software-engineering/localization/localization_translation_management_workflow.md
  - domain-discipleship/cross-cultural/discipleship_translated_material_pitfalls.md
---

# Translation Quality Review (MQM)

**Objective:** Turn "is this translation any good?" into an evidenced answer — every
error located, classified, and weighted on a scale agreed in advance, a score that
means the same thing next month, and feedback a translator can act on.

**When to Use:**
- Accepting or rejecting a delivered translation against a brief.
- Comparing translators or vendors on the same sample.
- Giving structured feedback to a translator, or calibrating a team of reviewers.
- **Not this prompt if** you need the brief and glossary the translation should have
  followed — write those first with `translation/translation_project_brief_and_glossary.md`.
  For a software release's translation pipeline and automated checks, use
  `domain-software-engineering/localization/localization_translation_management_workflow.md`.
  For whether translated *teaching material* carries its ideas across cultures, use
  `domain-discipleship/cross-cultural/discipleship_translated_material_pitfalls.md`.

> **Reviewer rule.** Accuracy can only be judged by someone fluent in **both** languages.
> A model may draft annotations as a first pass, but every major and critical error is
> confirmed by a qualified bilingual reviewer before the score is used; a
> target-language-only reader may judge fluency and style, never accuracy.

## Inputs / Context

1. **Source and translation**, aligned by segment or paragraph, with word count.
2. **The brief, glossary, and style sheet** the translator received.
3. **Purpose and stakes** — informational, marketing, legal, safety-related; this sets
   the threshold.
4. **Sample size** — full text, or a sample (state how it was chosen).
5. **Reviewer** — name, language pair, subject field.

## Method

1. **Fix the scale before reading (DP-03).** Record, dated:
   - **Categories (AG-11)** — the MQM top level: *Terminology* (glossary or domain term
     wrong or inconsistent), *Accuracy* (mistranslation, omission, addition,
     untranslated), *Linguistic conventions* (grammar, spelling, punctuation),
     *Style* (register, awkwardness, brand voice), *Locale conventions* (dates, numbers,
     units, address formats), *Audience appropriateness* (culturally unsuitable for the
     reader), *Design and markup* (layout, truncation, formatting).
   - **Severities with anchors** — *Minor*: noticeable, meaning intact; *Major*: meaning
     changed or the reader is misled or confused, but no serious consequence; *Critical*:
     could cause harm, legal exposure, safety risk, or serious reputational damage.
   - **Weights** — the MQM scoring model's commonly used minor 1 / major 5 / critical 25
     (some programmes use critical 10 — choose and record).
   - **Threshold** — e.g. pass at ≥ 98 with zero criticals for published informational
     text; stricter for legal or safety text.
2. **Annotate, segment by segment.** For each error: source span, target span,
   category, severity, a one-line explanation, and a proposed fix. Annotate the
   *smallest* span that carries the error.
3. **Exclude what is not an error (QA-12).**
   - **Preferential changes** — the reviewer would phrase it differently, but nothing is
     wrong. Log separately; score zero.
   - **Source defects** — errors present in the source. Log as source issues, not against
     the translator.
   - **Repeats** — the same error copied across segments counts once, noted as repeated.
   - **Brief-compliant choices** — a choice the brief or glossary required is not an error.
4. **Compute the score (NE-11).**
   `Penalty total (PT) = Σ (count × weight)` ·
   `Penalty per 1,000 words = PT ÷ (evaluated words ÷ 1,000)` ·
   `Quality score = 100 − (PT ÷ evaluated words × 100)`.
   Any critical → **FAIL** regardless of score.
5. **Report named sub-scores (QA-17).** Penalty per category, so "92" becomes "accuracy
   and terminology are fine; style is where the points went".
6. **Write feedback that teaches.** The three most frequent or most serious patterns,
   each with one example and the fix; then what the translator did well.
7. **Recommend the action.** Accept · accept with listed fixes · return for revision ·
   reject and re-assign. For a sample, say whether the result justifies reviewing the rest.

## Output Format

```
# Translation review — [project]   [pair]   Reviewer: [..]   Date: [..]
Scale fixed: [date]  Weights: minor 1 / major 5 / critical [25|10]  Threshold: [..]
Evaluated: [n] words ([full | sample: method])

## Errors
| # | Seg | Source span | Target span | Category | Severity | Why | Fix |

## Not counted
Preferential: [n] (listed) · Source issues: [n] · Repeats merged: [n]

## Score
PT = [..]   Per 1,000 words = [..]   Quality score = [..]   Criticals: [n]
Result: PASS | FAIL

## Sub-scores (penalty points by category)
| Terminology | Accuracy | Linguistic | Style | Locale | Audience | Design |

## Feedback for the translator
Patterns: 1. [...] 2. [...] 3. [...]   Done well: [...]

## Recommended action
[...]
```

## Verification

- [ ] Categories, severity anchors, weights, and threshold were recorded before annotation.
- [ ] Every error has spans, a category, a severity, a reason, and a fix.
- [ ] Preferential changes and source defects are listed but score zero.
- [ ] The arithmetic is shown and reproduces the score.
- [ ] Any critical error produces FAIL.
- [ ] Majors and criticals are confirmed by a bilingual reviewer.

## False-Positive Prevention

1. **"I'd say it differently" is not an error.** Preferential edits inflate penalties and
   teach translators to imitate the reviewer, not the brief.
2. **Don't punish the translator for the source.** A wrong figure in the source is a
   source issue.
3. **Don't double-count.** One mistranslated term repeated twelve times is one error,
   flagged as repeated, unless the brief says repeats count.
4. **Severity follows consequence, not annoyance.** A clumsy sentence is minor; "may"
   rendered as "must" in a contract clause is critical.
5. **A score without a fixed threshold is a number, not a verdict.** Agree it first.
6. **Fluency is not accuracy.** A smooth target can still omit a clause; read against the source.

## Example Output

Scenario: tenant handbook for a US housing association, English → Spanish (US Hispanic
readers); 1,200-word sample (sections 2–3), translated by a contracted linguist with a
supplied glossary. Threshold: ≥ 98, zero criticals.

```
# Translation review — Tenant Handbook §2–3   EN→ES (US)   Reviewer: M. Ortega   Date: 2026-10-02
Scale fixed: 2026-09-30  Weights: minor 1 / major 5 / critical 25  Threshold: ≥ 98, 0 critical
Evaluated: 1,200 words (sample: sections 2–3, chosen as rent and repairs)

## Errors
| 1 | 2.4 | "must report leaks within 48 hours" | "puede reportar fugas en 48 horas" | Accuracy (mistranslation) | Critical | "must" → "may": tenant could lose repair rights | "debe reportar las fugas dentro de 48 horas" |
| 2 | 2.1 | "lease" | "arrendamiento" | Terminology | Minor | glossary: "contrato de alquiler" | use glossary term (×6, merged) |
| 3 | 3.2 | "excluding public holidays" | — | Accuracy (omission) | Major | changes the deadline | add "excepto los días feriados" |
| 4 | 3.5 | "$1,250.00" | "1.250,00 $" | Locale conventions | Minor | US Spanish uses $1,250.00 | "$1,250.00" |
| 5 | 2.7 | "you" (informal tone) | "vosotros" | Audience appropriateness | Major | Peninsular form; brief says US readers, "usted" | "usted" |

## Not counted
Preferential: 4 (e.g. "inquilino" vs "arrendatario" — both acceptable) · Source issues: 1
(§3.1 says "30 days" here, "28 days" in §5 — queried to client) · Repeats merged: 1 (×6)

## Score
PT = 25 + 1 + 5 + 1 + 5 = 37   Per 1,000 words = 30.8   Quality score = 100 − 3.08 = 96.9
Criticals: 1   Result: FAIL

## Sub-scores (penalty points)
| Terminology 1 | Accuracy 30 | Linguistic 0 | Style 0 | Locale 1 | Audience 5 | Design 0 |

## Feedback for the translator
Patterns: 1. Modal verbs carry obligations — "must/may/shall" need checking in every
clause. 2. Use the supplied glossary; it was built for these readers. 3. Address form:
the brief specified "usted".  Done well: clear, natural sentences; headings concise.

## Recommended action
Return for revision of §2–3; because the critical is a pattern risk (modals), review the
full handbook's obligation clauses before acceptance.
```

## Techniques Used

- **AG-11 Taxonomy-Based Classification Systems** — the MQM category set every error is classified into.
- **DP-03 Anchored Scoring Scales** — severity anchors, weights, and threshold fixed before reading.
- **NE-11 Embedded Calculation Formulas** — penalty total, per-1,000-word normalisation, and quality score.
- **QA-17 Named Scores for Multi-Dimensional Metrics** — penalty by category beside the pass/fail verdict.
- **QA-12 False Positives Identification** — preferential edits, source defects, and repeats excluded.

## Related Prompts

- `domain-professional-writing/translation/translation_project_brief_and_glossary.md` — the brief and glossary this review checks against.
- `domain-software-engineering/localization/localization_translation_management_workflow.md` — the software-release pipeline, a different job.
- `domain-discipleship/cross-cultural/discipleship_translated_material_pitfalls.md` — whether translated teaching material carries across cultures.
