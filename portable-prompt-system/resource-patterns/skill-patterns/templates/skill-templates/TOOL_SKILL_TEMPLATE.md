# TOOL Skill Template

> **For technology and tool mastery.** Use this template when the skill provides comprehensive knowledge and operations for a specific technology, framework, or CLI tool.

---

## When to Use This Template

**Use TOOL when:**
- The skill focuses on mastering a specific technology or tool
- Operations are task-based rather than sequential
- Users need reference documentation alongside instructions
- The skill covers multiple independent operations

**Examples:**
- CLI tool mastery (kubectl, terraform, helm)
- Framework expertise (React, Django, Spring)
- Database tools (PostgreSQL, MongoDB, Redis)
- Build tools (webpack, vite, gradle)
- Infrastructure tools (Ansible, Pulumi)

---

## Directory Structure

```
{skill-name}/
├── SKILL.md                     # Required: operations reference
├── scripts/                     # Automation and helpers
│   ├── validate.sh             # Validation script
│   ├── generate.sh             # Generation script
│   └── diagnose.sh             # Diagnostic script
├── references/                  # Deep documentation
│   ├── commands.md             # Complete command reference
│   ├── configuration.md        # Config file reference
│   ├── best_practices.md       # Patterns and anti-patterns
│   └── migration_guide.md      # Version migration
└── assets/                      # Templates and examples
    ├── config.example.yaml     # Example configuration
    └── cheatsheet.md           # Quick reference
```

---

## SKILL.md Template

Copy everything below the line and customize:

---

```yaml
---
name: {skill-name}
description: Comprehensive {tool/technology} mastery for {use cases}. Use this skill when working with {context 1}, {context 2}, or when users mention "{trigger phrase 1}", "{trigger phrase 2}", "{command name}", or "{technology name}".
---
```

```markdown
# {Tool/Technology Name}

{Brief 1-2 sentence overview of what this tool does and why mastery matters.}

## Purpose

{Explain what problems this tool solves and what capabilities mastery provides. 2-3 sentences maximum.}

## When to Use This Skill

Use this skill when you need to:
- {Use case 1 - specific task}
- {Use case 2 - specific task}
- {Use case 3 - specific task}
- {User mentions: keyword1, keyword2, tool-name}

## When NOT to Use This Skill

Do NOT use this skill when:
- {Exclusion 1 - redirect to appropriate skill}
- {Exclusion 2 - explain why this doesn't apply}
- {Alternative tool is more appropriate - when to use it}

## Prerequisites

- **{Requirement 1}:** {Version/installation requirement}
- **{Requirement 2}:** {Access/permission requirement}
- **{Requirement 3}:** {Knowledge prerequisite}

**Verify installation:**
```bash
{tool} --version
# Expected: {expected version output}
```

---

## Quick Reference

### Most Common Operations

| Task | Command | Notes |
|------|---------|-------|
| {Task 1} | `{command 1}` | {When to use} |
| {Task 2} | `{command 2}` | {When to use} |
| {Task 3} | `{command 3}` | {When to use} |
| {Task 4} | `{command 4}` | {When to use} |
| {Task 5} | `{command 5}` | {When to use} |

### Essential Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `--{flag1}` | {What it does} | `{example usage}` |
| `--{flag2}` | {What it does} | `{example usage}` |
| `-{short}` | {What it does} | `{example usage}` |

---

## Core Operations

### Operation: {Operation Name 1}

**Purpose:** {What this operation accomplishes}

**Command:**
```bash
{tool} {subcommand} [OPTIONS] <ARGS>
```

**Parameters:**
| Parameter | Required | Description | Default |
|-----------|----------|-------------|---------|
| `{param1}` | Yes | {Description} | - |
| `{param2}` | No | {Description} | `{default}` |
| `--{option1}` | No | {Description} | `{default}` |

**Examples:**

Basic usage:
```bash
{basic example command}
```

With options:
```bash
{advanced example command}
```

**Expected output:**
```
{expected output}
```

**Common errors:**
| Error | Cause | Fix |
|-------|-------|-----|
| `{error message}` | {Why it happens} | {How to fix} |

---

### Operation: {Operation Name 2}

**Purpose:** {What this operation accomplishes}

**Command:**
```bash
{tool} {subcommand} [OPTIONS] <ARGS>
```

**Parameters:**
| Parameter | Required | Description | Default |
|-----------|----------|-------------|---------|
| `{param1}` | Yes | {Description} | - |
| `{param2}` | No | {Description} | `{default}` |

**Examples:**
```bash
# {Scenario 1}
{example command 1}

# {Scenario 2}
{example command 2}
```

---

### Operation: {Operation Name 3}

**Purpose:** {What this operation accomplishes}

{Continue pattern for additional operations...}

---

## Configuration Reference

### Configuration File Location

```bash
# Default locations
{path/to/default/config}

# User-specific
{path/to/user/config}

# Project-specific
{path/to/project/config}
```

### Configuration Structure

```yaml
# {config-filename}
{section1}:
  {key1}: {value1}     # {Description}
  {key2}: {value2}     # {Description}

{section2}:
  {key3}: {value3}     # {Description}
  {key4}:              # {Description}
    - {item1}
    - {item2}
```

### Essential Configuration Options

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `{key1}` | string | `{default}` | {What it controls} |
| `{key2}` | integer | `{default}` | {What it controls} |
| `{key3}` | boolean | `{default}` | {What it controls} |
| `{key4}` | list | `[]` | {What it controls} |

For complete configuration reference, see `references/configuration.md`.

---

## Best Practices

### Do

- **{Best practice 1}:** {Explanation of why}
  ```bash
  # Good
  {good example}
  ```

- **{Best practice 2}:** {Explanation of why}

- **{Best practice 3}:** {Explanation of why}

### Don't

- **{Anti-pattern 1}:** {Why it's problematic}
  ```bash
  # Bad
  {bad example}

  # Better
  {better example}
  ```

- **{Anti-pattern 2}:** {Why it's problematic}

### Performance Tips

1. **{Tip 1}:** {Explanation}
2. **{Tip 2}:** {Explanation}
3. **{Tip 3}:** {Explanation}

---

## Troubleshooting

### Common Issues

| Symptom | Cause | Solution |
|---------|-------|----------|
| {Symptom 1} | {Why it happens} | {How to fix} |
| {Symptom 2} | {Why it happens} | {How to fix} |
| {Symptom 3} | {Why it happens} | {How to fix} |
| {Symptom 4} | {Why it happens} | {How to fix} |

### Diagnostic Commands

```bash
# Check {tool} status
{diagnostic command 1}

# Verify configuration
{diagnostic command 2}

# Debug mode
{diagnostic command 3}
```

### Issue: {Specific Problem Name}

**Symptoms:** {What the user will observe}

**Quick Diagnosis:**
```bash
{diagnostic-command}
```

**Root Causes:**
1. {Cause A} - {How to identify}
2. {Cause B} - {How to identify}

**Resolution:**
```bash
{fix-command}
```

For additional troubleshooting, see `references/troubleshooting.md`.

---

## Integration Patterns

### With {Related Tool 1}

```bash
# Common integration pattern
{integration command example}
```

### With {Related Tool 2}

```bash
# Common integration pattern
{integration command example}
```

---

## Version Compatibility

| Version | Status | Notable Changes |
|---------|--------|-----------------|
| {v3.x} | Current | {Key features} |
| {v2.x} | Supported | {Key differences} |
| {v1.x} | Deprecated | {Migration notes} |

For migration guidance, see `references/migration_guide.md`.

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/validate.sh` | {What it validates} |
| `scripts/generate.sh` | {What it generates} |
| `references/commands.md` | Complete command reference |
| `references/configuration.md` | Full config documentation |
| `references/best_practices.md` | Patterns and anti-patterns |
| `assets/config.example.yaml` | Working configuration example |
| `assets/cheatsheet.md` | Quick reference card |

## Related Skills

- `{related-skill-1}` - {How it relates/when to use instead}
- `{related-skill-2}` - {How it complements this skill}
- `{related-skill-3}` - {Common companion tool}
```

---

## Key Patterns for TOOL Skills

| Pattern | Implementation | Example |
|---------|----------------|---------|
| **SP-03: Task-Based Organization** | Group by operation type | "Core Operations", "Configuration", "Troubleshooting" |
| **IP-02: CLI Pattern Templates** | Consistent command docs | Command → Parameters → Examples → Errors |
| **RP-01: Script Documentation** | Self-describing scripts | Full docstrings with usage examples |
| **QP-02: CLI Verbosity** | Show flag options | `--verbose`, `--debug` flags documented |
| **RP-03: Usable Templates** | Example configs | `assets/config.example.yaml` |
| **SP-07: Cross-References** | Link to deep docs | "See `references/configuration.md`" |

---

## Quality Checklist

Before releasing a TOOL skill:

- [ ] Quick Reference table covers most common tasks
- [ ] Each operation has command, parameters, examples, and errors
- [ ] Configuration reference is complete and typed
- [ ] Best practices include both Do and Don't examples
- [ ] Troubleshooting covers common issues with solutions
- [ ] Version compatibility is documented
- [ ] Integration patterns with related tools are shown
- [ ] Related skills link to complementary tools

---

## Example Skills to Study

Production TOOL skills in the repository:
- `terraform-module-library` - Infrastructure as Code tool mastery
- `kubectl-operations` - Kubernetes CLI operations
- `helm-chart-operations` - Helm package manager expertise

---

**Last Updated:** 2026-01-29
