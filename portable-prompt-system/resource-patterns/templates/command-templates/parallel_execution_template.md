# Parallel Execution Command Template

**Purpose:** Template for creating commands that execute multiple independent tasks simultaneously for maximum efficiency.

**Best For:**
- Multi-component implementations (backend/frontend/database)
- Cross-platform development (web/mobile/desktop)
- Parallel analysis (security/performance/quality)
- Batch processing operations
- Independent module development

**Quality Target:** 75-90/100 (Standard tier)

---

## Template Structure

Copy the structure below and replace placeholders (`{...}`) with your workflow-specific content.

---

```markdown
# {Command Name}

{One-line description emphasizing parallel execution and efficiency.}

<!--
PATTERNS APPLIED:
- OP-01: Multi-Phase Sequential (for phases)
- OP-02: Parallel Agent Execution
- OP-05: Milestone Convergence
- WP-01: Extended Thinking Introduction
- WP-03: Success Criteria Definition
- AIP-01: Task Tool Invocation
- AIP-02: Composite Agent Paths
- AIP-05: Conditional Agent Selection
- VP-01: Phase Gate Validation
- EHP-03: Graceful Degradation
- CP-01: Flag-Based Configuration
-->

[Extended thinking: This workflow maximizes efficiency by executing {N}
independent {task type} tasks in parallel. The approach divides work among
specialized agents, each handling their domain simultaneously. After parallel
execution completes, a convergence phase integrates all outputs and validates
the combined result. This achieves {time savings} while maintaining {quality}.]

## Configuration

### Supported Flags
- `--sequential`: Force sequential execution (debugging)
- `--skip-{component}`: Skip specific parallel component
- `--timeout={seconds}`: Set parallel task timeout
- `--fail-fast`: Abort all if any parallel task fails

### Parameters
- `parallel_limit`: Maximum concurrent tasks
  - Default: 3
- `convergence_timeout`: Seconds to wait for all tasks
  - Default: 300

---

## Phase 1: Preparation

### 1. {Preparation Step}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "Analyze and prepare for parallel execution on: $ARGUMENTS.

  Generate:
  1) {Shared context/specification}
  2) {Component breakdown}
  3) {Interface contracts between components}

  Ensure all parallel tasks can execute independently."

- Expected output:
  - {Shared specification}
  - {Task breakdown}
  - {Interface definitions}
- Context: Initial phase, establishes shared context for parallel tasks

---

### PHASE GATE: Preparation → Parallel Execution

Before parallel execution:
- [ ] Shared context defined
- [ ] All component interfaces specified
- [ ] No dependencies between parallel tasks
- [ ] Each parallel task can execute independently

**GATE**: Parallel tasks must be truly independent

---

## Phase 2: Parallel Execution

### ⚡ PARALLEL EXECUTION BLOCK

The following tasks execute simultaneously. Each task:
- Receives the same shared context from Phase 1
- Operates independently
- Produces its own deliverable
- Can complete in any order

---

### 2a. {Parallel Task A}
- Use Task tool with subagent_type="{category-a}::{specialist-a}"
- Prompt: "Using shared context, {implement/analyze/create} {component A} for: $ARGUMENTS.

  {Detailed instructions for Component A:}
  1) {Task A specific instruction 1}
  2) {Task A specific instruction 2}
  3) {Task A specific instruction 3}

  Ensure compatibility with defined interfaces."

- Expected output:
  - {Component A deliverable}
  - {Component A documentation}
- Context from Phase 1: {Shared specification}

---

### 2b. {Parallel Task B}
- Use Task tool with subagent_type="{category-b}::{specialist-b}"
- Prompt: "Using shared context, {implement/analyze/create} {component B} for: $ARGUMENTS.

  {Detailed instructions for Component B:}
  1) {Task B specific instruction 1}
  2) {Task B specific instruction 2}
  3) {Task B specific instruction 3}

  Ensure compatibility with defined interfaces."

- Expected output:
  - {Component B deliverable}
  - {Component B documentation}
- Context from Phase 1: {Shared specification}

---

### 2c. {Parallel Task C}
- Use Task tool with subagent_type="{category-c}::{specialist-c}"
- Prompt: "Using shared context, {implement/analyze/create} {component C} for: $ARGUMENTS.

  {Detailed instructions for Component C:}
  1) {Task C specific instruction 1}
  2) {Task C specific instruction 2}
  3) {Task C specific instruction 3}

  Ensure compatibility with defined interfaces."

- Expected output:
  - {Component C deliverable}
  - {Component C documentation}
- Context from Phase 1: {Shared specification}

---

### 2d. {Parallel Task D} (Optional)
- Use Task tool with subagent_type="{category-d}::{specialist-d}"
- Prompt: "{Optional fourth parallel task}..."

- Expected output: {Component D deliverable}
- Context from Phase 1: {Shared specification}

---

### ⏳ CONVERGENCE CHECKPOINT

All parallel tasks must complete before Phase 3:

| Task | Status | Deliverable |
|------|--------|-------------|
| 2a. {Task A} | ⬜ Pending | {Deliverable A} |
| 2b. {Task B} | ⬜ Pending | {Deliverable B} |
| 2c. {Task C} | ⬜ Pending | {Deliverable C} |
| 2d. {Task D} | ⬜ Pending | {Deliverable D} |

**Wait for all tasks** OR **proceed with partial results** if --partial-ok flag set.

### Partial Completion Handling

If some parallel tasks fail:
- Document which tasks completed
- Identify dependencies of failed tasks
- Assess if integration can proceed
- Flag gaps in final deliverable

---

## Phase 3: Integration

### 3. {Integration Step}
- Use Task tool with subagent_type="{integration-specialist}"
- Prompt: "Integrate outputs from all parallel tasks for: $ARGUMENTS.

  Received components:
  - Component A: {status}
  - Component B: {status}
  - Component C: {status}
  - Component D: {status}

  Integration tasks:
  1) Verify interface compatibility
  2) Connect components
  3) Resolve any conflicts
  4) Validate integrated system

  Generate integrated {deliverable}."

- Expected output:
  - {Integrated deliverable}
  - {Integration report}
- Context from Phase 2: All parallel task outputs

---

## Phase 4: Validation

### 4. {Validation Step}
- Use Task tool with subagent_type="{validator}"
- Prompt: "Validate integrated system for: $ARGUMENTS.

  Verify:
  1) All components function correctly
  2) Interfaces work as specified
  3) No integration issues
  4) {Domain-specific validation}

  Generate validation report."

- Expected output:
  - {Validation report}
  - {Issues/recommendations}
- Context from Phase 3: Integrated deliverable
- **GATE**: Block if critical integration issues

---

## Success Criteria

### Parallel Execution
- ✅ All parallel tasks completed (or acceptable partial completion)
- ✅ No resource conflicts between parallel tasks
- ✅ Each task produced expected deliverables

### Integration
- ✅ All components integrated successfully
- ✅ Interfaces function as specified
- ✅ No unresolved conflicts

### Overall
- ✅ {Domain-specific success criterion 1}
- ✅ {Domain-specific success criterion 2}
- ✅ {Domain-specific success criterion 3}

---

## Error Handling

### If Parallel Task Fails

1. Continue other parallel tasks (unless --fail-fast)
2. Document failure reason
3. Assess integration impact
4. Retry failed task OR proceed with partial results

### Graceful Degradation

| Failed Component | Impact | Fallback |
|-----------------|--------|----------|
| {Component A} | {Impact} | {Fallback behavior} |
| {Component B} | {Impact} | {Fallback behavior} |
| {Component C} | {Impact} | {Fallback behavior} |

### If Integration Fails

1. Identify incompatible components
2. Review interface specifications
3. Fix component or interface
4. Re-run integration

---

## Coordination Notes

### Parallel Execution Rules
- All parallel tasks receive same shared context
- Tasks must NOT depend on each other's output
- Each task has independent timeout
- Failures are isolated (unless --fail-fast)

### Resource Considerations
- Limit concurrent agents based on system capacity
- Consider API rate limits
- Monitor memory usage for large outputs

### Timing
- Parallel phase time = slowest task time
- Set appropriate timeouts per task type
- Plan for uneven completion times

---

## Parallel Task Matrix

| Task | Agent | Estimated Time | Dependencies | Can Fail? |
|------|-------|----------------|--------------|-----------|
| A | {specialist-a} | {time} | None | {Yes/No} |
| B | {specialist-b} | {time} | None | {Yes/No} |
| C | {specialist-c} | {time} | None | {Yes/No} |
| D | {specialist-d} | {time} | None | {Yes/No} |

---

Target: $ARGUMENTS
```

---

## Usage Instructions

### Step 1: Identify Parallel Opportunities

Tasks can run in parallel when:
- ✅ No data dependencies between them
- ✅ Different domains/specializations
- ✅ Independent outputs
- ✅ Same shared input context

### Step 2: Design Shared Context

All parallel tasks need the same starting point:

```markdown
## Phase 1: Preparation
- Generate shared specification
- Define interfaces between components
- Establish contracts for integration
```

### Step 3: Structure Parallel Block

```markdown
## Phase 2: Parallel Execution

### ⚡ PARALLEL EXECUTION BLOCK

### 2a. Backend Implementation
### 2b. Frontend Implementation
### 2c. Database Setup

### ⏳ CONVERGENCE CHECKPOINT
```

### Step 4: Plan Integration

After parallel tasks complete:
```markdown
## Phase 3: Integration
- Combine all outputs
- Verify interfaces
- Resolve conflicts
```

### Step 5: Validate Quality

Use COMMAND_QUALITY_RUBRIC.md:

| Category | Target |
|----------|--------|
| Workflow Structure | 15-18/20 |
| Agent Configuration | 14-16/20 |
| Validation & Gates | 11-13/15 |
| Error Handling | 11-13/15 |
| Documentation | 10-12/15 |
| Configuration | 7-9/10 |
| **Total** | **75-90/100** |

---

## Common Parallel Patterns

### Multi-Component Development
```
Preparation → [Backend | Frontend | Database] → Integration → Validation
```

### Multi-Platform Build
```
Preparation → [Web | iOS | Android | Desktop] → Release → Validation
```

### Multi-Domain Analysis
```
Preparation → [Security | Performance | Quality | Accessibility] → Report
```

### Batch Processing
```
Preparation → [Batch 1 | Batch 2 | Batch 3 | Batch 4] → Aggregation
```

---

## Related Resources

- **[COMMAND_PATTERN_INDEX.md](../../command-patterns/COMMAND_PATTERN_INDEX.md)** - All patterns referenced
- **[COMMAND_QUICK_START.md](../../command-patterns/COMMAND_QUICK_START.md)** - 5-step creation process
- **[COMMAND_QUALITY_RUBRIC.md](../../command-patterns/COMMAND_QUALITY_RUBRIC.md)** - Quality scoring
- **[GOLD_STANDARD_COMMAND.md](../GOLD_STANDARD_COMMAND.md)** - Annotated example

---

**Template Version:** 1.0
**Workflow Type:** Parallel Execution
**Patterns Applied:** 11 patterns (OP, WP, AIP, VP, EHP, CP)
