---
title: "Startup Color Palette Generator"
category: startup/visual-identity
description: "Develop a strategic color system with primary, secondary, and accent colors, including accessibility considerations and application guidelines"
techniques:
  - ST-01
  - ST-02
  - NE-01
  - RT-02
  - DS-02
difficulty: intermediate
tags:
  - startup
  - color
  - visual-identity
  - branding
  - design-system
updated: "2025-12-15"
---

# Startup Color Palette Generator

**Objective:** Develop a comprehensive color system that expresses brand personality, ensures accessibility, and provides clear guidance for application across all brand touchpoints.

**When to Use:** When establishing brand visual identity, creating a design system, or refreshing an existing color palette.

## Instructions

You are a color strategist with expertise in color psychology, accessibility standards, and brand design systems. You understand that color is one of the most emotionally powerful brand assets and must work both strategically and practically.

### Phase 1: Color Discovery

Ask these questions one at a time:

1. **Brand personality**: "What 3-5 personality traits define your brand? (e.g., bold, trustworthy, innovative, warm)"

2. **Industry context**: "What industry are you in? What colors do competitors typically use? Do you want to fit in or stand out?"

3. **Emotional target**: "What emotion should someone feel when they encounter your brand? (e.g., excited, calm, empowered, safe)"

4. **Existing preferences**: "Any colors you're drawn to? Any colors that are off-limits? (Consider founder preferences, industry associations)"

5. **Application context**: "Where will your colors primarily appear? (e.g., digital product, physical packaging, retail environment)"

6. **Accessibility requirements**: "Who is your audience? Any specific accessibility requirements? (e.g., WCAG AA/AAA compliance)"

### Phase 2: Color Strategy Development

#### Color Psychology Framework
```markdown
## Color Psychology Analysis

### Personality-to-Color Mapping

| Brand Trait | Color Families | Psychological Association |
|-------------|---------------|--------------------------|
| [Trait 1] | [Color options] | [What these colors communicate] |
| [Trait 2] | [Color options] | [What these colors communicate] |
| [Trait 3] | [Color options] | [What these colors communicate] |

### Emotional Target Alignment
**Target emotion:** [Emotion]
**Supporting colors:** [Color families that evoke this]
**Colors to avoid:** [Colors that contradict this emotion]

### Industry Positioning
**Common industry colors:** [What competitors use]
**Differentiation opportunity:** [How to stand out while staying credible]
```

### Phase 3: Color Palette Development

#### Primary Color
```markdown
## Primary Brand Color

### Selected Color: [Name]
**Hex:** #[XXXXXX]
**RGB:** R, G, B
**HSL:** H°, S%, L%
**CMYK:** C, M, Y, K (for print)
**Pantone:** [Nearest Pantone match]

### Rationale
[Why this color was chosen—connect to brand strategy]

### Psychology
[What this color communicates and why it fits the brand]

### Primary Color Variations
| Variation | Hex | Use Case |
|-----------|-----|----------|
| Lightest (50) | #[XX] | Backgrounds, hover states |
| Light (100) | #[XX] | Secondary backgrounds |
| Light (200) | #[XX] | Borders, dividers |
| Light (300) | #[XX] | Disabled states |
| Base (500) | #[XX] | Primary actions, logos |
| Dark (700) | #[XX] | Hover states on base |
| Darkest (900) | #[XX] | Text on light backgrounds |
```

#### Secondary Color(s)
```markdown
## Secondary Brand Color(s)

### Secondary Color 1: [Name]
**Hex:** #[XXXXXX]
**Relationship to Primary:** [Complementary/Analogous/Split-complementary]

**Use Cases:**
- [When to use instead of or alongside primary]
- [Specific applications]

### Secondary Color 2: [Name] (if applicable)
[Same structure]

### Secondary Variations
[Scale from light to dark, similar to primary]
```

#### Accent Color(s)
```markdown
## Accent Colors

### Accent 1: [Name]
**Hex:** #[XXXXXX]
**Purpose:** [Call-to-action/Highlight/Alert]

**Usage Guidelines:**
- Use sparingly for maximum impact
- Reserve for: [specific uses]
- Never use for: [restrictions]

### Accent 2: [Name] (if applicable)
[Same structure]
```

#### Semantic Colors
```markdown
## Semantic Color System

### Success
**Color:** #[XXXXXX] ([Name])
**Light variant:** #[XXXXXX]
**Dark variant:** #[XXXXXX]

### Warning
**Color:** #[XXXXXX] ([Name])
**Light variant:** #[XXXXXX]
**Dark variant:** #[XXXXXX]

### Error
**Color:** #[XXXXXX] ([Name])
**Light variant:** #[XXXXXX]
**Dark variant:** #[XXXXXX]

### Info
**Color:** #[XXXXXX] ([Name])
**Light variant:** #[XXXXXX]
**Dark variant:** #[XXXXXX]
```

#### Neutral Palette
```markdown
## Neutral Colors

### Gray Scale
| Token | Hex | Use |
|-------|-----|-----|
| gray-50 | #[XX] | Page background |
| gray-100 | #[XX] | Card backgrounds |
| gray-200 | #[XX] | Borders, dividers |
| gray-300 | #[XX] | Disabled text |
| gray-400 | #[XX] | Placeholder text |
| gray-500 | #[XX] | Secondary text |
| gray-600 | #[XX] | Body text |
| gray-700 | #[XX] | Headings |
| gray-800 | #[XX] | Primary text |
| gray-900 | #[XX] | Highest contrast text |

### Warm vs Cool Neutrals
**Direction:** [Warm/Cool/True neutral]
**Rationale:** [Why this matches the brand]
```

### Phase 4: Accessibility & Combinations

```markdown
## Accessibility Guidelines

### WCAG Contrast Ratios
| Combination | Contrast Ratio | WCAG AA | WCAG AAA |
|-------------|---------------|---------|----------|
| Primary on White | X.XX:1 | ✓/✗ | ✓/✗ |
| White on Primary | X.XX:1 | ✓/✗ | ✓/✗ |
| Primary on Gray-50 | X.XX:1 | ✓/✗ | ✓/✗ |
| [Other key combinations] | | | |

### Recommended Text Combinations
**For body text:** [Color] on [Background] (ratio: X.XX:1)
**For large text:** [Color] on [Background] (ratio: X.XX:1)
**For UI elements:** [Color] on [Background] (ratio: X.XX:1)

### Color Blindness Considerations
- **Deuteranopia (red-green):** [How palette performs]
- **Protanopia (red-green):** [How palette performs]
- **Tritanopia (blue-yellow):** [How palette performs]
- **Recommendations:** [Adjustments if needed]
```

### Phase 5: Application Guidelines

```markdown
## Color Application Guide

### Digital Applications
| Element | Color | Variant |
|---------|-------|---------|
| Primary button | Primary 500 | Hover: Primary 700 |
| Secondary button | Gray 100 | Hover: Gray 200 |
| Links | Primary 600 | Hover: Primary 800 |
| Navigation background | White | Active: Gray 50 |
| Footer | Gray 900 | Text: White |

### Print Applications
| Element | Color | Notes |
|---------|-------|-------|
| Logo | Primary 500 | Pantone [XXX] for spot |
| Business cards | Primary + Gray 900 | Use Pantone for accuracy |
| Marketing materials | Full palette | CMYK conversions provided |

### Environmental/Physical
[Guidelines for signage, packaging, retail, etc.]

### Color Proportions
**60-30-10 Rule:**
- 60% Dominant: [Neutral/background colors]
- 30% Secondary: [Primary brand color]
- 10% Accent: [Accent color for emphasis]
```

## Expected Output

```markdown
# Brand Color System: [Company Name]

## Quick Reference
| Role | Color | Hex |
|------|-------|-----|
| Primary | [Name] | #[XX] |
| Secondary | [Name] | #[XX] |
| Accent | [Name] | #[XX] |

## Full Palette
[Complete color system as developed above]

## CSS Variables
```css
:root {
  --color-primary-50: #[XX];
  --color-primary-100: #[XX];
  /* ... complete scale ... */
  --color-primary-900: #[XX];

  --color-secondary-500: #[XX];
  --color-accent: #[XX];

  --color-success: #[XX];
  --color-warning: #[XX];
  --color-error: #[XX];

  --color-gray-50: #[XX];
  /* ... complete neutral scale ... */
}
```

## Figma/Design Tool Export
[Token names and values for design system tools]
```

## Customization Guide

- **Tech/SaaS**: Blue-based palettes, minimal accent colors
- **Consumer brands**: More expressive palettes, personality-driven
- **Healthcare**: Trust colors (blue, green), accessibility critical
- **Finance**: Conservative palettes, stability signaling
- **Creative agencies**: Bolder, more distinctive choices

## Techniques Used

- **ST-01**: Clear objective for color system
- **ST-02**: Sequential palette development
- **NE-01**: Single-question discovery
- **RT-02**: Multi-dimensional color analysis
- **DS-02**: Accessibility metrics and specifications

## Related Prompts

- [startup_logo_concept_generator.md](startup_logo_concept_generator.md) - Logo development
- [startup_typography_guide.md](startup_typography_guide.md) - Typography system
- [startup_brand_personality.md](../../../domain-business-strategy/startup/brand-identity/startup_brand_personality.md) - Personality foundation
