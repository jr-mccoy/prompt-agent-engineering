---
title: "RTL Language Support Patterns"
category: domain-software-engineering/localization
description: "Audit and implement right-to-left (RTL) language support including layout mirroring, bidirectional text handling, and CSS logical properties"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - DS-06
difficulty: advanced
tags:
  - rtl
  - right-to-left
  - bidirectional
  - arabic
  - hebrew
  - css-logical-properties
  - layout-mirroring
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/localization/localization_i18n_architecture_strategy.md
  - domain-software-engineering/localization/localization_cultural_adaptation.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# RTL Language Support Patterns

**Objective:** Audit or implement right-to-left (RTL) language support in a codebase, covering layout mirroring, bidirectional text handling, CSS logical properties, component adaptation, and testing strategies for languages like Arabic, Hebrew, Persian, and Urdu.

**When to Use:**
- Adding Arabic, Hebrew, Persian, or Urdu language support
- Auditing existing RTL implementation for correctness
- Migrating from physical CSS properties to logical properties
- Fixing layout bugs in RTL mode
- Don't use when: Your app will never support RTL languages (but consider future-proofing)

**Instructions:**

1. **Assess RTL Readiness**
   - Check if the HTML `dir` attribute is set dynamically based on locale
   - Verify `<html lang="ar" dir="rtl">` is applied at the document level
   - Inventory all CSS that uses physical properties (`left`, `right`, `margin-left`, `padding-right`)
   - Identify hardcoded directional icons (arrows, chevrons, progress indicators)
   - Check for hardcoded text alignment (`text-align: left`)
   - Review media (images with directional content, charts with LTR axis assumptions)

2. **Implement CSS Logical Properties**
   - Replace physical properties with logical equivalents:
     - `margin-left` → `margin-inline-start`
     - `margin-right` → `margin-inline-end`
     - `padding-left` → `padding-inline-start`
     - `padding-right` → `padding-inline-end`
     - `left` → `inset-inline-start`
     - `right` → `inset-inline-end`
     - `text-align: left` → `text-align: start`
     - `text-align: right` → `text-align: end`
     - `float: left` → `float: inline-start`
     - `border-left` → `border-inline-start`
     - `width` / `height` → `inline-size` / `block-size` (where appropriate)
   - Handle shorthand properties:
     - `margin: 0 16px 0 8px` → `margin-inline: 8px 16px; margin-block: 0;`
     - `padding: 8px 16px 8px 24px` → use individual logical properties
   - Update Flexbox and Grid:
     - Flexbox automatically mirrors with `dir="rtl"` — verify this works
     - Avoid `flex-direction: row-reverse` as an RTL hack (use `dir` instead)

3. **Handle Bidirectional (Bidi) Text**
   - Implement Unicode Bidi Algorithm awareness:
     - Use `<bdi>` element for user-generated content with unknown direction
     - Use `unicode-bidi: isolate` for inline elements mixing directions
     - Use `dir="auto"` for content where direction is unknown
   - Handle mixed-direction content:
     - Embedded LTR content in RTL context (English brand names, URLs, code snippets)
     - Numbers and punctuation in RTL text
     - Email addresses and phone numbers
   - Avoid string concatenation that breaks bidi ordering

4. **Adapt UI Components**
   - **Navigation**: Menus, breadcrumbs, and tabs should flow RTL
   - **Forms**: Labels and inputs should align to the right; error messages follow input direction
   - **Tables**: Column order mirrors; numeric data may stay LTR
   - **Icons**: Mirror directional icons (arrows, back/forward, progress bars)
     - Do NOT mirror: Clocks, checkmarks, play/pause, media controls, brand logos
   - **Scrollbars**: Verify scrollbar position moves to the left in RTL
   - **Modals/Drawers**: Side drawers should open from the right in RTL
   - **Carousels/Sliders**: Swipe direction and navigation arrows mirror
   - **Charts/Graphs**: X-axis may need to run right-to-left; evaluate per chart type

5. **Handle Typography and Font Considerations**
   - Select fonts with proper Arabic/Hebrew glyph support
   - Adjust line-height (Arabic text often requires more vertical space)
   - Handle font fallback chains: `font-family: 'Noto Sans Arabic', 'Arial', sans-serif`
   - Consider letter-spacing (Arabic is cursive — `letter-spacing` breaks ligatures)
   - Adjust font-size if needed (Arabic text may appear smaller at the same font size)
   - Test kashida (Arabic text justification) vs. word-spacing justification

6. **Implement Direction Switching**
   - Set `dir` attribute on `<html>` element based on current locale
   - Conditionally load RTL-specific CSS (or use logical properties to avoid this)
   - Handle CSS-in-JS direction-aware styling:
     ```javascript
     // Example: styled-components with RTL support
     const isRTL = locale === 'ar' || locale === 'he';
     ```
   - If using a CSS framework (Tailwind, Bootstrap), enable its RTL mode:
     - Tailwind: `rtl:` variant or `@tailwindcss/rtl` plugin
     - Bootstrap 5: Built-in RTL support via `dir="rtl"` and RTL CSS bundle

7. **CRITICAL: Test RTL Implementation Thoroughly**
   - Enable pseudo-RTL mode for testing without actual translations
   - Test all pages in RTL mode, not just the homepage
   - Verify all interactive flows work in RTL (forms, checkout, wizards)
   - Test with actual Arabic/Hebrew text, not just mirrored English
   - Check for overlapping or clipped text with longer Arabic translations
   - Verify that LTR content embedded in RTL context renders correctly
   - Test on actual RTL OS settings (not just `dir` attribute override)

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag universally directional icons as needing mirroring (play button, checkmarks, plus/minus)
- Report number formatting as an RTL issue (Arabic-Indic numerals are a separate localization concern)
- Assume all `left`/`right` CSS must be converted (absolute positioning for overlays may be intentional)
- Flag `text-align: center` as an RTL issue (center is direction-neutral)
- Report `flex-direction: row` as needing change (Flexbox handles RTL automatically with `dir`)
- Assume charts and data visualizations must mirror their axes

✅ **DO:**
- Verify that flagged icons are actually directional before recommending mirroring
- Test with real RTL text to confirm layout issues (not just visual inspection)
- Check if `left`/`right` positioning is for overlays, tooltips, or animations that should remain fixed
- Confirm the CSS framework's built-in RTL support before recommending manual overrides
- Test interactive components (drag-and-drop, sliders) with both mouse and keyboard in RTL
- Verify that third-party components and libraries support RTL before recommending integration

**Expected Output:** An RTL support audit or implementation plan including:
- Readiness assessment with specific files and components needing changes
- CSS migration checklist (physical → logical properties)
- Component adaptation requirements
- Testing strategy and checklist
- Prioritized implementation plan

**Example Output:**

```markdown
## RTL Support Audit Report

### Application: E-commerce Dashboard (React + Tailwind CSS)
### Target RTL Languages: Arabic (ar), Hebrew (he)

---

### RTL Readiness Score: 3/10

| Category | Score | Issues Found |
|----------|-------|-------------|
| HTML direction setup | 2/10 | No dynamic `dir` attribute |
| CSS logical properties | 1/10 | 95% physical properties used |
| Bidirectional text | 4/10 | No `<bdi>` usage, concatenation issues |
| Component adaptation | 3/10 | Navigation and forms not RTL-aware |
| Typography | 5/10 | System fonts have Arabic support |
| Testing | 0/10 | No RTL tests exist |

---

### Critical Issues

#### 1. No Dynamic Direction Attribute (HIGH)
**File**: `src/app/layout.tsx:12`
```tsx
// Current — hardcoded LTR
<html lang="en">

// Required — dynamic direction
<html lang={locale} dir={isRTL(locale) ? 'rtl' : 'ltr'}>
```

#### 2. Pervasive Physical CSS Properties (HIGH)
**Scope**: 847 instances across 134 files

**Top offenders:**
| Property | Count | Replacement |
|----------|-------|-------------|
| `margin-left` | 189 | `margin-inline-start` |
| `margin-right` | 156 | `margin-inline-end` |
| `padding-left` | 143 | `padding-inline-start` |
| `padding-right` | 128 | `padding-inline-end` |
| `text-align: left` | 94 | `text-align: start` |
| `left:` (positioning) | 78 | `inset-inline-start` |
| `right:` (positioning) | 59 | `inset-inline-end` |

**Migration approach using Tailwind:**
```html
<!-- Before -->
<div class="ml-4 pl-2 text-left border-l-2">

<!-- After (Tailwind v3.3+ with logical properties) -->
<div class="ms-4 ps-2 text-start border-s-2">
```

#### 3. Directional Icons Not Mirrored (MEDIUM)
**Files**: `src/components/icons/`

| Icon | Mirror? | Reason |
|------|---------|--------|
| `ChevronRight` (next page) | Yes | Navigation direction |
| `ArrowLeft` (back) | Yes | Navigation direction |
| `ArrowRight` (forward) | Yes | Navigation direction |
| `ProgressBar` | Yes | Shows direction of progress |
| `Checkmark` | No | Universal symbol |
| `PlayButton` | No | Universal media convention |
| `Clock` | No | Universal representation |
| `ExternalLink` | No | Convention independent of direction |

**Implementation:**
```tsx
// RTL-aware icon component
function DirectionalIcon({ icon: Icon, ...props }) {
  const { dir } = useLocale();
  return (
    <Icon
      {...props}
      className={cn(props.className, dir === 'rtl' && 'scale-x-[-1]')}
    />
  );
}
```

#### 4. Sidebar Drawer Opens From Wrong Side (MEDIUM)
**File**: `src/components/Sidebar.tsx:45`
```tsx
// Current — always slides from left
<Drawer anchor="left" open={isOpen}>

// Required — direction-aware
<Drawer anchor={isRTL ? 'right' : 'left'} open={isOpen}>
```

---

### Bidirectional Text Issues

#### String Concatenation Breaking Bidi (HIGH)
**File**: `src/utils/formatters.ts:23`
```typescript
// ❌ Breaks in RTL — parenthetical appears in wrong position
const label = userName + ' (' + role + ')';

// ✅ Use template with bidi isolation
const label = t('user.nameWithRole', { name: userName, role });
// Message: "{name} ({role})" — formatter handles bidi correctly
```

#### User-Generated Content Without Isolation (MEDIUM)
**File**: `src/components/CommentList.tsx:67`
```tsx
// ❌ User comment may contain mixed LTR/RTL text
<span>{comment.author}: {comment.text}</span>

// ✅ Isolate user-generated content
<span>{comment.author}: <bdi>{comment.text}</bdi></span>
```

---

### Implementation Plan

| Phase | Scope | Effort | Priority |
|-------|-------|--------|----------|
| 1 | Add `dir` attribute and locale detection | 2 days | P0 |
| 2 | Enable Tailwind RTL plugin, migrate utilities | 1 week | P0 |
| 3 | Migrate custom CSS to logical properties | 1 week | P0 |
| 4 | Fix directional icons | 2 days | P1 |
| 5 | Adapt sidebar, modals, drawers | 3 days | P1 |
| 6 | Add bidi isolation for user content | 2 days | P1 |
| 7 | Typography and font optimization | 2 days | P2 |
| 8 | Automated RTL testing setup | 3 days | P2 |
| 9 | Manual testing with native speakers | 1 week | P2 |

### RTL Testing Checklist

- [ ] HTML `dir="rtl"` applied and text flows right-to-left
- [ ] Navigation bar items are mirrored
- [ ] Sidebar opens from the right
- [ ] Form labels align right, inputs flow correctly
- [ ] Breadcrumbs read right-to-left with correct separator direction
- [ ] Back/forward arrows are mirrored
- [ ] Progress indicators flow right-to-left
- [ ] Tables mirror column order
- [ ] Scrollbars appear on the left
- [ ] Modal close buttons are in the top-left (mirrored from top-right)
- [ ] No text overflow or clipping with Arabic text (typically 30% longer)
- [ ] Mixed LTR/RTL content renders correctly (brand names, URLs, code)
- [ ] Number input fields accept both Western and Arabic-Indic numerals
- [ ] Keyboard shortcuts that use arrow keys are mirrored
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Focuses on RTL support as a distinct concern from general i18n
- ST-02 (Sequential Step-by-Step Instructions) - Ordered from assessment through implementation to testing
- RT-02 (Multi-Dimensional Analysis) - Covers CSS, HTML, components, typography, and bidi text
- QA-01 (Chain-of-Verification) - RTL testing checklist validates each concern independently
- DS-06 (Prioritization Guidance) - Implementation phases ordered by blocking dependencies

**Related Prompts:**
- `localization_i18n_architecture_strategy.md` - Overall i18n architecture design
- `localization_cultural_adaptation.md` - Cultural considerations beyond text direction
- `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md` - Accessibility overlaps with RTL

**Customization Guide:**
- **For mobile apps (iOS/Android)**: Focus on platform-specific RTL APIs (`UISemanticContentAttribute` on iOS, `layoutDirection` on Android) and auto-mirroring in SwiftUI/Jetpack Compose
- **For Tailwind CSS projects**: Focus on the `rtl:` variant and logical property utilities (`ms-`, `me-`, `ps-`, `pe-`)
- **For CSS-in-JS (styled-components, Emotion)**: Recommend `stylis-plugin-rtl` or direction-aware theme tokens
- **For legacy Bootstrap 4 projects**: Provide RTLCSS post-processing configuration since Bootstrap 4 lacks native RTL
- **For design systems**: Add guidance on creating direction-agnostic component APIs and token naming
