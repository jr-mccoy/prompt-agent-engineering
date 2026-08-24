---
title: "Security Code Review Checklist"
category: code-analysis
description: "Provides comprehensive security-focused code review checklist covering common vulnerabilities and attack vectors"
tags:
  - code-analysis
  - review
  - security
updated: "2026-03-19"
---

# Security Code Review Checklist

**Objective:** Conduct a systematic security-focused code review using a comprehensive checklist to identify common security vulnerabilities, insecure coding practices, and potential attack vectors before code deployment.

**Instructions:**

1. **Perform systematic security review across all categories:**

   **A. Input Validation and Sanitization**

   Review all user input handling:
   - [ ] All user inputs are validated (type, length, format, range)
   - [ ] Input validation uses whitelist approach (not blacklist)
   - [ ] Server-side validation is present (not just client-side)
   - [ ] Special characters are properly escaped or rejected
   - [ ] File uploads validate type, size, and content
   - [ ] File upload names are sanitized
   - [ ] URL inputs are validated and sanitized
   - [ ] Integer inputs check for overflow/underflow
   - [ ] Array/list inputs have size limits
   - [ ] Regex patterns are not vulnerable to ReDoS

   For each validation issue found:
   - Document input source and code location
   - Identify validation gaps
   - Assess exploitation risk
   - Provide secure validation examples

   **B. Authentication and Session Management**

   Review authentication mechanisms:
   - [ ] Passwords are hashed using strong algorithms (bcrypt, Argon2, scrypt)
   - [ ] Password hashing includes unique salts
   - [ ] Minimum password complexity requirements enforced
   - [ ] Account lockout after failed login attempts
   - [ ] Rate limiting on authentication endpoints
   - [ ] Multi-factor authentication (MFA) implemented for sensitive operations
   - [ ] Session tokens are cryptographically random and sufficient length (≥128 bits)
   - [ ] Session tokens expire after inactivity
   - [ ] Absolute session timeout enforced
   - [ ] Sessions invalidated on logout
   - [ ] Session tokens not exposed in URLs
   - [ ] Secure cookie attributes set (HttpOnly, Secure, SameSite)
   - [ ] Password reset tokens are single-use and time-limited
   - [ ] No default or hardcoded credentials

   For each auth/session issue:
   - Document the security gap
   - Assess account takeover risk
   - Provide secure implementation examples

   **C. Authorization and Access Control**

   Review authorization implementation:
   - [ ] Authorization checks on all protected resources
   - [ ] Authorization enforced server-side (not client-side only)
   - [ ] Default deny access policy (fail closed)
   - [ ] Principle of least privilege applied
   - [ ] Role-based or attribute-based access control implemented
   - [ ] Direct object references checked for ownership
   - [ ] No privilege escalation paths (vertical or horizontal)
   - [ ] Multi-tenant data isolation verified
   - [ ] Admin functions require admin role
   - [ ] Authorization checks cannot be bypassed
   - [ ] File/resource access validated against user permissions
   - [ ] API endpoints have proper authorization

   For each authorization issue:
   - Document missing or weak checks
   - Identify privilege escalation paths
   - Provide secure access control examples

   **D. Injection Prevention**

   Review for injection vulnerabilities:
   - [ ] SQL queries use parameterized statements or ORMs
   - [ ] No string concatenation for SQL queries
   - [ ] Stored procedures use parameterized inputs
   - [ ] NoSQL queries parameterized or sanitized
   - [ ] OS commands avoid user input (or properly sanitized)
   - [ ] LDAP queries use parameterized methods
   - [ ] XPath queries are parameterized
   - [ ] XML parsers configured to prevent XXE
   - [ ] Template engines auto-escape by default
   - [ ] Server-side template injection prevented
   - [ ] Expression language (EL) injection prevented
   - [ ] Code evaluation (eval, exec) avoided with user input

   For each injection vulnerability:
   - Document injection point and type
   - Provide exploitation example
   - Recommend parameterization or sanitization

   **E. Cross-Site Scripting (XSS) Prevention**

   Review XSS protections:
   - [ ] Output encoding applied context-appropriately (HTML, JavaScript, URL, CSS)
   - [ ] Template engines auto-escape enabled
   - [ ] No dangerous methods used (innerHTML, eval, document.write)
   - [ ] User input not directly embedded in JavaScript
   - [ ] Content Security Policy (CSP) headers configured
   - [ ] X-XSS-Protection header set
   - [ ] HTML sanitization for rich text (DOMPurify, bleach)
   - [ ] JSON responses have proper Content-Type
   - [ ] No reflected user input in error messages
   - [ ] Framework XSS protections enabled (React, Vue, Angular)
   - [ ] Avoid dangerouslySetInnerHTML, v-html, bypassSecurityTrust

   For each XSS vulnerability:
   - Document XSS type (reflected, stored, DOM-based)
   - Provide attack payload example
   - Recommend context-appropriate encoding

   **F. Cross-Site Request Forgery (CSRF) Prevention**

   Review CSRF protections:
   - [ ] CSRF tokens on state-changing operations
   - [ ] CSRF tokens validated server-side
   - [ ] SameSite cookie attribute configured
   - [ ] Double-submit cookie pattern or synchronizer token
   - [ ] Custom headers for AJAX requests
   - [ ] No GET requests for state changes
   - [ ] Referrer validation (as defense in depth)
   - [ ] Critical operations require re-authentication

   For each CSRF vulnerability:
   - Document unprotected state-changing endpoints
   - Assess impact of CSRF attack
   - Provide CSRF token implementation

   **G. Cryptography and Data Protection**

   Review cryptographic implementations:
   - [ ] Strong encryption algorithms (AES-256, ChaCha20)
   - [ ] Authenticated encryption used (AES-GCM, ChaCha20-Poly1305)
   - [ ] No deprecated algorithms (DES, 3DES, RC4, MD5 for security)
   - [ ] Appropriate key lengths (RSA ≥2048, AES ≥128, ECC ≥256)
   - [ ] Cryptographically secure random number generator (CSPRNG)
   - [ ] Unique IVs/nonces for each encryption
   - [ ] No hardcoded encryption keys or secrets
   - [ ] TLS 1.2 or 1.3 enforced (TLS 1.0/1.1 disabled)
   - [ ] Strong TLS cipher suites configured
   - [ ] Certificate validation implemented
   - [ ] Sensitive data encrypted at rest
   - [ ] Sensitive data encrypted in transit
   - [ ] Memory cleared after processing sensitive data
   - [ ] No sensitive data in logs

   For each crypto issue:
   - Document weak algorithm or implementation
   - Assess data exposure risk
   - Recommend modern cryptography

   **H. Error Handling and Logging**

   Review error handling and logging:
   - [ ] Generic error messages to users (no stack traces)
   - [ ] Detailed errors logged server-side
   - [ ] No sensitive data in error messages
   - [ ] No sensitive data in logs (passwords, tokens, PII)
   - [ ] Authentication events logged (success, failure)
   - [ ] Authorization failures logged
   - [ ] Security events logged (admin actions, privilege changes)
   - [ ] Logs include timestamp, user, action, result
   - [ ] Logs protected from tampering
   - [ ] Centralized logging implemented
   - [ ] Log retention policy enforced
   - [ ] Monitoring and alerting configured
   - [ ] No information disclosure through timing differences

   For each logging issue:
   - Document logging gaps
   - Identify sensitive data exposure
   - Recommend comprehensive logging

   **I. Secure Configuration**

   Review configuration security:
   - [ ] No default passwords or accounts
   - [ ] Debug mode disabled in production
   - [ ] Unnecessary features/services disabled
   - [ ] Security headers configured (CSP, HSTS, X-Frame-Options, etc.)
   - [ ] CORS policy properly restrictive
   - [ ] Secure cookie settings (HttpOnly, Secure, SameSite)
   - [ ] HTTP to HTTPS redirect enforced
   - [ ] Directory listing disabled
   - [ ] Server version information hidden
   - [ ] Error pages don't reveal system information
   - [ ] Admin interfaces not publicly accessible
   - [ ] Development tools not in production
   - [ ] Environment variables for sensitive config
   - [ ] Secrets managed securely (not in code/repos)

   For each configuration issue:
   - Document misconfiguration
   - Assess exposure risk
   - Provide secure configuration

   **J. Dependency and Third-Party Security**

   Review dependencies:
   - [ ] All dependencies up-to-date
   - [ ] No dependencies with known vulnerabilities
   - [ ] Dependencies from trusted sources
   - [ ] Dependency integrity verified (checksums, signatures)
   - [ ] Minimal dependencies (remove unused)
   - [ ] License compliance verified
   - [ ] Third-party APIs accessed over HTTPS
   - [ ] Third-party API keys rotated regularly
   - [ ] Third-party data validated and sanitized

   For each dependency issue:
   - Document vulnerable or outdated libraries
   - Assess exploitation risk
   - Recommend updates or alternatives

   **K. Business Logic Security**

   Review business logic:
   - [ ] Rate limiting on resource-intensive operations
   - [ ] Transaction integrity verified
   - [ ] Race condition protections
   - [ ] Workflow bypass prevented
   - [ ] Price/quantity manipulation prevented
   - [ ] Discount code abuse prevented
   - [ ] Idempotency for critical operations
   - [ ] Proper state machine validation
   - [ ] Account enumeration prevented
   - [ ] Mass operations have limits

   For each business logic issue:
   - Document logical vulnerability
   - Assess abuse potential
   - Recommend controls

   **L. File and Upload Security**

   Review file handling:
   - [ ] File upload size limits enforced
   - [ ] File type validation (magic numbers, not just extension)
   - [ ] File names sanitized
   - [ ] Files stored outside webroot
   - [ ] Uploaded files not executed
   - [ ] Virus/malware scanning for uploads
   - [ ] File access requires authorization
   - [ ] No path traversal vulnerabilities
   - [ ] Zip bomb protection
   - [ ] Image processing library vulnerabilities addressed

   For each file handling issue:
   - Document insecure file operation
   - Assess malicious file upload risk
   - Provide secure file handling

   **M. API Security**

   Review API security:
   - [ ] API authentication required
   - [ ] API rate limiting implemented
   - [ ] API input validation
   - [ ] API versioning strategy
   - [ ] API documentation access controlled
   - [ ] GraphQL query depth/complexity limits
   - [ ] REST endpoints follow secure design
   - [ ] No excessive data exposure
   - [ ] Proper HTTP methods used
   - [ ] API keys not in URLs or client code

   For each API issue:
   - Document API vulnerability
   - Assess data exposure or abuse risk
   - Recommend API security controls

2. **Document findings with:**
   - Checklist item failed
   - Code location (file, function, line)
   - Vulnerability description
   - Severity (Critical, High, Medium, Low)
   - OWASP category (if applicable)
   - Exploitation scenario
   - Impact assessment
   - Remediation guidance with code examples
   - Testing verification steps

**Expected Output:** A comprehensive security code review report including:

- **Executive Summary:**
  - Total checklist items reviewed
  - Number of security issues by severity
  - Critical findings requiring immediate action
  - Overall security code quality assessment
  - Key risk areas

- **Checklist Results:**
  - Items passed: X%
  - Items failed: Y%
  - Items not applicable: Z%
  - Security score

- **Security Findings by Category:**

  For each security category (A-M):
  - Category assessment summary
  - Specific checklist items failed
  - Vulnerabilities identified
  - Code locations
  - Risk ratings
  - Remediation recommendations

- **Critical Security Issues:**
  - High-severity findings requiring immediate attention
  - Exploitation scenarios
  - Business impact
  - Urgent remediation steps

- **Remediation Roadmap:**
  - **Immediate (Critical):** Fix within 1-2 weeks
  - **Short-term (High):** Fix within 1-2 months
  - **Medium-term (Medium):** Fix within 3-6 months
  - **Low-priority (Low):** Address in future iterations

- **Security Best Practices Recommendations:**
  - Secure coding guidelines
  - Security testing integration
  - Developer training needs
  - Security tools and automation
  - Code review process improvements

**Example Output Format:**

```
CATEGORY: C. Authorization and Access Control
STATUS: FAILED (3 of 12 checks passed)

[✗] FAILED: Direct object references checked for ownership
Location: src/api/documents.js:67
Severity: HIGH

Finding: Insecure Direct Object Reference (IDOR)
Vulnerable Code:
  app.get('/api/documents/:docId', auth, async (req, res) => {
    const doc = await Document.findById(req.params.docId);
    res.json(doc);
  });

Issue:
  Endpoint retrieves document by ID without verifying the authenticated
  user owns or has permission to access the document.

Exploitation:
  1. User A authenticates and gets token
  2. User A discovers their document ID: 12345
  3. User A tries ID 12346 (User B's document)
  4. API returns User B's document without authorization check

Impact: Unauthorized access to sensitive documents, data breach

Remediation:
  app.get('/api/documents/:docId', auth, async (req, res) => {
    const doc = await Document.findById(req.params.docId);

    // Check ownership
    if (!doc || doc.ownerId !== req.user.id) {
      return res.status(403).json({ error: 'Forbidden' });
    }

    res.json(doc);
  });

Testing:
  1. Authenticate as User A
  2. Attempt to access User B's document
  3. Verify 403 Forbidden response
  4. Verify User A can access their own documents
```

**Related Prompts:**
- security_owasp_top_10_analysis.md - OWASP-focused security analysis
- security_authentication_authorization_review.md - Deep auth security review
- security_sql_injection_analysis.md - SQL injection testing
- security_xss_vulnerability_analysis.md - XSS vulnerability testing
- quality_code_style_consistency_analysis.md - Code quality review

**When to Use:**
Use this prompt for every code review, pull request review, pre-deployment security checks, security audits, or when reviewing legacy code. Essential for maintaining secure coding practices and preventing common vulnerabilities from reaching production.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Organized into 13 security categories
- DT-02 (Specific Focus Areas with Examples) - Comprehensive security checklists per category
- RT-02 (Multi-Dimensional Analysis Framework) - Finding, Location, Severity, Impact, Remediation
- DS-02 (Metric Specification) - Pass/fail percentages and security scores
- DS-06 (Prioritization and Severity Guidance) - Severity ratings and remediation timeline
- ST-03 (Output Format Templates) - Detailed finding output format
- AG-05 (Concrete Deliverable Templates) - Secure code remediation examples
