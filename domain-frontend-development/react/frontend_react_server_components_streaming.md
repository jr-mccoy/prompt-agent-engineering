---
title: "React Server Components & Streaming SSR Analysis"
category: frontend-development/react
description: "Analyze the server/client boundary in React Server Components apps — 'use client'/'use server' placement, Suspense streaming, RSC data fetching, and serialization boundaries — to find boundary mistakes and streaming bottlenecks."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - react
  - server-components
  - streaming-ssr
  - suspense
  - use-client
  - serialization
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/react/frontend_react_component_patterns.md
  - domain-frontend-development/react/frontend_react_performance.md
  - domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
---

# React Server Components & Streaming SSR Analysis

**Objective:** Audit a React Server Components (RSC) application for incorrect server/client boundaries, misused `'use client'`/`'use server'` directives, broken Suspense streaming, and unsafe serialization across the RSC boundary, then recommend specific, evidence-backed fixes.

**When to Use:**
- Use when: A component tree mixes Server and Client Components and you suspect the boundary is drawn in the wrong place (e.g. an entire page marked `'use client'`).
- Use when: Streaming SSR is not progressively rendering — the page blocks on a slow data dependency instead of streaming a Suspense fallback.
- Use when: You hit serialization errors (functions, class instances, Dates, or Symbols passed from Server to Client Components).
- Use when: Bundle size is unexpectedly large because client-only code leaked into shared modules.
- Don't use when: The app is a pure client-side SPA with no server rendering — boundary directives do not apply there.

## Instructions

1. **Map the Server/Client Boundary**
   - Identify which components are Server Components (the default in an RSC tree) versus Client Components (files or modules carrying `'use client'`).
   - For each `'use client'` directive, note where it sits in the tree. The directive marks an *entry point*: everything imported into that module becomes client code.
   - Flag pages or layouts where `'use client'` is placed at or near the root, forcing large subtrees to ship to the browser unnecessarily.

2. **Audit `'use client'` Placement**
   For each Client Component boundary:
   - Does the component actually need client capabilities (state, effects, event handlers, browser-only APIs, refs to DOM)? If not, it likely belongs on the server.
   - Could the boundary be pushed *down* the tree so that only the interactive leaf becomes a Client Component while data-fetching parents stay on the server?
   - Are Server Components being passed as `children` props into Client Components (the "donut" / slot pattern) to keep server content out of the client bundle?

3. **Audit `'use server'` Placement**
   - Confirm `'use server'` is used for Server Actions (functions invoked from the client), not as a way to "mark" Server Components — Server Components do not need a directive.
   - Verify exported server functions are intended to be callable from the client; treat each as a network endpoint with its own input validation and authorization.

4. **Analyze Data Fetching in RSC**
   - Confirm data is fetched in Server Components (async components, `await` at the top of the function) rather than re-fetched on the client where a server fetch would suffice.
   - Look for request waterfalls: sequential `await`s that could run concurrently (e.g. `Promise.all`) or be hoisted to parallel siblings.
   - Check that fetches relying on request-time data are not being statically cached in a way that serves stale content (verify caching semantics against current framework docs).

5. **Review Suspense Streaming**
   - Identify Suspense boundaries and confirm slow data dependencies are wrapped so the shell can stream immediately with a fallback.
   - Flag a single top-level Suspense (or none) that blocks the whole page on the slowest data source.
   - Confirm fallbacks are meaningful (skeletons that match layout) and that boundaries are placed to maximize useful first paint.

6. **Inspect Serialization Boundaries**
   For every prop crossing Server → Client:
   - Is the value serializable? Functions (except Server Action references), class instances, `Map`/`Set` (verify support against current docs), `Symbol`, and `Date` handling all warrant scrutiny.
   - Are large objects being passed wholesale when only a subset is needed? Over-serialization bloats the RSC payload.
   - Are event handlers being passed from a Server Component to a Client Component (not allowed)?

7. **Check for Client-Only Code Leakage**
   - Search for browser globals (`window`, `document`, `localStorage`) referenced in modules that may execute on the server.
   - Confirm client-only libraries are imported only within `'use client'` modules.

8. **CRITICAL: Verify findings before reporting**
   - For each finding, trace the actual import graph and directive placement rather than assuming. Assign a Confidence level:
     - **High:** Directive placement / serialization error is directly visible in the code and the failure mode is unambiguous (e.g. a function prop crossing the boundary).
     - **Medium:** The pattern is suspicious and likely problematic, but depends on runtime data or framework version-specific behavior you cannot fully see.
     - **Low:** A heuristic concern (e.g. "this boundary *might* be pushable lower") that needs the author to confirm intended interactivity.
   - Do not report a streaming or caching claim as fact without citing the specific code construct; where behavior is framework-version-dependent, note "verify against current docs."

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Don't assume every `'use client'` is wrong — interactive leaves legitimately need it.
- Don't claim a component "must" be a Server Component without checking for hidden client needs (a `useRef` to a DOM node, an `onClick`, a third-party client-only hook).
- Don't assert that a value "can't be serialized" without confirming its actual type — many plain objects and arrays serialize fine.
- Don't report a "waterfall" when the sequential awaits are genuinely dependent (the second needs the first's result).
- Don't state version-specific RSC/streaming behavior (e.g. exactly which types serialize) as settled fact — phrase as "verify against current docs."
- Don't flag missing Suspense on data that is fast and non-blocking; streaming has overhead and isn't free.
- Don't invent performance numbers for payload size or TTFB improvements.

✅ **DO:**
- Trace the import graph from each `'use client'` entry point to see what actually ships to the client.
- Distinguish "needs interactivity" (stays client) from "only renders data" (can be server).
- Cite the exact prop, line, or directive as evidence for each finding.
- Recommend pushing the boundary *down* the tree and using the children-slot pattern when server content is being needlessly clientized.
- Verify whether two awaits are independent before recommending `Promise.all`.
- Note when a behavior depends on the framework/runtime and flag it for doc verification.
- Prioritize fixes by user-visible impact (blocked streaming, hydration errors) over stylistic boundary nits.

## Expected Output

A structured report of boundary and streaming findings, each with severity, confidence, location, evidence, and a concrete fix, followed by a prioritized remediation list.

- Boundary map summarizing where server/client lines are drawn
- Per-finding detail with serialization and streaming implications
- Prioritized recommendations ordered by user-visible impact

### Output Format

```markdown
## RSC & Streaming Analysis Report

### Summary
- Server/Client boundary health: <good | mixed | inverted>
- Streaming status: <progressive | partially blocked | fully blocking>
- Total findings: <n> (High: <n>, Medium: <n>, Low: <n>)

### Boundary Map
| Component | Type | Directive | Notes |
|-----------|------|-----------|-------|
| ... | Server/Client | 'use client' / none | ... |

### Findings
#### [SEVERITY] <Title>
- **Severity:** Critical | High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** <file:line / component>
- **Evidence:** <exact code construct>
- **Impact:** <bundle / hydration / streaming / serialization>
- **Recommendation:** <specific fix>

### Prioritized Recommendations
1. ...
```

## Example Output

```markdown
## RSC & Streaming Analysis Report

### Summary
- Server/Client boundary health: inverted (root layout is a Client Component)
- Streaming status: fully blocking (single page-level await, no Suspense)
- Total findings: 5 (High: 2, Medium: 2, Low: 1)

### Boundary Map
| Component         | Type   | Directive    | Notes |
|-------------------|--------|--------------|-------|
| app/dashboard/page| Client | 'use client' | Forces entire subtree to client |
| <RevenueChart>    | Client | (inherited)  | Genuinely interactive (tooltips) |
| <UserTable>       | Client | (inherited)  | Only renders data — no interactivity |
| <fetchMetrics>    | Server | n/a          | Data fetch, but runs under client boundary |

### Findings

#### [HIGH] Root page marked 'use client', clientizing the whole tree
- **Severity:** High
- **Confidence:** High
- **Location:** app/dashboard/page.tsx:1
- **Evidence:**
  ```tsx
  'use client'
  export default function DashboardPage() {
    const metrics = useMetrics() // client fetch
    return <><UserTable rows={metrics.rows} /><RevenueChart data={metrics.series} /></>
  }
  ```
- **Impact:** `UserTable` (static) ships to the client unnecessarily; data is fetched client-side, adding a round trip and losing server caching.
- **Recommendation:** Make `page.tsx` a Server Component (remove `'use client'`), `await` the data on the server, render `UserTable` as a Server Component, and keep only `RevenueChart` as a `'use client'` leaf.

#### [HIGH] Event handler passed from Server to Client Component
- **Severity:** High
- **Confidence:** High
- **Location:** app/dashboard/Filters.tsx:14
- **Evidence:**
  ```tsx
  // Filters is a Server Component
  return <ClientDropdown onSelect={(v) => applyFilter(v)} />
  ```
- **Impact:** Functions are not serializable across the RSC boundary — this throws at render time.
- **Recommendation:** Move the handler into the Client Component, or pass a Server Action reference (`'use server'`) if the action must run on the server.

#### [MEDIUM] No Suspense around slow data — page blocks on the slowest fetch
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** app/dashboard/page.tsx (after server refactor)
- **Evidence:** Single top-level `await getSlowReport()` with no `<Suspense>` boundary.
- **Impact:** First paint is delayed by the slowest dependency; nothing streams early.
- **Recommendation:**
  ```tsx
  <Suspense fallback={<TableSkeleton />}>
    <SlowReport />   {/* async Server Component fetches internally */}
  </Suspense>
  ```
  Wrap each slow region in its own Suspense boundary so the shell streams immediately.

#### [MEDIUM] Sequential awaits create a request waterfall
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** app/dashboard/data.ts:8
- **Evidence:**
  ```ts
  const user = await getUser(id)
  const team = await getTeam(teamId) // does not depend on `user`
  ```
- **Impact:** Two independent requests run serially, doubling latency.
- **Recommendation:** `const [user, team] = await Promise.all([getUser(id), getTeam(teamId)])`. Confirm independence first.

#### [LOW] Whole object serialized when only two fields are used
- **Severity:** Low
- **Confidence:** Low
- **Location:** app/dashboard/page.tsx:30
- **Evidence:** `<RevenueChart data={fullReport} />` where the chart reads only `series` and `currency`.
- **Impact:** Larger RSC payload than necessary.
- **Recommendation:** Pass `{ series: fullReport.series, currency: fullReport.currency }` to shrink the serialized payload. (Verify chart prop usage before trimming.)

### Prioritized Recommendations
1. Invert the boundary: make the dashboard page a Server Component and push `'use client'` down to interactive leaves (fixes High #1 + bundle bloat).
2. Remove the cross-boundary event handler; relocate it or use a Server Action (fixes runtime error, High #2).
3. Add per-region Suspense boundaries to enable progressive streaming.
4. Parallelize independent server fetches.
5. Trim over-serialized props.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective scoping the audit to boundary, directives, streaming, and serialization.
- **ST-02 (Structured Sequential Instructions):** Walks from mapping the boundary → directive audits → data fetching → streaming → serialization in dependency order.
- **RT-02 (Multi-Dimensional Analysis Framework):** Examines bundle impact, hydration correctness, streaming behavior, and serialization safety as distinct dimensions.
- **RT-05 (Evidence-Based Reasoning):** Requires citing the exact directive, prop, or import for each finding and assigning a confidence level before reporting.
- **DS-06 (Prioritization Guidance):** Orders recommendations by user-visible impact (blocked streaming, hydration errors) ahead of stylistic concerns.

## Related Prompts
- [frontend_react_component_patterns.md](frontend_react_component_patterns.md) - Decide which components should be composed as server vs client building blocks.
- [frontend_react_performance.md](frontend_react_performance.md) - Pair boundary analysis with re-render and bundle profiling.
- [../nextjs/frontend_nextjs_data_fetching.md](../nextjs/frontend_nextjs_data_fetching.md) - Apply RSC data-fetching patterns within the App Router.
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Connect streaming improvements to LCP/INP outcomes.
