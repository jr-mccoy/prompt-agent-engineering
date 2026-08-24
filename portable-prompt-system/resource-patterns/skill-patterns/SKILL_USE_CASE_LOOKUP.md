# Skill Use Case Lookup

> **Quick pattern selection by user intent.** Find the right skill structure, patterns, and resources for any use case.

---

## How to Use This Guide

1. **Identify the user's core need** from the use case categories below
2. **Find the matching row** for recommended patterns and structure
3. **Apply the patterns** from [SKILL_PATTERN_INDEX.md](SKILL_PATTERN_INDEX.md)
4. **Follow the pattern guides** in [SKILL_PATTERN_INDEX.md](SKILL_PATTERN_INDEX.md)

---

## Use Case Categories

### 1. Process Automation Skills

**User says:** "Help me automate...", "Set up a workflow for...", "Guide me through..."

| Use Case | Skill Type | Key Patterns | Recommended Structure |
|----------|-----------|--------------|----------------------|
| CI/CD pipeline setup | WORKFLOW | SP-02, WP-01, WP-02 | Numbered steps with validation |
| Deployment workflow | WORKFLOW | SP-02, WP-03, WP-04 | Steps with fallbacks and branches |
| Data pipeline creation | WORKFLOW | SP-02, WP-05, QP-01 | Freedom levels + validation pipeline |
| Environment setup | WORKFLOW | SP-02, WP-01, RP-03 | Steps + config templates |
| Release process | WORKFLOW | SP-02, WP-02, QP-06 | Steps + safety constraints |

**Template:**
```markdown
---
name: [process]-workflow
description: Guides through [process] with step-by-step procedures. Use when [triggers].
---

# [Process] Workflow

## Prerequisites
- [Required tool/access]

## Step 1: [First Phase]
**Purpose:** [What this accomplishes]
**Skip if:** [Skip condition]

[Instructions...]

**Validation:**
- [ ] [Check 1]

## Step 2: [Second Phase]
...

## Troubleshooting
| Issue | Solution |
|-------|----------|
| ... | ... |
```

---

### 2. Tool Mastery Skills

**User says:** "Help me use...", "How do I configure...", "What are the commands for..."

| Use Case | Skill Type | Key Patterns | Recommended Structure |
|----------|-----------|--------------|----------------------|
| CLI tool reference | TOOL | SP-03, IP-02, RP-02 | Operations + command reference |
| Configuration guide | TOOL | SP-03, RP-03, RP-04 | Reference + templates |
| Database operations | TOOL | SP-03, IP-01, QP-05 | Operations + edge cases |
| Build tool setup | TOOL | SP-03, WP-01, WP-03 | Operations with fallbacks |
| IDE/editor configuration | TOOL | SP-03, RP-03, WP-01 | Settings + step-by-step |

**Template:**
```markdown
---
name: [tool]-mastery
description: Master [tool] for [use cases]. Use when working with [contexts].
---

# [Tool] Mastery

## Overview
[What tool does, when to use it]

## Core Operations

### Operation: [Name]
**Command:**
```bash
[command syntax]
```
**Parameters:**
| Param | Description | Default |
|-------|-------------|---------|
| ... | ... | ... |

**Example:**
```bash
[real example]
```

## Configuration Reference
See `references/configuration.md`

## Troubleshooting
| Symptom | Cause | Solution |
|---------|-------|----------|
| ... | ... | ... |
```

---

### 3. Domain Expertise Skills

**User says:** "What are the requirements for...", "How do I comply with...", "Best practices for..."

| Use Case | Skill Type | Key Patterns | Recommended Structure |
|----------|-----------|--------------|----------------------|
| Compliance guidance | DOMAIN | SP-04, QP-05, QP-06 | Requirements + checklist |
| Security standards | DOMAIN | SP-04, QP-06, RP-07 | Standards + constraints |
| API design principles | DOMAIN | SP-04, IP-01, RP-02 | Principles + patterns |
| Architecture patterns | DOMAIN | SP-04, WP-04, RP-04 | Patterns + decision trees |
| Industry standards | DOMAIN | SP-04, QP-05, RP-02 | Standards + validation |

**Template:**
```markdown
---
name: [domain]-expertise
description: Expert knowledge for [domain]. Use when implementing [requirements] or ensuring [compliance].
---

# [Domain] Expertise

## Core Requirements

### Requirement 1: [Name]
**Standard:** [Reference]
**Implementation:** [How to satisfy]
**Common Violations:** [What to avoid]

## Implementation Patterns

### Pattern: [Name]
**When to use:** [Conditions]
**How to implement:**
```[language]
[code]
```

## Compliance Checklist
- [ ] [Requirement 1]
- [ ] [Requirement 2]
```

---

### 4. Content Creation Skills

**User says:** "Create a...", "Generate...", "Convert... to..."

| Use Case | Skill Type | Key Patterns | Recommended Structure |
|----------|-----------|--------------|----------------------|
| Document generation | CREATION | SP-05, RP-03, RP-01 | Input-process-output + templates |
| Code generation | CREATION | SP-05, MG-02, QP-01 | Templates + validation |
| Format conversion | CREATION | SP-05, RP-01, QP-05 | Process + edge cases |
| Report creation | CREATION | SP-05, RP-03, WP-02 | Templates + validation |
| Asset generation | CREATION | SP-05, RP-01, RP-03 | Scripts + output templates |

**Template:**
```markdown
---
name: [output]-creator
description: Generate [artifact type] from [inputs]. Use when creating [outputs].
---

# [Output] Creator

## Inputs
**Required:**
- [Input 1]: [Description]

**Optional:**
- [Input 2]: [Description, default: value]

## Generation Process

### Step 1: Validate Inputs
[Validation logic]

### Step 2: Generate Output
Use `scripts/generate.py`:
```bash
python scripts/generate.py --input file.txt
```

## Output Format
**Structure:** [What is produced]
**Validation:** [How to verify]
```

---

### 5. Troubleshooting Skills

**User says:** "Debug...", "Fix...", "Why is... failing", "Investigate..."

| Use Case | Skill Type | Key Patterns | Recommended Structure |
|----------|-----------|--------------|----------------------|
| Error diagnosis | ANALYSIS | SP-06, WP-04, QP-05 | Investigation + common issues |
| Performance debugging | ANALYSIS | SP-06, RP-01, WP-03 | Diagnostic scripts + fallbacks |
| Configuration issues | ANALYSIS | SP-06, IP-03, RP-04 | Issue database + grep patterns |
| Integration failures | ANALYSIS | SP-06, IP-03, RP-02 | Error handling + references |
| Security investigation | ANALYSIS | SP-06, QP-06, RP-07 | Safe procedures + constraints |

**Template:**
```markdown
---
name: [domain]-troubleshooting
description: Investigate and resolve [problem type]. Use when diagnosing [symptoms].
---

# [Domain] Troubleshooting

## Investigation Approach
**Philosophy:** Evidence-based, systematic investigation

## Diagnostic Tools
- [Tool 1]: [What it reveals]

## Common Issues

### Issue: [Symptom]
**Quick Diagnosis:**
```bash
[diagnostic command]
```
**Root Causes:**
1. [Cause A] - [Identification]
2. [Cause B] - [Identification]

**Resolution:**
```bash
[fix command]
```

## Deep Dive References
See `references/common_issues.md`
```

---

### 6. Integration Skills

**User says:** "Connect to...", "Integrate with...", "Use the API for..."

| Use Case | Skill Type | Key Patterns | Recommended Structure |
|----------|-----------|--------------|----------------------|
| REST API integration | INTEGRATION | IP-01, IP-03, IP-04 | Auth + operations + errors |
| GraphQL integration | INTEGRATION | IP-01, IP-02, RP-02 | Schema + operations + reference |
| Webhook handling | INTEGRATION | IP-01, WP-02, QP-05 | Setup + validation + edge cases |
| OAuth implementation | INTEGRATION | IP-05, WP-02, RP-02 | Flow + validation + reference |
| Service connections | INTEGRATION | IP-01, IP-03, QP-06 | Auth + operations + safety |

**Template:**
```markdown
---
name: [service]-integration
description: Integrate with [service] API. Use when connecting to [service] or automating [operations].
---

# [Service] Integration

## Authentication
```bash
export API_KEY="your-key-here"
```

## Core Operations

### Operation: [Name]
**Endpoint:** `POST /api/v1/resource`
**Request:**
```bash
curl -X POST -H "Authorization: Bearer $API_KEY" \
  -d '{"key": "value"}' \
  https://api.example.com/resource
```
**Response:**
```json
{"id": 123}
```

## Error Handling
| Code | Meaning | Resolution |
|------|---------|------------|
| 401 | Auth failed | Check API key |
| 429 | Rate limited | Implement backoff |

## Rate Limits
[Limits and best practices]
```

---

### 7. Meta/Generative Skills

**User says:** "Create a skill for...", "Build me a template for...", "Generate boilerplate..."

| Use Case | Skill Type | Key Patterns | Recommended Structure |
|----------|-----------|--------------|----------------------|
| Skill creation | META | MG-01, MG-02, QP-01 | Self-exemplifying + templates |
| Template generation | META | MG-02, RP-03, WP-02 | Templates + validation |
| Code scaffolding | META | MG-02, RP-01, RP-03 | Scripts + templates |
| Documentation generation | META | MG-04, RP-03, WP-02 | Templates + self-updating |
| Workflow composition | META | MG-03, SP-08, WP-04 | Composition + related skills |

**Template:**
```markdown
---
name: [artifact]-generator
description: Generate [artifacts] for [use cases]. Use when creating new [artifacts] or scaffolding [projects].
---

# [Artifact] Generator

## About [Artifacts]
[What they are, why they're useful]

## Generation Process

### Step 1: Gather Requirements
[Questions to ask]

### Step 2: Choose Template
**Option A:** [When to use]
**Option B:** [When to use]

### Step 3: Customize
Use `scripts/init.py`:
```bash
python scripts/init.py [name] --template [type]
```

## Template Structure
See `assets/[template-name]/` for complete template.

## Validation
Run `scripts/validate.py` to verify.
```

---

## Pattern Combinations by Complexity

### Simple Skills (Single Operation)

**Patterns:** SP-03, MP-01, QP-05

```markdown
---
name: simple-operation
description: Performs [operation]. Use when [trigger].
---

# Simple Operation

## When to Use
- [Trigger condition]

## Procedure
1. [Step 1]
2. [Step 2]

## Edge Cases
- [What to do when X]
```

---

### Medium Skills (Multi-Step Workflow)

**Patterns:** SP-02, WP-01, WP-02, RP-01

```markdown
---
name: multi-step-workflow
description: Guides through [workflow]. Use when [triggers].
---

# Multi-Step Workflow

## Prerequisites
- [Required items]

## Step 1: [Phase]
**Skip if:** [Condition]
[Instructions]
**Validation:** [Check]

## Step 2: [Phase]
...

## Scripts
- `scripts/helper.py` - [What it does]
```

---

### Complex Skills (Multi-Resource)

**Patterns:** SP-01, SP-07, RP-03, QP-01

```markdown
---
name: complex-skill
description: Comprehensive [capability]. Use when [triggers].
---

# Complex Skill

## Overview
[High-level description]

## Architecture
[How components fit together]

## Workflow

### Phase 1: [Name]
See `references/phase1_details.md` for deep dive.

[Core instructions]

### Phase 2: [Name]
Use `scripts/phase2.py`:
```bash
python scripts/phase2.py --input data.json
```

## Templates
Copy from `assets/templates/`

## Validation
Run `scripts/validate.py` after each phase.

## Reference Files
- `references/[name].md` - [Content]
- `scripts/[name].py` - [Purpose]
- `assets/[name]` - [What it provides]
```

---

### Meta Skills (Creates Other Artifacts)

**Patterns:** MG-01, MG-02, QP-01, WP-02

```markdown
---
name: meta-creator
description: Creates [artifacts]. Use when building new [artifacts].
---

# Meta Creator

## About [Artifacts]
[Self-referential description - skill demonstrates what it teaches]

## Creation Process

### Step 1: Understand Requirements
[Questions to clarify needs]

### Step 2: Choose Architecture
**If [condition]:** Use [pattern A]
**If [condition]:** Use [pattern B]

### Step 3: Generate Scaffold
```bash
python scripts/init.py [name] --template [type]
```

### Step 4: Customize
[Guidance on what to change]

### Step 5: Validate
```bash
python scripts/validate.py [path]
```

## Quality Checklist
- [ ] [Verification 1]
- [ ] [Verification 2]
```

---

## Quick Selection Matrix

| User Intent | Type | Patterns | Resources Needed |
|-------------|------|----------|------------------|
| "Automate process X" | WORKFLOW | SP-02, WP-01, WP-02 | scripts/ |
| "How to use tool X" | TOOL | SP-03, IP-02, RP-02 | references/ |
| "Requirements for X" | DOMAIN | SP-04, QP-05, QP-06 | references/ |
| "Generate/Create X" | CREATION | SP-05, RP-03, MG-02 | scripts/, assets/ |
| "Debug/Fix X" | ANALYSIS | SP-06, WP-04, QP-05 | scripts/, references/ |
| "Connect to X API" | INTEGRATION | IP-01, IP-03, IP-04 | references/ |
| "Create a skill for X" | META | MG-01, MG-02, QP-01 | scripts/, assets/ |

---

## Bundled Resource Quick Reference

### When to Add scripts/

| Situation | Add Script? | Type |
|-----------|-------------|------|
| Same code rewritten repeatedly | Yes | Automation |
| Complex multi-step validation | Yes | Validation |
| File format conversion | Yes | Processing |
| API interaction automation | Yes | Integration |
| One-time simple operation | No | - |

### When to Add references/

| Situation | Add Reference? | Type |
|-----------|----------------|------|
| API documentation needed | Yes | API reference |
| Large configuration tables | Yes | Config reference |
| Compliance requirements | Yes | Standards doc |
| Common error database | Yes | Troubleshooting |
| Brief explanations | No | - |

### When to Add assets/

| Situation | Add Asset? | Type |
|-----------|------------|------|
| Output templates needed | Yes | Templates |
| Boilerplate code to copy | Yes | Scaffolding |
| Images/icons for output | Yes | Static assets |
| Configuration examples | Yes | Config examples |
| Documentation-only content | No | - |

---

## Real-World Skill Examples

### Example 1: helm-chart-scaffolding
- **Type:** WORKFLOW + TOOL
- **Patterns:** SP-02, WP-01, RP-03, SP-07
- **Resources:** scripts/validate-chart.sh, assets/*.template

### Example 2: github-ops
- **Type:** INTEGRATION
- **Patterns:** IP-01, IP-02, IP-03, RP-02
- **Resources:** 5 reference files for API docs

### Example 3: skill-creator
- **Type:** META
- **Patterns:** MG-01, MG-02, QP-01, WP-01
- **Resources:** 4 scripts, template generation

### Example 4: cloudflare-troubleshooting
- **Type:** ANALYSIS
- **Patterns:** SP-06, WP-04, RP-01, QP-05
- **Resources:** 2 scripts, 3 references

### Example 5: pdf-creator
- **Type:** CREATION
- **Patterns:** SP-05, RP-01, QP-05
- **Resources:** 2 scripts for conversion

---

## Decision Flowchart

```
START: What does the user need?
│
├─→ A repeatable process?
│   └─→ WORKFLOW type
│       └─→ Patterns: SP-02, WP-01, WP-02
│
├─→ Tool/technology help?
│   └─→ TOOL type
│       └─→ Patterns: SP-03, IP-02, RP-02
│
├─→ Domain knowledge?
│   └─→ DOMAIN type
│       └─→ Patterns: SP-04, QP-05, QP-06
│
├─→ Generate something?
│   └─→ CREATION type
│       └─→ Patterns: SP-05, RP-03, MG-02
│
├─→ Debug/investigate?
│   └─→ ANALYSIS type
│       └─→ Patterns: SP-06, WP-04, QP-05
│
├─→ Connect to external service?
│   └─→ INTEGRATION type
│       └─→ Patterns: IP-01, IP-03, IP-04
│
└─→ Create other skills/templates?
    └─→ META type
        └─→ Patterns: MG-01, MG-02, QP-01
```

---

**Next steps:**
1. Identify user need in matrix above
2. Select skill type and patterns
3. Apply patterns from [SKILL_PATTERN_INDEX.md](SKILL_PATTERN_INDEX.md)
4. Build using [SKILL_PATTERN_INDEX.md](SKILL_PATTERN_INDEX.md)
5. Validate against [SKILL_QUALITY_RUBRIC.md](SKILL_QUALITY_RUBRIC.md)
