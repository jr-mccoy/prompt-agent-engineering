# Translation — Human Translation Craft: Briefing, Quality Review, and Transcreation

Three prompts for commissioning, checking, and adapting **human translation** of
documents and creative copy. They are about language and readers, not software: string
files, translation-management systems, and release pipelines live in
[`domain-software-engineering/localization/`](../../domain-software-engineering/localization/README.md).

## Contents

| File | Use |
|---|---|
| [`translation_project_brief_and_glossary.md`](translation_project_brief_and_glossary.md) | Brief a translator: purpose in the target culture, audience, language variant, translation + independent revision (ISO 17100), defaults with reasons, style sheet, concept-based glossary with approved and forbidden terms, do-not-translate list, false friends, query route |
| [`translation_quality_review_mqm.md`](translation_quality_review_mqm.md) | Score a finished translation MQM-style: categories, severity anchors, weights and threshold fixed first; span-level annotation; preferential edits and source defects excluded; penalty per 1,000 words; named sub-scores; any critical = fail; feedback that teaches |
| [`translation_transcreation_brief.md`](translation_transcreation_brief.md) | Re-create slogans, headlines, and campaign lines: intent/mechanism decomposition, fixed vs free (claims never strengthened), close/adapted/free routes with back-translations, risk-gated scoring, in-market native check, trademark and legal flags |

Order of use: brief and glossary → translation (by a human translator) → MQM review;
transcreation runs alongside for the creative lines a brief should not translate literally.

## Guards (every prompt)

- **Humans judge what models cannot.** Accuracy is confirmed by a bilingual reviewer;
  transcreated lines by an in-market native speaker. A model may draft annotations or
  routes; it does not sign them off.
- **Source problems are queries,** never silent corrections by the translator.
- **Claims and legal lines stay fixed** in adaptation; names and claims go to a trademark
  or legal check in the target market.

## Boundaries — not here

| If you need… | Go to |
|---|---|
| Software localization: i18n architecture, TMS pipelines, ICU messages, pseudo-localization | [`domain-software-engineering/localization/`](../../domain-software-engineering/localization/README.md) (`localization_translation_management_workflow.md`) |
| Regional adaptation of a product's imagery, colour, and content strategy | [`domain-software-engineering/localization/localization_cultural_adaptation.md`](../../domain-software-engineering/localization/localization_cultural_adaptation.md) |
| Comparing Bible translations and why renderings differ | [`domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md`](../../domain-biblical-studies/exegesis-interpretation/biblical_translation_comparison.md) |
| Whether translated teaching material carries across cultures | [`domain-discipleship/cross-cultural/discipleship_translated_material_pitfalls.md`](../../domain-discipleship/cross-cultural/discipleship_translated_material_pitfalls.md) |
| Translation and foreign-rights deals for a book | [`domain-childrens-writing/publishing-business/childrens_translation_rights_considerations.md`](../../domain-childrens-writing/publishing-business/childrens_translation_rights_considerations.md) |
| Writing the source-language marketing copy | [`domain-agentic-resources/skills/marketing/copywriting/`](../../domain-agentic-resources/skills/marketing/copywriting/SKILL.md) |
