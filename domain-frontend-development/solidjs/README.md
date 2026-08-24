# SolidJS Prompts

**Category:** Frontend Development / SolidJS
**Prompts:** 1

---

## Overview

Production-grade prompts for SolidJS development, focused on its defining feature: fine-grained reactivity with no Virtual DOM. The coverage centers on the reactivity mental model — signals, stores, derivations/memos, and effects — and the common pitfalls developers hit when they carry a React "re-render on state change" model into Solid's run-once-component world. Prompts describe concepts and flag version-specific API names for verification.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_solidjs_reactivity_patterns.md](frontend_solidjs_reactivity_patterns.md) | Audit signals, stores, memos, and effects for correct fine-grained reactivity; catch destructuring breaks, derive-via-effect, missing cleanup, and store-update mistakes | Advanced |

## Usage Examples

### Diagnosing Lost or Excess Reactivity
Use `frontend_solidjs_reactivity_patterns.md` to find:
- Destructured props/signals that snapshot values and stop updating
- Signals read into a top-level variable outside any tracking scope
- Effects used to derive state that should be a memo (extra signals, loop risk)
- Stores replaced wholesale instead of path-updated, losing fine-grained reactivity
- Dynamic lists using `.map()` instead of the keyed control-flow primitive

## Key Concepts

- **No VDOM, run-once components:** component bodies execute once; reactivity lives in tracking scopes (JSX, effects, memos), not in re-running the component.
- **Don't destructure reactivity:** props and signals must stay accessed live (`props.value`, `signal()`); destructuring breaks updates.
- **Signals vs stores:** signals for primitive/atomic state; stores for nested objects/arrays where fine-grained nested reactivity matters.
- **Memos vs inline:** memoize expensive or multiply-consumed derivations; inline cheap ones — no manual dependency arrays.
- **Effects for side effects only:** subscriptions, DOM, logging — with cleanup; not for deriving state.
- **Resources for async:** loading/error/refetch integrate into the reactive graph.

---

## Related Prompts

- [../svelte/frontend_svelte_component_patterns.md](../svelte/frontend_svelte_component_patterns.md) - Compiler-based fine-grained reactivity for comparison
- [../qwik/frontend_qwik_resumability.md](../qwik/frontend_qwik_resumability.md) - Another no-VDOM, fine-grained model (with resumability)
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Choosing signals vs stores vs external state
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Performance impact of over-running effects
