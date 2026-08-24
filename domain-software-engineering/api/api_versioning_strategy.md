---
title: "API Versioning Strategy"
category: api-design
description: "Designs API versioning strategies balancing backward compatibility with evolution and deprecation management"
tags:
  - api-design
updated: "2026-03-19"
---

# API Versioning Strategy

**Objective:** Analyze API versioning requirements and design a comprehensive versioning strategy that balances backward compatibility, maintainability, developer experience, and business needs.

**When to Use:** Use this prompt when designing a new API versioning scheme, planning breaking changes to existing APIs, migrating between API versions, establishing organizational API standards, or evaluating versioning approaches for different API types (REST, GraphQL, gRPC).

**Instructions:**

1. **Assess Current State**
   - Document existing API versions and their usage
   - Identify current breaking change frequency
   - Map client dependencies and migration constraints
   - Analyze deprecation timeline requirements
   - Review SLA and support commitments

2. **Evaluate Versioning Approaches**
   - **URI Path Versioning**: `/v1/resource`, `/v2/resource`
   - **Query Parameter Versioning**: `/resource?version=1`
   - **Header Versioning**: `Accept: application/vnd.api.v1+json`
   - **Content Negotiation**: `Accept: application/vnd.company.resource.v1+json`
   - **No Versioning (Additive Only)**: Continuous evolution
   - **Date-Based Versioning**: `2024-01-15` style versions

3. **Define Breaking Change Policy**
   - Classify change types (breaking vs. non-breaking)
   - Establish breaking change criteria
   - Document acceptable evolution patterns
   - Define deprecation and sunset timelines
   - Create migration support commitments

4. **Design Version Lifecycle**
   - Define version states (Alpha, Beta, GA, Deprecated, Sunset)
   - Establish minimum support duration per state
   - Plan overlap periods for migrations
   - Create communication protocols for changes
   - Define rollback procedures

5. **Plan Backward Compatibility**
   - Design additive change patterns
   - Plan default value strategies for new fields
   - Create field deprecation patterns
   - Design response envelope evolution
   - Plan authentication/authorization compatibility

6. **Developer Experience Considerations**
   - Design clear version discovery mechanisms
   - Plan SDK and client library versioning
   - Create migration guides and tooling
   - Design changelog and notification systems
   - Establish version-specific documentation

7. **Implementation Strategy**
   - Design routing/dispatch mechanism
   - Plan code organization for multi-version support
   - Create testing strategy for all active versions
   - Design monitoring and analytics per version
   - Plan infrastructure and deployment considerations

**Expected Output:** A comprehensive API versioning strategy document including:
- Recommended versioning approach with rationale
- Breaking change classification matrix
- Version lifecycle definitions
- Migration playbook template
- Implementation architecture
- Timeline and rollout plan

**Example Output:**

```markdown
## API Versioning Strategy Document

### Executive Summary

**Recommended Approach**: URI Path Versioning (`/v1/`, `/v2/`)
**Rationale**: Clear visibility, easy routing, industry standard for REST APIs
**Alternative Considered**: Header versioning (rejected due to debugging complexity)

### Versioning Approach Comparison

| Approach | Visibility | Caching | Complexity | Recommendation |
|----------|------------|---------|------------|----------------|
| URI Path (`/v1/`) | High | Easy | Low | **Selected** |
| Header | Low | Complex | Medium | Alternative |
| Query Param | Medium | Possible | Low | Not recommended |
| Content-Type | Low | Complex | High | For specific use cases |

### Selected Approach: URI Path Versioning

**Format**: `https://api.example.com/v{major}/resources`

**Examples**:
```
GET /v1/users/123
GET /v2/users/123
POST /v1/orders
```

**Rationale**:
1. **Visibility**: Version immediately apparent in logs, documentation, debugging
2. **Caching**: Standard HTTP caching works without modification
3. **Routing**: Simple infrastructure routing without header inspection
4. **Discovery**: Self-documenting URLs
5. **Industry Standard**: Matches developer expectations (Google, Stripe, GitHub)

### Version Lifecycle States

```
┌─────────────────────────────────────────────────────────────────────┐
│                        VERSION LIFECYCLE                            │
├──────────┬──────────┬──────────┬─────────────┬──────────┬──────────┤
│  Alpha   │   Beta   │    GA    │ Deprecated  │  Sunset  │ Removed  │
│ (0-3 mo) │ (3-6 mo) │ (12+ mo) │  (6-12 mo)  │ (3-6 mo) │   End    │
├──────────┼──────────┼──────────┼─────────────┼──────────┼──────────┤
│ Breaking │ Breaking │    No    │     No      │    No    │   N/A    │
│ changes  │ possible │ breaking │  breaking   │ breaking │          │
│ expected │          │ changes  │  changes    │ changes  │          │
├──────────┼──────────┼──────────┼─────────────┼──────────┼──────────┤
│ No SLA   │ 99% SLA  │ 99.9%    │   99.9%     │ 99% SLA  │   N/A    │
│          │          │   SLA    │    SLA      │          │          │
└──────────┴──────────┴──────────┴─────────────┴──────────┴──────────┘
```

| State | Duration | Breaking Changes | SLA | Support |
|-------|----------|------------------|-----|---------|
| **Alpha** | 0-3 months | Expected, frequent | None | Best effort |
| **Beta** | 3-6 months | Possible with notice | 99% | Business hours |
| **GA (General Availability)** | 12+ months minimum | None allowed | 99.9% | Full support |
| **Deprecated** | 6-12 months | None, feature frozen | 99.9% | Security only |
| **Sunset** | 3-6 months | None, read-only | 99% | Migration support |
| **Removed** | N/A | N/A | N/A | N/A |

### Breaking Change Classification

#### Breaking Changes (Require New Major Version)

| Category | Change Type | Example |
|----------|-------------|---------|
| **Removal** | Remove endpoint | DELETE `/v1/legacy-users` endpoint |
| **Removal** | Remove required field | Remove `email` from User response |
| **Rename** | Change endpoint path | `/users` → `/accounts` |
| **Rename** | Change field name | `user_name` → `username` |
| **Type Change** | Change field type | `id: string` → `id: number` |
| **Semantic** | Change field meaning | `status: "active"` meaning changes |
| **Validation** | Add required field | New required `phone` in request |
| **Validation** | Strengthen validation | `name: 100 chars` → `name: 50 chars` |
| **Auth** | Require new permission | New scope required for existing endpoint |
| **Behavior** | Change default behavior | Pagination default 100 → 20 |

#### Non-Breaking Changes (Safe for Minor Version)

| Category | Change Type | Example |
|----------|-------------|---------|
| **Addition** | Add optional field | Add `nickname` to User response |
| **Addition** | Add new endpoint | Add `/users/{id}/preferences` |
| **Addition** | Add optional parameter | Add `?include=orders` query param |
| **Enhancement** | Increase limit | Max page size 100 → 200 |
| **Enhancement** | Add enum value | Status: add `"ARCHIVED"` option |
| **Deprecation** | Mark deprecated | Add `deprecated: true` to field |

### Deprecation Timeline Protocol

```
Day 0:     Announce deprecation (API response header, changelog, email)
           - Add `Deprecation` header to responses
           - Add `Sunset` header with sunset date
           - Update documentation with deprecation notice

Month 1-3: Active migration support
           - Migration guides published
           - SDK updates released
           - Support team trained

Month 4-6: Monitoring and outreach
           - Track usage of deprecated version
           - Direct outreach to high-volume users
           - Warning emails to all users

Month 7-9: Sunset warning phase
           - Increase header warning frequency
           - Rate limit deprecated version (optional)
           - Final migration deadline communications

Month 10-12: Sunset
           - Return 410 Gone for deprecated endpoints
           - Maintain documentation for reference
           - Support tickets for stragglers

Month 13+: Removal
           - Remove code and infrastructure
           - Archive documentation
```

**Response Headers for Deprecation**:
```http
HTTP/1.1 200 OK
Deprecation: Sun, 01 Jan 2025 00:00:00 GMT
Sunset: Sun, 01 Jul 2025 00:00:00 GMT
Link: </v2/users>; rel="successor-version"
X-Deprecation-Notice: This endpoint is deprecated. Migrate to /v2/users by July 1, 2025.
```

### Version Support Matrix

| Version | Released | GA Date | Deprecation | Sunset | Status |
|---------|----------|---------|-------------|--------|--------|
| v1 | 2022-01-01 | 2022-04-01 | 2024-01-01 | 2024-07-01 | Sunset |
| v2 | 2023-06-01 | 2023-09-01 | - | - | **Current GA** |
| v3 | 2024-09-01 | - | - | - | Beta |

### Migration Playbook Template

#### Pre-Migration Assessment
```markdown
## Migration: v1 → v2

### Impact Assessment
- [ ] Identify all v1 endpoints in use
- [ ] Map v1 fields to v2 equivalents
- [ ] List breaking changes affecting your integration
- [ ] Estimate development effort
- [ ] Plan rollback strategy

### Breaking Changes Affecting Your Integration
1. `/v1/users` → `/v2/users`
   - `user_name` renamed to `username`
   - `created` renamed to `createdAt` (ISO 8601 format)

2. `/v1/orders` → `/v2/orders`
   - Response wrapped in `data` envelope
   - Pagination changed from offset to cursor

### Field Mapping
| v1 Field | v2 Field | Transformation |
|----------|----------|----------------|
| user_name | username | Direct rename |
| created | createdAt | Unix timestamp → ISO 8601 |
| status | status | No change |
```

#### Migration Checklist
```markdown
## Development Phase
- [ ] Update API client library to v2
- [ ] Refactor field mappings in code
- [ ] Update request/response models
- [ ] Update error handling for new format
- [ ] Add feature flags for gradual rollout

## Testing Phase
- [ ] Unit tests passing with v2 responses
- [ ] Integration tests with v2 sandbox
- [ ] Performance benchmark comparison
- [ ] Error scenario testing

## Deployment Phase
- [ ] Deploy with feature flag disabled
- [ ] Enable for internal users (1%)
- [ ] Enable for beta users (10%)
- [ ] Monitor error rates and latency
- [ ] Full rollout (100%)
- [ ] Remove v1 code paths
```

### Implementation Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        API Gateway                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                  Version Router                           │   │
│  │   /v1/* → v1 Service    /v2/* → v2 Service               │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   v1 Service  │    │   v2 Service  │    │   v3 Service  │
│   (Sunset)    │    │   (Current)   │    │    (Beta)     │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
                    ┌───────────────┐
                    │  Shared Core  │
                    │   Services    │
                    └───────────────┘
```

### Code Organization Pattern

```
api/
├── v1/
│   ├── controllers/
│   ├── models/
│   ├── transformers/      # v1 response formatting
│   └── routes.ts
├── v2/
│   ├── controllers/
│   ├── models/
│   ├── transformers/      # v2 response formatting
│   └── routes.ts
├── shared/
│   ├── services/          # Business logic (version agnostic)
│   ├── repositories/      # Data access
│   └── utils/
└── core/
    ├── versioning.ts      # Version routing logic
    └── deprecation.ts     # Deprecation header middleware
```

### Monitoring & Analytics

**Track per version**:
- Request volume and trends
- Error rates by type
- Latency percentiles (p50, p95, p99)
- Unique client count
- Deprecated endpoint usage

**Alerting thresholds**:
- Deprecated version usage > expected decline rate
- Error rate increase after version release
- Latency regression between versions

### Communication Protocol

| Event | Channels | Lead Time |
|-------|----------|-----------|
| New version beta | Changelog, Email, Twitter | Immediate |
| Version GA | Changelog, Email, Blog post | Immediate |
| Deprecation announced | Changelog, Email, API header | 12 months before sunset |
| Sunset reminder | Email, API header | 6, 3, 1 month before |
| Version removed | Changelog, Email | Immediate |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement)
- ST-02 (Sequential Step-by-Step Instructions)
- RT-03 (Tree of Thoughts - multiple approaches)
- ST-03 (Structured Output Templates)
- DS-05 (Decision Framework Scaffolding)
- DS-06 (Prioritization and Severity Guidance)
- NE-02 (Phased Workflow Architecture)

**Related Prompts:**
- api_rest_design_review.md - For REST API design review
- api_graphql_schema_analysis.md - For GraphQL API design review
- api_openapi_documentation.md - For API documentation generation
- devops/devops_cicd_pipeline_analysis.md - For deployment automation
- engineering/engineering_post_mortem_root_cause_analysis.md - For version migration issues

**Customization Guide:**
- **For Startups**: Shorter deprecation cycles (3-6 months), faster iteration
- **For Enterprise**: Longer support windows (24+ months), formal change control
- **For B2B APIs**: Partner communication protocols, migration SLAs
- **For Public APIs**: Extensive documentation, developer portal integration
- **For Internal APIs**: Relaxed versioning, coordinated deployments
- **For GraphQL**: Focus on additive-only changes, field deprecation over versioning
