---
title: "SolidStart Data Loading and SSR Review — Queries, Route Preload, Server Functions, Actions, Suspense Placement, and Hydration Safety"
category: frontend-development/solidjs
description: "Review how a SolidStart app gets data to the page and keeps it correct: whether reads go through cached queries started by route preload rather than component-level fetches, where Suspense boundaries sit, whether server functions and actions validate and authorise as public endpoints, whether mutations revalidate the right queries, and which render paths cause hydration mismatches or leak state across requests on the server."
techniques:
  - RT-02
  - RT-05
  - IT-23
  - DS-06
difficulty: advanced
tags:
  - solidstart
  - server-functions
  - createasync
  - route-preload
  - ssr-hydration
  - solid-router-actions
  - page-data-loads-twice
  - hydration-mismatch-error
  - load-data-before-page-renders
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md
  - domain-frontend-development/react/frontend_react_server_components_streaming.md
  - domain-frontend-development/svelte/frontend_sveltekit_fullstack.md
---

# SolidStart Data Loading and SSR Review

**Objective:** Establish that a SolidStart app loads each page's data once, in parallel
with its code, behind sensibly placed Suspense boundaries; that every server function and
action is validated and authorised as a public endpoint; that mutations refresh exactly the
data they change; and that server rendering neither mismatches on hydration nor shares one
user's state with another.

**When to Use:**
- Pages show a spinner after navigation even though data could start loading earlier.
- The same request fires twice (server and client) or once per component that needs it.
- Hydration warnings appear, or content flickers from server to client value.
- After a form submit, some parts of the page update and others are stale.
- Before exposing `"use server"` functions to production traffic.
- **Not this prompt if** the problem is signals, memos, effects or store updates inside
  components — use
  `domain-frontend-development/solidjs/frontend_solidjs_reactivity_patterns.md`. For
  component APIs and control flow (`<For>`, `<Show>`, `splitProps`), use
  `frontend_solidjs_control_flow_components.md`. For the same job in SvelteKit, use
  `domain-frontend-development/svelte/frontend_sveltekit_fullstack.md`.

**Version note:** SolidStart's data APIs live in `@solidjs/router` and have been renamed
across releases (for example `cache` → `query`, route `load` → `preload`). Verify every
name below against current docs for the installed versions.

## Inputs / Context

1. **Versions**: `@solidjs/start`, `@solidjs/router`, `solid-js`; deployment preset.
2. **Route files** under `src/routes`, with any exported route config (preload).
3. **Data functions**: every `query(...)`, `createAsync`, `createResource`, `action(...)`
   and `"use server"` function, with the file that defines it.
4. **Suspense and ErrorBoundary placement** in the app shell and routes.
5. **Auth model**: how the request user is read on the server (request event, session).
6. **Observed symptoms**: duplicate requests (network panel), hydration warnings
   (console), stale UI after actions.

## Method

1. **Map routes to reads and writes (RT-02).** Per route: queries used, whether the
   route preloads them, server functions called, actions bound to forms, Suspense and
   ErrorBoundary that wrap each read.
2. **Check that reads are cached queries.** Server reads wrapped in `query(fn, key)` are
   de-duplicated within a request and reused across preload and component; plain
   `"use server"` calls or `createResource(fetch…)` inside components fetch per call site.
   Flag pages that fetch the same data from several components.
3. **Check preload.** A route that preloads its queries starts fetching while its code
   chunk loads, removing the code-then-data waterfall. Flag routes whose first read only
   starts when the component renders.
4. **Check Suspense placement.** Reads via `createAsync` suspend to the nearest Suspense
   boundary. With only a root boundary, any slow read blanks the whole page; place
   boundaries around independent regions. For SEO-critical data under streaming SSR,
   check whether the read is set to block the stream (verify the option name).
5. **Treat server functions and actions as public endpoints (RT-05).** Each `"use
   server"` function is reachable by a crafted request. Confirm it validates input,
   reads the user from the server request context (never from an argument the client
   sends), checks ownership/role, and returns only the fields the UI needs.
6. **Check mutations and revalidation.** Actions bound to `<form action={…}
   method="post">` work without JavaScript when the action is a server function; confirm
   pending and error states come from the submission APIs. After an action, confirm
   which queries revalidate (by default and by explicit keys) and flag stale regions or
   over-revalidation of expensive queries.
7. **Check hydration and request isolation (IT-23).** Symptoms → causes: *mismatch
   warning* → render-time `Date.now()`, `Math.random()`, locale/timezone formatting, or
   `typeof window` branches; fix with `isServer`/`onMount`, a client-only wrapper, or
   server-provided values. *Another user's data appears* → module-level signals or stores
   created at import time are shared by every request on the server; move state into
   context or request-scoped values.
8. **Prioritise (DS-06)**: authorisation and cross-request leaks first, then correctness
   (stale data, mismatches), then performance (waterfalls, duplicates). Confidence: High =
   reproduced (network panel, crafted request, console), Medium = read in code, Low =
   inferred.

## Output Format

```
# SolidStart data & SSR review — [app]   Versions: [..]   Date: [..]

## Route map
| Route | Queries | Preloaded? | Server fns / actions | Suspense regions | ErrorBoundary |
## Duplicate and waterfall reads
| Data | Call sites | Cached query? | Requests per navigation | Fix |
## Server functions and actions
| Function | Validation | User from server context? | AuthZ | Fields returned | Finding |
## Revalidation after mutations
## Hydration and request isolation
## Findings
| ID | Finding | Severity | Confidence | Evidence | Fix |
## Prioritised plan
```

## Verification

- [ ] Every route has a preload verdict.
- [ ] Duplicate requests were counted in the network panel, not inferred.
- [ ] Every `"use server"` function has an authorisation verdict.
- [ ] Each action lists the queries it revalidates.
- [ ] Hydration findings cite the console warning or a reproduced mismatch.
- [ ] Module-level state was searched for in server-rendered code.
- [ ] Version-sensitive names are marked "verify against current docs".

## False-Positive Prevention

1. **Every `createResource` as wrong.** Client-only data (geolocation, local storage) is
   a fine use; flag it only for server data that a query would cache.
2. **A root Suspense as a bug.** For small apps with one read per page it is adequate.
3. **Server function = private.** It compiles to an HTTP endpoint; treat it as public.
4. **Hydration mismatch from any `isServer` branch.** Branching on `isServer` inside
   effects or `onMount` is fine; it is render-time branching that mismatches.
5. **Over-revalidation as harmless.** Revalidating every query after a tiny action can
   multiply database load; check cost before blessing defaults.
6. **API names from a different release.** Renamed APIs are not bugs; check versions.

## Example Output

```
# SolidStart data & SSR review — "Brightwater" course platform
@solidjs/start 1.x, @solidjs/router 0.15 (verify), Node preset   Date: 2026-10-02

## Route map (excerpt)
| /courses/[slug]        | getCourse, getProgress | no  | enroll (action) | root only | root |
| /courses/[slug]/lesson | getLesson              | yes | markDone (action), getNotes (server fn) | 2 | yes |
| /dashboard             | getProgress ×3 call sites | no | — | root only | root |

## Duplicate and waterfall reads
| getProgress | Header, Sidebar, ProgressCard | no — plain server fn | 3 per navigation | wrap in query
  keyed by userId; preload in route |
| getCourse   | page component | yes | 1, but starts after 180 KB chunk loads | add route preload |

## Server functions and actions
| getNotes(lessonId, userId) | none | no — userId from client ✗ | none | all users' notes for lesson if
  userId omitted | F1 |
| enroll(courseId) | zod ✓ | yes ✓ | seat limit ✓ | ok | — |

## Revalidation after mutations
markDone revalidates all queries (default) incl. getCourse (1.2 s catalogue query) — scope to
progress keys only.

## Hydration and request isolation
| Warning on /dashboard: "Last active 3 minutes ago" text differs | render-time Date.now() | F3 |
| lib/currentUser.ts: const [user, setUser] = createSignal() at module scope, set during SSR |
  under load, page rendered with previous request's user name | F2 |

## Findings
| F1 | getNotes trusts client-sent userId | Critical | High | crafted POST returned other user's notes |
  read user from request context; check enrolment |
| F2 | Module-level user signal shared across SSR requests | Critical | High | reproduced with 2
  concurrent sessions in staging | provide user via context per request |
| F3 | Relative time computed at render | Low | High | console warning | render ISO server-side,
  format in onMount |
| F4 | getProgress fetched 3× per navigation | Medium | High | network panel | query + preload |
| F5 | getCourse not preloaded | Medium | High | waterfall in trace | export route preload |
| F6 | markDone revalidates catalogue | Medium | Medium | server logs | revalidate progress keys |

## Prioritised plan
1. F1, F2 immediately.   2. F4, F5, F6 this sprint.   3. F3 with next UI pass.
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — reads, writes, boundaries and isolation reviewed as separate dimensions per route.
- **RT-05 Evidence-Based Reasoning** — duplicates counted in the network panel; endpoints probed with crafted requests.
- **IT-23 Symptom-Based Troubleshooting Organization** — hydration and leak symptoms mapped to their usual causes.
- **DS-06 Prioritization and Severity Guidance** — data exposure, then correctness, then speed.

## Related Prompts

- `frontend_solidjs_reactivity_patterns.md` — signals, memos, effects and stores inside the components that consume this data.
- `domain-frontend-development/react/frontend_react_server_components_streaming.md` — comparing streaming SSR and server boundaries in React.
- `domain-frontend-development/svelte/frontend_sveltekit_fullstack.md` — the equivalent full-stack data review in SvelteKit.
