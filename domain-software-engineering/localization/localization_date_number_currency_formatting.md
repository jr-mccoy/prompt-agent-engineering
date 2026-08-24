---
title: "Date, Number, and Currency Formatting Across Locales"
category: domain-software-engineering/localization
description: "Implement locale-aware formatting for dates, times, numbers, currencies, and units using Intl APIs and i18n best practices"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - CM-02
difficulty: intermediate
tags:
  - date-formatting
  - number-formatting
  - currency
  - intl-api
  - locale-aware
  - timezone
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/localization/localization_i18n_architecture_strategy.md
  - domain-software-engineering/localization/localization_icu_message_format.md
---

# Date, Number, and Currency Formatting Across Locales

**Objective:** Implement or audit locale-aware formatting for dates, times, numbers, currencies, and measurement units using the `Intl` APIs and i18n best practices, ensuring correct display across all supported locales.

**When to Use:**
- Implementing date/time display for a multi-locale application
- Auditing existing formatting code for locale correctness
- Replacing manual formatting (regex, string slicing) with locale-aware APIs
- Adding currency display for international e-commerce
- Don't use when: You need calendar/scheduling logic (that's a date library concern, not i18n)

**Instructions:**

1. **Audit Current Formatting Patterns**
   - Search for manual date formatting:
     - Template literals: `` `${month}/${day}/${year}` ``
     - String methods: `.toLocaleDateString()` without locale argument
     - Library formatting with hardcoded patterns: `moment.format('MM/DD/YYYY')`
   - Search for manual number formatting:
     - `toFixed()` without locale-aware decimal separator
     - Manual comma insertion for thousands separators
     - Hardcoded currency symbols (`$`, `€`, `£`)
   - Identify timezone handling:
     - Are dates stored as UTC and converted for display?
     - Is the user's timezone detected or configurable?
     - Are relative times ("2 hours ago") locale-aware?

2. **Implement Date and Time Formatting**
   - Use `Intl.DateTimeFormat` as the primary API:
     ```javascript
     // Basic date formatting
     new Intl.DateTimeFormat('de-DE', {
       year: 'numeric', month: 'long', day: 'numeric'
     }).format(date);
     // → "15. März 2026"

     // With time and timezone
     new Intl.DateTimeFormat('ja-JP', {
       dateStyle: 'full', timeStyle: 'short',
       timeZone: 'Asia/Tokyo'
     }).format(date);
     // → "2026年3月15日日曜日 14:30"
     ```
   - Define standard format presets for your application:
     - **Short date**: `{ dateStyle: 'short' }` — "3/15/26" (en-US), "15.03.26" (de-DE)
     - **Medium date**: `{ dateStyle: 'medium' }` — "Mar 15, 2026" (en-US)
     - **Long date**: `{ dateStyle: 'long' }` — "March 15, 2026" (en-US)
     - **Time only**: `{ timeStyle: 'short' }` — "2:30 PM" (en-US), "14:30" (de-DE)
     - **Date + time**: `{ dateStyle: 'medium', timeStyle: 'short' }`
   - Handle relative time with `Intl.RelativeTimeFormat`:
     ```javascript
     new Intl.RelativeTimeFormat('fr', { numeric: 'auto' }).format(-1, 'day');
     // → "hier" (yesterday)
     ```

3. **Implement Number Formatting**
   - Use `Intl.NumberFormat` for all numeric display:
     ```javascript
     // Basic number with locale-aware separators
     new Intl.NumberFormat('de-DE').format(1234567.89);
     // → "1.234.567,89"

     // Percentage
     new Intl.NumberFormat('en-US', { style: 'percent', maximumFractionDigits: 1 }).format(0.856);
     // → "85.6%"

     // Compact notation
     new Intl.NumberFormat('en-US', { notation: 'compact' }).format(1500000);
     // → "1.5M"
     ```
   - Key locale differences to handle:
     | Locale | Thousands | Decimal | Example |
     |--------|-----------|---------|---------|
     | en-US | `,` | `.` | 1,234.56 |
     | de-DE | `.` | `,` | 1.234,56 |
     | fr-FR | ` ` (narrow space) | `,` | 1 234,56 |
     | hi-IN | `,` (lakh system) | `.` | 12,34,567.89 |
     | ar-SA | `٬` | `٫` | ١٬٢٣٤٫٥٦ (Arabic-Indic) |

4. **Implement Currency Formatting**
   - Use `Intl.NumberFormat` with `style: 'currency'`:
     ```javascript
     // Currency with locale-specific symbol placement
     new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(1234.5);
     // → "$1,234.50"

     new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(1234.5);
     // → "1.234,50 €"

     new Intl.NumberFormat('ja-JP', { style: 'currency', currency: 'JPY' }).format(1234);
     // → "￥1,234" (no decimals — JPY has 0 minor units)
     ```
   - Important currency rules:
     - Always use ISO 4217 currency codes (USD, EUR, GBP), never hardcode symbols
     - Some currencies have no minor units (JPY, KRW) — the API handles this
     - Currency and locale are independent: a German user can view USD prices
     - Store monetary values as integers (cents) to avoid floating-point issues
   - Handle multi-currency display:
     ```javascript
     // When displaying non-local currency, use narrow symbol to save space
     new Intl.NumberFormat('en-US', {
       style: 'currency', currency: 'EUR', currencyDisplay: 'narrowSymbol'
     }).format(1234.5);
     // → "€1,234.50" (instead of "EUR 1,234.50")
     ```

5. **Implement Unit and Measurement Formatting**
   - Use `Intl.NumberFormat` with `style: 'unit'`:
     ```javascript
     new Intl.NumberFormat('en-US', { style: 'unit', unit: 'kilometer' }).format(42);
     // → "42 km"

     new Intl.NumberFormat('de-DE', { style: 'unit', unit: 'liter', unitDisplay: 'long' }).format(3.5);
     // → "3,5 Liter"
     ```
   - Handle metric vs. imperial units based on locale preference
   - Consider `Intl.DisplayNames` for locale-aware display of:
     - Language names: `new Intl.DisplayNames(['fr'], { type: 'language' }).of('en')` → "anglais"
     - Region names: `new Intl.DisplayNames(['de'], { type: 'region' }).of('US')` → "Vereinigte Staaten"
     - Currency names: `new Intl.DisplayNames(['ja'], { type: 'currency' }).of('USD')` → "米ドル"

6. **Handle Timezone and Calendar Considerations**
   - Always store dates in UTC; convert to user timezone for display
   - Use IANA timezone identifiers (`America/New_York`, not `EST`)
   - Support non-Gregorian calendars where needed:
     ```javascript
     new Intl.DateTimeFormat('ar-SA-u-ca-islamic', { dateStyle: 'full' }).format(date);
     // → Islamic calendar date
     ```
   - Handle timezone-ambiguous inputs (user entering dates in forms)
   - Display timezone offset when showing times across regions

7. **CRITICAL: Validate Formatting Outputs**
   - Test all formatters with extreme values (0, negative, very large numbers, very small decimals)
   - Verify currency formatting for all supported currency/locale combinations
   - Test date formatting across DST boundaries
   - Confirm that `Intl` API polyfills are loaded for older browser targets if needed
   - Test with Arabic-Indic numerals if supporting Arabic locales

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag `toFixed()` used for internal calculations (not display) as a formatting issue
- Report date formatting in log files or analytics events as needing localization (machine-readable formats like ISO 8601 are correct)
- Assume all numbers need locale-aware formatting (IDs, version numbers, port numbers are not localized)
- Flag currency symbols in database seeds or test fixtures
- Report `Intl.DateTimeFormat` without explicit locale as broken (it uses the runtime default, which may be intentional)
- Assume Arabic locales always want Arabic-Indic numerals (many prefer Western Arabic numerals)

✅ **DO:**
- Verify flagged formatting is actually user-facing before recommending changes
- Check if the application already has a formatting utility layer wrapping `Intl` APIs
- Confirm browser/runtime support for specific `Intl` features before recommending them
- Test currency formatting with the actual currencies the business uses, not just USD/EUR
- Verify timezone handling end-to-end: storage → API → display
- Check that form inputs accept locale-appropriate formats (comma vs. dot for decimals)

**Expected Output:** A comprehensive formatting implementation or audit including:
- Current formatting pattern inventory
- Recommended `Intl` API usage for each format type
- Utility function implementations
- Edge case handling
- Test matrix across locales

**Example Output:**

```markdown
## Locale-Aware Formatting Audit Report

### Application: SaaS Analytics Dashboard
### Supported Locales: en-US, de-DE, fr-FR, ja-JP, ar-SA

---

### Formatting Issues Found

| Issue | Severity | Location | Current | Fix |
|-------|----------|----------|---------|-----|
| Hardcoded date format | High | `src/utils/date.ts:14` | `MM/DD/YYYY` | Use `Intl.DateTimeFormat` |
| Manual comma insertion | High | `src/utils/numbers.ts:8` | `num.toLocaleString()` with no locale | Pass explicit locale |
| Hardcoded `$` symbol | High | `src/components/PriceTag.tsx:22` | `$${price}` | Use `Intl.NumberFormat` with `style: 'currency'` |
| `toFixed(2)` for display | Medium | `src/components/Stats.tsx:45` | `value.toFixed(2)` | Use `Intl.NumberFormat` |
| Relative time in English | Medium | `src/utils/time.ts:31` | Custom "X ago" function | Use `Intl.RelativeTimeFormat` |

---

### Recommended Formatting Utilities

```typescript
// src/lib/formatters.ts

import { getLocale } from './i18n';

/**
 * Format a date for display using locale-appropriate patterns.
 */
export function formatDate(
  date: Date | number,
  style: 'short' | 'medium' | 'long' | 'full' = 'medium',
  options?: { timeZone?: string }
): string {
  const locale = getLocale();
  return new Intl.DateTimeFormat(locale, {
    dateStyle: style,
    timeZone: options?.timeZone,
  }).format(date);
}

/**
 * Format a date with time.
 */
export function formatDateTime(
  date: Date | number,
  options?: { dateStyle?: 'short' | 'medium' | 'long'; timeStyle?: 'short' | 'medium'; timeZone?: string }
): string {
  const locale = getLocale();
  return new Intl.DateTimeFormat(locale, {
    dateStyle: options?.dateStyle ?? 'medium',
    timeStyle: options?.timeStyle ?? 'short',
    timeZone: options?.timeZone,
  }).format(date);
}

/**
 * Format a relative time ("2 hours ago", "in 3 days").
 */
export function formatRelativeTime(date: Date): string {
  const locale = getLocale();
  const now = Date.now();
  const diffMs = date.getTime() - now;
  const diffSec = Math.round(diffMs / 1000);
  const diffMin = Math.round(diffSec / 60);
  const diffHr = Math.round(diffMin / 60);
  const diffDay = Math.round(diffHr / 24);

  const rtf = new Intl.RelativeTimeFormat(locale, { numeric: 'auto' });

  if (Math.abs(diffSec) < 60) return rtf.format(diffSec, 'second');
  if (Math.abs(diffMin) < 60) return rtf.format(diffMin, 'minute');
  if (Math.abs(diffHr) < 24) return rtf.format(diffHr, 'hour');
  if (Math.abs(diffDay) < 30) return rtf.format(diffDay, 'day');
  if (Math.abs(diffDay) < 365) return rtf.format(Math.round(diffDay / 30), 'month');
  return rtf.format(Math.round(diffDay / 365), 'year');
}

/**
 * Format a number with locale-appropriate separators.
 */
export function formatNumber(
  value: number,
  options?: { maximumFractionDigits?: number; notation?: 'standard' | 'compact' }
): string {
  const locale = getLocale();
  return new Intl.NumberFormat(locale, {
    maximumFractionDigits: options?.maximumFractionDigits,
    notation: options?.notation,
  }).format(value);
}

/**
 * Format a percentage.
 */
export function formatPercent(
  value: number, // 0.85 = 85%
  options?: { maximumFractionDigits?: number }
): string {
  const locale = getLocale();
  return new Intl.NumberFormat(locale, {
    style: 'percent',
    maximumFractionDigits: options?.maximumFractionDigits ?? 1,
  }).format(value);
}

/**
 * Format a currency value.
 * @param amountInMinorUnits - Amount in minor units (cents for USD, yen for JPY)
 * @param currencyCode - ISO 4217 currency code
 */
export function formatCurrency(
  amountInMinorUnits: number,
  currencyCode: string,
  options?: { display?: 'symbol' | 'narrowSymbol' | 'code' | 'name' }
): string {
  const locale = getLocale();

  // Determine minor unit factor (most currencies use 2 decimal places)
  const resolvedOptions = new Intl.NumberFormat(locale, {
    style: 'currency',
    currency: currencyCode,
  }).resolvedOptions();
  const minorUnitFactor = Math.pow(10, resolvedOptions.minimumFractionDigits);

  return new Intl.NumberFormat(locale, {
    style: 'currency',
    currency: currencyCode,
    currencyDisplay: options?.display ?? 'symbol',
  }).format(amountInMinorUnits / minorUnitFactor);
}
```

### Test Matrix

| Format | en-US | de-DE | fr-FR | ja-JP | ar-SA |
|--------|-------|-------|-------|-------|-------|
| Date (medium) | Mar 15, 2026 | 15.03.2026 | 15 mars 2026 | 2026/03/15 | ١٥ مارس ٢٠٢٦ |
| Time (short) | 2:30 PM | 14:30 | 14:30 | 14:30 | ٢:٣٠ م |
| Number (1234567.89) | 1,234,567.89 | 1.234.567,89 | 1 234 567,89 | 1,234,567.89 | ١٬٢٣٤٬٥٦٧٫٨٩ |
| Percent (0.856) | 85.6% | 85,6 % | 85,6 % | 85.6% | ٨٥٫٦٪ |
| Currency ($1234.50) | $1,234.50 | 1.234,50 $ | 1 234,50 $US | $1,234.50 | ١٬٢٣٤٫٥٠ US$ |
| Relative (-1 day) | yesterday | gestern | hier | 昨日 | أمس |

### Edge Cases Handled

- **Zero-decimal currencies (JPY)**: `formatCurrency(1234, 'JPY')` → "¥1,234" (not "¥12.34")
- **Negative currency**: `formatCurrency(-500, 'USD')` → "-$5.00" (en-US), "-5,00 $" (de-DE)
- **Very large numbers**: `formatNumber(1e12)` → "1,000,000,000,000" or "1T" (compact)
- **Indian numbering (lakh/crore)**: `formatNumber(1234567, { locale: 'hi-IN' })` → "12,34,567"
- **DST boundary dates**: Formatting handles spring-forward/fall-back correctly via timezone parameter
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Scoped to formatting, not general i18n
- ST-02 (Sequential Step-by-Step Instructions) - From audit through implementation
- RT-02 (Multi-Dimensional Analysis) - Covers dates, numbers, currencies, units, and timezones
- RT-05 (Evidence-Based Reasoning) - Example outputs demonstrate correctness with real locale data
- CM-02 (Constraint Specification) - Clear rules for what should and shouldn't be localized

**Related Prompts:**
- `localization_i18n_architecture_strategy.md` - Overall i18n architecture
- `localization_icu_message_format.md` - ICU message format for embedding formatted values in messages

**Customization Guide:**
- **For e-commerce**: Emphasize currency formatting, multi-currency display, and price formatting in lists/tables
- **For analytics dashboards**: Focus on number formatting (compact notation, percentages) and date range formatting
- **For mobile apps**: Note platform-specific formatters (`NSNumberFormatter` on iOS, `NumberFormat` on Android)
- **For server-side rendering**: Address Node.js `Intl` data availability (full-icu vs. small-icu builds)
- **For financial applications**: Add precision requirements, rounding rules, and accounting notation (`(1,234.50)` for negative)
