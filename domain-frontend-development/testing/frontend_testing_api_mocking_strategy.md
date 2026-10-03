---
title: "Frontend API Mocking Strategy — One Network-Level Mock Layer Across Tests, Stories and Dev, Typed Handlers, Drift Detection, and Error-State Coverage"
category: frontend-development/testing
description: "Design or review how a frontend fakes its back end: mock at the network boundary with one handler set shared by unit, component, Storybook, local development and selected end-to-end tests, type and validate handlers and fixtures against the real API contract so drift fails the build, make unhandled requests fail loudly, cover error and slow states deliberately, and decide which end-to-end journeys must hit a real back end."
techniques:
  - RT-02
  - DP-07
  - AG-12
  - DS-06
difficulty: intermediate
tags:
  - api-mocking
  - mock-service-worker
  - test-fixtures
  - mock-drift
  - storybook
  - integration-testing
  - tests-pass-but-app-is-broken
  - fake-data-out-of-date
  - test-error-states
updated: "2026-10-03"
related_prompts:
  - domain-frontend-development/react/frontend_react_testing.md
  - domain-software-engineering/testing/testing_contract_test_design.md
  - domain-frontend-development/testing/frontend_testing_playwright.md
---

# Frontend API Mocking Strategy

**Objective:** Replace a patchwork of `jest.mock('axios')`, hand-written JSON files and
per-test stubs with one network-level mock layer whose handlers and fixtures are checked
against the real API contract — so tests fail when the back end changes shape, every
important error and loading state is exercised on purpose, and the team knows which few
journeys still need a real back end.

**When to Use:**
- Tests were green but production broke because the API response changed shape.
- The same endpoint is mocked three different ways in unit tests, Storybook and E2E.
- Error, empty, slow and permission-denied states are untested or only tested by hand.
- Developers cannot run the UI without the full back-end stack.
- **Not this prompt if** you need test-runner setup and Testing Library patterns for a
  React app — use `domain-frontend-development/react/frontend_react_testing.md` (it shows
  how to install and wire a mock server; this prompt decides what the mock layer is and
  how it stays truthful). For consumer-driven contract tests between services, use
  `domain-software-engineering/testing/testing_contract_test_design.md`. For Playwright
  architecture and CI, use
  `domain-frontend-development/testing/frontend_testing_playwright.md`.

## Inputs / Context

1. **Endpoint list** the frontend calls (path, method, response shapes, status codes).
2. **API contract source**: OpenAPI/GraphQL schema, shared types, or none.
3. **Current mocking inventory**: module mocks of the HTTP client, MSW-style handlers,
   JSON fixtures, Storybook decorators, Playwright route interception, dev proxies.
4. **Test layers in use**: unit, component/integration, Storybook/visual, E2E, local dev.
5. **Incident history**: production bugs that tests should have caught.
6. **Library versions** (e.g. the mock server library's major version changed its
   handler API — verify against current docs).

## Method

1. **Inventory mocks per layer (RT-02).** For each endpoint and layer, record how it is
   faked: module mock, network-level handler, fixture file, route interception, or real.
   Count distinct mock implementations per endpoint; more than one is a drift risk.
2. **Mock at the network boundary.** Prefer request interception (a service-worker or
   Node interceptor such as MSW) over mocking the HTTP client module: the app's real
   client code, headers, serialization and error handling then run in tests. Keep module
   mocks only for non-HTTP dependencies.
3. **One handler set, many consumers.** Define handlers once and reuse them in unit and
   component tests (Node), Storybook (browser), local development (browser worker) and
   any E2E runs that mock. Tests override per case (`use`-style overrides) and reset
   after each test.
4. **Tie handlers to the contract.** Type handler responses with the generated API types
   and build fixtures with factories that fill required fields. In CI, validate every
   fixture against the schema (or against a runtime schema), so a renamed or reshaped
   field fails the build. Optionally record real responses from staging nightly and
   validate them against the same schema.
5. **Fail loudly on unhandled requests.** Configure the mock server to error on any
   request without a handler; silent pass-through hides missing mocks and real network
   calls in CI.
6. **Predict and cover failure states (DP-07).** For each critical endpoint, decide which
   states must be tested: 401 (session expired), 403, 404, 409 conflict, 422 validation
   with field errors, 429 with retry-after, 500, network failure, timeout/slow (delay
   handlers), empty list, last page. Build them as named handler variants.
7. **Decide what stays real.** Keep a small set of E2E journeys (sign-in, purchase,
   the one integration that has broken before) against a real back end in a staging
   environment; mock everything else. State the reason per journey.
8. **Define health metrics (AG-12) and prioritise (DS-06).** Metrics: endpoints with
   typed handlers ÷ endpoints called; distinct mock implementations per endpoint (target
   1); fixtures failing schema validation (target 0); unhandled-request errors in CI
   (target 0); critical endpoints with error-state coverage. Prioritise by incident
   history and endpoint criticality. Confidence: High = measured from code/CI, Medium =
   sampled, Low = from interviews.

## Output Format

```
# API mocking strategy — [app]   Endpoints: [n]   Date: [..]

## Current inventory
| Endpoint | Unit | Component | Storybook | E2E | Dev | Implementations |
## Target architecture
Layer → handler source → override mechanism → reset rule
## Contract linkage
Types source: [..]  Fixture validation: [..]  Real-response check: [..]
## Error-state coverage
| Endpoint | 401 | 403 | 404 | 409 | 422 | 429 | 500 | network | slow | empty |
## Real-back-end journeys
| Journey | Why real | Environment | Frequency |
## Metrics
| Metric | Today | Target |
## Migration plan
| Step | Scope | Order | Effort |
## Findings
| ID | Finding | Severity | Confidence | Evidence | Fix |
```

## Verification

- [ ] Every endpoint appears in the inventory with its mock implementation count.
- [ ] Handler responses are typed from the contract source, or the gap is stated.
- [ ] Fixture validation runs in CI and fails the build.
- [ ] Unhandled requests error in every test layer.
- [ ] Critical endpoints have named error-state handlers.
- [ ] Real-back-end journeys each have a stated reason.
- [ ] Metrics have current values and targets.

## False-Positive Prevention

1. **Mocking everything as best practice.** Some journeys must hit a real back end or
   integration bugs are invisible by construction.
2. **Network mocks as contract tests.** Typed handlers catch shape drift in fixtures; they
   do not prove the server behaves as the contract says. Pair with contract tests where
   the risk warrants it.
3. **Module mocks as always wrong.** Mocking a non-HTTP SDK or a date source at module
   level is fine; the problem is mocking the HTTP client and skipping the app's own
   request code.
4. **Happy-path fixtures as coverage.** A 200 with a full object is the least likely
   state to break the UI.
5. **Shared mutable fixtures.** One test mutating a fixture object breaks another;
   factories should return fresh objects.
6. **Handler API from memory.** Mock-library APIs changed between majors; check the
   installed version before recommending code.

## Example Output

```
# API mocking strategy — "Larkspur" field-service scheduling SPA (React)   Endpoints: 41

## Current inventory (excerpt)
| GET /jobs          | jest.mock(axios) | MSW (v1 style) | JSON file | real staging | none | 3 |
| PATCH /jobs/:id    | jest.mock(axios) | none           | none      | real staging | none | 1 |
| GET /technicians   | factory          | MSW            | JSON file | page.route   | none | 4 |
Totals: 41 endpoints; 17 with ≥3 implementations; 0 validated against the OpenAPI spec.

## Incident that motivated this
Release 5.2: back end changed job.price from number to { amount, currency }. All 212 tests
green (3 mocks still returned numbers); production list rendered "[object Object]" for 3 h.

## Target architecture
src/mocks/handlers/* (typed from openapi-typescript output) → used by Vitest (Node), Storybook
(MSW addon), `npm run dev:mock` (browser worker), and 14 mocked Playwright specs.
Overrides via server.use in tests; resetHandlers after each test; onUnhandledRequest: "error".

## Contract linkage
Types: generated from openapi.yaml on every build. Fixtures: factories; CI validates every
fixture against the spec's JSON Schema (fails build). Nightly: 20 recorded staging responses
validated against the same schema.

## Error-state coverage (critical endpoints)
| PATCH /jobs/:id | ✓ | ✓ | ✓ | ✓ (stale version) | ✓ (field errors) | — | ✓ | ✓ | ✓ | — |
| GET /jobs       | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ |

## Real-back-end journeys
| Sign in (SSO)          | redirect chain cannot be mocked faithfully | staging | every merge |
| Assign job → notify    | broke twice at the queue integration       | staging | every merge |
| Offline sync replay    | conflict resolution is server logic        | staging | nightly |

## Metrics
| Typed handlers / endpoints      | 0/41  | 41/41 |
| Endpoints with >1 mock impl.    | 17    | 0 |
| Fixtures failing schema         | n/a   | 0 |
| Unhandled requests in CI        | unknown (pass-through) | 0 |

## Migration plan
1. Handlers for the 12 most-called endpoints + unhandled=error (week 1).
2. Fixture schema validation in CI (week 1). 3. Replace axios module mocks (weeks 2–3).
4. Storybook and dev mode on shared handlers (week 3). 5. Error-state variants (week 4).
Confidence: inventory High (code search); effort Medium (estimated from 12-endpoint spike).
```

## Techniques Used

- **RT-02 Multi-Dimensional Analysis Framework** — every endpoint assessed per test layer, contract linkage and error coverage.
- **DP-07 Failure Mode Prediction** — the error states each endpoint can produce are listed before handlers are written.
- **AG-12 Quantitative Success Metrics** — typed-handler coverage, implementations per endpoint, schema failures and unhandled requests with targets.
- **DS-06 Prioritization and Severity Guidance** — migration ordered by incident history and endpoint criticality.

## Related Prompts

- `domain-frontend-development/react/frontend_react_testing.md` — test-runner and Testing Library mechanics that consume these handlers.
- `domain-software-engineering/testing/testing_contract_test_design.md` — proving the server honours the contract the mocks are typed from.
- `frontend_testing_playwright.md` — E2E architecture for the journeys that stay real.
