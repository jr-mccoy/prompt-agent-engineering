---
title: "OWASP Top 10 Comprehensive Security Analysis"
category: code-analysis/security
description: "Systematic security analysis against OWASP Top 10 vulnerabilities with actionable remediation guidance"
techniques:
  - ST-01
  - ST-02
  - DT-02
  - RT-02
  - RT-05
  - DS-06
  - DS-01
difficulty: intermediate
tags:
  - security
  - owasp
  - vulnerability-assessment
  - web-application
  - compliance
updated: "2026-03-19"
---

# OWASP Top 10 Comprehensive Security Analysis

**Objective:** Conduct a systematic security analysis of the codebase against the OWASP Top 10 most critical web application security risks to identify vulnerabilities and provide actionable remediation guidance.

**Instructions:**

1. **Review the codebase** with a focus on the OWASP Top 10 security risks (2021 edition):

   a. **A01:2021 – Broken Access Control**
      - Analyze authorization checks and access control mechanisms
      - Identify missing or inconsistent authorization checks
      - Review privilege escalation possibilities
      - Check for insecure direct object references (IDOR)
      - Examine path traversal vulnerabilities

   b. **A02:2021 – Cryptographic Failures**
      - Review sensitive data handling and encryption
      - Identify unencrypted sensitive data (passwords, tokens, PII)
      - Analyze cryptographic algorithm choices and implementations
      - Check for hardcoded secrets or weak key management
      - Review TLS/SSL configurations and certificate handling

   c. **A03:2021 – Injection**
      - Identify SQL injection vulnerabilities
      - Check for NoSQL injection risks
      - Analyze OS command injection possibilities
      - Review LDAP, XPath, and XML injection risks
      - Examine input validation and sanitization

   d. **A04:2021 – Insecure Design**
      - Evaluate security design patterns and threat modeling
      - Identify missing security controls and defensive measures
      - Review business logic vulnerabilities
      - Analyze trust boundaries and security assumptions
      - Check for rate limiting and abuse prevention

   e. **A05:2021 – Security Misconfiguration**
      - Review default configurations and hardening
      - Identify unnecessary features or services enabled
      - Check for detailed error messages exposing sensitive information
      - Analyze security headers and CORS configurations
      - Review cloud storage and service configurations

   f. **A06:2021 – Vulnerable and Outdated Components**
      - Identify dependencies with known vulnerabilities
      - Review component versions and update status
      - Analyze transitive dependencies
      - Check for deprecated or unmaintained libraries
      - Examine license compliance issues

   g. **A07:2021 – Identification and Authentication Failures**
      - Review authentication mechanisms and implementations
      - Identify weak password policies
      - Check for session management vulnerabilities
      - Analyze credential stuffing and brute-force protections
      - Review multi-factor authentication (MFA) implementation

   h. **A08:2021 – Software and Data Integrity Failures**
      - Check for insecure deserialization vulnerabilities
      - Review CI/CD pipeline security
      - Analyze software update mechanisms
      - Identify unsigned or unverified code/data
      - Examine integrity verification processes

   i. **A09:2021 – Security Logging and Monitoring Failures**
      - Review logging coverage and completeness
      - Identify missing security event logging
      - Analyze log protection and tampering prevention
      - Check for sensitive data in logs
      - Review alerting and incident response capabilities

   j. **A10:2021 – Server-Side Request Forgery (SSRF)**
      - Identify SSRF vulnerability patterns
      - Review URL validation and sanitization
      - Check for internal network access controls
      - Analyze cloud metadata access risks
      - Examine webhook and callback security

2. **CRITICAL: Verify each potential finding before reporting.** For each suspected vulnerability:
   - **Trace the actual code path** - Follow data flow from source to sink. Don't flag based on pattern matching alone.
   - **Check for existing protections** - Look for sanitization, validation, framework-provided security, or architectural safeguards that may exist elsewhere.
   - **Understand context** - Consider WHY the code is written this way. Framework constraints, library APIs, and platform-specific patterns may make seemingly risky code safe.
   - **Confirm exploitability** - What specific steps would an attacker need to exploit this? Is it actually reachable?

3. **For each VERIFIED vulnerability:**
   - Provide the specific code location AND the complete code path (source to sink)
   - Explain the vulnerability with evidence that protections don't exist elsewhere
   - Assess the severity (Critical, High, Medium, Low) based on CVSS
   - State your **confidence level** (High/Medium/Low) and what would change your assessment
   - Describe the potential business and technical impact
   - Provide detailed remediation recommendations with code examples

4. **Prioritize findings** based on:
   - Verification confidence (only High confidence findings should be Critical/High severity)
   - Severity and exploitability
   - Potential business impact
   - Ease of remediation
   - Exposure (internal vs external facing)

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag patterns based solely on keyword matching
- ❌ Do NOT flag framework-idiomatic code without understanding the framework's security model
- ❌ Do NOT report issues where mitigation exists elsewhere in the codebase
- ❌ Do NOT assume missing controls without searching for them
- ❌ Do NOT flag code that follows platform-specific security patterns (e.g., Android's threading model, iOS keychain usage)
- ✅ DO trace complete data flows from untrusted sources to sensitive operations
- ✅ DO verify framework/library documentation for built-in protections
- ✅ DO search the codebase for security utilities, middleware, or interceptors that may provide protection
- ✅ DO distinguish between "looks risky" and "is actually exploitable"

4. **Provide a security posture summary:**
   - Overall risk level assessment
   - Critical areas requiring immediate attention
   - Security strengths and weaknesses
   - Compliance implications

5. **Include actionable recommendations:**
   - Quick wins (easy, high-impact fixes)
   - Short-term improvements (1-3 months)
   - Long-term security enhancements
   - Security testing and validation strategies

**Expected Output:** A comprehensive OWASP Top 10 security analysis report including:
- Executive summary with overall risk assessment
- Detailed findings for each OWASP Top 10 category with:
  - Identified vulnerabilities with code locations
  - Severity ratings and risk assessments
  - Exploitation scenarios and impact analysis
  - Specific remediation guidance with code examples
- Prioritized remediation roadmap
- Security posture assessment
- Testing and validation recommendations

This analysis should provide development and security teams with a clear understanding of the application's security risks aligned with industry-standard OWASP Top 10 framework and actionable steps to improve security posture.

**Related Prompts:**
- security_vulnerability_analysis.md - General vulnerability analysis
- security_authentication_authorization_review.md - Detailed auth analysis
- security_api_testing.md - API-specific security testing
- quality_code_style_consistency_analysis.md - Code quality review

**When to Use:**
Use this prompt when conducting a comprehensive security audit, before major releases, after significant code changes, or as part of regular security assessment cycles to ensure alignment with OWASP Top 10 best practices.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps with comprehensive coverage
- DT-02 (Specific Focus Areas with Examples) - Detailed enumeration of OWASP Top 10 categories
- RT-02 (Multi-Dimensional Analysis Framework) - Location, Severity, Impact, Remediation structure
- RT-05 (Evidence-Based Reasoning) - Requires specific code locations and exploitation scenarios
- DS-06 (Prioritization and Severity Guidance) - CVSS-based severity ratings and prioritization
- DS-01 (Framework Application) - Applies OWASP Top 10 industry-standard framework
