---
title: "API Security Testing (REST and GraphQL)"
category: code-analysis
description: "API Security Testing (REST and GraphQL)"
tags:
  - code-analysis
  - security
  - testing
updated: "2026-03-19"
---

# API Security Testing (REST and GraphQL)

**Objective:** Conduct comprehensive security testing of REST and GraphQL APIs to identify vulnerabilities, misconfigurations, and security weaknesses that could lead to unauthorized access, data breaches, or service disruption.

**Instructions:**

1. **API Discovery and Enumeration:**

   a. **Endpoint Discovery**
      - Map all API endpoints and routes
      - Identify public vs authenticated endpoints
      - Discover hidden or undocumented endpoints
      - Analyze API versioning (v1, v2, etc.)
      - Review API documentation (OpenAPI/Swagger, GraphQL schema)
      - Check for development/debug endpoints in production

   b. **HTTP Methods Analysis**
      - Test supported HTTP methods for each endpoint
      - Identify method-based access control
      - Check for HTTP verb tampering vulnerabilities
      - Test OPTIONS method information disclosure
      - Verify HEAD method behavior

2. **REST API Security Analysis:**

   a. **Authentication and Authorization**
      - Test authentication mechanisms (JWT, OAuth2, API keys, Basic Auth)
      - Identify missing authentication on sensitive endpoints
      - Test authorization bypass techniques
      - Check for JWT vulnerabilities (weak signatures, algorithm confusion)
      - Test token expiration and refresh mechanisms
      - Verify scope and permission enforcement
      - Test for privilege escalation (vertical and horizontal)

   b. **Input Validation**
      - Test SQL injection in query parameters, headers, body
      - Check for NoSQL injection vulnerabilities
      - Test command injection vectors
      - Verify XML/XXE injection protections
      - Test LDAP injection
      - Check for path traversal vulnerabilities
      - Test file upload security
      - Verify content-type validation

   c. **Business Logic Vulnerabilities**
      - Test for rate limiting and throttling
      - Check for mass assignment vulnerabilities
      - Test numeric overflow/underflow
      - Verify transaction integrity
      - Test idempotency guarantees
      - Check for race conditions
      - Test order/workflow bypass

   d. **Data Exposure**
      - Test for excessive data exposure in responses
      - Check for sensitive data in error messages
      - Verify PII protection
      - Test for user enumeration
      - Check response header information disclosure
      - Analyze verbose error messages

   e. **API-Specific Attacks**
      - Test for BOLA (Broken Object Level Authorization)
      - Check for BFLA (Broken Function Level Authorization)
      - Test for mass assignment
      - Verify proper pagination and filtering
      - Test for API rate limiting bypass
      - Check for API versioning vulnerabilities

3. **GraphQL API Security Analysis:**

   a. **Schema Introspection**
      - Test if introspection is enabled in production
      - Analyze exposed schema for sensitive fields
      - Review query complexity and depth
      - Identify hidden or deprecated fields
      - Check for development-only queries/mutations

   b. **Query Security**
      - Test for query depth attacks
      - Check query complexity limits
      - Test for batch query attacks
      - Verify query cost analysis implementation
      - Test for query timeout protections
      - Check for field suggestion information disclosure

   c. **Authorization**
      - Test field-level authorization
      - Verify resolver-level access control
      - Check for type-level permissions
      - Test for data leakage through relationships
      - Verify query authorization consistency
      - Test mutation authorization

   d. **GraphQL-Specific Vulnerabilities**
      - Test for alias-based DoS attacks
      - Check for circular query attacks
      - Test for batch request abuse
      - Verify input validation on arguments
      - Test for injection in resolver logic
      - Check for N+1 query problems exposing timing attacks

4. **Security Headers and Configuration:**

   a. **Security Headers**
      - Check for CORS misconfigurations
      - Verify Content-Security-Policy
      - Test X-Frame-Options header
      - Check X-Content-Type-Options
      - Verify Strict-Transport-Security
      - Review X-XSS-Protection
      - Check Referrer-Policy

   b. **API Configuration**
      - Verify HTTPS enforcement
      - Check TLS/SSL configuration and cipher suites
      - Test for HTTP downgrade attacks
      - Verify certificate validation
      - Check for debug mode in production
      - Review error handling configuration

5. **Rate Limiting and DoS Protection:**
   - Test rate limiting implementation
   - Check for rate limit bypass techniques
   - Test for application-level DoS
   - Verify account lockout mechanisms
   - Test for resource exhaustion
   - Check for slowloris-type attacks

6. **Mass Assignment and Parameter Pollution:**
   - Test for mass assignment vulnerabilities
   - Check HTTP Parameter Pollution (HPP)
   - Verify whitelist vs blacklist for parameters
   - Test for hidden parameter discovery
   - Check for parameter type confusion

7. **API Abuse and Business Logic:**
   - Test for automated bot protection
   - Check for scraping protections
   - Test for account creation abuse
   - Verify transaction limits
   - Test for discount/promo code abuse
   - Check for referral system abuse

8. **For each identified vulnerability, provide:**
   - Endpoint and HTTP method
   - Vulnerability type and category (OWASP API Security Top 10)
   - Severity rating (Critical, High, Medium, Low)
   - Detailed reproduction steps
   - Request/response examples
   - Potential impact and exploitation scenario
   - Remediation recommendations with code examples
   - Testing and validation steps

**Expected Output:** A comprehensive API security testing report including:

- **Executive Summary:**
  - Total API endpoints tested
  - Number of vulnerabilities by severity
  - Critical findings requiring immediate attention
  - Overall API security posture
  - OWASP API Security Top 10 compliance

- **API Inventory:**
  - Complete endpoint list with methods
  - Authentication requirements
  - Public vs authenticated endpoints
  - Deprecated or undocumented endpoints

- **REST API Security Findings:**
  For each vulnerability:
  - Endpoint and HTTP method
  - Vulnerability description
  - OWASP API Security category
  - Severity and CVSS score
  - Reproduction steps with curl/HTTP examples
  - Attack payload examples
  - Impact assessment
  - Remediation guidance

- **GraphQL API Security Findings:**
  For each vulnerability:
  - Query/mutation affected
  - Vulnerability description
  - Severity rating
  - GraphQL query examples
  - Impact assessment
  - Remediation with schema/resolver examples

- **Authentication and Authorization Analysis:**
  - Authentication mechanism review
  - Token security assessment
  - Authorization model evaluation
  - Access control gaps
  - Privilege escalation risks

- **Security Configuration Review:**
  - CORS policy assessment
  - Security headers analysis
  - TLS/SSL configuration
  - Rate limiting evaluation
  - Error handling review

- **Remediation Roadmap:**

  **Immediate (Critical):**
  - Authentication bypass fixes
  - Critical injection vulnerabilities
  - Sensitive data exposure
  - Broken authorization

  **Short-term (High):**
  - Rate limiting implementation
  - Input validation improvements
  - Security header configuration
  - GraphQL query complexity limits

  **Medium-term:**
  - API documentation security review
  - Automated security testing integration
  - API gateway implementation
  - Comprehensive logging and monitoring

- **Testing Methodology:**
  - Tools used (Burp Suite, Postman, Insomnia, GraphQL Voyager)
  - Test coverage (% of endpoints tested)
  - Testing approach (black-box, gray-box, white-box)
  - Limitations and scope exclusions

**Example Output Format:**

```
HIGH: Broken Object Level Authorization (BOLA) on User Endpoint
Endpoint: GET /api/v1/users/{userId}/profile
Method: GET
OWASP: API1:2023 Broken Object Level Authorization

Vulnerability:
  The API does not verify that the authenticated user has permission
  to access the requested user's profile data.

Reproduction Steps:
  1. Authenticate as User A (userId: 100)
  2. Request: GET /api/v1/users/101/profile
     Headers: Authorization: Bearer <user_a_token>
  3. API returns User B's (userId: 101) profile data

Request Example:
  curl -X GET 'https://api.example.com/api/v1/users/101/profile' \
    -H 'Authorization: Bearer eyJhbGc...'

Response (Vulnerable):
  {
    "userId": 101,
    "email": "userb@example.com",
    "ssn": "123-45-6789",
    "address": "123 Main St"
  }

Impact:
  - Any authenticated user can access any other user's profile
  - PII exposure (email, SSN, address)
  - Compliance violations (GDPR, CCPA)

Remediation:
  // Before (Vulnerable)
  app.get('/api/v1/users/:userId/profile', auth, async (req, res) => {
    const profile = await User.findById(req.params.userId);
    res.json(profile);
  });

  // After (Secure)
  app.get('/api/v1/users/:userId/profile', auth, async (req, res) => {
    // Verify the authenticated user matches the requested userId
    if (req.user.id !== parseInt(req.params.userId)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    const profile = await User.findById(req.params.userId);
    res.json(profile);
  });

Testing:
  Repeat request with mismatched userId and verify 403 Forbidden response
```

**Related Prompts:**
- security_owasp_top_10_analysis.md - Comprehensive OWASP security analysis
- security_authentication_authorization_review.md - Detailed auth analysis
- security_sql_injection_analysis.md - SQL injection testing
- architecture_api_conformance_check.md - API design and architecture

**When to Use:**
Use this prompt when developing or reviewing APIs, before public API launches, during security audits, after API changes, as part of CI/CD security testing, or when investigating API security incidents. Essential for protecting API-driven applications and microservices.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for REST and GraphQL analysis
- DT-02 (Specific Focus Areas with Examples) - Detailed API vulnerability categories
- RT-02 (Multi-Dimensional Analysis Framework) - Endpoint, Method, Severity, Impact, Remediation
- DS-01 (Framework Application) - Applies OWASP API Security Top 10 framework
- DS-06 (Prioritization and Severity Guidance) - CVSS-based severity ratings
- ST-03 (Output Format Templates) - Detailed vulnerability output with curl examples
- AG-05 (Concrete Deliverable Templates) - Secure code remediation examples
