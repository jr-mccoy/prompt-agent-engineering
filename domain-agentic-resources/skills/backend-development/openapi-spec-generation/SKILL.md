---
name: openapi-spec-generation
description: Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documentation, generating SDKs, or ensuring API contract compliance.
metadata:
  tags:
    - api-design
    - generation
    - openapi
    - spec
    - swagger
  updated: "2026-04-11"
---
# OpenAPI Spec Generation

Comprehensive patterns for creating, maintaining, and validating OpenAPI 3.1 specifications for RESTful APIs.

## When to Use This Skill

- Creating API documentation from scratch
- Generating OpenAPI specs from existing code
- Designing API contracts (design-first approach)
- Validating API implementations against specs
- Generating client SDKs from specs
- Setting up API documentation portals

## Core Concepts

### 1. OpenAPI 3.1 Structure

```yaml
openapi: 3.1.0
info:
  title: API Title
  version: 1.0.0
servers:
  - url: https://api.example.com/v1
paths:
  /resources:
    get: ...
components:
  schemas: ...
  securitySchemes: ...
```

### 2. Design Approaches

| Approach | Description | Best For |
|----------|-------------|----------|
| **Design-First** | Write spec before code | New APIs, contracts |
| **Code-First** | Generate spec from code | Existing APIs |
| **Hybrid** | Annotate code, generate spec | Evolving APIs |

## Templates

### Template 1: Complete API Specification (Paths)

```yaml
openapi: 3.1.0
info:
  title: User Management API
  description: API for managing users and their profiles.
  version: 2.0.0

servers:
  - url: https://api.example.com/v2
    description: Production
  - url: http://localhost:3000/v2
    description: Local development

tags:
  - name: Users
    description: User management operations
  - name: Admin
    description: Administrative operations

paths:
  /users:
    get:
      operationId: listUsers
      summary: List all users
      description: Returns a paginated list of users with optional filtering.
      tags:
        - Users
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/LimitParam'
        - name: status
          in: query
          schema:
            $ref: '#/components/schemas/UserStatus'
        - name: search
          in: query
          schema:
            type: string
            minLength: 2
            maxLength: 100
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserListResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '429':
          $ref: '#/components/responses/RateLimited'
      security:
        - bearerAuth: []

    post:
      operationId: createUser
      summary: Create a new user
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
            examples:
              standard:
                value:
                  email: user@example.com
                  name: John Doe
                  role: user
      responses:
        '201':
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          headers:
            Location:
              schema:
                type: string
                format: uri
        '400':
          $ref: '#/components/responses/BadRequest'
        '409':
          description: Email already exists
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
      security:
        - bearerAuth: []

  /users/{userId}:
    parameters:
      - $ref: '#/components/parameters/UserIdParam'

    get:
      operationId: getUser
      summary: Get user by ID
      tags:
        - Users
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []

    patch:
      operationId: updateUser
      summary: Update user
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUserRequest'
      responses:
        '200':
          description: User updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          $ref: '#/components/responses/BadRequest'
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []

    delete:
      operationId: deleteUser
      summary: Delete user
      tags:
        - Users
        - Admin
      responses:
        '204':
          description: User deleted
        '404':
          $ref: '#/components/responses/NotFound'
      security:
        - bearerAuth: []
        - apiKey: []

# components: schemas, parameters, responses, securitySchemes
# See references/code-first-templates-and-sdk.md
```

## Code-First Templates, Validation & SDK

Python/FastAPI code-first generation, TypeScript/tsoa decorators, Spectral/Redocly validation rulesets, and SDK generation with `openapi-generator-cli`.

See [references/code-first-templates-and-sdk.md](references/code-first-templates-and-sdk.md)

## Best Practices

### Do's
- **Use $ref** - Reuse schemas, parameters, responses
- **Add examples** - Real-world values help consumers
- **Document errors** - All possible error codes
- **Version your API** - In URL or header
- **Use semantic versioning** - For spec changes

### Don'ts
- **Don't use generic descriptions** - Be specific
- **Don't skip security** - Define all schemes
- **Don't forget nullable** - Be explicit about null
- **Don't mix styles** - Consistent naming throughout
- **Don't hardcode URLs** - Use server variables

## Resources

- [OpenAPI 3.1 Specification](https://spec.openapis.org/oas/v3.1.0)
- [Swagger Editor](https://editor.swagger.io/)
- [Redocly](https://redocly.com/)
- [Spectral](https://stoplight.io/open-source/spectral)
