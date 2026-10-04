---
title: "Astro Rendering Mode, Server Islands and Caching Review — Prerender vs On-Demand per Route, Personalised Fragments, Middleware Reach, and Cache Headers"
category: frontend-development/astro
description: "Decide, route by route, whether an Astro page should be prerendered at build time or rendered on demand, when a personalised fragment should become a server island instead of turning the whole page dynamic, what middleware actually protects at runtime versus at build, and which cache headers each on-demand response and island should send."
techniques:
  - IT-22
  - DP-06
  - QA-02
  - DS-06
difficulty: intermediate
tags:
  - astro
  - on-demand-rendering
  - prerendering
  - server-islands
  - astro-adapters
  - cache-control
  - astro-middleware
  - static-site-shows-old-data
  - personalize-static-page
  - should-my-site-be-static
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/astro/frontend_astro_islands_architecture.md
  - domain-frontend-development/astro/frontend_astro_content_collections.md
  - domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md
---

# Astro Rendering Mode, Server Islands and Caching Review

**Objective:** Give each route of an Astro site the cheapest rendering strategy that still
meets its freshness, personalisation and protection needs — prerendered, on demand, or
prerendered with server islands — and set the cache policy and middleware placement that
make that strategy safe, with the build-time and hosting consequences stated.

**When to Use:**
- One page needed a form, login or live price, and the whole site was switched to server
  output to get it.
- Static pages show data hours out of date, or builds take too long because thousands of
  pages rebuild for one change.
- A mostly static page needs a per-user fragment (avatar, cart count, recommendations).
- Auth was added in middleware and nobody has checked which pages it really protects.
- **Not this prompt if** the question is which *client-side* `client:*` directive an
  interactive component should use — use
  `domain-frontend-development/astro/frontend_astro_islands_architecture.md` (client
  islands hydrate in the browser; server islands render on the server later). For
  content schemas and collection queries, use
  `domain-frontend-development/astro/frontend_astro_content_collections.md`. For the same
  freshness decisions in Next.js, use
  `domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md`.

**Version note:** Astro 5 folded the former `hybrid` output into `static` with per-route
opt-out, and introduced server islands (`server:defer`). Verify every option, directive
and adapter feature below against current docs for the installed version.

## Inputs / Context

1. **`astro.config.*`**: `output`, adapter and its options, integrations.
2. **Route inventory**: every page and endpoint with its current `prerender` export, page
   count for dynamic routes, and data sources.
3. **Freshness requirement per route**: how stale may the content be (seconds, hours,
   until next deploy)?
4. **Personalisation per route**: none, a fragment, or the whole page.
5. **Middleware** (`src/middleware.*`): what it checks and for which paths.
6. **Hosting and CDN**: adapter target, CDN in front, current response headers.
7. **Build metrics**: build duration, pages built, rebuild trigger (content publish,
   deploy).

## Method

1. **Classify every route on three drivers (IT-22).** Freshness (deploy-time OK /
   minutes / per request), personalisation (none / fragment / whole page), and
   protection (public / authenticated). Route rule of thumb:
   - none + deploy-time + public → **prerender**.
   - fragment personalisation, rest public → **prerender + server island** for the
     fragment, with a fallback.
   - whole-page personalisation or authenticated → **on demand**, private caching.
   - per-request freshness but identical for everyone → **on demand + shared cache**
     (`s-maxage` plus `stale-while-revalidate`), or adapter-level incremental
     regeneration where offered.
2. **Name the dominant driver per route (DP-06).** Record the single reason a route is
   not prerendered. If no driver applies, it should be prerendered.
3. **Check middleware reach.** Middleware runs at build time for prerendered pages and
   at request time only for on-demand ones. Auth in middleware therefore does **not**
   protect a prerendered page at runtime — anyone with the URL gets the built HTML. Every
   protected route must be on demand (or protected by the host/CDN).
4. **Design server islands.** For each personalised fragment: the component with
   `server:defer`, a fallback slot of the same size (avoid layout shift), the props it
   receives (serialised and encrypted into the island request — keep them small and
   non-sensitive; verify size limits), and its own cache header set on the island
   response. Islands render in a separate request after the page, so they suit
   below-the-fold or non-critical fragments, not the LCP element.
5. **Set cache policy per response.** Prerendered assets: long-lived at the CDN, purged on
   deploy. On-demand public: `public, s-maxage=N, stale-while-revalidate=M`. On-demand
   personalised and server islands with user data: `private, no-store` (or short private).
   Never allow a response that read `Astro.cookies` to be cached publicly.
6. **Stress-test the plan (QA-02).** Ask: what happens on a CDN cache hit for a
   logged-in user? when the session cookie is missing on an island request? when the
   content API is down during build vs during request? when a 20,000-page dynamic
   route is prerendered on every content edit?
7. **Prioritise (DS-06).** Protection failures first (prerendered pages that should be
   private, publicly cached personalised responses), then freshness defects, then build
   and hosting cost. Confidence: High = observed in real responses or build output,
   Medium = read from config/code, Low = inferred from requirements.

## Output Format

```
# Astro rendering review — [site]   Astro: [version]   Adapter: [..]   Date: [..]

## Route classification
| Route | Pages | Freshness | Personalisation | Protection | Today | Recommended | Dominant driver |
## Middleware reach
| Middleware check | Intended routes | Routes where it runs at request time | Gap |
## Server islands
| Fragment | Host route | Fallback size | Props (size, sensitive?) | Island cache header |
## Cache policy
| Response type | Cache-Control | CDN behaviour |
## Stress tests
## Findings
| ID | Finding | Severity | Confidence | Evidence | Fix |
## Build and hosting impact
Build time: [before → after]   Requests rendered on demand/day: [estimate + basis]
```

## Verification

- [ ] Every route has a recommended mode and a named dominant driver (or "none").
- [ ] Every protected route is on demand or protected outside Astro.
- [ ] Every server island has a fallback and a cache header.
- [ ] No response reading cookies is publicly cacheable.
- [ ] Cache headers were checked on real responses, not only in code.
- [ ] Build-time and on-demand load changes are estimated with their basis.
- [ ] Version-sensitive options are marked "verify against current docs".

## False-Positive Prevention

1. **On demand as "more modern".** A prerendered page served from a CDN is faster and
   cheaper; dynamic rendering needs a reason.
2. **Server islands as client islands.** `server:defer` ships no framework JavaScript for
   the fragment; it is a deferred server render, not hydration.
3. **Middleware as a guard for every page.** It is not one for prerendered pages at
   runtime.
4. **Long builds as a reason to go fully dynamic.** Often a handful of high-churn routes
   should be on demand while the rest stay static.
5. **Islands for the hero.** A deferred render of the LCP element delays it; keep
   critical content in the initial HTML.
6. **Adapter features as universal.** Incremental regeneration, edge middleware and
   image services differ per adapter; check the one in use.

## Example Output

```
# Astro rendering review — "Saltmarsh Gear" outdoor retailer   Astro 5.x   Adapter: Node, CDN in front
Today: output "server" for every route (switched last year for the account area). Build 3 min;
p75 TTFB on product pages 640 ms (every request renders, CDN bypassed).

## Route classification
| /, /about, /guides/*     | 1 + 6 + 420 | deploy-time | none     | public | on demand | prerender | none |
| /products/[slug]         | 2,300 | price/stock: 5 min | fragment (cart, "recently viewed") | public |
  on demand | prerender + 2 server islands; nightly + on-publish rebuild | personalisation (fragment) |
| /products/[slug]/stock   | endpoint | per request | none | public | on demand | on demand,
  s-maxage=60, swr=300 | freshness |
| /account/*               | 9 | per request | whole page | auth | on demand | on demand, private | protection |
| /checkout                | 1 | per request | whole page | auth | on demand | on demand, no-store | protection |

## Middleware reach
| session check → redirect /login | /account/*, /checkout | all routes today (server output) | after change,
  only on-demand routes — matches intended set ✓ (guides/products never needed auth) |

## Server islands
| CartCount       | header (all pages) | 32×24 px skeleton | none | private, no-store |
| RecentlyViewed  | /products/[slug] below fold | 4-card skeleton, 280 px | productId (8 bytes) | private, max-age=0 |
Stock badge moved to /stock endpoint fetched by a client:visible component (shared cache).

## Stress tests
| CDN hit for logged-in user on product page | HTML identical for all; islands fetched separately ✓ |
| Island request without cookie | renders "0" cart / hides RecentlyViewed ✓ |
| Content API down at build | build fails, previous deploy stays live ✓ (alert added) |
| 2,300 product pages rebuild per publish | +6 min build; acceptable vs 5-min price SLA via /stock endpoint |

## Findings
| R1 | 2,727 public pages rendered per request; CDN bypassed | High | High | TTFB traces; no Cache-Control |
  prerender (see table) |
| R2 | /products/[slug] would leak cart if cached as a whole page | High | Medium | design review | islands |
| R3 | /account pages send no Cache-Control | Medium | High | response headers | private, no-store |

## Build and hosting impact
Build 3 → ~9 min (2,727 prerendered pages, measured on a branch). On-demand renders/day
~310k → ~45k (account, checkout, islands, stock; basis: last 7 days of logs).
```

## Techniques Used

- **IT-22 Workflow Decision Matrix** — freshness × personalisation × protection mapped to prerender, server island or on demand.
- **DP-06 Dominant Driver Identification** — each non-prerendered route names the one reason it is dynamic.
- **QA-02 Adversarial Stress-Test** — cache hits, missing cookies, upstream outages and rebuild cost tested against the plan.
- **DS-06 Prioritization and Severity Guidance** — protection and leakage before freshness and cost.

## Related Prompts

- `frontend_astro_islands_architecture.md` — client-side hydration directives for the interactive components on these pages.
- `frontend_astro_content_collections.md` — the content model whose updates drive rebuilds.
- `domain-frontend-development/nextjs/frontend_nextjs_data_fetching.md` — the comparable static/dynamic and caching decisions in Next.js.
