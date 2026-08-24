# Sequential Workflow Command Template

**Purpose:** Template for creating commands with linear, step-by-step execution where each step depends on the previous step's output.

**Best For:**
- Pipeline-style workflows
- Code review and quality gates
- Git workflows (commit → review → merge)
- Step-by-step transformations
- Audit and compliance processes

**Quality Target:** 75-90/100 (Standard tier)

---

## Template Structure

Copy the structure below and replace placeholders (`{...}`) with your workflow-specific content.

---

```markdown
# {Command Name}

{One-line description of the sequential workflow and its outcome.}

<!--
PATTERNS APPLIED:
- OP-01: Multi-Phase Sequential
- OP-03: Context Passing Chain
- WP-01: Extended Thinking Introduction
- WP-03: Success Criteria Definition
- WP-05: Input Arguments Handling
- AIP-01: Task Tool Invocation
- AIP-03: Detailed Prompt Engineering
- AIP-04: Output Specification
- VP-01: Phase Gate Validation
- VP-05: Continuous Validation Loop
- EHP-02: Failure Recovery Workflow
- CP-01: Flag-Based Configuration
-->

[Extended thinking: This workflow implements a sequential pipeline for {goal}.
Each step builds directly on the previous step's output, creating a {result type}.
The approach ensures {quality attribute} through {mechanism}. Critical checkpoints
validate progress before proceeding to subsequent steps.]

## Configuration

### Supported Flags
- `--dry-run`: Analyze only, no modifications
- `--skip-validation`: Skip intermediate validation (use with caution)
- `--verbose`: Enable detailed step-by-step logging
- `--strict`: Fail on any warning, not just errors

### Parameters
- `{main_param}`: {Description}
  - Default: {default_value}

---

## Step 1: {Step 1 Name}

### Input
- Primary: $ARGUMENTS
- Prerequisites: {Any required preconditions}

### Execution
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Action verb} {target} for: $ARGUMENTS.

  {Detailed instructions:}
  1) {Specific task 1}
  2) {Specific task 2}
  3) {Specific task 3}

  Generate {output description}."

### Output
- {Deliverable}: {Format/description}

### Validation
- [ ] {Validation check 1}
- [ ] {Validation check 2}

---

## Step 2: {Step 2 Name}

### Input
- From Step 1: {Specific output used}

### Execution
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "Using {Step 1 output}, {action verb} {target}.

  {Detailed instructions:}
  1) {Specific task 1}
  2) {Specific task 2}
  3) {Specific task 3}

  {Additional requirements}."

### Output
- {Deliverable}: {Format/description}

### Validation
- [ ] {Validation check 1}
- [ ] {Validation check 2}

---

## Step 3: {Step 3 Name}

### Input
- From Step 1: {What's carried forward}
- From Step 2: {Specific output used}

### Execution
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "Based on {previous context}, {action verb} {target}.

  {Detailed instructions}."

### Output
- {Deliverable}: {Format/description}

### Validation
- [ ] {Validation check 1}
- [ ] {Validation check 2}
- **GATE**: Do not proceed if {blocking condition}

---

## Step 4: {Step 4 Name}

### Input
- Accumulated context from Steps 1-3

### Execution
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Final processing instructions}."

### Output
- {Final deliverable}: {Format/description}

### Validation
- [ ] {Final validation check 1}
- [ ] {Final validation check 2}

---

## Step 5: {Step 5 Name} (Final)

### Input
- All previous step outputs

### Execution
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Completion/delivery instructions}."

### Output
- {Final output}: {Format/description}

### Validation
- [ ] {Completion validation 1}
- [ ] {Completion validation 2}

---

## Context Flow

```
Step 1 ──output──→ Step 2 ──output──→ Step 3 ──output──→ Step 4 ──output──→ Step 5
  │                  │                  │                  │                  │
  └─validation       └─validation       └─validation       └─validation       └─final check
```

### Context Accumulation

| Step | Receives | Produces | Passes Forward |
|------|----------|----------|----------------|
| 1 | $ARGUMENTS | {Output 1} | {Output 1} |
| 2 | {Output 1} | {Output 2} | {Output 1}, {Output 2} |
| 3 | {Output 1}, {Output 2} | {Output 3} | All previous + {Output 3} |
| 4 | All previous | {Output 4} | All previous + {Output 4} |
| 5 | All previous | Final result | — |

---

## Success Criteria

- ✅ {Success criterion 1}
- ✅ {Success criterion 2}
- ✅ {Success criterion 3}
- ✅ {Success criterion 4}
- ✅ All intermediate validations passed
- ✅ No blocking conditions encountered

---

## Failure Recovery

### If Step {N} Fails

1. Capture failure details
2. Rollback to Step {N-1} state
3. Address failure cause
4. Retry from Step {N}

### Recovery Actions

| Step | Failure Type | Recovery Action |
|------|--------------|-----------------|
| 1 | {Failure type} | {Recovery action} |
| 2 | {Failure type} | {Recovery action} |
| 3 | {Failure type} | {Recovery action} |
| 4 | {Failure type} | {Recovery action} |
| 5 | {Failure type} | {Recovery action} |

### Abort Conditions

Stop workflow entirely if:
- {Abort condition 1}
- {Abort condition 2}
- {Abort condition 3}

---

## Reference

### Quick Workflow (3 steps)
1. {Essential step 1}
2. {Essential step 2}
3. {Essential step 3}

### Best Practices
- ✅ Validate after each step
- ✅ Preserve context chain
- ✅ Handle failures at each step
- ✅ Log progress for debugging

### Common Issues
- ❌ Skipping validation steps
- ❌ Not preserving context between steps
- ❌ Ignoring intermediate failures

---

Target: $ARGUMENTS
```

---

## Usage Instructions

### Step 1: Map Your Pipeline

Identify the linear sequence of operations:

```
Input → Process A → Process B → Process C → Output
```

### Step 2: Define Context Flow

For each step, specify:
- **Input**: What it receives from previous steps
- **Execution**: What it does
- **Output**: What it produces
- **Validation**: How to verify success

### Step 3: Establish Dependencies

```markdown
### Input
- From Step 1: Analysis report
- From Step 2: Implementation code

### Execution
- Using both inputs, validate integration...
```

### Step 4: Add Validation Points

After each step:
```markdown
### Validation
- [ ] Output meets format requirements
- [ ] No errors or warnings
- **GATE**: Block if critical issues found
```

### Step 5: Validate Quality

Use COMMAND_QUALITY_RUBRIC.md:

| Category | Target |
|----------|--------|
| Workflow Structure | 15-18/20 |
| Agent Configuration | 14-16/20 |
| Validation & Gates | 12-14/15 |
| Error Handling | 10-12/15 |
| Documentation | 10-12/15 |
| Configuration | 7-9/10 |
| **Total** | **75-90/100** |

---

## When to Use Sequential vs Parallel

**Use Sequential when:**
- ✅ Each step depends on previous output
- ✅ Order matters for correctness
- ✅ Validation needed between steps
- ✅ Linear pipeline (review → test → deploy)

**Consider Parallel when:**
- ❌ Steps are independent
- ❌ Multiple domains can work simultaneously
- ❌ Speed is critical
- ❌ Different agents don't need each other's output

---

## Related Resources

- **[COMMAND_PATTERN_INDEX.md](../../command-patterns/COMMAND_PATTERN_INDEX.md)** - All patterns referenced
- **[COMMAND_QUICK_START.md](../../command-patterns/COMMAND_QUICK_START.md)** - 5-step creation process
- **[COMMAND_QUALITY_RUBRIC.md](../../command-patterns/COMMAND_QUALITY_RUBRIC.md)** - Quality scoring
- **[GOLD_STANDARD_COMMAND.md](../GOLD_STANDARD_COMMAND.md)** - Annotated example

---

**Template Version:** 1.0
**Workflow Type:** Sequential Pipeline
**Patterns Applied:** 12 patterns (OP, WP, AIP, VP, EHP, CP)
