---
title: "Codebase Best Practice Analysis"
category: software-engineering/improvement
description: "Audit a codebase for both good and bad programming practices, producing a balanced, evidence-anchored report with prioritized issues, exemplary patterns to reuse, and an actionable improvement roadmap."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-01
difficulty: advanced
tags:
  - code-audit
  - best-practices
  - technical-debt
  - code-quality
  - improvement
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/improvement/improvement_refactoring.md
  - domain-engineering-workflows/workflows/coding_problems_catalog.md
  - domain-software-engineering/improvement/improvement_language_translation.md
---

# Codebase Best Practice Analysis

**Objective:** Analyze a provided codebase and produce a balanced assessment of good and bad practices — with quoted evidence, the underlying principle for each finding, severity ranking, and an actionable improvement roadmap.

**When to use:**
- Code audits and technical due diligence on an unfamiliar codebase.
- Onboarding a team to existing code (highlighting both models and pitfalls).
- Establishing or calibrating coding standards from real examples.
- Prioritizing technical-debt remediation before new feature work.

**When NOT to use:**
- A targeted security review only — use `domain-software-engineering/analysis/security/`.
- A single-file refactor with no audit dimension — use `improvement_refactoring.md`.
- When no code is available to inspect (this prompt requires real source).

**Audience:** Engineers, tech leads, architects, and reviewers auditing or onboarding to a codebase.

---

## Inputs / Context

The user supplies:
1. **The codebase or representative slice** — wrap pasted source in a `<code>` tag (note language and file paths); or a repo path / directory tree.
2. **Stack and conventions** — language(s), frameworks, any team style guide.
3. **Focus areas** (optional) — e.g. security-heavy, performance-heavy, onboarding-oriented.
4. **Known constraints** — legacy areas off-limits, deployment targets, compliance requirements.

If only a fragment is provided, scope findings to what is visible and say so explicitly.

---

## Constraints

### Must
- Quote the **specific code** (with file:line where available) behind every finding — no abstract claims.
- Name the **principle** demonstrated or violated (SOLID, DRY, fail-fast, least privilege, etc.).
- Rank issues by severity: **Critical / High / Medium / Low**.
- Present **both** exemplary patterns and problems — a balanced assessment, not a defect list.
- Provide a concrete, code-level fix for each problem.
- End with a phased roadmap distinguishing quick wins from strategic investments.

### Must Not
- Invent metrics, benchmark numbers, test-coverage percentages, or complexity scores not derivable from the code.
- Flag style preferences as defects without anchoring them to a stated standard or principle.
- Recommend a rewrite where a targeted fix suffices.
- Assert a security vulnerability without tracing the exploitable path.

---

## Instructions

1. **Establish the evaluation framework.** State the dimensions you will assess: code quality (readability, naming, complexity), design principles (SOLID, DRY, KISS, YAGNI), architecture (separation of concerns, coupling), security (input validation, authz, data protection), performance (efficiency, resource management), testability.
2. **Review the codebase systematically.**
   - Map directory/module structure.
   - Examine key classes and functions.
   - Trace data flow and dependencies.
   - Note patterns, anti-patterns, and consistency across files.
3. **Document positive examples.** For each: quote the code, name the principle/pattern, explain the benefit, note how it can serve as a team template.
4. **Document problems.** For each: quote the code, name the violated principle, explain the consequence, give a concrete fix.
5. **Prioritize findings.** Assign Critical (security/data-corruption), High (perf/maintainability blockers), Medium (code smell/inconsistency), Low (style/minor).
6. **Build the improvement roadmap.** Phase the work; separate quick wins (low effort, high impact) from strategic investments; define success criteria.
7. **Self-check before reporting.** Verify every finding has quoted evidence, every problem has a fix, severities are justified, and no numbers were fabricated. Label any low-confidence finding as such.

---

## False-Positive Prevention

❌ **DON'T:**
- Don't claim a SQL-injection or auth bug without showing the unsanitized path from input to sink.
- Don't invent cyclomatic-complexity numbers, coverage %, or line counts you didn't measure.
- Don't label idiomatic-but-unfamiliar code as a "smell" just because you'd write it differently.
- Don't propose extracting/refactoring code whose full call-graph you cannot see.

✅ **DO:**
- Trace evidence: quote the exact lines and explain the mechanism.
- Label confidence ("likely", "confirmed from this slice", "needs wider context").
- Tie every finding to a named principle or a stated team standard.
- Flag where a finding depends on code not shown.

---

## Output Format

```markdown
# Best Practice Analysis Report

## Executive Summary
- Codebase / scope: [...]
- Overall health: [qualitative — e.g. "moderate, security gaps dominate"]
- Top 3 strengths: [...]
- Top 3 concerns: [...]

## Positive Examples Gallery
### Example N: [pattern] ([principle])
**Location:** [file:line]
```[lang]
[quoted code]
```
**Why it's good:** [...]  **Reuse as:** [template guidance]

## Issues and Recommendations
### [Critical|High|Medium|Low] — [issue name]
**Location:** [file:line]  **Principle violated:** [...]
```[lang]
[quoted vulnerable/problem code]
```
**Problem:** [mechanism + consequence]
**Fix:**
```[lang]
[corrected code]
```

## Improvement Roadmap
- Phase 1 (quick wins): [...]
- Phase 2 (...): [...]
- Success criteria: [...]
```

## Example Output

```markdown
# Best Practice Analysis Report

## Executive Summary

**Codebase**: Payment Processing Service
**Analysis Date**: January 2024
**Overall Health**: 6.5/10 (Moderate - Room for Improvement)

### Key Findings

| Category | Score | Exemplary | Issues |
|----------|-------|-----------|--------|
| Code Quality | 7/10 | 8 examples | 12 issues |
| Design Principles | 6/10 | 5 examples | 15 issues |
| Security | 5/10 | 3 examples | 8 issues |
| Performance | 7/10 | 4 examples | 6 issues |
| Testability | 6/10 | 3 examples | 9 issues |

### Top 3 Strengths
1. Consistent error handling pattern across services
2. Well-structured repository layer with clean interfaces
3. Comprehensive input validation on API endpoints

### Top 3 Concerns
1. SQL injection vulnerability in search functionality
2. N+1 query patterns causing performance degradation
3. Large "god classes" violating Single Responsibility

---

## Positive Examples Gallery

### Example 1: Clean Repository Interface (SOLID - Interface Segregation)

**Location:** `src/repositories/interfaces/IPaymentRepository.ts`

```typescript
// Focused interface - each method has clear purpose
interface IPaymentRepository {
  findById(id: string): Promise<Payment | null>;
  findByUserId(userId: string): Promise<Payment[]>;
  save(payment: Payment): Promise<Payment>;
  updateStatus(id: string, status: PaymentStatus): Promise<void>;
}

// Separate interface for analytics queries
interface IPaymentAnalyticsRepository {
  getMonthlyTotals(year: number): Promise<MonthlyTotal[]>;
  getPaymentsByMethod(dateRange: DateRange): Promise<MethodBreakdown>;
}
```

**Why This Is Good:**
- **Interface Segregation**: Clients depend only on methods they use
- **Clear Contract**: Each method has single, clear purpose
- **Testability**: Easy to mock specific behaviors
- **Flexibility**: Analytics can be implemented separately (different database, caching)

**Principle**: Interface Segregation Principle (ISP) - "Clients should not be forced to depend on interfaces they don't use"

**Recommendation**: Use this as a template for other repository interfaces.

---

### Example 2: Defensive Input Validation (Security)

**Location:** `src/middleware/validation/paymentValidation.ts`

```typescript
const createPaymentSchema = z.object({
  amount: z.number()
    .positive('Amount must be positive')
    .max(1000000, 'Amount exceeds maximum limit'),
  currency: z.enum(['USD', 'EUR', 'GBP']),
  customerId: z.string()
    .uuid('Invalid customer ID format'),
  metadata: z.record(z.string())
    .optional()
    .refine(
      (meta) => !meta || Object.keys(meta).length <= 10,
      'Maximum 10 metadata fields allowed'
    )
});

export const validateCreatePayment = (req: Request, res: Response, next: NextFunction) => {
  const result = createPaymentSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({
      error: 'Validation failed',
      details: result.error.flatten()
    });
  }
  req.validatedBody = result.data;
  next();
};
```

**Why This Is Good:**
- **Fail-Fast**: Invalid data rejected at boundary
- **Type Safety**: Runtime validation matches TypeScript types
- **Clear Error Messages**: Users get specific feedback
- **Defense in Depth**: Limits prevent abuse (max amount, max metadata)

**Principle**: "Never trust user input" - Validate early, validate strictly

---

### Example 3: Consistent Error Handling (Maintainability)

**Location:** `src/utils/errors.ts` and usage throughout

```typescript
// Custom error hierarchy
class AppError extends Error {
  constructor(
    public message: string,
    public statusCode: number,
    public code: string,
    public isOperational: boolean = true
  ) {
    super(message);
    Error.captureStackTrace(this, this.constructor);
  }
}

class ValidationError extends AppError {
  constructor(message: string, public details?: object) {
    super(message, 400, 'VALIDATION_ERROR');
  }
}

class NotFoundError extends AppError {
  constructor(resource: string, id: string) {
    super(`${resource} with id '${id}' not found`, 404, 'NOT_FOUND');
  }
}

// Centralized error handler
const errorHandler = (err: Error, req: Request, res: Response, next: NextFunction) => {
  if (err instanceof AppError) {
    logger.warn('Operational error', { code: err.code, message: err.message });
    return res.status(err.statusCode).json({
      error: { code: err.code, message: err.message }
    });
  }

  // Unexpected errors
  logger.error('Unexpected error', { error: err.stack });
  return res.status(500).json({
    error: { code: 'INTERNAL_ERROR', message: 'An unexpected error occurred' }
  });
};
```

**Why This Is Good:**
- **Consistency**: All errors follow same structure
- **Distinction**: Operational vs programming errors handled differently
- **Logging**: Appropriate detail level for each error type
- **Security**: Internal details not leaked to clients

---

## Issues and Recommendations

### Critical Issues

#### Issue C1: SQL Injection Vulnerability

**Location:** `src/repositories/SearchRepository.ts:45`
**Severity:** Critical
**Principle Violated:** Secure coding - Never concatenate user input into queries

```typescript
// CURRENT CODE - VULNERABLE
async searchTransactions(query: string, filters: any): Promise<Transaction[]> {
  const sql = `
    SELECT * FROM transactions
    WHERE description LIKE '%${query}%'
    AND status = '${filters.status}'
    ORDER BY ${filters.sortBy} ${filters.sortOrder}
  `;
  return this.db.query(sql);
}
```

**Problem:**
- Direct string interpolation allows SQL injection
- Attacker input: `query = "'; DROP TABLE transactions; --"`
- All transaction data could be deleted or exfiltrated

**Recommended Fix:**
```typescript
async searchTransactions(query: string, filters: SearchFilters): Promise<Transaction[]> {
  // Whitelist allowed sort columns
  const allowedSortColumns = ['created_at', 'amount', 'status'];
  const sortBy = allowedSortColumns.includes(filters.sortBy)
    ? filters.sortBy
    : 'created_at';

  const sortOrder = filters.sortOrder === 'ASC' ? 'ASC' : 'DESC';

  const sql = `
    SELECT * FROM transactions
    WHERE description LIKE $1
    AND status = $2
    ORDER BY ${sortBy} ${sortOrder}
  `;

  return this.db.query(sql, [`%${query}%`, filters.status]);
}
```

---

### High Priority Issues

#### Issue H1: N+1 Query Problem

**Location:** `src/services/ReportService.ts:78`
**Severity:** High
**Principle Violated:** Performance - Minimize database round trips

```typescript
// CURRENT CODE - N+1 QUERIES
async generateUserReport(userIds: string[]): Promise<UserReport[]> {
  const reports = [];
  for (const userId of userIds) {
    const user = await this.userRepository.findById(userId);
    const payments = await this.paymentRepository.findByUserId(userId);
    const stats = await this.statsRepository.getUserStats(userId);
    reports.push({ user, payments, stats });
  }
  return reports;
}
// For 100 users: 1 + (100 * 3) = 301 queries!
```

**Recommended Fix:**
```typescript
async generateUserReport(userIds: string[]): Promise<UserReport[]> {
  // Batch fetch all data
  const [users, payments, stats] = await Promise.all([
    this.userRepository.findByIds(userIds),
    this.paymentRepository.findByUserIds(userIds),
    this.statsRepository.getUserStatsBatch(userIds)
  ]);

  // Group by userId
  const paymentsByUser = groupBy(payments, 'userId');
  const statsByUser = keyBy(stats, 'userId');

  return users.map(user => ({
    user,
    payments: paymentsByUser[user.id] || [],
    stats: statsByUser[user.id]
  }));
}
// For 100 users: 3 queries total!
```

---

#### Issue H2: God Class Violating Single Responsibility

**Location:** `src/services/PaymentService.ts`
**Severity:** High
**Principle Violated:** Single Responsibility Principle (SRP)

```typescript
// CURRENT: 800+ line class doing everything
class PaymentService {
  // Payment processing (should be its own service)
  async processPayment() { /* 100 lines */ }
  async refundPayment() { /* 80 lines */ }

  // Notification (should be NotificationService)
  async sendPaymentEmail() { /* 50 lines */ }
  async sendSmsNotification() { /* 40 lines */ }

  // Reporting (should be ReportingService)
  async generateDailyReport() { /* 120 lines */ }
  async exportToCSV() { /* 60 lines */ }

  // Analytics (should be AnalyticsService)
  async trackPaymentMetrics() { /* 40 lines */ }
  async calculateConversionRate() { /* 30 lines */ }

  // Fraud detection (should be FraudService)
  async checkFraudRisk() { /* 100 lines */ }
  async blockSuspiciousPayment() { /* 50 lines */ }
}
```

**Problems:**
- Hard to test (too many dependencies)
- Changes ripple across unrelated features
- Multiple reasons to change
- Difficult to understand and maintain

**Recommended Refactoring:**
```typescript
// Split into focused services
class PaymentProcessingService {
  constructor(
    private paymentRepository: IPaymentRepository,
    private paymentGateway: IPaymentGateway
  ) {}

  async processPayment(dto: ProcessPaymentDto): Promise<Payment> { }
  async refundPayment(paymentId: string, amount?: number): Promise<Refund> { }
}

class PaymentNotificationService {
  constructor(
    private emailService: IEmailService,
    private smsService: ISmsService
  ) {}

  async notifyPaymentSuccess(payment: Payment): Promise<void> { }
  async notifyPaymentFailure(payment: Payment, reason: string): Promise<void> { }
}

class PaymentAnalyticsService {
  async trackPayment(payment: Payment): Promise<void> { }
  async getConversionMetrics(dateRange: DateRange): Promise<Metrics> { }
}

// Orchestrator coordinates the services
class PaymentOrchestrator {
  constructor(
    private processingService: PaymentProcessingService,
    private notificationService: PaymentNotificationService,
    private analyticsService: PaymentAnalyticsService,
    private fraudService: FraudDetectionService
  ) {}

  async executePayment(dto: ProcessPaymentDto): Promise<PaymentResult> {
    await this.fraudService.checkRisk(dto);
    const payment = await this.processingService.processPayment(dto);
    await this.notificationService.notifyPaymentSuccess(payment);
    await this.analyticsService.trackPayment(payment);
    return payment;
  }
}
```

---

## Improvement Roadmap

### Phase 1: Critical Fixes (Week 1)
- [ ] Fix SQL injection in SearchRepository
- [ ] Add parameterized queries audit across all repositories
- [ ] Implement security review checklist

### Phase 2: Performance (Weeks 2-3)
- [ ] Resolve N+1 query issues in ReportService
- [ ] Add database query logging to identify other N+1 patterns
- [ ] Implement caching for frequently accessed data

### Phase 3: Architecture (Weeks 4-6)
- [ ] Refactor PaymentService into focused services
- [ ] Establish service boundary guidelines
- [ ] Create architectural decision records (ADRs)

### Success Metrics
- Zero critical security vulnerabilities
- 90% reduction in database queries for reports
- Average class size < 200 lines
- Test coverage > 80%
```

---

## Verification

- [ ] Every finding quotes specific code (file:line where available).
- [ ] Both exemplary patterns and problems are reported.
- [ ] Each finding names the underlying principle.
- [ ] Issues are ranked Critical / High / Medium / Low with justification.
- [ ] Every problem has a concrete, code-level fix.
- [ ] No metrics, coverage %, or complexity scores were fabricated.
- [ ] Security findings trace the exploitable path.
- [ ] Roadmap separates quick wins from strategic investments with success criteria.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the balanced-audit goal up front.
- **ST-02 (Structured Sequential Instructions):** Framework → review → document → prioritize → roadmap.
- **RT-02 (Multi-Dimensional Analysis):** Assesses quality, design, architecture, security, performance, testability in parallel.
- **DS-06 (Prioritization and Severity Guidance):** Critical/High/Medium/Low ranking drives the roadmap.
- **QA-01 (Self-Verification):** Pre-report self-check confirms evidence, fixes, and no fabrication.

---

## Related Prompts

- `domain-software-engineering/improvement/improvement_refactoring.md` — Execute fixes the audit surfaces.
- `domain-engineering-workflows/workflows/coding_problems_catalog.md` — Reference taxonomy of code issues to look for.
- `domain-software-engineering/improvement/improvement_language_translation.md` — Ensure quality when porting to a new language.
