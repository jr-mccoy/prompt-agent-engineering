---
title: "Spring Security Configuration Review"
category: software-engineering/java-spring
description: "Review Spring Security configuration for authentication, authorization, CSRF, CORS, and common misconfiguration vulnerabilities"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - java
  - spring-security
  - authentication
  - authorization
  - oauth2
  - security
  - enterprise
updated: "2026-03-19"
---

# Spring Security Configuration Review

**Objective:** Review a Spring Boot application's Spring Security configuration for correctness, completeness, and resistance to common authentication/authorization vulnerabilities.

---

## Inputs / Context

**Required:**
- Spring Security configuration files (Java config classes, `SecurityFilterChain` beans, or legacy `WebSecurityConfigurerAdapter` extensions)
- Spring Boot version and Spring Security version
- Authentication method in use (form login, JWT, OAuth2/OIDC, SAML, basic auth)

**Optional:**
- Custom filters, authentication providers, or `UserDetailsService` implementations
- URL patterns requiring protection
- Multi-tenancy or multi-realm requirements
- Compliance requirements (HIPAA, SOC2, PCI-DSS)

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Distinguish between Spring Security 5.x (legacy `WebSecurityConfigurerAdapter`) and 6.x (component-based `SecurityFilterChain`) patterns
- Verify actual security impact — not just style preferences
- Test authorization rules against both happy-path and adversarial scenarios

**Must Not:**
- Flag deprecated-but-functional patterns as critical vulnerabilities (flag as Medium for migration)
- Assume OAuth2/OIDC configuration is wrong without verifying the identity provider's requirements
- Recommend disabling security features without explaining the risk tradeoff

---

## Steps

1. **Review authentication configuration:**
   - Authentication mechanism setup (form login, HTTP Basic, JWT, OAuth2 Resource Server, OIDC Client)
   - `UserDetailsService` or `AuthenticationProvider` implementation correctness
   - Password encoding (`BCryptPasswordEncoder`, `Argon2PasswordEncoder` — flag `NoOpPasswordEncoder` or plain text)
   - Session management policy (stateless for APIs, session fixation protection for web apps)
   - Remember-me configuration (secure token storage, expiration)

2. **Review authorization rules:**
   - `SecurityFilterChain` request matchers — order matters (most specific first)
   - Method-level security (`@PreAuthorize`, `@Secured`, `@RolesAllowed`) consistency
   - Role hierarchy configuration
   - **Adversarial check:** Identify URLs that might bypass rules due to:
     - Matcher ordering (Spring evaluates top-to-bottom, first match wins)
     - Trailing slash or case sensitivity differences
     - Missing matchers for new endpoints
     - Actuator endpoints exposed without authentication

3. **Review CSRF and CORS configuration:**
   - CSRF protection: Enabled for browser-based apps, intentionally disabled only for stateless APIs
   - CSRF token repository (cookie-based vs. session-based)
   - CORS policy: Allowed origins, methods, headers — flag wildcard (`*`) in production
   - Preflight caching and credential handling

4. **Review token/session security (if applicable):**
   - JWT: Signature algorithm (flag `none` or HMAC with weak secret), expiration, audience/issuer validation
   - OAuth2: Token storage, refresh token rotation, scope validation
   - Session: Timeout settings, concurrent session control, session fixation protection
   - Cookie security: `HttpOnly`, `Secure`, `SameSite` attributes

5. **Review filter chain and custom filters:**
   - Custom filter ordering within the Spring Security filter chain
   - Exception handling in custom filters (must not swallow `AuthenticationException`)
   - Security context propagation in async/threaded operations
   - Request wrapper or response wrapper side effects

6. **Check for common Spring Security misconfigurations:**
   - `permitAll()` on sensitive endpoints
   - Debug mode enabled in production (`@EnableWebSecurity(debug = true)`)
   - Actuator endpoints exposed without authentication
   - H2 console enabled with frame options disabled in production
   - Default error page leaking stack traces
   - Missing security headers (CSP, HSTS, X-Frame-Options)

---

## Output Format

### Security Posture Summary
Overall assessment (Strong / Adequate / Weak) with 2-3 sentence justification.

### Critical and High Findings

For each finding:
```
File: [file path]
Line(s): [line numbers]
Severity: [Critical | High]
Category: [Authentication | Authorization | CSRF/CORS | Token/Session | Filter Chain | Misconfiguration]
Vulnerability: [Clear description of the security issue]
Attack Scenario: [How an attacker could exploit this]
Recommendation: [Specific fix with code example]
```

### Medium and Low Findings

For each finding:
```
File: [file path]
Line(s): [line numbers]
Severity: [Medium | Low]
Category: [same categories as above]
Issue: [Description]
Recommendation: [Fix]
```

### Authorization Matrix Review
Table showing endpoint patterns, required roles, and whether the current configuration correctly enforces them.

| Endpoint Pattern | Required Auth | Current Config | Status |
|-----------------|---------------|----------------|--------|
| `/api/admin/**` | ROLE_ADMIN | `hasRole('ADMIN')` | Correct |
| `/actuator/**` | Authenticated | `permitAll()` | **VULNERABLE** |

### Migration Notes (if applicable)
If using deprecated patterns, list specific migration steps to current Spring Security version.

---

## Verification

**Quick self-check:**
- [ ] Authentication mechanism is correctly configured and tested
- [ ] Authorization rules are evaluated in correct order
- [ ] CSRF configuration matches the application type (browser vs. API)
- [ ] No actuator endpoints are unintentionally exposed
- [ ] Password encoding uses a strong algorithm
- [ ] Security headers are configured

**High-stakes verification:**
After completing the review, explicitly answer:
1. Can an unauthenticated user access any protected resource through matcher ordering or path traversal?
2. Can a low-privilege user escalate to admin through method-level security gaps?
3. Are there any endpoints that were added after the security configuration was written and might be unprotected?

**False-Positive Prevention:**
- Do NOT flag CSRF disabled on a purely stateless REST API as a vulnerability
- Do NOT flag `permitAll()` on intentionally public endpoints (login page, health check, public API)
- Do NOT flag OAuth2 configuration as wrong without understanding the IdP's token format
- DO verify that `@PreAuthorize` annotations are actually enforced (check `@EnableMethodSecurity` is present)
- DO check that test-only security configurations don't leak into production profiles

---

**Techniques Used:**
- ST-01 (Clear Objective Statement) — Focused on Spring Security review
- ST-02 (Structured Sequential Instructions) — 6-step security review process
- RT-02 (Multi-Dimensional Analysis Framework) — Multi-category analysis per finding
- RT-05 (Evidence-Based Reasoning) — Attack scenarios and code evidence required
- DS-06 (Prioritization Guidance) — Findings categorized by severity
- QA-01 (Chain-of-Verification) — High-stakes adversarial verification questions
