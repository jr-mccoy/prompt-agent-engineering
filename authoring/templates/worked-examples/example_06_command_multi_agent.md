# Example 06: Command Orchestrating Multiple Agents

**Goal:** Demonstrate how a command coordinates multiple specialized agents for a complete workflow.

**Time Estimate:** 40 minutes

**Concepts Covered:**
- Multi-agent orchestration
- Agent selection by domain
- Context passing between agents
- Validation gates with agent handoffs

---

## Scenario

**Task:** Create a "Code Review Pipeline" command that orchestrates agents for:
1. Static analysis (code-reviewer)
2. Security review (security-auditor)
3. Documentation check (docs-architect)
4. Final synthesis (architect-review)

---

## Step 1: Map Agents to Phases

### Workflow Design

```
Code Submission
      │
      ▼
┌─────────────────┐
│ Static Analysis │ ← code-quality::code-reviewer
│ (Code patterns) │
└────────┬────────┘
         │ findings
         ▼
┌─────────────────┐
│ Security Review │ ← security-scanning::security-auditor
│ (Vulnerabilities)│
└────────┬────────┘
         │ security findings
         ▼
┌─────────────────┐
│ Documentation   │ ← documentation-generation::docs-architect
│ (Completeness)  │
└────────┬────────┘
         │ doc findings
         ▼
┌─────────────────┐
│ Final Synthesis │ ← comprehensive-review::architect-review
│ (Combined report)│
└────────┬────────┘
         │
         ▼
    Review Report
```

### Agent Selection Rationale

| Phase | Agent | Why This Agent |
|-------|-------|----------------|
| 1 | code-reviewer | Specializes in code patterns, complexity, maintainability |
| 2 | security-auditor | Deep security knowledge, OWASP expertise |
| 3 | docs-architect | Documentation standards and API documentation |
| 4 | architect-review | Synthesizes technical findings, provides architectural perspective |

**Pattern Applied:** OP-04 (Domain-Specific Agent Selection), AIP-02 (Composite Agent Paths)

---

## Step 2: Design Context Flow

### What Each Agent Receives and Produces

```
Agent 1 (code-reviewer)
  Input:  $ARGUMENTS (code to review)
  Output: Code quality findings, complexity metrics, pattern issues

Agent 2 (security-auditor)
  Input:  $ARGUMENTS + code quality findings
  Output: Security vulnerabilities, CVSS scores, remediation

Agent 3 (docs-architect)
  Input:  $ARGUMENTS + previous findings
  Output: Documentation gaps, API doc issues, completeness score

Agent 4 (architect-review)
  Input:  All previous outputs
  Output: Synthesized report, prioritized issues, recommendations
```

**Pattern Applied:** OP-03 (Context Passing Chain)

---

## Step 3: Build the Command

```markdown
# Code Review Pipeline

Orchestrate comprehensive code review using specialized agents for quality, security, documentation, and synthesis.

[Extended thinking: This workflow coordinates four specialized agents to deliver comprehensive code review. Each agent brings domain expertise: code patterns, security vulnerabilities, documentation quality, and architectural synthesis. Context flows sequentially, with each agent building on previous findings. The final synthesis agent resolves conflicts, eliminates duplicates, and produces a unified, prioritized review report.]

## Configuration

### Supported Flags
- `--quick`: Skip documentation review for faster results
- `--security-focus`: Prioritize security findings
- `--skip-synthesis`: Get individual reports without synthesis
- `--strict`: Block on any CRITICAL or HIGH findings

### Review Depth
- `quick`: Essential checks only (~5 min)
- `standard`: Balanced review (~15 min, default)
- `thorough`: Comprehensive review (~30 min)

---

## Phase 1: Static Analysis

### 1. Code Quality Review
- Use Task tool with subagent_type="code-quality::code-reviewer"
- Prompt: "Perform comprehensive code quality review on: $ARGUMENTS.

  Analyze the following aspects:
  1) Code complexity (cyclomatic, cognitive)
  2) SOLID principle adherence
  3) Design pattern usage and anti-patterns
  4) Error handling patterns
  5) Code duplication
  6) Naming conventions and readability
  7) Test coverage assessment

  For each finding:
  - Severity: CRITICAL, HIGH, MEDIUM, LOW
  - Location: File and line number
  - Description: What the issue is
  - Recommendation: How to fix

  Generate code quality report with metrics and findings."

- Expected output:
  - Code quality findings (severity-classified)
  - Complexity metrics
  - Pattern analysis
  - Improvement recommendations
- Context: Initial review, no prior context

---

### PHASE GATE: Quality → Security

Before security review:
- [ ] Code quality analysis complete
- [ ] Findings severity-classified
- [ ] Critical patterns identified for security context

---

## Phase 2: Security Review

### 2. Security Vulnerability Analysis
- Use Task tool with subagent_type="security-scanning::security-auditor"
- Prompt: "Perform security review on: $ARGUMENTS.

  Context from code quality review: Consider the code patterns and
  complexity identified, especially in authentication and data handling.

  Analyze for:
  1) OWASP Top 10 vulnerabilities
  2) Injection vulnerabilities (SQL, XSS, Command)
  3) Authentication/authorization issues
  4) Sensitive data exposure
  5) Security misconfiguration
  6) Dependency vulnerabilities
  7) Secrets/credential handling

  For each finding:
  - Severity with CVSS score
  - CWE/CVE reference if applicable
  - Proof of concept (conceptual)
  - Remediation steps

  Generate security report with prioritized findings."

- Expected output:
  - Security findings (CVSS-scored)
  - Vulnerability details with CWE/CVE
  - Remediation recommendations
  - Dependency audit results
- Context from previous: Code quality findings (especially complexity hotspots)

---

### PHASE GATE: Security → Documentation

Before documentation review:
- [ ] Security analysis complete
- [ ] Critical vulnerabilities flagged
- [ ] Remediation recommendations provided

**GATE**: If CRITICAL security issues and --strict flag, stop and report

---

## Phase 3: Documentation Review

### 3. Documentation Completeness Check
- Use Task tool with subagent_type="documentation-generation::docs-architect"
- Prompt: "Assess documentation quality and completeness for: $ARGUMENTS.

  Context from previous reviews: The code quality and security reviews
  have identified certain complex areas and security-sensitive functions
  that especially need documentation.

  Evaluate:
  1) API documentation completeness
  2) Code comments and inline documentation
  3) README and setup instructions
  4) Architecture documentation
  5) Security considerations documentation
  6) Change log and versioning
  7) Example usage and tutorials

  For each gap:
  - Priority: HIGH, MEDIUM, LOW
  - Location: Where documentation is needed
  - Suggestion: What should be documented

  Generate documentation assessment with completeness score."

- Expected output:
  - Documentation gaps (prioritized)
  - Completeness score (percentage)
  - Priority documentation needs
  - Template suggestions
- Context from previous: Quality findings (complex areas) + Security findings (sensitive areas)

---

## Phase 4: Synthesis and Final Report

### 4. Review Synthesis
- Use Task tool with subagent_type="comprehensive-review::architect-review"
- Prompt: "Synthesize all review findings for: $ARGUMENTS.

  You have received:
  - Code quality findings with complexity metrics
  - Security vulnerability analysis with CVSS scores
  - Documentation assessment with completeness score

  Your tasks:
  1) Merge all findings into unified list
  2) Remove duplicates and consolidate related issues
  3) Resolve any conflicting recommendations
  4) Create priority ranking considering:
     - Severity (CRITICAL > HIGH > MEDIUM > LOW)
     - Security impact
     - Effort to fix
     - Business risk
  5) Identify quick wins vs major refactoring
  6) Provide architectural recommendations

  Generate synthesis report with:
  - Executive summary
  - Top 10 priority issues
  - Complete findings by category
  - Recommended action plan
  - Metrics dashboard"

- Expected output:
  - Executive summary
  - Prioritized issue list
  - Unified findings
  - Action plan with effort estimates
  - Metrics summary
- Context from previous: All Phase 1-3 outputs

---

## Agent Coordination Summary

```
┌──────────────────────────────────────────────────────────────┐
│                    CODE REVIEW PIPELINE                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │ code-       │───▶│ security-   │───▶│ docs-       │      │
│  │ reviewer    │    │ auditor     │    │ architect   │      │
│  └─────────────┘    └─────────────┘    └─────────────┘      │
│        │                  │                  │               │
│        │ quality          │ security         │ docs          │
│        │ findings         │ findings         │ findings      │
│        │                  │                  │               │
│        └──────────────────┼──────────────────┘               │
│                           │                                  │
│                           ▼                                  │
│                  ┌─────────────┐                             │
│                  │ architect-  │                             │
│                  │ review      │                             │
│                  └─────────────┘                             │
│                           │                                  │
│                           ▼                                  │
│                   Final Report                               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## Success Criteria

- ✅ All four agents completed their analysis
- ✅ Context passed correctly between agents
- ✅ No blocking issues in phase gates (or properly flagged)
- ✅ Synthesis resolved duplicates
- ✅ Final report includes all categories

---

## Error Handling

### If Code Quality Review Fails
- Retry with smaller scope
- Fall back to basic static analysis
- Document gap for security agent

### If Security Review Fails
- Continue with quality + docs
- Flag security gap prominently
- Recommend dedicated security audit

### If Documentation Review Fails
- Continue to synthesis
- Omit documentation section from report
- Note incomplete review

### If Synthesis Fails
- Generate individual reports from each agent
- Provide manual consolidation guidance

---

## Key Orchestration Patterns Demonstrated

### 1. Domain-Specific Agent Selection (OP-04)

Each phase uses the most qualified agent:
```markdown
subagent_type="code-quality::code-reviewer"      # Quality expertise
subagent_type="security-scanning::security-auditor"  # Security expertise
subagent_type="documentation-generation::docs-architect"  # Docs expertise
subagent_type="comprehensive-review::architect-review"  # Synthesis expertise
```

### 2. Context Passing Chain (OP-03)

Each agent receives relevant context:
```markdown
# Security receives quality context
"Context from code quality review: Consider the code patterns and
complexity identified, especially in authentication..."

# Docs receives both quality and security context
"Context from previous reviews: The code quality and security reviews
have identified certain complex areas..."

# Synthesis receives everything
"You have received:
- Code quality findings with complexity metrics
- Security vulnerability analysis with CVSS scores
- Documentation assessment with completeness score"
```

### 3. Phase Gate Validation (VP-01)

Gates between each agent handoff:
```markdown
### PHASE GATE: Security → Documentation
- [ ] Security analysis complete
- [ ] Critical vulnerabilities flagged
**GATE**: If CRITICAL security issues and --strict flag, stop
```

---

Target: $ARGUMENTS
```

---

## Key Takeaways

1. **Select agents by expertise** - Each domain gets its specialist
2. **Chain context explicitly** - Tell each agent what it receives
3. **Gate between handoffs** - Validate before passing to next agent
4. **Synthesize at the end** - Final agent integrates all findings
5. **Handle partial failure** - Each agent failure has fallback

---

## Files Referenced

- **Command Pattern Reference:** [COMMAND_PATTERN_INDEX.md](../../command-patterns/COMMAND_PATTERN_INDEX.md)
- **Agent Directory:** ../../agents/
- **Command Templates:** [../command-templates/](../command-templates/)
