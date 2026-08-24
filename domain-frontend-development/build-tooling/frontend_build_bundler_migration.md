---
title: "Frontend Bundler Migration Planning"
category: frontend-development/build-tooling
description: "Plan and execute a frontend bundler migration (e.g. Webpack → Vite / Rspack / esbuild): inventory the current build, design an incremental migration, translate config and plugins, and define risk/rollback gates."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - bundler-migration
  - webpack
  - vite
  - rspack
  - esbuild
  - build-tooling
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/build-tooling/frontend_build_vite_optimization.md
  - domain-frontend-development/build-tooling/frontend_build_micro_frontends_module_federation.md
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
  - domain-frontend-development/nextjs/frontend_nextjs_performance.md
---

# Frontend Bundler Migration Planning

**Objective:** Produce a safe, incremental plan to migrate a project from one bundler to another (for example Webpack → Vite, Rspack, or esbuild), covering build inventory, config and plugin translation, sequencing, and explicit risk/rollback gates.

**When to Use:**
- Use when: Build/dev-server times have become a bottleneck and a faster bundler is being evaluated.
- Use when: A toolchain is unmaintained or blocking framework/feature upgrades.
- Use when: Standardizing several apps onto one bundler and you need a repeatable migration playbook.
- Don't use when: The current bundler is merely *configured* poorly — tune it first (e.g. `frontend_build_vite_optimization.md` for Vite) before committing to a full migration.

## Instructions

1. **Inventory the current build**
   - Read the existing config (`webpack.config.*`, `craco`, framework wrappers) and `package.json` scripts; record entry points, output, dev server, and the full loader/plugin list.
   - Catalog build-specific features in use: code splitting, asset/loader handling (CSS modules, SVG, images, fonts), env injection, source maps, polyfills/legacy targets, Module Federation, and any custom loaders.
   - Capture baseline metrics from *this* project (cold build, incremental rebuild, dev start, bundle size). Do not substitute remembered benchmarks — measure.

2. **Confirm the target and map capabilities**
   - For the candidate bundler, map each current feature to its equivalent and grade it: native, plugin-available, manual workaround, or unsupported. Treat plugin names/options as items to verify against current docs.
   - Surface known gaps early (custom Webpack loaders, federation parity, unusual asset pipelines). Unsupported items are go/no-go inputs, not afterthoughts.
   - Decide migration shape: big-bang vs incremental (run both builds side-by-side behind a flag/branch during transition).

3. **Translate configuration and plugins**
   - Produce a side-by-side translation table: loader/plugin → target equivalent → notes/risk.
   - Translate resolve aliases, env handling, define/replacements, source-map settings, and the browser target to the target's idioms.
   - Flag any behavior that cannot be 1:1 translated (e.g. loader execution order, magic comments, runtime-specific globals) and design an explicit replacement.

4. **Sequence the incremental migration**
   - Order the work to keep the app shippable at every step: e.g. stand up the new dev build first, then the production build, then asset edge cases, then CI.
   - Keep a parallel path so the old bundler remains the source of truth until parity is proven; gate the switch on output equivalence.
   - Identify per-step validation: visual/functional smoke tests, bundle-diff, and key user flows.

5. **Define risk, parity checks, and rollback**
   - List the highest-risk areas (asset hashing/caching, SSR/hydration, env boundaries, federation, CSS ordering) and the specific test that proves each is safe.
   - Define the rollback trigger and mechanism (keep old config + scripts until N clean releases; feature-flag or branch the build).
   - Specify the "done" bar: functional parity + acceptable metrics measured on this project, not assumed.

6. **CRITICAL: Verify each claim before reporting**
   - Tie every capability/risk claim to the actual current config, a measured baseline, or target docs — never to a remembered build-speed multiplier or a version-specific assertion you have not confirmed.
   - For each finding, give evidence and a confidence level:
     - **High Confidence:** Backed by the real config and a reproduced build result on this project.
     - **Medium Confidence:** Inferred from config + general target behavior; not yet built.
     - **Low Confidence:** Plausible parity/gap; flagged "verify against current docs / prototype it."

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Promise a specific speedup ("10x faster builds") — measure this project's before/after instead.
- Assume every Webpack loader/plugin has a drop-in equivalent; some require a manual workaround or block the migration.
- Recommend a big-bang cutover for a large app without a parallel/rollback path.
- Translate config mechanically without checking behavior-level differences (loader order, asset hashing, env inlining).
- Treat env/`define` translation as cosmetic — a wrong boundary can leak secrets or break runtime config.
- State target-bundler option names/defaults from memory; they are version-sensitive.

✅ **DO:**
- Capture real baseline metrics before touching anything.
- Build a capability map that explicitly marks unsupported features as go/no-go inputs.
- Keep the old build runnable until parity is proven, and gate the switch on output equivalence.
- Validate per step with smoke tests, bundle-diffs, and the riskiest user flows.
- Define an explicit rollback trigger and keep the old config until several clean releases.
- Flag every version-sensitive detail as "verify against current docs."

## Expected Output

A bundler migration plan containing:
- A current-build inventory with measured baselines.
- A capability map (feature → target equivalent → grade).
- A config/plugin translation table with per-item risk.
- A sequenced, shippable-at-every-step migration plan.
- A risk register with parity checks and an explicit rollback gate.

### Output Format

```markdown
## Bundler Migration Plan: <From> → <To>

### Current Build Inventory
[Entries, loaders/plugins, features, baseline metrics]

### Capability Map
[Feature → target equivalent → grade (native/plugin/workaround/unsupported)]

### Config & Plugin Translation
[Table: current → target → notes/risk]

### Migration Sequence
[Ordered, shippable steps with per-step validation]

### Risk Register & Rollback
[Risks, parity checks, rollback trigger]
```

## Example Output

```markdown
## Bundler Migration Plan: Webpack → Vite

### Current Build Inventory

| Aspect | Current (Webpack) |
|--------|-------------------|
| Entries | Single SPA entry |
| Loaders | babel, css/postcss, svgr, file-loader |
| Plugins | HtmlWebpackPlugin, DefinePlugin, MiniCssExtract |
| Features | route code splitting, CSS modules, env via Define |
| SSR | none |

**Measured baselines (this project):**

| Metric | Value (measured) |
|--------|------------------|
| Cold prod build | record locally |
| Dev server start | record locally |
| Incremental rebuild | record locally |
| Initial bundle (gzipped) | record locally |

> Numbers are placeholders to be filled from this project's actual runs.
> No remembered benchmark is substituted.

---

### Capability Map

| Feature | Vite Equivalent | Grade |
|---------|-----------------|-------|
| Babel transpile | esbuild / `@vitejs/plugin-*` | Native |
| CSS modules / PostCSS | Built-in CSS handling | Native |
| SVG as component | `vite-plugin-svgr` | Plugin |
| `file-loader` assets | `import` URL / `assetsInclude` | Native (different API) |
| `DefinePlugin` env | `define` / `import.meta.env` | Native (different semantics) |
| Route code splitting | Dynamic `import()` | Native |
| Custom Webpack loader X | none | Unsupported → workaround needed |

**Go/no-go input:** custom loader X has no equivalent and must be replaced
by a Vite plugin or a build step before migration can complete.

---

### Config & Plugin Translation

| Webpack | Vite | Notes / Risk |
|---------|------|--------------|
| `DefinePlugin` | `define` + `VITE_` env | Re-check secret boundary; only expose public values |
| `svgr` loader | `vite-plugin-svgr` | Verify import syntax differs; update call sites |
| `file-loader` | URL imports | Asset hashing/path differs — check cache busting |
| `MiniCssExtract` | built-in | CSS ordering may differ — visual diff required |
| magic-comment chunk names | manual chunk config | Names not 1:1; update any code referencing chunk names |

---

### Migration Sequence

1. **Stand up Vite dev build in parallel** (new script, branch); keep Webpack
   as source of truth. Validate: app boots, key routes render.
2. **Wire production build** with deliberate chunking; bundle-diff vs Webpack
   output. Validate: route splitting + asset URLs resolve.
3. **Resolve asset edge cases** (SVG, fonts, public dir, env boundary).
   Validate: visual smoke test of asset-heavy screens.
4. **Replace unsupported loader X** with a Vite plugin/step. Validate: the
   feature it powered works end-to-end.
5. **Switch CI + delete Webpack** only after N clean releases. Validate: CI
   build + deploy parity.

Each step ships independently; the old build stays runnable until step 5.

---

### Risk Register & Rollback

| Risk | Parity Check | Severity | Confidence |
|------|--------------|----------|------------|
| Env boundary change leaks/breaks config | Diff inlined values; grep client bundle for secrets | High | High |
| CSS ordering differs (visual regressions) | Visual diff of key screens | Medium | Medium |
| Asset hashing breaks long-term caching | Compare emitted filenames/headers | Medium | Medium |
| Unsupported loader X has no clean replacement | Prototype before committing | High | Medium |

**Rollback trigger:** any P0 parity failure (broken core flow, leaked secret,
unbuildable CI) → revert to the retained Webpack scripts/config.
**Rollback mechanism:** old config + scripts kept on `main` until 3 clean
production releases on Vite; switch is a one-line script change to revert.

**Done bar:** functional parity on all key flows + build/dev metrics measured
on this project that meet or beat the recorded baselines.
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Defines the task as producing a safe, incremental bundler-migration plan with rollback gates.
- **ST-02 (Structured Sequential Instructions):** Sequences inventory → capability map → translation → migration order → risk/rollback → verification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Analyzes the migration across config, assets, env, performance, and CI dimensions rather than as a single config swap.
- **RT-05 (Evidence-Based Reasoning):** Forces capability and risk claims to rest on the real config, measured baselines, and target docs instead of recalled speed multipliers.
- **DS-06 (Prioritization Guidance):** Orders steps to stay shippable and ranks risks with explicit rollback triggers.

## Related Prompts

- [frontend_build_vite_optimization.md](frontend_build_vite_optimization.md) - Tune the existing/target Vite build before or after migrating; sometimes a better config removes the need to migrate.
- [frontend_build_micro_frontends_module_federation.md](frontend_build_micro_frontends_module_federation.md) - When the migration must preserve a federated multi-bundle setup across bundlers.
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - To compare bundle composition before and after the migration.
- [../nextjs/frontend_nextjs_performance.md](../nextjs/frontend_nextjs_performance.md) - For framework-managed build migrations within Next.js.
