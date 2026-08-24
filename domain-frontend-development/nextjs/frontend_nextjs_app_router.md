---
title: "Next.js App Router Architecture Analysis"
category: frontend-development/nextjs
description: "Analyze Next.js applications using the App Router for server/client component boundaries, routing patterns, layouts, and metadata configuration"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - nextjs
  - app-router
  - server-components
  - react-server-components
  - routing
  - layouts
updated: "2026-03-19"
related_prompts:
  - domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md
  - domain-frontend-development/nextjs/frontend_nextjs_performance.md
  - domain-frontend-development/react/frontend_react_component_patterns.md
  - domain-frontend-development/react/frontend_react_performance.md
---

# Next.js App Router Architecture Analysis

**Objective:** Analyze a Next.js application using the App Router for proper server/client component boundaries, routing patterns, layout architecture, metadata configuration, and adherence to Next.js conventions for optimal performance and developer experience.

**When to Use:**
- Use when: Reviewing existing Next.js App Router applications for architectural improvements
- Use when: Migrating from Pages Router to App Router
- Use when: Auditing server/client component boundaries for performance
- Use when: Evaluating routing, layout, and metadata patterns
- Don't use when: Working with Pages Router only (different patterns apply)

## Instructions

1. **Assess App Router Adoption and Structure**
   - Identify if the app uses App Router, Pages Router, or hybrid
   - Review `app/` directory structure: file conventions (`page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`)
   - Check route groups `(groupName)`, parallel routes `@slot`, and intercepting routes `(.)`, `(..)`, `(..)(..)`
   - Verify `next.config.js` / `next.config.ts` configuration

2. **Analyze Server/Client Component Boundaries**
   - Which components are Server Components (default) vs Client Components (`'use client'`)?
   - Is `'use client'` placed at the right boundary (as low as possible)?
   - Are there unnecessary client components that could be server components?
   - Is data fetched in server components where appropriate?
   - Check for improper patterns:
     - Passing non-serializable props from server to client
     - Importing server-only code in client components
     - Unnecessary `'use client'` on components that don't use browser APIs

3. **Evaluate Data Fetching Patterns**
   - Server-side: `fetch()` in server components, Route Handlers, Server Actions
   - Caching: `fetch` cache options, `revalidatePath()`, `revalidateTag()`
   - Data loading: parallel vs sequential (waterfall detection)
   - Server Actions: form handling, mutations, revalidation
   - Error handling in data fetching

4. **Review Layout and Template Architecture**
   - Root layout configuration (metadata, fonts, global styles)
   - Nested layout composition and shared UI patterns
   - `template.tsx` vs `layout.tsx` usage
   - Loading states: streaming with `loading.tsx` and `<Suspense>`
   - Error boundaries: `error.tsx` placement and error recovery
   - Route-level code organization

5. **CRITICAL: Verify findings before reporting**
   - Check Next.js version for available features
   - Verify that patterns match the project's rendering strategy (SSR, SSG, ISR)
   - Consider the deployment target (Vercel, self-hosted, edge)
   - Test server/client boundary issues in actual builds, not just dev mode
   - **Confidence level** for each finding:
     - **High Confidence**: Clear anti-pattern violating Next.js documentation
     - **Medium Confidence**: Suboptimal but may have context-specific reasons
     - **Low Confidence**: Preference or needs more investigation

6. **Prioritize Recommendations**
   - Rank by impact on performance, UX, and maintainability
   - Consider migration effort for major refactors
   - Separate build-time issues from runtime concerns

## False-Positive Prevention (MUST follow)

**DON'T:**
- Flag all `'use client'` as wrong (interactive components genuinely need it)
- Report missing `loading.tsx` for routes that load instantly
- Criticize Pages Router usage if migration isn't planned
- Assume all data fetching must happen in server components
- Flag route groups as unnecessary complexity without understanding organization needs
- Report missing ISR/caching for pages that need real-time data
- Criticize `fetch` without cache options when the defaults are appropriate

**DO:**
- Check the Next.js version before suggesting features (App Router matured significantly in 14+)
- Consider the deployment platform when evaluating caching strategies
- Verify `'use client'` boundary issues with actual build output
- Account for third-party library limitations (many require client components)
- Test data fetching patterns under realistic conditions
- Evaluate caching strategy in context of data freshness requirements
- Acknowledge valid trade-offs between DX and performance

## Expected Output

A comprehensive App Router analysis including:
- App structure and convention usage assessment
- Server/client component boundary audit
- Data fetching and caching evaluation
- Layout and streaming architecture review
- Prioritized recommendations

### Output Format

```markdown
## Next.js App Router Analysis

### Executive Summary
[High-level assessment]

### App Structure
[Convention usage, route organization]

### Server/Client Boundaries
[Component classification and boundary issues]

### Data Fetching & Caching
[Patterns, waterfalls, caching strategy]

### Layout Architecture
[Layouts, loading, error boundaries]

### Recommendations
[Prioritized improvements]
```

## Example Output

```markdown
## Next.js App Router Analysis

### Executive Summary
The application is on Next.js 14.2 using the App Router with a well-organized route structure. However, `'use client'` is overused — 65% of components are client components when analysis suggests only 30% need to be. This pushes significant JavaScript to the client, inflating bundle size by an estimated 40%. Data fetching has sequential waterfall patterns in 3 key routes, and caching is not configured, causing redundant API calls. Fixing component boundaries and data fetching patterns would significantly improve LCP and TTI.

### App Structure

**Next.js Version:** 14.2.8
**Router:** App Router (100%)
**TypeScript:** Yes, strict mode

```
app/
├── layout.tsx              # Root layout with metadata
├── page.tsx                # Home page
├── loading.tsx             # Global loading
├── error.tsx               # Global error boundary
├── not-found.tsx           # Custom 404
├── (marketing)/            # Route group - marketing pages
│   ├── layout.tsx          # Marketing layout (no nav)
│   ├── about/page.tsx
│   ├── pricing/page.tsx
│   └── blog/
│       ├── page.tsx        # Blog list
│       └── [slug]/page.tsx # Blog detail
├── (app)/                  # Route group - authenticated app
│   ├── layout.tsx          # App layout (with sidebar)
│   ├── dashboard/
│   │   ├── page.tsx
│   │   ├── loading.tsx
│   │   └── analytics/page.tsx
│   ├── projects/
│   │   ├── page.tsx
│   │   ├── [id]/
│   │   │   ├── page.tsx
│   │   │   ├── settings/page.tsx
│   │   │   └── layout.tsx
│   │   └── new/page.tsx
│   └── settings/
│       ├── page.tsx
│       └── profile/page.tsx
└── api/
    ├── auth/[...nextauth]/route.ts
    ├── projects/route.ts
    └── webhooks/stripe/route.ts
```

**Convention Usage:**

| Convention | Used | Assessment |
|------------|------|------------|
| `page.tsx` | All routes | Good |
| `layout.tsx` | Root + 3 nested | Good |
| `loading.tsx` | 2 routes | Partial - missing on slow routes |
| `error.tsx` | Root only | Needs route-level error boundaries |
| `not-found.tsx` | Root only | Good |
| Route groups | 2 `(marketing)`, `(app)` | Good organization |
| Dynamic routes | `[slug]`, `[id]` | Good |
| Route Handlers | 3 API routes | Good |
| Parallel routes | None | Could benefit dashboard |
| Intercepting routes | None | Not needed currently |

### Server/Client Boundary Analysis

**Current distribution:**
| Type | Count | Percentage |
|------|-------|------------|
| Server Components | 12 | 35% |
| Client Components (`'use client'`) | 22 | 65% |

**Recommended distribution:**
| Type | Count | Percentage |
|------|-------|------------|
| Server Components | 24 | 70% |
| Client Components | 10 | 30% |

#### Issue 1: Unnecessary `'use client'` on Data Display Components
- **Severity:** High
- **Confidence:** High
- **Found:** 12 components that are client-side but don't use browser APIs
- **Evidence:**
  ```typescript
  // app/(app)/projects/[id]/page.tsx
  'use client';  // WHY? This component only fetches and displays data

  import { useEffect, useState } from 'react';

  export default function ProjectPage({ params }: { params: { id: string } }) {
    const [project, setProject] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
      fetch(`/api/projects/${params.id}`)
        .then(res => res.json())
        .then(data => {
          setProject(data);
          setLoading(false);
        });
    }, [params.id]);

    if (loading) return <ProjectSkeleton />;
    return <ProjectDetail project={project} />;
  }
  ```
- **Impact:** Sends component JS to browser, prevents streaming, loses RSC benefits
- **Recommendation:** Convert to Server Component:
  ```typescript
  // app/(app)/projects/[id]/page.tsx
  // No 'use client' needed - this is a Server Component
  import { notFound } from 'next/navigation';

  async function getProject(id: string) {
    const res = await fetch(`${process.env.API_URL}/projects/${id}`, {
      next: { tags: [`project-${id}`] },
    });
    if (!res.ok) return null;
    return res.json();
  }

  export default async function ProjectPage({
    params,
  }: {
    params: Promise<{ id: string }>;
  }) {
    const { id } = await params;
    const project = await getProject(id);
    if (!project) notFound();

    return <ProjectDetail project={project} />;
  }
  ```

#### Issue 2: `'use client'` Boundary Too High
- **Severity:** Medium
- **Confidence:** High
- **Location:** `app/(app)/dashboard/page.tsx`
- **Evidence:**
  ```typescript
  'use client';  // Entire page is client component

  export default function DashboardPage() {
    return (
      <div>
        <h1>Dashboard</h1>
        <StatsOverview />    {/* Static - could be server */}
        <RecentActivity />   {/* Static - could be server */}
        <QuickActions />     {/* Interactive - needs client */}
        <NotificationBell /> {/* Interactive - needs client */}
      </div>
    );
  }
  ```
- **Recommendation:** Push `'use client'` to the interactive leaf components:
  ```typescript
  // app/(app)/dashboard/page.tsx - Server Component
  import { Suspense } from 'react';

  export default function DashboardPage() {
    return (
      <div>
        <h1>Dashboard</h1>
        <Suspense fallback={<StatsSkeleton />}>
          <StatsOverview />    {/* Server Component - fetches data */}
        </Suspense>
        <Suspense fallback={<ActivitySkeleton />}>
          <RecentActivity />   {/* Server Component - fetches data */}
        </Suspense>
        <QuickActions />       {/* 'use client' inside this component */}
        <NotificationBell />   {/* 'use client' inside this component */}
      </div>
    );
  }
  ```

### Data Fetching & Caching Analysis

#### Issue 3: Sequential Data Fetching Waterfall
- **Severity:** High
- **Confidence:** High
- **Location:** `app/(app)/dashboard/page.tsx` (after conversion to server component)
- **Evidence:**
  ```typescript
  // Sequential fetches - each waits for the previous
  export default async function DashboardPage() {
    const stats = await getStats();          // 200ms
    const activity = await getActivity();    // 300ms
    const projects = await getProjects();    // 250ms
    // Total: 750ms (sequential)

    return (
      <div>
        <StatsOverview stats={stats} />
        <RecentActivity activity={activity} />
        <ProjectList projects={projects} />
      </div>
    );
  }
  ```
- **Fix:** Parallel fetching with `Promise.all` or Suspense streaming:
  ```typescript
  // Option A: Promise.all (parallel, single loading state)
  export default async function DashboardPage() {
    const [stats, activity, projects] = await Promise.all([
      getStats(),       // 200ms
      getActivity(),    // 300ms
      getProjects(),    // 250ms
    ]);
    // Total: 300ms (parallel)

    return (
      <div>
        <StatsOverview stats={stats} />
        <RecentActivity activity={activity} />
        <ProjectList projects={projects} />
      </div>
    );
  }

  // Option B: Suspense streaming (parallel, independent loading states)
  export default function DashboardPage() {
    return (
      <div>
        <Suspense fallback={<StatsSkeleton />}>
          <StatsOverview />   {/* Each fetches its own data */}
        </Suspense>
        <Suspense fallback={<ActivitySkeleton />}>
          <RecentActivity />
        </Suspense>
        <Suspense fallback={<ProjectsSkeleton />}>
          <ProjectList />
        </Suspense>
      </div>
    );
  }
  ```
- **Impact:** 60% faster page load (750ms → 300ms)

#### Issue 4: No Caching Strategy
- **Severity:** Medium
- **Confidence:** High
- **Evidence:** All `fetch()` calls use defaults without explicit caching:
  ```typescript
  // No cache configuration - relies on defaults
  const res = await fetch(`${API_URL}/projects`);
  ```
- **Recommendation:** Add explicit caching with tags for targeted revalidation:
  ```typescript
  // Static data: cache indefinitely, revalidate on demand
  const res = await fetch(`${API_URL}/projects`, {
    next: { tags: ['projects'] },
  });

  // Time-based revalidation (ISR)
  const res = await fetch(`${API_URL}/stats`, {
    next: { revalidate: 60 },  // Revalidate every 60 seconds
  });

  // Dynamic data: no cache
  const res = await fetch(`${API_URL}/notifications`, {
    cache: 'no-store',
  });

  // Revalidate in Server Action after mutation
  'use server';
  async function createProject(formData: FormData) {
    await db.projects.create({ ... });
    revalidateTag('projects');       // Revalidate project list
    revalidatePath('/dashboard');    // Revalidate dashboard
  }
  ```

### Layout Architecture

#### Issue 5: Missing Loading States on Slow Routes
- **Severity:** Medium
- **Confidence:** Medium
- **Location:** `app/(app)/projects/[id]/page.tsx`, `app/(app)/dashboard/analytics/page.tsx`
- **Evidence:** These routes fetch data but have no `loading.tsx` or `<Suspense>` boundaries, causing a blank screen during data loading.
- **Recommendation:**
  ```typescript
  // app/(app)/projects/[id]/loading.tsx
  export default function ProjectLoading() {
    return (
      <div className="animate-pulse">
        <div className="h-8 bg-gray-200 rounded w-1/3 mb-4" />
        <div className="h-4 bg-gray-200 rounded w-2/3 mb-2" />
        <div className="h-4 bg-gray-200 rounded w-1/2 mb-2" />
        <div className="h-64 bg-gray-200 rounded mt-6" />
      </div>
    );
  }
  ```

### Metadata and SEO

| Page | `metadata` / `generateMetadata` | Assessment |
|------|---------------------------------|------------|
| Root layout | Static metadata | Good |
| Blog `[slug]` | `generateMetadata` | Good - dynamic titles |
| Project `[id]` | Missing | Needs dynamic metadata |
| Marketing pages | Static | Good |

**Recommendation for missing dynamic metadata:**
```typescript
// app/(app)/projects/[id]/page.tsx
export async function generateMetadata({
  params,
}: {
  params: Promise<{ id: string }>;
}): Promise<Metadata> {
  const { id } = await params;
  const project = await getProject(id);

  return {
    title: project?.name ?? 'Project Not Found',
    description: project?.description,
  };
}
```

### Prioritized Recommendations

#### Quick Wins (< 1 day each)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Convert 12 data-display components to Server Components | 40% less client JS | 4-6 hours |
| 2 | Add `Promise.all` for parallel data fetching | 60% faster loads | 2 hours |
| 3 | Add `loading.tsx` for 3 slow routes | Better perceived performance | 1 hour |
| 4 | Add cache tags to fetch calls | Efficient revalidation | 2 hours |

#### Major Refactors (> 1 week each)
| # | Action | Impact | Effort | Dependencies |
|---|--------|--------|--------|--------------|
| 1 | Push `'use client'` boundaries to leaf components | Maximize RSC benefits | 1 week | Identify interactive leaves |
| 2 | Implement Suspense streaming for dashboard | Progressive loading | 3 days | Server component migration |
| 3 | Add `generateMetadata` for all dynamic routes | SEO improvement | 2 days | None |

### Patterns to Preserve
- **Route group organization**: `(marketing)` and `(app)` cleanly separate concerns
- **Route Handlers for API**: Proper `/api` routes for external integrations
- **Root error boundary**: Good foundation for error handling
- **Dynamic routes**: Proper use of `[slug]` and `[id]` conventions
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Focused on App Router architecture
- **ST-02 (Structured Sequential Instructions):** Systematic review of Next.js patterns
- **RT-02 (Multi-Dimensional Analysis):** Covers components, data, caching, layouts
- **RT-05 (Evidence-Based Reasoning):** Code evidence for each finding
- **DS-06 (Prioritization Guidance):** Impact/effort ranking for recommendations

## Related Prompts

- [frontend_nextjs_data_fetching.md](frontend_nextjs_data_fetching.md) - Data fetching and caching deep dive
- [frontend_nextjs_performance.md](frontend_nextjs_performance.md) - Performance optimization
- [../react/frontend_react_component_patterns.md](../react/frontend_react_component_patterns.md) - React patterns (Next.js builds on React)
- [../react/frontend_react_performance.md](../react/frontend_react_performance.md) - React performance

## Customization Guide

- **For Pages Router Migration**: Focus on incremental adoption with `/app` alongside `/pages`
- **For Vercel Deployment**: Leverage edge runtime, ISR, and image optimization features
- **For Self-Hosted**: Emphasize `output: 'standalone'`, Docker considerations, caching without CDN
- **For E-commerce**: Focus on product page ISR, cart client components, checkout Server Actions
- **For SaaS Dashboard**: Emphasize Suspense streaming, parallel routes for modals, route groups for auth
