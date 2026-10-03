---
title: "Translation Project Brief and Glossary — Purpose, Audience, Style Sheet, Approved Terms, and a Query Route Before a Human Translator Starts"
category: professional-writing/translation
description: "Prepare a human translation job so the translator does not have to guess: a brief built on the text's purpose in the target culture (audience, language variant, register, form of address, what the text must achieve), the workflow of translation plus independent revision by a second linguist as in ISO 17100, a style sheet, a concept-based glossary with approved and forbidden target terms and do-not-translate items, reference materials, and a named query route — with stated defaults for anything the client leaves open."
techniques:
  - CM-01
  - MP-06
  - IT-26
  - DS-26
difficulty: intermediate
tags:
  - human-translation
  - translation-brief
  - terminology
  - glossary
  - style-sheet
  - iso-17100
  - brief-a-translator
  - hire-a-translator
  - consistent-terms-across-languages
updated: "2026-10-02"
related_prompts:
  - domain-professional-writing/translation/translation_quality_review_mqm.md
  - domain-professional-writing/translation/translation_transcreation_brief.md
  - domain-software-engineering/localization/localization_translation_management_workflow.md
---

# Translation Project Brief and Glossary

**Objective:** Give a professional translator everything they need before the first
sentence — why the text exists in the new language, who reads it, how it should sound,
which terms are fixed, and who answers questions — so that the translation is right
the first time and consistent across translators and later jobs.

**When to Use:**
- You are commissioning a human translation of a document, report, book, exhibition,
  website copy, or set of materials, and want it done to a professional standard.
- Several translators or a series of jobs must use the same terms.
- A previous translation came back accurate but wrong in tone, address, or terminology.
- **Not this prompt if** you are wiring translation into a software release process —
  string files, translation-management systems, automated pipelines — use
  `domain-software-engineering/localization/localization_translation_management_workflow.md`.
  For slogans, headlines, and campaign lines that must be re-created rather than
  translated, use `translation/translation_transcreation_brief.md`. To score a finished
  translation, `translation/translation_quality_review_mqm.md`.

## Inputs / Context

1. **Source text** — final version, word count, file format, and what may still change.
2. **Purpose** — what the text must do for its new readers (inform, persuade, instruct,
   comply), and where it will appear.
3. **Audience** — who reads it, their expertise, country or region.
4. **Target language and variant** — e.g. European vs Brazilian Portuguese, Mexican vs
   European Spanish, French for France vs Canada.
5. **Existing materials** — earlier translations, a client glossary or style guide,
   bilingual reference documents, brand voice.
6. **Constraints** — deadline, budget, regulated wording, legal sign-off, space limits.
7. **People** — who answers subject questions; who approves the final text.

## Method

1. **Ask before assuming (MP-06).** If purpose, audience, or language variant is missing,
   ask; those three change the translation itself. Everything else can take a stated default.
2. **Frame the brief around purpose (CM-01).** The same source can need different
   translations: a museum label for visitors and a catalogue essay for specialists are
   two jobs. State the function in the target culture, the reader, and what success
   looks like ("a German visitor reads the panel in under a minute and knows why the
   expedition failed").
3. **Fix the workflow.** Professional practice (ISO 17100, the translation-services
   standard) separates **translation** from **revision** by a second qualified linguist
   comparing source and target; add **review** by a target-language subject expert and
   **proofreading** of the final layout where stakes justify it. Name who does each step.
4. **Set defaults for everything unstated (DS-26).**

   | Parameter | Default | Change when |
   |---|---|---|
   | Register | as in the source | the target culture expects more or less formality |
   | Form of address | the target culture's norm for this text type | brand voice specifies |
   | Names of people, places, organisations | keep; add an established target name if one exists | client glossary says otherwise |
   | Units, dates, numbers, currency | target conventions; original in brackets if legally relevant | regulated text |
   | Quotations from published works | use the existing published translation, cited | none exists → translate and mark |
   | Inclusive language | target-language norms the client approves | client policy |
   | Ambiguity in source | query, do not choose silently | — |

5. **Build the glossary as a reference catalogue (IT-26).** One **concept** per entry,
   not one word: definition or context, the source term, the **approved** target term,
   **forbidden** alternatives with why, part of speech and gender where relevant, a usage
   example, status (approved / proposed / under query), and who approved it. Add a
   **do-not-translate** list (brand names, product names, titles of works with no
   published translation) and a short list of known **false friends** for the pair.
6. **Write the style sheet.** Tone in three adjectives with an example sentence; punctuation
   and quotation-mark conventions; capitalisation of titles; how to handle source errors
   (query, never silently correct a figure).
7. **Set the query route.** One named person, a response time, a shared query log;
   translator queries are expected, and answers are added back to the glossary.

## Output Format

```
# Translation brief — [project]   [source] → [target variant]   [n] words   Due: [..]

## Purpose and audience
Function in target culture: [...]  Reader: [...]  Where it appears: [...]
Success looks like: [...]

## Workflow
Translation: [..]  Revision (second linguist): [..]  Review: [..]  Proofread: [..]

## Defaults applied
| Parameter | Setting | Reason |

## Style sheet
Tone: [...]  Address: [...]  Conventions: [...]  Source errors: query

## Glossary
| # | Concept / context | Source term | Approved target | Forbidden (why) | Notes | Status |

## Do not translate
[...]

## Known false friends
[...]

## References supplied
[...]

## Queries
To: [..]  Response within: [..]  Log: [location]
```

## Verification

- [ ] Purpose, audience, and language variant are stated, not defaulted.
- [ ] Translation and revision are done by different people, both named.
- [ ] Every default lists its reason; every client override is visible.
- [ ] Each glossary entry is one concept with context, an approved term, and a status.
- [ ] Forbidden alternatives say why (wrong sense, competitor's term, outdated, offensive).
- [ ] The query route names a person and a response time.

## False-Positive Prevention

1. **A glossary is not a word list.** "Board" without context is three concepts
   (directors, plank, committee); one entry per concept.
2. **Don't over-fix terms.** Lock the terms that must be consistent; leave ordinary
   vocabulary to the translator's judgement.
3. **Don't brief the language, brief the reader.** "Spanish" is not an audience.
4. **Don't let the brief rewrite the source.** Source problems are queries for the
   author, not instructions to the translator to improve the text.
5. **Machine output is not a translation brief's starting text** unless the client has
   chosen post-editing; if so, say so, because it changes the job and the price.
6. **Don't copy an old glossary forward unexamined.** Outdated or offensive terms in a
   previous job's list are fixed here, with the reason.

## Example Output

Scenario: a touring exhibition, "Into the Ice: The Franklin Expedition", 14 wall panels
and 60 object labels (6,200 words), English → German (Germany), opening in Hamburg;
existing English catalogue; curator available for questions.

```
# Translation brief — Into the Ice   EN → DE (Germany)   6,200 words   Due: 2026-11-20

## Purpose and audience
Function: visitors read panels standing up; labels identify and explain objects.
Reader: general adult visitors, many families; no specialist knowledge.
Success looks like: a panel is read in under a minute; labels match object captions in the guide.

## Workflow
Translation: A. Becker (EN→DE, museum texts) · Revision: K. Wolf (second linguist) ·
Review: Hamburg curator (subject) · Proofread: final panel PDFs.

## Defaults applied
| Address     | none — impersonal panels; "Sie" in the family trail | German museum convention |
| Ship names  | Erebus, Terror — unchanged, italic | names of vessels |
| Units       | metric first, imperial from quotes kept in brackets | quotes are historical |
| Quotations  | published German edition of Franklin's journal where one exists | cite edition |

## Style sheet
Tone: clear, sober, vivid. "Am 26. Juli 1845 sahen Walfänger die Schiffe zum letzten Mal."
Quotation marks: „…“  Source errors: query to the curator.

## Glossary
| 1 | sledge hauled by crew      | sledge          | Schlitten         | Rodel (toboggan)      | — | approved |
| 2 | Indigenous people of the Arctic | Inuit      | Inuit             | "Eskimo" (outdated, offensive to many) | plural and adjective "Inuit" | approved |
| 3 | sea ice compressed by wind | pack ice        | Packeis           | Treibeis (drift ice — different concept) | — | approved |
| 4 | expedition members         | expedition party| Expeditionsmannschaft | Partei (political party) | — | approved |
| 5 | Admiralty orders           | Admiralty       | Admiralität       | — | institutional name | under query |

## Do not translate
HMS Erebus, HMS Terror; lender names on credit lines

## Known false friends
eventually ≠ eventuell · actual ≠ aktuell · provisions (supplies) ≠ Provision (commission)

## Queries
To: curator J. Hale · within 2 working days · shared query sheet; answers added to glossary.
```

## Techniques Used

- **CM-01 Explicit Context Framing** — purpose, reader, and setting drive the brief before any terms.
- **MP-06 Fallback Question Protocol** — purpose, audience, and variant are asked, never assumed.
- **IT-26 Reference Catalog Pattern** — the concept-based glossary, do-not-translate list, and false friends.
- **DS-26 Safe Defaults Pattern** — defaults for every unstated parameter, each with a reason to change.

## Related Prompts

- `domain-professional-writing/translation/translation_quality_review_mqm.md` — scoring the finished translation against this brief.
- `domain-professional-writing/translation/translation_transcreation_brief.md` — lines that need re-creation, not translation.
- `domain-software-engineering/localization/localization_translation_management_workflow.md` — the software-release pipeline, a different job.
