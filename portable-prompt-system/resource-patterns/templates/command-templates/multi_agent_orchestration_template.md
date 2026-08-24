# Multi-Agent Orchestration Command Template

**Purpose:** Template for creating complex commands that coordinate multiple specialized agents across multiple phases to complete end-to-end workflows.

**Best For:**
- Full-stack feature development
- Complex migrations and transformations
- End-to-end deployment pipelines
- Multi-domain operations requiring diverse expertise

**Quality Target:** 85-100/100 (Exemplary tier)

---

## Template Structure

Copy the structure below and replace placeholders (`{...}`) with your workflow-specific content.

---

```markdown
# {Command Name}

{One-line description of what this command orchestrates and delivers.}

<!--
PATTERNS APPLIED:
- OP-01: Multi-Phase Sequential
- OP-02: Parallel Agent Execution
- OP-03: Context Passing Chain
- OP-04: Domain-Specific Agent Selection
- OP-05: Milestone Convergence
- WP-01: Extended Thinking Introduction
- WP-02: Configuration Block
- WP-03: Success Criteria Definition
- WP-04: Coordination Notes Section
- AIP-01: Task Tool Invocation
- AIP-02: Composite Agent Paths
- AIP-03: Detailed Prompt Engineering
- AIP-04: Output Specification
- VP-01: Phase Gate Validation
- EHP-01: Rollback Procedures
- EHP-02: Failure Recovery Workflow
- CP-02: Parameter Configuration
- CP-04: Mode Selection
-->

[Extended thinking: This workflow implements {methodology/approach} for {goal}.
It coordinates {N} specialized agents across {M} phases to deliver {outcome}.
The approach ensures {key benefit 1}, {key benefit 2}, and {key benefit 3}.
Each phase builds on previous outputs, creating {cohesive result} with
{quality attribute 1}, {quality attribute 2}, and {quality attribute 3}.]

## Configuration

### Supported Flags
- `--dry-run`: Analyze and plan only, no implementation
- `--skip-{phase}`: Skip specified phase (use with caution)
- `--{mode-1}`: Enable {mode-1} workflow
- `--{mode-2}`: Enable {mode-2} workflow (default)
- `--verbose`: Enable detailed logging

### Parameters
- `{param_1}`: {Description}
  - Values: `"{value_a}"`, `"{value_b}"`, `"{value_c}"`
  - Default: `"{default_value}"`
- `{param_2}`: {Description}
  - Values: `{range or options}`
  - Default: `{default_value}`

### Modes
- `{mode_quick}`: {Brief description} (~{time estimate})
- `{mode_standard}`: {Brief description} (~{time estimate}, default)
- `{mode_comprehensive}`: {Brief description} (~{time estimate})

---

## Phase 1: {Phase 1 Name}

### 1. {Step 1 Name}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Action verb} {target} for: $ARGUMENTS.

  {Detailed instructions including:}
  1) {Specific task 1}
  2) {Specific task 2}
  3) {Specific task 3}
  4) {Specific task 4}
  5) {Specific task 5}

  Generate {deliverable description} including:
  - {Output component 1}
  - {Output component 2}
  - {Output component 3}

  Consider {constraint or consideration}."

- Expected output:
  - {Deliverable 1}
  - {Deliverable 2}
  - {Deliverable 3}
- Context: {Context requirements or "Initial phase, no prior context needed"}

---

### 2. {Step 2 Name}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Action verb} {target} for: $ARGUMENTS.

  Using {previous output reference}:
  1) {Specific task 1}
  2) {Specific task 2}
  3) {Specific task 3}

  {Additional instructions}."

- Expected output:
  - {Deliverable}
- Context from previous: {Specific output from Step 1}

---

### PHASE GATE: Phase 1 → Phase 2

Before proceeding to {Phase 2 Name}:
- [ ] {Validation checkpoint 1}
- [ ] {Validation checkpoint 2}
- [ ] {Validation checkpoint 3}
- [ ] {Validation checkpoint 4}

**GATE**: Do not proceed until {gate condition}

---

## Phase 2: {Phase 2 Name}

### 3. {Step 3 Name}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Action verb} {target} based on {previous context}..."

- Expected output: {Deliverable}
- Context from previous: {Previous outputs}

---

### 4. {Step 4 Name} (PARALLEL)
- Use Task tool with subagent_type="{category-a}::{specialist-a}"
- Prompt: "{Parallel task A instructions}..."

- Expected output: {Deliverable A}
- Context from previous: {Shared context}

---

### 5. {Step 5 Name} (PARALLEL)
- Use Task tool with subagent_type="{category-b}::{specialist-b}"
- Prompt: "{Parallel task B instructions}..."

- Expected output: {Deliverable B}
- Context from previous: {Shared context}

---

### 6. {Step 6 Name} (PARALLEL)
- Use Task tool with subagent_type="{category-c}::{specialist-c}"
- Prompt: "{Parallel task C instructions}..."

- Expected output: {Deliverable C}
- Context from previous: {Shared context}

---

### CONVERGENCE CHECKPOINT

Steps 4, 5, and 6 can run in parallel but must complete before Phase 3:
- [ ] {Parallel task A} complete
- [ ] {Parallel task B} complete
- [ ] {Parallel task C} complete

---

## Phase 3: {Phase 3 Name}

### 7. {Step 7 Name}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Integration/validation task}..."

- Expected output: {Deliverable}
- Context from previous: All Phase 2 outputs
- **GATE**: Block if {critical condition}

---

### 8. {Step 8 Name}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Quality assurance task}..."

- Expected output: {Deliverable}
- Context from previous: {Previous outputs}

---

## Phase 4: {Phase 4 Name}

### 9. {Step 9 Name}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Deployment/finalization task}..."

- Expected output: {Deliverable}
- Context from previous: All previous phase outputs

---

### 10. {Step 10 Name}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Final task}..."

- Expected output: {Final deliverable}
- Context from previous: {Previous outputs}

---

## Success Criteria

### Technical Criteria
- ✅ {Technical success criterion 1}
- ✅ {Technical success criterion 2}
- ✅ {Technical success criterion 3}
- ✅ {Technical success criterion 4}

### Process Criteria
- ✅ {Process success criterion 1}
- ✅ {Process success criterion 2}
- ✅ {Process success criterion 3}

### Operational Criteria
- ✅ {Operational success criterion 1}
- ✅ {Operational success criterion 2}
- ✅ {Operational success criterion 3}

---

## Rollback Procedures

### Immediate Rollback (< 5 minutes)
1. **{Quick rollback action}**
   ```bash
   # Command for quick rollback
   {command}
   ```

2. **Verify rollback**
   ```bash
   # Verification command
   {command}
   ```

### Standard Rollback (< 30 minutes)
1. **{Standard rollback step 1}**
2. **{Standard rollback step 2}**
3. **{Standard rollback step 3}**

### Full Rollback (< 2 hours)
1. **{Full rollback step 1}**
2. **{Full rollback step 2}**
3. **{Full rollback step 3}**

### Communication Protocol
1. {Communication step 1}
2. {Communication step 2}
3. {Communication step 3}

---

## Error Handling

### If {Failure Scenario 1}
1. {Recovery step 1}
2. {Recovery step 2}
3. {Recovery step 3}

### If {Failure Scenario 2}
1. {Recovery step 1}
2. {Recovery step 2}
3. {Recovery step 3}

### Escalation Path

| Level | Trigger | Action | Contact |
|-------|---------|--------|---------|
| L1 | {Trigger 1} | {Action 1} | {Contact 1} |
| L2 | {Trigger 2} | {Action 2} | {Contact 2} |
| L3 | {Trigger 3} | {Action 3} | {Contact 3} |

---

## Coordination Notes

### Agent Coordination
- {Agent coordination note 1}
- {Agent coordination note 2}
- {Agent coordination note 3}

### Feedback Loops
- {Feedback loop 1}
- {Feedback loop 2}

### Timing Dependencies
- {Timing dependency 1}
- {Timing dependency 2}
- {Timing dependency 3}

### Context Accumulation
- {Context note 1}
- {Context note 2}

---

## Reference Workflows

### Workflow 1: {Quick/Simple Variant}
1. {Simplified step 1}
2. {Simplified step 2}
3. {Simplified step 3}

### Workflow 2: {Comprehensive Variant}
1. {Comprehensive step 1}
2. {Comprehensive step 2}
3. {Comprehensive step 3}

### Anti-Patterns to Avoid
- ❌ {Anti-pattern 1}
- ❌ {Anti-pattern 2}
- ❌ {Anti-pattern 3}

### Best Practices
- ✅ {Best practice 1}
- ✅ {Best practice 2}
- ✅ {Best practice 3}

---

Target: $ARGUMENTS
```

---

## Usage Instructions

### Step 1: Define Your Workflow

1. Identify the end-to-end goal
2. Break into 3-6 phases
3. Identify 8-15 steps across phases
4. Map agents to each step

### Step 2: Configure Phases

| Phase | Purpose | Steps | Agents |
|-------|---------|-------|--------|
| 1 | Foundation/Analysis | 2-3 | Analyst, Architect |
| 2 | Implementation | 3-4 (parallel) | Developers, DB |
| 3 | Validation | 2-3 | Testers, Security |
| 4 | Deployment | 2-3 | DevOps, Monitoring |

### Step 3: Set Up Parallel Execution

Identify independent steps that can run simultaneously:
```markdown
### 4. Backend (PARALLEL)
### 5. Frontend (PARALLEL)
### 6. Database (PARALLEL)

### CONVERGENCE CHECKPOINT
All parallel tasks must complete before Phase 3
```

### Step 4: Define Validation Gates

Between each phase:
```markdown
### PHASE GATE: Phase N → Phase N+1
- [ ] Required condition 1
- [ ] Required condition 2
**GATE**: Block until all conditions met
```

### Step 5: Validate Quality

Use COMMAND_QUALITY_RUBRIC.md to score:

| Category | Target |
|----------|--------|
| Workflow Structure | 18-20/20 |
| Agent Configuration | 16-18/20 |
| Validation & Gates | 13-15/15 |
| Error Handling | 12-15/15 |
| Documentation | 12-15/15 |
| Configuration | 8-10/10 |
| **Total** | **85-100/100** |

---

## Related Resources

- **[COMMAND_PATTERN_INDEX.md](../../command-patterns/COMMAND_PATTERN_INDEX.md)** - All patterns referenced
- **[COMMAND_QUICK_START.md](../../command-patterns/COMMAND_QUICK_START.md)** - 5-step creation process
- **[COMMAND_QUALITY_RUBRIC.md](../../command-patterns/COMMAND_QUALITY_RUBRIC.md)** - Quality scoring
- **[GOLD_STANDARD_COMMAND.md](../GOLD_STANDARD_COMMAND.md)** - Annotated example

---

**Template Version:** 1.0
**Workflow Type:** Multi-Agent Orchestration
**Patterns Applied:** 18 patterns (OP, WP, AIP, VP, EHP, CP)
