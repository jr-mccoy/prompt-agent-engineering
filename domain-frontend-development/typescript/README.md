# TypeScript Prompts

**Category:** Frontend Development / TypeScript
**Prompts:** 2

---

## Overview

Production-grade prompts for raising type safety in frontend codebases — both at the component-API level (designing precise props, generics, variant unions, and event/ref types) and at the whole-codebase level (auditing for `any` leakage, unsafe assertions, missing strict flags, and untyped boundaries). Both prompts produce evidence-based findings and prioritized, low-risk remediation.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_typescript_component_typing.md](frontend_typescript_component_typing.md) | Design/review type-safe component contracts — props, generics, discriminated unions, event handlers, refs, children — across React/Vue/Angular | Intermediate |
| [frontend_typescript_type_safety_audit.md](frontend_typescript_type_safety_audit.md) | Audit a frontend codebase for `any` leakage, unsafe assertions, missing strict flags, unsound patterns, and untyped boundaries | Advanced |

## Usage Examples

### Designing a Component's Type API
Use `frontend_typescript_component_typing.md` when building a reusable component and you want misuse caught at compile time — e.g., expressing mutually-exclusive props as a discriminated union or making a `Select`/table generic over its value type.

### Hardening an Existing Codebase
Use `frontend_typescript_type_safety_audit.md` when "we use TypeScript" but type-shaped bugs still reach runtime — it finds `any` at boundaries, blind API-response casts, dangerous `!` assertions, and scopes a safe path to enabling `strict`.

---

## Key Concepts

| Concept | Where it applies |
|---------|------------------|
| Discriminated unions for variant APIs | Component typing |
| Generics that infer from props | Component typing |
| Precise event / ref / children types | Component typing |
| `any` leakage & blast radius | Type-safety audit |
| Boundary validation (schema/parser) | Type-safety audit |
| Incremental strict-flag adoption | Type-safety audit |

> Anti-fabrication note: these prompts avoid asserting version-specific compiler/library behavior or error counts; they recommend measuring (e.g., flipping a flag in a branch) and verifying against current TypeScript docs.

---

## Related Prompts

- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - Component patterns the types should mirror
- [../vue/frontend_vue_composition_api.md](../vue/frontend_vue_composition_api.md) - Typing `defineProps`/composables in Vue
- [../angular/frontend_angular_architecture.md](../angular/frontend_angular_architecture.md) - Typed inputs/outputs in Angular
- [../styling/frontend_styling_css_in_js_review.md](../styling/frontend_styling_css_in_js_review.md) - Typed styled/variant component APIs
