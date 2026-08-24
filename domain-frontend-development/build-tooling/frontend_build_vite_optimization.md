---
title: "Vite Build Configuration Audit & Optimization"
category: frontend-development/build-tooling
description: "Audit a Vite project's configuration and optimize dev server performance, build splitting, dependency pre-bundling, plugins, env handling, SSR builds, and bundle analysis."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - vite
  - build-tooling
  - bundling
  - rollup
  - dependency-pre-bundling
  - ssr
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/build-tooling/frontend_build_bundler_migration.md
  - domain-frontend-development/build-tooling/frontend_build_micro_frontends_module_federation.md
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
  - domain-frontend-development/nextjs/frontend_nextjs_performance.md
---

# Vite Build Configuration Audit & Optimization

**Objective:** Systematically audit a Vite project's configuration to identify dev-server friction, build inefficiencies, and misconfigured plugins/dependencies, then recommend evidence-backed optimizations across dev, production, and SSR builds.

**When to Use:**
- Use when: The Vite dev server is slow to start or has sluggish HMR on large codebases.
- Use when: Production builds are slow, produce poorly-split chunks, or ship unexpected vendor weight.
- Use when: Setting up SSR/SSG with Vite and need a correct `ssr` build + externalization strategy.
- Don't use when: The project does not use Vite — for migrating off another bundler, use `frontend_build_bundler_migration.md` instead.

## Instructions

1. **Inventory the Vite Setup**
   - Locate and read `vite.config.{js,ts,mjs}`, including any conditional `mode`/`command` branches and merged configs.
   - Record the declared Vite version, plugins, and framework integration (React, Vue, Svelte, etc.). Treat version-specific feature availability as something to verify against current docs, not assert from memory.
   - Note `root`, `base`, `publicDir`, `resolve.alias`, and any monorepo workspace layout.

2. **Audit the Dev Server & HMR**
   - Review `optimizeDeps` (`include`, `exclude`, `entries`, `force`) — esbuild dependency pre-bundling is the main lever for cold-start and HMR speed.
   - Look for dependencies that are large, CommonJS, or deeply nested and may benefit from explicit `include`; look for ESM-friendly local packages that should be `exclude`d.
   - Check `server` options (`warmup`, `fs.allow`, `watch` ignores, proxy) and whether source maps or plugins add per-request overhead.

3. **Audit the Production Build (Rollup output)**
   - Review `build.target`, `build.minify`, `build.sourcemap`, `build.cssCodeSplit`, and `build.assetsInlineLimit`.
   - Inspect `build.rollupOptions.output.manualChunks` (or function form) for vendor/route splitting; flag over-splitting (request waterfalls) and under-splitting (monolithic vendor chunk).
   - Verify tree-shaking prerequisites: ESM imports, correct `sideEffects`, no accidental barrel-file bloat.

4. **Audit Plugins, Env, and Assets**
   - Map each plugin to a justification; flag redundant, overlapping, or order-sensitive plugins (plugin order affects transforms).
   - Review env handling: `import.meta.env`, `envPrefix`, `define`, and the boundary between public (`VITE_`-prefixed) and secret values. Flag any secret exposed to the client bundle.
   - Review asset handling, `worker` config, and any legacy/polyfill plugin against the declared browser target.

5. **Audit SSR / SSG Build (if applicable)**
   - Confirm a separate `ssr` build entry and correct `ssr.noExternal` / `ssr.external` boundaries.
   - Check for code that assumes a browser/global at module top-level (will break in the SSR build).
   - Verify the manifest/`ssrManifest` wiring used for preloading client assets.

6. **CRITICAL: Verify each finding before reporting**
   - Tie every claim to a concrete config line, build artifact, or measurable signal — never to a remembered benchmark or a Vite version number you have not confirmed.
   - For each finding, state evidence and a confidence level:
     - **High Confidence:** Backed by the actual config + a reproducible build/analyzer output or error.
     - **Medium Confidence:** Inferred from config patterns; not yet measured in this project.
     - **Low Confidence:** Plausible based on general Vite behavior; explicitly flagged "verify against current docs / measure locally."

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Assert specific build-time or HMR numbers ("3x faster", "starts in 200ms") without a measurement from this project.
- Add packages to `optimizeDeps.include` without evidence they are causing pre-bundling churn or full reloads.
- Recommend `manualChunks` splits without checking the actual dependency graph — arbitrary splits cause request waterfalls.
- Assume a plugin is required just because it is present; confirm it is referenced by the build.
- Treat `define`/`import.meta.env` replacements as safe for secrets — anything inlined reaches the client.
- Copy a `vite.config` snippet that targets a different Vite major version without flagging the version dependency.

✅ **DO:**
- Read the real `vite.config` and `package.json` and quote the exact lines you are reacting to.
- Run (or instruct the user to run) the bundle analyzer (e.g. `rollup-plugin-visualizer`) and reason from its output.
- Separate dev-server findings from production-build findings — they have different levers.
- Verify the browser `build.target` matches the project's actual support matrix before touching polyfills/legacy.
- Preserve SSR/CSR boundaries when recommending externalization changes.
- Phrase version-sensitive guidance as "verify against current Vite/Rollup docs."

## Expected Output

A structured Vite configuration audit containing:
- A snapshot of the current setup (version, plugins, framework, build mode).
- Findings grouped by surface (dev server, production build, plugins/env, SSR), each with severity, confidence, evidence, and a recommendation.
- A prioritized remediation plan separating quick wins from larger refactors.
- Concrete config diffs/snippets, flagged where they are version-sensitive.

### Output Format

```markdown
## Vite Configuration Audit

### Current Setup
[Version, framework, plugins, build mode]

### Findings
[Grouped by surface — each with Severity / Confidence / Evidence / Recommendation]

### Recommended Config Changes
[Concrete snippets with version caveats]

### Prioritized Remediation Plan
[Quick wins → structural changes]
```

## Example Output

```markdown
## Vite Configuration Audit

### Current Setup

| Attribute | Value |
|-----------|-------|
| Vite version | 5.x (verify exact patch against lockfile) |
| Framework | React 18 (`@vitejs/plugin-react`) |
| Build mode | SPA, single client build |
| Plugins | react, legacy, svgr, visualizer (dev only) |
| Notable config | `manualChunks` not set; `optimizeDeps` default |

**Headline:** Dev server cold start is dominated by repeated dependency
pre-bundling, and the production build emits one large vendor chunk because
no chunking strategy is defined.

---

### Findings

#### F1 — Vendor code ships as a single monolithic chunk
- **Severity:** High
- **Confidence:** High
- **Evidence:** `visualizer` output shows one `vendor.js` containing React,
  the charting library, and the design-system library. No
  `build.rollupOptions.output.manualChunks` is present in `vite.config.ts`.
- **Recommendation:** Introduce deliberate vendor/route chunking so rarely-used
  libraries do not block first load (see config below). Validate chunk
  boundaries against the analyzer after the change.

#### F2 — Repeated full-page reloads from CJS dependency churn
- **Severity:** Medium
- **Confidence:** Medium
- **Evidence:** Dev logs show "new dependencies optimized" re-running on
  several boots; the dependency is a CommonJS package imported deep in a route.
- **Recommendation:** Add the package to `optimizeDeps.include` so it is
  pre-bundled deterministically. Measure cold start before/after locally
  rather than assuming a fixed speedup.

#### F3 — Secret-looking value inlined via `define`
- **Severity:** High
- **Confidence:** High
- **Evidence:** `vite.config.ts` contains
  `define: { __API_TOKEN__: JSON.stringify(process.env.API_TOKEN) }`, which
  inlines the token into the client bundle.
- **Recommendation:** Remove server-only secrets from `define`/`import.meta.env`.
  Only expose `VITE_`-prefixed, non-secret values to the client.

#### F4 — `legacy` plugin enabled against a modern-only target
- **Severity:** Low
- **Confidence:** Medium
- **Evidence:** `@vitejs/plugin-legacy` is enabled but the stated support
  matrix is evergreen browsers only; legacy adds duplicate transpiled bundles.
- **Recommendation:** Confirm the real browser support matrix; if legacy
  browsers are out of scope, drop the plugin. Verify behavior against current
  plugin docs.

---

### Recommended Config Changes

> Snippets below target Vite 5-era config. Verify option names and defaults
> against the version in your lockfile before applying.

```ts
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig(({ command }) => ({
  plugins: [
    react(),
    command === 'build' &&
      visualizer({ filename: 'dist/bundle-analysis.html', gzipSize: true }),
  ].filter(Boolean),

  optimizeDeps: {
    // Pre-bundle the CJS dependency that triggers reloads (F2)
    include: ['some-cjs-charting-lib'],
  },

  build: {
    sourcemap: false,
    cssCodeSplit: true,
    rollupOptions: {
      output: {
        // Deliberate splitting (F1) — keep this aligned with the dep graph
        manualChunks(id) {
          if (id.includes('node_modules')) {
            if (id.includes('react')) return 'vendor-react';
            if (id.includes('charting')) return 'vendor-charts';
            return 'vendor';
          }
        },
      },
    },
    chunkSizeWarningLimit: 600,
  },
}));
```

For SSR projects, build the server bundle separately and keep the
client/server boundary explicit:

```ts
// vite.config.ts (SSR additions)
export default defineConfig({
  ssr: {
    // Bundle ESM-only deps that break when left external; verify per dep
    noExternal: ['esm-only-ui-kit'],
  },
  build: {
    ssrManifest: true, // enables client asset preloading from SSR
  },
});
```

---

### Prioritized Remediation Plan

| # | Action | Surface | Effort | Priority |
|---|--------|---------|--------|----------|
| 1 | Remove secret from `define` | Security/env | Low | P0 |
| 2 | Add deliberate `manualChunks` | Prod build | Medium | P1 |
| 3 | Pre-bundle CJS dep via `optimizeDeps.include` | Dev server | Low | P1 |
| 4 | Re-validate browser target; drop `legacy` if unneeded | Plugins | Low | P2 |
| 5 | Wire `ssrManifest` + asset preloading (SSR only) | SSR | Medium | P2 |

**Validation:** Re-run the analyzer and a clean dev cold start after each
change; record real before/after numbers from this project rather than
relying on generic benchmarks.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Scopes the task to auditing and optimizing a Vite configuration across dev, build, and SSR surfaces.
- **ST-02 (Structured Sequential Instructions):** Walks inventory → dev server → production build → plugins/env → SSR → verification in order.
- **RT-02 (Multi-Dimensional Analysis Framework):** Separates dev-server, production-build, plugin/env, and SSR concerns as distinct dimensions with their own levers.
- **RT-05 (Evidence-Based Reasoning):** Requires each finding to cite a config line, analyzer output, or error rather than a remembered benchmark.
- **DS-06 (Prioritization Guidance):** Closes with a P0–P2 remediation plan separating quick wins from structural changes.

## Related Prompts

- [frontend_build_bundler_migration.md](frontend_build_bundler_migration.md) - When the goal is moving onto Vite from another bundler rather than tuning an existing Vite setup.
- [frontend_build_micro_frontends_module_federation.md](frontend_build_micro_frontends_module_federation.md) - When the Vite app participates in a federated, multi-bundle architecture.
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Deeper dependency-level bundle-size reduction once the build config is sound.
- [../nextjs/frontend_nextjs_performance.md](../nextjs/frontend_nextjs_performance.md) - Equivalent build/performance concerns in a Next.js context.
