---
title: "Authentication and Authorization Security Review"
category: code-analysis
description: "Authentication and Authorization Security Review"
tags:
  - code-analysis
  - review
  - security
updated: "2026-03-19"
---

# Authentication and Authorization Security Review

**Objective:** Conduct a comprehensive security review of authentication and authorization mechanisms to identify vulnerabilities, weaknesses, and misconfigurations that could lead to unauthorized access, privilege escalation, or account compromise.

**Instructions:**

1. **Analyze Authentication Mechanisms:**

   a. **Credential Management**
      - Review password storage (hashing algorithms: bcrypt, Argon2, PBKDF2)
      - Check salt generation and uniqueness
      - Analyze password complexity requirements
      - Review password change and reset flows
      - Identify hardcoded credentials or default passwords
      - Check for credential exposure in logs or error messages

   b. **Session Management**
      - Review session token generation (randomness, entropy)
      - Analyze session storage (cookies, localStorage, sessionStorage)
      - Check session expiration and timeout policies
      - Review session invalidation on logout
      - Identify session fixation vulnerabilities
      - Analyze concurrent session handling
      - Check for secure cookie attributes (HttpOnly, Secure, SameSite)

   c. **Multi-Factor Authentication (MFA)**
      - Review MFA implementation completeness
      - Check for MFA bypass vulnerabilities
      - Analyze backup code security
      - Review TOTP/SMS/email verification implementation
      - Identify missing MFA on sensitive operations
      - Check for MFA recovery process security

   d. **Authentication Flow Security**
      - Analyze login rate limiting and account lockout
      - Review brute-force attack prevention
      - Check for timing attack vulnerabilities
      - Identify credential stuffing protections
      - Review CAPTCHA implementation
      - Analyze account enumeration vulnerabilities

2. **Analyze Authorization Mechanisms:**

   a. **Access Control Models**
      - Identify access control model (RBAC, ABAC, ACL)
      - Review role and permission definitions
      - Analyze privilege hierarchy and inheritance
      - Check for principle of least privilege implementation
      - Review default access policies (deny-by-default vs allow-by-default)
      - Identify missing authorization checks

   b. **Authorization Check Completeness**
      - Review authorization checks on all endpoints/routes
      - Identify endpoints missing authorization
      - Check for consistent authorization enforcement
      - Analyze client-side vs server-side authorization
      - Review authorization check placement (before vs after operations)
      - Identify TOCTOU (Time-of-check to Time-of-use) issues

   c. **Vertical Privilege Escalation**
      - Test for admin function access by regular users
      - Review role elevation mechanisms
      - Check for privilege escalation through parameter manipulation
      - Analyze sudo/impersonation functionality security
      - Identify missing role validation

   d. **Horizontal Privilege Escalation**
      - Check for Insecure Direct Object References (IDOR)
      - Review user isolation and data segregation
      - Analyze object ownership validation
      - Test multi-tenant isolation
      - Identify cross-user data access vulnerabilities
      - Review UUID/ID predictability

3. **Review Token-Based Authentication:**

   a. **JWT (JSON Web Token) Security**
      - Review JWT signing algorithm (avoid 'none', use RS256/ES256)
      - Check for secret key strength and management
      - Analyze token expiration (exp claim)
      - Review token refresh mechanism
      - Identify token storage vulnerabilities
      - Check for JWT signature verification
      - Analyze sensitive data in JWT payload

   b. **OAuth 2.0 / OpenID Connect**
      - Review OAuth flow implementation (Authorization Code, PKCE)
      - Check redirect URI validation
      - Analyze state parameter usage (CSRF protection)
      - Review scope validation and enforcement
      - Check for token leakage in URLs or logs
      - Analyze client authentication security
      - Review refresh token rotation

   c. **API Keys and Access Tokens**
      - Review API key generation and complexity
      - Check for API key exposure (client-side code, repositories)
      - Analyze API key rotation policies
      - Review rate limiting per API key
      - Check for API key scoping and permissions
      - Identify leaked API keys

4. **Analyze Identity Management:**
   - Review user registration and verification
   - Check for account takeover vulnerabilities
   - Analyze email verification process
   - Review account recovery security
   - Check for account deletion and data retention
   - Analyze federated identity integration (SAML, OAuth)

5. **Review Security Best Practices:**
   - Check for defense in depth implementation
   - Analyze error handling (avoid information disclosure)
   - Review logging of authentication/authorization events
   - Check for security headers (X-Frame-Options, X-Content-Type-Options)
   - Analyze CORS configuration
   - Review TLS/SSL enforcement

6. **CRITICAL: Verify each potential finding before reporting.** For each suspected vulnerability:
   * **Trace the actual authentication/authorization flow** - Don't flag based on pattern matching alone:
     - Follow the complete request path from entry to data access
     - Check for middleware, interceptors, or base classes that enforce authorization
     - Verify that missing checks at one level aren't handled at another
   * **Understand the security model** - Consider the application's security design:
     - Is this endpoint intentionally public?
     - Are there layer-specific authorization patterns (API gateway, service layer, repository)?
     - Does the framework provide implicit protections?
   * **Check for defense-in-depth** - Look for multiple layers of protection:
     - Network-level controls (VPCs, security groups)
     - Application-level checks (middleware, decorators)
     - Database-level constraints (row-level security)
   * **Confirm actual exploitability** - Can this really be exploited in practice?

7. **For each VERIFIED vulnerability, provide:**
   - Specific code location AND the complete authentication/authorization flow
   - Vulnerability type and category
   - Severity rating (Critical, High, Medium, Low) with **confidence level**
   - Attack scenario with step-by-step exploitation (verified as possible)
   - Evidence that protections don't exist elsewhere
   - Potential impact (unauthorized access, data breach, privilege escalation)
   - Detailed remediation with secure code examples
   - Framework-specific security recommendations

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag endpoints as "missing auth" without checking middleware/base classes
- ❌ Do NOT assume IDOR without verifying object ownership isn't checked elsewhere
- ❌ Do NOT flag framework-idiomatic auth patterns as vulnerable
- ❌ Do NOT flag intentionally public endpoints as "missing authorization"
- ❌ Do NOT assume JWT/session handling is broken without tracing the complete flow
- ✅ DO trace complete authentication flows from request to response
- ✅ DO check for authorization middleware, decorators, or framework-provided protections
- ✅ DO verify that apparent vulnerabilities are actually exploitable
- ✅ DO understand the security architecture before flagging violations

**Expected Output:** A comprehensive authentication and authorization security analysis including:

- **Executive Summary:**
  - Overall security posture assessment
  - Critical vulnerabilities requiring immediate attention
  - Authentication/authorization maturity level
  - Key risk areas

- **Authentication Security Analysis:**
  - Credential management findings
  - Session management vulnerabilities
  - MFA implementation review
  - Authentication flow weaknesses
  - Brute-force and account enumeration risks

- **Authorization Security Analysis:**
  - Access control model evaluation
  - Missing authorization checks
  - Privilege escalation vulnerabilities (vertical and horizontal)
  - IDOR vulnerabilities
  - Multi-tenancy isolation issues

- **Token Security Analysis:**
  - JWT implementation review
  - OAuth/OIDC security assessment
  - API key management evaluation
  - Token storage and transmission security

- **Detailed Findings:**
  For each vulnerability:
  - Code location and vulnerable code snippet
  - Vulnerability description
  - Severity and CVSS score
  - Exploitation scenario
  - Business and technical impact
  - Step-by-step remediation with code examples
  - Testing and validation steps

- **Remediation Roadmap:**
  - Quick wins (immediate fixes)
  - Short-term improvements (1-3 months)
  - Long-term security enhancements
  - Architecture improvements
  - Policy and procedure recommendations

- **Security Testing:**
  - Recommended testing tools (Burp Suite, OWASP ZAP, Postman)
  - Test case examples
  - Penetration testing scope
  - Continuous security monitoring

**Example Output Format:**

```
CRITICAL: Missing Authorization Check on Admin Endpoint
Location: src/api/routes/admin.js:45
Vulnerable Code:
  app.get('/api/admin/users', (req, res) => {
    const users = db.getAllUsers();
    res.json(users);
  });

Attack Vector:
  1. Regular user obtains valid session token
  2. User directly accesses /api/admin/users endpoint
  3. Endpoint returns all user data without authorization check

Impact: Any authenticated user can access admin functionality and retrieve sensitive user data

Remediation:
  app.get('/api/admin/users', requireAuth, requireRole('admin'), (req, res) => {
    const users = db.getAllUsers();
    res.json(users);
  });

Testing:
  curl -H "Authorization: Bearer <regular_user_token>" https://api.example.com/api/admin/users
```

**Related Prompts:**
- security_owasp_top_10_analysis.md - Comprehensive OWASP security audit
- security_api_testing.md - API security testing including auth
- security_secret_detection.md - Credential and secret scanning
- architecture_api_conformance_check.md - API design and security

**When to Use:**
Use this prompt when conducting security audits, reviewing authentication systems, investigating unauthorized access incidents, before implementing new auth features, during compliance assessments, or as part of regular security review cycles.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for comprehensive coverage
- DT-02 (Specific Focus Areas with Examples) - Detailed auth mechanism categories
- RT-02 (Multi-Dimensional Analysis Framework) - Location, Severity, Attack, Impact, Remediation
- DS-06 (Prioritization and Severity Guidance) - CVSS-based severity ratings
- RT-05 (Evidence-Based Reasoning) - Requires specific code snippets and locations
- ST-03 (Output Format Templates) - Detailed vulnerability output format
