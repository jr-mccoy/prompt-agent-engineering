# Skill Type Templates

> **Type-specific starting points for skill creation.** Each template provides structure, patterns, and examples optimized for a specific skill type.

---

## Quick Selection Guide

| User Request Pattern | Skill Type | Template |
|---------------------|------------|----------|
| "How do I set up..." / "Walk me through..." | **WORKFLOW** | [WORKFLOW_SKILL_TEMPLATE.md](WORKFLOW_SKILL_TEMPLATE.md) |
| "Help me use [tool]..." / "How does [tool] work..." | **TOOL** | [TOOL_SKILL_TEMPLATE.md](TOOL_SKILL_TEMPLATE.md) |
| "What are the requirements for..." / "Ensure compliance with..." | **DOMAIN** | [DOMAIN_SKILL_TEMPLATE.md](DOMAIN_SKILL_TEMPLATE.md) |
| "Create/Generate/Build..." | **CREATION** | [CREATION_SKILL_TEMPLATE.md](CREATION_SKILL_TEMPLATE.md) |
| "Debug/Fix/Investigate/Why is..." | **ANALYSIS** | [ANALYSIS_SKILL_TEMPLATE.md](ANALYSIS_SKILL_TEMPLATE.md) |
| "Connect/Integrate with..." | **INTEGRATION** | [INTEGRATION_SKILL_TEMPLATE.md](INTEGRATION_SKILL_TEMPLATE.md) |

---

## Template Overview

### WORKFLOW — Multi-Step Sequential Processes

**Use when:** The skill guides through ordered steps with validation checkpoints

**Key features:**
- Numbered step structure
- Skip conditions for optional steps
- Validation checkpoints between phases
- Rollback procedures
- Decision point branching

**Examples:** CI/CD setup, deployment workflows, migration processes, onboarding

📄 [WORKFLOW_SKILL_TEMPLATE.md](WORKFLOW_SKILL_TEMPLATE.md)

---

### TOOL — Technology/Tool Mastery

**Use when:** The skill provides comprehensive knowledge for a specific technology or CLI tool

**Key features:**
- Task-based organization (not sequential)
- Quick reference tables
- Command/operation documentation
- Configuration reference
- Troubleshooting section

**Examples:** kubectl, terraform, helm, webpack, database tools

📄 [TOOL_SKILL_TEMPLATE.md](TOOL_SKILL_TEMPLATE.md)

---

### DOMAIN — Domain Expertise Application

**Use when:** The skill encapsulates specialized knowledge, standards, or compliance requirements

**Key features:**
- Core concepts definitions
- Requirements and standards reference
- Implementation patterns
- Evaluation criteria and rubrics
- Compliance checklists

**Examples:** PCI-DSS compliance, API design principles, accessibility (WCAG), security standards

📄 [DOMAIN_SKILL_TEMPLATE.md](DOMAIN_SKILL_TEMPLATE.md)

---

### CREATION — Artifact Generation

**Use when:** The skill generates output artifacts from inputs

**Key features:**
- Input specification with validation
- Generation process steps
- Output format specification
- Template files in assets/
- Quality validation

**Examples:** PDF generation, code scaffolding, configuration generation, report creation

📄 [CREATION_SKILL_TEMPLATE.md](CREATION_SKILL_TEMPLATE.md)

---

### ANALYSIS — Troubleshooting and Diagnosis

**Use when:** The skill investigates problems and provides root cause analysis

**Key features:**
- Symptom lookup tables
- Decision tree for diagnosis
- Known issues database
- Resolution procedures
- Escalation criteria

**Examples:** Performance troubleshooting, security analysis, error diagnosis, incident investigation

📄 [ANALYSIS_SKILL_TEMPLATE.md](ANALYSIS_SKILL_TEMPLATE.md)

---

### INTEGRATION — External API/Service Connections

**Use when:** The skill connects to external APIs or services

**Key features:**
- Authentication documentation
- Core operations with full request/response
- Rate limit handling
- Error code reference
- Webhook setup

**Examples:** GitHub API, Stripe, Slack, AWS services, third-party SaaS

📄 [INTEGRATION_SKILL_TEMPLATE.md](INTEGRATION_SKILL_TEMPLATE.md)

---

## How to Use These Templates

### 1. Select the Right Template

Ask: **What does the user get from this skill?**

| If they get... | Use... |
|----------------|--------|
| A guided process | WORKFLOW |
| Tool mastery | TOOL |
| Expert knowledge | DOMAIN |
| A generated artifact | CREATION |
| A diagnosis/fix | ANALYSIS |
| API connectivity | INTEGRATION |

### 2. Copy the Template Content

Each template has a section marked:

```
Copy everything below the line and customize:
---
```

Copy from that point into your new `SKILL.md` file.

### 3. Customize for Your Skill

1. Replace all `{placeholders}` with actual content
2. Remove sections that don't apply
3. Add sections specific to your skill
4. Populate bundled resources (scripts/, references/, assets/)

### 4. Validate with Quality Rubric

Use [SKILL_QUALITY_RUBRIC.md](../../SKILL_QUALITY_RUBRIC.md) to score your skill.

**Target:** 80+ points for production-ready quality.

---

## Template Comparison

| Aspect | WORKFLOW | TOOL | DOMAIN | CREATION | ANALYSIS | INTEGRATION |
|--------|----------|------|--------|----------|----------|-------------|
| **Primary Structure** | Sequential steps | Operations | Knowledge sections | Input→Output | Investigation phases | API operations |
| **Core Section** | Step 1, 2, 3... | Core Operations | Requirements & Standards | Generation Process | Known Issues Database | Core Operations |
| **Key Pattern** | SP-02: Numbered Steps | SP-03: Task-Based | SP-04: Knowledge Org | SP-05: Output Org | SP-06: Investigation Flow | IP-01: API Docs |
| **Bundled Scripts** | Step automation | Validation, diagnostics | Checklist runners | Generation, validation | Diagnostic tools | API wrappers |
| **Main Asset Type** | Checklists, templates | Config examples, cheatsheets | Compliance checklists, rubrics | Templates, schemas | Report templates, decision trees | Config templates, schemas |

---

## Combining Types

Some skills combine aspects of multiple types. When this happens:

1. **Choose the primary type** based on the skill's main purpose
2. **Incorporate patterns** from secondary types as needed
3. **Maintain clarity** — don't try to do everything

**Common combinations:**

| Primary | + Secondary | Example |
|---------|-------------|---------|
| WORKFLOW | + INTEGRATION | Deployment workflow that calls APIs |
| TOOL | + DOMAIN | Tool mastery with best practices |
| CREATION | + WORKFLOW | Multi-step artifact generation |
| ANALYSIS | + INTEGRATION | Diagnosis using external monitoring APIs |

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [../GOLD_STANDARD_SKILL.md](../GOLD_STANDARD_SKILL.md) | Annotated example of a production skill |
| [../SKILL_PATTERN_INDEX.md](../../SKILL_PATTERN_INDEX.md) | Complete pattern catalog |
| [../SKILL_USE_CASE_LOOKUP.md](../../SKILL_USE_CASE_LOOKUP.md) | Pattern selection by use case |
| [../SKILL_QUALITY_RUBRIC.md](../../SKILL_QUALITY_RUBRIC.md) | Quality scoring criteria |
| [../SKILL_PATTERN_INDEX.md](../../SKILL_PATTERN_INDEX.md) | Full skill building guide |

---

## Template Maintenance

These templates are living documents. When updating:

1. Keep templates aligned with patterns in `SKILL_PATTERN_INDEX.md`
2. Update examples when new production skills demonstrate better patterns
3. Add new sections discovered through real-world skill creation
4. Maintain consistency across all 6 templates

---

**Last Updated:** 2026-01-29
