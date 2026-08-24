---
title: "Client-Side Error Handling & Resilience Audit"
category: frontend-development/architecture
description: "Design and audit client-side resilience: error boundaries, fallback UI, retry and recovery, error reporting, graceful degradation, and error handling around Suspense and async data."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - error-handling
  - error-boundary
  - resilience
  - fallback-ui
  - retry
  - suspense
  - error-reporting
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/react/frontend_react_component_patterns.md
  - domain-frontend-development/architecture/frontend_state_management_selection.md
  - domain-frontend-development/react/frontend_react_performance.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
---

# Client-Side Error Handling & Resilience Audit

**Objective:** Ensure the UI fails gracefully — runtime errors are caught at sensible boundaries, users see recoverable fallback UI instead of a blank screen, transient failures can be retried, and errors are reported with enough context to debug.

**When to Use:**
- Use when: A single component error blanks the whole app, or users hit white screens.
- Use when: Designing error boundaries, fallback UI, and retry strategy for a new feature or app.
- Use when: Async/data-fetching errors (failed requests, Suspense boundaries) aren't handled coherently.
- Use when: Setting up or reviewing error reporting/telemetry for the frontend.
- Don't use when: There is no error surface to evaluate (e.g., a pure static page with no runtime logic).

## Instructions

1. **Map Error Surfaces**
   - Enumerate where errors can originate: render errors, event handlers, async data fetches, lazy/code-split chunk loads, third-party widgets, and Suspense data reads.
   - Note which errors are recoverable (retry/refresh) vs unrecoverable (must isolate and report).
   - Record current handling for each surface (caught, swallowed, or crashes the tree).

2. **Audit Error Boundary Placement**
   - Identify existing boundaries and the subtree each protects. Confirm there is a top-level boundary plus granular boundaries around independent regions (routes, widgets, panels) so one failure doesn't take down unrelated UI.
   - Flag over-broad boundaries (whole app behind one) and missing boundaries around risky subtrees.
   - Note that error boundaries do not catch errors in event handlers or async code — verify those use explicit try/catch or promise rejection handling.

3. **Audit Fallback UI Quality**
   - For each boundary, assess the fallback: is it informative, branded, and actionable (retry button, link to safe state) rather than a raw stack trace or blank box?
   - Confirm fallback UI is itself robust (won't throw) and preserves enough layout that the page doesn't collapse.
   - Check that user-facing messages avoid leaking internal/stack details.

4. **Audit Retry and Recovery**
   - For transient failures (network, chunk load), confirm a retry path exists: a user-triggered "Try again" and/or automatic retry with backoff and a cap.
   - Ensure retries reset boundary state correctly and don't loop infinitely.
   - For chunk-load failures after a deploy, confirm a reload/recovery path (stale chunk handling).

5. **Audit Async & Suspense Error States**
   - Confirm data-fetching layers expose error states the UI renders (not silent failures).
   - Where Suspense is used, confirm an error boundary wraps the Suspense boundary so a thrown fetch surfaces as fallback UI, with a path to retry the suspended resource.
   - Distinguish loading, empty, error, and success states — ensure all four are handled.

6. **Audit Error Reporting**
   - Confirm uncaught errors and boundary catches are reported to a monitoring service with context (component stack, route, user action, release/version).
   - Verify reporting respects privacy (no PII/secrets in payloads) and is sampled/deduplicated to avoid noise.
   - Confirm a global handler exists for unhandled promise rejections and window errors.

7. **Audit Graceful Degradation**
   - For non-critical features (analytics, recommendations, embeds), confirm failure degrades that feature only, not the core flow.
   - Verify the app remains usable when an optional dependency or third-party script fails.

8. **CRITICAL: Verify findings before reporting**
   - Reproduce at least one failure path (throw in a subtree, simulate a failed fetch) to confirm the boundary/fallback actually engages.
   - Do not assume a boundary catches a given error type — verify (event-handler and async errors notably are not caught by render boundaries).
   - **Confidence level** for each finding:
     - **High Confidence:** Reproduced the failure and observed the handling (or its absence).
     - **Medium Confidence:** Code structure strongly implies behavior but not reproduced.
     - **Low Confidence:** Inferred; flagged to test.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assume one top-level error boundary is sufficient — it turns any error into a full-app fallback.
- Assume error boundaries catch event-handler or async errors (they don't; those need try/catch).
- Show raw stack traces or internal messages to users.
- Implement automatic retry without a cap/backoff (risk of infinite loops and request storms).
- Swallow errors silently to "avoid crashes" — silent failure hides real problems.
- Send PII, tokens, or full request bodies to the error reporter.
- Treat loading and error as the same state, or skip the empty state.

✅ **DO:**
- Layer boundaries: one app-level plus granular ones around independent regions.
- Handle event-handler/async errors explicitly and route them to fallback or report.
- Provide actionable, branded fallback UI with a retry/escape path.
- Cap and back off retries; handle stale-chunk reloads after deploys.
- Report to monitoring with component stack, route, and release context, scrubbed of sensitive data.
- Degrade non-critical features in isolation.
- Reproduce a failure to confirm handling before declaring it resilient.

## Expected Output

A resilience audit/design report including:
- A map of error surfaces and current handling.
- Boundary placement assessment.
- Fallback UI and retry/recovery assessment.
- Async/Suspense error-state handling.
- Error reporting assessment.
- Prioritized remediations.

### Output Format

```markdown
## Resilience Audit: [App/Feature]

### Error Surface Map

| Surface | Recoverable? | Current Handling | Gap |
|---------|--------------|------------------|-----|

### Findings

| ID | Issue | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|----------|------------|----------|----------|----------------|

### Boundary Placement
[Assessment]

### Fallback & Retry
[Assessment]

### Async / Suspense
[Assessment]

### Error Reporting
[Assessment]

### Prioritized Remediations
1. ...
```

## Example Output

```markdown
## Resilience Audit: Dashboard App

### Error Surface Map

| Surface | Recoverable? | Current Handling | Gap |
|---------|--------------|------------------|-----|
| Widget render errors | yes (isolate) | none — crashes whole app | No granular boundaries |
| API fetches (widgets) | yes (retry) | error swallowed, shows blank | No error state rendered |
| Lazy route chunks | yes (reload) | unhandled rejection | No stale-chunk recovery |
| Analytics script | yes (degrade) | throws into app | Not isolated |
| Suspense data read | yes (retry) | no boundary around Suspense | White screen on throw |

### Findings

| ID | Issue | Severity | Confidence | Location | Evidence | Recommendation |
|----|-------|----------|------------|----------|----------|----------------|
| E1 | Single error in one widget blanks entire dashboard | High | High | only `<App>` boundary | Throwing in `RevenueWidget` unmounts all widgets | Wrap each widget in its own boundary with a card-sized fallback |
| E2 | Failed widget fetches show nothing (swallowed) | High | High | `useWidgetData.ts` | `catch {}` empty; no error returned | Surface error state + "Retry" in the widget |
| E3 | Suspense not wrapped by an error boundary | High | High | `<Suspense>` in route | Thrown fetch escapes to white screen | Wrap Suspense in an error boundary with retry |
| E4 | Stale chunk after deploy → unhandled rejection | Medium | Medium | dynamic `import()` | Old clients fail to load new chunk | Catch chunk-load error → prompt reload |
| E5 | No retry cap on auto-retry | Medium | High | `retryFetch.ts` | Recursion with no limit | Add max attempts + exponential backoff |
| E6 | Error reports include full request body (may contain PII) | Medium | High | reporter config | `extra: { body }` | Scrub payloads; send route + status only |
| E7 | Analytics failure throws into app | Low | Medium | `analytics.init()` | Uncaught error if blocked | Wrap in try/catch; degrade silently |

### Boundary Placement
Only an app-level boundary exists (E1). Add per-region boundaries: per widget, per route, and around the Suspense boundary (E3). Keep the app-level boundary as the last-resort catch.

### Fallback & Retry
Widget fallbacks should be card-sized with a "Retry" action (E1/E2). Auto-retry needs a cap and backoff (E5). Add stale-chunk reload handling (E4).

### Async / Suspense
Data hooks must return `{ data, error, isLoading }` and the UI must render the error branch (E2). Wrap Suspense in a boundary so suspended-resource throws become recoverable fallback UI (E3).

### Error Reporting
Reporting works but leaks request bodies (E6) and lacks a global unhandled-rejection handler. Add component stack + route + release; scrub sensitive fields; add `window.onunhandledrejection`.

### Prioritized Remediations
1. **E1 & E3 — Add granular + Suspense error boundaries.** Stops single failures from blanking the app.
2. **E2 — Render fetch error states with retry.** Replaces silent failure with recoverable UI.
3. **E6 — Scrub error-report payloads.** Removes PII-leak risk.
4. **E4 & E5 — Stale-chunk recovery + bounded retry.** Handles deploy/transient failures safely.
5. **E7 — Isolate analytics.** Non-critical feature shouldn't crash core flow.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Sets the goal — graceful failure with recovery, not blank screens.
- **ST-02 (Structured Sequential Instructions):** Sequences surface map → boundaries → fallback/retry → async → reporting → degradation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates each surface across recoverability, isolation, reporting, and UX.
- **RT-05 (Evidence-Based Reasoning):** Each finding is tied to a reproduced failure path and code location.
- **DS-06 (Prioritization Guidance):** Ranks fixes by blast radius (app-wide crashes first).

## Related Prompts

- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - Where error boundaries fit in component architecture
- [frontend_state_management_selection.md](frontend_state_management_selection.md) - Server-cache libraries' built-in error/retry states
- [../react/frontend_react_performance.md](../react/frontend_react_performance.md) - Avoiding re-render storms from retry loops
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Fallback UI and layout stability
