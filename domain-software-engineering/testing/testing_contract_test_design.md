---
title: "Contract Test Design (OpenAPI / AsyncAPI / Pact)"
category: testing
description: "Design a contract-testing strategy for HTTP, gRPC, and event-driven services using OpenAPI, AsyncAPI, and consumer-driven contracts (Pact). Output a contract-test plan covering producer, consumer, and broker responsibilities."
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
  - testing
  - contract-testing
  - openapi
  - asyncapi
  - pact
  - consumer-driven-contracts
  - api-governance
  - microservices
updated: "2026-04-17"
related_prompts:
  - testing_integration_test_design.md
  - testing_e2e_test_scenario_creation.md
  - ../api/api_openapi_documentation.md
---

# Contract Test Design

**Objective:** Design a contract-testing strategy that catches integration breakage **before** deploy, covering HTTP (OpenAPI), event-driven (AsyncAPI), and bidirectional (gRPC) contracts. Choose between spec-driven and consumer-driven approaches based on team topology, deliver a concrete test plan, and define the CI/CD gating behavior.

## When to Use

- Microservices with 3+ services exchanging data.
- Producer-consumer teams that deploy independently.
- After a bug where "API changed and nobody told the consumer."
- Before public-API / partner-API release to establish a stability contract.
- When adopting event-driven architecture with Kafka / NATS / RabbitMQ / EventBridge.

**Do NOT use this prompt for:**
- Unit tests (use `testing_unit_test_generation.md`).
- End-to-end user-journey tests (use `testing_e2e_test_scenario_creation.md`).
- Load / stress tests (use `testing_performance_load_test_planning.md`).

## Inputs / Context

Collect:
- **Protocol mix**: REST, gRPC, GraphQL, Kafka, NATS, EventBridge, etc.
- **Team topology**: are producer and consumer owned by the same team, or different teams/orgs?
- **Release cadence**: do services deploy independently or in coordinated releases?
- **Spec source of truth**: OpenAPI / AsyncAPI / proto files — hand-maintained or code-generated?
- **Existing testing**: what's there now (integration, E2E, smoke)?
- **Broker availability**: for Pact, is a Pact Broker (or Pactflow) available or wanted?

## Must / Must Not

**Must:**
- Choose the right approach per boundary:
  - **Spec-driven** (OpenAPI / AsyncAPI validation) when the spec is authoritative and teams coordinate.
  - **Consumer-driven (Pact)** when consumers have diverse needs and producer should not break them.
  - **Schema registry** (Avro / Protobuf + Confluent / Buf) for event streams with evolution rules.
- Specify **producer-side** and **consumer-side** responsibilities separately.
- Define **breaking-change policy**: which changes are allowed under what conditions, with what notice.
- Include **CI/CD gating**: contract test failures must block deploy OR require explicit override.
- Differentiate **verification** (contract matches) from **can-i-deploy** (safe to ship given consumer state).

**Must Not:**
- Recommend Pact when a shared-team setup makes spec-driven testing simpler and sufficient.
- Use contract tests to replace E2E tests — they do NOT test business logic or multi-service workflows.
- Treat OpenAPI validation as "contract testing" without producer-side conformance checks (validator must check actual request/response against spec, not just document spec).
- Omit the consumer side for REST services — server-side validation alone leaves consumers blind to changes.
- Overlook **evolution policy** for events (forward / backward / full compatibility).

## Instructions

Work through four phases:

1. **Map boundaries**: For every inter-service boundary, identify protocol, stability need, team ownership, and release independence.
2. **Select approach** per boundary:
   - Shared-team + code-gen = spec-driven (OpenAPI validation in producer tests + consumer client regeneration).
   - Cross-team + REST/gRPC = Pact (consumer-driven).
   - Event streams = schema registry + compatibility rules (Avro/Proto).
   - Spec-first external API = OpenAPI linting + spec-conformance tests.
3. **Design the test matrix**:
   - Producer side: spec lint, spec conformance, consumer contract verification.
   - Consumer side: mock producer from contract, assert consumer accepts expected responses.
   - Broker: Pact broker / Buf Schema Registry / Confluent Schema Registry — which contracts flow where.
4. **Wire into CI/CD**: gating, `can-i-deploy`, contract publishing cadence, versioning.

## Output Format

```
# Contract Test Plan — <Service / System>

## Boundary Map
| Boundary | Protocol | Producer Team | Consumer Team(s) | Approach |
|----------|----------|---------------|------------------|----------|
| svc-a → svc-b | REST | team-x | team-y | Pact |
| svc-a → kafka:events.orders | Kafka/Avro | team-x | multiple | Schema Registry |
...

## Approach per Boundary

### svc-a → svc-b (Pact)
- **Consumer test**: <what consumer asserts>
- **Provider verification**: <how producer verifies>
- **Broker**: Pact Broker / Pactflow at <URL>
- **Publish cadence**: on every PR merge
- **can-i-deploy**: required gate on consumer deploy

### svc-a → kafka:events.orders (Schema Registry)
- **Schema source**: Avro files in `schemas/`
- **Evolution rule**: backward-compatible
- **Registry**: Confluent Schema Registry
- **CI gate**: `buf breaking` on PR

## CI/CD Integration
- Producer pipeline: ...
- Consumer pipeline: ...
- Gating: <which stage blocks deploy>
- Override mechanism: <who can skip and how>

## Breaking-Change Policy
- Allowed with: <deprecation notice window, version bump>
- Not allowed: <removing fields, changing types, renaming endpoints>

## Gaps vs Ideal
- <what we couldn't cover with contract tests — what still needs E2E / manual>
```

## Verification (Self-Check)

Before emitting:

1. Every inter-service boundary has an approach chosen AND justified.
2. Spec-driven vs consumer-driven decisions reference team topology.
3. CI gating is concrete (pipeline step, stage, fail-closed behavior).
4. Event-stream boundaries reference a compatibility rule (forward / backward / full).
5. The plan states explicitly what contract tests will NOT catch (business logic, multi-step flows) so teams don't over-trust.
6. Confidence per recommendation (High if team topology confirmed; Medium if inferred).

## False-Positive Prevention

Rule out:

- **"Use Pact for everything"** — Over-kill for single-team systems; adds broker + versioning burden.
- **"OpenAPI validation = contract tests"** — Only if the producer validates actual responses against the spec at test time, not just documents a spec.
- **"No need for E2E now"** — Contract tests DO NOT cover business logic; E2E still needed for user journeys.
- **"Schema registry solves events"** — Only enforces compatibility rules; semantic changes still slip through.
- **"Consumer-driven means consumer defines everything"** — Producer still owns the contract; consumer drives *what subset* they need.
- **"Pact broker always required"** — For 2-service setups, file-based contracts in Git can be enough.

Confidence must be **Medium** or higher for each approach recommendation; if team topology wasn't confirmed, ask before shipping the plan.

## Techniques Applied

ST-01, ST-02, ST-03, RT-02, RT-05, CM-02, QA-01.
