---
title: "SolidJS Control Flow and Component API Review — For vs Index, Show and Switch, splitProps and mergeProps, children, Context Ownership, and Boundaries"
category: frontend-development/solidjs
description: "Review a SolidJS codebase's component layer: choose the right list primitive for each list, use Show, Switch and Dynamic instead of patterns that recreate DOM, forward and default props without breaking reactivity, resolve children once, keep context and refs inside the owner that needs them, and place error and suspense boundaries where a failure should stop."
techniques:
  - DS-29
  - IT-22
  - RT-05
  - QA-24
difficulty: intermediate
tags:
  - solidjs
  - control-flow
  - splitprops
  - mergeprops
  - for-vs-index
  - component-api
  - list-rerenders-everything
  - default-props-not-working
  - input-loses-focus-while-typing
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md
  - domain-frontend-development/typescript/frontend_typescript_component_typing.md
  - domain-frontend-development/architecture/frontend_error_boundary_resilience.md
---

# SolidJS Control Flow and Component API Review

**Objective:** Find the places where a Solid component layer recreates DOM it should keep,
loses reactivity at a component boundary, renders children twice, or loses context —
and replace each with the primitive built for that job, so lists keep focus and state,
props stay live, and failures stay contained.

**When to Use:**
- Typing in a list row loses focus, or row-local state resets when data refreshes.
- Default props or forwarded props stop updating when the parent changes them.
- A wrapper component renders its children twice or in the wrong place.
- `useContext` returns `undefined` in some code paths but not others.
- Building or reviewing a shared component library on Solid.
- **Not this prompt if** the bug is in signals, memos, effects or store updates — use
  `domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md` (it also
  covers the basic "don't destructure props" rule; this prompt covers forwarding and
  defaults at scale). For data loading and SSR, use
  `frontend_solidjs_solidstart_data_ssr.md`. For prop *type* design, use
  `domain-frontend-development/typescript/frontend_typescript_component_typing.md`.

**Version note:** names and behaviours below are Solid 1.x; verify against current docs
for the installed version, particularly if moving to a newer major release.

## Inputs / Context

1. **Components in scope**, especially shared/library components and list-heavy views.
2. **Symptoms**: focus loss, reset state, stale props, double rendering, missing context.
3. **List data shapes**: arrays of objects with stable identity vs arrays of primitives
   or objects recreated on every fetch.
4. **Boundary placement**: `ErrorBoundary`, `Suspense`, `Portal` usage.

## Method

1. **Choose list primitives by data shape (IT-22).**
   - `<For each>`: keyed by item reference; the index is a signal. Right for arrays of
     objects whose identity is stable (store items, immutable updates that keep
     unchanged items).
   - `<Index each>`: keyed by position; each item is a signal. Right for primitives and
     fixed-length lists whose values change (inputs bound to array positions).
   - `.map()` in JSX: recreates every row on change — flag for dynamic lists.
   - If data is refetched as fresh objects every time, `<For>` recreates every row;
     either reconcile into a store (keyed reconciliation) or use `<Index>`.
2. **Conditional rendering (DS-29).** `<Show when fallback>` for one branch, with the
   callback-children form to receive a narrowed, non-null value; `<Switch>/<Match>`
   for several branches instead of nested ternaries; `<Dynamic component>` for
   runtime-chosen components. Note that toggling `<Show>` destroys and recreates its
   subtree — local state inside resets by design.
3. **Forward and default props without breaking tracking.** Use `splitProps` to
   separate local props from those passed through (`...others`), and `mergeProps` for
   defaults. Flag destructuring with defaults (`{ size = "md" }`), object spread of
   `props` into new objects outside JSX, and `Object.assign` copies — each snapshots
   values.
4. **Resolve children once.** Reading `props.children` more than once can create the
   DOM more than once. When a component inspects, filters or places children in several
   slots, resolve them with the `children()` helper and read the result.
5. **Keep context and ownership intact.** `useContext` finds providers through the
   current owner. Calls after an `await`, inside `setTimeout`, or in event-handler code
   that creates computations run without that owner — context returns `undefined` and
   computations are never disposed. Read context synchronously during setup; if work
   must happen later, capture the owner and run with it (verify the owner APIs).
   Provider values are not reactive by themselves — pass signals or stores, not plain
   snapshots.
6. **Check refs and lifecycle.** Refs are assigned during render and are safe to use in
   `onMount`, not in the component body before the JSX is created.
7. **Place boundaries where failure should stop.** `ErrorBoundary` around independent
   regions (a widget, not the whole app), with a reset path; `Suspense` around reads that
   can be slow independently; `Portal` content keeps its owner but not its DOM parent —
   check styles and focus management.
8. **Evidence and clearance (RT-05, QA-24).** Cite each finding with the line and the
   symptom it explains; list patterns checked and judged fine. Confidence: High =
   reproduced, Medium = read in code, Low = style preference.

## Output Format

```
# Solid control flow & component API review — [scope]   Solid: [version]   Date: [..]

## List inventory
| List | Data shape | Identity stable? | Primitive used | Recommended | Symptom explained |
## Conditional rendering
## Prop forwarding and defaults
| Component | Pattern found | Breaks tracking? | Fix |
## Children handling
## Context and ownership
## Boundaries
| Region | ErrorBoundary | Suspense | Reset path | Finding |
## Findings
| ID | Finding | Severity | Confidence | Evidence | Fix |
## Checked and cleared
## Library conventions to adopt
```

## Verification

- [ ] Each list states its data shape and identity stability before a primitive is chosen.
- [ ] Each prop-forwarding finding shows the line that snapshots the value.
- [ ] Children-resolution findings name the component reading `props.children` twice.
- [ ] Context findings identify the async or deferred call that lost the owner.
- [ ] Boundary findings name what the user sees on failure today.
- [ ] A checked-and-cleared table exists.

## False-Positive Prevention

1. **`<For>` as always right.** With primitives or freshly recreated objects it recreates
   rows; `<Index>` or reconciliation fits better.
2. **`<Index>` as a performance trick.** It changes what is keyed; row-local state then
   follows the position, not the item. Only use it when that is what you want.
3. **State reset inside `<Show>` as a bug.** Unmounting resets local state by design;
   lift state if it must survive.
4. **Every spread as a reactivity break.** `{...others}` from `splitProps` in JSX is the
   intended pattern.
5. **Nested ternaries as wrong.** They work; `<Switch>` is clearer and avoids some
   recreation, but rate it Low unless a symptom is explained.
6. **React patterns imported.** `React.memo`, `useCallback` and key props have no Solid
   equivalent need; do not recommend them.

## Example Output

```
# Solid control flow & component API review — "Copperline" admin UI kit + invoices view
Solid 1.8   Date: 2026-10-02

## List inventory
| Invoice line items (editable) | objects, refetched after each save | no | <For> | reconcile into
  store, keep <For> | inputs lose focus after autosave |
| Tag chips (string[]) | primitives | n/a | .map() | <Index> | all chips re-mount on any edit |
| Notifications | store items | yes | <For> | keep | — |

## Prop forwarding and defaults
| Button   | const { variant = "primary", ...rest } = props | yes | mergeProps({ variant: "primary" }, props)
  then splitProps(merged, ["variant"]) |
| TextField | const attrs = { ...props, class: cx(props.class) } outside JSX | yes | splitProps + class in JSX |

## Children handling
Card reads props.children in header slot check and body → body DOM created twice (2 timers
started in child). Fix: const c = children(() => props.children); use c() in both places.

## Context and ownership
InvoiceActions: after `await saveDraft()`, calls useToast() → undefined → toast silently
fails. Fix: const toast = useToast() during setup; call toast.show() after await.

## Boundaries
| Invoices page | root only | root only | none | a failed PDF preview blanks the page |
  wrap preview in ErrorBoundary with "Retry" calling reset |

## Findings
| C1 | Line items recreated on refetch → focus loss | High | High | reproduced; <For> + fresh objects |
  reconcile(store) |
| C2 | Button default variant snapshot | Medium | High | parent toggles variant; button stays primary |
| C3 | Card children rendered twice | Medium | High | duplicate timers in profiler |
| C4 | useToast after await | Medium | High | reproduced |
| C5 | No local ErrorBoundary on preview | Medium | High | forced error → blank page |
| C6 | Tag chips via .map() | Low | High | — |

## Checked and cleared
| Modal via Portal | focus trap and owner context work | manual test |
| Nested ternary in StatusPill | 2 branches, no symptom | source |

## Library conventions to adopt
mergeProps for defaults → splitProps for forwarding → children() when reading twice →
read context during setup → ErrorBoundary per independent widget. Verify names for version.
```

## Techniques Used

- **DS-29 Domain Pattern Library** — named Solid primitives (For, Index, Show, Switch, Dynamic, splitProps, mergeProps, children) with selection guidance.
- **IT-22 Workflow Decision Matrix** — list primitive chosen from data shape and identity stability.
- **RT-05 Evidence-Based Reasoning** — each finding ties a line of code to a reproduced symptom.
- **QA-24 Dismissed-Candidates Coverage Table** — acceptable patterns recorded as checked and cleared.

## Related Prompts

- `frontend_solidjs_reactivity_patterns.md` — signal, memo, effect and store correctness beneath these components.
- `domain-frontend-development/typescript/frontend_typescript_component_typing.md` — typing the props these components forward and default.
- `domain-frontend-development/architecture/frontend_error_boundary_resilience.md` — framework-independent error-boundary placement and recovery design.
