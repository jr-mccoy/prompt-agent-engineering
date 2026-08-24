---
title: "SQL Injection Detection and Prevention Analysis"
category: code-analysis
description: "SQL Injection Detection and Prevention Analysis"
tags:
  - analysis
  - code-analysis
  - security
updated: "2026-03-19"
---

# SQL Injection Detection and Prevention Analysis

**Objective:** Identify SQL injection vulnerabilities in the codebase and provide comprehensive remediation guidance to prevent data breaches and unauthorized database access.

**Instructions:**

1. **Analyze all database interaction points** in the codebase:
   - Identify SQL query construction methods
   - Locate dynamic SQL query generation
   - Find stored procedure calls and their parameters
   - Review ORM (Object-Relational Mapping) usage patterns
   - Examine database connection and query execution code

2. **Identify SQL injection vulnerability patterns:**

   a. **String Concatenation Vulnerabilities**
      - Locate queries built using string concatenation
      - Identify user input directly embedded in SQL strings
      - Find template literals or string formatting with user data
      - Check for interpolated variables in SQL statements

   b. **Improper Parameterization**
      - Review parameterized query usage
      - Identify missing or incorrect parameter binding
      - Check for bypassed prepared statements
      - Analyze stored procedure parameter handling

   c. **Second-Order SQL Injection**
      - Identify data stored in database and later used in queries
      - Review data validation on retrieval from database
      - Check for encoded or obfuscated malicious input

   d. **Blind SQL Injection Risks**
      - Analyze error handling and response differences
      - Review timing-based attack possibilities
      - Check for boolean-based blind injection vectors

   e. **NoSQL Injection (if applicable)**
      - Review MongoDB, CouchDB, or other NoSQL query construction
      - Identify JavaScript code injection in NoSQL queries
      - Check for operator injection vulnerabilities

3. **Analyze input validation and sanitization:**
   - Review input validation mechanisms
   - Identify missing or weak validation
   - Analyze whitelist vs blacklist approaches
   - Check for encoding and escaping mechanisms
   - Review input length and type restrictions

4. **Review database security configurations:**
   - Analyze database user permissions and privileges
   - Check for least privilege principle implementation
   - Review connection string security
   - Identify overprivileged database accounts
   - Examine database access control mechanisms

5. **Assess ORM and framework usage:**
   - Review ORM configuration and usage patterns
   - Identify raw SQL queries in ORM code
   - Check for ORM-specific injection vulnerabilities
   - Analyze query builder security
   - Review framework-provided security features

6. **CRITICAL: Verify each potential finding before reporting.** For each suspected vulnerability:
   * **Trace the complete data flow** - Follow user input from entry point to query execution:
     - Is the input actually user-controllable?
     - Are there validation/sanitization steps between input and query?
     - Does the framework/ORM handle parameterization automatically?
   * **Understand the ORM/framework behavior** - Many frameworks prevent injection by default:
     - ORMs like Hibernate, Entity Framework, SQLAlchemy parameterize by default
     - Query builders often escape automatically
     - Prepared statement APIs handle parameterization
   * **Check for existing protections** - Look for:
     - Input validation middleware
     - Parameterized query patterns elsewhere in the codebase
     - Framework-provided sanitization
   * **Confirm actual exploitability** - Can malicious input actually reach the query?

7. **For each VERIFIED vulnerability, provide:**
   - Exact code location (file, function, line numbers) AND the complete data flow path
   - Type of SQL injection vulnerability
   - Severity rating (Critical, High, Medium, Low) with **confidence level**
   - Evidence that no parameterization/sanitization exists
   - Attack vector and exploitation example (verified as possible)
   - Potential impact (data breach, data manipulation, privilege escalation)
   - Secure code example demonstrating proper remediation
   - Framework-specific best practices

**False-Positive Prevention (MUST follow):**
- ❌ Do NOT flag ORM queries as vulnerable without checking if they parameterize automatically
- ❌ Do NOT flag query builders without understanding their escaping behavior
- ❌ Do NOT flag code where input is validated/sanitized before reaching the query
- ❌ Do NOT flag internal data (not user-controllable) as injection vectors
- ❌ Do NOT flag prepared statement usage as "string concatenation"
- ✅ DO trace complete data flow from user input to query execution
- ✅ DO verify the framework/ORM doesn't handle parameterization automatically
- ✅ DO check for validation/sanitization middleware or utility functions
- ✅ DO distinguish between user input and internal/trusted data

8. **Test and validation recommendations:**
   - Suggest specific test cases for VERIFIED vulnerabilities
   - Recommend automated scanning tools
   - Provide manual testing techniques
   - Suggest SQL injection fuzzing strategies

**Expected Output:** A comprehensive SQL injection analysis report including:

- **Executive Summary:**
  - Total number of SQL injection vulnerabilities found
  - Risk level assessment (Critical, High, Medium, Low)
  - Overall security posture regarding SQL injection

- **Detailed Findings:**
  - Categorized list of vulnerabilities with:
    - Code locations and vulnerable code snippets
    - Vulnerability type and severity
    - Attack scenarios with example payloads
    - Impact analysis (data exposure, modification, deletion)
    - Step-by-step remediation guidance with secure code examples

- **Prevention Strategy:**
  - Recommended parameterized query patterns for the codebase
  - Input validation best practices
  - ORM configuration recommendations
  - Database security hardening steps
  - Developer training recommendations

- **Quick Wins:**
  - High-impact, easy-to-fix vulnerabilities
  - Framework-provided security features to implement
  - Code patterns to search and replace

- **Testing Plan:**
  - Recommended security testing tools
  - Test cases for validation
  - Continuous security testing integration

**Example Output Format:**

```
CRITICAL: SQL Injection in User Authentication
Location: src/auth/login.js:45
Vulnerable Code:
  const query = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`

Attack Vector: Attacker can input: username = ' OR '1'='1' --
Impact: Authentication bypass, unauthorized access to any account

Remediation:
  const query = 'SELECT * FROM users WHERE username=? AND password=?'
  db.query(query, [username, hashedPassword])
```

**Related Prompts:**
- security_owasp_top_10_analysis.md - Comprehensive security audit including injection
- security_api_testing.md - API security testing including injection vectors
- security_authentication_authorization_review.md - Authentication security review
- quality_code_style_consistency_analysis.md - Code quality and consistency

**When to Use:**
Use this prompt when conducting security audits, reviewing database-intensive applications, investigating potential SQL injection incidents, before major releases, or as part of secure code review processes.

**Techniques Used:**
- ST-01 (Clear Objective Statement) - Opens with concise, unambiguous objective
- ST-02 (Structured Sequential Instructions) - Numbered steps for systematic analysis
- DT-02 (Specific Focus Areas with Examples) - Detailed SQL injection vulnerability types
- RT-02 (Multi-Dimensional Analysis Framework) - Location, Type, Severity, Attack, Remediation
- DS-06 (Prioritization and Severity Guidance) - Severity ratings and quick wins section
- ST-03 (Output Format Templates) - Detailed vulnerability output format
- AG-05 (Concrete Deliverable Templates) - Secure code remediation examples
