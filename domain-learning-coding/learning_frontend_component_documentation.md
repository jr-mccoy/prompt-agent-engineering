---
title: "Frontend Component Documentation Generator — Props, Usage, A11y, and Anti-Patterns from Real Code"
category: "learning-coding"
description: "Generate accurate documentation for UI components — props API, usage examples, accessibility behavior, and anti-patterns — derived from the actual component source, so developers can use and extend the component library correctly."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - component-documentation
  - frontend
  - design-system
  - accessibility
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_backend_api_documentation.md
  - domain-learning-coding/learning_frontend_code_analysis.md
  - domain-frontend-development/accessibility/frontend_accessibility_aria_patterns.md
  - domain-learning-coding/learning_code_style_readability_analysis.md
---

# Frontend Component Documentation Generator

**Objective:** Generate accurate documentation for UI components — props API, usage examples, accessibility behavior, and anti-patterns — derived from the actual component source, so developers can use and extend the component library correctly.

**When to use:**
- Documenting a component library or design system.
- Onboarding frontend developers to existing components.
- Producing first-draft Storybook docs or an API reference.
- Teaching how a component is meant to be used by walking its real props.

**When NOT to use:**
- Designing a new component API from scratch.
- Auditing component code quality — use `learning_frontend_code_analysis.md`.
- When you have no component source and would invent the props API.

**Audience:** Design-system teams, frontend developers, technical writers, and learners.

---

## Inputs / Context

The user supplies:
1. **The component source** — component definition, prop types/interface, and (if relevant) story files, pasted wrapped in a named tag, e.g. `<component>...</component>`, or a reference (framework + file paths).
2. **Framework** (React, Vue, Angular, Web Components).
3. **Audience** (library consumers, contributors) to calibrate depth.
4. **Design tokens / style system** if relevant.
5. **Optional:** existing usage examples or accessibility requirements.

Reference the source by its tag name (e.g. "the `variant` prop in `<component>`") when documenting.

---

## Constraints

### Must
- Document only props, events, slots, and refs that exist in `<component>`; derive types and defaults from the actual interface/prop definitions.
- Mark required vs optional exactly as the source declares.
- Provide working usage examples consistent with the documented API.
- Document accessibility behavior the component actually implements; if a11y handling isn't present, note it as a gap rather than claiming compliance.
- Include realistic anti-patterns (do/don't) relevant to the component.

### Must Not
- Invent props, events, default values, or accessibility features not in the source.
- Claim keyboard/ARIA support the component doesn't implement.
- Provide examples that use props that don't exist.
- Document a "version changelog" with versions you don't have.

---

## Instructions

1. **Read the component.** From `<component>`, extract the props (name, type, default, required), events/callbacks, slots/children, and any exposed refs. Flag anything ambiguous.
2. **Write the props API.** Tabulate props with types/defaults/required exactly as declared.
3. **Write usage examples.** Basic usage, common variations, and at least one edge/state example — all using real props.
4. **Document accessibility.** Keyboard interactions, ARIA roles/attributes, and focus behavior the component actually implements; flag gaps explicitly.
5. **Document anti-patterns.** 2–3 do/don't pairs grounded in how the component is meant to be used.
6. **Add integration notes.** Composition, form handling, loading/error states — only as supported.
7. **Self-check (verification).** Does every prop/event/example trace to the source? Are a11y claims true? Are gaps marked rather than glossed?

---

## False-Positive Prevention

❌ **DON'T:**
- Document a prop, event, or default the source doesn't define.
- Claim "fully accessible" or specific ARIA support the component doesn't implement.
- Write examples using non-existent props.
- Assume a default value — read it from the source.
- Invent version history or breaking-change notes.

✅ **DO:**
- Derive every documented detail from the component source.
- Mark required/optional and defaults exactly as declared.
- State the a11y behavior the code actually has, and flag gaps.
- Keep examples consistent with the real API.
- Note where information (e.g., versions) isn't available.

---

## Output Format

```
# [Component] Component

## Overview
[purpose + import]

## Props API
| Prop | Type | Default | Required | Description |

## Usage Examples
### Basic / Variations / States
[code using real props]

## Accessibility
### Keyboard / ARIA / Focus
[what the component implements; gaps flagged]

## Anti-Patterns
### Don't / Do

## Integration Notes
```

---

## Example Output

```markdown
# Button Component

## Overview
A versatile, accessible interactive element for triggering actions.

**Import:** `import { Button } from '@acme/components';`

## Props API
| Prop | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| `variant` | `'primary' \| 'secondary' \| 'danger'` | `'primary'` | No | Visual style |
| `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | No | Button size |
| `disabled` | `boolean` | `false` | No | Disables interaction |
| `loading` | `boolean` | `false` | No | Shows loading spinner |
| `onClick` | `(e: MouseEvent) => void` | — | No | Click handler |
| `children` | `ReactNode` | — | Yes | Button label |

*(All entries derived from the `ButtonProps` interface in `<component>`.)*

## Usage Examples

### Basic
```tsx
<Button onClick={() => console.log('clicked')}>Click Me</Button>
```

### Loading state
```tsx
<Button loading={isLoading} disabled={isLoading}>
  {isLoading ? 'Saving...' : 'Save'}
</Button>
```

## Accessibility

### Keyboard
- `Enter` / `Space`: activates the button (renders a native `<button>`, so this is built in).
- `Tab`: moves focus to/from the button.

### Gaps to address
- The component does **not** set `aria-label` automatically; icon-only usage must pass one. *(Flagged: no fallback label logic found in source.)*

## Anti-Patterns

### Don't: two competing primary actions
```tsx
<Button variant="primary">Save</Button>
<Button variant="primary">Cancel</Button>
```
### Do: clear hierarchy
```tsx
<Button variant="primary">Save</Button>
<Button variant="secondary">Cancel</Button>
```

## Integration Notes
- For form submission, pass `type="submit"` (forwarded to the native button).
- Disable during async submission via `disabled={isSubmitting}`.

*(Version/changelog not available from the supplied source.)*
```

---

## Verification

- [ ] Every documented prop/event/slot/ref exists in the component source.
- [ ] Types, defaults, and required flags match the source declarations.
- [ ] All examples use only real props.
- [ ] Accessibility claims reflect what the component actually implements; gaps are flagged.
- [ ] No invented props, defaults, a11y features, or version history.
- [ ] Anti-patterns are realistic and relevant.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as accurate, source-derived component docs.
- **ST-02 (Structured Sequential Instructions):** Read → props API → examples → a11y → anti-patterns → integration → verify.
- **ST-03 (Output Format Specification):** Fenced template fixes the doc structure.
- **RT-05 (Evidence-Based Reasoning):** Requires every documented detail to trace to the source.
- **QA-01 (Self-Verification):** Final pass checks every claim against the component code.

---

## Related Prompts

- `domain-learning-coding/learning_backend_api_documentation.md` — Document the backend APIs the components consume.
- `domain-learning-coding/learning_frontend_code_analysis.md` — Analyze component quality before documenting.
- `domain-frontend-development/accessibility/frontend_accessibility_aria_patterns.md` — Verify and improve ARIA patterns.
- `domain-learning-coding/learning_code_style_readability_analysis.md` — Keep component code consistent and readable.
