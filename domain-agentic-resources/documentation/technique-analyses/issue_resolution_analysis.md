# Technique Analysis: issue (GitHub Issue Resolution)

**Resource Type:** Command
**Path:** claude-code-resources/commands/orchestration/issue.md
**Date Analyzed:** 2025-12-22

---

## Identified Techniques

### Technique 1: Systematic Investigation Framework
- **Category:** DT (Decomposition) + DS (Domain-Specific)
- **Pattern:** Multi-stage investigation (Triage → Root Cause → Planning → Implementation → Testing → Deployment)
- **Example:** "Issue Analysis and Triage" → "Investigation and Root Cause Analysis" → "Implementation Planning" with specific steps for each
- **Maps to existing:** DT-01 (Hierarchical Task Breakdown)
- **Effectiveness:** Prevents jumping to solutions before understanding the problem

### Technique 2: Tool Integration with Explicit Commands
- **Category:** DS (Domain-Specific) + OT (Output)
- **Pattern:** Embedded bash/CLI commands showing exact tool usage
- **Example:**
```bash
gh issue view $ISSUE_NUMBER --comments
git bisect start && git bisect bad HEAD
rg "functionName" --type js -A 3 -B 3
```
- **Maps to existing:** DS-03 (Tool and Methodology Suggestions) but more specific with actual commands
- **Effectiveness:** Actionable immediately, no translation needed

### Technique 3: Priority Classification Framework
- **Category:** DS (Domain-Specific)
- **Pattern:** Explicit 4-tier priority system (P0-P3) with criteria
- **Example:** "P0/Critical: Production breaking... P1/High: Major feature broken... P2/Medium: Workaround available..."
- **Maps to existing:** DS-06 (Prioritization and Severity Guidance)
- **Effectiveness:** Ensures appropriate response time and resource allocation

### Technique 4: Code Archaeology Techniques
- **Category:** NEW (Investigation methodology)
- **Pattern:** Systematic historical analysis using git bisect, blame, and log
- **Example:**
```bash
git bisect run ./test_issue.sh
git blame -L <start>,<end> path/to/file.js
```
- **Maps to existing:** NEW - specific tooling for understanding code history
- **Effectiveness:** Quickly identifies when and why issues were introduced

### Technique 5: Test-Driven Bug Fixing
- **Category:** DS (Domain-Specific)
- **Pattern:** Write failing test first, then implement fix, following TDD principles
- **Example:** "Create failing test cases" in Phase 1, then implement fix in subsequent phases
- **Maps to existing:** DS-02 (Metric Specification) applied to testing
- **Effectiveness:** Prevents regressions and validates fix

### Technique 6: Incremental Commit Strategy
- **Category:** DS (Domain-Specific) + OT (Output)
- **Pattern:** Explicit guidance on atomic commits with conventional commit messages
- **Example:**
```bash
git add -p  # Partial staging
git commit -m "feat(auth): add user validation schema (#123)"
git commit -m "test(auth): add unit tests for validation (#123)"
```
- **Maps to existing:** OC-01 (Output Format Templates) for git commits
- **Effectiveness:** Creates clear project history and enables easy rollback

### Technique 7: Comprehensive PR Template
- **Category:** OT (Output) + QA (Quality Assurance)
- **Pattern:** Detailed PR creation with all required sections via gh CLI
- **Example:**
```markdown
## Summary, ## Changes Made, ## Testing, ## Performance Impact, ## Screenshots, ## Checklist
```
- **Maps to existing:** OC-01 (Output Format Templates) + QA-01 (Chain-of-Verification via checklist)
- **Effectiveness:** Ensures reviewers have all context needed

### Technique 8: Multi-Test-Layer Strategy
- **Category:** DS (Domain-Specific)
- **Pattern:** Unit → Integration → E2E test pyramid with examples for each
- **Example:** Jest unit tests, Pytest integration tests, Playwright E2E tests all provided
- **Maps to existing:** DS-02 (Metric Specification) applied to test coverage
- **Effectiveness:** Comprehensive validation at appropriate levels

---

## Novel Patterns (Not in MASTER_TECHNIQUE_INDEX)

### Pattern 1: Code Archaeology as Investigation Technique
- **Description:** Systematic use of version control tools (bisect, blame, log) to understand problem origins
- **Implementation:** Dedicated "Code Archaeology" section with bisect automation and blame analysis
- **Use case:** Debugging issues with unclear origins or suspected regressions
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-15

### Pattern 2: Issue-to-PR Complete Lifecycle
- **Description:** End-to-end workflow from issue analysis through deployment verification and closure
- **Implementation:** 8-stage process covering full development lifecycle with explicit outputs at each stage
- **Use case:** Systematic issue resolution in team environments with full traceability
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-16

### Pattern 3: Embedded Tool Integration Patterns
- **Description:** Providing exact CLI commands and API usage patterns within workflow steps
- **Implementation:** Bash/Python/TypeScript code blocks showing exact tool invocation
- **Use case:** Workflows requiring specific tool usage with zero ambiguity
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-17

### Pattern 4: Branch Naming Convention Enforcement
- **Description:** Explicit branch naming patterns tied to issue types
- **Implementation:**
```bash
feature/issue-${ISSUE_NUMBER}-short-description
fix/issue-${ISSUE_NUMBER}-component-bug
hotfix/issue-${ISSUE_NUMBER}-critical-fix
```
- **Use case:** Team standardization and automated tooling integration
- **Proposed category:** DS (Domain-Specific)
- **Proposed code:** DS-18

---

## Multi-Technique Combinations

**Technique Stack:** Investigation Framework + Code Archaeology + TDD + Tool Integration + Incremental Commits + PR Template + Multi-Layer Testing

**Combination Purpose:** Create systematic, traceable, high-quality issue resolution workflow

**Synergies:**
- Code archaeology + TDD = Understand history, prevent future issues
- Tool integration + incremental commits = Clear development trail
- PR template + multi-layer testing = Comprehensive quality validation
- Priority framework + investigation = Appropriate effort allocation

---

## Notes for Integration

**Add to MASTER_TECHNIQUE_INDEX:**
- DS-15: Code Archaeology as Investigation Technique
- DS-16: Issue-to-PR Complete Lifecycle
- DS-17: Embedded Tool Integration Patterns
- DS-18: Branch Naming Convention Enforcement

**Cross-reference with prompts:**
- Related to: `engineering/engineering_prompt_for_debugging_code.md`
- Related to: `testing/testing_*.md` (all testing prompts)
- Complements: `engineering/engineering_post_mortem_root_cause_ladder.md`

**Best practices:**
- Always investigate before implementing
- Use version control as investigation tool
- Write tests before fixes
- Follow conventional commits for clarity
- Provide comprehensive PR context

---

## Analysis Metadata

**Analyzer:** Claude (Task 2.2 implementation)
**Analysis Duration:** 15 minutes
**Confidence Level:** High
**Review Status:** Draft
**Priority for Integration:** High - Comprehensive development workflow patterns
