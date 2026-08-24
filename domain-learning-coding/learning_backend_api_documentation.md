---
title: "Backend API Documentation Generator — Endpoints, Auth, Errors, and Integration Examples"
category: "learning-coding"
description: "Generate accurate, consumer-ready documentation for a backend API — endpoints, request/response schemas, authentication, error handling, and integration examples — from the actual route and handler code, so frontend developers and third-party integrators can use the service correctly."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - api-documentation
  - backend
  - rest
  - developer-experience
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_frontend_component_documentation.md
  - domain-learning-coding/learning_backend_code_analysis.md
  - domain-software-engineering/api/api_rest_design_review.md
  - domain-software-engineering/api/api_openapi_linting_governance.md
---

# Backend API Documentation Generator

**Objective:** Produce accurate, consumer-ready documentation for a backend API — endpoints, request/response schemas, authentication, error handling, and integration examples — derived from the actual route and handler code rather than guessed conventions.

**When to use:**
- Documenting a public or partner-facing API before release.
- Generating internal service docs to onboard frontend developers or other teams.
- Teaching a learner how an existing API is structured by walking its real endpoints.
- Producing a first-draft OpenAPI/Swagger-style reference from source.

**When NOT to use:**
- Designing a new API from scratch — use `domain-software-engineering/api/api_rest_design_review.md`.
- Auditing an API for design or security flaws — use the analysis prompts.
- When you have no access to the route/handler code and would have to invent endpoints.

**Audience:** Backend developers, platform/DevEx teams, technical writers, and learners studying an existing API.

---

## Inputs / Context

The user supplies:
1. **The API source** — route definitions, controllers/handlers, DTOs/validators, and auth middleware, pasted wrapped in a named tag, e.g. `<api>...</api>`, or a clear reference (framework + file paths).
2. **Framework / language** (Express, NestJS, FastAPI, Spring, etc.).
3. **Audience for the docs** (internal devs, public consumers, partners) so depth and tone can be calibrated.
4. **Auth model** if not evident from the code (API key, OAuth, JWT, session).
5. **Optional:** base URL, versioning scheme, rate limits, existing examples.

Reference the pasted source by its tag name (e.g. "the `POST /orders` handler in `<api>`") when documenting each endpoint.

---

## Constraints

### Must
- Document only endpoints, parameters, and fields that exist in the supplied code; if a detail (e.g. a status code or rate limit) is not in the code, mark it as **"unconfirmed — verify"** rather than stating it.
- Derive request/response schemas from the actual DTOs, validators, or serializers in the source.
- Document the real authentication and authorization requirements (scopes, guards, middleware) as written.
- Provide at least one working integration example (cURL plus one language) per representative endpoint.
- Document the error response shape using the code's actual error format.

### Must Not
- Invent endpoints, fields, status codes, query parameters, or error codes not present in the source.
- Assume standard REST conventions the code does not follow (e.g. claiming `PUT` is idempotent if the handler isn't).
- Copy example payloads that contradict the documented schema.
- Hardcode real secrets or credentials in examples.

---

## Instructions

1. **Inventory endpoints.** From `<api>`, list every route: HTTP method, path, path/query parameters, and one-line purpose. Group by resource. Flag any route whose behavior you cannot determine from the code.
2. **Document requests.** For each endpoint, extract required/optional headers, path and query parameters (with constraints), and the request body schema from the DTO/validator. Note content types.
3. **Document responses.** Extract success status codes and response body schemas from the serializers/return statements. Capture pagination, rate-limit, and caching headers if the code sets them.
4. **Document auth.** State the authentication method and any per-endpoint scope/permission/guard exactly as enforced in the code. Describe token acquisition only if that flow is in the source; otherwise mark it unconfirmed.
5. **Document errors.** Extract the actual error envelope and enumerate the error codes the handlers can emit, with their triggering conditions and resolutions.
6. **Write integration examples.** Provide a cURL command and one language example per representative endpoint, using payloads consistent with the documented schema. Include a retry/backoff example for transient errors if the code surfaces them.
7. **Self-check (verification).** Re-read each documented field against the source: does every field, status code, and scope trace to a line in `<api>`? Have you marked everything unconfirmed that you could not verify?

---

## False-Positive Prevention

❌ **DON'T:**
- Describe an endpoint's behavior you haven't traced through its handler.
- Invent fields, query parameters, status codes, or error codes to make the docs feel complete.
- Assume REST idioms (idempotency, standard status codes) the code doesn't actually implement.
- State rate limits, SLAs, or versioning that aren't in the source.
- Assume the reader knows the framework's conventions — spell out what's framework-specific.

✅ **DO:**
- Trace each route to its handler and each field to its DTO/validator before documenting it.
- Mark anything you can't confirm from the code as "unconfirmed — verify."
- Keep example payloads schema-consistent and free of real secrets.
- Calibrate depth to the stated audience (public consumers need more onboarding than internal teams).
- Document the actual error envelope, not a generic one.

---

## Output Format

```
# [Resource] API Documentation

## Overview
- Base URL: [... or "unconfirmed — verify"]
- Authentication: [method from code]
- Versioning / rate limits: [from code, or "unconfirmed — verify"]

## Authentication
[Method, token acquisition if in source, header format]

## Endpoints

### [Method] [path]
[One-line purpose] — Auth: [scope/guard from code]

#### Request
- Headers: [table]
- Path / query params: [table with constraints]
- Body: [schema from DTO/validator]

**Example (cURL):**
```bash
[request]
```

#### Response
- Success ([code]): [schema]
- Errors: [codes + conditions]

## Error Handling
[Actual error envelope + error-code table]

## Code Examples
[cURL + one language per representative endpoint]
```

---

## Example Output

```markdown
# Orders API Documentation

## Overview

The Orders API allows you to create, retrieve, and list customer orders.

**Base URL:** `https://api.example.com/v1`
**Authentication:** Bearer token (JWT)
**Rate Limit:** 100 requests/minute per API key *(unconfirmed — verify against gateway config)*

---

## Authentication

All requests require a Bearer token in the `Authorization` header.

### Obtaining a Token

```bash
curl -X POST https://api.example.com/v1/auth/token \
  -H "Content-Type: application/json" \
  -d '{
    "client_id": "your_client_id",
    "client_secret": "your_client_secret"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

Include the token in subsequent requests: `Authorization: Bearer <token>`

---

## Endpoints

### Create Order

Creates a new order for a customer.

**Endpoint:** `POST /orders` — Auth: required (scope: `orders:write`)

#### Request

**Headers:**
| Header | Required | Description |
|--------|----------|-------------|
| Authorization | Yes | Bearer token |
| Content-Type | Yes | `application/json` |
| Idempotency-Key | Recommended | Unique key for idempotent requests |

**Body Parameters** (from `CreateOrderDto`):
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| customer_id | string | Yes | Customer identifier |
| items | array | Yes | Array of order items |
| items[].product_id | string | Yes | Product identifier |
| items[].quantity | integer | Yes | Quantity (min: 1) |
| shipping_address | object | Yes | Shipping address |
| shipping_address.street | string | Yes | Street address |
| shipping_address.city | string | Yes | City |
| shipping_address.postal_code | string | Yes | Postal code |
| shipping_address.country | string | Yes | ISO country code |
| notes | string | No | Order notes (max: 500 chars) |

**Example Request:**
```bash
curl -X POST https://api.example.com/v1/orders \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: unique-request-123" \
  -d '{
    "customer_id": "cust_abc123",
    "items": [
      { "product_id": "prod_xyz789", "quantity": 2 },
      { "product_id": "prod_def456", "quantity": 1 }
    ],
    "shipping_address": {
      "street": "123 Main St",
      "city": "San Francisco",
      "postal_code": "94102",
      "country": "US"
    },
    "notes": "Please leave at door"
  }'
```

#### Response

**Success (201 Created):**
```json
{
  "id": "ord_1234567890",
  "status": "pending",
  "customer_id": "cust_abc123",
  "items": [
    { "product_id": "prod_xyz789", "name": "Wireless Mouse", "quantity": 2, "unit_price": 29.99, "total": 59.98 },
    { "product_id": "prod_def456", "name": "USB-C Cable", "quantity": 1, "unit_price": 12.99, "total": 12.99 }
  ],
  "subtotal": 72.97,
  "tax": 6.57,
  "shipping": 5.99,
  "total": 85.53,
  "currency": "USD",
  "created_at": "2024-01-15T10:30:00Z"
}
```

---

### Get Order

**Endpoint:** `GET /orders/{order_id}` — Auth: required (scope: `orders:read`)

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| order_id | string | Order identifier (e.g., `ord_1234567890`) |

**Not Found (404):**
```json
{ "error": { "code": "order_not_found", "message": "Order with ID 'ord_invalid' not found", "request_id": "req_abc123xyz" } }
```

---

### List Orders

**Endpoint:** `GET /orders` — Auth: required (scope: `orders:read`)

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| customer_id | string | - | Filter by customer |
| status | string | - | `pending`, `processing`, `shipped`, `delivered`, `cancelled` |
| page | integer | 1 | Page number |
| per_page | integer | 20 | Items per page (max: 100) |
| sort | string | `-created_at` | Sort field (prefix `-` for descending) |

**Success (200 OK):**
```json
{
  "data": [ /* order objects */ ],
  "pagination": { "page": 1, "per_page": 10, "total_items": 47, "total_pages": 5 }
}
```

---

## Error Handling

All errors use this envelope (from the global exception filter):

```json
{
  "error": {
    "code": "error_code",
    "message": "Human-readable error message",
    "details": [ /* optional array of specific issues */ ],
    "request_id": "req_abc123xyz"
  }
}
```

| Code | HTTP Status | Description | Resolution |
|------|-------------|-------------|------------|
| `validation_error` | 400 | Field validation failed | See `details` |
| `unauthorized` | 401 | Missing/invalid token | Refresh access token |
| `forbidden` | 403 | Insufficient scope | Check required scopes |
| `not_found` | 404 | Resource doesn't exist | Verify the ID |
| `rate_limited` | 429 | Too many requests | Back off and retry |

### Retry Strategy (transient errors)

```javascript
async function fetchWithRetry(url, options, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    const response = await fetch(url, options);
    if (response.ok) return response;
    if (response.status === 429 || response.status >= 500) {
      await new Promise(r => setTimeout(r, Math.pow(2, attempt) * 1000));
      continue;
    }
    throw new Error(`API error: ${response.status}`);
  }
  throw new Error('Max retries exceeded');
}
```

---

## Code Examples

### JavaScript (Node.js)
```javascript
const axios = require('axios');
const api = axios.create({
  baseURL: 'https://api.example.com/v1',
  headers: { Authorization: `Bearer ${process.env.API_TOKEN}`, 'Content-Type': 'application/json' }
});
async function createOrder(customerId, items, shippingAddress) {
  const { data } = await api.post('/orders', { customer_id: customerId, items, shipping_address: shippingAddress });
  return data;
}
```

### Python
```python
import requests

class OrdersAPI:
    def __init__(self, api_token):
        self.base_url = "https://api.example.com/v1"
        self.headers = {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}

    def create_order(self, customer_id, items, shipping_address):
        r = requests.post(f"{self.base_url}/orders", headers=self.headers,
                          json={"customer_id": customer_id, "items": items, "shipping_address": shipping_address})
        r.raise_for_status()
        return r.json()
```
```

---

## Verification

- [ ] Every documented endpoint exists in the supplied source.
- [ ] Request/response schemas trace to actual DTOs/validators/serializers.
- [ ] Auth requirements (scopes/guards) match what the code enforces.
- [ ] Error envelope and codes match the code's actual error handling.
- [ ] Each representative endpoint has a working cURL + one language example.
- [ ] No secrets are hardcoded in examples.
- [ ] Anything unverifiable from the code is marked "unconfirmed — verify."

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Locks the goal to accurate, source-derived API docs.
- **ST-02 (Structured Sequential Instructions):** Inventory → request → response → auth → errors → examples → verify.
- **ST-03 (Output Format Specification):** Fenced template fixes the documentation structure.
- **RT-05 (Evidence-Based Reasoning):** Requires every field and code to trace to a line in the source.
- **QA-01 (Self-Verification):** Final pass re-checks each documented detail against the code.

---

## Related Prompts

- `domain-learning-coding/learning_frontend_component_documentation.md` — Document the frontend consumers of these APIs.
- `domain-learning-coding/learning_backend_code_analysis.md` — Analyze the backend before documenting it.
- `domain-software-engineering/api/api_rest_design_review.md` — Review the API's design quality.
- `domain-software-engineering/api/api_openapi_linting_governance.md` — Govern and lint the resulting OpenAPI spec.
