---
title: "Astro Content Collections and Type-Safe Content Audit"
category: frontend-development/astro
description: "Review an Astro project's content collections for schema validation and type safety, content-layer loaders, MDX usage, routing from content, and correct build-time vs request-time data handling."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - astro
  - content-collections
  - type-safety
  - mdx
  - content-layer
  - routing
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/astro/frontend_astro_islands_architecture.md
  - domain-frontend-development/performance/frontend_performance_core_web_vitals.md
  - domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md
  - domain-frontend-development/architecture/frontend_state_management_selection.md
---

# Astro Content Collections and Type-Safe Content Audit

**Objective:** Audit how an Astro site defines, validates, queries, and routes content collections — confirming schemas enforce type safety, loaders are used appropriately, MDX is configured correctly, and data is resolved at the right time (build vs request).

**When to Use:**
- Use when: Reviewing a content-heavy Astro site (blog, docs, marketing) for content modeling quality
- Use when: Schema/type errors surface in content queries or frontmatter drifts from the schema
- Use when: Deciding between local file collections and external content-layer loaders
- Use when: Setting up dynamic routes generated from collection entries
- Don't use when: The content is purely runtime/user-generated with no build-time component (use a data-fetching/backend review instead)

## Instructions

1. **Inventory Collections and Their Definitions**
   - Locate the content config (commonly a `content.config.*` or `src/content/config.*`; verify the current filename/location against docs).
   - List each `defineCollection` entry, its loader/type, and its schema.
   - Note which collections are local Markdown/MDX/JSON/YAML vs sourced via a content-layer loader (file, glob, or external API). Verify loader names against current docs.
   - Confirm whether the project uses the content layer (loader-based) or legacy folder-based collections, and whether the version supports the feature being used — flag for verification.

2. **Audit Schemas for Type Safety**
   - Confirm each collection has a schema (commonly Zod-based) rather than untyped frontmatter.
   - Check required vs optional fields, enums for constrained values (e.g., status, category), defaults, and refinements/transforms (e.g., string→Date).
   - Look for `image()` helper usage so referenced images are validated and optimized; verify the helper name against docs.
   - Verify `reference()` is used for relations between collections (e.g., post → author) instead of raw string IDs.
   - Flag `z.any()`, missing schemas, or schemas that don't match the actual frontmatter in entries.

3. **Review Querying Patterns**
   - Check `getCollection` / `getEntry` usage (verify names against docs) and whether filtering happens in the query callback vs after fetching everything.
   - Confirm draft/unpublished filtering is applied consistently (e.g., excluding `draft: true` in production).
   - Verify sorting (e.g., by date) is stable and timezone-safe.
   - Look for N+1 patterns where related entries are resolved one-by-one in a loop instead of batched.

4. **Evaluate MDX and Rendering**
   - Confirm the MDX integration is installed/configured if `.mdx` is used; verify integration name against docs.
   - Check how entries are rendered (the render/`<Content />` mechanism — verify current API) and that components passed to MDX are tree-shaken / hydrated only when interactive.
   - Watch for heavy interactive components embedded directly in MDX that ship JS on every content page; recommend island directives where appropriate.
   - Confirm headings/TOC, syntax highlighting, and remark/rehype plugins are configured at build time, not re-run client-side.

5. **Check Routing and Build-Time Data Flow**
   - Verify dynamic routes (`[slug].astro` / `[...slug].astro`) generate paths from collections via `getStaticPaths` (static) or handle them on-demand (server mode). Verify the function name against docs.
   - Confirm `getStaticPaths` returns serializable params/props and that the entry is passed through rather than re-queried in the page.
   - Distinguish build-time data (collections, frontmatter) from request-time data (server endpoints/API). Flag content that is fetched at request time when it could be resolved at build for cacheability.
   - Check pagination and tag/category index pages are generated from the collection, not hardcoded.

6. **CRITICAL: Verify findings before reporting**
   - Open the schema and a sample entry to confirm a "missing field" is real and not satisfied by a default or transform.
   - Confirm a flagged query inefficiency actually runs per-request/per-entry rather than once at build.
   - Verify any API name (`getCollection`, `render`, `image()`, `reference()`, loader names) against current docs before asserting it; if unsure, label it "verify against current docs."
   - **Confidence level** for each finding:
     - **High Confidence:** Schema gap or build/runtime misplacement confirmed in source
     - **Medium Confidence:** Likely improvement depending on content scale
     - **Low Confidence:** Modeling/style preference

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag a collection as "untyped" without opening the config to confirm no schema exists
- Assume a specific config filename or API name — verify against current Astro docs
- Treat build-time resolution as a bug; for static content it is the desired behavior
- Recommend `z.any()` or loosening schemas to "fix" validation errors — fix the data or schema instead
- Report MDX components as over-hydrated unless they actually use a client directive
- Claim a draft is leaking without checking the production filter logic
- Invent loader names or content-layer features that may not exist in the project's version

✅ **DO:**
- Confirm each collection's schema and compare it against real entry frontmatter
- Prefer `reference()` for cross-collection relations and `image()` for validated assets
- Push filtering/sorting into the query and resolve relations in batches
- Resolve content at build time when it is static and cacheable
- Recommend island directives only for genuinely interactive MDX components
- Verify route generation uses the collection as the source of truth
- Label any version-specific API or filename as "verify against current docs"

## Expected Output

A content-collections audit including:
- Collection and loader inventory
- Schema/type-safety findings
- Query-pattern review
- MDX and rendering assessment
- Routing and build-time data-flow review
- Prioritized recommendations

### Output Format

```markdown
## Astro Content Collections Audit

### Executive Summary
[Type-safety posture, build-time correctness, headline findings]

### Collection Inventory
[Table: collection | source/loader | schema? | entries]

### Schema & Type Safety
[Per-collection schema findings]

### Query Patterns
[Filtering, drafts, sorting, relations]

### MDX & Rendering
[Integration, components, plugins]

### Routing & Build-Time Data
[getStaticPaths, build vs request time]

### Recommendations
[Prioritized by impact/effort]
```

## Example Output

```markdown
## Astro Content Collections Audit

### Executive Summary
Two of three collections are well-typed, but the `authors` collection has no schema and posts reference authors by raw string ID instead of `reference()`, so a typo silently breaks the byline with no build error. Drafts are filtered on the blog index but not on the tag pages, leaking unpublished posts. MDX is configured correctly. Adding a schema + `reference()` and centralizing the draft filter resolves the correctness issues.

### Collection Inventory

| Collection | Source / Loader | Schema? | Entries |
|------------|-----------------|---------|---------|
| `blog` | Local `.mdx` (glob loader — verify name) | Yes (Zod) | 84 |
| `authors` | Local `.json` | No | 6 |
| `pages` | Local `.md` | Yes (Zod) | 12 |

### Schema & Type Safety

#### Finding 1: `authors` Collection Has No Schema
- **Severity:** High
- **Confidence:** High
- **Location:** content config — `authors` defined without `schema`
- **Evidence:**
  ```ts
  // illustrative — verify API names against current docs
  const authors = defineCollection({
    loader: file('src/data/authors.json'),
    // schema missing → entries are untyped, typos uncaught
  });
  ```
- **Recommendation:**
  ```ts
  const authors = defineCollection({
    loader: file('src/data/authors.json'),
    schema: z.object({
      name: z.string(),
      avatar: z.string().url().optional(),
      twitter: z.string().optional(),
    }),
  });
  ```

#### Finding 2: Posts Reference Authors by Raw String
- **Severity:** High
- **Confidence:** High
- **Location:** `blog` schema
- **Evidence:**
  ```ts
  schema: z.object({
    title: z.string(),
    author: z.string(), // raw id — a typo won't fail the build
    pubDate: z.coerce.date(),
    draft: z.boolean().default(false),
  })
  ```
- **Recommendation:** Use `reference()` so the relation is validated at build:
  ```ts
  author: reference('authors'), // verify helper name against docs
  ```
  Then resolve with `getEntry('authors', post.data.author)`.

### Query Patterns

#### Finding 3: Drafts Leak on Tag Pages
- **Severity:** Medium
- **Confidence:** High
- **Location:** `src/pages/tags/[tag].astro`
- **Evidence:** The blog index filters `!data.draft`, but the tag page does `getCollection('blog')` with no draft filter, so draft posts appear under tags in production.
- **Recommendation:** Centralize the filter:
  ```ts
  export const publishedPosts = async () =>
    (await getCollection('blog')).filter(p =>
      import.meta.env.PROD ? !p.data.draft : true
    );
  ```

### MDX & Rendering
- `@astrojs/mdx` is configured (verify integration name). Syntax highlighting and a remark TOC plugin run at build time. Interactive components inside MDX correctly use `client:visible`. No over-hydration detected.

### Routing & Build-Time Data

| Route | Source | Mechanism | Assessment |
|-------|--------|-----------|------------|
| `/blog/[slug]` | `blog` | `getStaticPaths` | Correct — built from collection |
| `/tags/[tag]` | derived | `getStaticPaths` | Correct, but inherits draft leak |
| `/authors/[id]` | `authors` | hardcoded list | Generate from collection instead |

#### Finding 4: Author Pages Hardcoded
- **Severity:** Low
- **Confidence:** Medium
- **Recommendation:** Generate author routes from `getCollection('authors')` so new authors don't require manual route edits.

### Prioritized Recommendations

#### Critical (This Week)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Add schema to `authors` collection | Catches data errors at build | 30 min |
| 2 | Convert `author` field to `reference()` | Validated byline relation | 45 min |
| 3 | Centralize draft filter; apply on tag pages | Stops draft leak | 30 min |

#### Medium (This Month)
| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Generate author routes from collection | Less manual upkeep | 1 hr |
| 2 | Add `image()` validation to post hero images | Optimized, validated assets | 1 hr |

#### Patterns to Preserve
- Zod schemas on `blog` and `pages`
- Build-time route generation via `getStaticPaths`
- MDX components hydrated only when interactive
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Audit scoped to schemas, loaders, MDX, routing, and build-time data.
- **ST-02 (Structured Sequential Instructions):** Inventory → schemas → queries → MDX → routing → verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Evaluates type safety, query efficiency, rendering, and data timing together.
- **RT-05 (Evidence-Based Reasoning):** Findings cite the schema/config/entry that supports them.
- **DS-06 (Prioritization Guidance):** Recommendations ranked by impact/effort with confidence levels.

## Related Prompts

- [frontend_astro_islands_architecture.md](frontend_astro_islands_architecture.md) - How content data flows into hydrated islands
- [../performance/frontend_performance_core_web_vitals.md](../performance/frontend_performance_core_web_vitals.md) - Performance impact of MDX components and images
- [../nextjs/frontend_nextjs_data_fetching.md](../nextjs/frontend_nextjs_data_fetching.md) - Compare build-time vs request-time data strategies
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - When content needs client-side state vs build-time resolution
