---
title: "Micro-Frontend Architecture with Module Federation"
category: frontend-development/build-tooling
description: "Design or review a micro-frontend architecture using Module Federation: shared dependency singletons, version skew handling, runtime integration, boundary/ownership design, and a clear test for when NOT to use it."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - micro-frontends
  - module-federation
  - build-tooling
  - shared-dependencies
  - runtime-integration
  - architecture
updated: "2026-06-21"
related_prompts:
  - domain-frontend-development/build-tooling/frontend_build_vite_optimization.md
  - domain-frontend-development/build-tooling/frontend_build_bundler_migration.md
  - domain-frontend-development/architecture/frontend_state_management_selection.md
  - domain-frontend-development/performance/frontend_performance_bundle_optimization.md
---

# Micro-Frontend Architecture with Module Federation

**Objective:** Design or review a Module Federation–based micro-frontend (MFE) architecture, making deliberate decisions about boundaries, shared dependency singletons, version-skew tolerance, and runtime integration — and validate whether MFEs are warranted at all.

**When to Use:**
- Use when: Multiple independently-deployed teams must compose a single application at runtime.
- Use when: An existing MFE setup suffers from duplicate dependencies, singleton conflicts, or version skew between remotes and host.
- Use when: Evaluating whether to adopt Module Federation versus a monorepo or build-time composition.
- Don't use when: One team owns the whole frontend and a monorepo with build-time code splitting would suffice — recommend that simpler path instead of forcing MFEs.

## Instructions

1. **Justify (or reject) Module Federation first**
   - State the concrete driver: independent deployability, separate team ownership, or runtime composition of third-party-owned UI. If none applies, document why a monorepo + lazy chunks (see `frontend_build_vite_optimization.md`) is the better answer and stop.
   - Identify the host(s) and remotes, who owns each, and their release cadences.
   - Note the bundler(s) in play (Webpack Module Federation, Rspack, Vite via a federation plugin) and treat exact plugin/option names as something to verify against current docs.

2. **Design the boundaries and ownership**
   - Map each remote to a team, a deploy pipeline, and a public contract (exposed modules, props, events).
   - Define the integration seam: route-level remotes, slot/widget remotes, or shared-layout host. Prefer coarse, stable seams over chatty cross-remote calls.
   - Specify versioning of the *contract* (exposed module shape) separately from the *code*.

3. **Design shared dependencies and singletons**
   - Enumerate dependencies that MUST be singletons (frameworks with global state — e.g. React, the router, a shared state/store, design-system context providers).
   - For each shared dependency decide: `singleton` (one instance enforced), `eager` (loaded with the host shell), and the `requiredVersion`/version range. Justify each choice; do not blanket-share everything.
   - Flag dependencies that should NOT be shared (small, side-effect-free utilities) where sharing adds coordination cost without benefit.

4. **Handle version skew**
   - Define the policy when a remote's `requiredVersion` cannot be satisfied by the host's provided version: fail loud, fall back to a remote-bundled copy, or block deploy.
   - Identify singletons where two incompatible major versions would break global invariants (e.g. two React instances breaking hooks/context) and make those hard constraints.
   - Specify how the contract evolves without a lockstep deploy (additive changes, deprecation windows).

5. **Design runtime integration & resilience**
   - Define remote loading (static vs dynamic remote URLs / manifest-driven), and how the host degrades when a remote fails to load (error boundary, fallback UI, timeout).
   - Address cross-remote communication: shared event bus, URL/route state, or a shared store — and where state ownership lives.
   - Cover shared concerns once at the host: auth/session, theming, i18n, telemetry — so remotes inherit rather than re-implement them.

6. **CRITICAL: Verify each recommendation before reporting**
   - Tie every claim to a real config (`exposes`/`remotes`/`shared`), an observed runtime error, or the team/ownership map — not to a remembered benchmark or a specific plugin version asserted from memory.
   - For each finding, give evidence and a confidence level:
     - **High Confidence:** Backed by actual federation config and/or a reproduced runtime/version-skew error.
     - **Medium Confidence:** Inferred from the dependency and ownership map; not yet reproduced.
     - **Low Confidence:** General Module Federation behavior; flagged "verify against current docs."

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Recommend Module Federation when a single team owns everything and a monorepo would do — that is the most common over-engineering trap.
- Mark every shared library as `singleton: true` without checking whether it actually holds global state.
- Assume two semver-compatible versions are interchangeable for stateful singletons (React, router, store) — incompatibility there is a hard break, not a warning.
- Quote a specific Webpack/Rspack/Vite federation option name or default without flagging it as version-dependent.
- Ignore the failure path — design that assumes every remote always loads is incomplete.
- Invent performance figures for "extra network requests" or "duplicate bytes"; reason from the actual `shared` graph instead.

✅ **DO:**
- Start from the ownership/deploy-independence driver and reject MFEs when it is absent.
- Enumerate singletons explicitly and justify each `shared` entry.
- Treat host/remote version ranges as a contract with an explicit skew policy.
- Design error boundaries and fallback UI for remote-load failures up front.
- Keep cross-remote coupling coarse and contract-based; avoid chatty shared mutable state.
- Phrase plugin/option specifics as "verify against current Module Federation / bundler docs."

## Expected Output

A micro-frontend architecture design or review containing:
- A go/no-go judgment on Module Federation with the driver stated.
- A boundary + ownership map (host, remotes, contracts, teams).
- A shared-dependency table (singleton/eager/version) with justification per entry.
- A version-skew and runtime-resilience policy.
- Findings (for a review) and a prioritized set of recommendations, each with severity, confidence, and evidence.

### Output Format

```markdown
## Micro-Frontend Architecture (Module Federation)

### Suitability Verdict
[Go / No-go + driver]

### Boundary & Ownership Map
[Host, remotes, contracts, owning teams]

### Shared Dependencies
[Table: dependency / singleton / eager / version / justification]

### Version Skew & Resilience Policy
[Skew handling, failure fallbacks, contract evolution]

### Findings & Recommendations
[Each with Severity / Confidence / Evidence / Recommendation]
```

## Example Output

```markdown
## Micro-Frontend Architecture (Module Federation)

### Suitability Verdict

**Verdict:** Go (with constraints).
**Driver:** Three independently-deployed teams (Shell, Checkout, Account)
ship on separate cadences and must compose at runtime without a coordinated
release. A monorepo with build-time chunks was rejected because deploys are
not independent there.

> If only one team owned all three areas, the recommendation would be a
> monorepo with lazy-loaded route chunks instead — see the Vite optimization
> prompt. Module Federation's coordination cost is only justified by
> independent deployability.

---

### Boundary & Ownership Map

| Unit | Role | Owner | Exposes / Contract |
|------|------|-------|--------------------|
| `shell` | Host | Platform team | Layout, auth, theming, router |
| `checkout` | Remote | Checkout team | `./CheckoutRoute` (route-level) |
| `account` | Remote | Account team | `./AccountWidget` (slot) |

Integration seam: **route-level** for Checkout, **slot/widget** for Account.
Cross-remote calls are avoided; shared state flows through the host.

---

### Shared Dependencies

| Dependency | singleton | eager | version policy | Justification |
|------------|-----------|-------|----------------|---------------|
| react / react-dom | yes | yes | strict major match | Multiple instances break hooks/context — hard constraint |
| router | yes | yes | strict major match | Single history/global routing state |
| design-system (theme ctx) | yes | no | range, additive | Context provider must be one instance |
| date utility | no | no | not shared | Small, stateless; sharing adds coordination with no payoff |

---

### Version Skew & Resilience Policy

- **Singletons (react, router, design-system):** host provides the version;
  a remote requiring an incompatible **major** fails the build/deploy gate.
  Two React majors at runtime is treated as a hard break, not a fallback.
- **Non-singleton shared deps:** if `requiredVersion` is unmet, the remote
  loads its own bundled copy (duplicate bytes accepted as the safe default).
- **Contract evolution:** exposed module props change additively; removals go
  through a deprecation window so host and remote need not deploy in lockstep.
- **Runtime failure:** every remote mounts behind an error boundary with a
  timeout and a fallback UI; a failed Checkout remote degrades to a
  "temporarily unavailable" panel rather than crashing the shell.

---

### Findings & Recommendations

#### F1 — React not enforced as a singleton
- **Severity:** High
- **Confidence:** High
- **Evidence:** `shared` config lists `react` without `singleton: true`;
  console shows "Invalid hook call" intermittently when the Account remote
  loads, consistent with a second React instance.
- **Recommendation:** Set `react`/`react-dom` to `singleton: true, eager: true`
  with a strict version range on host and all remotes. Verify exact option
  spelling against current federation plugin docs.

#### F2 — Every dependency marked shared
- **Severity:** Medium
- **Confidence:** Medium
- **Evidence:** `shared` includes ~20 packages, most stateless utilities.
- **Recommendation:** Share only stateful/framework singletons; unshare
  small stateless utilities to cut coordination overhead. Re-measure the
  actual `shared` graph after pruning rather than assuming a byte figure.

#### F3 — No fallback when a remote fails to load
- **Severity:** High
- **Confidence:** High
- **Evidence:** Remote mounts directly with no error boundary; a 404 on the
  remote entry blanks the route.
- **Recommendation:** Wrap each remote in an error boundary with a timeout and
  fallback component; surface load failures to telemetry.

---

### Prioritized Recommendations

| # | Action | Effort | Priority |
|---|--------|--------|----------|
| 1 | Enforce react/router/design-system singletons | Low | P0 |
| 2 | Add remote-load error boundaries + fallbacks | Medium | P0 |
| 3 | Prune over-shared stateless deps | Low | P1 |
| 4 | Document contract-evolution + skew gate in CI | Medium | P1 |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as designing/reviewing a Module Federation architecture with an explicit suitability gate.
- **ST-02 (Structured Sequential Instructions):** Orders the work justify → boundaries → shared deps → skew → runtime → verify.
- **RT-02 (Multi-Dimensional Analysis Framework):** Treats ownership, sharing/singletons, version skew, and runtime resilience as separate dimensions.
- **RT-05 (Evidence-Based Reasoning):** Requires each finding to cite federation config, a reproduced error, or the ownership map rather than recalled numbers.
- **DS-06 (Prioritization Guidance):** Ends with a P0–P1 recommendation ranking driven by severity and blast radius.

## Related Prompts

- [frontend_build_vite_optimization.md](frontend_build_vite_optimization.md) - The simpler monorepo + lazy-chunk alternative when independent deploys are not actually required.
- [frontend_build_bundler_migration.md](frontend_build_bundler_migration.md) - When adopting/changing the bundler that provides federation (e.g. Webpack → Rspack).
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - For deciding where cross-remote state ownership should live.
- [../performance/frontend_performance_bundle_optimization.md](../performance/frontend_performance_bundle_optimization.md) - For analyzing duplicate/shared bytes across the federated graph.
