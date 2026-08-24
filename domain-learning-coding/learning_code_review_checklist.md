---
title: "Code Review Checklist Generation — Build a Codebase-Specific, Observable Review Checklist"
category: "learning-coding"
description: "Generate a codebase-specific code-review checklist with observable yes/no criteria across quality, correctness, security, performance, testing, and docs — calibrated to the project's real stack, conventions, and past incidents."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - code-review
  - checklist
  - quality
  - team-standards
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_code_style_readability_analysis.md
  - domain-learning-coding/learning_socratic_dialogue_code_review.md
  - domain-software-engineering/analysis/security/security_vulnerability_analysis.md
  - domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md
---

# Code Review Checklist Generation

**Objective:** Generate a codebase-specific code-review checklist with observable yes/no criteria across quality, correctness, security, performance, testing, and documentation — calibrated to the project's real stack, conventions, and past incidents.

**When to use:**
- Establishing or standardizing code-review practice for a team.
- Onboarding reviewers and creating a PR template.
- Auditing inconsistent review quality.
- Teaching newer engineers what "good review" looks like for this codebase.

**When NOT to use:**
- A one-off review of a single PR (just review it directly).
- A pure security audit (use the security prompts).
- A generic checklist with no project context — the value here is specificity.

**Audience:** Team leads, reviewers, and developers learning to review for a specific codebase.

---

## Inputs / Context

The user supplies:
1. **Codebase context** — languages/frameworks, style guide, architecture patterns, and (optionally) representative code wrapped in a named tag, e.g. `<code>...</code>`.
2. **Compliance/security requirements** if any.
3. **Past incidents or recurring review issues** to encode as checks.
4. **Team maturity level** (junior-heavy vs senior) to calibrate explanation depth.
5. **Optional:** existing checklist to improve.

Reference any supplied code by its tag name when deriving project-specific checks.

---

## Constraints

### Must
- Make every item **observable** (a reviewer can answer yes/no without subjective debate) and concise.
- Include project-specific checks derived from the supplied stack, conventions, or incidents — not just generic items.
- Mark priority (blocking vs suggestion) and skip conditions where appropriate.
- Provide a short quick-scan list and a full categorized list.
- Where a check is generic best practice (not codebase-derived), don't claim it's a project convention.

### Must Not
- Pad the checklist with vague, unobservable items ("code should be clean").
- Invent project conventions, incidents, or thresholds not supplied or evident.
- Make every item blocking (it destroys signal).
- Copy a generic template without tailoring to the inputs.

---

## Instructions

1. **Assess context.** From the inputs (and `<code>` if provided), note the stack, conventions, architecture, and any incident-driven checks.
2. **Define categories.** Quality, correctness, security, performance, testing, documentation — adjusted to what's relevant for this project.
3. **Write observable items.** Each as a yes/no check with a good/bad example where it aids clarity; mark priority and skip conditions.
4. **Add project-specific checks.** Encode conventions and past incidents as concrete items, clearly flagged as project-specific.
5. **Build the quick-scan.** Pull the ~6–10 highest-leverage items for a 5-minute first pass.
6. **Add a review workflow and feedback legend.** Phases, escalation criteria, and comment-prefix conventions.
7. **Self-check (verification).** Is every item observable? Are project-specific items actually grounded in the inputs? Are priorities sensible?

---

## False-Positive Prevention

❌ **DON'T:**
- Include items a reviewer can't objectively check.
- Present generic best practices as if they were this team's established conventions.
- Invent incident history or numeric thresholds.
- Make everything blocking.
- Assume the reviewer knows why a check matters — give a one-line rationale or example for non-obvious ones.

✅ **DO:**
- Phrase items so two reviewers would answer the same way.
- Clearly separate project-specific checks (grounded in inputs) from generic ones.
- Mark blocking vs non-blocking and skip conditions.
- Keep items scannable.
- Calibrate explanation depth to team maturity.

---

## Output Format

```
# Code Review Checklist — [project]

## Quick Scan (5 min)
- [ ] [highest-leverage items]

## Full Checklist
### 1. Code Quality
- [ ] **[item]** [rationale/example] — [priority] [skip-if]
### 2. Functionality
### 3. Security
### 4. Performance
### 5. Testing
### 6. Documentation

## Project-Specific Checks
- [ ] [item grounded in stack/convention/incident]

## Review Workflow
[phases + escalation criteria]

## Feedback Legend
| Prefix | Meaning | Blocks Merge? |
```

---

## Example Output

```markdown
# Code Review Checklist — Orders Service (TypeScript / NestJS / PostgreSQL)

## Quick Scan (5 min)
- [ ] PR description explains the change and links a ticket
- [ ] PR is appropriately sized (< ~400 lines)
- [ ] No hardcoded secrets, no string-concatenated SQL
- [ ] New functionality has tests
- [ ] CI passes

## Full Checklist

### 1. Code Quality
- [ ] **Naming**: descriptive names — Bad `const d = new Date()` → Good `const createdAt = new Date()`. [suggestion]
- [ ] **Function length**: focused, < ~30 lines. [suggestion] [skip-if: simple data transforms]
- [ ] **No magic numbers**: literals replaced with named constants. [suggestion]

### 3. Security
- [ ] **Parameterized queries** (project uses TypeORM; raw queries must use `$1` params, not interpolation). [blocking]
  ```typescript
  // BAD
  db.query(`SELECT * FROM users WHERE id = '${userId}'`)
  // GOOD
  db.query('SELECT * FROM users WHERE id = $1', [userId])
  ```
- [ ] **No secrets in code**: config reads from env. [blocking]
- [ ] **Auth guard present** on protected routes (`@UseGuards`). [blocking]

### 4. Performance
- [ ] **No N+1**: list endpoints use `relations`/joins, not per-row queries. [blocking]
- [ ] Large datasets paginated. [suggestion]

### 5. Testing
- [ ] New code covered; error paths and edge cases tested. [blocking for new logic]
- [ ] Tests assert behavior, not implementation. [suggestion]

### 6. Documentation
- [ ] OpenAPI spec updated if API changed. [blocking if API changed]

## Project-Specific Checks
- [ ] **Idempotency-Key honored** on `POST /orders` — added after the "Double Charge Incident". [blocking]
- [ ] **No business logic in controllers** — must live in services (team convention). [suggestion]

## Review Workflow
- **Phase 1 (5 min):** description, size, CI, quick-scan.
- **Phase 2 (15–30 min):** file-by-file against the full checklist.
- **Escalate** to security/senior if: auth changes, new deps, schema changes, infra changes.

## Feedback Legend
| Prefix | Meaning | Blocks Merge? |
|--------|---------|---------------|
| `[blocking]` | Must fix before merge | Yes |
| `[suggestion]` | Optional improvement | No |
| `[question]` | Need clarification | Maybe |
| `[nitpick]` | Style preference | No |
| `[praise]` | Highlight good work | No |
```

---

## Verification

- [ ] Every item is observable (objective yes/no).
- [ ] Project-specific checks are grounded in the supplied stack/conventions/incidents.
- [ ] Generic checks aren't misrepresented as project conventions.
- [ ] Priorities (blocking vs non-blocking) and skip conditions are set.
- [ ] A quick-scan and a full checklist are both present.
- [ ] No invented incidents or thresholds.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as a specific, observable review checklist.
- **ST-02 (Structured Sequential Instructions):** Assess → categorize → write items → add specifics → quick-scan → workflow → verify.
- **ST-03 (Output Format Specification):** Fenced template fixes the checklist structure.
- **CM-02 (Constraint Specification):** Encodes must/must-not review criteria as explicit checks.
- **QA-01 (Self-Verification):** Final pass confirms observability and grounding.

---

## Related Prompts

- `domain-learning-coding/learning_code_style_readability_analysis.md` — Generate the style criteria behind the quality section.
- `domain-learning-coding/learning_socratic_dialogue_code_review.md` — Train reviewers conversationally.
- `domain-software-engineering/analysis/security/security_vulnerability_analysis.md` — Deeper security review.
- `domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md` — Complexity metrics behind the quality checks.
