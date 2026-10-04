---
title: "Remix / React Router Sessions, Route Authorization and HTTP Caching Review — Per-Loader Checks, Cookie Configuration, Redirect Safety, and Cache Headers"
category: frontend-development/remix
description: "Review the security and caching of a Remix or React Router framework-mode app at the route level: confirm every loader and action authorises independently because nested loaders run in parallel and route data is fetchable directly, check session cookie flags, secrets rotation, size and session fixation, validate post-login redirects, and make sure personalised responses are never cached by a shared cache."
techniques:
  - QA-02
  - RT-02
  - QA-24
  - DS-06
difficulty: advanced
tags:
  - remix-sessions
  - route-authorization
  - cookie-security
  - csrf
  - cache-control
  - open-redirect
  - logged-out-user-can-see-page
  - user-sees-someone-elses-data
  - protect-pages-behind-login
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/remix/frontend_remix_data_loading.md
  - domain-software-engineering/analysis/security/security_authentication_authorization_review.md
  - domain-frontend-development/nextjs/frontend_nextjs_server_actions_mutations.md
---

# Remix / React Router Sessions, Route Authorization and HTTP Caching Review

**Objective:** Prove, route by route, that a Remix or React Router (framework mode) app
cannot be made to return one user's data to another — through a child loader nobody
protected, a forgeable or oversized session cookie, an action that trusts an ID in the form,
an open post-login redirect, or a CDN caching a personalised response — and list the fixes
in order of harm.

**When to Use:**
- Adding login, roles, multi-tenant data, or an admin area to a Remix/React Router app.
- A layout "requires login", and nobody has checked whether its children do.
- A CDN sits in front of the app and personalised pages have ever been cached.
- Before a security review or penetration test, to fix the framework-specific issues first.
- **Not this prompt if** the concern is where data loads, revalidation after mutations, or
  progressive enhancement — use
  `domain-frontend-development/remix/frontend_remix_data_loading.md`. For the design of the
  identity system itself (password storage, MFA, OAuth flows), use
  `domain-software-engineering/analysis/security/security_authentication_authorization_review.md`.
  For Next.js Server Actions, use
  `domain-frontend-development/nextjs/frontend_nextjs_server_actions_mutations.md`.

**Version note:** single fetch, middleware and headers behaviour differ between Remix v2
and React Router v7 releases. Verify each API and default against current docs.

## Inputs / Context

1. **Route tree** with every `loader`, `action`, `headers` export and resource route.
2. **Session setup**: session storage type (cookie, database-backed, memory), cookie
   options, secrets source and rotation history.
3. **Auth helpers**: the function(s) that read the user (e.g. `requireUser(request)`) and
   where they are called.
4. **Roles and tenancy model**: what a user may read and change.
5. **Edge**: CDN or reverse proxy, its cache rules, and real response headers for a public
   page, a personalised page, and a route data request.

## Method

1. **Build the route × protection matrix (RT-02).** For each route: does the loader call
   the auth helper? does the action? which role/ownership check? what cache header is
   sent? Read each file — inheritance is not assumed.
2. **Apply the parallel-loader rule.** Nested loaders run in parallel, and each route's
   data can be requested on its own (the `_data` query in classic Remix, `.data` requests
   under single fetch — verify for the version). A parent layout's auth check therefore
   does **not** protect a child loader. Every loader that returns non-public data must
   authorise itself. Route-level middleware, where the version supports it, changes this;
   confirm it is enabled and covers the route before clearing a finding.
3. **Attack each action (QA-02).** For every action, ask: can I change another user's
   record by editing the ID in the form? Does the action check ownership against the
   session, not the payload? Does a multi-intent action (`intent` field) authorise each
   intent separately? Is input validated server-side? Try the request with curl or the
   browser network panel.
4. **Check the session cookie.** `httpOnly`, `secure` in production, `sameSite: "lax"`
   (or strict), a bounded `maxAge`, a `secrets` array where new secrets are prepended for
   rotation, and contents limited to identifiers (cookies are limited to about 4 KB, and
   cookie-session data is readable by the client unless encrypted). Confirm
   `commitSession` is set on the response whenever the session changes, and that login
   creates a fresh session (prevents session fixation) and logout destroys it.
5. **Check CSRF exposure.** `SameSite=Lax` blocks cross-site POSTs carrying the cookie in
   modern browsers, but not GET loaders with side effects, not sibling subdomains (same
   site, different origin), and not older clients. Flag state-changing GETs; add an
   Origin check or CSRF token where subdomains are untrusted.
6. **Check redirects.** Post-login `redirectTo` parameters must be validated as
   same-origin relative paths (reject `//evil.com`, `https://…`, and backslash variants).
7. **Check caching.** Personalised loader responses and route data requests must send
   `Cache-Control: private, no-store` (or `private, max-age=…` if intentional); public
   pages may set `public, s-maxage=…, stale-while-revalidate=…`. Confirm how parent and
   child `headers` combine for the version, and that responses setting cookies are never
   cached by the CDN.
8. **Check data exposure.** Everything a loader returns reaches the browser. Flag
   password hashes, tokens, internal flags and other users' fields in loader output.
9. **Record checked-and-cleared routes (QA-24); prioritise (DS-06):** cross-user data
   exposure, then privilege escalation, then session weaknesses, then caching performance.
   Confidence: High = reproduced with a request, Medium = read in code, Low = inferred.

## Output Format

```
# Route security & caching review — [app]   Version: [..]   Date: [..]

## Route × protection matrix
| Route | Loader authZ | Action authZ | Ownership/role check | Cache-Control sent | Data exposed |
## Session configuration
| Option | Value | Expected | Finding |
## Actions under attack
| Action | Intent(s) | Tampered request tried | Result |
## Redirects and CSRF
## Caching
## Findings
| ID | Finding | Severity | Confidence | Evidence | Fix |
## Checked and cleared
## Prioritised plan
```

## Verification

- [ ] Every loader returning non-public data has its own authorisation verdict.
- [ ] Every action was tried with a tampered ID or intent.
- [ ] Cookie flags were read from a real `Set-Cookie` header.
- [ ] Cache headers were read from real responses, including a route data request.
- [ ] Redirect validation was tested with at least three malicious inputs.
- [ ] Version-dependent behaviours are marked "verify against current docs".

## False-Positive Prevention

1. **Child routes as protected by the layout.** Loaders run in parallel; read each one.
   Conversely, do not report a route unprotected if enabled middleware covers it.
2. **Every cookie session as insecure.** Signed cookie sessions holding only a user ID
   with correct flags are a sound design.
3. **CSRF everywhere.** With `SameSite=Lax` and no state-changing GETs on a single
   origin, a token is defence in depth, not a critical gap.
4. **`private` caching as a bug.** Browser caching of the user's own data is often fine;
   the defect is shared (CDN) caching of personalised responses.
5. **Assuming headers merge.** How parent and child `headers` combine is version-specific;
   test real responses before asserting.
6. **Severity from theory.** An IDOR you reproduced is Critical; one inferred from naming
   is Medium until tried.

## Example Output

```
# Route security & caching review — "Hollis" clinic scheduling (staff app)
React Router 7 framework mode, single fetch, Node + CDN   Date: 2026-10-02

## Route × protection matrix (excerpt; 22 routes)
| /staff (layout)            | requireStaff ✓ | — | role=staff | private | name, role |
| /staff/patients/:id        | none ✗ | updateNotes: requireStaff ✓ | none ✗ | none (CDN default 60 s) | full record |
| /staff/schedule            | requireStaff ✓ | book: ✓ | clinicId from session ✓ | private | ok |
| /login                     | — | login | — | no-store | — |

## Session configuration
| httpOnly | true | true | ok |
| secure   | false | true in prod | F3 |
| secrets  | ["dev-secret"] | env, rotatable | F3 |
| login creates new session | no (reuses) | yes | F4 |

## Actions under attack
| updateNotes | save | changed :id to another clinic's patient | 200 — note saved (F2) |

## Findings
| F1 | patients/:id loader has no auth; /staff/patients/88.data returns full record logged out |
  Critical | High | curl without cookie → 200 JSON | requireStaff + clinic check in loader |
| F2 | updateNotes checks staff role but not patient.clinicId === session.clinicId | Critical | High |
  tampered POST succeeded | ownership check before write |
| F3 | Cookie not secure; hard-coded secret | High | High | Set-Cookie header; source | secure: prod;
  SESSION_SECRETS env array, prepend new |
| F4 | Session not regenerated on login | Medium | Medium | source | destroy + new session on login |
| F5 | /login?redirectTo=//evil.example redirects off-site | High | High | reproduced |
  allow only paths starting with a single "/" |
| F6 | CDN caches /staff/patients/:id for 60 s (no Cache-Control) | Critical | High | Age: 41 header seen |
  private, no-store on all /staff routes; CDN bypass on Cookie |

## Checked and cleared
| /staff/schedule loader | own requireStaff + clinicId from session | source + curl |
| Public /clinics pages | public, s-maxage=600; no session read | headers |

## Prioritised plan
1. F1, F2, F6 today — cross-patient data exposure.   2. F5, F3 this week.   3. F4 next sprint.
```

## Techniques Used

- **QA-02 Adversarial Stress-Test** — every action and data endpoint is attacked with tampered IDs, intents and redirects.
- **RT-02 Multi-Dimensional Analysis Framework** — authorisation, session, CSRF, redirect and cache treated as separate dimensions per route.
- **QA-24 Dismissed-Candidates Coverage Table** — routes confirmed safe are listed with their evidence.
- **DS-06 Prioritization and Severity Guidance** — cross-user exposure first, then escalation, session and caching.

## Related Prompts

- `frontend_remix_data_loading.md` — data placement, revalidation and progressive enhancement for the same routes.
- `domain-software-engineering/analysis/security/security_authentication_authorization_review.md` — reviewing the identity and permission model behind `requireUser`.
- `domain-frontend-development/nextjs/frontend_nextjs_server_actions_mutations.md` — the equivalent mutation and authorisation review in Next.js.
