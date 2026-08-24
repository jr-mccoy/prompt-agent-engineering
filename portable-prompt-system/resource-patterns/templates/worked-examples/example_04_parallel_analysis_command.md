# Example 04: Creating a Parallel Analysis Command

**Goal:** Create a command that runs multiple independent code analyses in parallel for efficiency.

**Time Estimate:** 35 minutes

**Final Quality Score:** 85/100

---

## Step 1: Design Workflow

**Question:** What analyses can run independently?

### Parallel Analysis Opportunities

| Analysis Type | Dependencies | Can Parallelize? |
|---------------|--------------|------------------|
| Security Scan | Source code only | ✅ Yes |
| Performance Analysis | Source code only | ✅ Yes |
| Code Quality | Source code only | ✅ Yes |
| Accessibility Audit | Source code only | ✅ Yes |

All four analyses only need the source code - they can run simultaneously.

### Workflow Structure

```
Preparation → [Security | Performance | Quality | Accessibility] → Integration → Report
```

**Pattern Applied:** OP-02 (Parallel Agent Execution), OP-05 (Milestone Convergence)

---

## Step 2: Select Agents

**Question:** Which agents handle each parallel task?

| Task | Agent | Rationale |
|------|-------|-----------|
| Preparation | `code-quality::code-reviewer` | Analyze structure |
| Security | `security-scanning::security-auditor` | Security expertise |
| Performance | `application-performance::performance-engineer` | Performance focus |
| Quality | `code-quality::code-reviewer` | Quality patterns |
| Accessibility | `frontend-mobile-development::frontend-developer` | A11y knowledge |
| Integration | `comprehensive-review::architect-review` | Synthesize findings |

**Pattern Applied:** OP-04 (Domain-Specific Agent Selection), AIP-05 (Conditional Agent Selection)

---

## Step 3: Design Convergence

**Question:** How do parallel results merge?

### Convergence Requirements

All parallel tasks must:
- Complete (success or partial)
- Produce standardized output format
- Include severity classification

**Pattern Applied:** OP-05 (Milestone Convergence), VP-02 (Severity-Based Classification)

---

## Step 4: Build Command File

Here's the complete parallel analysis command:

```markdown
# Comprehensive Code Analysis

Execute multiple independent code analyses in parallel for maximum efficiency, then synthesize findings into a unified report.

[Extended thinking: This workflow maximizes efficiency by running four independent analysis types simultaneously. Security, performance, quality, and accessibility analyses each operate on the source code without dependencies on each other. After all parallel tasks complete, an integration phase synthesizes findings, resolves conflicts, and produces a unified prioritized report. This achieves 4x speedup compared to sequential execution while maintaining comprehensive coverage.]

## Configuration

### Supported Flags
- `--skip-{analysis}`: Skip specific analysis (security, performance, quality, accessibility)
- `--fail-fast`: Abort all if any analysis fails
- `--parallel-limit=N`: Maximum concurrent analyses (default: 4)
- `--severity-threshold={level}`: Minimum severity to report (LOW, MEDIUM, HIGH, CRITICAL)

### Severity Classification
- **CRITICAL**: Must fix immediately, blocks deployment
- **HIGH**: Fix before next release
- **MEDIUM**: Fix within sprint
- **LOW**: Track for future improvement

---

## Phase 1: Preparation

### 1. Codebase Analysis
- Use Task tool with subagent_type="code-quality::code-reviewer"
- Prompt: "Analyze codebase structure at: $ARGUMENTS.

  Generate:
  1) File inventory by type (frontend, backend, config)
  2) Technology stack identification
  3) Entry points and critical paths
  4) Shared context for parallel analyses

  This context will be provided to all parallel analysis tasks."

- Expected output:
  - Codebase structure map
  - Technology stack summary
  - Critical path identification
  - Shared analysis context

---

### PHASE GATE: Preparation → Parallel Execution

- [ ] All source files cataloged
- [ ] Technology stack identified
- [ ] Critical paths mapped
- [ ] Shared context prepared

**GATE**: Parallel tasks require shared context to operate

---

## Phase 2: Parallel Execution

### ⚡ PARALLEL EXECUTION BLOCK

The following analyses execute simultaneously:

---

### 2a. Security Analysis
- Use Task tool with subagent_type="security-scanning::security-auditor"
- Prompt: "Perform security analysis on: $ARGUMENTS.

  Using shared context, analyze:
  1) OWASP Top 10 vulnerabilities
  2) Dependency vulnerabilities (CVEs)
  3) Secret/credential exposure
  4) Authentication/authorization issues
  5) Input validation problems
  6) Injection vulnerabilities

  Classify findings by severity (CRITICAL/HIGH/MEDIUM/LOW).
  Include CVE references where applicable."

- Expected output:
  - Security findings with severity
  - CVE references
  - Remediation recommendations
- Context from Phase 1: Shared analysis context

---

### 2b. Performance Analysis
- Use Task tool with subagent_type="application-performance::performance-engineer"
- Prompt: "Perform performance analysis on: $ARGUMENTS.

  Using shared context, analyze:
  1) Algorithm complexity issues (O(n²), etc.)
  2) Memory leak potential
  3) Database query efficiency (N+1, missing indexes)
  4) API response time concerns
  5) Resource utilization patterns
  6) Caching opportunities

  Classify findings by severity based on impact.
  Estimate performance improvement potential."

- Expected output:
  - Performance findings with severity
  - Estimated impact metrics
  - Optimization recommendations
- Context from Phase 1: Shared analysis context

---

### 2c. Code Quality Analysis
- Use Task tool with subagent_type="code-quality::code-reviewer"
- Prompt: "Perform code quality analysis on: $ARGUMENTS.

  Using shared context, analyze:
  1) Code complexity (cyclomatic, cognitive)
  2) Duplication and DRY violations
  3) SOLID principle adherence
  4) Design pattern usage and anti-patterns
  5) Test coverage gaps
  6) Documentation completeness

  Classify findings by severity based on maintainability impact.
  Reference specific code locations."

- Expected output:
  - Quality findings with severity
  - Complexity metrics
  - Refactoring recommendations
- Context from Phase 1: Shared analysis context

---

### 2d. Accessibility Analysis
- Use Task tool with subagent_type="frontend-mobile-development::frontend-developer"
- Prompt: "Perform accessibility analysis on: $ARGUMENTS.

  Using shared context, analyze:
  1) WCAG 2.1 AA compliance
  2) Keyboard navigation support
  3) Screen reader compatibility
  4) Color contrast issues
  5) Form accessibility
  6) ARIA usage correctness

  Classify findings by severity based on user impact.
  Reference WCAG success criteria."

- Expected output:
  - Accessibility findings with severity
  - WCAG criteria references
  - Remediation recommendations
- Context from Phase 1: Shared analysis context

---

### ⏳ CONVERGENCE CHECKPOINT

All parallel tasks must complete before Phase 3:

| Task | Status | Findings |
|------|--------|----------|
| 2a. Security | ⬜ | {count} |
| 2b. Performance | ⬜ | {count} |
| 2c. Quality | ⬜ | {count} |
| 2d. Accessibility | ⬜ | {count} |

**Wait for all tasks** before proceeding.

### Partial Completion Handling

If some analyses fail:
- Document which analyses completed
- Generate partial report noting gaps
- Recommend re-running failed analyses

---

## Phase 3: Integration

### 3. Finding Synthesis
- Use Task tool with subagent_type="comprehensive-review::architect-review"
- Prompt: "Synthesize findings from all analyses for: $ARGUMENTS.

  Integration tasks:
  1) Merge findings from all analyses
  2) Deduplicate overlapping issues
  3) Identify cross-domain relationships
  4) Create unified priority ranking
  5) Resolve any conflicting recommendations
  6) Calculate aggregate metrics

  Generate synthesis report with:
  - Total findings by severity
  - Cross-domain issue clusters
  - Priority-ordered remediation list"

- Expected output:
  - Unified findings list
  - Cross-domain analysis
  - Priority matrix
- Context from Phase 2: All analysis outputs

---

## Phase 4: Report Generation

### 4. Final Report
- Use Task tool with subagent_type="documentation-generation::docs-architect"
- Prompt: "Generate comprehensive analysis report for: $ARGUMENTS.

  Include:
  1) Executive summary with key metrics
  2) Findings by category and severity
  3) Top 10 priority issues
  4) Remediation roadmap
  5) Metrics dashboard
  6) Appendix with full details

  Format for stakeholder presentation."

- Expected output:
  - Executive report (markdown)
  - Detailed findings appendix
  - Remediation roadmap
- Context from Phase 3: Synthesized findings

---

## Success Criteria

### Parallel Execution
- ✅ All 4 analyses completed (or documented partial completion)
- ✅ No resource conflicts between analyses
- ✅ Consistent severity classification

### Integration
- ✅ Findings successfully merged
- ✅ Duplicates removed
- ✅ Cross-domain issues identified

### Final Report
- ✅ Executive summary generated
- ✅ Priority roadmap created
- ✅ All findings documented

---

## Error Handling

### Graceful Degradation

| Failed Analysis | Impact | Fallback |
|-----------------|--------|----------|
| Security | HIGH | Flag gap, recommend manual audit |
| Performance | MEDIUM | Generate report without perf data |
| Quality | MEDIUM | Generate report without quality data |
| Accessibility | LOW | Generate report without a11y data |

### If Integration Fails
1. Generate separate reports per analysis
2. Document integration failure
3. Recommend manual synthesis

---

## Coordination Notes

### Parallel Execution Rules
- All analyses receive same shared context from Phase 1
- Analyses do NOT depend on each other's output
- Each has independent timeout (default: 5 minutes)
- Failures are isolated unless --fail-fast

### Resource Management
- Limit to 4 concurrent agents by default
- Each analysis approximately equal duration
- Monitor for rate limiting

---

## Parallel Task Matrix

| Task | Agent | Est. Time | Can Fail? | Priority |
|------|-------|-----------|-----------|----------|
| Security | security-auditor | 2 min | No | HIGH |
| Performance | performance-engineer | 3 min | Yes | MEDIUM |
| Quality | code-reviewer | 2 min | Yes | MEDIUM |
| Accessibility | frontend-developer | 2 min | Yes | LOW |

---

Target: $ARGUMENTS
```

---

## Step 5: Validate Quality

### Quality Rubric Assessment

| Category | Score | Notes |
|----------|-------|-------|
| **Workflow Structure** | 17/20 | Clear parallel + convergence structure |
| **Agent Configuration** | 17/20 | Domain-appropriate agents, good prompts |
| **Validation & Gates** | 12/15 | Convergence checkpoint, severity classification |
| **Error Handling** | 13/15 | Graceful degradation table |
| **Documentation** | 14/15 | Clear parallel execution block |
| **Configuration** | 8/10 | Good flags and options |
| **Bonus** | 4/5 | Efficient parallel design |
| **TOTAL** | **85/100** | Strong standard tier |

### Pattern Verification

| Pattern | Applied | Evidence |
|---------|---------|----------|
| OP-01 | ✅ | 4 phases |
| OP-02 | ✅ | Parallel execution block (2a-2d) |
| OP-05 | ✅ | Convergence checkpoint |
| WP-01 | ✅ | Extended thinking |
| WP-03 | ✅ | Success criteria |
| AIP-01 | ✅ | Task tool format |
| AIP-02 | ✅ | Composite paths |
| AIP-05 | ✅ | Multiple agent types |
| VP-02 | ✅ | Severity classification |
| EHP-03 | ✅ | Graceful degradation |
| CP-01 | ✅ | Flags |

---

## Key Takeaways

1. **Identify true independence** - All analyses only need source code
2. **Prepare shared context** - Phase 1 creates context for all parallel tasks
3. **Clear convergence point** - All must complete before integration
4. **Handle partial failure** - Graceful degradation per component
5. **Estimate timing** - Parallel time = slowest task, not sum

---

## Files Referenced

- **Template Used:** [parallel_execution_template.md](../command-templates/parallel_execution_template.md)
- **Pattern Reference:** [COMMAND_PATTERN_INDEX.md](../../command-patterns/COMMAND_PATTERN_INDEX.md)
- **Quality Rubric:** [COMMAND_QUALITY_RUBRIC.md](../../command-patterns/COMMAND_QUALITY_RUBRIC.md)
