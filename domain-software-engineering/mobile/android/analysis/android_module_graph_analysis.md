---
title: "Android Module Graph Analysis"
category: mobile-development
description: "Analyzes an existing multi-module Android project's dependency graph for coupling, layering violations, god-modules, dependency direction, and :core/:feature boundaries, with prioritized restructuring recommendations."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - android
  - modularization
  - architecture
  - module-graph
  - coupling
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_architecture_review.md
  - domain-software-engineering/mobile/android/analysis/android_build_gradle_health_analysis.md
  - domain-software-engineering/mobile/android/planning/android_modularization_strategy.md
---

# Android Module Graph Analysis

**Objective:** Analyze the dependency graph of an existing multi-module Android project — module count and layering, dependency direction, coupling and fan-in/fan-out, god-modules, cyclic or upward dependencies, and `:core`/`:feature`/`:app` boundary integrity — and report structural issues with concrete, low-risk restructuring recommendations. This is the **analysis-phase** counterpart to the forward-looking `planning/android_modularization_strategy.md`.

**When to Use:** Use this when build times grow with module count, when feature teams keep colliding in shared modules, when a "common"/"utils" module has become a dumping ground, before a large modularization push, or when onboarding engineers struggle to navigate boundaries. For single-module apps, use `android_architecture_review.md` instead.

---

## Context Gathering

1. **Graph inputs:** "Can you share `settings.gradle(.kts)` and each module's dependency block (or a `./gradlew :app:dependencies` / module graph)?"
2. **Convention:** "What layering is intended (e.g., app → feature → domain → data → core)? Any naming convention (`:feature:*`, `:core:*`)?"
3. **Pain points:** "Where do merge conflicts, slow builds, or boundary confusion concentrate?"
4. **Scale:** "How many modules and feature teams?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Map the real dependency edges** — from build files / dependency reports, not assumptions. Cite the module and its dependency block.
2. **Confirm direction violations** — a "wrong-way" edge is one that contradicts the stated/intended layering; establish the intended direction first.
3. **Distinguish coupling from cohesion** — high fan-in on a genuinely shared `:core:ui` may be correct; high fan-out from a feature into many siblings is the smell.
4. **Assess change cost** — restructuring is expensive; tie each recommendation to a concrete benefit (build time, team autonomy, testability).

**A clean module graph is an acceptable outcome.** Don't recommend churn for its own sake.

### False-Positive Prevention

- ❌ Do NOT flag many modules depending on `:core:*` design-system/util modules — that's expected fan-in.
- ❌ Do NOT flag `:app` depending on everything — the app module aggregates by design.
- ❌ Do NOT recommend splitting a cohesive module purely to raise the module count.
- ❌ Do NOT treat `api` vs `implementation` purely as style — assess leak impact.
- ✅ DO flag feature-to-feature direct dependencies that should route through an abstraction.
- ✅ DO flag cycles and upward (lower-layer → higher-layer) edges.
- ✅ DO flag god-modules with unrelated responsibilities and very high fan-in+fan-out.

---

### Phase 1: Graph Inventory

| Item | What to Capture |
|------|-----------------|
| Modules | Name, inferred layer (app/feature/domain/data/core), purpose |
| Edges | Each module's direct dependencies and the configuration (`api`/`implementation`) |
| Fan-in / fan-out | How many depend on it / how many it depends on |
| Shared modules | `:core`/`:common`/`:utils` — responsibilities they carry |

Produce a textual adjacency summary (and an ASCII/mermaid sketch if helpful).

---

### Phase 2: Layering & Direction Analysis

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Dependency cycle | CRITICAL | Two modules depending on each other (directly or transitively) |
| Upward dependency | HIGH | Lower layer (e.g., `:data`) depending on a higher layer (`:feature`) |
| Feature-to-feature | HIGH | One `:feature` directly depending on another instead of via `:domain`/navigation contract |
| Layer skipping | MEDIUM | UI reaching into `:data` directly, bypassing `:domain` |
| `api` over-exposure | MEDIUM | Transitive leakage forcing wide recompiles and hidden coupling |

---

### Phase 3: Coupling & Cohesion Analysis

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| God-module | HIGH | Very high fan-in+fan-out with mixed, unrelated responsibilities |
| Kitchen-sink `:common`/`:utils` | MEDIUM | Catch-all module bundling unrelated helpers; change magnet |
| Under-split feature | MEDIUM | One huge feature module that multiple teams edit (conflict hotspot) |
| Orphan/duplicate modules | LOW | Modules unused, or two modules doing the same job |
| Missing abstraction boundary | MEDIUM | Repeated cross-feature need with no shared contract module |

---

### Phase 4: Build & Team Impact

| Dimension | What to Assess |
|-----------|----------------|
| Build time | Which edges cause wide recompilation (`api` leaks, god-modules on the critical path) |
| Team autonomy | Which shared modules force cross-team coordination |
| Testability | Modules that can't be tested in isolation due to coupling |
| Reuse | Code duplicated across features that belongs in a shared module |

---

## Output Format

```markdown
## Android Module Graph Analysis Report

### Module Inventory
| Module | Layer | Fan-in | Fan-out | Responsibility |
|--------|-------|--------|---------|----------------|

### Structural Findings (severity-ordered)
**[SEVERITY] title** — Modules/edge involved · Why it's a problem · Recommended change

### Restructuring Recommendations (prioritized)
- **P1 (cycles / wrong-direction edges):** …
- **P2 (god-modules / hot conflict zones):** …
- **P3 (cohesion & reuse):** …
  Each with: target end-state, migration steps, risk, expected benefit.

### What's Already Healthy
```

---

## Expected Output

1. **Module inventory** with fan-in/out and layers.
2. **Structural findings** (cycles, direction, coupling).
3. **Prioritized, incremental restructuring plan** with risk/benefit.
4. **Affirmation** of healthy structure.

---

## Techniques Used

- **ST-01** (Clear Objective): Module-graph scope.
- **ST-02** (Structured Sequential Instructions): Inventory → layering → coupling → impact.
- **RT-02** (Multi-Dimensional Analysis): Structure + build + team lenses.
- **RT-05** (Evidence-Based Reasoning): Cite real edges/blocks.
- **DS-06** (Prioritization Guidance): Risk- and benefit-ranked changes.

---

## Related Prompts

- [android_architecture_review.md](android_architecture_review.md) - In-module layer/boundary analysis
- [android_build_gradle_health_analysis.md](android_build_gradle_health_analysis.md) - Build config behind module wiring
- [android_modularization_strategy.md](../planning/android_modularization_strategy.md) - Forward-design the target module structure
