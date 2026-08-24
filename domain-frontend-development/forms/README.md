# Forms Prompts

**Category:** Frontend Development / Forms
**Prompts:** 2

---

## Overview

Production-grade prompts for building and auditing web forms — covering layered validation strategy (schema, client, server, async) and accessible, well-timed error UX. The two prompts are designed to be used together: design the validation logic, then make its errors perceivable and operable for every user.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_forms_validation_design.md](frontend_forms_validation_design.md) | Design/audit a layered validation strategy (Zod/Yup schemas, client+server enforcement, async checks, error UX) across React Hook Form, Formik, or native forms | Intermediate |
| [frontend_forms_accessibility_ux.md](frontend_forms_accessibility_ux.md) | Audit/design accessible forms: label association, error announcement, fieldset/legend, required/invalid states, keyboard, inline validation timing | Intermediate |

## Key Concepts

- **Layered enforcement**: Client validation is UX; every integrity/security rule must also run server-side.
- **Single source of truth**: One schema (Zod/Yup) drives both runtime validation and inferred types.
- **Race-safe async**: Debounce, cancel stale requests, and block submit while async checks are pending.
- **Programmatic state**: Required/invalid must be conveyed via `required`/`aria-required`/`aria-invalid`, not color alone.
- **Announced errors**: Errors need a live region and/or focus management; visual-only errors are silent to AT users.
- **Timing**: Validate after first blur/submit, then on change once errored — not on every keystroke from empty.

## Usage Examples

### Designing Validation for a New Form
Use `frontend_forms_validation_design.md` to inventory rules, define the schema layer, map client vs server enforcement, and design async checks.

### Making a Form Accessible
Use `frontend_forms_accessibility_ux.md` to audit labels, error announcement, grouping, keyboard operability, and validation timing against WCAG.

---

## Related Prompts

- [../accessibility/frontend_accessibility_aria_patterns.md](../accessibility/frontend_accessibility_aria_patterns.md) - ARIA for custom form widgets
- [../accessibility/frontend_accessibility_screen_reader.md](../accessibility/frontend_accessibility_screen_reader.md) - Verifying error announcements with screen readers
- [../react/frontend_react_state_management.md](../react/frontend_react_state_management.md) - Where form state belongs relative to app state
- [../typescript/frontend_typescript_component_typing.md](../typescript/frontend_typescript_component_typing.md) - Typing form values and schema-inferred types
