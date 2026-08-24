---
title: "Android Backend & API Contract Plan"
category: mobile-development
description: "Decide the backend strategy and define the client-facing API contract — endpoints/schema, error model, pagination, auth/token strategy, offline-sync contract, versioning, and codegen — before any networking code is written, so the Android client builds against a stable, agreed contract."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - CM-02
  - AG-08
difficulty: advanced
tags:
  - android
  - mobile-development
  - api-contract
  - backend-strategy
  - rest-graphql-grpc
  - authentication
  - pagination
  - offline-sync
updated: "2026-06-06"
related_prompts:
  - android_domain_data_model_design.md
  - android_offline_first_architecture.md
  - ../implementation/android_api_integration.md
  - android_tech_stack_selection.md
---

# Android Backend & API Contract Plan

**Objective:** Choose the backend strategy for an Android app and define the complete client-facing API contract — resources/endpoints (or schema), request/response shapes, a consistent error model and status-code taxonomy, pagination, authentication and token lifecycle, the offline-sync contract, versioning/deprecation policy, and how the contract is shared and code-generated — *before* a single line of Retrofit/Ktor is written. This is a decision-and-contract plan, not an implementation.

**When to Use:** Use this prompt after the architecture and domain data model are settled but before networking implementation begins. Use it when the backend doesn't exist yet (you're specifying what to ask for), when integrating a third-party/BaaS backend (you're documenting what you'll consume), or when an existing API is ad hoc and the client keeps breaking on undocumented changes.

**Sequence Map:** Use after `android_domain_data_model_design.md` and architecture selection; use before `../implementation/android_api_integration.md`. The offline-sync portion must be coordinated with `android_offline_first_architecture.md`.

**Important context:** The single most expensive Android networking mistake is writing client code against an unstable, undocumented, or implicit contract — then discovering pagination, error semantics, auth refresh, and sync conflict rules screen-by-screen during implementation. A written contract turns those discoveries into decisions made once. This plan does NOT produce Retrofit interfaces or Ktor clients — it produces the artifact those clients will be generated from (OpenAPI / proto / GraphQL schema) plus the decision record explaining the backend and contract choices.

---

## Context Gathering

Ask before deciding. The backend choice is mostly determined by the answers here, not by preference.

1. **What the app needs from a backend:**
   - "What are the core resources/entities (from the domain data model)?"
   - "Do you need real-time push (live updates, presence, chat) or is request/response enough?"
   - "How strong are the offline requirements (read-only cache, or full offline write + sync)?"
   - "What's the expected read:write ratio and rough request volume?"

2. **Team & control:**
   - "Does the team have backend engineers, or is mobile-only? (Pushes toward BaaS if mobile-only.)"
   - "Do you need to own/host the data, or is a managed backend acceptable (compliance, data residency)?"
   - "Existing backend or greenfield? Existing tech the org standardizes on?"

3. **Constraints:**
   - "Cost ceiling / pricing model sensitivity (per-read pricing vs flat compute)?"
   - "Auth requirements (social login, enterprise SSO, anonymous, multi-tenant)?"
   - "Latency/region requirements; metered-data markets?"

4. **Contract ownership:**
   - "Who owns the API contract — can the client team influence it, or is it fixed upstream?"
   - "Is there an existing OpenAPI/proto/GraphQL schema, or are we defining it?"

CHECKPOINT — do not pick a backend until real-time needs, offline needs, and team/control constraints are explicit. Those three answers usually decide it.

---

## Instructions

### Phase 1: Backend Strategy Decision Matrix

Score each candidate against weighted criteria for *this* app. Use 1-5 (5 = best fit). Multiply by weight, sum, decide — and record why.

| Criterion (weight) | Firebase / Firestore | Supabase | Custom REST | GraphQL | gRPC | Serverless / BaaS | BFF (backend-for-frontend) |
|--------------------|:-------------------:|:--------:|:-----------:|:-------:|:----:|:-----------------:|:--------------------------:|
| Team capacity / mobile-only friendliness | | | | | | | |
| Offline support (built-in vs DIY) | | | | | | | |
| Real-time push support | | | | | | | |
| Query flexibility / over-fetch control | | | | | | | |
| Cost model fit (per-read vs flat) | | | | | | | |
| Control / data ownership / portability | | | | | | | |
| Ecosystem & Android client maturity | | | | | | | |
| **Weighted total** | | | | | | | |

Reference notes (steer scoring, not pre-decide):

| Option | Strong when | Weak when |
|--------|-------------|-----------|
| **Firebase / Firestore** | Mobile-only team, real-time + offline cache built in, fast start | Complex relational queries, per-read cost at scale, vendor lock-in |
| **Supabase** | Want Postgres + auth + realtime as a managed product, SQL control | Need bespoke server logic beyond row-level rules |
| **Custom REST** | Full control, conventional, widest tooling/codegen | Over/under-fetching, more endpoints to version |
| **GraphQL** | Many screens with varied data needs, client-driven fetching, Apollo Kotlin codegen | Caching/complexity overhead, N+1 risk on server |
| **gRPC** | Internal/high-throughput, strict contracts via proto, streaming | Browser/edge friction, heavier client setup |
| **Serverless / BaaS** | Spiky load, minimal ops, glue logic | Cold starts, vendor specifics, harder local dev |
| **BFF** | Multiple clients need tailored aggregation; shield app from upstream churn | Extra layer to build/own |

CHECKPOINT — produce a single recommended backend with the weighted total and a 2-3 sentence rationale. State the top runner-up and the one fact that would flip the decision.

### Phase 2: Resource / Endpoint (or Schema) Definition

List every resource the client touches. For REST, enumerate endpoints; for GraphQL, the types/queries/mutations; for gRPC, the services/RPCs. Keep it contract-level, not implementation.

REST example shape:

| Resource | Method + path | Purpose | Auth | Idempotent? |
|----------|---------------|---------|:----:|:-----------:|
| Items | `GET /v1/items` | List (paginated) | Bearer | Yes |
| Items | `POST /v1/items` | Create | Bearer | No (use Idempotency-Key) |
| Item | `GET /v1/items/{id}` | Fetch one | Bearer | Yes |
| Item | `PATCH /v1/items/{id}` | Update | Bearer | Yes (with version/ETag) |
| Item | `DELETE /v1/items/{id}` | Soft delete | Bearer | Yes |
| Sync | `GET /v1/sync?since={token}` | Delta pull | Bearer | Yes |

Define request/response shapes for each (field name, type, nullability, required-on-write). Example:

```jsonc
// POST /v1/items  request
{
  "title": "string (required, 1..200)",
  "content": "string (nullable)",
  "clientId": "string uuid (required, client-generated for idempotency)"
}
// 201 response
{
  "id": "string",
  "title": "string",
  "content": "string|null",
  "version": 1,            // server-incremented, used for optimistic concurrency
  "updatedAt": "ISO-8601 string",
  "serverUpdatedAt": "ISO-8601 string"
}
```

### Phase 3: Error Model & Status-Code Taxonomy

Define ONE error envelope used everywhere, plus the status-code meaning table. The client builds a single error mapper against this.

```jsonc
// Consistent error envelope (every non-2xx)
{
  "error": {
    "code": "ITEM_NOT_FOUND",       // stable machine string (client switches on this)
    "message": "Human-readable",     // for logs, not necessarily UI
    "field": "title",                // optional, for validation errors
    "retryable": false,              // hint to client retry policy
    "requestId": "abc-123"           // for support/debugging correlation
  }
}
```

| HTTP status | Meaning | Client behavior |
|-------------|---------|-----------------|
| 200 / 201 / 204 | Success | Proceed |
| 400 | Validation / malformed | Show field error; do NOT retry |
| 401 | Token invalid/expired | Attempt single refresh, then re-auth (see Phase 5) |
| 403 | Authorized but forbidden | Surface permission error; no retry |
| 404 | Not found | Treat as deleted upstream; reconcile local state |
| 409 | Conflict (version mismatch) | Trigger conflict resolution (see Phase 6) |
| 422 | Semantic validation | Field errors; no retry |
| 429 | Rate limited | Back off per `Retry-After`; queue |
| 5xx | Server error | Exponential backoff + jitter; bounded retries |

Map machine `code` strings to client actions in a table so the mapping is owned in the contract, not improvised in the UI layer.

### Phase 4: Pagination Strategy

Choose cursor vs offset and state why; the Android client uses Paging 3, so the contract must be Paging-3-compatible (a `RemoteMediator` needs a stable forward cursor/key).

| Strategy | Use when | Paging 3 fit | Risk |
|----------|----------|--------------|------|
| **Cursor / keyset** (recommended) | Feeds, large/changing datasets | Excellent — opaque `nextKey` maps to load key | Can't jump to arbitrary page |
| **Offset / limit** | Small, stable, admin lists | Works but drifts | Duplicate/skipped rows on insert during paging |

Define the page response envelope:

```jsonc
{
  "data": [ /* items */ ],
  "pageInfo": {
    "nextCursor": "opaque-string|null",  // null = end of list
    "pageSize": 20
  }
}
```

State the default and max page size, and confirm the cursor is opaque and stable across inserts.

### Phase 5: Authentication & Token Strategy

Specify the auth flow and token lifecycle as a contract the client implements once.

| Decision | Specify |
|----------|---------|
| Auth protocol | OAuth 2.0 / OIDC (provider), or custom; social/SSO/anonymous |
| Token types | Short-lived access token + long-lived refresh token |
| Access token TTL | e.g. 15 min; refresh TTL e.g. 30 days, rotating |
| Refresh flow | Single-flight refresh on 401; queue concurrent requests during refresh; one retry |
| 401 handling | Authenticator/interceptor refreshes once; on refresh failure → force re-auth, clear session |
| Secure token storage | Android Keystore-backed encryption (e.g. encrypted DataStore / Tink); never plaintext SharedPreferences |
| Logout / revocation | Endpoint to revoke refresh token; clear local secure store |
| Multi-tenant / scopes | How tenant/scope is conveyed (claim, header) |

Contract requirement: define the exact refresh endpoint, request/response, and the rotation behavior, so the client's token authenticator is unambiguous.

### Phase 6: Offline-Sync Contract (coordinate with offline-first architecture)

If the app does offline writes, the sync semantics are part of the API contract — not an afterthought. Decide and document:

| Sync decision | Options | This app's choice |
|---------------|---------|-------------------|
| Sync model | Full re-pull vs delta/since-token vs change-feed | |
| Delta token | Server-issued opaque `syncToken` / timestamp / version vector | |
| Conflict authority | Last-write-wins, server-authoritative, client-wins, field-merge, user-resolved | |
| Concurrency control | `version` field / ETag / `If-Match`; server returns 409 on mismatch | |
| Tombstones | How deletes propagate (soft-delete flag in delta payload) | |
| Idempotency | Client-generated id / Idempotency-Key so retried writes don't duplicate | |
| Ordering | Server reconciliation order; client queue FIFO | |

State explicitly: the offline-first architecture (`android_offline_first_architecture.md`) owns the *local* SoT and queue; this contract owns the *wire* semantics (delta format, conflict response, idempotency). They must agree on the conflict-resolution ownership decision — name it here.

### Phase 7: Versioning, Deprecation, Contract Sharing & Codegen

| Concern | Decision |
|---------|----------|
| Versioning scheme | URI (`/v1/`) vs header vs GraphQL evolution; pick one |
| Breaking-change policy | What counts as breaking; additive-only within a version |
| Deprecation | `Deprecation`/`Sunset` headers; min-supported-client window; force-upgrade path |
| Contract artifact | OpenAPI 3.x (REST), `.proto` (gRPC), or SDL (GraphQL) as the source of truth |
| Codegen | Generate Kotlin models/clients from the artifact (e.g. OpenAPI generator → Retrofit/Ktor; protoc/gRPC; Apollo Kotlin) — contract drives code, never the reverse |
| Contract testing | Plan for contract/consumer tests so client and server can't silently drift |

### Phase 8: Rate Limits & Retry/Backoff Policy

| Concern | Decision |
|---------|----------|
| Server rate limits | Documented limits + `429` + `Retry-After` + `X-RateLimit-*` headers |
| Client retry policy | Exponential backoff with jitter; only retry idempotent ops + `retryable:true`; bounded attempts |
| Offline/queued writes | Persisted queue, retried via WorkManager with network constraint (coordinate with offline-first) |
| Timeouts | Connect/read/write/call timeout budgets (align with the latency budget in the performance plan) |

CHECKPOINT — before finishing, confirm every Phase-2 endpoint maps to: an auth rule, an error behavior, a pagination decision (if a list), and an idempotency stance (if a write).

---

## Expected Output

1. **Backend recommendation** — completed decision matrix with weighted totals, one recommended backend, runner-up, and the fact that would flip the choice.
2. **Resource/endpoint (or schema) catalog** — every client-touched resource with method/path (or type/RPC), purpose, auth, idempotency, and request/response field shapes.
3. **Error model** — one error envelope + status-code taxonomy + machine-code → client-action mapping.
4. **Pagination decision** — cursor vs offset with Paging-3 compatibility confirmed, page envelope, default/max sizes.
5. **Auth & token contract** — protocol, token TTLs, single-flight refresh + 401 handling, Keystore-backed secure storage, revocation.
6. **Offline-sync contract** — sync model, delta token, conflict authority (named, agreed with offline-first architecture), idempotency, tombstones.
7. **Versioning/deprecation + contract artifact + codegen plan** — OpenAPI/proto/SDL as source of truth, codegen direction, contract testing intent.
8. **Rate-limit + retry/backoff policy** — server limits, client retry rules, timeout budgets.

---

## CRITICAL: Verification Requirements

- [ ] A single backend is recommended with a completed, weighted decision matrix and an explicit flip condition.
- [ ] Every resource/endpoint has a defined request/response shape with field types and nullability — no "TBD" payloads.
- [ ] Exactly ONE error envelope is defined and used across all endpoints; status codes map to specific client behaviors.
- [ ] Pagination is decided (cursor vs offset), justified, and confirmed Paging-3-compatible with an opaque stable cursor.
- [ ] The auth contract specifies access/refresh TTLs, single-flight 401 refresh-and-retry, and Android Keystore-backed token storage (not plaintext).
- [ ] The offline-sync contract names the conflict-resolution authority and confirms it agrees with `android_offline_first_architecture.md`.
- [ ] Writes specify an idempotency mechanism (client id / Idempotency-Key) so retries don't duplicate.
- [ ] A versioning scheme and a single contract artifact (OpenAPI/proto/SDL) are chosen as the source of truth for codegen.
- [ ] No Retrofit/Ktor client *implementation* is produced — this stays at contract/decision level.

## False-Positive Prevention

- ❌ Do NOT pick a backend by popularity ("everyone uses Firebase") — pick by the matrix score for this app's offline/real-time/team constraints.
- ✅ DO record the runner-up and the single fact that would change the decision.
- ❌ Do NOT define a different error shape per endpoint — that forces N error mappers in the client.
- ✅ DO define one envelope with a stable machine `code` the client switches on.
- ❌ Do NOT default to offset pagination for feeds — it drifts under concurrent inserts and fights Paging 3.
- ✅ DO use an opaque, stable cursor and confirm it maps cleanly to a Paging 3 load key.
- ❌ Do NOT store tokens in plaintext SharedPreferences or hand-wave "secure storage."
- ✅ DO specify Android Keystore-backed encrypted storage and a single-flight refresh policy.
- ❌ Do NOT leave conflict resolution "to be decided during implementation" — that is the most expensive thing to retrofit.
- ✅ DO name the conflict authority in the contract and reconcile it with the offline-first plan.
- ❌ Do NOT write Retrofit interfaces, Ktor clients, or DI wiring here — that's `../implementation/android_api_integration.md`.
- ✅ DO produce the OpenAPI/proto/SDL artifact and let codegen produce the client.
- ❌ Do NOT pin exact library/AGP/Apollo/gRPC version numbers as part of the contract — version the API behavior, not the toolchain.

## Techniques Used

- **ST-01** (Clear Objective Statement): One goal — a backend decision plus a complete, implementation-free API contract.
- **ST-02** (Structured Sequential Instructions): Phased flow from backend choice → endpoints → errors → pagination → auth → sync → versioning → limits.
- **RT-02** (Multi-Dimensional Analysis Framework): Weighted decision matrix scoring backends across team/offline/real-time/cost/control axes.
- **DS-06** (Prioritization and Severity Guidance): Status-code taxonomy and retryability drive prioritized client behavior.
- **CM-02** (Constraint Specification): The contract is framed as binding constraints the client and server both honor.
- **AG-08** (Evidence-Based Decision Gates): CHECKPOINT gates force a justified backend choice and complete per-endpoint coverage before completion.

## Related Prompts

- [android_domain_data_model_design.md](android_domain_data_model_design.md) — Define the domain entities this contract exposes (run first).
- [android_offline_first_architecture.md](android_offline_first_architecture.md) — Owns the local source of truth and sync queue; coordinate the sync contract with it.
- [android_api_integration.md](../implementation/android_api_integration.md) — Implements Retrofit/Ktor against this contract (run after).
- [android_tech_stack_selection.md](android_tech_stack_selection.md) — Selects the networking/serialization libraries that consume this contract.
