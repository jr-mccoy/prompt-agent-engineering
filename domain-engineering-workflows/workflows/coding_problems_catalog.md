---
title: "Coding Problems, Issues, and Errors Catalog"
category: engineering-workflows/workflows
description: "A categorized reference taxonomy of architecture, quality, security, performance, and evolution defects — with manifestations, impact, detection method, and remediation — to drive code review, audits, and refactoring prioritization."
techniques:
  - ST-01
  - RT-02
  - DS-06
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - code-review
  - code-smells
  - defect-taxonomy
  - technical-debt
  - reference
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/improvement/improvement_best_practice_analysis.md
  - domain-software-engineering/improvement/improvement_refactoring.md
  - domain-engineering-workflows/workflows/engineering_debugging_root_cause.md
---

# Coding Problems, Issues, and Errors Catalog

**Objective:** Provide and apply a categorized taxonomy of common code defects — architecture, quality, security, performance, and evolution — so a reviewer can name what they found, explain its impact, choose a detection method, and prioritize remediation.

**When to use:**
- As a checklist during code review or a codebase audit.
- To classify and label an issue you've already spotted.
- To prioritize a backlog of technical-debt items by category and impact.
- As shared vocabulary for communicating problems to a team.

**When NOT to use:**
- Executing a specific refactor — use `improvement_refactoring.md`.
- Producing a full evidence-anchored audit report — use `improvement_best_practice_analysis.md`.
- Diagnosing one live bug's root cause — use `engineering_debugging_root_cause.md`.

**Audience:** Engineers, reviewers, and tech leads classifying and prioritizing code issues.

---

## Inputs / Context

The user supplies:
1. **The code or findings to classify** — wrap pasted source in a `<code>` tag (note language/paths), or a list of observed issues.
2. **Focus area** (optional) — architecture, quality, security, performance, or evolution.
3. **Constraints** — what counts as in-scope (e.g. severity floor, off-limits modules).

When applying the catalog, map each finding to a category, cite the evidence, and assign severity. Do not assert an issue exists without the supporting code.

---

## Constraints

### Must
- Map each finding to a catalog category and name the specific problem.
- Quote the evidence (code or observed behavior) behind each classification.
- State impact and a detection method for each issue.
- Assign severity (Critical / High / Medium / Low) when prioritizing.

### Must Not
- Fabricate metrics (complexity scores, coverage %, line counts) not measured from the code.
- Label a style preference as a defect without a principle or stated standard.
- Assert a security vulnerability without tracing the exploitable path.
- Force a finding into a category it doesn't fit — leave it "uncategorized / needs review" instead.

---

## Instructions

1. **Identify the category.** Architecture, quality, security, performance, or evolution — using the taxonomy below.
2. **Name the specific problem.** Match to the catalog entry (e.g. "N+1 query," "god object," "SQL injection").
3. **Quote the evidence.** Cite the code or observed behavior; for security, trace input → sink.
4. **State impact and detection.** Use the catalog's impact and detection notes, adapted to the actual code.
5. **Assign severity and remediation.** Critical/High/Medium/Low plus the catalog's solution.
6. **Self-check before reporting.** Confirm each finding has evidence, a category, and a non-fabricated impact statement; flag anything uncertain.

---

## 1. Architecture Issues

### 1.1 API-Related Problems

#### API Specification Mismatches
- **Problem:** Code implementation doesn't match the API specification (OpenAPI/Swagger)
- **Manifestations:**
  - Incorrect HTTP methods (GET vs POST)
  - Missing or extra request parameters
  - Mismatched request/response body structures
  - Wrong HTTP status codes for error conditions
  - Missing required endpoints
- **Impact:** Integration failures, client confusion, contract violations
- **Detection:** API conformance checking against specification documents

#### Missing or Incorrect API Client Code
- **Problem:** No standardized way to interact with APIs
- **Manifestations:**
  - Manual HTTP request construction in multiple places
  - Inconsistent error handling across API calls
  - Missing authentication implementation
  - No data model classes for API responses
- **Impact:** Code duplication, inconsistent API usage, harder maintenance
- **Detection:** Absence of client libraries or SDKs

### 1.2 Coupling and Cohesion Problems

#### High Coupling (Tight Coupling)
- **Problem:** Modules depend heavily on many other modules
- **Manifestations:**
  - Changes in one module require changes in many others
  - Circular dependencies between modules
  - Direct access to internal implementation details
  - Hard-coded dependencies
- **Impact:** Difficult to test, maintain, or modify independently
- **Detection:** Dependency graph analysis showing many connections

#### Low Cohesion
- **Problem:** Modules contain unrelated functionalities
- **Manifestations:**
  - A single class handling UI, business logic, and data access
  - Utility classes with unrelated helper methods
  - Modules with responsibilities that don't belong together
- **Impact:** Harder to understand, difficult to reuse, violation of Single Responsibility Principle
- **Detection:** Analysis of class/module responsibilities

### 1.3 Database Architecture Issues

#### Poor Normalization
- **Problem:** Database schema has redundant data or isn't properly normalized
- **Manifestations:**
  - Duplicate data across multiple tables
  - Update anomalies (updating one place but not others)
  - Insertion anomalies (can't add data without other data)
  - Deletion anomalies (deleting one thing removes unrelated data)
- **Impact:** Data inconsistency, wasted storage, harder maintenance
- **Detection:** Schema analysis against normal forms (1NF, 2NF, 3NF)

#### Missing or Inefficient Indexes
- **Problem:** Database queries are slow due to lack of proper indexes
- **Manifestations:**
  - Full table scans on large tables
  - Slow WHERE clause evaluations
  - Inefficient JOIN operations
  - Queries timing out under load
- **Impact:** Poor query performance, slow application response times
- **Detection:** Query plan analysis, performance profiling

#### Inefficient Data Types
- **Problem:** Using wrong or suboptimal data types
- **Manifestations:**
  - VARCHAR(255) for everything
  - Storing dates as strings
  - Using TEXT for short strings
  - No use of ENUM or specialized types
- **Impact:** Wasted storage, slower queries, data validation issues
- **Detection:** Schema review

### 1.4 Layer Separation Issues

#### Blurred Architectural Layers
- **Problem:** Presentation, business logic, and data access layers are mixed
- **Manifestations:**
  - SQL queries in UI code
  - Business logic in database stored procedures
  - Direct database access from controllers
  - UI logic in business services
- **Impact:** Hard to test, difficult to change persistence or UI, poor separation of concerns
- **Detection:** Code analysis for layer violations

#### Missing Architectural Patterns
- **Problem:** No clear architectural pattern followed (MVC, MVVM, Clean Architecture)
- **Manifestations:**
  - No consistent code organization
  - Each developer using different patterns
  - Mixed responsibilities across layers
- **Impact:** Inconsistent codebase, harder onboarding, maintainability issues
- **Detection:** Architecture analysis and pattern identification

### 1.5 Design Pattern Issues

#### Absence of Needed Design Patterns
- **Problem:** Common design problems solved with ad-hoc code instead of established patterns
- **Manifestations:**
  - Complex conditional logic instead of Strategy pattern
  - Global state access instead of Singleton or Dependency Injection
  - Manual object creation instead of Factory pattern
  - Direct class coupling instead of Adapter or Facade
- **Impact:** Less maintainable, harder to extend, more error-prone
- **Detection:** Code smell analysis, pattern recognition

#### Anti-Patterns
- **Problem:** Known bad practices implemented in code
- **Common Anti-Patterns:**
  - God Object (one class does everything)
  - Spaghetti Code (no structure, everything tangled)
  - Golden Hammer (using one solution for all problems)
  - Magic Strings/Numbers (hardcoded values everywhere)
  - Copy-Paste Programming
- **Impact:** Poor maintainability, bugs, difficulty understanding code

---

## 2. Quality Issues

### 2.1 Complexity Issues

#### High Cyclomatic Complexity
- **Problem:** Too many decision points in a single function/method
- **Manifestations:**
  - Deeply nested if-else statements
  - Long switch/case statements
  - Multiple intertwined conditions
  - Functions with 10+ decision paths
- **Impact:** Hard to understand, difficult to test completely, error-prone
- **Detection:** Cyclomatic complexity metrics (McCabe complexity)
- **Threshold:** Generally >10 is concerning, >20 is problematic

#### Deep Nesting
- **Problem:** Code has many levels of indentation
- **Manifestations:**
  - Indentation levels >3-4
  - Nested loops within conditionals within loops
  - "Arrow code" pattern (>>>>> shape)
- **Impact:** Difficult to read and follow logic, prone to errors
- **Detection:** Static analysis of indentation levels

#### Excessive Method/Function Length
- **Problem:** Functions that are too long
- **Manifestations:**
  - Functions spanning hundreds of lines
  - Single function doing multiple distinct tasks
  - Difficult to name because it does too much
- **Impact:** Hard to understand, difficult to reuse, testing challenges
- **Detection:** Lines of code per function metrics
- **Threshold:** >50 lines often indicates issues, >100 is problematic

### 2.2 Code Duplication Issues

#### Exact Duplication
- **Problem:** Identical or nearly identical code in multiple places
- **Manifestations:**
  - Copy-pasted functions with minor modifications
  - Repeated code blocks
  - Same logic implemented multiple times
- **Impact:** Bugs fixed in one place but not others, maintenance burden
- **Detection:** Clone detection tools, similarity analysis
- **Threshold:** >6 lines of identical code is concerning

#### Structural Duplication
- **Problem:** Same pattern or structure repeated with different values
- **Manifestations:**
  - Similar functions differing only in constants
  - Repeated patterns that could be abstracted
  - Template-like code not using templates
- **Impact:** Missed abstraction opportunities, harder to maintain
- **Detection:** Structural pattern analysis

### 2.3 Documentation Issues

#### Insufficient Documentation Coverage
- **Problem:** Code lacks adequate documentation
- **Manifestations:**
  - Undocumented public APIs
  - No class or module-level documentation
  - Complex algorithms without explanation
  - No parameter or return value descriptions
- **Impact:** Difficult for others to understand and use, poor maintainability
- **Detection:** Documentation coverage analysis
- **Metrics:** % of public APIs documented, % of classes with docstrings

#### Poor Documentation Quality
- **Problem:** Documentation exists but is not helpful
- **Manifestations:**
  - Obvious comments ("i++; // increment i")
  - Outdated documentation that doesn't match code
  - Vague descriptions
  - No examples of usage
- **Impact:** Misleading, wastes developer time, can cause errors
- **Detection:** Documentation quality review

### 2.4 Code Style Issues

#### Inconsistent Naming Conventions
- **Problem:** Variables, functions, classes named inconsistently
- **Manifestations:**
  - Mix of camelCase and snake_case
  - Inconsistent capitalization
  - Abbreviations in some places, full words in others
  - No clear naming pattern
- **Impact:** Confusion, harder to search, unprofessional appearance
- **Detection:** Style linters, naming convention analysis

#### Formatting Inconsistencies
- **Problem:** Inconsistent code formatting
- **Manifestations:**
  - Mix of tabs and spaces
  - Inconsistent indentation width
  - Varying line lengths
  - Inconsistent brace placement
  - Inconsistent whitespace usage
- **Impact:** Merge conflicts, harder to read, team friction
- **Detection:** Code formatters, style checkers

#### Comment Style Inconsistencies
- **Problem:** No standard for how comments are written
- **Manifestations:**
  - Mix of inline and block comments for same purpose
  - Inconsistent comment headers
  - Some files with extensive comments, others with none
- **Impact:** Unprofessional appearance, harder to maintain
- **Detection:** Comment style analysis

### 2.5 Code Smell Issues

#### Large Class/God Object
- **Problem:** One class that knows or does too much
- **Impact:** Hard to understand, test, and maintain
- **Solution:** Break into smaller, focused classes

#### Long Method
- **Problem:** Method doing too many things
- **Impact:** Hard to understand and reuse
- **Solution:** Extract smaller methods

#### Shotgun Surgery
- **Problem:** Making a change requires touching many classes
- **Impact:** Error-prone, time-consuming changes
- **Solution:** Consolidate related changes

#### Divergent Change
- **Problem:** One class changes for multiple different reasons
- **Impact:** Violates Single Responsibility Principle
- **Solution:** Split into focused classes

---

## 3. Security Issues

### 3.1 Injection Vulnerabilities

#### SQL Injection
- **Problem:** User input directly concatenated into SQL queries
- **Manifestations:**
  - String concatenation to build SQL: `"SELECT * FROM users WHERE id=" + userId`
  - No parameterized queries
  - No input validation before database queries
- **Impact:** Database compromise, data theft, data manipulation
- **Detection:** Static analysis for SQL string concatenation
- **Solution:** Use parameterized queries, ORMs, input validation

#### Command Injection
- **Problem:** User input passed to system commands
- **Manifestations:**
  - `os.system()` or `exec()` with user input
  - Shell command construction with string concatenation
- **Impact:** System compromise, arbitrary code execution
- **Detection:** Static analysis for system call patterns
- **Solution:** Avoid shell commands, use libraries, validate input

### 3.2 Cross-Site Scripting (XSS)

#### Reflected XSS
- **Problem:** User input reflected in HTML without sanitization
- **Manifestations:**
  - Echoing URL parameters directly to page
  - Displaying user input without encoding
- **Impact:** Cookie theft, session hijacking, malicious actions
- **Solution:** HTML encoding, Content Security Policy

#### Stored XSS
- **Problem:** Malicious input stored and displayed to others
- **Manifestations:**
  - Storing unvalidated user content
  - Displaying stored content without sanitization
- **Impact:** Persistent attacks affecting multiple users
- **Solution:** Input validation, output encoding, sanitization

### 3.3 Authentication and Authorization Issues

#### Broken Authentication
- **Problem:** Weak or missing authentication mechanisms
- **Manifestations:**
  - Passwords stored in plain text
  - Weak password requirements
  - No account lockout after failed attempts
  - Predictable session tokens
- **Impact:** Unauthorized access, account takeover
- **Detection:** Security audit of authentication flows
- **Solution:** Strong password hashing, MFA, secure session management

#### Broken Authorization
- **Problem:** Users can access resources they shouldn't
- **Manifestations:**
  - No permission checks before operations
  - Client-side only authorization
  - Insecure Direct Object Reference (IDOR)
  - Missing function-level access control
- **Impact:** Privilege escalation, data exposure
- **Detection:** Authorization testing, code review
- **Solution:** Server-side authorization checks, role-based access control

### 3.4 Data Exposure

#### Sensitive Data Exposure
- **Problem:** Sensitive information not properly protected
- **Manifestations:**
  - Passwords, API keys in source code
  - Sensitive data logged
  - No encryption for sensitive data
  - Detailed error messages revealing system info
- **Impact:** Data breaches, compliance violations
- **Detection:** Secret scanning, code review
- **Solution:** Environment variables, encryption, error handling

#### Cross-Site Request Forgery (CSRF)
- **Problem:** Malicious sites can make requests as authenticated user
- **Manifestations:**
  - State-changing operations without CSRF tokens
  - No validation of request origin
- **Impact:** Unwanted actions performed as user
- **Solution:** CSRF tokens, SameSite cookies

---

## 4. Performance Issues

### 4.1 Algorithm Efficiency Problems

#### Inefficient Algorithms
- **Problem:** Using algorithms with poor time complexity
- **Manifestations:**
  - O(n²) when O(n log n) available
  - Linear search when hash lookup possible
  - Nested loops that could be optimized
  - No memoization for recursive calls
- **Impact:** Slow execution, poor scalability
- **Detection:** Algorithm analysis, profiling
- **Solution:** Use appropriate data structures and algorithms

#### Inefficient Data Structures
- **Problem:** Wrong data structure for the use case
- **Manifestations:**
  - Array for frequent insertions/deletions
  - List for frequent lookups
  - No use of hash maps where appropriate
- **Impact:** Poor performance, wasted resources
- **Solution:** Choose data structures based on access patterns

### 4.2 Database Performance Issues

#### N+1 Query Problem
- **Problem:** Making N database queries instead of 1
- **Manifestations:**
  - Query in a loop
  - Lazy loading causing multiple queries
  - No use of JOINs or eager loading
- **Impact:** Severe performance degradation
- **Detection:** Query logging, profiling
- **Solution:** Batch queries, eager loading, JOINs

#### Missing Query Optimization
- **Problem:** Queries not optimized for performance
- **Manifestations:**
  - SELECT * instead of specific columns
  - No use of LIMIT
  - Inefficient JOIN conditions
  - No use of query hints
- **Impact:** Slow queries, high database load
- **Solution:** Query optimization, indexing

#### Missing Database Connection Pooling
- **Problem:** Creating new database connections for each request
- **Impact:** High overhead, resource exhaustion
- **Solution:** Connection pooling

### 4.3 Network Performance Issues

#### Excessive Network Requests
- **Problem:** Too many network calls
- **Manifestations:**
  - No batching of requests
  - No use of pagination
  - Fetching all data when partial data needed
- **Impact:** Slow response times, high bandwidth usage
- **Solution:** Request batching, pagination, GraphQL

#### Large Payload Sizes
- **Problem:** Transferring too much data
- **Manifestations:**
  - No data compression
  - Sending full objects when partial data needed
  - Large images without optimization
- **Impact:** Slow transfers, high bandwidth costs
- **Solution:** Compression, field filtering, image optimization

### 4.4 Resource Usage Issues

#### Memory Leaks
- **Problem:** Objects not released when no longer needed
- **Manifestations:**
  - Event listeners not removed
  - Circular references preventing GC
  - Global variables holding references
  - Cached data never cleared
- **Impact:** Increasing memory usage, eventual crashes
- **Detection:** Memory profiling, heap dumps
- **Solution:** Proper cleanup, weak references

#### Excessive CPU Usage
- **Problem:** Code consuming too much CPU
- **Manifestations:**
  - Tight loops without sleep
  - Inefficient algorithms on hot paths
  - No use of async operations
  - Redundant calculations
- **Impact:** Slow response, high costs
- **Detection:** CPU profiling
- **Solution:** Optimization, caching, async operations

#### High Disk I/O
- **Problem:** Excessive file system operations
- **Manifestations:**
  - Reading files in loops
  - No buffering for file operations
  - Frequent small writes
- **Impact:** Slow operations, disk wear
- **Solution:** Batching, caching, buffering

### 4.5 Concurrency Issues

#### Race Conditions
- **Problem:** Multiple threads accessing shared data concurrently
- **Manifestations:**
  - Unsynchronized access to shared variables
  - Check-then-act patterns without locks
  - Counter updates without atomic operations
- **Impact:** Data corruption, inconsistent state
- **Detection:** Concurrency testing, static analysis
- **Solution:** Locks, atomic operations, immutability

#### Deadlocks
- **Problem:** Threads waiting for each other indefinitely
- **Manifestations:**
  - Incorrect lock ordering
  - Nested locks
  - Resource contention
- **Impact:** Application hangs, timeouts
- **Detection:** Deadlock detection tools
- **Solution:** Lock ordering, timeouts, deadlock detection

#### Excessive Locking
- **Problem:** Too much synchronization causing contention
- **Manifestations:**
  - Locking at coarse granularity
  - Holding locks too long
  - No use of lock-free data structures
- **Impact:** Poor concurrency performance
- **Solution:** Fine-grained locking, lock-free structures

### 4.6 Scalability Issues

#### Lack of Horizontal Scalability
- **Problem:** Can't add more instances to handle load
- **Manifestations:**
  - Shared state across instances
  - Session data in local memory
  - No load balancing support
- **Impact:** Limited by single machine capacity
- **Solution:** Stateless design, distributed caching

#### Database Scalability Bottlenecks
- **Problem:** Database becomes bottleneck
- **Manifestations:**
  - No read replicas
  - No sharding strategy
  - All queries to master
- **Impact:** Database overload under high traffic
- **Solution:** Replication, sharding, caching

---

## 5. Code Evolution Issues

### 5.1 Technical Debt

#### Accumulated Quick Fixes
- **Problem:** Hasty fixes that weren't properly addressed
- **Manifestations:**
  - TODO comments never addressed
  - Workarounds instead of root cause fixes
  - "Temporary" code that became permanent
- **Impact:** Growing maintenance burden
- **Detection:** Code review, TODO analysis

#### Deferred Refactoring
- **Problem:** Known improvements postponed
- **Manifestations:**
  - Documented need for refactoring never done
  - Growing code complexity over time
  - Increasing difficulty making changes
- **Impact:** Compounding difficulty, reduced velocity
- **Detection:** Complexity trend analysis

### 5.2 Code Churn Issues

#### High Churn Hotspots
- **Problem:** Files changed very frequently
- **Manifestations:**
  - Same files modified in most commits
  - Frequent bug fixes in same areas
  - Constant refactoring of same code
- **Impact:** Indicates design problems, complexity
- **Detection:** Version control analysis
- **Solution:** Refactor high-churn areas

### 5.3 Change Impact Issues

#### Unpredictable Ripple Effects
- **Problem:** Changes affecting unexpected parts of codebase
- **Manifestations:**
  - Changes breaking seemingly unrelated features
  - Difficult to predict impact of changes
  - Extensive testing needed for small changes
- **Impact:** Fear of making changes, bugs
- **Detection:** Dependency analysis, impact analysis
- **Solution:** Better modularity, decoupling

---

## Summary Table: Issue Categories

| Category | Issue Types | Detection Method | Primary Impact |
|----------|-------------|------------------|----------------|
| **Architecture** | Coupling, cohesion, layers, patterns | Dependency analysis, architecture review | Maintainability, testability |
| **Quality** | Complexity, duplication, documentation, style | Static analysis, metrics | Readability, maintainability |
| **Security** | Injection, XSS, auth, data exposure | Security scanning, code review | Data breaches, compliance |
| **Performance** | Algorithms, database, network, resources | Profiling, load testing | Speed, scalability, costs |
| **Evolution** | Technical debt, churn, impact | VCS analysis, trend analysis | Long-term maintainability |

---

## Common Root Causes

Across all categories, these root causes appear repeatedly:

1. **Lack of Planning:** Coding without design leads to architecture issues
2. **Time Pressure:** Rushing leads to technical debt and security issues
3. **Insufficient Knowledge:** Not knowing best practices causes multiple issues
4. **Poor Code Review:** Missing problems during review allows issues to accumulate
5. **No Automated Checks:** Without linters/scanners, issues slip through
6. **Inadequate Testing:** Poor tests miss performance and security issues
7. **Lack of Refactoring:** Not cleaning code leads to complexity and debt

---

## Conclusion

This catalog represents the comprehensive set of coding problems that professional code analysis addresses. Understanding these issues helps developers:

1. **Prevent problems** during initial development
2. **Recognize problems** during code review
3. **Diagnose problems** when debugging
4. **Prioritize problems** during refactoring
5. **Communicate problems** to team members

Each issue has detection methods and solutions, making this catalog a practical reference for improving code quality.

---

## False-Positive Prevention

❌ **DON'T:**
- Don't report cyclomatic-complexity, coverage %, or churn numbers you didn't measure — use the thresholds as guidance, not as findings.
- Don't classify code as a "god object" or "high coupling" without showing the responsibilities/dependencies that justify it.
- Don't flag a SQL-injection or auth issue without tracing the unsanitized path from input to sink.
- Don't tag idiomatic-but-unfamiliar code as a smell because you'd write it differently.

✅ **DO:**
- Quote the code or behavior behind each classification.
- Map each finding to a real category; leave true ambiguities "uncategorized / needs review."
- Tie severity to impact, and label any estimate as an estimate.
- Trace exploitable paths for security findings.

---

## Output Format

```markdown
# Issue Classification

## Findings
### [Category] — [specific problem]
**Location/Evidence:** [file:line or observed behavior]
**Manifestation:** [...]
**Impact:** [...]   **Detection:** [...]
**Severity:** Critical | High | Medium | Low
**Remediation:** [...]

## Prioritized Remediation
| Priority | Issue | Category | Effort | Impact |
|----------|-------|----------|--------|--------|
```

## Example Output

```markdown
# Issue Classification

## Findings

### Performance — N+1 Query Problem
**Location/Evidence:** `ReportService.generateUserReport` loops `findById` per user id.
**Manifestation:** One query per user inside a loop (1 + 3N queries for N users).
**Impact:** Severe latency and DB load as user count grows.   **Detection:** Query logging / profiling shows repeated single-row reads.
**Severity:** High
**Remediation:** Batch-fetch with `findByIds` and group in memory (3 queries total).

### Security — SQL Injection
**Location/Evidence:** `SearchRepository.searchTransactions` interpolates `query` and `filters.sortBy` into the SQL string.
**Manifestation:** User input concatenated into the query and ORDER BY clause.
**Impact:** Data exfiltration or destruction via crafted input.   **Detection:** Static analysis for string-built SQL; trace input → query sink.
**Severity:** Critical
**Remediation:** Parameterize values; whitelist sortable columns and sort direction.

## Prioritized Remediation
| Priority | Issue | Category | Effort | Impact |
|----------|-------|----------|--------|--------|
| Critical | SQL injection in search | Security | Low | Prevents breach |
| High | N+1 in report service | Performance | Medium | Major latency win |
```

---

## Verification

- [ ] Each finding mapped to a category and a specific named problem.
- [ ] Evidence (code/behavior) quoted for every classification.
- [ ] Impact and detection method stated per finding.
- [ ] Severity assigned; remediation provided.
- [ ] No fabricated metrics; security findings trace the exploitable path.
- [ ] Genuinely ambiguous findings marked "uncategorized / needs review."

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the classify-and-prioritize purpose.
- **RT-02 (Multi-Dimensional Analysis):** Covers architecture, quality, security, performance, and evolution dimensions.
- **DS-06 (Prioritization and Severity Guidance):** Severity ranking drives the remediation order.
- **CM-01 (Explicit Context Framing):** Each category includes manifestations, impact, and detection context.
- **QA-01 (Self-Verification):** Pre-report check enforces evidence and blocks fabricated metrics.

---

## Related Prompts

- `domain-software-engineering/improvement/improvement_best_practice_analysis.md` — Full evidence-anchored audit using this taxonomy.
- `domain-software-engineering/improvement/improvement_refactoring.md` — Remediate the issues this catalog surfaces.
- `domain-engineering-workflows/workflows/engineering_debugging_root_cause.md` — Diagnose a single live defect to root cause.
