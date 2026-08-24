# ANALYSIS Skill Template

> **For troubleshooting and diagnosis.** Use this template when the skill investigates problems, diagnoses issues, analyzes systems, or provides root cause analysis.

---

## When to Use This Template

**Use ANALYSIS when:**
- The skill diagnoses problems or issues
- Investigation follows a systematic approach
- Root cause analysis is required
- Resolution recommendations are provided based on findings

**Examples:**
- Performance troubleshooting
- Security analysis
- Error diagnosis
- System health checks
- Code quality analysis
- Incident investigation

---

## Directory Structure

```
{skill-name}/
├── SKILL.md                     # Required: analysis instructions
├── scripts/                     # Diagnostic automation
│   ├── diagnose.py             # Main diagnostic script
│   ├── collect_data.sh         # Data collection
│   └── generate_report.py      # Report generation
├── references/                  # Knowledge base
│   ├── known_issues.md         # Common issues database
│   ├── symptoms.md             # Symptom-to-cause mapping
│   ├── resolution_playbooks.md # Fix procedures
│   └── escalation_guide.md     # When to escalate
└── assets/                      # Templates and tools
    ├── report_template.md      # Analysis report template
    ├── checklist.md            # Investigation checklist
    └── decision_tree.md        # Diagnosis decision tree
```

---

## SKILL.md Template

Copy everything below the line and customize:

---

```yaml
---
name: {skill-name}
description: Investigate and diagnose {problem domain}. Provides systematic analysis of {issue types} with root cause identification and resolution guidance. Use this skill when troubleshooting {symptoms}, debugging {issues}, analyzing {systems}, or when users mention "why is {X} happening", "fix {problem}", "debug {issue}", or "{domain} not working".
---
```

```markdown
# {Domain} Analysis

{Brief 1-2 sentence overview of what this skill investigates and the value of systematic analysis.}

## Purpose

{Explain what problems this skill diagnoses, what systems it analyzes, and what outcomes it provides. 2-3 sentences maximum.}

## When to Use This Skill

Use this skill when you need to:
- {Use case 1 - specific symptom or issue}
- {Use case 2 - system not behaving as expected}
- {Use case 3 - need root cause analysis}
- {User says: "why...", "debug...", "fix...", "troubleshoot..."}

## When NOT to Use This Skill

Do NOT use this skill when:
- {Exclusion 1 - different domain's issue}
- {Exclusion 2 - prevention, not diagnosis}
- {Exclusion 3 - implementation, not investigation}

## Prerequisites

Before starting analysis:
- **Access:** {Required access/permissions}
- **Tools:** {Required diagnostic tools}
- **Context:** {Information needed before starting}

---

## Investigation Philosophy

**Approach:** {Evidence-based, systematic, hypothesis-driven, etc.}

**Principles:**
1. {Principle 1 - e.g., "Gather data before theorizing"}
2. {Principle 2 - e.g., "Reproduce before analyzing"}
3. {Principle 3 - e.g., "Change one variable at a time"}

**Tool Requirements:**
- {Tool 1}: {What it's used for}
- {Tool 2}: {What it's used for}
- {Tool 3}: {What it's used for}

---

## Quick Diagnosis

### Symptom Lookup

| Symptom | Likely Cause | Quick Check | Resolution |
|---------|--------------|-------------|------------|
| {Symptom 1} | {Most common cause} | `{diagnostic command}` | → See Issue #{N} |
| {Symptom 2} | {Most common cause} | `{diagnostic command}` | → See Issue #{N} |
| {Symptom 3} | {Most common cause} | `{diagnostic command}` | → See Issue #{N} |
| {Symptom 4} | {Most common cause} | `{diagnostic command}` | → See Issue #{N} |
| {Symptom 5} | {Most common cause} | `{diagnostic command}` | → See Issue #{N} |

### Decision Tree

```
START: User reports problem
│
├─→ Is the system responding at all?
│   │
│   ├─→ NO
│   │   └─→ Check: {basic connectivity/availability}
│   │       ├─→ DOWN → Issue #1: {Total Outage}
│   │       └─→ UP → Continue investigation
│   │
│   └─→ YES, but with issues
│       │
│       ├─→ Is it slow?
│       │   └─→ YES → Issue #2: {Performance}
│       │
│       ├─→ Is it returning errors?
│       │   └─→ YES → Issue #3: {Errors}
│       │
│       └─→ Is it producing wrong results?
│           └─→ YES → Issue #4: {Logic/Data}
```

---

## Systematic Investigation

### Phase 1: Data Collection

**Purpose:** Gather all relevant information before analysis.

**Automated collection:**
```bash
# Collect diagnostic data
scripts/collect_data.sh --output diagnostics/

# Or using the diagnostic script
python scripts/diagnose.py collect --target {target}
```

**Manual collection checklist:**
- [ ] {Data point 1 - e.g., error logs}
- [ ] {Data point 2 - e.g., metrics}
- [ ] {Data point 3 - e.g., configuration}
- [ ] {Data point 4 - e.g., recent changes}
- [ ] {Data point 5 - e.g., timeline of events}

**Key questions to answer:**
1. When did the issue start?
2. What changed before the issue appeared?
3. Is the issue reproducible?
4. What is the scope of impact?

### Phase 2: Initial Assessment

**Purpose:** Form initial hypotheses based on collected data.

**Assessment commands:**
```bash
# Quick health check
{health-check-command}

# Status overview
{status-command}

# Recent activity
{activity-command}
```

**Analyze patterns:**
- {Pattern to look for 1}
- {Pattern to look for 2}
- {Pattern to look for 3}

**Initial hypothesis formation:**
Based on {data point}, the likely cause is {hypothesis}.

### Phase 3: Deep Dive

**Purpose:** Test hypotheses and identify root cause.

**For each hypothesis:**

1. **State the hypothesis clearly**
2. **Identify what would confirm/refute it**
3. **Run the specific diagnostic**
4. **Evaluate results**

**Deep diagnostic commands:**
```bash
# Detailed analysis
{deep-diagnostic-command}

# Verbose mode
{verbose-diagnostic-command}

# Trace/debug mode
{trace-command}
```

### Phase 4: Root Cause Identification

**Purpose:** Confirm the root cause with evidence.

**Root cause confirmed when:**
- [ ] Evidence directly supports the conclusion
- [ ] Alternative hypotheses have been ruled out
- [ ] The cause explains all observed symptoms
- [ ] Fixing the cause resolves the issue

**Document findings:**
- **Root cause:** {Description}
- **Evidence:** {What confirms this}
- **Impact:** {Scope of the issue}
- **Timeline:** {When it started, when detected}

---

## Known Issues Database

### Issue #1: {Issue Name}

**Symptoms:**
- {Symptom 1}
- {Symptom 2}

**Quick Diagnosis:**
```bash
{diagnostic-command}
```

**Expected output if this is the issue:**
```
{what you'll see}
```

**Root Causes:**
1. **{Cause A}** (Most common - {X}% of cases)
   - How to identify: {Identification method}
   - Resolution: {Fix steps}

2. **{Cause B}** ({Y}% of cases)
   - How to identify: {Identification method}
   - Resolution: {Fix steps}

3. **{Cause C}** (Rare)
   - How to identify: {Identification method}
   - Resolution: {Fix steps}

**Verification:**
```bash
# Verify the fix worked
{verification-command}
```

---

### Issue #2: {Issue Name}

**Symptoms:**
- {Symptom 1}
- {Symptom 2}

**Quick Diagnosis:**
```bash
{diagnostic-command}
```

**Root Causes:**
1. **{Cause A}**
   - How to identify: {Identification method}
   - Resolution: {Fix steps}

2. **{Cause B}**
   - How to identify: {Identification method}
   - Resolution: {Fix steps}

---

### Issue #3: {Issue Name}

{Continue pattern for additional issues...}

---

## Resolution Procedures

### Procedure: {Fix Name 1}

**Addresses:** Issue #{N}

**Prerequisites:**
- {Required access/permissions}
- {Backup requirements}

**Steps:**

1. **Prepare**
   ```bash
   # Backup current state
   {backup-command}
   ```

2. **Apply fix**
   ```bash
   # Apply the fix
   {fix-command}
   ```

3. **Verify**
   ```bash
   # Confirm fix worked
   {verify-command}
   ```

**Rollback if needed:**
```bash
# Restore from backup
{rollback-command}
```

---

### Procedure: {Fix Name 2}

**Addresses:** Issue #{N}

{Continue pattern...}

---

## Escalation Criteria

### When to Escalate

Escalate immediately if:
- [ ] {Critical condition 1}
- [ ] {Critical condition 2}
- [ ] {Cannot reproduce but impact is severe}
- [ ] {Resolution requires elevated access}
- [ ] {Issue persists after standard fixes}

### Escalation Information to Include

When escalating, provide:
1. **Summary:** {One-line description}
2. **Timeline:** {When started, when detected, actions taken}
3. **Impact:** {Scope, severity, affected users/systems}
4. **Diagnostics collected:** {Attach logs, data}
5. **Hypotheses tested:** {What was tried, what was ruled out}
6. **Current state:** {Is it stable, degraded, down?}

### Escalation Contacts

| Severity | Contact | Channel |
|----------|---------|---------|
| Critical | {Team/Person} | {Method} |
| High | {Team/Person} | {Method} |
| Medium | {Team/Person} | {Method} |

---

## Reporting

### Analysis Report Template

```markdown
# {Domain} Analysis Report

**Date:** {Date}
**Analyst:** {Name}
**Issue ID:** {Reference}

## Executive Summary
{One paragraph summary of findings}

## Symptoms Observed
- {Symptom 1}
- {Symptom 2}

## Investigation Timeline
| Time | Action | Finding |
|------|--------|---------|
| {T1} | {Action} | {Result} |
| {T2} | {Action} | {Result} |

## Root Cause
{Description of root cause with evidence}

## Resolution
{Steps taken to resolve}

## Prevention Recommendations
1. {Recommendation 1}
2. {Recommendation 2}

## Attachments
- {Diagnostic logs}
- {Configuration snapshots}
```

For full template, see `assets/report_template.md`.

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/diagnose.py` | Main diagnostic script |
| `scripts/collect_data.sh` | Automated data collection |
| `scripts/generate_report.py` | Report generation |
| `references/known_issues.md` | Expanded issues database |
| `references/symptoms.md` | Symptom-to-cause mapping |
| `references/resolution_playbooks.md` | Detailed fix procedures |
| `references/escalation_guide.md` | Escalation procedures |
| `assets/report_template.md` | Analysis report template |
| `assets/checklist.md` | Investigation checklist |
| `assets/decision_tree.md` | Complete diagnostic tree |

## Related Skills

- `{related-skill-1}` - {Related domain analysis}
- `{related-skill-2}` - {Prevention/monitoring skill}
- `{related-skill-3}` - {Implementation/fix skill}
```

---

## Key Patterns for ANALYSIS Skills

| Pattern | Implementation | Example |
|---------|----------------|---------|
| **SP-06: Investigation Flow** | Symptom → Diagnosis → Resolution | Phases: Collection → Assessment → Deep Dive → Root Cause |
| **WP-04: Branching Logic** | Decision trees for diagnosis | Quick Diagnosis decision tree |
| **QP-05: Edge Cases** | Known Issues database | Issue-by-issue with causes and fixes |
| **QP-03: Error Messages** | Clear diagnostic output | Expected output examples |
| **RP-04: Grep Patterns** | Searchable issues | Symptom lookup table |
| **IP-03: Error Handling** | Escalation criteria | When to escalate section |

---

## Quality Checklist

Before releasing an ANALYSIS skill:

- [ ] Symptom lookup table covers common cases
- [ ] Decision tree provides clear diagnostic path
- [ ] Investigation phases are systematic
- [ ] Each known issue has symptoms, diagnosis, causes, and resolution
- [ ] Resolution procedures include verification steps
- [ ] Rollback procedures exist for fixes
- [ ] Escalation criteria are clear
- [ ] Report template is provided
- [ ] Diagnostic scripts are documented

---

## Example Skills to Study

Production ANALYSIS skills in the repository:
- `cloudflare-troubleshooting` - CDN/DNS issue diagnosis
- `kubernetes-troubleshooting` - K8s cluster analysis
- `performance-analysis` - Application performance diagnosis
- `security-audit` - Security vulnerability analysis

---

**Last Updated:** 2026-01-29
