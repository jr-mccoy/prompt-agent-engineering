---
title: "SvelteKit Full-Stack Patterns Analysis"
category: frontend-development/svelte
description: "Analyze SvelteKit applications for routing, load functions, form actions, server hooks, and full-stack architecture patterns"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - sveltekit
  - routing
  - load-functions
  - form-actions
  - server-hooks
  - ssr
updated: "2026-03-19"
related_prompts:
  - domain-frontend-development/svelte/frontend_svelte_component_patterns.md
  - domain-frontend-development/svelte/frontend_svelte_state_management.md
  - domain-frontend-development/nextjs/frontend_nextjs_app_router.md
---

# SvelteKit Full-Stack Patterns Analysis

**Objective:** Analyze a SvelteKit application for proper use of routing conventions, load functions, form actions, server hooks, and full-stack architecture patterns, identifying opportunities to improve data flow, security, and performance.

**When to Use:**
- Use when: Reviewing existing SvelteKit applications for architectural improvements
- Use when: Auditing data loading patterns for correctness and performance
- Use when: Evaluating form handling and mutation patterns
- Use when: Assessing server-side security (hooks, auth, validation)
- Don't use when: Working with standalone Svelte (no SvelteKit)

## Instructions

1. **Assess Route Architecture**
   - Review `src/routes/` structure and organization
   - Check file convention usage: `+page.svelte`, `+page.ts`, `+page.server.ts`, `+layout.svelte`, `+layout.ts`, `+layout.server.ts`, `+server.ts`, `+error.svelte`
   - Route groups `(group)` organization
   - Dynamic routes `[param]`, rest parameters `[...rest]`, optional parameters `[[optional]]`
   - Route-level configuration (`+page.ts`: `export const ssr`, `prerender`, `csr`)

2. **Analyze Load Functions**
   - Universal load (`+page.ts`) vs server load (`+page.server.ts`)
   - Data flow from load functions to page components
   - Parallel vs sequential data loading
   - Error handling in load functions
   - Dependency tracking and invalidation
   - Parent data access with `await parent()`
   - Streaming with promises in load functions

3. **Evaluate Form Actions**
   - Default and named actions in `+page.server.ts`
   - Form validation patterns (server-side + client-side)
   - Progressive enhancement: do forms work without JS?
   - `use:enhance` customization
   - Redirect and error handling after actions
   - File upload handling

4. **Review Server-Side Patterns**
   - `hooks.server.ts`: authentication, logging, CSRF protection
   - API routes (`+server.ts`): REST endpoint patterns
   - Environment variable usage (`$env/static/private`, `$env/dynamic/private`)
   - Server-only modules (`$lib/server/`)
   - Cookie and session management

5. **CRITICAL: Verify findings before reporting**
   - Test load functions with both SSR and CSR navigation
   - Verify form actions work with and without JavaScript
   - Check that server-only code doesn't leak to the client
   - Test error boundaries at route level
   - **Confidence level** for each finding:
     - **High Confidence**: Security issue or clear bug with evidence
     - **Medium Confidence**: Suboptimal pattern likely causing problems
     - **Low Confidence**: Style or architecture preference

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag universal load functions as wrong (they're needed for client-side navigation)
- Report missing `+page.server.ts` when `+page.ts` is sufficient
- Criticize `+server.ts` API routes when they serve external clients
- Assume all forms need `use:enhance` (progressive enhancement is a spectrum)
- Flag `export const prerender = false` as wrong for genuinely dynamic pages
- Report `fetch` in load functions as redundant (SvelteKit deduplicates)
- Suggest moving all logic to server-only without considering client navigation

**DO:**
- Verify sensitive data isn't exposed through universal load functions
- Test that forms degrade gracefully without JavaScript
- Check that `+page.server.ts` is used when accessing databases or secrets
- Consider the trade-off between SSR and client-side navigation
- Verify that error boundaries exist for routes that can fail
- Check adapter configuration matches deployment target
- Test load function behavior during both initial SSR and client navigation

## Expected Output

A comprehensive SvelteKit analysis including:
- Route architecture assessment
- Load function audit
- Form action patterns review
- Server-side security evaluation
- Prioritized recommendations

### Output Format

```markdown
## SvelteKit Full-Stack Analysis

### Route Architecture
[Structure, conventions, organization]

### Load Functions
[Data loading patterns, performance, correctness]

### Form Actions
[Mutation patterns, validation, progressive enhancement]

### Server-Side Security
[Hooks, auth, data exposure]

### Recommendations
[Prioritized improvements]
```

## Example Output

```markdown
## SvelteKit Full-Stack Analysis

### Executive Summary
The SvelteKit application has a well-organized route structure with 24 routes, but load function patterns are inconsistent: 5 routes use universal loads that expose sensitive data to the client, 3 routes have waterfall data loading, and form actions lack server-side validation in 4 cases. The `hooks.server.ts` authentication check has a bypass vulnerability. Fixing the security issues and standardizing load patterns would significantly improve both security and UX.

### Route Architecture

**SvelteKit Version:** 2.8.1
**Adapter:** @sveltejs/adapter-node
**Routes:** 24

```
src/routes/
├── +layout.svelte           # Root layout (nav, footer)
├── +layout.server.ts        # Auth check, user data
├── +page.svelte             # Home page
├── +error.svelte            # Global error page
├── (auth)/                  # Auth route group (no layout)
│   ├── login/
│   │   ├── +page.svelte
│   │   └── +page.server.ts  # Login action
│   ├── register/
│   │   ├── +page.svelte
│   │   └── +page.server.ts  # Register action
│   └── +layout.svelte       # Auth layout (centered card)
├── (app)/                   # Authenticated app
│   ├── +layout.svelte       # App layout (sidebar)
│   ├── +layout.server.ts    # Verify auth, load user
│   ├── dashboard/
│   │   ├── +page.svelte
│   │   └── +page.ts         # ⚠️ Universal load
│   ├── projects/
│   │   ├── +page.svelte
│   │   ├── +page.server.ts
│   │   ├── [id]/
│   │   │   ├── +page.svelte
│   │   │   ├── +page.ts     # ⚠️ Universal load
│   │   │   ├── settings/
│   │   │   │   ├── +page.svelte
│   │   │   │   └── +page.server.ts
│   │   │   └── +layout.svelte
│   │   └── new/
│   │       ├── +page.svelte
│   │       └── +page.server.ts
│   └── settings/
│       ├── +page.svelte
│       └── +page.server.ts
├── api/
│   ├── webhooks/stripe/+server.ts
│   └── health/+server.ts
└── blog/
    ├── +page.svelte
    ├── +page.ts
    └── [slug]/
        ├── +page.svelte
        └── +page.ts
```

**Convention Usage:**

| Convention | Count | Assessment |
|------------|-------|------------|
| `+page.svelte` | 14 | All routes have pages |
| `+page.server.ts` (server load + actions) | 7 | Good for mutations |
| `+page.ts` (universal load) | 5 | 3 should be server-only |
| `+layout.svelte` | 5 | Good hierarchy |
| `+layout.server.ts` | 2 | Auth check pattern |
| `+server.ts` (API routes) | 2 | Appropriate for webhooks |
| `+error.svelte` | 1 (root only) | Needs route-level errors |
| Route groups | 2 | Good organization |

### Load Function Analysis

#### Issue 1: Sensitive Data in Universal Load
- **Severity:** Critical (Security)
- **Confidence:** High
- **Location:** `src/routes/(app)/dashboard/+page.ts`
- **Evidence:**
  ```typescript
  // +page.ts - Universal load, runs on BOTH server and client
  import type { PageLoad } from './$types';

  export const load: PageLoad = async ({ fetch }) => {
    const res = await fetch('/api/dashboard');
    const data = await res.json();

    return {
      stats: data.stats,
      revenue: data.revenue,       // Sensitive financial data
      apiKeys: data.apiKeys,       // API keys exposed to client!
      internalNotes: data.notes,   // Internal notes visible in network tab
    };
  };
  ```
- **Impact:** Universal load data is serialized and sent to the client. API keys and internal data are visible in the page HTML source and network tab.
- **Fix:** Move to server load:
  ```typescript
  // +page.server.ts - Server-only load, data never sent raw to client
  import type { PageServerLoad } from './$types';
  import { db } from '$lib/server/database';

  export const load: PageServerLoad = async ({ locals }) => {
    const user = locals.user;

    const [stats, revenue] = await Promise.all([
      db.stats.get(user.orgId),
      db.revenue.get(user.orgId),
    ]);

    return {
      stats,
      revenue: revenue.summary,  // Only return what the UI needs
      // apiKeys and internalNotes stay server-side
    };
  };
  ```

#### Issue 2: Waterfall Data Loading
- **Severity:** High
- **Confidence:** High
- **Location:** `src/routes/(app)/projects/[id]/+page.ts`
- **Evidence:**
  ```typescript
  export const load: PageLoad = async ({ fetch, params }) => {
    // Sequential - each fetch waits for the previous
    const project = await fetch(`/api/projects/${params.id}`).then(r => r.json());
    const members = await fetch(`/api/projects/${params.id}/members`).then(r => r.json());
    const activity = await fetch(`/api/projects/${params.id}/activity`).then(r => r.json());
    // Total: sum of all three response times

    return { project, members, activity };
  };
  ```
- **Fix:**
  ```typescript
  // Option A: Promise.all for parallel loading
  export const load: PageServerLoad = async ({ params }) => {
    const id = params.id;

    const [project, members, activity] = await Promise.all([
      db.projects.get(id),
      db.projectMembers.list(id),
      db.projectActivity.recent(id),
    ]);

    return { project, members, activity };
  };

  // Option B: Streaming with deferred data
  export const load: PageServerLoad = async ({ params }) => {
    const id = params.id;

    const project = await db.projects.get(id);  // Critical, await

    return {
      project,
      // These stream in after initial render
      members: db.projectMembers.list(id),      // Promise, not awaited
      activity: db.projectActivity.recent(id),  // Promise, not awaited
    };
  };
  ```

  **Streaming usage in component:**
  ```svelte
  <!-- +page.svelte -->
  <script>
    let { data } = $props();
  </script>

  <ProjectHeader project={data.project} />

  {#await data.members}
    <MembersSkeleton />
  {:then members}
    <MembersList {members} />
  {/await}

  {#await data.activity}
    <ActivitySkeleton />
  {:then activity}
    <ActivityFeed {activity} />
  {/await}
  ```

#### Issue 3: Missing `depends()` for Invalidation
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** `src/routes/(app)/projects/+page.server.ts`
- **Evidence:** After creating a new project, the project list doesn't update until full page refresh
- **Fix:**
  ```typescript
  // +page.server.ts
  export const load: PageServerLoad = async ({ depends }) => {
    depends('app:projects');  // Register custom dependency

    const projects = await db.projects.list();
    return { projects };
  };

  // In the create action or a component:
  import { invalidate } from '$app/navigation';
  await invalidate('app:projects');  // Triggers reload of dependent loads
  ```

### Form Actions Analysis

#### Issue 4: Missing Server-Side Validation
- **Severity:** High
- **Confidence:** High
- **Found:** 4 form actions with no server validation
- **Location:** `src/routes/(app)/projects/new/+page.server.ts`
- **Evidence:**
  ```typescript
  export const actions = {
    default: async ({ request, locals }) => {
      const data = await request.formData();
      const name = data.get('name') as string;
      const description = data.get('description') as string;

      // No validation! Directly inserting user input
      const project = await db.projects.create({
        name,           // Could be empty, too long, contain malicious content
        description,    // No sanitization
        ownerId: locals.user.id,
      });

      redirect(303, `/projects/${project.id}`);
    }
  };
  ```
- **Fix:**
  ```typescript
  import { fail, redirect } from '@sveltejs/kit';
  import { z } from 'zod';

  const createProjectSchema = z.object({
    name: z.string().min(1, 'Name is required').max(100, 'Name too long').trim(),
    description: z.string().max(1000).trim().optional(),
  });

  export const actions = {
    default: async ({ request, locals }) => {
      const formData = await request.formData();
      const rawData = Object.fromEntries(formData);

      const result = createProjectSchema.safeParse(rawData);
      if (!result.success) {
        return fail(400, {
          data: rawData,
          errors: result.error.flatten().fieldErrors,
        });
      }

      const project = await db.projects.create({
        ...result.data,
        ownerId: locals.user.id,
      });

      redirect(303, `/projects/${project.id}`);
    }
  };
  ```

  **With progressive enhancement in the form:**
  ```svelte
  <!-- +page.svelte -->
  <script>
    import { enhance } from '$app/forms';

    let { form } = $props();
  </script>

  <form method="POST" use:enhance>
    <label>
      Project Name
      <input name="name" value={form?.data?.name ?? ''} />
      {#if form?.errors?.name}
        <span class="error">{form.errors.name[0]}</span>
      {/if}
    </label>

    <label>
      Description
      <textarea name="description">{form?.data?.description ?? ''}</textarea>
      {#if form?.errors?.description}
        <span class="error">{form.errors.description[0]}</span>
      {/if}
    </label>

    <button type="submit">Create Project</button>
  </form>
  ```

#### Issue 5: `use:enhance` Without Loading State
- **Severity:** Low
- **Confidence:** Medium
- **Found:** 3 forms with `use:enhance` but no submission feedback
- **Recommendation:**
  ```svelte
  <script>
    import { enhance } from '$app/forms';
    let submitting = $state(false);
  </script>

  <form method="POST" use:enhance={() => {
    submitting = true;
    return async ({ update }) => {
      await update();
      submitting = false;
    };
  }}>
    <button type="submit" disabled={submitting}>
      {submitting ? 'Saving...' : 'Save'}
    </button>
  </form>
  ```

### Server-Side Security

#### Issue 6: Auth Hook Bypass
- **Severity:** Critical (Security)
- **Confidence:** High
- **Location:** `src/hooks.server.ts`
- **Evidence:**
  ```typescript
  export const handle: Handle = async ({ event, resolve }) => {
    const session = event.cookies.get('session');

    if (session) {
      const user = await verifySession(session);
      event.locals.user = user;
    }

    // Missing: no check that protected routes require auth!
    // Anyone can access /dashboard, /projects, etc. without a session
    return resolve(event);
  };
  ```
- **Fix:**
  ```typescript
  export const handle: Handle = async ({ event, resolve }) => {
    const session = event.cookies.get('session');

    if (session) {
      try {
        const user = await verifySession(session);
        event.locals.user = user;
      } catch {
        event.cookies.delete('session', { path: '/' });
      }
    }

    // Protect authenticated routes
    if (event.url.pathname.startsWith('/(app)') ||
        event.route.id?.startsWith('/(app)')) {
      if (!event.locals.user) {
        redirect(303, '/login');
      }
    }

    return resolve(event);
  };
  ```
  Or better, use the layout server load:
  ```typescript
  // src/routes/(app)/+layout.server.ts
  export const load: LayoutServerLoad = async ({ locals }) => {
    if (!locals.user) {
      redirect(303, '/login');
    }
    return { user: locals.user };
  };
  ```

### Prioritized Recommendations

#### Critical (Fix Immediately)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Fix auth hook bypass | Security vulnerability | 1 hour |
| 2 | Move sensitive data to server loads | Data exposure risk | 2 hours |
| 3 | Add server-side validation to 4 form actions | Input validation | 3 hours |

#### High Priority (This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Parallelize waterfall load functions | 50%+ faster page loads | 2 hours |
| 2 | Add `depends()` for proper invalidation | Fix stale data after mutations | 1 hour |
| 3 | Add route-level `+error.svelte` for app routes | Better error handling | 2 hours |

#### Medium Priority (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Implement streaming for non-critical data | Progressive loading | 4 hours |
| 2 | Add loading states to enhanced forms | Better UX | 2 hours |
| 3 | Add `prerender` to blog and marketing pages | Faster static pages | 1 hour |
| 4 | Add CSRF protection in hooks | Security hardening | 2 hours |

### Patterns to Preserve
- **Route group organization**: Clean separation of auth and app routes
- **Layout hierarchy**: Proper nesting of layouts for shared UI
- **Progressive enhancement**: Forms work without JS (mostly)
- **Server loads for mutations**: Actions properly placed in `+page.server.ts`
- **Adapter configuration**: Correct adapter for deployment target
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on SvelteKit full-stack patterns
- **ST-02 (Structured Sequential Instructions):** Systematic review of SvelteKit layers
- **RT-02 (Multi-Dimensional Analysis):** Covers routing, data loading, actions, security
- **RT-05 (Evidence-Based Reasoning):** Code evidence for each finding
- **DS-06 (Prioritization Guidance):** Security-first prioritization

## Related Prompts

- [frontend_svelte_component_patterns.md](frontend_svelte_component_patterns.md) - Svelte component patterns
- [frontend_svelte_state_management.md](frontend_svelte_state_management.md) - State management
- [../nextjs/frontend_nextjs_app_router.md](../nextjs/frontend_nextjs_app_router.md) - Similar full-stack analysis for Next.js

## Customization Guide

- **For Static Sites**: Focus on `prerender`, adapter-static, and build-time data loading
- **For Edge Deployment**: Evaluate adapter-cloudflare/vercel, edge-compatible data sources
- **For API-First**: Emphasize `+server.ts` route handlers, REST conventions
- **For Auth-Heavy Apps**: Focus on hooks, session management, and route protection
- **For Migration from Next.js**: Compare load functions to getServerSideProps, actions to API routes
