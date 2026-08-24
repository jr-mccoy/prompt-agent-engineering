---
title: "i18n Architecture Strategy"
category: domain-software-engineering/localization
description: "Design and audit internationalization architecture including string extraction, locale management, framework selection, and i18n-ready code patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - i18n
  - internationalization
  - architecture
  - locale-management
  - string-extraction
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/localization/localization_icu_message_format.md
  - domain-software-engineering/localization/localization_translation_management_workflow.md
  - domain-software-engineering/localization/localization_pseudo_localization_testing.md
---

# i18n Architecture Strategy

**Objective:** Design or audit a codebase's internationalization architecture — covering string extraction, locale management, framework selection, fallback chains, and i18n-ready code patterns — to enable scalable multi-language support.

**When to Use:**
- Starting internationalization on a greenfield or existing project
- Auditing current i18n setup for completeness and best practices
- Planning expansion to new languages or regions
- Migrating between i18n frameworks or approaches
- Don't use when: You only need to format dates/numbers (use `localization_date_number_currency_formatting.md` instead)

**Instructions:**

1. **Assess Current State and Requirements**
   - Identify target languages and regions (now and planned)
   - Determine if the app needs locale-specific content, not just translation
   - Inventory existing hardcoded strings, templates, and user-facing text
   - Identify the tech stack (React, Vue, Angular, iOS, Android, backend framework)
   - Determine deployment model (single build vs. per-locale builds)
   - Check for existing i18n library usage and configuration

2. **Select i18n Framework and Tooling**
   - Match framework to tech stack:
     - **React**: `react-intl` (FormatJS), `react-i18next`, `next-intl`
     - **Vue**: `vue-i18n`, `nuxt-i18n`
     - **Angular**: `@angular/localize`, `ngx-translate`
     - **iOS**: `NSLocalizedString`, String Catalogs (Xcode 15+)
     - **Android**: `strings.xml` resource system
     - **Backend (Node.js)**: `i18next`, `FormatJS/intl-messageformat`
     - **Backend (Python)**: `gettext`, `Babel`
     - **Backend (Java/Kotlin)**: `java.util.ResourceBundle`, Spring `MessageSource`
   - Evaluate key criteria: ICU MessageFormat support, pluralization, interpolation, lazy loading, SSR compatibility, TypeScript support
   - Assess tooling for extraction (e.g., `formatjs extract`, `i18next-parser`)

3. **Design String Management Architecture**
   - Define message key naming convention:
     - Hierarchical: `pages.checkout.form.email.label`
     - Feature-scoped: `checkout.emailLabel`
     - Flat with namespaces: `checkout:emailLabel`
   - Choose translation file format: JSON, YAML, XLIFF, PO/POT, ARB
   - Define file organization strategy:
     - **Single file per locale**: `en.json`, `fr.json` — simple but large
     - **Namespace-split per locale**: `en/common.json`, `en/checkout.json` — enables lazy loading
     - **Co-located**: Translation files alongside components — good for DX, harder to manage
   - Plan for lazy loading / code-splitting translations by route or feature
   - Design fallback chain: `en-GB` → `en` → default messages

4. **Establish Extraction and Enforcement Patterns**
   - Set up automated string extraction from source code
   - Configure linting rules to prevent hardcoded strings:
     - ESLint: `eslint-plugin-i18next`, `eslint-plugin-formatjs`
     - Custom lint rules for template literals with user-facing text
   - Create CI checks that fail on un-extracted strings
   - Define patterns for dynamic strings, error messages, and validation text
   - Handle strings in constants, enums, and configuration files

5. **Design Locale Detection and Switching**
   - Implement locale detection priority chain:
     1. URL path/subdomain (`/fr/products`, `fr.example.com`)
     2. User preference (stored in profile/cookie)
     3. `Accept-Language` header
     4. Browser/OS default
     5. Application default
   - Design locale switching UX (dropdown, auto-detect, remember preference)
   - Handle locale persistence across sessions
   - Plan URL strategy: path-based (`/fr/`), subdomain (`fr.`), query param (`?lang=fr`), or domain (`example.fr`)

6. **Address Non-String i18n Concerns**
   - Date/time formatting with timezone awareness
   - Number and currency formatting
   - Sorting and collation (locale-aware `Intl.Collator`)
   - Text direction (LTR/RTL support)
   - Pluralization rules (different languages have 1, 2, 3, or 6 plural forms)
   - Gender-dependent text
   - Concatenation avoidance (use parameterized messages instead)
   - Image and media localization
   - Legal and regulatory text per region

7. **CRITICAL: Validate Architecture Decisions**
   - Verify the chosen framework handles all target languages' plural rules
   - Test that lazy loading works with SSR/SSG if applicable
   - Confirm the extraction pipeline catches all string patterns used in the codebase
   - Validate that the fallback chain produces correct results (not partial translations)
   - Check that locale switching doesn't cause full page reloads or state loss

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag log messages, debug strings, or developer-facing console output as needing i18n
- Recommend extracting brand names, product names, or proper nouns into translation files
- Suggest i18n for code identifiers, API field names, or internal constants
- Flag strings in test files or fixtures as hardcoded i18n violations
- Assume every string concatenation is an i18n problem (some are internal-only)
- Recommend a framework without checking compatibility with the existing tech stack

✅ **DO:**
- Distinguish user-facing strings from developer-facing strings before flagging
- Verify that flagged hardcoded strings actually appear in UI or user communications
- Check if "hardcoded" strings are actually coming from a CMS or database (already externalized)
- Confirm that recommended frameworks support the project's build system and SSR requirements
- Test the extraction tool against the project's actual code patterns (JSX, templates, string literals)
- Consider whether strings in error boundaries or fallback UIs also need i18n

**Expected Output:** A comprehensive i18n architecture document including:
- Framework recommendation with rationale
- String management strategy (naming, file structure, extraction)
- Locale detection and switching design
- Migration plan for existing hardcoded strings
- CI/CD integration for i18n enforcement
- Risk assessment and timeline estimate

**Example Output:**

```markdown
## i18n Architecture Strategy Report

### Project Context
- **Application**: SaaS Dashboard (React + Next.js)
- **Current State**: English-only, ~2,400 user-facing strings (estimated)
- **Target Languages**: English, Spanish, French, German, Japanese, Arabic
- **Timeline**: Phase 1 (EN/ES/FR) — 6 weeks, Phase 2 (DE/JA/AR) — 8 weeks

---

### Framework Recommendation

**Selected: `next-intl` v3**

| Criteria | next-intl | react-intl | react-i18next |
|----------|-----------|------------|---------------|
| Next.js App Router support | Native | Partial | Plugin |
| ICU MessageFormat | Yes | Yes | Via plugin |
| TypeScript-safe keys | Yes | No | Via codegen |
| SSR/SSG support | Native | Manual | Plugin |
| Lazy loading | Built-in | Manual | Built-in |
| Bundle size | 14kb | 22kb | 40kb+ |

**Rationale**: Native Next.js App Router integration, built-in ICU support, type-safe message keys, and smallest bundle size. The project already uses Next.js 14 with App Router.

---

### String Management Architecture

#### Key Naming Convention
```
{feature}.{component}.{element}.{property}
```

Examples:
```json
{
  "auth.login.email.label": "Email address",
  "auth.login.email.placeholder": "Enter your email",
  "auth.login.email.error.required": "Email is required",
  "auth.login.email.error.invalid": "Please enter a valid email",
  "auth.login.submit": "Sign in",
  "dashboard.header.welcome": "Welcome back, {name}",
  "dashboard.stats.activeUsers": "{count, plural, one {# active user} other {# active users}}"
}
```

#### File Structure
```
messages/
├── en/
│   ├── common.json          # Shared strings (nav, footer, buttons)
│   ├── auth.json             # Authentication flows
│   ├── dashboard.json        # Dashboard features
│   ├── settings.json         # Settings pages
│   ├── billing.json          # Billing and payments
│   └── errors.json           # Error messages
├── es/
│   ├── common.json
│   ├── auth.json
│   └── ...
└── fr/
    ├── common.json
    └── ...
```

#### Lazy Loading Strategy
```typescript
// app/[locale]/layout.tsx
import { NextIntlClientProvider } from 'next-intl';
import { getMessages } from 'next-intl/server';

export default async function LocaleLayout({ children, params: { locale } }) {
  // Only loads messages for current locale and route
  const messages = await getMessages();
  return (
    <NextIntlClientProvider messages={messages}>
      {children}
    </NextIntlClientProvider>
  );
}
```

---

### Locale Detection Chain

```
1. URL path segment: /es/dashboard → Spanish
2. Cookie (NEXT_LOCALE): Stored on explicit switch
3. Accept-Language header: Browser preference
4. Default: en (English)
```

#### URL Strategy: Path-based
```
example.com/en/dashboard    → English
example.com/es/dashboard    → Spanish
example.com/fr/dashboard    → French
```

**Rationale**: Path-based is best for SEO, works with Next.js middleware, and doesn't require multiple domains or subdomains.

#### Middleware Configuration
```typescript
// middleware.ts
import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
  locales: ['en', 'es', 'fr', 'de', 'ja', 'ar'],
  defaultLocale: 'en',
  localeDetection: true,
  localePrefix: 'always'
});
```

---

### String Extraction Pipeline

#### Automated Extraction
```bash
# Extract strings from source code
npx next-intl extract 'src/**/*.{ts,tsx}' --output messages/en/

# Detect untranslated strings
npx next-intl lint --locale es --compare-to en
```

#### ESLint Configuration
```json
{
  "plugins": ["formatjs"],
  "rules": {
    "formatjs/no-literal-string-in-jsx": "error",
    "formatjs/enforce-default-message": "error",
    "formatjs/enforce-id": ["error", { "idInterpolationPattern": "[sha512:contenthash:base64:6]" }]
  }
}
```

#### CI Check (GitHub Actions)
```yaml
- name: Check for untranslated strings
  run: |
    npx next-intl lint --locale es --compare-to en --fail-on-missing
    npx next-intl lint --locale fr --compare-to en --fail-on-missing
```

---

### Migration Plan (Existing Hardcoded Strings)

| Phase | Scope | Estimated Strings | Duration |
|-------|-------|-------------------|----------|
| 1 | Shared UI (nav, footer, buttons) | ~200 | 1 week |
| 2 | Auth flows (login, signup, reset) | ~150 | 1 week |
| 3 | Dashboard and core features | ~800 | 2 weeks |
| 4 | Settings and billing | ~400 | 1 week |
| 5 | Error messages and edge cases | ~300 | 1 week |
| 6 | Email templates and notifications | ~250 | 1 week |

**Total estimated strings**: ~2,100 (lower than initial estimate after deduplication)

#### Migration Pattern
```tsx
// Before
<h1>Welcome back, {user.name}</h1>
<p>You have {count} notifications</p>

// After
import { useTranslations } from 'next-intl';

const t = useTranslations('dashboard');
<h1>{t('header.welcome', { name: user.name })}</h1>
<p>{t('notifications.count', { count })}</p>
```

---

### Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Missed hardcoded strings | Medium | Low | ESLint rule + pseudo-localization testing |
| String concatenation patterns | Medium | Medium | Code review checklist + lint rules |
| RTL layout issues (Arabic) | High | High | Dedicated RTL testing phase in Phase 2 |
| Performance (bundle size) | Low | Medium | Namespace-based lazy loading already planned |
| Translation sync drift | Medium | Medium | CI check on every PR + TMS webhook |
| Date/number formatting edge cases | Medium | Medium | Use Intl APIs exclusively, no manual formatting |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Focuses the audit on architecture, not implementation details
- ST-02 (Sequential Step-by-Step Instructions) - Ordered workflow from assessment to validation
- RT-02 (Multi-Dimensional Analysis) - Evaluates framework, file structure, detection, and enforcement dimensions
- CM-01 (Explicit Context Framing) - Requires tech stack and language target context before recommendations
- DS-06 (Prioritization Guidance) - Migration phases ordered by impact and dependency

**Related Prompts:**
- `localization_icu_message_format.md` - Deep dive on ICU MessageFormat and pluralization
- `localization_translation_management_workflow.md` - TMS integration and translation pipelines
- `localization_pseudo_localization_testing.md` - Testing i18n readiness before real translations
- `domain-software-engineering/analysis/architecture/architecture_layer_identification.md` - General architecture review

**Customization Guide:**
- **For mobile apps (iOS/Android)**: Replace framework comparison with platform-native tools (NSLocalizedString, strings.xml), adjust file structure for platform conventions
- **For monorepos**: Add section on shared translation packages and workspace-level i18n configuration
- **For server-rendered apps (non-Next.js)**: Adjust locale detection to focus on server-side header parsing and session storage
- **For microservices**: Address distributed string management, API response localization, and error message translation at service boundaries
- **For legacy jQuery/vanilla JS apps**: Focus on gettext-style extraction and runtime injection patterns
