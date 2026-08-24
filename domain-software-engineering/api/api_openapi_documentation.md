---
title: "OpenAPI/Swagger Documentation Generation"
category: api-design
description: "OpenAPI/Swagger Documentation Generation"
tags:
  - api-design
updated: "2026-03-19"
---

# OpenAPI/Swagger Documentation Generation

**Objective:** Generate comprehensive, accurate, and developer-friendly OpenAPI (Swagger) documentation that enables seamless API integration, client SDK generation, and automated testing.

**When to Use:** Use this prompt when creating API documentation from scratch, generating OpenAPI specs from existing code, improving existing documentation quality, preparing APIs for public release, or enabling automated API testing and client generation.

**Instructions:**

1. **Document API Overview**
   - Define API title, description, and version
   - Document server URLs (production, staging, sandbox)
   - Specify contact information and terms of service
   - Add license information
   - Create comprehensive API description with use cases

2. **Define Security Schemes**
   - Document authentication methods (OAuth2, API Key, Bearer, Basic)
   - Specify security requirements per endpoint
   - Document scope definitions for OAuth2
   - Include authorization flow examples
   - Add security requirement inheritance patterns

3. **Document Path Operations**
   - Define all endpoints with HTTP methods
   - Write clear operation summaries and descriptions
   - Document path parameters with constraints
   - Specify query parameters with defaults
   - Document request headers
   - Add operation IDs for SDK generation

4. **Define Request Bodies**
   - Create reusable schema components
   - Document required vs. optional fields
   - Add field descriptions and examples
   - Specify validation constraints (min, max, pattern)
   - Include content type specifications

5. **Document Response Schemas**
   - Define success response structures
   - Document error response formats
   - Include response headers
   - Add realistic examples
   - Document pagination patterns

6. **Add Examples and Use Cases**
   - Include request/response examples for each operation
   - Document common workflows
   - Add error scenario examples
   - Include SDK usage examples
   - Document rate limiting responses

7. **Enhance Documentation Quality**
   - Add tags for logical grouping
   - Include external documentation links
   - Document webhooks (if applicable)
   - Add deprecation notices
   - Include changelog references

**Expected Output:** A complete OpenAPI 3.0+ specification including:
- Info section with API metadata
- Server definitions for all environments
- Security scheme definitions
- Path operations with full documentation
- Reusable component schemas
- Comprehensive examples

**Example Output:**

```yaml
openapi: 3.0.3
info:
  title: Order Management API
  description: |
    ## Overview
    The Order Management API enables you to create, manage, and track customer orders
    throughout their lifecycle.

    ## Getting Started
    1. Obtain API credentials from the [Developer Portal](https://developers.example.com)
    2. Authenticate using OAuth2 or API Key
    3. Create your first order using POST /orders

    ## Rate Limiting
    - Standard tier: 1,000 requests/minute
    - Premium tier: 10,000 requests/minute
    - Rate limit headers included in all responses

    ## Versioning
    This API uses URI versioning. Current version: v2

    ## Support
    - Documentation: https://docs.example.com
    - Status: https://status.example.com
    - Email: api-support@example.com
  version: 2.1.0
  termsOfService: https://example.com/terms
  contact:
    name: API Support
    url: https://example.com/support
    email: api-support@example.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
  x-logo:
    url: https://example.com/logo.png
    altText: Example Company Logo

servers:
  - url: https://api.example.com/v2
    description: Production server
  - url: https://api-staging.example.com/v2
    description: Staging server
  - url: https://api-sandbox.example.com/v2
    description: Sandbox server (test data only)

tags:
  - name: Orders
    description: Order management operations
    externalDocs:
      description: Order lifecycle documentation
      url: https://docs.example.com/orders
  - name: Products
    description: Product catalog operations
  - name: Customers
    description: Customer management operations

security:
  - bearerAuth: []
  - apiKey: []

paths:
  /orders:
    get:
      tags:
        - Orders
      summary: List orders
      description: |
        Retrieve a paginated list of orders with optional filtering.

        ## Filtering
        Use query parameters to filter results:
        - `status`: Filter by order status
        - `customer_id`: Filter by customer
        - `created_after`: Filter by creation date

        ## Sorting
        Use `sort` parameter with field name. Prefix with `-` for descending.
        Example: `sort=-created_at`
      operationId: listOrders
      parameters:
        - name: status
          in: query
          description: Filter by order status
          required: false
          schema:
            type: string
            enum: [pending, confirmed, shipped, delivered, cancelled]
          example: pending
        - name: customer_id
          in: query
          description: Filter by customer ID
          required: false
          schema:
            type: string
            format: uuid
        - name: created_after
          in: query
          description: Filter orders created after this date (ISO 8601)
          required: false
          schema:
            type: string
            format: date-time
          example: "2024-01-01T00:00:00Z"
        - name: sort
          in: query
          description: Sort field (prefix with - for descending)
          required: false
          schema:
            type: string
            default: -created_at
          example: -created_at
        - $ref: '#/components/parameters/PageSize'
        - $ref: '#/components/parameters/PageCursor'
      responses:
        '200':
          description: Successful response with list of orders
          headers:
            X-RateLimit-Limit:
              $ref: '#/components/headers/X-RateLimit-Limit'
            X-RateLimit-Remaining:
              $ref: '#/components/headers/X-RateLimit-Remaining'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderListResponse'
              examples:
                success:
                  summary: Successful order list
                  value:
                    data:
                      - id: "ord_123abc"
                        status: "pending"
                        total: 9999
                        currency: "USD"
                        customer_id: "cus_456def"
                        created_at: "2024-01-15T10:30:00Z"
                    pagination:
                      has_more: true
                      next_cursor: "eyJpZCI6MTAwfQ=="
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '429':
          $ref: '#/components/responses/RateLimitExceeded'
        '500':
          $ref: '#/components/responses/InternalError'

    post:
      tags:
        - Orders
      summary: Create an order
      description: |
        Create a new order for a customer.

        ## Required Fields
        - `customer_id`: The customer placing the order
        - `items`: At least one order item

        ## Idempotency
        Use the `Idempotency-Key` header to safely retry requests.
        Keys are valid for 24 hours.
      operationId: createOrder
      parameters:
        - name: Idempotency-Key
          in: header
          description: Unique key for idempotent request (UUID recommended)
          required: false
          schema:
            type: string
            format: uuid
          example: "550e8400-e29b-41d4-a716-446655440000"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateOrderRequest'
            examples:
              basic:
                summary: Basic order
                value:
                  customer_id: "cus_456def"
                  items:
                    - product_id: "prod_789ghi"
                      quantity: 2
                  shipping_address:
                    line1: "123 Main St"
                    city: "San Francisco"
                    state: "CA"
                    postal_code: "94102"
                    country: "US"
              with_discount:
                summary: Order with discount code
                value:
                  customer_id: "cus_456def"
                  items:
                    - product_id: "prod_789ghi"
                      quantity: 2
                  discount_code: "SAVE20"
                  shipping_address:
                    line1: "123 Main St"
                    city: "San Francisco"
                    state: "CA"
                    postal_code: "94102"
                    country: "US"
      responses:
        '201':
          description: Order created successfully
          headers:
            Location:
              description: URL of the created order
              schema:
                type: string
              example: /orders/ord_123abc
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '422':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ValidationError'
              example:
                type: "https://api.example.com/errors/validation"
                title: "Validation Error"
                status: 422
                errors:
                  - field: "items"
                    message: "At least one item is required"
                  - field: "shipping_address.postal_code"
                    message: "Invalid postal code format"
        '429':
          $ref: '#/components/responses/RateLimitExceeded'

  /orders/{order_id}:
    get:
      tags:
        - Orders
      summary: Get order details
      description: Retrieve details of a specific order by ID
      operationId: getOrder
      parameters:
        - $ref: '#/components/parameters/OrderId'
        - name: expand
          in: query
          description: Related resources to expand in response
          required: false
          schema:
            type: array
            items:
              type: string
              enum: [customer, items.product, shipments]
          style: form
          explode: false
          example: [customer, items.product]
      responses:
        '200':
          description: Order details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
        '404':
          $ref: '#/components/responses/NotFound'

    patch:
      tags:
        - Orders
      summary: Update order
      description: |
        Update an existing order. Only certain fields can be updated
        depending on the order status.

        ## Updatable Fields by Status
        - **pending**: All fields
        - **confirmed**: shipping_address, notes
        - **shipped**: Cannot be updated
      operationId: updateOrder
      parameters:
        - $ref: '#/components/parameters/OrderId'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateOrderRequest'
      responses:
        '200':
          description: Order updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '404':
          $ref: '#/components/responses/NotFound'
        '409':
          description: Conflict - order cannot be updated in current state
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
              example:
                type: "https://api.example.com/errors/order-locked"
                title: "Order Locked"
                status: 409
                detail: "Order cannot be modified after shipping"

  /orders/{order_id}/cancel:
    post:
      tags:
        - Orders
      summary: Cancel order
      description: |
        Cancel an order. Orders can only be cancelled if not yet shipped.

        ## Cancellation Policy
        - Orders in `pending` or `confirmed` status can be cancelled
        - Full refund is issued automatically
        - Cancellation is irreversible
      operationId: cancelOrder
      parameters:
        - $ref: '#/components/parameters/OrderId'
      requestBody:
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                reason:
                  type: string
                  description: Cancellation reason
                  maxLength: 500
                  example: "Customer requested cancellation"
      responses:
        '200':
          description: Order cancelled successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderResponse'
        '409':
          description: Order cannot be cancelled
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |
        JWT token obtained from OAuth2 authorization flow.

        Example: `Authorization: Bearer eyJhbGciOiJIUzI1NiIs...`

    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
      description: |
        API key for server-to-server authentication.
        Obtain from Developer Portal.

        Example: `X-API-Key: sk_live_abc123...`

    oauth2:
      type: oauth2
      description: OAuth2 authentication
      flows:
        authorizationCode:
          authorizationUrl: https://auth.example.com/authorize
          tokenUrl: https://auth.example.com/token
          refreshUrl: https://auth.example.com/refresh
          scopes:
            orders:read: Read order information
            orders:write: Create and modify orders
            customers:read: Read customer information

  parameters:
    OrderId:
      name: order_id
      in: path
      description: Unique order identifier
      required: true
      schema:
        type: string
        pattern: '^ord_[a-zA-Z0-9]+$'
      example: ord_123abc

    PageSize:
      name: limit
      in: query
      description: Number of items per page
      required: false
      schema:
        type: integer
        minimum: 1
        maximum: 100
        default: 20
      example: 20

    PageCursor:
      name: cursor
      in: query
      description: Pagination cursor for next page
      required: false
      schema:
        type: string
      example: eyJpZCI6MTAwfQ==

  headers:
    X-RateLimit-Limit:
      description: Request limit per minute
      schema:
        type: integer
      example: 1000

    X-RateLimit-Remaining:
      description: Remaining requests in current window
      schema:
        type: integer
      example: 950

  schemas:
    Order:
      type: object
      required:
        - id
        - status
        - customer_id
        - items
        - total
        - currency
        - created_at
      properties:
        id:
          type: string
          description: Unique order identifier
          pattern: '^ord_[a-zA-Z0-9]+$'
          example: ord_123abc
          readOnly: true
        status:
          type: string
          description: Current order status
          enum: [pending, confirmed, shipped, delivered, cancelled]
          example: pending
        customer_id:
          type: string
          description: Customer who placed the order
          example: cus_456def
        items:
          type: array
          description: Order line items
          items:
            $ref: '#/components/schemas/OrderItem'
          minItems: 1
        total:
          type: integer
          description: Order total in smallest currency unit (cents)
          minimum: 0
          example: 9999
        currency:
          type: string
          description: Three-letter ISO currency code
          pattern: '^[A-Z]{3}$'
          example: USD
        shipping_address:
          $ref: '#/components/schemas/Address'
        notes:
          type: string
          description: Optional order notes
          maxLength: 1000
        created_at:
          type: string
          format: date-time
          description: Order creation timestamp
          readOnly: true
          example: "2024-01-15T10:30:00Z"
        updated_at:
          type: string
          format: date-time
          description: Last update timestamp
          readOnly: true

    OrderItem:
      type: object
      required:
        - product_id
        - quantity
        - unit_price
      properties:
        id:
          type: string
          readOnly: true
        product_id:
          type: string
          description: Product identifier
          example: prod_789ghi
        quantity:
          type: integer
          description: Quantity ordered
          minimum: 1
          maximum: 1000
          example: 2
        unit_price:
          type: integer
          description: Price per unit in smallest currency unit
          minimum: 0
          example: 4999
          readOnly: true

    Address:
      type: object
      required:
        - line1
        - city
        - country
      properties:
        line1:
          type: string
          maxLength: 200
          example: "123 Main St"
        line2:
          type: string
          maxLength: 200
        city:
          type: string
          maxLength: 100
          example: "San Francisco"
        state:
          type: string
          maxLength: 100
          example: "CA"
        postal_code:
          type: string
          maxLength: 20
          example: "94102"
        country:
          type: string
          description: Two-letter ISO country code
          pattern: '^[A-Z]{2}$'
          example: "US"

    CreateOrderRequest:
      type: object
      required:
        - customer_id
        - items
      properties:
        customer_id:
          type: string
          description: Customer placing the order
        items:
          type: array
          items:
            type: object
            required:
              - product_id
              - quantity
            properties:
              product_id:
                type: string
              quantity:
                type: integer
                minimum: 1
          minItems: 1
        shipping_address:
          $ref: '#/components/schemas/Address'
        discount_code:
          type: string
          maxLength: 50
        notes:
          type: string
          maxLength: 1000

    UpdateOrderRequest:
      type: object
      properties:
        shipping_address:
          $ref: '#/components/schemas/Address'
        notes:
          type: string
          maxLength: 1000

    OrderResponse:
      type: object
      properties:
        data:
          $ref: '#/components/schemas/Order'

    OrderListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/Order'
        pagination:
          $ref: '#/components/schemas/Pagination'

    Pagination:
      type: object
      properties:
        has_more:
          type: boolean
          description: Whether more results exist
        next_cursor:
          type: string
          description: Cursor for next page
        prev_cursor:
          type: string
          description: Cursor for previous page

    Error:
      type: object
      description: RFC 7807 Problem Details
      required:
        - type
        - title
        - status
      properties:
        type:
          type: string
          format: uri
          description: Error type URI
          example: "https://api.example.com/errors/not-found"
        title:
          type: string
          description: Human-readable error title
          example: "Resource Not Found"
        status:
          type: integer
          description: HTTP status code
          example: 404
        detail:
          type: string
          description: Detailed error explanation
          example: "Order with ID ord_123abc was not found"
        instance:
          type: string
          description: URI of the specific occurrence
          example: "/orders/ord_123abc"
        trace_id:
          type: string
          description: Request trace ID for support
          example: "abc-123-xyz"

    ValidationError:
      allOf:
        - $ref: '#/components/schemas/Error'
        - type: object
          properties:
            errors:
              type: array
              items:
                type: object
                properties:
                  field:
                    type: string
                    description: Field with validation error
                  message:
                    type: string
                    description: Validation error message

  responses:
    BadRequest:
      description: Bad request - invalid parameters
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            type: "https://api.example.com/errors/bad-request"
            title: "Bad Request"
            status: 400
            detail: "Invalid query parameter: status must be one of [pending, confirmed, shipped, delivered, cancelled]"

    Unauthorized:
      description: Authentication required or failed
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            type: "https://api.example.com/errors/unauthorized"
            title: "Unauthorized"
            status: 401
            detail: "Invalid or expired authentication token"

    NotFound:
      description: Resource not found
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            type: "https://api.example.com/errors/not-found"
            title: "Not Found"
            status: 404
            detail: "The requested resource was not found"

    RateLimitExceeded:
      description: Rate limit exceeded
      headers:
        X-RateLimit-Limit:
          $ref: '#/components/headers/X-RateLimit-Limit'
        X-RateLimit-Remaining:
          schema:
            type: integer
          example: 0
        Retry-After:
          description: Seconds until rate limit resets
          schema:
            type: integer
          example: 30
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            type: "https://api.example.com/errors/rate-limit"
            title: "Rate Limit Exceeded"
            status: 429
            detail: "Request limit of 1000/minute exceeded. Retry after 30 seconds."

    InternalError:
      description: Internal server error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            type: "https://api.example.com/errors/internal"
            title: "Internal Server Error"
            status: 500
            detail: "An unexpected error occurred. Please try again later."
            trace_id: "abc-123-xyz"

webhooks:
  orderStatusChanged:
    post:
      summary: Order status changed webhook
      description: Fired when an order's status changes
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                event:
                  type: string
                  example: order.status_changed
                data:
                  type: object
                  properties:
                    order_id:
                      type: string
                    previous_status:
                      type: string
                    new_status:
                      type: string
                    changed_at:
                      type: string
                      format: date-time
      responses:
        '200':
          description: Webhook received successfully
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- ST-03 (Structured Output Templates)
- OC-02 (Format Specification)
- DS-03 (Technology-Specific Guidance)
- RT-05 (Evidence-Based Reasoning)
- ST-03 (Explicit Output Specification)

**Related Prompts:**
- api_rest_design_review.md - For REST API design review
- api_graphql_schema_analysis.md - For GraphQL schema analysis
- api_versioning_strategy.md - For API versioning decisions
- code-analysis/architecture/architecture_api_client_generation.md - For generating API clients
- learning/learning_backend_api_documentation.md - For API documentation learning

**Customization Guide:**
- **For Internal APIs**: Reduce examples, focus on essential documentation
- **For Public APIs**: Maximize examples, add SDKs section, expand descriptions
- **For GraphQL**: Use GraphQL SDL format instead of OpenAPI
- **For gRPC**: Use Protocol Buffers documentation patterns
- **For Event-Driven APIs**: Emphasize AsyncAPI format for webhooks/events
- **For Multiple Environments**: Add server variables for environment switching


---

## Must / Must Not

**Must:**
- Output a valid OpenAPI 3.1+ document (or clearly state when targeting 3.0 for legacy tool compatibility).
- Reference only schemas, parameters, and responses that actually exist or that you are also defining in this output.
- For every operation, include: `summary`, `description`, `operationId`, `tags`, at least one success response, and at least one error response.
- Use `$ref` for any schema reused across 2+ operations to keep the spec DRY.
- Preserve the existing API's behavior — document what IS, not what you wish were true.

**Must Not:**
- Invent endpoints, parameters, or status codes that the source code / existing spec does not expose.
- Use deprecated OpenAPI 2.0 (Swagger) constructs unless the user has explicitly requested 2.0.
- Include real credentials, production URLs, PII, or tenant IDs in examples.
- Emit a spec that fails `openapi-cli lint` or `spectral lint` — validate structure before output.
- Paper over ambiguity with vague descriptions like "various errors can occur" — list them.

## Verification (Self-Check Before Emitting Spec)

Before finalizing the OpenAPI document:

1. **Every path parameter in `paths:` is declared in `parameters:`** (no orphan `{id}` placeholders).
2. **Every `$ref` resolves** within the document (no dangling references).
3. **Every response uses a defined schema** — no inline anonymous `object`s larger than 3 fields.
4. **Security schemes are referenced** — if the API uses auth, the spec has a `securitySchemes` block and each protected operation references it.
5. **Examples are realistic but non-production** — plausible shapes, never real user data.
6. **The spec passes a validator** — mentally simulate `spectral lint`; if anything would warn, fix it before emitting.

## False-Positive Prevention

When analyzing an existing OpenAPI spec or generating one from code, rule out:

- **"Missing description"** — A property with an obvious name (`id`, `createdAt`) may not need a description; don't bloat the spec.
- **"Inconsistent response codes"** — Different verbs legitimately return different codes; don't force uniformity.
- **"Missing 400 response"** — Only flag if the endpoint accepts input that can be invalid; read-only GETs without query params don't need one.
- **"Schema should be reusable"** — Only if it appears 2+ times. Single-use schemas can stay inline.
- **"OpenAPI 3.0 vs 3.1"** — Respect the target version in `openapi:` field; do not rewrite 3.0 to 3.1 unless asked.

Report findings as **High** / **Medium** / **Low** confidence based on whether you inspected the backing code or inferred from spec alone.
