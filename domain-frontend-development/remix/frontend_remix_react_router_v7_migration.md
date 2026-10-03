---
title: "Remix v2 to React Router v7 Migration Plan — Future-Flag Readiness, Phased Cutover, Behaviour Changes, and Rollback Points"
category: frontend-development/remix
description: "Plan and review the move from Remix v2 to React Router v7 framework mode: audit which future flags are already on, sequence each flag and the package swap as a separate reversible phase with entry and exit criteria, list the behaviour changes that break apps silently (serialization, revalidation after errors, relative splat paths, headers), and define the tests that gate each phase."
techniques:
  - AG-40
  - QA-09
  - DP-07
  - RT-05
difficulty: advanced
tags:
  - react-router-v7
  - remix-migration
  - future-flags
  - single-fetch
  - route-module-types
  - framework-mode
  - upgrade-old-remix-app
  - remix-app-broke-after-upgrade
  - plan-framework-upgrade
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/remix/frontend_remix_data_loading.md
  - domain-frontend-development/build-tooling/frontend_build_bundler_migration.md
  - domain-agentic-resources/skills/framework-migration/dependency-upgrade/SKILL.md
---

# Remix v2 to React Router v7 Migration Plan

**Objective:** Turn "upgrade Remix to React Router v7" into a sequence of small, separately
shippable and reversible phases — each with entry criteria, the changes made, the tests
that must pass, and how to back out — and surface in advance the behaviour changes that
pass type-checking but change what users see.

**When to Use:**
- A Remix v2 app needs to move to React Router v7, the framework Remix converged into.
- A team started the upgrade, hit unexplained bugs, and needs to know which change
  caused them.
- You need an effort estimate and a risk list before committing a quarter to it.
- **Not this prompt if** you want to audit loaders, actions, revalidation and error
  boundaries as they stand — use
  `domain-frontend-development/remix/frontend_remix_data_loading.md`. For moving from
  webpack or the Remix classic compiler to Vite as a build-tool change, use
  `domain-frontend-development/build-tooling/frontend_build_bundler_migration.md`. For
  general dependency upgrade mechanics across a codebase, see
  `domain-agentic-resources/skills/framework-migration/dependency-upgrade/SKILL.md`.

**Version note:** React Router v7 and its Remix upgrade path are actively evolving. Every
flag name, package name, codemod and default below must be verified against the current
React Router upgrade guide before it is acted on.

## Inputs / Context

1. **Current versions**: `@remix-run/*` packages, React version, Node version, compiler
   (Vite plugin or classic compiler).
2. **`future` flags** currently set in the Remix config.
3. **Route conventions**: flat routes, folder routes, or a third-party route convention
   package.
4. **Server runtime and adapter**: Express, Node server, Cloudflare, Vercel, Netlify.
5. **Test coverage**: unit tests of loaders/actions, E2E coverage of critical journeys.
6. **Patterns in use**: `json()`, `defer()` with `<Await>`, `headers` exports,
   `shouldRevalidate`, fetchers with keys, splat routes with relative links,
   `createRemixStub` in tests, sessions and cookies.

## Method

1. **Phase 0 — Baseline (AG-40).** Entry: green CI. Actions: record E2E pass rate, Core
   Web Vitals, error rate, and a list of every route with its loader/action/headers/
   `shouldRevalidate`. Exit: baseline numbers saved. Nothing ships.
2. **Phase 1 — Vite.** If still on the classic compiler, move to the Remix Vite plugin
   first; React Router v7 framework mode requires Vite. Exit: production build parity
   (routes, assets, env vars) and no E2E regressions.
3. **Phase 2 — One future flag per release.** Enable the v3 flags one at a time (verify
   the current list; it has included `v3_fetcherPersist`, `v3_relativeSplatPath`,
   `v3_throwAbortReason`, `v3_singleFetch`, `v3_lazyRouteDiscovery`, `v3_routeConfig`).
   Each flag is its own release with its own rollback (flip it off) (QA-09).
4. **Predict how each flag fails (DP-07)** before enabling it:
   - *Relative splat path*: relative links inside splat routes resolve one level
     differently — audit every `<Link to="..">` and `navigate("..")` in splat routes.
   - *Fetcher persist*: fetchers survive unmount until idle — UI that relied on
     unmount to cancel or reset may show stale fetcher state.
   - *Single fetch*: data is streamed with a richer serializer, so `Date`, `Map`,
     `Set` and promises arrive as themselves instead of JSON strings — code that called
     `new Date(data.createdAt)` or compared strings changes behaviour and types change;
     `headers` export semantics change; after an action returns a 4xx/5xx, loaders may no
     longer revalidate by default; `json()` and `defer()` become unnecessary (return
     objects and promises; use `data()` for status and headers).
   - *Lazy route discovery*: the route manifest loads progressively — check any code that
     inspected the full manifest and any CSP rules for the discovery requests.
   - *Route config*: routes come from `app/routes.ts`; keep file conventions with the
     flat-routes adapter so no route moves.
5. **Phase 3 — Package swap.** Run the official codemod (verify its current name) to move
   `@remix-run/*` imports to `react-router` and `@react-router/*`; rename entry
   components (server and browser entry components are renamed); update the Vite plugin
   and add the React Router config file; replace test stubs with the new routes stub.
   Exit: type-check clean, E2E parity, no new console errors.
6. **Phase 4 — Adopt generated route types.** Turn on type generation, import route
   module types per route, and delete hand-written `useLoaderData<typeof loader>` casts
   that the generated types replace. Add the generated types directory to `.gitignore`
   and the TypeScript config as the guide describes.
7. **Phase 5 — Clean up.** Remove `json()`/`defer()` wrappers, dead future flags, and
   compatibility shims. Each removal is behaviour-neutral by then.
8. **Gate every phase with evidence (RT-05)**: E2E critical journeys, a no-JS form
   submission test, error-boundary test per route type, and production error rate
   compared with baseline for 48 hours. Rate each risk: High confidence when observed in
   this codebase by grep or test, Medium when the pattern exists but impact is untested,
   Low when inferred from the guide alone.

## Output Format

```
# Remix → React Router v7 migration — [app]   From: [versions]   Date: [..]

## Readiness
| Item | Current | Required | Gap |
## Pattern exposure (grep counts)
| Pattern | Count | Files | Affected by | Risk |
## Phases
| # | Entry criteria | Changes | Exit tests | Rollback | Est. effort |
## Predicted failure modes per phase
| Phase | What could break | How we'd notice | Confidence |
## Test gates
## Open questions to verify against current docs
```

## Verification

- [ ] Each future flag is its own phase with its own rollback.
- [ ] The package swap happens only after all flags are on and stable.
- [ ] Pattern exposure is counted from the codebase, not estimated.
- [ ] Serialization, revalidation-after-error and splat-path changes each have a test.
- [ ] Every version-sensitive name is listed under "verify against current docs".
- [ ] Effort estimates state what they are based on.

## False-Positive Prevention

1. **"Type-check passes, so it works."** Single fetch changes runtime values (Dates no
   longer strings) in ways types may hide behind `any` or old casts.
2. **Codemod as the migration.** The codemod moves imports; it does not fix behaviour
   changes from flags. Flags first, codemod second.
3. **Big-bang upgrade.** Flipping all flags and swapping packages in one release makes
   every bug ambiguous. One change per release.
4. **Assuming `json()` must be removed immediately.** It is deprecated, not the risk;
   remove it last, when it is behaviour-neutral.
5. **Treating the guide's flag list as fixed.** Flags and names have changed between
   releases; read the guide for the exact versions involved.
6. **Ignoring the server adapter.** Adapter packages move too; a passing local build can
   fail on the deploy target.

## Example Output

```
# Remix → React Router v7 migration — "Quayside" property management app
From: @remix-run/* 2.9, Vite plugin, Express adapter, React 18   Date: 2026-10-01

## Readiness
| Compiler      | Vite        | Vite        | none |
| future flags  | 2 of 6 on (fetcherPersist, throwAbortReason) | all 6 | 4 |
| Node          | 18          | 20+ (verify) | upgrade first |

## Pattern exposure
| json()/defer() returns        | 112 | 64 | singleFetch | Low |
| new Date(loaderData.x)        | 37  | 21 | singleFetch (Dates arrive as Date) | High |
| <Link to=".."> in splat routes | 9  | 3  | relativeSplatPath | Medium |
| headers export                | 14  | 14 | singleFetch | Medium |
| shouldRevalidate              | 6   | 6  | singleFetch | Medium |
| createRemixStub in tests      | 48  | 48 | package swap | Low |

## Phases
| 0 | green CI | baseline metrics | — | — | 0.5 d |
| 1 | baseline saved | Node 20 | E2E parity | redeploy Node 18 image | 0.5 d |
| 2a | — | v3_relativeSplatPath | 9 link tests | flag off | 1 d |
| 2b | 2a stable 1 wk | v3_singleFetch | Date tests, headers tests, 422-action test | flag off | 4 d |
| 2c | 2b stable 1 wk | lazyRouteDiscovery, routeConfig | route count = 87 | flags off | 1 d |
| 3 | all flags on | codemod; entry renames; routes stub | type-check, E2E | revert PR | 2 d |
| 4 | 3 stable | route typegen | remove 112 casts | revert PR | 2 d |
| 5 | 4 stable | drop json/defer, shims | E2E | revert PR | 1 d |
Total ≈ 12 engineer-days over ~5 weeks (stability windows dominate).

## Predicted failure modes
| 2b | lease end dates render "Invalid Date": 11 of the 37 sites call parseISO(loaderData.leaseEnd),
       which now receives a Date, not a string | E2E lease page | High (grep: 37 sites) |
| 2b | tenant form returns 422; list loader no longer revalidates, error banner shows stale count |
       422 action test | Medium |
| 2b | Cache-Control from child route headers lost/merged differently | header snapshot test | Medium |

## Open questions to verify against current docs
Exact flag list for 2.9 → 7.x; codemod name; headers merging under single fetch; Node minimum.
```

## Techniques Used

- **AG-40 Numbered Phase Discipline (Entry / Actions / Exit)** — every phase has entry criteria, actions, exit tests and rollback.
- **QA-09 Reversibility Assessment** — each phase is shippable alone and undone by a flag flip or a revert.
- **DP-07 Failure Mode Prediction** — how each flag can break the app is written down before it is enabled.
- **RT-05 Evidence-Based Reasoning** — exposure counted by grep; phase exit judged on tests and production error rates.

## Related Prompts

- `frontend_remix_data_loading.md` — auditing loaders, actions and revalidation once the app runs on v7.
- `domain-frontend-development/build-tooling/frontend_build_bundler_migration.md` — moving the build to Vite when that is the first blocker.
- `domain-agentic-resources/skills/framework-migration/dependency-upgrade/SKILL.md` — general mechanics for staged dependency upgrades.
