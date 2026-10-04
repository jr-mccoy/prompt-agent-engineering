---
title: "Design Token Architecture — Primitive, Semantic, and Component Tiers, Theme Axes, Naming Grammar, and Contrast-Checked Pairs"
category: frontend-development/design-direction
description: "Design or restructure a design-token system so themes, brands, and modes can change without touching components: separate primitive, semantic, and component tiers with reference rules, fix a naming grammar, model theme axes without combinatorial explosion, validate every semantic foreground/background pair for contrast in every theme, and stress-test the architecture against the next brand or mode."
techniques:
  - ST-05
  - DP-04
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - design-tokens
  - theming
  - dark-mode
  - semantic-tokens
  - naming-conventions
  - white-label
  - design-system
  - add-dark-mode
  - rebrand-without-rewriting
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/design-direction/frontend_design_system_audit.md
  - domain-frontend-development/styling/frontend_styling_css_architecture.md
  - domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md
---

# Design Token Architecture

**Objective:** Produce a token architecture — tiers, reference rules, naming grammar, theme
model, and contrast-validated pairs — under which a new brand, colour scheme, or density
mode is a mapping change rather than a component rewrite.

**When to Use:**
- You are adding dark mode, high-contrast mode, or a second brand (white-label, sub-brand,
  acquisition) and the current tokens are named after colours (`blue-primary`).
- Token count has grown past what anyone can navigate and nobody knows which to use.
- Design and code use different names for the same decision.
- You are starting a design system and want the token layer right before components exist.
- **Not this prompt if** you need to **measure** how much of the product uses tokens today
  — use `frontend_design_system_audit.md`; if the question is how CSS is layered and how
  custom properties cascade, use
  `domain-frontend-development/styling/frontend_styling_css_architecture.md`; if the tokens
  live in a Tailwind config and you are reviewing that config, use
  `domain-frontend-development/styling/frontend_styling_tailwind_design_system.md`. If the
  visual direction itself (palette intent, type personality) is undecided, settle it first
  with `frontend_look_and_feel_hunt.md` — this prompt structures decisions, it does not
  make aesthetic ones.

## Inputs / Context

1. **Current tokens** (export or list) with resolved values, or "none yet".
2. **Theme axes required now and within 18 months**: colour scheme (light/dark/high
   contrast), brands, density, platform (web/iOS/Android).
3. **Consumers**: frameworks, native platforms, design tool, email templates — each needs a
   build output.
4. **Brand constraints**: mandated brand colours, typefaces, and any partner brand rules.
5. **Accessibility target** (normally WCAG 2.2 AA) and any internal stricter rule.
6. **Who owns tokens** in design and in code.

## Method

1. **Separate three tiers (ST-05).**
   a. *Primitive* — the raw scale: `color.teal.700`, `space.400`, `radius.200`. Values only;
      no meaning. Never referenced by product code.
   b. *Semantic* — decisions by role: `color.text.subtle`, `color.surface.raised`,
      `color.action.primary.background`, `space.inset.md`. References primitives. This is
      the tier themes remap.
   c. *Component* — `button.primary.background`. References semantic tokens. Create one
      **only** when a theme must vary that component independently of its semantic
      default; otherwise components use semantic tokens directly.
2. **Fix the naming grammar.** `{category}.{concept}.{variant?}.{state?}` for semantics,
   e.g. `color.action.danger.background.hover`. Write the allowed vocabulary for each slot
   (closed lists), so two people would name a new token the same way. Align the file format
   with the W3C Design Tokens Community Group format where your toolchain supports it.
3. **Write the must-not rules (DP-04).** Components must not reference primitives. Semantic
   names must not contain colour or size words (`text.grey` is a primitive in disguise).
   Themes must not add tokens — only remap existing semantic ones. Raw values must not
   appear in component code.
4. **Model theme axes as orthogonal (CM-02).** Each axis remaps only the semantic tokens it
   owns: colour scheme and brand remap colour; density remaps spacing and size. Resolved
   sets = product of axis sizes; keep each axis's mapping file independent so 2 brands × 3
   schemes is 5 mapping files, not 6 hand-built themes.
5. **Validate every semantic pair in every theme.** List the foreground/background
   pairings the system intends (text on surface, text on action, icon on surface, focus ring
   on surface, border of inputs on surface) and compute contrast per resolved theme: text
   ≥4.5:1 (≥3:1 for large text, WCAG 1.4.3); non-text UI components and focus indicators
   ≥3:1 against adjacent colours (1.4.11).
6. **Stress-test the architecture (QA-02).** Simulate: add a third brand; add high-contrast
   mode; change the primary hue. Count the files and tokens each change touches. If any
   requires editing a component, the tiers leak.
7. **Plan migration.** Old-name → new-name map, deprecation aliases with a removal date, a
   codemod for mechanical renames, and a lint rule enforcing the must-nots.

## Output Format

```
# Token architecture — [system]   Axes: [..]   Target: WCAG [..]

## Tiers and reference rules
| Tier | Example | References | Who may consume |
## Naming grammar
{slot}.{slot}... — closed vocabulary per slot
## Must-not rules (enforced by: lint rule / review / build check)
## Token counts
| Tier | Count | Notes |
## Theme model
| Axis | Values | Semantic tokens it remaps | Mapping files |
## Contrast matrix (per resolved theme)
| Pair | Theme | Fg | Bg | Ratio | Requirement | Pass |
## Stress tests
| Change | Files touched | Tokens touched | Components touched (must be 0) |
## Migration
old → new map · alias period · codemod · lint
```

## Verification

- [ ] No component-tier token exists without a theme that overrides it.
- [ ] Every semantic name passes the grammar and contains no colour or size words.
- [ ] Each theme axis remaps only its own tokens; mapping file count is the sum, not the product.
- [ ] Every intended pair is listed with a computed ratio for every resolved theme.
- [ ] Each stress test reports zero components touched, or names the leak.
- [ ] Migration has aliases with a removal date and an enforcing lint rule.

## False-Positive Prevention

1. **Three tiers by default.** Component tokens for every property multiply count and
   maintenance; most systems need a few dozen at most.
2. **Semantic in name only.** `color.brand.blue` is still a primitive; a rebrand breaks it.
3. **Passing contrast in the light theme only.** Dark and partner themes fail most often;
   check each resolved theme.
4. **Contrast computed on primitives, not pairs.** A colour is not accessible on its own;
   only a foreground/background pair has a ratio.
5. **Tokens for every one-off.** A value used once is not a decision; leave it local or
   question the design.
6. **Theme as a copy.** Duplicating the whole semantic set per theme silently diverges;
   remap only what the axis owns.
7. **Aesthetic decisions smuggled in.** This prompt structures palette decisions; it does
   not pick brand colours.

## Example Output

```
# Token architecture — "Ledger" (fintech, white-label)   Axes: scheme × brand   Target: WCAG 2.2 AA

Current state: 410 flat tokens (`blue-primary`, `grey-text-2`); dark mode and a partner
brand (teal) requested for Q1.

## Tiers and reference rules
| Primitive | color.teal.700 = #0f766e | — | token build only |
| Semantic  | color.action.primary.background → color.blue.600 | primitives | components, product code |
| Component | button.primary.background → color.action.primary.background | semantic | that component |

## Naming grammar
color.{text|surface|border|icon|action|status}.{role}.{variant?}.{state?}
role ∈ {default, subtle, inverse, primary, danger, success, warning}; state ∈ {hover, active, disabled}

## Must-not rules
Components → primitives: lint error. Raw hex in .tsx/.css: lint error. Themes adding keys: build fails.

## Token counts
Primitive 132 (9 hues × 11 steps = 99, space 12, radius 6, type 15) · Semantic 86 · Component 24
(down from 410; 24 component tokens exist only because the partner theme restyles buttons and tabs)

## Theme model
| Scheme | light, dark | 54 colour semantics | 2 files |
| Brand  | ledger, partner | 9 action/brand semantics | 2 files |
4 resolved themes from 4 mapping files.

## Contrast matrix (excerpt)
| text.subtle on surface.default | light | #4b5563 | #ffffff | 7.56 | 4.5 | ✓ |
| text.subtle on surface.default | dark  | #6b7280 | #111827 | 3.67 | 4.5 | ✗ → remap to grey.400 #9ca3af = 6.99 ✓ |
| text.inverse on action.primary.bg | partner light | #ffffff | #14b8a6 | 2.49 | 4.5 | ✗ → teal.700 #0f766e = 5.47 ✓ |
| text.inverse on action.primary.bg | ledger light | #ffffff | #2563eb | 5.17 | 4.5 | ✓ |

## Stress tests
| Third brand (purple) | 1 new brand file | 9 | 0 ✓ |
| High-contrast scheme | 1 new scheme file | 54 | 0 ✓ |
| Primary hue blue → indigo | 1 brand file | 3 | 0 ✓ |

## Migration
410 old names mapped (318 → semantic, 61 → primitive-only, 31 retired as one-offs);
aliases until v5.0 (removal 2027-03-31); codemod for renames; stylelint + ESLint rules
for the must-nots.
```

## Techniques Used

- **ST-05 Hierarchical Organization** — primitive → semantic → component tiers with one-directional references.
- **DP-04 Must-Not Constraints** — explicit forbidden references, enforced by lint and build.
- **QA-02 Adversarial Stress-Test** — simulated new brand, new mode and hue change must touch zero components.
- **CM-02 Constraint Specification** — each theme axis constrained to remap only the tokens it owns.

## Related Prompts

- `frontend_design_system_audit.md` — measure how much of the product actually uses the tokens.
- `domain-frontend-development/styling/frontend_styling_css_architecture.md` — how custom properties and cascade layers carry the tokens in CSS.
- `domain-frontend-development/accessibility/frontend_accessibility_wcag_audit.md` — conformance testing of the shipped UI after the theme work.
