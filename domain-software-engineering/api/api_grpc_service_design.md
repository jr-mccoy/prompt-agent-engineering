---
title: "gRPC Service Design Review"
category: api
description: "Review or design a gRPC service: proto style, service/method shape, streaming decisions, error model, versioning / evolution, deadline / retry / backoff policy, auth, and transcoding / gateway strategy."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - api
  - grpc
  - protobuf
  - streaming
  - buf
  - service-design
  - versioning
  - deadline-propagation
updated: "2026-04-17"
related_prompts:
  - api_rest_design_review.md
  - api_openapi_documentation.md
  - api_versioning_strategy.md
  - api_openapi_linting_governance.md
---

# gRPC Service Design Review

**Objective:** Review (or design) a gRPC service end-to-end: proto style, service/method shape, streaming pattern, error model, evolution rules, deadline / retry / backoff, authn/authz, and transcoding / gateway for REST clients. Deliver actionable, style-guide-aligned recommendations.

## When to Use

- Designing a new service and choosing between REST and gRPC.
- Reviewing an existing `.proto` package before public / partner exposure.
- Hitting production issues that map to gRPC anti-patterns (unbounded streaming, no deadlines, wide protos).
- Migrating from REST to gRPC, or adding gRPC alongside REST.
- Adopting buf for schema governance and unsure about ruleset.

**Do NOT use this prompt for:**
- REST-specific review (use `api_rest_design_review.md`).
- OpenAPI documentation (use `api_openapi_documentation.md`).
- Versioning strategy in isolation (use `api_versioning_strategy.md`).

## Inputs / Context

Collect:
- **Language mix**: server language(s), client language(s).
- **Deployment topology**: mesh (Istio / Linkerd) / direct / via envoy / via API gateway.
- **Scale**: RPS, streaming sessions concurrent, cross-DC.
- **Clients**: internal only / mobile / browser (needs grpc-web or gRPC-JSON transcoding).
- **Governance**: buf / protoc-gen / custom lint.
- **Evolution history**: any breaking changes done before? With what policy?

## Must / Must Not

**Must:**
- Enforce a **proto style guide** (Buf Style Guide is the default): `PascalCase` messages, `snake_case` fields, field numbers packed low, no re-use of retired numbers.
- For every service, decide **streaming pattern** consciously: unary (default), server-streaming (large results), client-streaming (large uploads), bidi (chat / interactive).
- Specify **error model**: `google.rpc.Status` + `Code` + rich error details (`BadRequest`, `PreconditionFailure`, etc.) — NOT ad-hoc error strings.
- Set **deadlines** on every RPC; propagate across service calls.
- Define **retry policy**: idempotent RPCs only, bounded retries, exponential backoff + jitter, hedging for reads.
- Specify **authn** (mTLS or token) and **authz** (per-method, per-tenant).
- Decide **transcoding** up front: if browser clients exist, either grpc-web (binary) or gRPC-JSON transcoding (via `google.api.http` annotations + gateway).
- Use **field masks** for partial updates (`google.protobuf.FieldMask`) rather than sentinel values.

**Must Not:**
- Recycle retired field numbers — reserve them with `reserved N;`.
- Use `string` for IDs where a `bytes` or typed ID would catch misuse.
- Use unbounded streaming without deadlines and flow control.
- Design a wide "god message" — split by responsibility and use composition.
- Mix REST-style HTTP semantics into gRPC without intent (gRPC status is NOT HTTP status).
- Accept unbounded retries — amplifies load during an incident.
- Skip a load-balancing strategy for gRPC (sticky L4 balancing starves backends; prefer L7 / client-side / mesh).

## Instructions

Work through eight dimensions:

1. **Proto style & layout**: file organization, package naming (`<org>.<domain>.<version>`), versioning (`v1alpha`, `v1`, `v2`), import hygiene.
2. **Service / method shape**: RPC naming, single-responsibility, request/response message boundaries, pagination (`page_size` + `page_token`, not `offset`).
3. **Streaming decisions**: per-method — justify streaming vs unary.
4. **Error model**: `google.rpc.Status` usage, error detail types, client guidance.
5. **Deadlines, retries, backoff**: defaults, idempotency marking, hedging.
6. **Evolution rules**: breaking-change policy, `buf breaking` in CI, `reserved` discipline.
7. **Authn / authz**: transport (mTLS), application-layer token, per-method authz.
8. **Transcoding & gateway**: grpc-web, gRPC-JSON transcoder (envoy), REST clients.

## Output Format

```
# gRPC Service Review — <Package / Service>

## Summary
- Package: <org.domain.v1>
- Services: <N>  Methods: <N>
- Streaming methods: <N>
- Evolution maturity: <sound / ad hoc / broken>

## Findings by Dimension

### 1. Proto Style & Layout
- **State**: <evidence>
- **Gaps**: <list>
- **Recommendation**: <specific>
- **Effort**: S / M / L

### 2. Service / Method Shape
...

## Breaking-Change Risk Audit
| Method | Field change | Risk | Recommended action |
|--------|-------------|------|-------------------|
| Foo.Update | added required | breaking | add as optional, deprecate later |
...

## Evolution Plan (next 3 months)
- <additive-only commits>
- <deprecations with sunset>
- <next package version: v2 timing>

## Governance
- buf config: <ruleset>
- CI: `buf lint` + `buf breaking` required on PR
- Publication: <buf.build / internal registry>
```

## Verification (Self-Check)

Before emitting:

1. All 8 dimensions addressed.
2. Every streaming decision is justified (not default).
3. Error model is consistent with `google.rpc.Status` + Code.
4. Deadline defaults and propagation rules stated.
5. Retry policy references idempotency.
6. Evolution rules include `buf breaking` gating.
7. Browser client path is explicit if clients exist.
8. Confidence per finding (High if inspected .proto; Medium if inferred from service code).

## False-Positive Prevention

Rule out:

- **"Use streaming"** — Unary + pagination is usually simpler and better cacheable. Only stream when the use case needs it (large result, push notifications, interactivity).
- **"Ad hoc error strings are fine"** — Not for external / partner APIs; rich error details make them parseable.
- **"Retries solve reliability"** — Only for **idempotent** RPCs. Non-idempotent retries duplicate side effects.
- **"Migrate from REST to gRPC"** — Only if performance, streaming, or schema evolution needs outweigh browser / CLI / tooling ecosystem of REST.
- **"Field masks are optional"** — For `Update` with partial-fields, they're essential; PATCH semantics on gRPC rely on them.
- **"L4 LB is fine for gRPC"** — No — single connection pins, backends starve. Use L7 / client-side / mesh.

Cap confidence at **Medium** if `.proto` files were not directly inspected; Low if only service description provided.

## Techniques Applied

ST-01, ST-02, ST-03, RT-02 (8-dimension), RT-05, CM-02, QA-01.
