---
title: "Qwik Reactive State and Tasks Review — Signals vs Stores, Tracking, Computed vs Task, Server-First Task Execution, and Cleanup"
category: frontend-development/qwik
description: "Diagnose why a Qwik component does not update, updates twice, loops, or crashes on the server: check signal and store choice and mutation, what each task actually tracks, whether derived values use computed rather than tasks, which code runs on the server first, async races and cleanup, and values marked non-serializable that vanish after resume."
techniques:
  - IT-23
  - RT-09
  - RT-05
  - QA-24
difficulty: advanced
tags:
  - qwik-signals
  - qwik-stores
  - usetask
  - usecomputed
  - useresource
  - reactivity-bugs
  - qwik-ui-not-updating
  - code-runs-on-server-and-crashes
  - effect-runs-twice
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/qwik/frontend_qwik_resumability.md
  - domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md
  - domain-frontend-development/qwik/frontend_qwik_city_loaders_actions.md
---

# Qwik Reactive State and Tasks Review

**Objective:** Trace each reported reactivity symptom in a Qwik app to its root cause in
how state is declared, mutated, read and tracked — and separate genuine bugs from code that
merely looks unusual to someone used to React — with a fix and a confidence level per
finding.

**When to Use:**
- The UI does not update after state changes, or updates only sometimes.
- A task runs on the server when the author expected the browser (`window is not
  defined`), or runs twice, or never re-runs.
- Derived values are stale or computed through a chain of tasks writing to signals.
- A value works on first load but is `undefined` after navigation or resume.
- **Not this prompt if** the problem is too much JavaScript executing on load, handlers
  without `$` boundaries, or serialization errors when the page renders — use
  `domain-frontend-development/qwik/frontend_qwik_resumability.md`. For route loaders,
  actions and server data flow, use `frontend_qwik_city_loaders_actions.md`. Solid's
  signal model is similar in vocabulary but different in execution; for Solid use
  `domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md`.

## Inputs / Context

1. **Symptoms** as observed: what the user did, what should have changed, what did.
2. **Components and hooks involved**: every `useSignal`, `useStore`, `useComputed$`,
   `useTask$`, `useVisibleTask$`, `useResource$`, and `noSerialize` in scope.
3. **Where it fails**: SSR, first client interaction, client-side navigation.
4. **Qwik version** (v1 vs v2 differ in package names and some hook details — verify
   every API name and default below against current docs).

## Method

1. **Index by symptom (IT-23).** Sort reports into: *not updating*, *updating too often
   or looping*, *server crash*, *stale derived value*, *lost after resume*, *async race*.
   Each symptom has a short list of usual causes; start there.
2. **Not updating — check mutation shape.** A `useSignal` holding an object or array is
   shallow: `sig.value.push(x)` or `sig.value.name = 'a'` does not notify; assign a new
   value. A `useStore` is deep by default and tracks nested mutation; if it was created
   with deep tracking turned off, nested writes do not notify. Destructuring a store
   (`const { count } = store`) copies the value once and loses reactivity.
3. **Not re-running — check what the task tracks.** `useTask$` runs once (on the server
   during SSR, if the component renders there) and re-runs only when something read
   through `track()` changes. A task that reads `sig.value` without `track` will not
   re-run on change. Conversely, tracking a whole store re-runs on any nested change.
4. **Looping — check writes to tracked state.** A task that tracks `a` and writes `a`, or
   two tasks that write each other's inputs, loop or thrash. Derivations belong in
   `useComputed$` (synchronous, no side effects); async derivations belong in
   `useResource$`; side effects belong in tasks.
5. **Server crash — check execution location.** `useTask$` bodies run on the server
   first; browser APIs there must be guarded with the build-time `isServer`/`isBrowser`
   flags or moved to `useVisibleTask$`. Do not "fix" this by making every task visible —
   that adds eager client work the resumability review will flag.
6. **Lost after resume — check `noSerialize`.** Values wrapped in `noSerialize` (SDK
   clients, chart instances, DOM handles) are not in the serialized state; after resume
   they are `undefined` until re-created. Code must re-create them lazily where used.
7. **Async races — check cleanup.** Tasks and resources that fetch when a tracked value
   changes must abort the previous request in the provided `cleanup` callback; otherwise
   a slow earlier response overwrites a newer one.
8. **Explain root cause (RT-09) with evidence (RT-05).** For each finding: root cause,
   the symptom it produces, why, and the fix — citing the line. Record suspected causes
   ruled out (QA-24). Confidence: High = reproduced and traced; Medium = traced in code,
   not reproduced; Low = pattern match only.

## Output Format

```
# Qwik reactive state review — [app/feature]   Qwik version: [..]   Date: [..]

## Symptom index
| Symptom | Where (SSR / interaction / navigation) | Components | Finding IDs |
## State inventory
| Name | Primitive | Holds | Mutated how | Read where | Tracked by |
## Findings
### [ID] [title]   Severity: [..]   Confidence: [..]
Root cause → Symptom → Why → Fix (file:line, before/after)
## Ruled out
| Suspected cause | Why ruled out | Evidence |
## Patterns to adopt team-wide
```

## Verification

- [ ] Every reported symptom maps to a finding or a ruled-out entry.
- [ ] Each finding states whether the code runs on the server, client, or both.
- [ ] Every task finding shows exactly what is tracked.
- [ ] Derived-state fixes use computed or resource, not another task.
- [ ] Fixes do not move server-safe tasks to visible tasks without reason.
- [ ] Version-sensitive API names are flagged for verification.

## False-Positive Prevention

1. **React habits as bugs.** Qwik has no dependency arrays; the absence of one is not a
   defect. Tracking is explicit through `track()`.
2. **"Runs on the server" as wrong.** Server-first task execution is the design; it is
   only a bug when the body needs the browser.
3. **Every `useVisibleTask$` as a smell.** Measuring layout or wiring a third-party DOM
   widget legitimately needs it; flag only when a server-safe task would do.
4. **Deep stores as always wrong.** Deep tracking costs little for small objects; flag it
   for large collections that change often.
5. **Loader data as client state.** Values from route loaders refresh on navigation and
   actions; copying them into a local signal and then wondering why it is stale is the
   bug, not the loader.
6. **Assuming component bodies never re-run.** Unlike Solid, a Qwik component can
   re-render when state it read during render changes; do not import Solid's run-once
   rule (verify render semantics for the version).

## Example Output

```
# Qwik reactive state review — "Tidepool" event ticketing, seat picker   Qwik 1.x

## Symptom index
| Selected seats don't highlight | interaction | SeatMap | R1 |
| Total price shows previous selection | interaction | Summary | R2 |
| "window is not defined" in logs | SSR | SeatMap | R3 |
| Map blank after back-navigation | navigation | SeatMap | R4 |
| Price flickers between two values on fast clicks | interaction | Summary | R5 |

## Findings
### R1 Signal array mutated in place   Severity: High   Confidence: High
Root cause: const selected = useSignal<string[]>([]); onClick$ does selected.value.push(id)
Symptom: highlight never updates. Why: signals notify on assignment, not inner mutation.
Fix: selected.value = [...selected.value, id]   (SeatMap.tsx:44)

### R2 Total derived through a task   Severity: Medium   Confidence: High
Root cause: useTask$ reads selected.value without track(), writes total.value
Symptom: total computed once on server, never again.
Fix: const total = useComputed$(() => sum(selected.value, prices.value))   (Summary.tsx:18)

### R3 Browser API in server-run task   Severity: Medium   Confidence: High
Root cause: useTask$(() => { const w = window.innerWidth; ... })
Fix: compute layout in CSS (container query); or guard with isBrowser and track the size
signal. Not moved to useVisibleTask$ — map renders server-side fine without it.

### R4 noSerialize chart instance gone after resume   Severity: High   Confidence: Medium
Root cause: store.renderer = noSerialize(new SeatRenderer(canvas)) set once on first load
Fix: create renderer lazily in the canvas visible task; never read it from serialized state.

### R5 Price fetch race   Severity: Medium   Confidence: High
Root cause: useResource$ tracks selected, fetches /price, no abort
Fix: const c = new AbortController(); cleanup(() => c.abort()); fetch(url, { signal: c.signal })

## Ruled out
| Missing $ on onClick | handler is inline arrow inside onClick$ | source |
| Store deep tracking disabled | store created with defaults | source |

## Patterns to adopt team-wide
Assign, don't mutate, signal values · derive with useComputed$ · abort in cleanup ·
re-create noSerialize values where used. API names — verify against current docs.
```

## Techniques Used

- **IT-23 Symptom-Based Troubleshooting Organization** — reports grouped by what the user sees before causes are examined.
- **RT-09 Root Cause Explanation Pattern** — each finding written as root cause → symptom → why → fix.
- **RT-05 Evidence-Based Reasoning** — findings cite the exact line and, where possible, a reproduction.
- **QA-24 Dismissed-Candidates Coverage Table** — plausible causes ruled out are listed with evidence.

## Related Prompts

- `frontend_qwik_resumability.md` — `$`-boundaries, serialization and eager-execution leaks.
- `domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md` — comparable fine-grained reactivity review for Solid's run-once model.
- `frontend_qwik_city_loaders_actions.md` — server data flow that feeds this client state.
