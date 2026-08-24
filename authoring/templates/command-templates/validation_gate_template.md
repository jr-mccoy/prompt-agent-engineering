# Validation Gate Command Template

**Purpose:** Template for creating commands with strong validation checkpoints, quality gates, and compliance verification at each stage.

**Best For:**
- Security scanning and hardening
- Compliance verification (GDPR, HIPAA, SOC2)
- Code quality enforcement
- Pre-deployment verification
- TDD and testing workflows
- Audit trail operations

**Quality Target:** 80-95/100 (Quality-focused tier)

---

## Template Structure

Copy the structure below and replace placeholders (`{...}`) with your workflow-specific content.

---

```markdown
# {Command Name}

{One-line description emphasizing validation, quality gates, and compliance.}

<!--
PATTERNS APPLIED:
- OP-01: Multi-Phase Sequential
- OP-03: Context Passing Chain
- WP-01: Extended Thinking Introduction
- WP-02: Configuration Block
- WP-03: Success Criteria Definition
- AIP-01: Task Tool Invocation
- AIP-04: Output Specification
- VP-01: Phase Gate Validation
- VP-02: Severity-Based Classification
- VP-03: Threshold-Based Validation
- VP-04: Validation Checkpoint Matrix
- VP-05: Continuous Validation Loop
- EHP-02: Failure Recovery Workflow
- EHP-04: Error Escalation Path
- CP-01: Flag-Based Configuration
- CP-03: Threshold Configuration
-->

[Extended thinking: This workflow implements {validation approach} for {domain}.
Quality gates are enforced at {N} checkpoints with {threshold type} requirements.
The approach ensures {compliance/quality standard} through continuous validation.
No phase proceeds until its gate criteria are met, providing {audit/safety guarantee}.]

## Configuration

### Validation Thresholds

| Threshold | Default | Override |
|-----------|---------|----------|
| {threshold_1} | {value} | --{threshold_1}={value} |
| {threshold_2} | {value} | --{threshold_2}={value} |
| {threshold_3} | {value} | --{threshold_3}={value} |
| {threshold_4} | {value} | Cannot override |

### Severity Levels

- **CRITICAL**: {Definition} - Blocks all progress
- **HIGH**: {Definition} - Blocks phase transition
- **MEDIUM**: {Definition} - Must fix within {timeframe}
- **LOW**: {Definition} - Track for future improvement

### Supported Flags
- `--strict`: Fail on any finding (including LOW)
- `--audit-mode`: Generate compliance audit trail
- `--exemptions={file}`: Load approved exemptions
- `--dry-run`: Report findings without blocking

---

## Phase 1: {Initial Assessment Phase}

### 1. {Assessment Step}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "{Analyze/Assess/Scan} {target} for: $ARGUMENTS.

  Perform {assessment type}:
  1) {Assessment task 1}
  2) {Assessment task 2}
  3) {Assessment task 3}
  4) {Assessment task 4}

  Classify findings by severity (CRITICAL/HIGH/MEDIUM/LOW).
  Generate baseline for subsequent validation."

- Expected output:
  - {Assessment report}
  - {Findings with severity classification}
  - {Baseline metrics}

### Validation Matrix - Step 1

| Check | Threshold | Status |
|-------|-----------|--------|
| {Check 1} | {Threshold} | ⬜ |
| {Check 2} | {Threshold} | ⬜ |
| {Check 3} | {Threshold} | ⬜ |

---

### VALIDATION GATE 1: Assessment Complete

**Blocking Conditions:**
- ❌ Any CRITICAL findings → BLOCK, escalate immediately
- ❌ {Threshold} CRITICAL/HIGH combined → BLOCK, require remediation

**Pass Conditions:**
- ✅ All CRITICAL findings resolved
- ✅ HIGH findings below {threshold}
- ✅ Baseline metrics captured

**Gate Decision:**
```
IF CRITICAL_COUNT > 0:
    BLOCK → Escalate to L3
ELIF HIGH_COUNT > {threshold}:
    BLOCK → Remediation required
ELSE:
    PASS → Proceed to Phase 2
```

---

## Phase 2: {Remediation/Processing Phase}

### 2. {Remediation Step}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "Address findings from assessment on: $ARGUMENTS.

  Remediate in priority order:
  1) CRITICAL findings (if any remain)
  2) HIGH findings
  3) MEDIUM findings (if time permits)

  For each finding:
  - Identify root cause
  - Implement fix
  - Verify fix effectiveness
  - Document change

  Generate remediation report."

- Expected output:
  - {Remediation report}
  - {Changes made}
  - {Verification results}
- Context from previous: Assessment report and findings

### Continuous Validation Loop - Step 2

```
For each remediation:
  1. Apply fix
  2. Run validation check
  3. IF check passes:
       Mark finding resolved
     ELSE:
       Retry fix OR escalate
  4. Update progress report
```

### Validation Matrix - Step 2

| Finding | Severity | Fix Applied | Verified |
|---------|----------|-------------|----------|
| {Finding 1} | {Severity} | ⬜ | ⬜ |
| {Finding 2} | {Severity} | ⬜ | ⬜ |
| {Finding 3} | {Severity} | ⬜ | ⬜ |

---

### VALIDATION GATE 2: Remediation Complete

**Blocking Conditions:**
- ❌ Any CRITICAL findings unresolved → BLOCK
- ❌ More than {N} HIGH findings unresolved → BLOCK

**Pass Conditions:**
- ✅ Zero CRITICAL findings
- ✅ HIGH findings ≤ {threshold} (with approved exemptions)
- ✅ All remediation changes verified

---

## Phase 3: {Verification Phase}

### 3. {Verification Step}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "Verify {target} after remediation for: $ARGUMENTS.

  Re-run {assessment type} to confirm:
  1) All claimed remediations effective
  2) No new issues introduced
  3) Thresholds met

  Compare against baseline from Phase 1.
  Generate verification report."

- Expected output:
  - {Verification report}
  - {Comparison to baseline}
  - {Final metrics}
- Context from previous: Baseline + Remediation report

### Validation Matrix - Step 3

| Metric | Baseline | Current | Threshold | Status |
|--------|----------|---------|-----------|--------|
| {Metric 1} | {value} | {value} | {threshold} | ⬜ |
| {Metric 2} | {value} | {value} | {threshold} | ⬜ |
| {Metric 3} | {value} | {value} | {threshold} | ⬜ |

### Regression Check

- [ ] No new CRITICAL findings
- [ ] No new HIGH findings
- [ ] MEDIUM/LOW count not increased significantly
- [ ] All metrics improved or stable

---

### VALIDATION GATE 3: Verification Complete

**Blocking Conditions:**
- ❌ New CRITICAL or HIGH findings → BLOCK, return to Phase 2
- ❌ Metrics below threshold → BLOCK
- ❌ Regression detected → BLOCK

**Pass Conditions:**
- ✅ All thresholds met
- ✅ No regressions
- ✅ Improvement from baseline

---

## Phase 4: {Certification/Completion Phase}

### 4. {Certification Step}
- Use Task tool with subagent_type="{category}::{specialist}"
- Prompt: "Generate {certification/compliance} report for: $ARGUMENTS.

  Document:
  1) Final state and metrics
  2) Remediation summary
  3) Exemptions and justifications
  4) Recommendations for future
  5) Audit trail

  Generate formal {certification type}."

- Expected output:
  - {Certification report}
  - {Audit trail}
  - {Recommendations}

### Final Validation Matrix

| Requirement | Status | Evidence |
|-------------|--------|----------|
| {Requirement 1} | ⬜ | {Evidence location} |
| {Requirement 2} | ⬜ | {Evidence location} |
| {Requirement 3} | ⬜ | {Evidence location} |
| {Requirement 4} | ⬜ | {Evidence location} |

---

### FINAL VALIDATION GATE

**Certification Requirements:**
- ✅ All phase gates passed
- ✅ All thresholds met
- ✅ Audit trail complete
- ✅ Documentation generated

**Certification Status:**
```
IF all_requirements_met:
    STATUS = CERTIFIED
    Generate certification
ELSE:
    STATUS = NOT CERTIFIED
    List gaps
    Recommend remediation
```

---

## Success Criteria

### Quality Gates
- ✅ Zero CRITICAL findings in final state
- ✅ HIGH findings ≤ {threshold} with approved exemptions
- ✅ All thresholds met (coverage, performance, etc.)
- ✅ No regressions from baseline

### Compliance
- ✅ All required checks completed
- ✅ Audit trail generated
- ✅ Evidence documented
- ✅ Certification issued (if applicable)

### Process
- ✅ All phase gates passed
- ✅ Continuous validation maintained
- ✅ Escalation paths followed when needed

---

## Escalation Path

| Level | Trigger | Action | SLA |
|-------|---------|--------|-----|
| L1 | MEDIUM findings | Track in backlog | 7 days |
| L2 | HIGH findings | Require remediation | 24 hours |
| L3 | CRITICAL findings | Immediate escalation | 1 hour |
| L4 | Multiple CRITICAL | War room activation | Immediate |

### Escalation Contacts

- L1: {Team/system for tracking}
- L2: {Team lead/senior engineer}
- L3: {Security team/management}
- L4: {Executive/incident command}

---

## Failure Recovery

### If Validation Gate Fails

1. **Identify blocking condition**
   - Which threshold not met?
   - Which findings unresolved?

2. **Determine recovery path**
   - Return to previous phase
   - Apply targeted remediation
   - Request exemption (with justification)

3. **Document and retry**
   - Log failure reason
   - Track remediation attempt
   - Re-run validation

### Exemption Process

For approved exemptions:
1. Document finding and reason for exemption
2. Identify compensating controls
3. Get approval from {authority}
4. Add to exemption file
5. Set review date

---

## Audit Trail

### Required Documentation

| Document | Purpose | Location |
|----------|---------|----------|
| Assessment Report | Initial state | {path} |
| Findings Log | Issue tracking | {path} |
| Remediation Log | Fix documentation | {path} |
| Verification Report | Confirmation | {path} |
| Certification | Final approval | {path} |
| Exemptions | Approved exceptions | {path} |

### Audit Queries

```
# Find all CRITICAL findings
grep "CRITICAL" findings.log

# Check remediation status
cat remediation.log | jq '.status'

# Verify thresholds
compare_metrics baseline.json current.json
```

---

Target: $ARGUMENTS
```

---

## Usage Instructions

### Step 1: Define Quality Thresholds

```markdown
### Validation Thresholds
| Threshold | Default |
|-----------|---------|
| min_coverage | 80% |
| max_critical | 0 |
| max_high | 3 |
```

### Step 2: Design Validation Gates

For each phase transition:
```markdown
### VALIDATION GATE N

**Blocking Conditions:**
- ❌ Condition that blocks progress

**Pass Conditions:**
- ✅ Condition required to proceed

**Gate Decision:** (pseudocode logic)
```

### Step 3: Add Continuous Validation

Within phases:
```markdown
### Continuous Validation Loop
For each change:
  1. Apply change
  2. Run validation
  3. Verify threshold
  4. Continue or rollback
```

### Step 4: Implement Escalation

```markdown
## Escalation Path
| Level | Trigger | Action | SLA |
```

### Step 5: Validate Quality

Use COMMAND_QUALITY_RUBRIC.md:

| Category | Target |
|----------|--------|
| Workflow Structure | 16-18/20 |
| Agent Configuration | 14-16/20 |
| Validation & Gates | 14-15/15 |
| Error Handling | 12-14/15 |
| Documentation | 12-14/15 |
| Configuration | 8-10/10 |
| **Total** | **80-95/100** |

---

## Related Resources

- **[COMMAND_PATTERN_INDEX.md](../../command-patterns/COMMAND_PATTERN_INDEX.md)** - All patterns referenced
- **[COMMAND_QUICK_START.md](../../command-patterns/COMMAND_QUICK_START.md)** - 5-step creation process
- **[COMMAND_QUALITY_RUBRIC.md](../../command-patterns/COMMAND_QUALITY_RUBRIC.md)** - Quality scoring
- **[GOLD_STANDARD_COMMAND.md](../GOLD_STANDARD_COMMAND.md)** - Annotated example

---

**Template Version:** 1.0
**Workflow Type:** Validation Gate
**Patterns Applied:** 16 patterns (heavy VP emphasis)
