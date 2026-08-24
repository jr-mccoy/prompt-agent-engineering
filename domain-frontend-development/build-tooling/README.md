# Build Tooling Prompts

**Category:** Frontend Development / Build Tooling
**Prompts:** 3

---

## Overview

Production-grade prompts for auditing, architecting, and migrating frontend build toolchains. They cover tuning a Vite configuration end to end, designing Module Federation micro-frontends with safe shared-dependency and version-skew handling, and planning incremental bundler migrations with explicit risk and rollback gates. Each prompt is evidence-first and anti-fabrication: findings must cite real config, measured output, or current docs rather than remembered benchmarks or version-specific assertions.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_build_vite_optimization.md](frontend_build_vite_optimization.md) | Audit and optimize a Vite config: dev server/HMR, build splitting, dependency pre-bundling, plugins, env, SSR builds, and bundle analysis | Advanced |
| [frontend_build_micro_frontends_module_federation.md](frontend_build_micro_frontends_module_federation.md) | Design or review a Module Federation micro-frontend architecture: shared singletons, version skew, runtime integration, boundaries, and a when-NOT-to-use gate | Advanced |
| [frontend_build_bundler_migration.md](frontend_build_bundler_migration.md) | Plan an incremental bundler migration (e.g. Webpack → Vite/Rspack/esbuild): inventory, capability map, config/plugin translation, sequencing, and risk/rollback | Advanced |

## Usage Examples

### Vite Configuration Optimization
Use `frontend_build_vite_optimization.md` for:
- Diagnosing slow dev-server cold start or sluggish HMR
- Designing deliberate `manualChunks` vendor/route splitting
- Tuning `optimizeDeps` dependency pre-bundling
- Setting up correct SSR/SSG builds and env boundaries

### Micro-Frontend Architecture
Use `frontend_build_micro_frontends_module_federation.md` for:
- Deciding whether Module Federation is warranted versus a monorepo
- Enforcing framework singletons and avoiding duplicate instances
- Defining version-skew and remote-load failure policies
- Designing boundary/ownership contracts across teams

### Bundler Migration
Use `frontend_build_bundler_migration.md` for:
- Inventorying an existing build and capturing real baselines
- Mapping loaders/plugins to a target bundler's equivalents
- Sequencing a shippable, parallel-path migration
- Defining parity checks and rollback triggers

---

## Key Concepts

| Concept | Why It Matters |
|---------|----------------|
| Dependency pre-bundling | Drives Vite dev-server cold start and HMR stability |
| Manual chunking | Balances vendor/route splitting against request waterfalls |
| Shared singletons | Prevents duplicate framework instances breaking global state |
| Version skew policy | Keeps independently-deployed remotes interoperable |
| Capability mapping | Surfaces unsupported features as migration go/no-go inputs |
| Parity & rollback gates | Keep a migration safe and reversible at every step |

---

## Related Prompts

- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - Dependency-level bundle-size reduction once the build config is sound
- [../nextjs/frontend_nextjs_performance.md](../nextjs/frontend_nextjs_performance.md) - Build and performance concerns in a Next.js context
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Deciding where cross-remote/cross-bundle state ownership lives
- [../styling/frontend_styling_css_architecture.md](../styling/frontend_styling_css_architecture.md) - CSS ordering and extraction concerns that surface during build changes
