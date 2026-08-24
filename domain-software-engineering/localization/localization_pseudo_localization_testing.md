---
title: "Pseudo-Localization Testing"
category: domain-software-engineering/localization
description: "Implement pseudo-localization testing to detect i18n issues like hardcoded strings, text truncation, and layout breakage before real translations"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - ST-03
difficulty: intermediate
tags:
  - pseudo-localization
  - testing
  - i18n-testing
  - string-expansion
  - text-overflow
  - localization-qa
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/localization/localization_i18n_architecture_strategy.md
  - domain-software-engineering/localization/localization_rtl_language_support.md
  - domain-software-engineering/testing/testing_e2e_test_scenario_creation.md
---

# Pseudo-Localization Testing

**Objective:** Implement pseudo-localization testing to detect internationalization defects — hardcoded strings, text truncation, layout breakage, encoding issues, and concatenation problems — before real translations are available.

**When to Use:**
- Before starting actual translation work (validates i18n readiness)
- As a CI gate to catch new i18n regressions on every PR
- When onboarding a codebase to i18n for the first time
- To verify that all user-facing strings flow through the i18n system
- Don't use when: Translations already exist and you need in-language QA (use real translation testing instead)

**Instructions:**

1. **Understand Pseudo-Localization Techniques**
   - **Accented characters**: Replace ASCII with accented equivalents to test encoding
     - `Hello World` → `Ħëľľö Ŵöŕľð`
   - **String expansion**: Add padding to simulate longer translations (German is ~30% longer, Finnish ~40%)
     - `Submit` → `[Ṣüƀṁïẗ ẗëxẗ ƥàð]` (with ~40% extra length)
   - **Brackets/markers**: Wrap strings in delimiters to spot un-extracted strings
     - `Save changes` → `[!! Ṣàṿë çĥàñğëṡ !!]`
   - **Mirror/RTL simulation**: Reverse characters to test layout flexibility
   - **Long string replacement**: Replace with extremely long strings to find truncation
   - **CJK simulation**: Use wide characters to test fixed-width assumptions

2. **Select Pseudo-Localization Tooling**
   - **Built-in framework support**:
     - `next-intl`: Pseudo-locale configuration
     - `react-intl` / FormatJS: `@formatjs/cli --pseudo-locale`
     - `i18next`: `i18next-pseudo` plugin
     - `Android`: Pseudolocales built into developer settings (`en-XA`, `ar-XB`)
     - `iOS`: Enable pseudo-language in Xcode scheme settings
   - **Standalone tools**:
     - `pseudo-localization` npm package
     - Custom script (see implementation below)
   - **Browser extensions**:
     - Chrome pseudo-localization extensions for quick visual testing

3. **Implement Pseudo-Locale Generation**
   - Create a pseudo-locale that transforms source strings:
     ```javascript
     // pseudo-locale generator
     function pseudoLocalize(str) {
       // 1. Replace characters with accented equivalents
       const charMap = {
         'a': 'à', 'b': 'ƀ', 'c': 'ç', 'd': 'ð', 'e': 'ë',
         'f': 'ƒ', 'g': 'ğ', 'h': 'ĥ', 'i': 'ï', 'j': 'ĵ',
         'k': 'ķ', 'l': 'ľ', 'm': 'ṁ', 'n': 'ñ', 'o': 'ö',
         'p': 'ƥ', 'q': 'ǫ', 'r': 'ŕ', 's': 'ṡ', 't': 'ẗ',
         'u': 'ü', 'v': 'ṿ', 'w': 'ŵ', 'x': 'x', 'y': 'ÿ',
         'z': 'ž',
         'A': 'À', 'B': 'Ɓ', 'C': 'Ç', 'D': 'Ð', 'E': 'Ë',
         'F': 'Ƒ', 'G': 'Ğ', 'H': 'Ĥ', 'I': 'Ï', 'J': 'Ĵ',
         'K': 'Ķ', 'L': 'Ľ', 'M': 'Ṁ', 'N': 'Ñ', 'O': 'Ö',
         'P': 'Ƥ', 'Q': 'Ǫ', 'R': 'Ŕ', 'S': 'Ṣ', 'T': 'Ṫ',
         'U': 'Ü', 'V': 'Ṿ', 'W': 'Ŵ', 'X': 'Ẍ', 'Y': 'Ÿ',
         'Z': 'Ž'
       };

       // Preserve ICU/interpolation tokens
       let result = '';
       let insideToken = false;
       let braceDepth = 0;

       for (const char of str) {
         if (char === '{') { braceDepth++; insideToken = true; }
         if (insideToken) {
           result += char;
           if (char === '}') { braceDepth--; if (braceDepth === 0) insideToken = false; }
           continue;
         }
         result += charMap[char] || char;
       }

       // 2. Add ~40% expansion padding
       const expansionLength = Math.ceil(result.length * 0.4);
       const padding = ' ẗëxẗ'.repeat(Math.ceil(expansionLength / 5)).slice(0, expansionLength);

       // 3. Wrap in brackets for visual identification
       return `[!! ${result}${padding} !!]`;
     }
     ```
   - Generate pseudo-locale files from source translations
   - Register the pseudo-locale in your i18n configuration (e.g., `qps-ploc` or `xx-pseudo`)

4. **Configure Pseudo-Locale in Your Framework**
   - **React (i18next)**:
     ```javascript
     import pseudoLocalization from 'i18next-pseudo';

     i18n.use(pseudoLocalization).init({
       // Enable pseudo-localization in development
       postProcess: process.env.NODE_ENV === 'development' ? ['pseudo'] : [],
       pseudo: {
         enabled: true,
         languageToPseudo: 'en',
       }
     });
     ```
   - **Next.js (next-intl)**: Add pseudo-locale to supported locales and generate pseudo JSON files
   - **Android**: Enable pseudo-locales in developer options:
     - `en-XA` (accented English — tests character encoding and expansion)
     - `ar-XB` (RTL pseudo-locale — tests layout mirroring)
   - **iOS**: Edit scheme → Options → App Language → Pseudolanguages

5. **Define What to Test With Pseudo-Localization**
   - **Hardcoded strings**: Any text NOT wrapped in `[!! ... !!]` brackets is un-extracted
   - **Text truncation**: Look for strings cut off by fixed-width containers
   - **Layout breakage**: Expanded text causing overlaps, wrapping, or alignment issues
   - **Encoding issues**: Accented characters appearing as `?`, `□`, or mojibake
   - **Concatenation problems**: Mixed pseudo/normal text indicates string concatenation
   - **Placeholder corruption**: `{name}` rendered as `{ñàṁë}` means tokens aren't preserved
   - **Image/icon text**: Text baked into images won't be pseudo-localized
   - **Form validation**: Length validators rejecting expanded pseudo text

6. **Automate Pseudo-Localization in CI**
   - Generate pseudo-locale files as a CI step
   - Run visual regression tests with pseudo-locale enabled
   - Screenshot critical pages in pseudo-locale for review
   - Optionally run Playwright/Cypress tests in pseudo-locale mode:
     ```javascript
     // e2e/pseudo-locale.spec.ts
     test.describe('Pseudo-localization checks', () => {
       test.beforeEach(async ({ page }) => {
         // Set pseudo-locale via cookie or URL parameter
         await page.goto('/?locale=pseudo');
       });

       test('no un-extracted strings on checkout page', async ({ page }) => {
         await page.goto('/checkout?locale=pseudo');

         // All visible text should contain pseudo markers [!! ... !!]
         const textElements = await page.locator('body *:visible').allTextContents();
         const nonPseudoStrings = textElements
           .filter(text => text.trim().length > 0)
           .filter(text => !text.includes('!!') && !/^\d+$/.test(text) && !/^[^a-zA-Z]+$/.test(text));

         // Report any un-extracted strings
         expect(nonPseudoStrings).toEqual([]);
       });

       test('no text truncation on dashboard', async ({ page }) => {
         await page.goto('/dashboard?locale=pseudo');

         // Check for text overflow
         const overflowElements = await page.evaluate(() => {
           const elements = document.querySelectorAll('*');
           const overflowing = [];
           for (const el of elements) {
             if (el.scrollWidth > el.clientWidth && el.textContent.trim()) {
               overflowing.push({
                 tag: el.tagName,
                 class: el.className,
                 text: el.textContent.slice(0, 50)
               });
             }
           }
           return overflowing;
         });

         expect(overflowElements).toEqual([]);
       });
     });
     ```

7. **CRITICAL: Interpret Results Correctly**
   - Not every un-bracketed string is a bug — check the exceptions list
   - Layout issues with 40% expansion may not occur with actual translations (check per-language expansion rates)
   - Test with both pseudo-locale AND actual translations for complete coverage
   - Compare pseudo-locale screenshots against baseline to catch regressions

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag brand names, product names, or trademarked terms as "un-extracted" strings
- Report third-party widget text (e.g., Stripe elements, Google Maps, reCAPTCHA) as i18n failures
- Flag numeric values, dates formatted by `Intl` APIs, or currency symbols as hardcoded
- Report text inside `<code>` or `<pre>` blocks as needing localization
- Assume every layout shift in pseudo-locale is a real bug (some are artifacts of extreme expansion)
- Flag aria-labels or screen-reader-only text that appears unhidden during pseudo testing

✅ **DO:**
- Maintain an allow-list of strings that should not be pseudo-localized (brand names, technical terms)
- Verify reported "hardcoded strings" are actually user-facing, not tooltips from browser defaults
- Cross-check layout issues with realistic expansion rates for target languages (not just 40% blanket expansion)
- Confirm encoding issues reproduce in production builds, not just dev server
- Test form submission flows to catch validation that rejects pseudo-locale input
- Verify that pseudo-locale testing doesn't break end-to-end test assertions

**Expected Output:** A pseudo-localization testing strategy including:
- Tooling setup and configuration
- Pseudo-locale generation script or configuration
- Test scenarios and automation code
- CI integration configuration
- Known exceptions and allow-list
- Example issue report

**Example Output:**

```markdown
## Pseudo-Localization Testing Report

### Application: Task Management App (React + i18next)
### Pseudo-Locale: `qps-ploc`

---

### Setup

**Pseudo-locale generation:**
```bash
node scripts/generate-pseudo.js --source messages/en.json --output messages/qps-ploc.json
```

**i18next configuration:**
```javascript
supportedLngs: ['en', 'es', 'fr', ..., 'qps-ploc'],
```

**Enable via URL:** `?lng=qps-ploc` or `?debug_pseudo=true`

---

### Issues Found

#### Hardcoded Strings (5 found)

| Location | Text | Type | Fix |
|----------|------|------|-----|
| `Header.tsx:34` | "Beta" | Badge label | Extract to `common.betaBadge` |
| `Footer.tsx:12` | "© 2026 Acme Inc." | Copyright | Extract to `common.copyright` with year param |
| `ErrorBoundary.tsx:8` | "Something went wrong" | Fallback UI | Extract to `errors.generic` |
| `Onboarding.tsx:45` | "Step 1 of 3" | Progress label | Extract to `onboarding.stepProgress` with params |
| `Toast.tsx:22` | "Copied!" | Toast notification | Extract to `common.copiedToClipboard` |

#### Text Truncation (3 found)

| Component | Container Width | Source Length | Pseudo Length | Fix |
|-----------|----------------|-------------|--------------|-----|
| `TaskCard` title | 200px fixed | ~20 chars | ~28 chars | Use `text-overflow: ellipsis` + tooltip |
| `Sidebar` nav items | 180px fixed | ~15 chars | ~21 chars | Allow wrapping or use `min-width` |
| `Button` "Save changes" | `fit-content` with max-width 120px | 12 chars | 17 chars | Increase max-width to 180px |

#### Layout Issues (2 found)

| Page | Issue | Screenshot | Fix |
|------|-------|-----------|-----|
| Dashboard | Stats cards overlap when labels expand | `pseudo-dashboard.png` | Use CSS Grid with `auto-fit` instead of fixed columns |
| Settings | Radio button labels wrap and misalign | `pseudo-settings.png` | Add `align-items: start` to radio group |

#### Encoding Issues (1 found)

| Location | Issue | Fix |
|----------|-------|-----|
| PDF export (`/api/export`) | Accented characters render as `?` in generated PDF | Set PDF font to one supporting Unicode (Noto Sans) |

### Exceptions List (Do Not Flag)

| String | Reason |
|--------|--------|
| "Acme" | Brand name |
| "JIRA-1234" | External system reference format |
| "API", "URL", "ID" | Technical abbreviations |
| Google Maps labels | Third-party widget |
| `<code>` block content | Code examples, not user-facing text |

### CI Configuration

```yaml
name: Pseudo-Localization Check
on: pull_request

jobs:
  pseudo-locale-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - name: Generate pseudo-locale
        run: node scripts/generate-pseudo.js
      - name: Run pseudo-locale E2E tests
        run: npx playwright test tests/pseudo-locale/
      - name: Upload screenshots
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: pseudo-locale-screenshots
          path: test-results/
```
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Focused on detecting i18n issues via pseudo-localization, not translation quality
- ST-02 (Sequential Step-by-Step Instructions) - From understanding through implementation to CI automation
- RT-02 (Multi-Dimensional Analysis) - Covers hardcoded strings, truncation, layout, encoding, and concatenation
- QA-01 (Chain-of-Verification) - Each defect type has specific detection and validation criteria
- ST-03 (Structured Output Templates) - Consistent issue reporting format

**Related Prompts:**
- `localization_i18n_architecture_strategy.md` - Ensures i18n framework is set up before testing
- `localization_rtl_language_support.md` - Pseudo-RTL is a complementary technique
- `domain-software-engineering/testing/testing_e2e_test_scenario_creation.md` - E2E test patterns for i18n

**Customization Guide:**
- **For mobile apps**: Use platform-built-in pseudo-locales (Android `en-XA`/`ar-XB`, iOS scheme pseudolanguages) instead of custom scripts
- **For design systems**: Run pseudo-localization on the component library Storybook to catch issues at the component level
- **For SSR/SSG apps**: Test that pseudo-locale works with server-rendered pages, not just client-side switching
- **For monorepos**: Generate pseudo-locales per package and test each independently
- **For legacy apps with no i18n framework**: Use pseudo-localization as the discovery tool to inventory all hardcoded strings before adding i18n
