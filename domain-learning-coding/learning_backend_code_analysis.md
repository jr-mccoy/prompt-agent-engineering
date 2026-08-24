---
title: "Backend Code Analysis — Teach a Learner the Strengths, Risks, and Fixes in Backend Code"
category: "learning-coding"
description: "Analyze supplied backend code to teach a learner its architecture, data-access, security, scalability, and testing characteristics — surfacing accurate strengths, real issues with before/after fixes, and a prioritized improvement list grounded in the actual code."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - backend
  - code-analysis
  - security
  - performance
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_frontend_code_analysis.md
  - domain-learning-coding/learning_code_pattern_recognition.md
  - domain-software-engineering/analysis/security/security_vulnerability_analysis.md
  - domain-software-engineering/analysis/performance/performance_bottleneck_identification.md
---

# Backend Code Analysis

**Objective:** Analyze supplied backend code to teach a learner its quality, surfacing accurate strengths, real issues (with before/after fixes), and a prioritized improvement list — all grounded in the actual code, never invented.

**When to use:**
- Helping a learner understand an unfamiliar backend codebase by walking its real patterns.
- Onboarding a new backend developer to a service's architecture and risks.
- Preparing a code-quality or pre-production review of a backend module.
- Teaching security, data-access, and scalability concepts using concrete examples.

**When NOT to use:**
- A formal penetration test or compliance audit — use dedicated security prompts.
- Frontend code — use `learning_frontend_code_analysis.md`.
- When you have no code to analyze and would have to speculate about behavior.

**Audience:** Backend learners (junior to mid-level), engineers onboarding, and reviewers teaching quality standards.

---

## Inputs / Context

The user supplies:
1. **The backend code** — pasted wrapped in a named tag, e.g. `<code>...</code>`, or a reference (framework + file paths).
2. **Language / framework** (Node/Express, NestJS, Spring, Django, Go, etc.).
3. **Learner level** (beginner / intermediate / advanced) so explanations and depth can be calibrated.
4. **Learning goal** (architecture understanding, security, performance, scalability, testability).
5. **Optional:** known pain points, SLAs, or scaling targets.

Reference the pasted code by its tag name (e.g. "the query in `<code>`") when citing issues.

---

## Constraints

### Must
- Analyze only what the supplied code shows; trace the actual control and data flow before judging it. If behavior is unclear, say so and ask rather than assume.
- Cite a concrete location (file/function/line range or quoted snippet) for every issue and every strength.
- For each issue, show a before/after with an explanation a learner at the stated level can follow.
- Distinguish confirmed issues from suspected ones; label severity honestly.
- Cover architecture, data access, security, scalability, and testing/observability.

### Must Not
- Invent vulnerabilities, N+1 queries, or behaviors that the code does not contain.
- Assume framework behavior (e.g. that an ORM auto-parameterizes) without confirming it in the code.
- Flag style preferences as critical issues.
- Oversimplify a fix to the point where it would break correctness.

---

## Instructions

1. **Trace the code.** Read `<code>` and map the layers (controllers/handlers, services, data access), the request/data flow, and external dependencies. Flag anything you cannot determine with certainty.
2. **Assess architecture.** Evaluate layer separation, dependency injection, configuration handling, and error strategy as they actually appear.
3. **Review data access.** Look for real query inefficiencies (N+1, missing indexes evident from code, unbounded fetches), transaction boundaries, and caching/invalidation.
4. **Assess security.** Check input handling, query construction (injection risk), authn/authz, secrets handling, and logging of sensitive data — citing the exact code.
5. **Evaluate scalability and operability.** Statelessness, background work, idempotency, health checks, structured logging, and metrics, where present.
6. **Write findings.** For each issue: location, severity, why it matters (level-appropriate), and a before/after fix. For each strength: location and why it's good.
7. **Prioritize.** Produce a ranked action table (severity × effort) with a sequenced next-steps plan.
8. **Self-check (verification).** Re-trace each finding: is the cited code real, is the severity honest, does the fix preserve behavior, and is any uncertainty flagged?

---

## False-Positive Prevention

❌ **DON'T:**
- Report a vulnerability or performance problem you haven't traced to specific code.
- Assume an ORM/library parameterizes input, handles transactions, or caches unless the code shows it.
- Inflate severity to make the report look thorough.
- Recommend a fix without checking it preserves the original behavior.
- Assume the learner knows terms like "N+1," "idempotent," or "DI" — define them at the stated level.

✅ **DO:**
- Trace control and data flow on a concrete request path before judging.
- Cite the exact location for every claim.
- Mark suspected-but-unconfirmed issues as such, and ask when behavior is ambiguous.
- Calibrate explanations and fix complexity to the stated learner level.
- Verify each before/after preserves correctness.

---

## Output Format

```
# Backend Code Analysis — [module/service]

## Summary
- Health snapshot: [per-category one-liners]
- Critical issues: [bulleted, each with location]

## Architecture
- Strengths: [location + why]
- Issues: [Issue ID — severity — location — fix]

## Data Access
[same structure]

## Security
[same structure]

## Scalability & Observability
[same structure]

## Prioritized Recommendations
| Priority | Issue | Action | Effort |
|----------|-------|--------|--------|

## Next Steps (sequenced)
[immediate / this sprint / this quarter]
```

---

## Example Output

```markdown
# Backend Code Analysis — Order Service

## Summary
| Category | Assessment |
|----------|------------|
| Architecture | Good layer separation; some logic leaking into controllers |
| Security | Critical: SQL injection in product search |
| Data Access | High: N+1 in order listing |
| Scalability | Mostly stateless; missing cache layer |
| Testing | Coverage gaps on error paths |

### Critical Issues
1. **SQL injection** in `ProductRepository.searchProducts` (`<code>` line ~45)
2. **Hardcoded DB credentials** in `config/database.ts`
3. **N+1 query** in `OrderService.getOrdersWithItems`

---

## Security

**Issue S1: SQL Injection (Critical)** — `ProductRepository.searchProducts`

```typescript
// BEFORE: user input concatenated into SQL — injectable
async searchProducts(query: string): Promise<Product[]> {
  return this.db.query(`SELECT * FROM products WHERE name LIKE '%${query}%'`);
}
// Attack: query = "'; DROP TABLE products; --"

// AFTER: parameterized query
async searchProducts(query: string): Promise<Product[]> {
  return this.db.query('SELECT * FROM products WHERE name LIKE $1', [`%${query}%`]);
}
```
*Why it matters (intermediate):* anything the user types becomes part of the SQL command. Parameterized queries send the value separately from the command, so it can't change the query's structure.

**Issue S2: Hardcoded Secrets (High)** — `config/database.ts`

```typescript
// BEFORE
export const dbConfig = { host: 'prod-db', username: 'admin', password: 'super_secret_123' };
// AFTER
export const dbConfig = { host: process.env.DB_HOST, username: process.env.DB_USERNAME, password: process.env.DB_PASSWORD };
const required = ['DB_HOST', 'DB_USERNAME', 'DB_PASSWORD'];
for (const v of required) if (!process.env[v]) throw new Error(`Missing env var: ${v}`);
```

---

## Data Access

**Issue P1: N+1 Query (High)** — `OrderService.getOrdersWithItems`

```typescript
// BEFORE: 1 query for orders + 1 per order for items
const orders = await this.orderRepository.findByUserId(userId);
for (const order of orders) {
  order.items = await this.orderItemRepository.findByOrderId(order.id); // x N
}

// AFTER: single query with eager loading
return this.orderRepository.find({ where: { userId }, relations: ['items', 'items.product'] });
```
*Why it matters (intermediate):* "N+1" means one query to get the list, then one extra query per row — 20 orders = 21 queries. Eager loading fetches everything in one round trip.

---

## Prioritized Recommendations

| Priority | Issue | Action | Effort |
|----------|-------|--------|--------|
| Critical | SQL injection | Parameterize the query | 1 day |
| Critical | Hardcoded secrets | Move to env + validate at startup | 0.5 day |
| High | N+1 queries | Eager loading | 2 days |
| Medium | Logic in controllers | Move to service layer | 3 days |

## Next Steps (sequenced)
1. **Immediate:** fix SQL injection, remove secrets.
2. **This sprint:** resolve N+1, add input validation.
3. **This quarter:** thin controllers, raise test coverage on error paths.
```

---

## Verification

- [ ] Every issue and strength cites a real location in the supplied code.
- [ ] Control/data flow was traced before judgments were made.
- [ ] Suspected-but-unconfirmed items are labeled as such; ambiguity prompted a question.
- [ ] Each before/after fix preserves the original behavior.
- [ ] Severity ratings are honest, not inflated.
- [ ] Explanations are calibrated to the stated learner level.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the task as accurate, teaching-oriented backend analysis.
- **ST-02 (Structured Sequential Instructions):** Trace → architecture → data → security → scalability → prioritize → verify.
- **RT-02 (Multi-Dimensional Analysis Framework):** Examines architecture, security, performance, scalability, and testing together.
- **RT-05 (Evidence-Based Reasoning):** Requires a cited location for every claim.
- **QA-01 (Self-Verification):** Final pass re-checks accuracy, severity, and fix correctness.

---

## Related Prompts

- `domain-learning-coding/learning_frontend_code_analysis.md` — Frontend counterpart.
- `domain-learning-coding/learning_code_pattern_recognition.md` — Identify the patterns in the code first.
- `domain-software-engineering/analysis/security/security_vulnerability_analysis.md` — Deeper security pass.
- `domain-software-engineering/analysis/performance/performance_bottleneck_identification.md` — Performance deep-dive.
