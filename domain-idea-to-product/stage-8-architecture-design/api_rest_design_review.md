---
title: "REST API Design Review"
category: api-design
description: "REST API Design Review"
tags:
  - api-design
  - review
updated: "2026-03-19"
---

# REST API Design Review

**Objective:** Analyze REST API designs for adherence to best practices, consistency, usability, and alignment with REST architectural constraints to produce well-designed, developer-friendly APIs.

**When to Use:** Use this prompt when designing new REST APIs, reviewing existing API endpoints, preparing for API releases, onboarding teams to API design standards, or auditing APIs for consistency and quality.

**Instructions:**

1. **Analyze Resource Modeling**
   - Evaluate resource naming conventions (nouns, plural forms)
   - Check for proper resource hierarchy and nesting
   - Assess URL structure clarity and predictability
   - Identify any verb-based endpoints that should be resources
   - Review collection vs. individual resource patterns
   - Evaluate sub-resource relationships

2. **Review HTTP Method Usage**
   - Verify correct HTTP verb usage (GET, POST, PUT, PATCH, DELETE)
   - Check for method idempotency compliance
   - Assess safe method usage (GET, HEAD, OPTIONS)
   - Identify any method override patterns and their necessity
   - Review OPTIONS and HEAD implementation

3. **Evaluate Response Design**
   - Check HTTP status code usage and appropriateness
   - Analyze response body structure consistency
   - Review error response format standardization
   - Assess pagination implementation (offset, cursor, keyset)
   - Evaluate filtering, sorting, and field selection patterns
   - Check for HATEOAS/hypermedia implementation where appropriate

4. **Assess Request Design**
   - Review request body structure and validation
   - Check query parameter naming conventions
   - Analyze header usage patterns
   - Evaluate content negotiation support
   - Review request size limits and handling

5. **Security Analysis**
   - Check authentication mechanism appropriateness (OAuth2, API keys, JWT)
   - Review authorization patterns and scope definitions
   - Assess rate limiting implementation
   - Evaluate input validation completeness
   - Check for sensitive data exposure in URLs or responses
   - Review CORS configuration

6. **Performance Considerations**
   - Analyze caching strategy (ETags, Cache-Control)
   - Review compression support
   - Check for N+1 query patterns in responses
   - Assess bulk operation support
   - Evaluate async operation patterns for long-running tasks

7. **Developer Experience**
   - Check documentation completeness
   - Review error message clarity and actionability
   - Assess consistency across endpoints
   - Evaluate SDK/client generation friendliness
   - Review versioning clarity

**Expected Output:** A comprehensive REST API design review report including:
- Overall design quality score (1-10)
- Resource model diagram or summary
- Prioritized list of issues with severity ratings
- Specific recommendations with before/after examples
- Best practice alignment assessment
- Developer experience evaluation

**Example Output:**

```markdown
## REST API Design Review Report

### Summary
- **API Name**: Order Management API v2
- **Endpoints Reviewed**: 23
- **Design Quality Score**: 7.2/10
- **Critical Issues**: 2
- **Improvements Identified**: 11

### Resource Model Assessment

#### Current Structure
```
/api/v2/orders
/api/v2/orders/{id}
/api/v2/orders/{id}/items
/api/v2/customers/{id}/orders
/api/v2/getOrderStatus/{id}        # Issue: Verb in URL
/api/v2/order-cancel               # Issue: Action as resource
```

#### Recommended Structure
```
/api/v2/orders
/api/v2/orders/{orderId}
/api/v2/orders/{orderId}/items
/api/v2/orders/{orderId}/items/{itemId}
/api/v2/orders/{orderId}/status    # GET for status
/api/v2/orders/{orderId}/cancel    # POST for action (or PATCH to /orders/{id})
/api/v2/customers/{customerId}/orders
```

### Critical Issues

#### Issue 1: Inconsistent Resource Naming (HIGH)
**Location**: Multiple endpoints
**Problem**: Mix of singular/plural and verb-based URLs
**Current**:
- `GET /api/v2/getOrderStatus/{id}` - Verb in URL
- `POST /api/v2/order-cancel` - Action as resource name

**Recommended**:
- `GET /api/v2/orders/{orderId}/status` - Resource-based
- `POST /api/v2/orders/{orderId}/cancel` - Action on resource

**Rationale**: REST uses nouns (resources), not verbs. Actions on resources should use HTTP methods or sub-resources.

#### Issue 2: Missing Standard Error Format (HIGH)
**Problem**: Inconsistent error responses across endpoints
**Current Responses**:
```json
// Endpoint A
{"error": "Not found"}

// Endpoint B
{"message": "Order not found", "code": 404}

// Endpoint C
{"errors": [{"field": "email", "message": "Invalid"}]}
```

**Recommended Standard Format (RFC 7807)**:
```json
{
  "type": "https://api.example.com/errors/order-not-found",
  "title": "Order Not Found",
  "status": 404,
  "detail": "Order with ID 12345 does not exist",
  "instance": "/orders/12345",
  "traceId": "abc-123-xyz"
}
```

### HTTP Method Compliance

| Endpoint | Current Method | Issue | Recommendation |
|----------|---------------|-------|----------------|
| /orders | GET | None | Correct |
| /orders/{id} | GET | None | Correct |
| /orders | POST | None | Correct |
| /orders/{id} | POST | Wrong method for update | Use PUT or PATCH |
| /orders/{id}/cancel | GET | Side effect on GET | Use POST |

### Response Design Analysis

#### Pagination Assessment
**Current**: Offset-based pagination
```json
{
  "data": [...],
  "page": 1,
  "pageSize": 20,
  "total": 150
}
```

**Issue**: Offset pagination has performance issues at scale and inconsistency with concurrent writes.

**Recommended**: Cursor-based pagination for large datasets
```json
{
  "data": [...],
  "pagination": {
    "cursors": {
      "after": "eyJpZCI6MTAwfQ==",
      "before": "eyJpZCI6ODJ9"
    },
    "hasNextPage": true,
    "hasPreviousPage": true
  }
}
```

### Security Checklist

| Check | Status | Notes |
|-------|--------|-------|
| Authentication | PASS | OAuth2 with JWT properly implemented |
| Authorization | WARN | Missing scope validation on 3 endpoints |
| Rate Limiting | PASS | 1000 req/min with headers |
| Input Validation | WARN | Missing validation on 2 POST bodies |
| HTTPS Only | PASS | All endpoints enforce HTTPS |
| Sensitive Data in URL | FAIL | PII in query params on /search |

### Performance Recommendations

1. **Add ETags for Caching** (Medium Priority)
   - Currently no caching headers on GET /orders/{id}
   - Add `ETag` and support `If-None-Match` for conditional requests
   - Expected: 30-40% reduction in bandwidth for unchanged resources

2. **Implement Compression** (Low Priority)
   - Add `Accept-Encoding: gzip` support
   - Response size reduction: ~70% for JSON payloads

3. **Add Bulk Operations** (High Priority)
   - Currently requires N requests for N updates
   - Add `PATCH /orders/batch` for bulk status updates
   - Expected: 90% reduction in requests for bulk operations

### Developer Experience Score

| Aspect | Score | Notes |
|--------|-------|-------|
| URL Intuitiveness | 6/10 | Some verb-based URLs confuse developers |
| Error Clarity | 5/10 | Inconsistent format, missing error codes |
| Documentation | 7/10 | Good coverage, missing examples |
| Consistency | 6/10 | Naming varies between endpoints |
| Discoverability | 4/10 | No HATEOAS, limited link relations |

### Action Plan

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| 1 | Standardize error response format | Medium | High |
| 2 | Rename verb-based endpoints | Small | High |
| 3 | Add authorization scopes | Medium | High |
| 4 | Implement cursor pagination | Medium | Medium |
| 5 | Add ETags for caching | Small | Medium |
| 6 | Add bulk operation endpoints | Large | High |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-02 (Multi-Dimensional Analysis)
- ST-03 (Structured Output Templates)
- DS-06 (Prioritization and Severity Guidance)
- RT-05 (Evidence-Based Reasoning)
- QA-01 (Explicit Verification Requirements)

**Related Prompts:**
- api_graphql_schema_analysis.md - For GraphQL API design review
- api_versioning_strategy.md - For API versioning decisions
- api_openapi_documentation.md - For generating API documentation
- code-analysis/security/security_api_security_testing.md - For API security testing
- code-analysis/architecture/architecture_api_client_generation.md - For API client code

**Customization Guide:**
- **For Internal APIs**: Reduce emphasis on documentation, focus on consistency
- **For Public APIs**: Increase emphasis on developer experience, versioning, and stability
- **For Microservices**: Add service mesh integration, circuit breaker patterns
- **For Mobile-First APIs**: Focus on payload size, offline support, field selection
- **For High-Traffic APIs**: Emphasize caching, rate limiting, pagination strategies


---

## Must / Must Not

**Must:**
- Cite concrete evidence (endpoint path, method, status code, request/response shape) for every finding.
- Classify each finding by severity: **Critical** (breaks clients or violates REST contract), **Major** (inconsistent or risky), **Minor** (stylistic), **Nit**.
- Distinguish between **public API** (external consumers, SemVer rules apply) and **internal API** (service-to-service, looser contract) in every recommendation.
- Label each recommendation with **Breaking**, **Non-Breaking**, or **Additive**.
- Produce the output in the exact structure specified above (Findings Table + Migration Checklist + Example Requests).

**Must Not:**
- Recommend breaking changes to a **public API** without proposing a versioning / deprecation path.
- Flag something as a "REST violation" based on dogma (e.g., "must use PUT for X") without citing the RFC or style guide that was violated.
- Invent endpoint behavior the code does not actually implement — verify against the source.
- Propose wholesale rewrites when the finding is isolated; prefer minimal targeted fixes.
- Recommend HATEOAS / hypermedia when the team has explicitly chosen JSON:API, OpenAPI, or plain-JSON conventions.

## Verification (Self-Check Before Reporting)

Before emitting findings, the model must confirm:

1. **Evidence cited** — Every Critical/Major finding references a specific endpoint path + HTTP method.
2. **Breaking-change risk identified** — Every proposed change is labeled Breaking / Non-Breaking / Additive with consumer-impact note.
3. **API stability context understood** — The review explicitly states whether this is a public, partner, or internal API (ask the user if unclear).
4. **Confidence marked** — Each Critical finding is labeled **High** / **Medium** / **Low** confidence based on how directly the code evidences it.
5. **No scope creep** — The review covers REST design; it does NOT critique application logic, database schema, or infrastructure except where they leak into the API contract.

## False-Positive Prevention

Before reporting any finding, rule out these common false positives:

- **"Should be PUT instead of POST"** — Verify POST is actually being used for idempotent update. If POST is creating a child resource, POST is correct.
- **"Inconsistent naming"** — Verify across multiple endpoints, not a single outlier — one endpoint may be legacy with a documented freeze.
- **"Missing pagination"** — Verify the endpoint actually returns collections. A single-object endpoint does not need pagination.
- **"Missing rate limiting"** — Rate limiting may be enforced at the gateway / ingress, not in the application code. Ask where the enforcement layer lives before flagging.
- **"Missing HATEOAS links"** — Only flag if the documented API style is hypermedia-driven. Most REST APIs deliberately do not use HATEOAS.
- **"No 201 for POST"** — Verify the response body; some POSTs correctly return 204 No Content or 200 with a body when creation is a side-effect.

If confidence drops below **Medium**, downgrade the finding severity rather than reporting a false Critical.
