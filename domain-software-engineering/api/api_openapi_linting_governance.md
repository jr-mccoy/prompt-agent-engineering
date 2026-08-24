---
title: "OpenAPI Linting & Governance"
category: api
description: "Design an OpenAPI linting and governance program: ruleset selection (Spectral, Redocly), style guide authorship, CI enforcement, exception workflow, breaking-change detection, and documentation publishing pipeline."
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
  - openapi
  - governance
  - linting
  - spectral
  - redocly
  - style-guide
  - breaking-change
  - api-first
updated: "2026-04-17"
related_prompts:
  - api_openapi_documentation.md
  - api_rest_design_review.md
  - api_versioning_strategy.md
  - api_grpc_service_design.md
---

# OpenAPI Linting & Governance

**Objective:** Design an OpenAPI governance program: choose linting tooling (Spectral / Redocly / vacuum), codify the org's API style guide as a ruleset, wire lint + breaking-change checks into CI, define an exception workflow, and set up a documentation publishing pipeline so specs remain the single source of truth.

## When to Use

- Multiple teams produce OpenAPI specs and they drift in quality and style.
- API consumers complain about inconsistency ("service A returns errors this way, service B another way").
- Moving to an API-first workflow where specs must be authoritative.
- Before external / partner API launch — governance prevents embarrassment.
- When existing specs pass `openapi-cli` validation but miss organizational conventions.

**Do NOT use this prompt for:**
- Writing a single OpenAPI spec (use `api_openapi_documentation.md`).
- gRPC governance (use `api_grpc_service_design.md`).
- REST design review per-endpoint (use `api_rest_design_review.md`).
- API versioning strategy alone (use `api_versioning_strategy.md`).

## Inputs / Context

Collect:
- **Number of specs / services** governed by this program.
- **Team topology**: centralized platform team or federated service teams.
- **Existing style guide**: documented? enforced? ignored?
- **Existing tooling**: Spectral / Redocly / Stoplight / Postman / vacuum / none.
- **CI platform**: GitHub Actions / GitLab / Jenkins / CircleCI.
- **Spec lifecycle**: hand-written, code-generated, design-first, code-first.
- **Doc publishing**: ReadMe / Redocly / Swagger UI / custom portal.

## Must / Must Not

**Must:**
- Codify the org's API conventions as a **Spectral ruleset** (or equivalent). Examples to encode:
  - `operationId` required, unique, camelCase.
  - `description` required on paths, responses, and schemas > 3 fields.
  - Error response schema references the org's canonical `ErrorResponse`.
  - Pagination parameters follow `page_size` + `page_token` (cursor) or `limit` + `offset`.
  - No inline anonymous objects > N fields; use `$ref`.
  - Security scheme references required on protected operations.
  - Tags match the canonical tag list.
- Gate PRs with:
  - **Spec validation** (`openapi-cli` / `redocly lint`) — must pass.
  - **Style lint** (`spectral lint`) — must pass or exceptions approved.
  - **Breaking-change detection** (`openapi-diff` / `oasdiff` / Redocly `diff`) — must either be non-breaking, or go through explicit approval.
- Define an **exception workflow**: how a team can get a temporary waiver, who signs off, sunset date.
- Publish the style guide **as living documentation** next to the ruleset.
- Automate **doc publishing** on merge: generate site, include diff, archive prior versions.
- Distinguish **errors** (block CI) from **warnings** (informational) in the ruleset.

**Must Not:**
- Copy the default Spectral `oas` ruleset and call it a style guide — that's validation, not governance.
- Enforce rules teams never agreed to — build consensus BEFORE rollout.
- Flag style violations as Critical — they're typically Medium at most.
- Allow breaking changes to pass on "we'll tell consumers" — require semver bump OR a deprecation path.
- Ignore **generated specs** — they still need to lint clean; regenerate with conforming options.
- Tie governance to one vendor tool — the ruleset should be portable.

## Instructions

Work through six phases:

1. **Discovery**: inventory specs, versions, generators, current violations, team pain points.
2. **Style guide authorship**: 10–30 rules that encode the *most valuable* conventions. Err on fewer rules strictly enforced.
3. **Ruleset implementation**: write Spectral ruleset; include rule description, severity, rationale, good/bad examples.
4. **CI integration**:
   - Validate + lint on every PR.
   - Breaking-change gate with override mechanism.
   - Preview doc diff posted as PR comment.
5. **Exception workflow**: waiver request template, approver role, sunset date, tracking.
6. **Docs publishing**:
   - Auto-generated portal (Redocly / Stoplight / ReadMe) on merge.
   - Historical versions retained.
   - Change log from OpenAPI diff.

## Output Format

```
# OpenAPI Governance Plan — <Organization>

## Current State
- Specs in scope: <N>
- Teams: <N>
- Tooling: <current>
- Violations observed: <sample>

## Style Guide (Living Doc)
Top rules (30 max):
1. `operationId` required — rationale: ...
2. Pagination uses `page_size` + `page_token` — rationale: ...
...

## Spectral Ruleset Sketch
```yaml
extends: ["spectral:oas"]
rules:
  operation-operationId:
    description: operationId is required and camelCase
    severity: error
    given: "$.paths[*][*]"
    then:
      - field: operationId
        function: truthy
      - field: operationId
        function: pattern
        functionOptions:
          match: "^[a-z][a-zA-Z0-9]*$"
  # ... 10–30 rules
```

## CI Workflow
| Stage | Tool | Blocking? | Override |
|-------|------|-----------|----------|
| Validate | `redocly lint` | Yes | No override |
| Style lint (error) | `spectral lint` | Yes | PR waiver label + approver |
| Style lint (warn) | `spectral lint` | No | — |
| Breaking change | `oasdiff` / `redocly diff` | Yes on major versions | Versioned release path |
| Doc preview | Redocly | No | — (informational) |

## Exception Workflow
- Requester fills waiver template.
- Approver: API Platform team lead.
- Tracked in: <ticket tag / dashboard>.
- Sunset date: required; default 90 days.

## Publishing Pipeline
- Source: main branch of spec repo.
- Builder: Redocly CLI.
- Destination: <portal URL>.
- Versioning: path-prefixed `/v1/`, `/v2/`.
- Change log: generated from diff.

## Rollout Plan
1. Week 1–2: Publish style guide; run lint on all specs as info-only.
2. Week 3–4: Flip top 10 rules to blocking.
3. Month 2: Breaking-change gate active.
4. Month 3: Full ruleset blocking; exception workflow in use.
```

## Verification (Self-Check)

Before emitting:

1. Ruleset is finite (≤ 30 rules) and each rule has a rationale.
2. Every rule's severity is set consciously (error vs warn) — no default severities.
3. CI integration identifies what blocks vs what informs.
4. Exception workflow has named approver and sunset.
5. Breaking-change detection is separate from style lint.
6. Doc publishing pipeline is concrete (tool, trigger, destination).
7. Rollout plan is staged, not big-bang.
8. Confidence per recommendation (High if current state inspected; Medium if inferred).

## False-Positive Prevention

Rule out:

- **"Enforce every rule as error"** — Warning severity has a place; reserve error for rules the org actually committed to.
- **"Breaking changes allowed if we communicate"** — Not durable. Use semver + deprecation paths.
- **"One ruleset for all services"** — Internal vs external APIs may legitimately differ; use ruleset layers (base + overrides).
- **"Generated specs don't need governance"** — They do; wrong codegen options produce messy specs.
- **"Docs portal solves discovery"** — Only if specs are *trusted*; governance is what earns that trust.
- **"Spectral is the only tool"** — Redocly's ruleset / vacuum / `oasdiff` each have strengths; pick by org fit.

Cap confidence at **Medium** if the actual specs were not inspected.

## Techniques Applied

ST-01, ST-02, ST-03, RT-02 (6-phase), RT-05, CM-02, QA-01.
