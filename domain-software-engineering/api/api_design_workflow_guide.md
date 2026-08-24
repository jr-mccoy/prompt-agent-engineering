---
title: "API Design Workflow Guide"
category: api
description: "API Design Workflow Guide."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: beginner
tags:
  - api
  - design
  - guide
  - workflow
updated: "2026-04-03"
related_prompts: []
artifact_type: "reference"
---

# API Design Workflow Guide

This guide provides a complete workflow for designing, documenting, and maintaining APIs using the prompts in this category.

## Overview

The API Design category contains prompts for building high-quality, developer-friendly APIs:

| Prompt | Purpose | When to Use |
|--------|---------|-------------|
| `api_rest_design_review.md` | REST API design review | Designing or reviewing REST endpoints |
| `api_graphql_schema_analysis.md` | GraphQL schema analysis | Building or auditing GraphQL APIs |
| `api_versioning_strategy.md` | API versioning planning | Planning breaking changes or new versions |
| `api_openapi_documentation.md` | OpenAPI/Swagger docs | Generating API documentation |

## API Design Workflow

### Phase 1: Design

```
┌─────────────────────────────────────────────────────────────────┐
│                      API DESIGN WORKFLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. REQUIREMENTS        2. DESIGN           3. DOCUMENTATION    │
│  ┌─────────────┐       ┌─────────────┐     ┌─────────────┐     │
│  │ Use Cases   │──────▶│ REST or     │────▶│ OpenAPI     │     │
│  │ Consumers   │       │ GraphQL     │     │ Spec        │     │
│  │ Constraints │       │ Review      │     │ Generation  │     │
│  └─────────────┘       └─────────────┘     └─────────────┘     │
│                                                   │             │
│  4. VERSIONING          5. SECURITY         6. RELEASE         │
│  ┌─────────────┐       ┌─────────────┐     ┌─────────────┐     │
│  │ Strategy    │◀──────│ Auth/Authz  │◀────│ Go Live     │     │
│  │ Planning    │       │ Review      │     │ Monitoring  │     │
│  └─────────────┘       └─────────────┘     └─────────────┘     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Step-by-Step Process

#### Step 1: Define API Requirements
Before using any prompts, gather:
- Target consumers (internal teams, partners, public developers)
- Use cases and user stories
- Data models and relationships
- Performance requirements (latency, throughput)
- Security requirements (authentication, authorization)

#### Step 2: Choose API Style
| Factor | Choose REST | Choose GraphQL |
|--------|-------------|----------------|
| Simple CRUD operations | ✅ | |
| Complex data relationships | | ✅ |
| Cacheable responses needed | ✅ | |
| Mobile apps with varying needs | | ✅ |
| Multiple teams consuming | ✅ | ✅ |
| Real-time updates required | | ✅ (subscriptions) |

#### Step 3: Design Review
Use the appropriate prompt based on your API style:

**For REST APIs:**
```
Use: api_rest_design_review.md

Focus areas:
- Resource modeling
- HTTP method compliance
- Response design
- Error handling
```

**For GraphQL APIs:**
```
Use: api_graphql_schema_analysis.md

Focus areas:
- Schema structure
- Query performance
- Security (depth limiting, complexity)
- Mutation design
```

#### Step 4: Generate Documentation
```
Use: api_openapi_documentation.md

Deliverables:
- Complete OpenAPI 3.0+ specification
- Request/response examples
- Authentication documentation
- Error response documentation
```

#### Step 5: Plan Versioning Strategy
```
Use: api_versioning_strategy.md

Decisions:
- Versioning approach (URI, header, etc.)
- Breaking change policy
- Deprecation timeline
- Migration support
```

## Common Scenarios

### Scenario 1: New API from Scratch

```
Recommended workflow:
1. api_versioning_strategy.md → Establish versioning approach upfront
2. api_rest_design_review.md OR api_graphql_schema_analysis.md → Design review
3. api_openapi_documentation.md → Generate documentation
```

### Scenario 2: Existing API Audit

```
Recommended workflow:
1. api_rest_design_review.md OR api_graphql_schema_analysis.md → Identify issues
2. api_versioning_strategy.md → Plan for breaking changes
3. api_openapi_documentation.md → Update/improve documentation
```

### Scenario 3: API Migration (REST to GraphQL)

```
Recommended workflow:
1. api_rest_design_review.md → Document current REST API
2. api_graphql_schema_analysis.md → Design new GraphQL schema
3. api_versioning_strategy.md → Plan migration strategy
4. api_openapi_documentation.md → Document both during transition
```

### Scenario 4: Preparing for Public Release

```
Recommended workflow:
1. api_rest_design_review.md → Full design audit
2. api_versioning_strategy.md → Establish public API versioning policy
3. api_openapi_documentation.md → Generate comprehensive public docs
4. Security review (see code-analysis/security/)
```

## Integration with Other Categories

### Security Integration
```
Combine with:
- code-analysis/security/security_api_security_testing.md → Security audit
- code-analysis/security/security_authentication_authorization.md → Auth review
```

### Performance Integration
```
Combine with:
- code-analysis/performance/performance_bottleneck_identification.md → Performance review
- testing/testing_performance_load_test_planning.md → Load testing
```

### DevOps Integration
```
Combine with:
- devops/devops_cicd_pipeline_analysis.md → API deployment automation
- devops/devops_monitoring_observability.md → API metrics and monitoring
```

## Best Practices

### 1. Design First
- Always design your API before implementing
- Use OpenAPI/GraphQL SDL as a contract
- Get stakeholder review before coding

### 2. Version Early
- Establish versioning strategy from day one
- Use semantic versioning for API changes
- Document breaking change policy upfront

### 3. Document Everything
- Every endpoint needs documentation
- Include realistic examples
- Document error scenarios

### 4. Security by Design
- Authentication from the start
- Rate limiting before launch
- Input validation everywhere

### 5. Developer Experience
- Consistent naming conventions
- Clear error messages
- Comprehensive SDKs when possible

## API Design Checklist

### Pre-Design
- [ ] Requirements documented
- [ ] Consumers identified
- [ ] Security requirements defined
- [ ] Performance SLAs established

### Design Phase
- [ ] API style chosen (REST/GraphQL)
- [ ] Resource/schema design complete
- [ ] Design review conducted
- [ ] Versioning strategy defined

### Documentation
- [ ] OpenAPI/GraphQL spec generated
- [ ] All endpoints documented
- [ ] Examples provided
- [ ] Error responses documented

### Pre-Release
- [ ] Security review complete
- [ ] Performance testing complete
- [ ] Rate limiting configured
- [ ] Monitoring in place

### Release
- [ ] Developer portal updated
- [ ] SDK/client libraries available
- [ ] Changelog published
- [ ] Support process established

## Related Resources

### Internal Prompts
- `code-analysis/architecture/architecture_api_client_generation.md`
- `code-analysis/security/security_api_security_testing.md`
- `learning/learning_backend_api_documentation.md`
- `testing/testing_integration_test_design.md`

### External Resources
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [GraphQL Specification](https://spec.graphql.org/)
- [REST API Design Guidelines](https://github.com/microsoft/api-guidelines)
- [Google API Design Guide](https://cloud.google.com/apis/design)

---

**Category Count:** 4 prompts + 1 workflow guide
**Last Updated:** 2026-04-17


## Agent-Friendly Prompt Addendum

Because these are prompts (not tools), include an agent contract when using them with AI coding agents:

- Require compatibility constraints (existing clients, version windows, sunset dates).
- Require concrete migration artifacts (OpenAPI diff, deprecation headers, changelog entries).
- Require executable verification (`contract tests`, schema lint, breaking-change check).

Reusable addendum:

```
Assume this API is already in production unless stated otherwise.
Before proposing changes, list breaking-change risks and consumer impact.
Return machine-checkable outputs: endpoint diff table, versioning decision, migration checklist, and validation commands.
```
