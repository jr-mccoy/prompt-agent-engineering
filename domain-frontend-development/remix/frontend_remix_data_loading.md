---
title: "Remix / React Router Data Loading and Mutations Audit"
category: frontend-development/remix
description: "Audit a Remix (or React Router framework mode) app's data flow — loaders, actions, nested routes, progressive enhancement, error/catch boundaries, and mutation + revalidation — to confirm data lives on routes, forms work without JS, and the UI stays in sync after writes."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - remix
  - react-router
  - loaders-actions
  - nested-routes
  - progressive-enhancement
  - revalidation
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/nextjs/frontend_nextjs_app_router.md
  - domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md
  - domain-frontend-development/react/frontend_react_server_components_streaming.md
  - domain-frontend-development/architecture/frontend_state_management_selection.md
---

# Remix / React Router Data Loading and Mutations Audit

**Objective:** Audit how a Remix (or React Router in framework mode) app loads and mutates data — verifying loaders/actions live on routes, nested routes load data in parallel, forms degrade gracefully without JS, error/catch boundaries are present, and mutations trigger correct revalidation.

**When to Use:**
- Use when: Reviewing a Remix/React Router app for data-flow correctness and request waterfalls
- Use when: Mutations don't refresh the UI, or stale data persists after a write
- Use when: Forms break without JavaScript, or error states render a blank page
- Use when: Migrating from client-side fetching to route loaders/actions
- Don't use when: Comparing Remix vs Next.js for adoption (use a framework-comparison prompt)

## Instructions

1. **Map the Route Tree and Where Data Lives**
   - Inventory routes and confirm data is fetched in route **loaders** (server) rather than in component `useEffect` client fetches.
   - Verify nested routes each declare their own loader so segments load in **parallel**, not in a parent→child waterfall.
   - Confirm loaders return serializable data and that components read it via the typed data hook (verify hook name against current docs).
   - Flag client-side data fetching that duplicates what a loader could provide server-side.

2. **Audit Loaders for Correctness and Efficiency**
   - Check loaders handle auth/redirects server-side (throwing redirect/response) rather than rendering and redirecting on the client.
   - Verify request-scoped data (params, headers, cookies, search params) is read from the loader arguments, not from globals.
   - Look for over-fetching (loading data a segment doesn't use) and N+1 queries inside a single loader.
   - Confirm caching/headers are set where appropriate and that deferred/streamed data (verify the `defer`/streaming API name) is used for slow, non-critical data instead of blocking the whole route.

3. **Audit Actions and Mutations**
   - Confirm writes go through route **actions** invoked by `<Form>`/`useSubmit`/`useFetcher` (verify names), not ad-hoc client `fetch` to a separate API with manual state juggling.
   - Verify actions validate input server-side and return structured errors (field-level) rather than throwing on validation failure.
   - Check that after an action completes, **revalidation** refreshes affected loaders automatically (the default), and that any manual revalidation control is used intentionally (verify API name).
   - Flag optimistic UI that doesn't reconcile with the revalidated server state, and fetchers that mutate without revalidating dependent data.

4. **Verify Progressive Enhancement**
   - Confirm interactive forms use the framework `<Form>` so they submit and work **without JavaScript**, then enhance when JS loads.
   - Flag forms built on raw `onSubmit` + client `fetch` that break with JS disabled or before hydration.
   - Check that navigation, pending states, and links degrade to standard browser behavior when JS is unavailable.
   - Verify pending/optimistic UI uses navigation/fetcher state hooks (verify names) rather than manual loading flags.

5. **Review Error and Catch Boundaries**
   - Confirm routes define error boundaries so a thrown error in a loader/action/render shows a scoped fallback instead of a blank page or whole-app crash.
   - Verify expected error responses (404/403/etc.) are handled distinctly from unexpected errors (verify whether the version uses a unified error boundary or separate catch boundary — flag for verification).
   - Check that boundaries are placed at the right nesting level so only the failing segment falls back, preserving the rest of the layout.
   - Flag routes with loaders/actions but no boundary coverage.

6. **Assess State That Belongs on the Server vs Client**
   - Confirm server data is not duplicated into client state stores that then drift from the loader.
   - Identify genuinely client-only state (UI toggles, ephemeral form state) vs server state that should come from loaders and be revalidated.
   - Flag global client caches reimplementing what route loaders + revalidation already provide.

7. **CRITICAL: Verify findings before reporting**
   - Confirm a "waterfall" is real by checking the route nesting and that a child loader depends on a parent's result vs simply being nested.
   - Before flagging missing revalidation, confirm the mutation path (action vs raw fetch) and the default behavior for that version.
   - Verify any hook/API name (`<Form>`, loader/action signatures, `defer`, revalidation) against current docs; if unsure, label it "verify against current docs."
   - **Confidence level** for each finding:
     - **High Confidence:** Client fetch where a loader belongs, missing boundary, or mutation without revalidation, confirmed in source
     - **Medium Confidence:** Probable waterfall/over-fetch depending on data dependencies
     - **Low Confidence:** Style/organization preference

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag nested loaders as a waterfall — by default sibling/nested loaders run in parallel
- Assume a raw `fetch` is wrong without confirming it isn't a legitimate non-route call
- Recommend client state stores for data that loaders already own
- Invent hook/API names or version-specific behavior; label uncertain APIs "verify against current docs"
- Treat optimistic UI as a bug — flag only when it fails to reconcile with revalidated state
- Assume Remix and Next.js App Router data models are identical
- Report a missing catch boundary without checking whether the version uses a unified error boundary

✅ **DO:**
- Keep data in route loaders and mutations in route actions
- Verify forms use `<Form>` and work without JS, then enhance
- Confirm mutations trigger revalidation so the UI reflects server state
- Place error boundaries to scope failures to the failing segment
- Use deferred/streamed data for slow, non-critical loads
- Distinguish server state (loaders) from genuine client-only state
- Phrase version-specific APIs neutrally and flag for verification

## Expected Output

A data-loading and mutations audit including:
- Route tree and data-location map
- Loader correctness/efficiency findings
- Action/mutation + revalidation review
- Progressive-enhancement assessment
- Error/catch boundary coverage
- Server-vs-client state evaluation
- Prioritized recommendations

### Output Format

```markdown
## Remix Data Loading & Mutations Audit

### Executive Summary
[Data-on-routes posture, PE health, headline findings]

### Route & Data Map
[Table: route | loader? | action? | boundary? | notes]

### Loader Findings
[Waterfalls, over-fetch, auth, deferral]

### Actions & Revalidation
[Mutation path, validation, revalidation]

### Progressive Enhancement
[Form usage, no-JS behavior, pending UI]

### Error/Catch Boundaries
[Coverage and placement]

### Server vs Client State
[Duplication, drift]

### Recommendations
[Prioritized by impact/effort]
```

## Example Output

```markdown
## Remix Data Loading & Mutations Audit

### Executive Summary
Most routes correctly load data in loaders, but the dashboard fetches its widgets in `useEffect` (client waterfall + spinner flash), the "update profile" form uses raw `fetch` so it breaks without JS and never revalidates the profile loader (stale name after save), and three routes with loaders have no error boundary, so a failed loader blanks the whole app. Moving the dashboard to a loader, switching the form to `<Form>`/action, and adding boundaries resolves the correctness issues.

### Route & Data Map

| Route | Loader? | Action? | Boundary? | Notes |
|-------|---------|---------|-----------|-------|
| `routes/_index` | Yes | — | Yes | OK |
| `routes/dashboard` | No (client fetch) | — | No | Move to loader |
| `routes/profile` | Yes | Raw fetch | No | Use `<Form>` + action |
| `routes/posts.$id` | Yes | Yes | Yes | OK |

### Loader Findings

#### Finding 1: Dashboard Fetches Client-Side
- **Severity:** High
- **Confidence:** High
- **Location:** `app/routes/dashboard.tsx`
- **Evidence:**
  ```tsx
  useEffect(() => {
    fetch('/api/widgets').then(r => r.json()).then(setWidgets); // client waterfall
  }, []);
  ```
- **Fix:** Move to a route loader so data arrives with the document:
  ```tsx
  export async function loader() {
    return json({ widgets: await getWidgets() });
  }
  // const { widgets } = useLoaderData<typeof loader>(); // verify hook name
  ```

### Actions & Revalidation

#### Finding 2: Profile Form Skips Action and Revalidation
- **Severity:** High
- **Confidence:** High
- **Location:** `app/routes/profile.tsx`
- **Evidence:**
  ```tsx
  const onSave = async (e) => {
    e.preventDefault();
    await fetch('/api/profile', { method: 'POST', body });
    // no revalidation → loader-provided name stays stale; breaks without JS
  };
  ```
- **Fix:** Use `<Form>` + a route action; default revalidation refreshes the loader:
  ```tsx
  export async function action({ request }) {
    const data = await request.formData();
    const errors = validate(data);
    if (errors) return json({ errors }, { status: 400 });
    await updateProfile(data);
    return redirect('/profile');
  }
  // <Form method="post"> ... </Form>  (verify Form/action names)
  ```

### Progressive Enhancement
- `posts.$id` correctly uses `<Form>` for comments and shows pending state via navigation/fetcher state. The profile form (above) is the one PE gap.

### Error/Catch Boundaries

#### Finding 3: Missing Boundaries on Loader Routes
- **Severity:** Medium
- **Confidence:** High
- **Location:** `dashboard.tsx`, `profile.tsx`
- **Evidence:** Both declare/should declare loaders but export no error boundary; a thrown loader error blanks the app shell.
- **Fix:** Add a scoped error boundary per route so only that segment falls back. (Verify whether this version uses a unified error boundary or a separate catch boundary for expected responses.)

### Server vs Client State
- A Redux slice mirrors the profile loader data and is updated manually after the raw fetch — this is the source of the stale-name drift. Once the form uses an action + revalidation, drop the slice and read from the loader.

### Prioritized Recommendations

#### Critical (This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Convert profile form to `<Form>` + action | Fixes no-JS + stale data | 2 hrs |
| 2 | Move dashboard fetch into a loader | Removes client waterfall | 1.5 hrs |

#### High (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Add error boundaries to loader routes | Scoped failures, no blank app | 1.5 hrs |
| 2 | Remove duplicated profile state from Redux | Stops drift | 1 hr |

#### Patterns to Preserve
- Loaders on index/posts routes with parallel nested loading
- `<Form>` + action with pending state on comments
- Server-side auth/redirect in loaders
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Audit scoped to loaders, actions, nested routes, PE, boundaries, and revalidation.
- **ST-02 (Structured Sequential Instructions):** Route map → loaders → actions → progressive enhancement → boundaries → state → verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates loading, mutation, enhancement, errors, and state together.
- **RT-05 (Evidence-Based Reasoning):** Each finding cites the route/loader/action/form in source.
- **DS-06 (Prioritization Guidance):** Recommendations ranked by impact/effort with confidence levels.

## Related Prompts

- [../nextjs/frontend_nextjs_app_router.md](../nextjs/frontend_nextjs_app_router.md) - Compare with Next.js App Router data conventions
- [../nextjs/frontend_nextjs_data_fetching.md](../nextjs/frontend_nextjs_data_fetching.md) - Server vs client data-fetching strategies
- [../react/frontend_react_server_components_streaming.md](../react/frontend_react_server_components_streaming.md) - Server-first rendering and streaming comparison
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Deciding server state vs client state
