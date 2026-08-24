---
title: "Security Testing and Vulnerability Assessment"
category: testing
description: "Design comprehensive security tests to identify vulnerabilities and validate security controls"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-06
  - QA-02
difficulty: advanced
tags:
  - testing
  - security
  - vulnerability
  - penetration-testing
  - owasp
  - compliance
updated: "2026-01-25"
---

# Security Testing and Vulnerability Assessment

**Objective:** Design and implement comprehensive security tests to identify vulnerabilities, validate security controls, and ensure application security throughout the development lifecycle.

**When to Use:** Use this prompt when implementing security testing for applications, conducting penetration test planning, validating authentication/authorization systems, preparing for security audits, or ensuring compliance with security standards (OWASP, PCI-DSS, SOC2).

**Instructions:**

1. **Assess Security Testing Requirements**
   Identify the scope and objectives:
   - Application type (web, API, mobile, desktop)
   - Deployment environment (cloud, on-premise, hybrid)
   - Compliance requirements (OWASP, PCI-DSS, HIPAA, SOC2)
   - Data sensitivity levels (PII, financial, healthcare)
   - Authentication mechanisms in use
   - Third-party integrations and dependencies

2. **Map Attack Surface**
   Document all potential entry points:
   - **User Inputs**: Forms, file uploads, URL parameters, headers
   - **APIs**: REST endpoints, GraphQL queries, WebSockets
   - **Authentication**: Login flows, session management, tokens
   - **Authorization**: Role-based access, resource permissions
   - **Data Storage**: Databases, caches, file systems
   - **External Interfaces**: Third-party APIs, webhooks, integrations

3. **Design Security Test Categories**
   Structure tests by vulnerability type:

   **A. Authentication Testing**
   - Credential validation and storage
   - Password policy enforcement
   - Multi-factor authentication flows
   - Session management and timeout
   - Account lockout mechanisms
   - Password reset security

   **B. Authorization Testing**
   - Horizontal privilege escalation (accessing other users' data)
   - Vertical privilege escalation (accessing admin functions)
   - IDOR (Insecure Direct Object References)
   - Missing function-level access control
   - JWT/Token validation

   **C. Injection Testing**
   - SQL Injection (SQLi)
   - Cross-Site Scripting (XSS)
   - Command Injection
   - LDAP Injection
   - XML/XXE Injection
   - NoSQL Injection

   **D. Data Protection Testing**
   - Sensitive data exposure
   - Encryption at rest and in transit
   - API response data leakage
   - Error message information disclosure
   - Secure cookie flags

   **E. Security Misconfiguration**
   - Default credentials
   - Unnecessary features enabled
   - Missing security headers
   - Verbose error messages
   - Outdated dependencies

4. **Select Security Testing Tools**
   Choose appropriate tools for each test type:
   - **SAST (Static Analysis)**: SonarQube, Semgrep, CodeQL, Checkmarx
   - **DAST (Dynamic Analysis)**: OWASP ZAP, Burp Suite, Nikto
   - **Dependency Scanning**: Snyk, Dependabot, npm audit, OWASP Dependency-Check
   - **Secret Detection**: GitLeaks, TruffleHog, detect-secrets
   - **Container Security**: Trivy, Anchore, Clair
   - **API Security**: Postman, OWASP ZAP API Scan

5. **Implement Automated Security Tests**
   Integrate security tests into CI/CD:
   - Pre-commit hooks for secret detection
   - SAST scans on pull requests
   - Dependency vulnerability checks
   - Container image scanning
   - DAST scans in staging environments
   - Compliance policy checks

6. **Document Security Test Cases**
   For each test, document:
   - Vulnerability being tested (OWASP reference)
   - Test methodology and steps
   - Expected secure behavior
   - Attack payloads/test inputs
   - Pass/fail criteria
   - Remediation guidance

7. **Establish Security Testing Cadence**
   Define testing frequency:
   - Continuous: SAST, dependency scanning, secret detection
   - Per Release: DAST, penetration testing
   - Quarterly: Full security audit, compliance review
   - Annual: Third-party penetration test

8. **CRITICAL: Verify Findings Before Reporting**
   - Confirm each vulnerability is actually exploitable
   - Check for existing mitigations elsewhere in the codebase
   - Verify the attack vector is accessible from the threat model
   - **Assign confidence level:** High/Medium/Low for each finding
   - Document the exploitation path with concrete evidence

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag input fields as "vulnerable" without tracing data flow to a sensitive operation
- Report SQL injection based on string concatenation without checking for parameterized queries elsewhere
- Mark authentication as "weak" without understanding the full auth stack (WAF, rate limiting, MFA)
- Assume XSS is exploitable without checking Content-Security-Policy headers
- Flag CSRF without verifying the endpoint performs state-changing operations
- Report "missing security headers" when they're set at the reverse proxy/CDN level
- Mark dependencies as "vulnerable" without checking if the vulnerable code path is used

✅ **DO:**
- Trace complete attack paths from untrusted input to sensitive operations
- Verify that reported vulnerabilities are actually exploitable in context
- Check for layered security controls (defense in depth) before claiming something is unprotected
- Include proof-of-concept or clear exploitation steps for High/Critical findings
- For dependency vulnerabilities, verify the application actually uses the affected function
- Document confidence level: High (exploited/verified), Medium (likely exploitable), Low (theoretical)
- Reference specific OWASP/CWE codes for each finding

**Expected Output:** A comprehensive security testing strategy including:
- Security test plan covering all OWASP Top 10 categories
- Automated security test configurations for CI/CD
- Manual penetration test scenarios
- Security test case documentation
- Remediation guidance for common vulnerabilities
- Compliance mapping to relevant standards
- **Confidence levels** for each vulnerability finding (High/Medium/Low)
- **Verification evidence** showing exploitability or attack path

**Example Output:**

```markdown
## Security Testing Plan for E-Commerce API

**Application:** Online Store REST API
**Version:** 2.4.0
**Compliance Requirements:** PCI-DSS, OWASP Top 10

---

### 1. Attack Surface Analysis

| Entry Point | Type | Risk Level | Priority |
|------------|------|------------|----------|
| /api/auth/login | Authentication | Critical | P0 |
| /api/users/{id} | User Data | High | P1 |
| /api/orders | Transactions | Critical | P0 |
| /api/products/search | Query Params | Medium | P2 |
| /api/upload/image | File Upload | High | P1 |

---

### 2. Authentication Security Tests

```javascript
// tests/security/auth.security.test.js
const request = require('supertest');
const app = require('../app');

describe('Authentication Security Tests', () => {
  describe('Brute Force Protection', () => {
    it('should lock account after 5 failed login attempts', async () => {
      const credentials = { email: 'test@example.com', password: 'wrong' };

      // Attempt 5 failed logins
      for (let i = 0; i < 5; i++) {
        await request(app)
          .post('/api/auth/login')
          .send(credentials)
          .expect(401);
      }

      // 6th attempt should be blocked
      const response = await request(app)
        .post('/api/auth/login')
        .send(credentials);

      expect(response.status).toBe(429);
      expect(response.body.message).toContain('Account locked');
    });

    it('should implement rate limiting on login endpoint', async () => {
      const requests = Array(100).fill().map(() =>
        request(app).post('/api/auth/login').send({
          email: 'test@example.com',
          password: 'test'
        })
      );

      const responses = await Promise.all(requests);
      const rateLimited = responses.filter(r => r.status === 429);

      expect(rateLimited.length).toBeGreaterThan(0);
    });
  });

  describe('Session Security', () => {
    it('should invalidate session on logout', async () => {
      // Login and get token
      const loginResponse = await request(app)
        .post('/api/auth/login')
        .send({ email: 'user@example.com', password: 'validpass' });

      const token = loginResponse.body.token;

      // Logout
      await request(app)
        .post('/api/auth/logout')
        .set('Authorization', `Bearer ${token}`)
        .expect(200);

      // Attempt to use invalidated token
      const response = await request(app)
        .get('/api/users/me')
        .set('Authorization', `Bearer ${token}`);

      expect(response.status).toBe(401);
    });

    it('should not accept expired tokens', async () => {
      const expiredToken = generateExpiredToken(); // Helper function

      const response = await request(app)
        .get('/api/users/me')
        .set('Authorization', `Bearer ${expiredToken}`);

      expect(response.status).toBe(401);
      expect(response.body.error).toContain('expired');
    });
  });

  describe('Password Security', () => {
    it('should reject weak passwords', async () => {
      const weakPasswords = ['123456', 'password', 'qwerty', 'abc123'];

      for (const password of weakPasswords) {
        const response = await request(app)
          .post('/api/auth/register')
          .send({
            email: 'newuser@example.com',
            password: password
          });

        expect(response.status).toBe(400);
        expect(response.body.error).toContain('password');
      }
    });

    it('should not expose password in API responses', async () => {
      const response = await request(app)
        .get('/api/users/me')
        .set('Authorization', `Bearer ${validToken}`);

      expect(response.body).not.toHaveProperty('password');
      expect(response.body).not.toHaveProperty('passwordHash');
      expect(JSON.stringify(response.body)).not.toContain('password');
    });
  });
});
```

---

### 3. Authorization Security Tests (IDOR/Privilege Escalation)

```javascript
// tests/security/authorization.security.test.js
describe('Authorization Security Tests', () => {
  describe('Horizontal Privilege Escalation (IDOR)', () => {
    it('should prevent users from accessing other users orders', async () => {
      const user1Token = await loginAsUser('user1@example.com');
      const user2OrderId = 'order-belonging-to-user2';

      const response = await request(app)
        .get(`/api/orders/${user2OrderId}`)
        .set('Authorization', `Bearer ${user1Token}`);

      expect(response.status).toBe(403);
    });

    it('should prevent users from modifying other users profiles', async () => {
      const user1Token = await loginAsUser('user1@example.com');

      const response = await request(app)
        .put('/api/users/user2-id')
        .set('Authorization', `Bearer ${user1Token}`)
        .send({ name: 'Hacked Name' });

      expect(response.status).toBe(403);
    });

    it('should use indirect object references', async () => {
      // Verify API uses UUIDs not sequential IDs
      const response = await request(app)
        .get('/api/orders')
        .set('Authorization', `Bearer ${validToken}`);

      const orderIds = response.body.orders.map(o => o.id);

      orderIds.forEach(id => {
        // Should be UUID format, not sequential integer
        expect(id).toMatch(
          /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i
        );
      });
    });
  });

  describe('Vertical Privilege Escalation', () => {
    it('should prevent regular users from accessing admin endpoints', async () => {
      const userToken = await loginAsUser('regular@example.com');

      const adminEndpoints = [
        '/api/admin/users',
        '/api/admin/orders',
        '/api/admin/settings',
        '/api/admin/logs'
      ];

      for (const endpoint of adminEndpoints) {
        const response = await request(app)
          .get(endpoint)
          .set('Authorization', `Bearer ${userToken}`);

        expect(response.status).toBe(403);
      }
    });

    it('should prevent role elevation through API manipulation', async () => {
      const userToken = await loginAsUser('regular@example.com');

      const response = await request(app)
        .put('/api/users/me')
        .set('Authorization', `Bearer ${userToken}`)
        .send({ role: 'admin' });

      // Should either reject or ignore the role field
      expect(response.status).not.toBe(200);

      // Verify role wasn't changed
      const profileResponse = await request(app)
        .get('/api/users/me')
        .set('Authorization', `Bearer ${userToken}`);

      expect(profileResponse.body.role).toBe('user');
    });
  });
});
```

---

### 4. Injection Security Tests

```javascript
// tests/security/injection.security.test.js
describe('Injection Security Tests', () => {
  describe('SQL Injection', () => {
    const sqlPayloads = [
      "'; DROP TABLE users; --",
      "1' OR '1'='1",
      "1; SELECT * FROM users",
      "admin'--",
      "' UNION SELECT * FROM users --"
    ];

    it('should sanitize SQL injection in search parameters', async () => {
      for (const payload of sqlPayloads) {
        const response = await request(app)
          .get('/api/products/search')
          .query({ q: payload });

        // Should not return server error (indicates SQL error)
        expect(response.status).not.toBe(500);
        // Should return empty results, not all data
        expect(response.body.products.length).toBeLessThan(100);
      }
    });

    it('should use parameterized queries for user input', async () => {
      // This test verifies via code review annotation
      // The actual protection is in the implementation
      const response = await request(app)
        .get('/api/users')
        .query({ id: "1 OR 1=1" });

      expect(response.status).toBe(400);
    });
  });

  describe('XSS (Cross-Site Scripting)', () => {
    const xssPayloads = [
      '<script>alert("XSS")</script>',
      '<img src=x onerror=alert("XSS")>',
      'javascript:alert("XSS")',
      '<svg onload=alert("XSS")>',
      '"><script>alert("XSS")</script>'
    ];

    it('should escape XSS payloads in user-generated content', async () => {
      for (const payload of xssPayloads) {
        // Create content with XSS payload
        await request(app)
          .post('/api/products/reviews')
          .set('Authorization', `Bearer ${validToken}`)
          .send({ productId: 'prod-123', comment: payload });

        // Retrieve and verify it's escaped
        const response = await request(app)
          .get('/api/products/prod-123/reviews');

        const reviewContent = JSON.stringify(response.body);
        expect(reviewContent).not.toContain('<script>');
        expect(reviewContent).not.toContain('onerror=');
        expect(reviewContent).not.toContain('javascript:');
      }
    });

    it('should set appropriate security headers', async () => {
      const response = await request(app).get('/api/health');

      expect(response.headers['x-content-type-options']).toBe('nosniff');
      expect(response.headers['x-xss-protection']).toBe('1; mode=block');
      expect(response.headers['content-security-policy']).toBeDefined();
    });
  });

  describe('Command Injection', () => {
    const commandPayloads = [
      '; ls -la',
      '| cat /etc/passwd',
      '`whoami`',
      '$(cat /etc/passwd)',
      '&& rm -rf /'
    ];

    it('should sanitize command injection in file operations', async () => {
      for (const payload of commandPayloads) {
        const response = await request(app)
          .post('/api/export')
          .set('Authorization', `Bearer ${adminToken}`)
          .send({ filename: `report${payload}.pdf` });

        expect(response.status).toBe(400);
        expect(response.body.error).toContain('invalid');
      }
    });
  });
});
```

---

### 5. Security Headers and Configuration Tests

```javascript
// tests/security/headers.security.test.js
describe('Security Headers Tests', () => {
  it('should have all required security headers', async () => {
    const response = await request(app).get('/api/health');

    // Required headers
    expect(response.headers).toMatchObject({
      'x-content-type-options': 'nosniff',
      'x-frame-options': expect.stringMatching(/DENY|SAMEORIGIN/),
      'x-xss-protection': '1; mode=block',
      'strict-transport-security': expect.stringContaining('max-age='),
      'content-security-policy': expect.any(String)
    });

    // Should NOT expose server info
    expect(response.headers['x-powered-by']).toBeUndefined();
    expect(response.headers['server']).not.toContain('Express');
  });

  it('should use secure cookie settings', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({ email: 'user@example.com', password: 'validpass' });

    const cookies = response.headers['set-cookie'];

    if (cookies) {
      cookies.forEach(cookie => {
        expect(cookie).toContain('HttpOnly');
        expect(cookie).toContain('Secure');
        expect(cookie).toContain('SameSite');
      });
    }
  });

  it('should not expose sensitive information in errors', async () => {
    const response = await request(app)
      .get('/api/debug/error')
      .set('Authorization', `Bearer ${validToken}`);

    const errorBody = JSON.stringify(response.body);

    // Should not expose stack traces
    expect(errorBody).not.toContain('at Function');
    expect(errorBody).not.toContain('node_modules');
    expect(errorBody).not.toContain('.js:');

    // Should not expose internal paths
    expect(errorBody).not.toContain('/home/');
    expect(errorBody).not.toContain('/var/');
  });
});
```

---

### 6. CI/CD Security Integration

```yaml
# .github/workflows/security.yml
name: Security Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'  # Daily security scan

jobs:
  secret-detection:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: GitLeaks Scan
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  dependency-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

  sast-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/security-audit
            p/owasp-top-ten

  security-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Security Test Suite
        run: |
          npm install
          npm run test:security
        env:
          NODE_ENV: test

  container-scan:
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    steps:
      - uses: actions/checkout@v4
      - name: Build Image
        run: docker build -t app:${{ github.sha }} .
      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: app:${{ github.sha }}
          severity: 'CRITICAL,HIGH'
          exit-code: '1'
```

---

### 7. Security Testing Checklist

| Category | Test | OWASP Ref | Status |
|----------|------|-----------|--------|
| **Authentication** | Brute force protection | A07:2021 | [ ] |
| | Password policy enforcement | A07:2021 | [ ] |
| | Session timeout | A07:2021 | [ ] |
| | MFA implementation | A07:2021 | [ ] |
| **Authorization** | IDOR prevention | A01:2021 | [ ] |
| | Role-based access control | A01:2021 | [ ] |
| | Function-level access | A01:2021 | [ ] |
| **Injection** | SQL injection | A03:2021 | [ ] |
| | XSS prevention | A03:2021 | [ ] |
| | Command injection | A03:2021 | [ ] |
| **Data Protection** | Encryption at rest | A02:2021 | [ ] |
| | Encryption in transit | A02:2021 | [ ] |
| | Sensitive data masking | A02:2021 | [ ] |
| **Configuration** | Security headers | A05:2021 | [ ] |
| | Error handling | A05:2021 | [ ] |
| | Dependency updates | A06:2021 | [ ] |
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Defines purpose of comprehensive security testing
- ST-02 (Sequential Step-by-Step Instructions) - Guides through assessment, mapping, design, and implementation
- RT-02 (Multi-Dimensional Analysis) - Covers auth, injection, data protection, and configuration
- RT-05 (Evidence-Based Reasoning) - Requires proof-of-concept and exploitation paths
- ST-03 (Structured Output Templates) - Provides consistent security report formats
- OC-04 (Comprehensive Example Outputs) - Demonstrates complete security test suites
- QA-02 (Adversarial Thinking) - False-positive prevention ensures verified vulnerabilities only
- QA-04 (Compliance Verification) - Maps tests to OWASP, PCI-DSS standards

**Related Prompts:**
- testing_unit_test_generation.md - For general unit testing patterns
- testing_integration_test_design.md - For testing component interactions
- security_owasp_top_10_analysis.md - For OWASP vulnerability analysis
- security_authentication_authorization_review.md - For auth system review
- code-analysis/security/security_comprehensive_analysis.md - For code security audit

**Customization Guide:**
- **For Web Applications**: Focus on XSS, CSRF, and session management tests
- **For APIs**: Emphasize authentication, authorization, and injection tests
- **For Mobile Apps**: Add certificate pinning, local storage, and binary analysis
- **For Microservices**: Include service-to-service auth and API gateway tests
- **For Compliance**: Map tests directly to PCI-DSS, HIPAA, or SOC2 requirements
