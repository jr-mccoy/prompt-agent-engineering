# Qwik Prompts

**Category:** Frontend Development / Qwik
**Prompts:** 1

---

## Overview

Production-grade prompts for Qwik development, focused on its defining feature: resumability instead of hydration. The coverage centers on `$`-boundaries (how the optimizer splits code into lazy-loadable segments), serialization (what can safely cross a boundary and survive resume), lazy execution, and judging where resumability genuinely pays off versus adds complexity. Prompts describe the model and flag version-specific `$` APIs and config keys for verification.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_qwik_resumability.md](frontend_qwik_resumability.md) | Audit `$`-boundaries, serialization of state/handlers, eager-execution leaks, and where resumability helps vs adds tax; verify SSR/streaming and routing don't force client re-execution | Advanced |

## Usage Examples

### Diagnosing Eager Execution
Use `frontend_qwik_resumability.md` to find:
- Handlers used without a `$` wrapper, forcing eager module inclusion
- Non-serializable values (class instances, closures) captured across a boundary, breaking resume
- Eager tasks running analytics/setup on load where a lazier trigger would do
- Module-level mutable state expected (wrongly) to survive resume

## Key Concepts

- **Resumability vs hydration:** hydration re-executes component code on the client to re-attach state/listeners; resumability serializes that wiring into the HTML so the client resumes without re-running everything upfront.
- **`$`-boundaries:** the optimizer splits `$`-wrapped handlers and lazy logic into separately downloadable segments that load on interaction.
- **Serialization:** values crossing a `$`-boundary must be serializable (plain data, signals, stores) — not class instances or closures over DOM nodes.
- **Lazy execution:** avoid top-of-module side effects, eager heavy imports, and over-eager tasks that defeat laziness.
- **Where it pays off:** content-rich pages with deferred interactivity and large apps that need flat time-to-interactive; less upside for tiny apps or ones that must execute most logic on load.

---

## Related Prompts

- [../solidjs/frontend_solidjs_reactivity_patterns.md](../solidjs/frontend_solidjs_reactivity_patterns.md) - Another no-VDOM, fine-grained model for comparison
- [../react/frontend_react_server_components_streaming.md](../react/frontend_react_server_components_streaming.md) - Compare resumability with React server-first/streaming hydration
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Measure TTI / JS-execution impact
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Serializable state that survives resume
