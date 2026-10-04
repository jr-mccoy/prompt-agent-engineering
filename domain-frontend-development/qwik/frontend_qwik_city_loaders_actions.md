---
title: "Qwik City Routing, Loaders, Actions and Middleware Review — Server Data Flow, Form Progressive Enhancement, and Endpoint Exposure"
category: frontend-development/qwik
description: "Review how a Qwik City app moves data across the server boundary: whether data is loaded in route loaders rather than client tasks, what loader return values expose in the serialized HTML, whether actions validate and authorise their input, whether forms work before JavaScript, and whether middleware, server functions and cache headers protect and cache the right routes."
techniques:
  - RT-02
  - RT-05
  - QA-24
  - DS-06
difficulty: advanced
tags:
  - qwik-city
  - route-loaders
  - route-actions
  - server-functions
  - middleware
  - progressive-enhancement
  - where-to-load-data-in-qwik
  - qwik-form-without-javascript
  - protect-page-behind-login
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/qwik/frontend_qwik_resumability.md
  - domain-frontend-development/remix/frontend_remix_data_loading.md
  - domain-software-engineering/analysis/security/security_authentication_authorization_review.md
---

# Qwik City Routing, Loaders, Actions and Middleware Review

**Objective:** Establish, route by route, that a Qwik City app loads data on the server
before render, exposes nothing in loader output it should not, validates and authorises
every action and server function as the public endpoint it is, keeps forms working without
JavaScript, and caches only what is safe to cache — with each finding tied to the file and
line that shows it.

**When to Use:**
- A Qwik City app shows loading spinners for data that could have arrived with the HTML.
- You are adding authentication, roles, or per-user data and need to know what protects
  what.
- Forms behave differently with JavaScript disabled or before the page is interactive.
- Pages are slow on repeat visits and nobody has set cache headers deliberately.
- **Not this prompt if** the question is whether handlers and state cross `$`-boundaries
  correctly or why too much JavaScript runs on load — use
  `domain-frontend-development/qwik/frontend_qwik_resumability.md`. For signals, stores and
  task reactivity bugs inside components, use `frontend_qwik_reactive_state_tasks.md`.
  For the same review in Remix/React Router, use
  `domain-frontend-development/remix/frontend_remix_data_loading.md`.

## Inputs / Context

1. **Route tree**: `src/routes/` listing with `layout.tsx`, `index.tsx`, endpoint files
   (`index.ts`), and plugin files.
2. **Every `routeLoader$`, `routeAction$`, `globalAction$` and `server$`** definition with
   the file that exports it.
3. **Middleware**: `onRequest`, `onGet`, `onPost` exports in layouts, routes and plugins.
4. **Auth model**: how a session is read, what roles exist, which routes need which role.
5. **Deployment**: adapter (Node, edge, static), CDN in front, and current cache headers.
6. **Qwik version.** Qwik v2 renames packages and moves Qwik City to "Qwik Router";
   verify every API name below against current docs for the version in use.

## Method

1. **Map routes to data sources (RT-02).** For each route record: loaders used, actions
   used, middleware that runs, auth requirement, and cache policy. Loaders must be
   exported from a route boundary file (a layout or index) to run; a loader defined in a
   shared module and not re-exported from the route is a common silent failure (verify
   current rules).
2. **Find client-side loading that belongs in loaders.** Flag `useTask$`,
   `useVisibleTask$` or `useResource$` that fetch first-paint data on the client. They
   delay content, defeat SSR, and add a request waterfall. Legitimate exceptions: data
   that depends on browser-only state or is below the fold and optional.
3. **Check loader output exposure.** Everything a loader returns is serialized into the
   HTML for resumability. Flag secrets, internal IDs not needed by the UI, other users'
   data, and full records where the view needs three fields. Check loaders that depend on
   each other use the documented resolve mechanism rather than duplicate queries.
4. **Review actions and server functions as public endpoints (RT-05).** For each
   `routeAction$`, `globalAction$` and `server$`: is input validated (e.g. `zod$`), is the
   caller authorised *inside* the function for the specific resource (not only "logged
   in"), are failures returned with the documented failure helper and a status code rather
   than thrown, and is the operation idempotent or protected against double submit.
   `server$` functions can be called directly by anyone who can reach the URL.
5. **Check progressive enhancement.** Mutations should use the framework `<Form>` bound
   to an action so they submit before JavaScript loads and enhance afterwards. Flag
   `<form onSubmit$>` with a manual `fetch`, and buttons that only work after resume.
   Confirm pending state uses the action's running state rather than a hand-rolled flag.
6. **Review middleware coverage.** Middleware in a layout runs for nested routes; confirm
   the auth check sits at the right level, redirects unauthenticated users server-side
   (thrown redirect), and does not rely on a client guard. Confirm request-scoped data is
   passed via the request event's shared store rather than module-level variables, which
   are shared across requests on the server.
7. **Review caching.** Public, non-personalised pages should set an explicit cache policy
   (e.g. `maxAge` plus `staleWhileRevalidate` via the request event's cache helper).
   Personalised pages must not be cached by a shared CDN. Flag any route that both reads
   the session and sets a public cache header.
8. **Record what you checked and cleared (QA-24)**, then **prioritise (DS-06)**:
   authorisation and data exposure first, then correctness, then performance. Rate
   confidence: High = read in source and reproduced (e.g. direct POST, curl of the page),
   Medium = read in source only, Low = inferred from naming or behaviour.

## Output Format

```
# Qwik City review — [app]   Qwik version: [..]   Adapter: [..]   Date: [..]

## Route map
| Route | Loaders | Actions / server$ | Middleware | Auth needed | Cache policy |
## Client-side loading that belongs in loaders
## Loader output exposure
| Loader | Fields returned | Fields used by UI | Sensitive? | Action |
## Actions and server functions
| Endpoint | Validation | AuthZ inside? | Failure handling | Idempotent? | Finding |
## Progressive enhancement
## Middleware and auth coverage
## Caching
## Findings
| ID | Finding | Severity | Confidence | Evidence (file:line) | Fix |
## Checked and cleared
## Prioritised plan
```

## Verification

- [ ] Every route in `src/routes` appears in the route map.
- [ ] Each action and `server$` has a validation and authorisation verdict.
- [ ] Loader exposure compares fields returned with fields actually rendered.
- [ ] At least one form was tested with JavaScript disabled.
- [ ] Cache headers were read from a real response, not only from code.
- [ ] Every API name is marked "verify against current docs" where version-sensitive.
- [ ] Every finding carries severity and confidence.

## False-Positive Prevention

1. **Every client fetch as a defect.** Data that depends on viewport, local storage or a
   user gesture legitimately loads on the client.
2. **Logged-in check as authorisation.** "Has a session" does not mean "may edit order
   812". Look for the ownership or role check.
3. **Layout middleware as missing.** Middleware in a parent layout covers children; read
   the tree before reporting an unprotected route.
4. **Loader output as private.** It is in the page source. Anything returned is public to
   whoever can load the page.
5. **Validation on the client as validation.** `zod$` on the action is the trust boundary;
   client-side checks are UX only.
6. **API names from another version.** Qwik v1 and v2 differ in package names; do not
   report a "wrong import" without checking the version.
7. **Public caching everywhere.** A fast cached page that shows the previous visitor's
   cart is a data leak, not an optimisation.

## Example Output

```
# Qwik City review — "Fernhill" B2B ordering portal   Qwik 1.x   Adapter: Node behind CDN

## Route map (excerpt; 14 routes)
| /                    | useFeatured          | —                      | layout onRequest | no  | none set |
| /orders              | useOrders            | useCancelOrder         | layout onRequest | yes | public, max-age=300 (!) |
| /orders/[id]         | useOrder             | useUpdateQty, server$ recalcTotals | layout onRequest | yes | none |
| /account/settings    | — (useVisibleTask$ fetch) | <form onSubmit$> fetch | layout onRequest | yes | none |

## Loader output exposure
| useOrder | 41 fields incl. supplierCostPrice, internalMarginPct | 12 | yes | return a view model |

## Actions and server functions
| useCancelOrder | zod$ ✓ | session only, no ownership | fail() ✓ | yes | F2 |
| server$ recalcTotals | none | none | throws | yes | F3 |

## Findings
| F1 | /orders sends Cache-Control public, max-age=300 on a personalised list | Critical | High |
  curl shows header; CDN served customer A's orders to customer B in staging |
  private, no-store; cache only / and product pages |
| F2 | useCancelOrder cancels any order ID in the payload | Critical | High | routes/orders/index.tsx:58;
  reproduced with a crafted POST | check order.customerId === session.customerId |
| F3 | server$ recalcTotals callable without session, no validation | High | High | lib/orders.ts:12 |
  validate input; read session inside; or move logic into the action |
| F4 | useOrder exposes supplier cost and margin in HTML | High | High | view-source | trim to 12 fields |
| F5 | Settings loads via useVisibleTask$ and saves via fetch | Medium | High | spinner on load; no-JS
  save fails | routeLoader$ + routeAction$ with <Form> |

## Checked and cleared
| /orders/[id] auth | parent layout onRequest redirects with 302 to /login | source + curl |
| useFeatured client cache | public, non-personalised; caching it is safe | data review |

## Prioritised plan
1. F1, F2 today (data exposure across customers).  2. F3, F4 this sprint.  3. F5 next sprint.
API names (routeLoader$, routeAction$, server$, zod$, cacheControl) — verify against current docs.
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — each route assessed for loading, mutation, protection and caching separately.
- **RT-05 Evidence-Based Reasoning** — every finding cites file and line or a reproduced request.
- **QA-24 Dismissed-Candidates Coverage Table** — protections confirmed in place are recorded, not omitted.
- **DS-06 Prioritization and Severity Guidance** — exposure and authorisation before correctness and speed.

## Related Prompts

- `frontend_qwik_resumability.md` — whether the client resumes without eager JavaScript once the data arrives.
- `domain-frontend-development/remix/frontend_remix_data_loading.md` — the equivalent loader/action review for Remix and React Router.
- `domain-software-engineering/analysis/security/security_authentication_authorization_review.md` — a framework-independent review of the auth model itself.
