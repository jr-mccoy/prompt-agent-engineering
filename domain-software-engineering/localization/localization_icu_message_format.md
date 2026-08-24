---
title: "ICU Message Format and Pluralization Rules"
category: domain-software-engineering/localization
description: "Implement ICU MessageFormat for complex translations including pluralization, gender selection, number formatting, and nested message patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - ST-03
difficulty: advanced
tags:
  - icu-messageformat
  - pluralization
  - gender
  - select
  - intl-messageformat
  - plural-rules
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/localization/localization_i18n_architecture_strategy.md
  - domain-software-engineering/localization/localization_date_number_currency_formatting.md
  - domain-software-engineering/localization/localization_translation_management_workflow.md
---

# ICU Message Format and Pluralization Rules

**Objective:** Implement ICU MessageFormat for handling complex translatable messages including pluralization, gender-dependent text, number/date formatting within messages, and nested selection patterns — ensuring correct linguistic output across all supported locales.

**When to Use:**
- Implementing messages that change based on count ("1 item" vs "5 items")
- Handling gender-dependent text in gendered languages (French, German, Arabic, Spanish)
- Embedding formatted numbers, dates, or currencies within translatable messages
- Migrating from string concatenation to structured message patterns
- Don't use when: All your messages are simple strings with no variables or plural forms

**Instructions:**

1. **Understand ICU MessageFormat Syntax**
   - ICU MessageFormat is the standard for parameterized, linguistically correct messages
   - Core syntax:
     ```
     {variableName, type, style}
     ```
   - Types available:
     - **Plain interpolation**: `Hello, {name}!`
     - **number**: `{count, number}` — locale-aware number formatting
     - **date**: `{when, date, medium}` — locale-aware date formatting
     - **time**: `{when, time, short}` — locale-aware time formatting
     - **plural**: `{count, plural, one {# item} other {# items}}`
     - **select**: `{gender, select, male {He} female {She} other {They}}`
     - **selectordinal**: `{rank, selectordinal, one {#st} two {#nd} few {#rd} other {#th}}`

2. **Implement Pluralization Correctly**
   - CLDR plural categories (not all languages use all categories):
     | Category | Used By | Rule (example) |
     |----------|---------|---------------|
     | `zero` | Arabic, Latvian, Welsh | Exact 0 in Arabic |
     | `one` | Most languages | 1 in English; 1, 21, 31... in Russian |
     | `two` | Arabic, Hebrew, Slovenian | Exact 2 in Arabic; 2, 102... in Slovenian |
     | `few` | Russian, Czech, Polish, Arabic | 2-4 in Russian; 3-10 in Arabic |
     | `many` | Russian, Polish, Arabic | 5-20 in Russian; 11-99 in Arabic |
     | `other` | ALL languages (required) | Fallback / default category |

   - English pluralization (simple — `one` + `other`):
     ```
     {count, plural,
       one {You have # new message}
       other {You have # new messages}
     }
     ```

   - Russian pluralization (complex — `one` + `few` + `many` + `other`):
     ```
     {count, plural,
       one {У вас # новое сообщение}
       few {У вас # новых сообщения}
       many {У вас # новых сообщений}
       other {У вас # новых сообщений}
     }
     ```

   - Arabic pluralization (6 forms):
     ```
     {count, plural,
       zero {ليس لديك رسائل}
       one {لديك رسالة واحدة}
       two {لديك رسالتان}
       few {لديك # رسائل}
       many {لديك # رسالة}
       other {لديك # رسالة}
     }
     ```

   - The `#` symbol is replaced with the formatted count value
   - Always include the `other` category — it's the required fallback
   - Exact matches override categories: `=0 {No messages}` overrides `zero`

3. **Implement Gender Selection**
   - Use `select` for gender-dependent text:
     ```
     {gender, select,
       male {He left a comment on his project}
       female {She left a comment on her project}
       other {They left a comment on their project}
     }
     ```
   - Gendered languages need gender for nouns AND adjective agreement:
     - French:
       ```
       {gender, select,
         male {{name} est connecté}
         female {{name} est connectée}
         other {{name} est connecté(e)}
       }
       ```
     - German (noun gender affects articles and adjective endings):
       ```
       {articleGender, select,
         masculine {Der neue {item} wurde erstellt}
         feminine {Die neue {item} wurde erstellt}
         neuter {Das neue {item} wurde erstellt}
         other {{item} wurde erstellt}
       }
       ```
   - Always include `other` as fallback for non-binary or unknown cases

4. **Combine Plural and Select (Nested Patterns)**
   - For messages that depend on both count and another variable:
     ```
     {gender, select,
       male {{count, plural,
         one {He added # photo to his album}
         other {He added # photos to his album}
       }}
       female {{count, plural,
         one {She added # photo to her album}
         other {She added # photos to her album}
       }}
       other {{count, plural,
         one {They added # photo to their album}
         other {They added # photos to their album}
       }}
     }
     ```
   - Keep nesting to a maximum of 2 levels (deeper nesting becomes unmaintainable for translators)
   - If logic exceeds 2 levels, split into separate messages

5. **Embed Formatted Values in Messages**
   - Numbers within messages:
     ```
     You have {count, number} items totaling {total, number, ::currency/USD}
     ```
   - Dates within messages:
     ```
     Your subscription renews on {date, date, long}
     ```
   - Custom number skeletons (ICU 67+):
     ```
     {price, number, ::currency/EUR unit-width-narrow}
     {percent, number, ::.0%}
     {fileSize, number, ::compact-short}
     ```
   - Ranges:
     ```
     Showing {start, number}-{end, number} of {total, number} results
     ```

6. **Implement in Your Framework**
   - **FormatJS (react-intl / intl-messageformat)**:
     ```tsx
     import { FormattedMessage } from 'react-intl';

     <FormattedMessage
       id="inbox.messageCount"
       defaultMessage="{count, plural, one {You have # new message} other {You have # new messages}}"
       values={{ count: messageCount }}
     />
     ```
   - **i18next (with ICU plugin)**:
     ```javascript
     // Install: npm install i18next-icu
     import ICU from 'i18next-icu';
     i18next.use(ICU).init({ /* config */ });

     // In translation file:
     { "messageCount": "{count, plural, one {You have # new message} other {You have # new messages}}" }

     // Usage:
     t('messageCount', { count: 5 });
     ```
   - **next-intl**:
     ```tsx
     const t = useTranslations('inbox');
     t('messageCount', { count: messageCount });
     // Message file: "{count, plural, one {You have # new message} other {You have # new messages}}"
     ```
   - **Android (strings.xml)**:
     ```xml
     <plurals name="message_count">
       <item quantity="one">You have %d new message</item>
       <item quantity="other">You have %d new messages</item>
     </plurals>
     ```
   - **iOS (Stringsdict)**:
     ```xml
     <key>message_count</key>
     <dict>
       <key>NSStringLocalizedFormatKey</key>
       <string>%#@count@</string>
       <key>count</key>
       <dict>
         <key>NSStringFormatSpecTypeKey</key>
         <string>NSStringPluralRuleType</string>
         <key>one</key>
         <string>You have %d new message</string>
         <key>other</key>
         <string>You have %d new messages</string>
       </dict>
     </dict>
     ```

7. **CRITICAL: Validate ICU Messages**
   - Parse all ICU messages at build time to catch syntax errors:
     ```javascript
     import { parse } from '@formatjs/icu-messageformat-parser';
     // Throws on syntax error
     parse('{count, plural, one {# item} other {# items}}');
     ```
   - Validate that all plural categories for target locales are present
   - Test with edge case values: 0, 1, 2, 5, 11, 21, 100, 101, 1000000
   - Verify that `#` is used (not hardcoded numbers) so formatting is locale-aware
   - Check that translators haven't broken ICU syntax (common: missing closing brace, extra spaces)

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag messages as needing pluralization when the count is always > 1 (e.g., "Compare 2 plans" — always exactly 2)
- Report missing `zero` category for languages that don't use it (only Arabic, Latvian, Welsh use `zero`)
- Assume all gendered languages need gender selection (only flag it when the translation actually varies)
- Flag Android `quantity="zero"` as unused — Android uses it for `=0` exact match regardless of CLDR
- Report ICU syntax errors in strings that aren't meant to be ICU format (some systems mix formats)
- Assume `one` always means "exactly 1" (in French, `one` covers 0 and 1; in Russian, it covers 1, 21, 31...)

✅ **DO:**
- Check CLDR plural rules for each target language before specifying required categories
- Verify that the i18n framework actually supports ICU MessageFormat (some only support simple interpolation)
- Test plural forms with values specific to each language's rule boundaries (e.g., test 2, 5, 21 for Russian)
- Validate that translators receive clear documentation about ICU syntax and placeholder meaning
- Confirm the parser version matches the ICU features used (number skeletons require ICU 67+)
- Test that the `other` category alone produces acceptable output as a minimum viable translation

**Expected Output:** An ICU MessageFormat implementation guide including:
- Message patterns for all complex strings
- Plural category requirements per target language
- Framework-specific implementation code
- Validation approach
- Translator documentation

**Example Output:**

```markdown
## ICU MessageFormat Implementation Guide

### Application: Task Management App
### Languages: English, French, German, Russian, Arabic, Japanese

---

### Plural Category Requirements

| Language | Categories Needed | Test Values |
|----------|------------------|-------------|
| English (en) | one, other | 0→other, 1→one, 2→other, 100→other |
| French (fr) | one, other | 0→one, 1→one, 2→other, 1000000→other |
| German (de) | one, other | 0→other, 1→one, 2→other, 100→other |
| Russian (ru) | one, few, many, other | 1→one, 2→few, 5→many, 21→one, 11→many |
| Arabic (ar) | zero, one, two, few, many, other | 0→zero, 1→one, 2→two, 5→few, 13→many, 100→other |
| Japanese (ja) | other | (All values→other — no plural distinction) |

---

### Message Catalog

#### Simple Plural Messages

**Task count (key: `tasks.count`):**

| Locale | Message |
|--------|---------|
| en | `{count, plural, =0 {No tasks} one {# task} other {# tasks}}` |
| fr | `{count, plural, =0 {Aucune tâche} one {# tâche} other {# tâches}}` |
| de | `{count, plural, =0 {Keine Aufgaben} one {# Aufgabe} other {# Aufgaben}}` |
| ru | `{count, plural, =0 {Нет задач} one {# задача} few {# задачи} many {# задач} other {# задач}}` |
| ar | `{count, plural, zero {لا توجد مهام} one {مهمة واحدة} two {مهمتان} few {# مهام} many {# مهمة} other {# مهمة}}` |
| ja | `{count, plural, =0 {タスクなし} other {タスク#件}}` |

**Test matrix:**

| Value | en | fr | ru | ar |
|-------|----|----|----|----|
| 0 | No tasks | Aucune tâche | Нет задач | لا توجد مهام |
| 1 | 1 task | 1 tâche | 1 задача | مهمة واحدة |
| 2 | 2 tasks | 2 tâches | 2 задачи | مهمتان |
| 5 | 5 tasks | 5 tâches | 5 задач | ٥ مهام |
| 21 | 21 tasks | 21 tâches | 21 задача | ٢١ مهمة |
| 100 | 100 tasks | 100 tâches | 100 задач | ١٠٠ مهمة |

---

#### Gender + Plural (Nested)

**User action notification (key: `notifications.userAction`):**

English:
```
{gender, select,
  male {{count, plural,
    one {{name} completed # task on his project}
    other {{name} completed # tasks on his project}
  }}
  female {{count, plural,
    one {{name} completed # task on her project}
    other {{name} completed # tasks on her project}
  }}
  other {{count, plural,
    one {{name} completed # task on their project}
    other {{name} completed # tasks on their project}
  }}
}
```

French (adjective agreement):
```
{gender, select,
  male {{count, plural,
    one {{name} a terminé # tâche sur son projet}
    other {{name} a terminé # tâches sur son projet}
  }}
  female {{count, plural,
    one {{name} a terminé # tâche sur son projet}
    other {{name} a terminé # tâches sur son projet}
  }}
  other {{count, plural,
    one {{name} a terminé # tâche sur son projet}
    other {{name} a terminé # tâches sur son projet}
  }}
}
```

---

#### Embedded Formatting

**Storage usage (key: `storage.usage`):**
```
You are using {used, number, ::compact-short} of {total, number, ::compact-short}
```

| Values | en | de | ja |
|--------|----|----|-----|
| used=1500000, total=5000000 | You are using 1.5M of 5M | Sie verwenden 1,5 Mio. von 5 Mio. | 150万中150万使用中 |

**Subscription renewal (key: `subscription.renewal`):**
```
Your plan renews on {date, date, long} for {price, number, ::currency/USD}
```

---

### Build-Time Validation Script

```typescript
// scripts/validate-icu-messages.ts
import { parse } from '@formatjs/icu-messageformat-parser';
import * as fs from 'fs';
import * as path from 'path';

const LOCALES_DIR = './messages';
const errors: string[] = [];

for (const locale of fs.readdirSync(LOCALES_DIR)) {
  const localeDir = path.join(LOCALES_DIR, locale);
  if (!fs.statSync(localeDir).isDirectory()) continue;

  for (const file of fs.readdirSync(localeDir)) {
    if (!file.endsWith('.json')) continue;
    const messages = JSON.parse(fs.readFileSync(path.join(localeDir, file), 'utf-8'));

    for (const [key, value] of Object.entries(messages)) {
      const message = typeof value === 'string' ? value : (value as any).message;
      if (!message) continue;

      try {
        parse(message);
      } catch (e) {
        errors.push(`[${locale}/${file}] ${key}: ${(e as Error).message}`);
      }
    }
  }
}

if (errors.length > 0) {
  console.error(`Found ${errors.length} ICU MessageFormat errors:`);
  errors.forEach(e => console.error(`  ❌ ${e}`));
  process.exit(1);
} else {
  console.log('✅ All ICU messages are valid');
}
```

### Translator Documentation

Provide this guide to translators:

**ICU Syntax Quick Reference for Translators:**

| Pattern | Meaning | Example |
|---------|---------|---------|
| `{name}` | Variable — replaced at runtime | `Hello, {name}!` → "Hello, Alice!" |
| `#` | Current number in a plural block | `{count, plural, other {# items}}` → "5 items" |
| `{count, plural, ...}` | Different text based on count | See plural category guide |
| `{gender, select, ...}` | Different text based on selection | `male {He} female {She} other {They}` |
| `'{'` | Literal brace (escaped) | `It costs {price} '{'not free'}'` |

**Rules for translators:**
1. Never remove or rename `{variables}` — they must stay exactly as-is
2. You CAN reorder variables and text — different languages have different word order
3. Always include all plural categories provided in the source
4. Use `#` for the number, don't type the number literally
5. If unsure about ICU syntax, add a comment — don't guess
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Focused on ICU MessageFormat, not general i18n
- ST-02 (Sequential Step-by-Step Instructions) - From syntax understanding through implementation to validation
- RT-02 (Multi-Dimensional Analysis) - Covers plurals, gender, formatting, nesting, and validation
- RT-05 (Evidence-Based Reasoning) - CLDR data drives plural category requirements per language
- ST-03 (Structured Output Templates) - Consistent message catalog and test matrix format

**Related Prompts:**
- `localization_i18n_architecture_strategy.md` - Framework selection affects ICU support
- `localization_date_number_currency_formatting.md` - Standalone formatting for non-message contexts
- `localization_translation_management_workflow.md` - Translator handoff for ICU messages

**Customization Guide:**
- **For React (FormatJS)**: Focus on `<FormattedMessage>` and `intl.formatMessage()` with ICU syntax
- **For mobile (iOS)**: Focus on Stringsdict XML format for plurals and `String(localized:)` API
- **For mobile (Android)**: Focus on `plurals` resources in `strings.xml` and `MessageFormat` in Kotlin/Java
- **For languages with complex plurals (Arabic, Russian, Polish)**: Provide extended test matrices with all boundary values
- **For teams new to ICU**: Include a translator training section with interactive examples
