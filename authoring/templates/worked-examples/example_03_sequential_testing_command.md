# Example 03: Creating a Sequential Testing Command

**Goal:** Create a command that runs a sequential testing pipeline: analyze → write tests → run tests → report.

**Time Estimate:** 30 minutes

**Final Quality Score:** 82/100

---

## Step 1: Design Workflow

**Question:** What is the step-by-step flow?

### Workflow Analysis

```
Input Code → Analyze Coverage → Write Tests → Execute Tests → Generate Report
     ↓              ↓                ↓              ↓              ↓
  $ARGUMENTS    Coverage Map     Test Files    Test Results    Final Report
```

### Dependencies

Each step depends on the previous:
- Test writing needs coverage analysis
- Test execution needs written tests
- Report needs execution results

**Pattern Applied:** OP-01 (Multi-Phase Sequential), OP-03 (Context Passing Chain)

---

## Step 2: Select Agents

**Question:** Which agents handle each step?

| Step | Task | Agent |
|------|------|-------|
| 1 | Coverage Analysis | `code-quality::code-reviewer` |
| 2 | Test Generation | `unit-testing::test-automator` |
| 3 | Test Execution | `unit-testing::test-automator` |
| 4 | Report Generation | `documentation-generation::docs-architect` |

**Pattern Applied:** OP-04 (Domain-Specific Agent Selection), AIP-02 (Composite Agent Paths)

---

## Step 3: Add Validation Gates

**Question:** What must be validated between steps?

### Gate Analysis

| After Step | Validation Required |
|------------|---------------------|
| 1 | Coverage report generated, target files identified |
| 2 | Tests compile, follow naming conventions |
| 3 | All tests pass OR failures categorized |
| 4 | Report complete with all sections |

**Pattern Applied:** VP-01 (Phase Gate Validation), VP-03 (Threshold-Based Validation)

---

## Step 4: Build Command File

Here's the complete sequential testing command:

```markdown
# Test Coverage Pipeline

Execute a sequential testing pipeline that analyzes code, generates tests, executes them, and produces a coverage report.

[Extended thinking: This workflow implements a sequential testing pipeline where each step builds on the previous step's output. The analysis phase identifies coverage gaps, which drives targeted test generation. Tests are then executed and validated before producing a final report. Each step validates its output before proceeding, ensuring quality at every stage.]

## Configuration

### Thresholds
- Minimum line coverage: 80%
- Minimum branch coverage: 75%
- Maximum test execution time: 300s

### Supported Flags
- `--dry-run`: Analyze only, don't generate tests
- `--skip-execution`: Generate tests but don't run them
- `--verbose`: Enable detailed logging
- `--strict`: Fail on any test failure

---

## Step 1: Coverage Analysis

### Input
- Primary: $ARGUMENTS (path to code to analyze)
- Prerequisites: Valid source code directory

### Execution
- Use Task tool with subagent_type="code-quality::code-reviewer"
- Prompt: "Analyze test coverage for code at: $ARGUMENTS.

  Perform comprehensive analysis:
  1) Identify all testable functions/methods/classes
  2) Detect existing test coverage
  3) Find untested code paths and branches
  4) Prioritize testing needs by complexity and criticality
  5) Map dependencies for test isolation requirements

  Generate coverage analysis report with:
  - List of all testable units
  - Current coverage percentage
  - Prioritized list of coverage gaps
  - Dependency graph for test planning"

### Output
- Coverage Analysis Report
- Prioritized testing targets
- Dependency map

### Validation
- [ ] All source files analyzed
- [ ] Coverage metrics calculated
- [ ] Testing targets identified and prioritized

---

## Step 2: Test Generation

### Input
- From Step 1: Coverage analysis, prioritized targets, dependency map

### Execution
- Use Task tool with subagent_type="unit-testing::test-automator"
- Prompt: "Generate comprehensive tests for: $ARGUMENTS.

  Using the coverage analysis:
  1) Create tests for each prioritized target
  2) Include edge cases and boundary conditions
  3) Test error handling paths
  4) Add integration points where needed
  5) Follow project's existing test patterns

  For each test:
  - Clear, descriptive test names
  - Arrange-Act-Assert pattern
  - Appropriate mocking/stubbing
  - Comments explaining test purpose

  Target coverage: 80% line, 75% branch."

### Output
- Generated test files
- Test manifest listing all new tests
- Mocking requirements documentation

### Validation
- [ ] Tests follow naming conventions
- [ ] Tests compile without errors
- [ ] All priority targets covered
- [ ] Mocks properly isolated

---

### VALIDATION GATE: Generation → Execution

Before running tests:
- [ ] All generated tests compile
- [ ] Test framework dependencies resolved
- [ ] Test configuration valid
- [ ] No syntax errors in test files

**GATE**: Do not execute if tests fail to compile

---

## Step 3: Test Execution

### Input
- From Step 1: Target code paths
- From Step 2: Generated test files

### Execution
- Use Task tool with subagent_type="unit-testing::test-automator"
- Prompt: "Execute generated tests for: $ARGUMENTS.

  Execution requirements:
  1) Run all new tests with coverage tracking
  2) Capture detailed results for each test
  3) Record execution time per test
  4) Collect coverage metrics
  5) Identify any flaky tests

  For failures:
  - Capture full error message and stack trace
  - Identify root cause if possible
  - Suggest fix or flag for manual review

  Generate execution report with pass/fail counts."

### Output
- Test execution results
- Coverage metrics (line, branch, function)
- Failure analysis (if any)
- Performance metrics

### Validation
- [ ] All tests executed
- [ ] Coverage metrics collected
- [ ] Failures documented with details
- **GATE**: If --strict, block on any failure

---

## Step 4: Report Generation

### Input
- From Step 1: Initial coverage analysis
- From Step 2: Test manifest
- From Step 3: Execution results

### Execution
- Use Task tool with subagent_type="documentation-generation::docs-architect"
- Prompt: "Generate comprehensive test report for: $ARGUMENTS.

  Include:
  1) Executive summary with key metrics
  2) Coverage comparison (before vs after)
  3) Test inventory with status
  4) Failure analysis with recommendations
  5) Coverage gap analysis (remaining gaps)
  6) Recommendations for further improvement

  Format as markdown with clear sections and tables."

### Output
- Comprehensive test report (markdown)
- Coverage trend data
- Actionable recommendations

### Validation
- [ ] All sections complete
- [ ] Metrics accurately reported
- [ ] Recommendations actionable

---

## Context Flow

```
Step 1 ──────────────────→ Step 2 ──────────────→ Step 3 ──────────────→ Step 4
Coverage Analysis          Test Generation        Test Execution          Report
       │                         │                      │                    │
       └─→ targets, deps         └─→ test files         └─→ results          └─→ final report
```

### Context Accumulation

| Step | Input | Output | Passes Forward |
|------|-------|--------|----------------|
| 1 | $ARGUMENTS | Coverage analysis | Analysis, targets, deps |
| 2 | Analysis | Test files | Tests + previous |
| 3 | Tests + code | Results | Results + previous |
| 4 | All previous | Report | — |

---

## Success Criteria

- ✅ Coverage analysis completed for all targets
- ✅ Tests generated for prioritized coverage gaps
- ✅ All tests execute (pass or documented failures)
- ✅ Coverage meets threshold (80% line, 75% branch)
- ✅ Final report generated with all sections
- ✅ No unvalidated gates skipped

---

## Failure Recovery

### If Coverage Analysis Fails
1. Verify source code path is valid
2. Check for supported languages
3. Retry with verbose logging
4. Fall back to manual file list if needed

### If Test Generation Fails
1. Review coverage analysis for issues
2. Check test framework compatibility
3. Generate tests in smaller batches
4. Flag complex targets for manual writing

### If Test Execution Fails
1. Capture detailed error output
2. Separate passing from failing tests
3. Re-run flaky tests individually
4. Generate partial report if needed

### If Report Generation Fails
1. Verify all input data available
2. Generate sections individually
3. Create minimal report with core metrics

---

Target: $ARGUMENTS
```

---

## Step 5: Validate Quality

### Quality Rubric Assessment

| Category | Score | Notes |
|----------|-------|-------|
| **Workflow Structure** | 16/20 | Clear sequential flow with context passing |
| **Agent Configuration** | 16/20 | Good agent selection, detailed prompts |
| **Validation & Gates** | 12/15 | Good gates, could add more thresholds |
| **Error Handling** | 11/15 | Recovery defined for each step |
| **Documentation** | 13/15 | Clear flow documentation |
| **Configuration** | 8/10 | Good flags and thresholds |
| **Bonus** | 6/5 | Practical, reusable design |
| **TOTAL** | **82/100** | Strong standard tier |

### Pattern Verification

| Pattern | Applied | Evidence |
|---------|---------|----------|
| OP-01 | ✅ | 4 sequential steps |
| OP-03 | ✅ | Each step receives previous output |
| WP-01 | ✅ | Extended thinking block |
| WP-03 | ✅ | Success criteria section |
| AIP-01 | ✅ | Task tool invocation format |
| AIP-02 | ✅ | Composite agent paths |
| AIP-03 | ✅ | Detailed prompts with numbered items |
| AIP-04 | ✅ | Expected output specified |
| VP-01 | ✅ | Validation gate between 2→3 |
| VP-03 | ✅ | Coverage thresholds |
| EHP-02 | ✅ | Failure recovery for each step |
| CP-01 | ✅ | Supported flags |
| CP-03 | ✅ | Threshold configuration |

---

## Key Takeaways

1. **Map dependencies first** - Sequential requires clear input/output flow
2. **Explicit context passing** - Each step states what it receives
3. **Gates between critical transitions** - Compile check before execution
4. **Recovery at each step** - Failures are isolated and recoverable
5. **Accumulated context** - Later steps have access to all previous outputs

---

## Files Referenced

- **Template Used:** [sequential_workflow_template.md](../command-templates/sequential_workflow_template.md)
- **Pattern Reference:** [COMMAND_PATTERN_INDEX.md](../../command-patterns/COMMAND_PATTERN_INDEX.md)
- **Quality Rubric:** [COMMAND_QUALITY_RUBRIC.md](../../command-patterns/COMMAND_QUALITY_RUBRIC.md)
