# Technique Analysis: api-design-principles

**Resource Type:** Skill
**Path:** `skills/backend-development/api-design-principles/`
**Date Analyzed:** 2025-12-22
**Bundled Resources:** 2 references, 2 assets (137-line checklist + template code)
**Total Lines Analyzed:** ~665+ lines (528 SKILL.md + 137 checklist + references)

---

## Executive Summary

This is a **comprehensive API design knowledge base** covering both REST and GraphQL paradigms. It provides domain theory, pattern libraries, working code examples, and a pre-implementation checklist. The skill demonstrates how to teach complex technical domains through multi-paradigm comparison and extensive practical examples.

**Key Innovation:** Pre-implementation checklist with 100+ verification points covering design, security, performance, and monitoring—catching issues before they're built.

**Complexity:** 5/5 (Very High - multiple paradigms, extensive patterns, production-grade examples, comprehensive coverage)

---

## Identified Techniques

### Technique 1: Domain Theory Grounding (NEW)
- **Category:** ST (Structural)
- **Pattern:** Teach fundamental domain principles before practical patterns
- **Example from resource:**
  ```markdown
  ## Core Concepts

  ### 1. RESTful Design Principles
  **Resource-Oriented Architecture**
  - Resources are nouns (users, orders, products), not verbs
  - Use HTTP methods for actions (GET, POST, PUT, PATCH, DELETE)
  - URLs represent resource hierarchies
  ```
- **Maps to existing:** NEW (ST-26 from previous analysis, but more comprehensive)
- **Effectiveness:** Ensures users understand "why" before learning "how"; builds mental models

### Technique 2: Multi-Paradigm Comparison (NEW)
- **Category:** ST (Structural)
- **Pattern:** Teach multiple approaches to same problem side-by-side
- **Example from resource:**
  ```markdown
  ### 1. RESTful Design Principles
  [REST patterns...]

  ### 2. GraphQL Design Principles
  [GraphQL patterns...]
  ```
- **Maps to existing:** NEW (ST-30)
- **Effectiveness:** Users can choose appropriate paradigm; understand trade-offs

### Technique 3: Domain Pattern Library (NEW)
- **Category:** DS (Domain-Specific)
- **Pattern:** Curated collection of proven patterns with working implementations
- **Example from resource:**
  - Pattern 1: Resource Collection Design
  - Pattern 2: Pagination and Filtering
  - Pattern 3: Error Handling and Status Codes
  - Pattern 4: HATEOAS
  - Pattern 5+: GraphQL Schema Design, Resolver Design, DataLoader
- **Maps to existing:** NEW (DS-41)
- **Effectiveness:** Provides ready-to-use patterns; accelerates implementation

### Technique 4: HTTP Semantics Enforcement (NEW)
- **Category:** DS (Domain-Specific)
- **Pattern:** Use protocol semantics (HTTP methods, status codes) as design constraints
- **Example from resource:**
  ```python
  **HTTP Methods Semantics:**
  - `GET`: Retrieve resources (idempotent, safe)
  - `POST`: Create new resources
  - `PUT`: Replace entire resource (idempotent)
  - `PATCH`: Partial resource updates
  - `DELETE`: Remove resources (idempotent)
  ```
- **Maps to existing:** NEW (DS-42)
- **Effectiveness:** Leverages existing standards; produces predictable, RESTful APIs

### Technique 5: Pre-Implementation Checklist (NEW)
- **Category:** QA (Quality Assurance)
- **Pattern:** 137-point verification checklist covering all aspects before building
- **Example from resource:**
  ```markdown
  ## Pre-Implementation Review

  ### Resource Design
  - [ ] Resources are nouns, not verbs
  - [ ] Plural names for collections
  - [ ] Consistent naming across all endpoints

  ### HTTP Methods
  - [ ] GET for retrieval (safe, idempotent)
  - [ ] POST for creation
  ...
  [137 total checklist items across 14 categories]
  ```
- **Maps to existing:** NEW (QA-13)
- **Effectiveness:** Catches design flaws before implementation; ensures comprehensive review

### Technique 6: Good/Bad Code Comparison
- **Category:** ST (Structural - existing)
- **Pattern:** Extensive side-by-side comparison of correct vs incorrect implementations
- **Example from resource:**
  ```python
  # Good: Resource-oriented endpoints
  GET    /api/users              # List users (with pagination)
  POST   /api/users              # Create user
  GET    /api/users/{id}         # Get specific user

  # Bad: Action-oriented endpoints (avoid)
  POST   /api/createUser
  POST   /api/getUserById
  POST   /api/deleteUser
  ```
- **Maps to existing:** ST-28 (Anti-Pattern Documentation) - enhanced with extensive examples
- **Effectiveness:** Visual contrast makes mistakes obvious; accelerates learning

### Technique 7: Bundled Code Templates (NEW)
- **Category:** IT (Interaction)
- **Pattern:** Working code templates packaged with skill for immediate use
- **Example from resource:**
  - `assets/rest-api-template.py` - Complete FastAPI template
  - `assets/graphql-schema-template.graphql` - GraphQL schema example
- **Maps to existing:** NEW (IT-23)
- **Effectiveness:** Zero-to-production faster; reduces boilerplate writing

### Technique 8: N+1 Problem Prevention Pattern
- **Category:** DS (Domain-Specific - existing but well-implemented)
- **Pattern:** DataLoader pattern with batch loading to prevent query multiplication
- **Example from resource:**
  ```python
  class UserLoader(DataLoader):
      async def batch_load_fn(self, user_ids: List[str]) -> List[Optional[dict]]:
          """Load multiple users in single query."""
          users = await fetch_users_by_ids(user_ids)
          user_map = {user["id"]: user for user in users}
          return [user_map.get(user_id) for user_id in user_ids]
  ```
- **Maps to existing:** DS-09 (Performance Optimization Patterns)
- **Effectiveness:** Prevents exponential query growth; critical for GraphQL performance

### Technique 9: Pagination Pattern Library
- **Category:** DS (Domain-Specific - existing)
- **Pattern:** Multiple pagination strategies (offset, cursor, Relay) with implementations
- **Example from resource:**
  - Offset-based: Page number + page size
  - Cursor-based: After/before with opaque cursors
  - Relay spec: Connection/Edge/PageInfo pattern
- **Maps to existing:** DS-03 (Structured Analysis Patterns)
- **Effectiveness:** Provides battle-tested pagination; handles edge cases

### Technique 10: Common Pitfalls Section
- **Category:** ST (Structural - existing)
- **Pattern:** Explicitly list common mistakes developers make
- **Example from resource:**
  ```markdown
  ## Common Pitfalls
  - Over-fetching/Under-fetching (REST): Fixed in GraphQL but requires DataLoaders
  - Breaking Changes: Version APIs or use deprecation strategies
  - Inconsistent Error Formats: Standardize error responses
  - Missing Rate Limits: APIs without limits are vulnerable to abuse
  ```
- **Maps to existing:** ST-28 (Anti-Pattern Documentation)
- **Effectiveness:** Proactive warning system; saves debugging time

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: ST-30 - Multi-Paradigm Comparison
- **Description:** Teach multiple technical approaches to same problem side-by-side
- **Implementation:** Organize content by paradigm (REST vs. GraphQL), show parallel solutions
- **Use case:** Teaching systems design, framework comparison, architecture decisions
- **Example:** "REST: Multiple endpoints | GraphQL: Single endpoint with selective queries"
- **Proposed category:** ST (Structural)
- **Proposed code:** ST-30

### Pattern 2: DS-41 - Domain Pattern Library
- **Description:** Curated collection of proven patterns with working implementations for specific domain
- **Implementation:** Organize by pattern category, provide complete code examples, document when to use each
- **Use case:** API design, database patterns, security patterns, UI patterns
- **Example:** "Pattern 1: Resource Collection Design | Pattern 2: Pagination | Pattern 3: Error Handling"
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-41

### Pattern 3: DS-42 - HTTP Semantics Enforcement
- **Description:** Use protocol/standard semantics as design constraints and validation criteria
- **Implementation:** Document protocol semantics, enforce in design, validate against standards
- **Use case:** REST API design, protocol compliance, standards-based systems
- **Example:** "GET must be idempotent and safe; PUT must be idempotent; POST creates resources"
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-42

### Pattern 4: QA-13 - Pre-Implementation Checklist
- **Description:** Comprehensive verification checklist applied BEFORE building (not after)
- **Implementation:** 100+ checkpoints across design, security, performance, monitoring
- **Use case:** API design review, architecture review, security review, pre-deployment checks
- **Example:** "Before implementation: [ ] Resources are nouns [ ] HTTP methods correct [ ] Pagination defined"
- **Proposed category:** QA (Quality Assurance)
- **Proposed code:** QA-13

### Pattern 5: IT-23 - Bundled Code Templates
- **Description:** Working, production-grade code templates packaged with instructional content
- **Implementation:** Templates in assets/ directory, referenced in skill, immediately usable
- **Use case:** Framework quickstarts, boilerplate reduction, standard implementations
- **Example:** "assets/rest-api-template.py - Complete FastAPI REST API template"
- **Proposed category:** IT (Interaction)
- **Proposed code:** IT-23

---

## Multi-Technique Combinations

### Combination 1: Domain Theory + Pattern Library
Domain theory grounding (ST-26) establishes principles, pattern library (DS-41) provides implementations.

**Effectiveness:** Theory → Practice pipeline; users understand both why and how.

### Combination 2: Multi-Paradigm + HTTP Semantics
Multi-paradigm comparison (ST-30) shows options, HTTP semantics (DS-42) constrains REST choices.

**Effectiveness:** Understand trade-offs while maintaining standards compliance.

### Combination 3: Pre-Implementation Checklist + Code Templates
Pre-implementation checklist (QA-13) verifies design, code templates (IT-23) accelerate implementation.

**Effectiveness:** Quality gates before coding + fast implementation after approval.

### Combination 4: Pattern Library + Good/Bad Examples
Pattern library (DS-41) shows solutions, good/bad comparisons (ST-28) highlight mistakes.

**Effectiveness:** Positive examples + negative warnings = comprehensive learning.

### Combination 5: N+1 Prevention + DataLoader Pattern
N+1 problem documentation + working DataLoader implementation.

**Effectiveness:** Problem awareness + ready solution = immediate application.

---

## Notes for Integration

### 1. Pre-Implementation Checklists for All Domains
QA-13 pattern should be applied across domains:
- **Frontend**: Component design checklist (accessibility, performance, responsiveness)
- **Database**: Schema design checklist (normalization, indexing, constraints)
- **Security**: Threat model checklist (STRIDE, OWASP Top 10)
- **Infrastructure**: Deployment checklist (monitoring, scaling, disaster recovery)

Create template in prompt-techniques/ for domain-specific adaptation.

### 2. Domain Pattern Libraries
DS-41 represents a new type of prompting resource:
- Not a single prompt, but a **pattern collection**
- Organized by category/scenario
- Each pattern: Name + When to use + Implementation + Pitfalls
- Examples: Database patterns, Security patterns, Testing patterns

### 3. Multi-Paradigm Teaching
ST-30 should be used when multiple valid approaches exist:
- **State management**: Redux vs. Context vs. MobX
- **Database**: SQL vs. NoSQL vs. Graph
- **Architecture**: Monolith vs. Microservices vs. Serverless

Document as technique in MASTER_TECHNIQUE_INDEX with template.

### 4. HTTP Semantics as Constraint Pattern
DS-42 generalizes to "Protocol/Standard Semantics Enforcement":
- **HTTP**: REST API design
- **SQL**: Database query patterns
- **GraphQL**: Schema design
- **OpenAPI**: API specification

Principle: Leverage existing standards to reduce decision-making.

### 5. Bundled Templates Best Practices
IT-23 (Bundled Code Templates) guidelines:
- **Production-ready**: Not toy examples, real code
- **Well-commented**: Explain non-obvious choices
- **Customizable**: Clear extension points
- **Tested**: Include test examples
- **Dependencies listed**: Requirements documented

### 6. Common Pitfalls as Standard Section
Every technical skill should include "Common Pitfalls" section:
- Proactive problem prevention
- Drawn from real-world experience
- Specific to domain
- Actionable (not just "don't do X" but "do Y instead")

---

## Real-World Usage

From api-design-principles/SKILL.md:
- Lines 1-19: When to use (activation criteria)
- Lines 20-68: Core concepts (domain theory)
- Lines 69-242: REST API patterns (4 major patterns with code)
- Lines 244-487: GraphQL patterns (3 major patterns with code)
- Lines 489-517: Best practices + common pitfalls

From assets/api-design-checklist.md:
- Lines 1-104: REST-specific checklist (100+ items across 14 categories)
- Lines 105-137: GraphQL-specific checklist (32 items across 5 categories)
- Total: 137 verification points

---

## Summary

**api-design-principles** is a comprehensive knowledge base demonstrating how to teach complex technical domains. It introduces **5 novel techniques** focused on:

1. **Multi-paradigm teaching** (ST-30: REST + GraphQL comparison)
2. **Pattern libraries** (DS-41: Curated proven patterns)
3. **Protocol enforcement** (DS-42: HTTP semantics as constraints)
4. **Pre-implementation QA** (QA-13: 137-point checklist)
5. **Template bundling** (IT-23: Working code templates)

**Key Insight:** Comprehensive technical skills require multiple complementary resources:
- **Theory**: Domain principles (why)
- **Patterns**: Proven solutions (what)
- **Examples**: Working code (how)
- **Templates**: Starting points (accelerators)
- **Checklists**: Verification (quality gates)

**Recommendation:** Use this skill as a template for creating domain knowledge bases in other areas (database design, security, testing). The combination of theory, patterns, examples, templates, and checklists provides complete coverage.

**Bundled Resources Value:** The 137-point checklist alone justifies this skill. Pre-implementation verification prevents costly rework. The code templates (FastAPI, GraphQL) provide immediate production starting points.

**Coverage Depth:** This skill demonstrates "complete domain coverage" - both paradigms (REST + GraphQL), all CRUD operations, pagination, error handling, N+1 prevention, security, performance, monitoring. Use as exemplar for comprehensive technical documentation.
