# API Design Prompts

Prompts for designing, documenting, and reviewing APIs including REST, GraphQL, and OpenAPI specifications.

**Total Prompts:** 5

---

## Prompts

| Prompt | When to Use |
|--------|-------------|
| `api_rest_design_review.md` | Review REST API design |
| `api_graphql_schema_analysis.md` | Analyze GraphQL schema |
| `api_grpc_service_design.md` | Review/design gRPC services (proto, streaming, evolution) |
| `api_openapi_documentation.md` | Generate/review OpenAPI specs |
| `api_openapi_linting_governance.md` | Design OpenAPI linting ruleset + CI governance |
| `api_versioning_strategy.md` | Plan API versioning |
| `api_rate_limiting_patterns.md` | Design rate-limit patterns, headers, fallback |
| `api_design_workflow_guide.md` | Overall API design workflow (reference) |

---

## By API Type

### REST APIs
- `api_rest_design_review.md` - RESTful design principles
- `api_openapi_documentation.md` - OpenAPI/Swagger specs
- `api_versioning_strategy.md` - Version management

### GraphQL
- `api_graphql_schema_analysis.md` - Schema design review

---

## Quick Selection Guide

**"Review my REST API"** → `api_rest_design_review.md`

**"Review GraphQL schema"** → `api_graphql_schema_analysis.md`

**"Generate OpenAPI docs"** → `api_openapi_documentation.md`

**"Plan API versioning"** → `api_versioning_strategy.md`

---

## Related Categories

- **Code Analysis/Architecture** - API conformance and client generation
- **[Testing](../testing/)** - API testing
- **[Code Analysis/Security](../analysis/security/)** - API security testing
- **[DevOps](../devops/)** - API deployment

---

## REST Design Principles

The `api_rest_design_review.md` prompt evaluates:
- Resource naming conventions
- HTTP method usage
- Status code appropriateness
- HATEOAS compliance
- Pagination patterns
- Error response format
- Authentication/authorization

---

## GraphQL Best Practices

The `api_graphql_schema_analysis.md` prompt covers:
- Schema design patterns
- Query complexity analysis
- N+1 problem detection
- Mutation design
- Subscription patterns
- Authorization at field level

---

## Versioning Strategies

The `api_versioning_strategy.md` prompt helps choose between:
- URL path versioning (`/v1/users`)
- Header versioning (`Accept: application/vnd.api+json;version=1`)
- Query parameter versioning (`?version=1`)
- Content negotiation
