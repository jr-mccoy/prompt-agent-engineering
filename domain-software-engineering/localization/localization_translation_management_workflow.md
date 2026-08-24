---
title: "Translation Management Workflow"
category: domain-software-engineering/localization
description: "Design and implement translation management workflows including TMS integration, translator handoff, quality assurance, and CI/CD automation"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - ST-03
difficulty: intermediate
tags:
  - translation-management
  - tms
  - localization-workflow
  - translation-pipeline
  - crowdin
  - lokalise
  - phrase
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/localization/localization_i18n_architecture_strategy.md
  - domain-software-engineering/localization/localization_icu_message_format.md
  - domain-software-engineering/localization/localization_pseudo_localization_testing.md
---

# Translation Management Workflow

**Objective:** Design and implement a translation management workflow including TMS (Translation Management System) integration, developer-translator handoff processes, translation quality assurance, and CI/CD automation for continuous localization.

**When to Use:**
- Setting up a translation pipeline for the first time
- Integrating a TMS (Crowdin, Lokalise, Phrase, Transifex) into your development workflow
- Improving translation turnaround time or quality
- Scaling from manual translation management to automated workflows
- Don't use when: You have fewer than 50 strings and plan to manage translations manually in JSON files

**Instructions:**

1. **Assess Translation Requirements**
   - Count total translatable strings and estimate growth rate
   - Identify target languages and regional variants (e.g., `pt-BR` vs `pt-PT`)
   - Determine translation sources: professional translators, in-house team, community, machine translation
   - Assess content types: UI strings, long-form content, legal text, marketing copy
   - Identify content that changes frequently vs. rarely
   - Check for context requirements (screenshots, developer notes, character limits)

2. **Select a Translation Management System (TMS)**
   - Evaluate platforms against key criteria:

     | Feature | Crowdin | Lokalise | Phrase | Transifex |
     |---------|---------|----------|--------|-----------|
     | GitHub/GitLab integration | Native | Native | Native | Native |
     | In-context editing | Yes | Yes | Yes | Limited |
     | Machine translation | 30+ engines | 8+ engines | 10+ engines | 5+ engines |
     | Translation memory | Yes | Yes | Yes | Yes |
     | Glossary/terminology | Yes | Yes | Yes | Yes |
     | API & CLI | Full | Full | Full | Full |
     | Branching support | Yes | Limited | Yes | No |
     | Screenshot context | Yes | Yes | Yes | Limited |
     | Pluralization (ICU) | Yes | Yes | Yes | Yes |

   - Additional factors: pricing model (per-word, per-user, flat), freelancer marketplace access, QA checks, workflow customization

3. **Design the Translation Pipeline**
   - Define the end-to-end flow:
     ```
     Developer adds string → Extraction → Upload to TMS →
     Translator translates → Review → QA checks →
     Download → PR/merge → Deploy
     ```
   - Decide on sync strategy:
     - **Push-based**: CI pushes source strings to TMS on merge to main
     - **Pull-based**: CI pulls translations from TMS before build
     - **Bidirectional**: GitHub integration syncs both ways automatically
   - Configure branch-aware translations (feature branch strings don't pollute main)
   - Set up translation memory (TM) to reuse existing translations for similar strings

4. **Implement Developer-Translator Handoff**
   - Add context for translators on every string:
     - **Description/note**: Explain where the string appears and its purpose
     - **Character limit**: Maximum length for UI constraints
     - **Screenshot**: Automated or manual screenshot showing the string in context
     - **Placeholders**: Document all variables (`{name}`, `{count}`) with example values
   - Example context-rich source file:
     ```json
     {
       "checkout.submit": {
         "message": "Complete purchase ({total})",
         "description": "Button text on checkout page. {total} is formatted price like $49.99",
         "maxLength": 30,
         "screenshot": "checkout-page.png"
       }
     }
     ```
   - Establish a process for translators to ask questions (TMS comments, Slack channel)
   - Define turnaround time expectations per priority level

5. **Implement Translation Quality Assurance**
   - Configure automated QA checks in the TMS:
     - **Placeholder consistency**: All `{variables}` from source exist in translation
     - **ICU syntax validation**: Plural/select patterns are syntactically correct
     - **Length constraints**: Translation doesn't exceed character limits
     - **Terminology consistency**: Glossary terms are used correctly
     - **Punctuation consistency**: Matching trailing periods, colons, etc.
     - **Untranslated segments**: Flag strings left in source language
   - Implement review workflows:
     - **Single review**: Translator → Reviewer → Done
     - **Two-pass**: Machine translation → Human post-edit → Reviewer → Done
     - **Community**: Translator → Community vote → Moderator approval → Done
   - Run linguistic QA on full pages (not just individual strings) for context coherence

6. **Automate with CI/CD**
   - Configure source string extraction in CI:
     ```yaml
     # On merge to main: push new/changed source strings to TMS
     - name: Extract and push source strings
       run: |
         npx formatjs extract 'src/**/*.tsx' --out-file extracted.json
         crowdin push --source extracted.json
     ```
   - Configure translation download before build:
     ```yaml
     # On build: pull latest translations from TMS
     - name: Pull translations
       run: |
         crowdin pull --all
         # Verify no missing translations for release languages
         node scripts/check-translation-coverage.js --min-coverage 95
     ```
   - Set up webhooks for translation completion notifications
   - Create a translation coverage gate:
     - Block release if coverage < threshold (e.g., 95% for Tier 1 languages)
     - Warn but don't block for Tier 2 languages (e.g., 80%)
   - Automate PR creation when new translations are ready

7. **CRITICAL: Validate the Workflow End-to-End**
   - Test the full cycle: add a string → see it in TMS → translate → verify in app
   - Confirm that updated translations don't require a full redeploy
   - Verify translation memory works across similar strings
   - Check that branch translations don't leak into production
   - Validate QA checks catch real issues (introduce deliberate errors to test)
   - Confirm the process handles string deletion and key renaming gracefully

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Recommend a TMS that doesn't support the project's file format (e.g., suggesting XLIFF workflows for a JSON-based project without confirming format support)
- Flag machine-translated strings as quality issues if the project intentionally uses MT for non-critical content
- Report missing translations for strings marked as "do not translate" in the TMS
- Assume all strings need human translation (technical terms, brand names, numbers may not)
- Flag translation coverage gaps for languages still in pilot/beta phase
- Recommend complex branching workflows for teams with < 3 translators

✅ **DO:**
- Verify the TMS integration actually syncs correctly before declaring it "set up"
- Check if existing translation memory from a previous TMS can be migrated
- Confirm that the CI/CD pipeline handles TMS API rate limits and timeouts
- Test QA checks against known good and known bad translations
- Validate that the workflow handles concurrent translators working on the same file
- Check if screenshots auto-update when UI changes

**Expected Output:** A complete translation management workflow document including:
- TMS recommendation with rationale
- Pipeline architecture diagram
- CI/CD configuration
- QA check specifications
- Coverage thresholds and release gates
- Team roles and responsibilities

**Example Output:**

```markdown
## Translation Management Workflow

### Application: E-commerce Platform (Next.js)
### Languages: English (source), Spanish, French, German, Japanese
### TMS: Crowdin (selected)

---

### Pipeline Architecture

```
┌──────────────┐     ┌──────────┐     ┌──────────────┐
│  Developer    │────▶│  GitHub   │────▶│   Crowdin    │
│  adds string  │     │  (main)  │     │   (source)   │
└──────────────┘     └──────────┘     └──────┬───────┘
                                              │
                     ┌──────────────────────────┤
                     ▼              ▼           ▼
               ┌──────────┐ ┌──────────┐ ┌──────────┐
               │ Spanish  │ │ French   │ │ German   │
               │translator│ │translator│ │translator│
               └────┬─────┘ └────┬─────┘ └────┬─────┘
                    │             │             │
                    ▼             ▼             ▼
               ┌──────────────────────────────────┐
               │       Crowdin QA Checks          │
               │  (placeholders, length, glossary) │
               └──────────────┬───────────────────┘
                              │
                              ▼
               ┌──────────────────────────────────┐
               │    Review & Approval Workflow     │
               └──────────────┬───────────────────┘
                              │
                              ▼
               ┌──────────────────────────────────┐
               │  Auto-PR to GitHub (translations) │
               └──────────────┬───────────────────┘
                              │
                              ▼
               ┌──────────────────────────────────┐
               │   CI: Coverage check + build     │
               └──────────────┬───────────────────┘
                              │
                              ▼
               ┌──────────────────────────────────┐
               │          Deploy                   │
               └──────────────────────────────────┘
```

### Crowdin Configuration

**`crowdin.yml`:**
```yaml
project_id: "12345"
api_token_env: "CROWDIN_TOKEN"
preserve_hierarchy: true
files:
  - source: "/messages/en/**/*.json"
    translation: "/messages/%locale%/**/%original_file_name%"
    type: "json"
    translatable_elements:
      - "/message"
    context:
      - "/description"
    max_length:
      - "/maxLength"
```

### CI/CD Integration

**Source String Push (on merge to `main`):**
```yaml
name: Push Source Strings
on:
  push:
    branches: [main]
    paths: ['messages/en/**']

jobs:
  push-sources:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Push to Crowdin
        uses: crowdin/github-action@v2
        with:
          upload_sources: true
          upload_translations: false
        env:
          CROWDIN_PROJECT_ID: ${{ secrets.CROWDIN_PROJECT_ID }}
          CROWDIN_PERSONAL_TOKEN: ${{ secrets.CROWDIN_TOKEN }}
```

**Translation Pull (nightly + on-demand):**
```yaml
name: Pull Translations
on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC
  workflow_dispatch: {}

jobs:
  pull-translations:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Pull from Crowdin
        uses: crowdin/github-action@v2
        with:
          download_translations: true
          create_pull_request: true
          pull_request_title: 'i18n: update translations'
          pull_request_labels: 'i18n,automated'
        env:
          CROWDIN_PROJECT_ID: ${{ secrets.CROWDIN_PROJECT_ID }}
          CROWDIN_PERSONAL_TOKEN: ${{ secrets.CROWDIN_TOKEN }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Coverage Gate (on PR):**
```yaml
- name: Check translation coverage
  run: |
    node scripts/check-coverage.js \
      --tier1 "es,fr,de" --tier1-min 95 \
      --tier2 "ja" --tier2-min 80 \
      --fail-on-tier1
```

### QA Checks Enabled in Crowdin

| Check | Severity | Action |
|-------|----------|--------|
| Missing placeholders | Error | Block approval |
| Extra placeholders | Error | Block approval |
| ICU syntax errors | Error | Block approval |
| Exceeds max length | Warning | Flag for review |
| Inconsistent terminology | Warning | Flag for review |
| Untranslated strings | Info | Track in dashboard |
| Leading/trailing spaces | Warning | Auto-fix |
| Double spaces | Warning | Auto-fix |

### Translation Coverage Thresholds

| Tier | Languages | Min Coverage | Release Gate |
|------|-----------|-------------|-------------|
| Tier 1 | es, fr, de | 95% | Block release |
| Tier 2 | ja | 80% | Warn only |
| Pilot | (future) | 50% | No gate |

### Roles and Responsibilities

| Role | Responsibility | Person/Team |
|------|---------------|-------------|
| i18n Lead | Pipeline maintenance, TMS admin, coverage tracking | Engineering |
| Developers | Add context/descriptions, use i18n APIs correctly | All devs |
| Translators | Translate, ask questions, flag ambiguities | External agency |
| Reviewers | Approve translations, resolve disputes | Native speakers (internal) |
| QA | Verify translations in-app, report visual issues | QA team |

### String Context Template

Every new translatable string must include:
```json
{
  "checkout.promoCode.apply": {
    "message": "Apply code",
    "description": "Button to apply a promotional discount code on the checkout page. Appears next to the promo code input field.",
    "maxLength": 20,
    "placeholders": {}
  },
  "checkout.promoCode.applied": {
    "message": "{code} applied — you save {amount}",
    "description": "Success message after applying a promo code. {code} is the promo code text (e.g., 'SAVE20'). {amount} is a formatted price (e.g., '$15.00').",
    "maxLength": 60,
    "placeholders": {
      "code": { "example": "SAVE20" },
      "amount": { "example": "$15.00" }
    }
  }
}
```
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Scoped to translation workflow, not i18n architecture
- ST-02 (Sequential Step-by-Step Instructions) - From assessment through automation
- RT-02 (Multi-Dimensional Analysis) - Covers TMS selection, pipeline, QA, and CI/CD dimensions
- CM-01 (Explicit Context Framing) - Requires project details before TMS recommendation
- ST-03 (Structured Output Templates) - Consistent table and configuration formats

**Related Prompts:**
- `localization_i18n_architecture_strategy.md` - Overall i18n architecture (file structure, framework)
- `localization_icu_message_format.md` - ICU message syntax that translators will encounter
- `localization_pseudo_localization_testing.md` - Testing translations before they arrive
- `domain-software-engineering/devops/devops_cicd_pipeline_analysis.md` - General CI/CD pipeline patterns

**Customization Guide:**
- **For open-source projects**: Focus on Crowdin's free OSS plan, community translation, and Weblate (self-hosted alternative)
- **For enterprise with legal/regulated content**: Add legal review step, translation memory segmentation for regulated vs. non-regulated content
- **For mobile apps**: Add app store listing translation, screenshot localization, and platform-specific file format handling
- **For CMS-driven content**: Integrate TMS with headless CMS (Contentful, Sanity) rather than code-level strings
- **For small teams (< 5 languages)**: Simplify to GitHub-integrated workflow without full TMS; use Crowdin/Lokalise free tier


---

## Must / Must Not

**Must:**
- Tailor the workflow to team size, regulated-content status, platform (web/mobile/CMS), and language count (< 5 vs. 20+).
- Specify TMS (Translation Management System) selection criteria: file-format support, CI/CD integration, QA features, pricing model.
- Cover the full loop: string extraction → TMS sync → translator review → QA → merge back → deployment → monitoring.
- Include **translation memory** and **term base** strategy — these are the two artifacts that compound value over time.
- Address **pseudo-localization** as a pre-translation QA gate.

**Must Not:**
- Recommend a single TMS as "best" without acknowledging fit depends on the team profile.
- Ignore **plurals**, **gendered** forms, and **RTL** handling — these are where naïve workflows break.
- Recommend GitHub-only workflows for 10+ language, enterprise-scale programs (won't scale).
- Suggest machine translation without a human review gate for legal, medical, or marketing content.
- Overlook the **app-store / listing localization** side of the workflow — it's often a separate track with its own deadlines.

## Verification (Self-Check)

Before delivering the workflow:

1. **Team profile confirmed** — Size, languages, regulated content yes/no, platform mix.
2. **Full loop covered** — Extraction, translation, QA, merge, deploy, monitor all specified.
3. **Quality gates explicit** — Pseudo-localization in CI, in-context review, TM/glossary enforcement, back-translation for critical content.
4. **Confidence labeled** — High for well-trodden mobile/web workflows; Medium for unusual combinations.

## False-Positive Prevention

Rule out:

- **"Need a full TMS"** — Teams with < 5 languages and < 500 strings may be fine with a spreadsheet + git.
- **"Machine translation everything"** — Fine for bulk draft, but every string in a regulated domain needs human review.
- **"One merge flow fits all"** — Marketing copy and UI strings often have different cadences and reviewers.
- **"Continuous localization = no review"** — Continuous localization still requires QA gates; it just automates the plumbing.
