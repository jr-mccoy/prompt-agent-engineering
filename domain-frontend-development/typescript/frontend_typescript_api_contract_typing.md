---
title: "TypeScript API Contract Typing Strategy — Choosing the Source of Truth, Generated vs Shared Types, Runtime Validation at the Boundary, and CI Drift Gates"
category: frontend-development/typescript
description: "Decide how a frontend's types for back-end data are produced and trusted: pick the source of truth (OpenAPI or GraphQL code generation, shared schemas, end-to-end typed RPC, or hand-written types) from who owns the API and how releases couple, decide per endpoint whether responses are validated at runtime and what happens on failure, model errors, dates, nullability and open enums honestly, and gate drift in CI."
techniques:
  - DP-06
  - IPC-08
  - IPC-09
  - RT-02
difficulty: advanced
tags:
  - typescript
  - api-types
  - openapi-codegen
  - runtime-validation
  - zod
  - type-drift
  - frontend-breaks-when-backend-changes
  - api-returns-unexpected-data
  - keep-frontend-and-backend-types-in-sync
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/typescript/frontend_typescript_type_safety_audit.md
  - domain-software-engineering/testing/testing_contract_test_design.md
  - domain-software-engineering/analysis/architecture/architecture_api_client_code_generation.md
---

# TypeScript API Contract Typing Strategy

**Objective:** Give a frontend one honest answer to "how do we know this response has this
type?" — a chosen source of truth, a generation or sharing mechanism, a per-endpoint
runtime validation policy with defined failure behaviour, type modelling that matches what
JSON actually carries, and CI checks that make drift a build failure rather than a
production incident.

**When to Use:**
- API response types are hand-written interfaces that nobody updates when the back end
  changes.
- `as User` casts on `response.json()` are how the codebase "types" network data.
- A team is choosing between OpenAPI codegen, GraphQL codegen, tRPC-style RPC, or shared
  schema packages.
- A back-end change shipped and the frontend broke at runtime with no compile error.
- **Not this prompt if** you want a whole-codebase audit of `any`, assertions and strict
  flags — use
  `domain-frontend-development/typescript/frontend_typescript_type_safety_audit.md` (it
  *finds* untyped boundaries; this prompt *designs* the boundary). To generate a client
  library from a spec, use
  `domain-software-engineering/analysis/architecture/architecture_api_client_code_generation.md`.
  To prove the server honours its contract, use
  `domain-software-engineering/testing/testing_contract_test_design.md`.

## Inputs / Context

1. **API landscape**: number of endpoints/operations, REST vs GraphQL vs RPC, back-end
   language(s), who owns each API (same team, other team, third party).
2. **Repository shape**: monorepo with the back end, separate repos, published packages.
3. **Existing contract artefacts**: OpenAPI/GraphQL schema, its accuracy (generated from
   code or hand-maintained), versioning.
4. **Current typing practice**: hand-written interfaces, casts, any runtime schemas.
5. **Risk profile per endpoint**: payments, auth, health or legal data vs display-only.
6. **Incident history** of type/shape mismatches.

## Method

1. **Choose the source of truth by its dominant driver (DP-06).**
   - *TypeScript back end in the same monorepo, one consumer* → shared runtime schemas
     (e.g. Zod) or end-to-end typed RPC; types flow without generation.
   - *Other-language back end or separate team* → the published schema (OpenAPI or
     GraphQL SDL) is the contract; generate TypeScript types from it.
   - *Third-party API without a reliable schema* → hand-written runtime schemas at the
     boundary; the schema is your contract.
   Name the one driver that decides it; record the runner-up and why it lost.
2. **Decide how types are produced.** For codegen: which generator (verify current tool
   names and options), where the spec comes from (fetched at build, vendored with a
   version), and whether generated files are committed. Generated types describe the
   *spec*, not the running server — if the spec is hand-maintained, its accuracy is the
   real risk.
3. **Set a runtime validation policy per endpoint (IPC-08).** Validate responses at the
   boundary — parse, then check shape, before any code uses the data — for endpoints that
   are third-party, high-risk, or owned by a team that ships independently. Do not
   "repair" invalid data (coercing, defaulting missing fields) except through an explicit,
   short whitelist. Display-only endpoints from a tightly coupled back end may skip
   validation or validate in development and test only. Record the policy per endpoint.
4. **Define failure behaviour (IPC-09).** A validation failure becomes a typed error
   (`{ ok: false, error: { kind: "contract", endpoint, issues } }`) that propagates to
   the caller and is reported to monitoring — never swallowed into an empty list or a
   partially rendered object. Decide what the UI shows per endpoint class.
5. **Model JSON honestly (RT-02).**
   - Dates arrive as strings; type them as strings at the boundary and convert in one
     place, or validate-and-transform into `Date` in the schema.
   - Distinguish optional (key may be absent) from nullable (key present, value `null`)
     as the API actually behaves.
   - Treat server enums as *open* unless the contract promises otherwise: a new status
     value must not crash a `switch`; map unknown values to an explicit "unknown" branch.
   - Type error bodies too (e.g. RFC 9457 problem details) and model responses as unions
     of success and error shapes.
6. **Gate drift in CI.** Regenerate types from the pinned spec and fail on diff; run a
   breaking-change check on spec updates (verify tool choice); validate recorded or
   fixture responses against the schema; forbid `as`-casts on network data with a lint
   rule or a single typed fetch wrapper.
7. **Plan migration.** Order endpoints by risk × change frequency; replace hand-written
   interfaces and casts endpoint by endpoint behind the typed client. Confidence for each
   finding: High = measured (grep counts, incidents), Medium = sampled, Low = inferred.

## Output Format

```
# API contract typing strategy — [app]   APIs: [..]   Date: [..]

## Source of truth decision
Chosen: [..]   Dominant driver: [..]   Runner-up: [..] — lost because [..]
## Type production
Generator/mechanism · spec location & version · committed or built · regeneration trigger
## Runtime validation policy
| Endpoint class | Validate? (prod / test only / no) | On failure | UI behaviour |
## Modelling rules
Dates · optional vs nullable · open enums · error unions
## CI gates
| Gate | Tool/mechanism | Fails build when |
## Current state findings
| ID | Finding | Severity | Confidence | Evidence | Fix |
## Migration order
| Step | Endpoints | Why first | Effort |
```

## Verification

- [ ] The source-of-truth decision names one dominant driver and a rejected alternative.
- [ ] Every endpoint class has a validation policy and failure behaviour.
- [ ] No policy silently repairs invalid data outside a stated whitelist.
- [ ] Dates, nullability and enums have explicit modelling rules.
- [ ] At least one CI gate fails the build on drift.
- [ ] Tool names are marked "verify against current docs".

## False-Positive Prevention

1. **Generated types as runtime truth.** They are only as accurate as the spec; a
   hand-maintained spec can be wrong in the same way hand-written interfaces are.
2. **Validate everything everywhere.** Parsing large payloads on every response costs CPU
   on low-end devices; validate where the risk justifies it.
3. **Shared types as a contract across teams.** Importing the back end's types couples
   release cycles; across independent teams, a versioned schema is safer.
4. **Closed enums by default.** Exhaustive `switch` on a server enum is correct for
   values you own, brittle for values someone else can add.
5. **`unknown` + cast as validation.** `as` after `unknown` is still an assertion; only a
   parser narrows honestly.
6. **Tool names from memory.** Codegen and diff tools change; verify before recommending.

## Example Output

```
# API contract typing strategy — "Kestrel" logistics customer portal (React + TS)
APIs: 64 REST operations from a Kotlin back end (separate team), Stripe, a geocoding vendor

## Source of truth decision
Chosen: OpenAPI spec generated from the Kotlin controllers, published per release (v2.18.0).
Dominant driver: back end is another language and team, shipping weekly on its own cadence.
Runner-up: hand-written Zod schemas for all 64 — lost: duplicates a spec that already exists.

## Type production
openapi-typescript (verify) generates src/api/schema.d.ts at build from the pinned spec version;
a typed fetch wrapper exposes only generated operation types. Generated file not committed.

## Runtime validation policy
| Payments, invoices (9 ops)      | prod   | contract error → block action, show "refresh" | F2 |
| Shipments list/detail (14 ops)  | prod (full; payloads < 40 KB, parse cost measured at 3 ms p75 mobile) | contract error banner |
| Display-only reference (41 ops) | test only | — |
| Geocoding vendor (third party)  | prod, Zod schema hand-written | fall back to manual address entry |

## Modelling rules
Dates: string in schema; toDate() in the wrapper only. Status enums open: ShipmentStatus |
{ kind: "unknown"; raw: string }. Errors: problem+json union on every operation.

## CI gates
| Spec diff vs pinned version  | breaking-change checker (verify) | removed/renamed field without major bump |
| Fixture validation           | JSON Schema from spec            | any fixture invalid |
| No casts on network data     | lint rule on fetch wrapper output | `as` on response bodies |

## Current state findings
| T1 | 58 hand-written interfaces; 23 differ from spec | High | High | script diff | generated types |
| T2 | 112 `as` casts on response.json() | High | High | grep | typed wrapper |
| T3 | status "on_hold" added Aug; exhaustive switch threw, tracking page blank 2 h | High | High |
  incident #482 | open enum |
| T4 | invoice.paidAt typed Date, arrives string; sort by date compares strings | Medium | High | source |

## Migration order
1. Payments/invoices (risk). 2. Shipments (incident T3). 3. Reference data (bulk, low risk).
```

## Techniques Used

- **DP-06 Dominant Driver Identification** — the source of truth is chosen by naming the one factor that decides it.
- **IPC-08 Validation Gate, Reject-Don't-Repair** — responses are parsed and checked at the boundary; invalid data is rejected, not silently coerced.
- **IPC-09 Error Propagation over Absorption** — contract failures become typed errors that reach the caller and monitoring.
- **RT-02 Multi-Dimensional Analysis Framework** — source, production, validation, modelling and CI gates decided separately.

## Related Prompts

- `frontend_typescript_type_safety_audit.md` — finding the casts and `any` at boundaries this strategy replaces.
- `domain-software-engineering/testing/testing_contract_test_design.md` — verifying the server actually honours the spec.
- `domain-software-engineering/analysis/architecture/architecture_api_client_code_generation.md` — generating a full client from the same spec.
