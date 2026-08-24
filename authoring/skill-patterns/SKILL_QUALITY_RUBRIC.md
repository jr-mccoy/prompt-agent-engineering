# Skill Quality Rubric

> **Scoring guide for Agent Skill quality assessment.** Use this rubric to evaluate skills before release or to identify improvement areas in existing skills.

---

## Quick Quality Score

**Calculate total score (0-100):**

| Category | Max Points | Your Score |
|----------|-----------|------------|
| [Metadata Quality](#1-metadata-quality-20-points) | 20 | ___ |
| [Structure Quality](#2-structure-quality-20-points) | 20 | ___ |
| [Content Quality](#3-content-quality-25-points) | 25 | ___ |
| [Resource Quality](#4-resource-quality-15-points) | 15 | ___ |
| [Safety & Reliability](#5-safety--reliability-20-points) | 20 | ___ |
| **TOTAL** | **100** | **___** |

**Score interpretation:**
- **90-100:** Production ready, exemplary skill
- **75-89:** Good quality, minor improvements possible
- **60-74:** Acceptable, needs polish before wide distribution
- **45-59:** Functional but significant issues
- **Below 45:** Requires substantial rework

---

## Detailed Scoring Criteria

### 1. Metadata Quality (20 points)

#### 1.1 Name Compliance (5 points)

| Criteria | Points | Check |
|----------|--------|-------|
| 1-64 characters | 1 | [ ] |
| Lowercase only | 1 | [ ] |
| Alphanumeric + hyphens only | 1 | [ ] |
| No leading/trailing/consecutive hyphens | 1 | [ ] |
| Matches directory name exactly | 1 | [ ] |

**Example scoring:**
```yaml
# 5/5
name: helm-chart-scaffolding

# 3/5 (uppercase, doesn't match directory)
name: Helm-Chart-Scaffolding

# 1/5 (too short, unclear, special chars)
name: hcs!
```

---

#### 1.2 Description Completeness (10 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Describes WHAT skill does (primary action) | 2 | [ ] |
| Describes WHEN to use (trigger conditions) | 2 | [ ] |
| Includes trigger phrases/keywords | 2 | [ ] |
| Uses third-person voice | 2 | [ ] |
| Length 50-500 characters (optimal) | 2 | [ ] |

**Scoring examples:**

```yaml
# 10/10 - Excellent
description: Extracts Mermaid diagrams from markdown files and generates high-quality PNG images using bundled scripts. Activates when working with Mermaid diagrams, converting diagrams to PNG, extracting diagrams from markdown, or processing markdown files with embedded Mermaid code.

# 7/10 - Good but missing triggers
description: Creates Helm charts for Kubernetes applications. Provides templates and validation for chart creation.

# 4/10 - Too vague
description: Handles Helm charts.

# 2/10 - Wrong voice, no context
description: Use this to make charts.
```

---

#### 1.3 Optional Metadata (5 points)

| Criteria | Points | Check |
|----------|--------|-------|
| License specified (if applicable) | 1 | [ ] |
| Compatibility noted (if constraints exist) | 2 | [ ] |
| allowed-tools defined (if tool-heavy) | 2 | [ ] |

**Example:**
```yaml
---
name: my-skill
description: ...
license: MIT
compatibility: Requires Python 3.10+, jq installed
allowed-tools: Bash(python:*) Bash(jq:*) Read Write
---
```

---

### 2. Structure Quality (20 points)

#### 2.1 Progressive Disclosure (8 points)

| Criteria | Points | Check |
|----------|--------|-------|
| SKILL.md < 500 lines | 2 | [ ] |
| Large content pushed to references/ | 2 | [ ] |
| Core instructions in SKILL.md | 2 | [ ] |
| Explicit references to bundled resources | 2 | [ ] |

**Scoring:**
```
# 8/8 - SKILL.md is 150 lines, references detailed API docs
## API Reference
For complete endpoint documentation, see `references/api_docs.md`.

# 4/8 - All content crammed into 800-line SKILL.md
[No references/, everything inline]

# 2/8 - References exist but never mentioned
references/
├── api.md  # Never referenced in SKILL.md
```

---

#### 2.2 Section Organization (6 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Clear "When to Use" section | 1 | [ ] |
| Clear "When NOT to Use" section | 1 | [ ] |
| Logical section ordering | 2 | [ ] |
| Related Skills section | 2 | [ ] |

**Scoring examples:**

```markdown
# 6/6 - All sections present, logical flow
## When to Use This Skill
- [Clear triggers]

## When NOT to Use This Skill
- [Clear exclusions]

## [Main Content]
...

## Related Skills
- `related-skill` - [Relationship]
```

---

#### 2.3 Directory Structure (6 points)

| Criteria | Points | Check |
|----------|--------|-------|
| SKILL.md exists at root | 2 | [ ] |
| No nested skill directories | 1 | [ ] |
| Resource directories correctly named | 1 | [ ] |
| No extraneous files | 2 | [ ] |

**Correct structure:**
```
skill-name/
├── SKILL.md              # Required, at root
├── scripts/              # If used
├── references/           # If used
└── assets/               # If used
```

**Incorrect:**
```
skill-name/
├── skill.md              # Wrong casing
├── SKILL.md
├── sub-skill/            # No nesting
│   └── SKILL.md
└── random-notes.txt      # Extraneous
```

---

### 3. Content Quality (25 points)

#### 3.1 Actionability (10 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Instructions are imperative/actionable | 3 | [ ] |
| Steps can be executed by agent | 3 | [ ] |
| Code examples are complete and runnable | 2 | [ ] |
| Commands include all necessary context | 2 | [ ] |

**Scoring examples:**

```markdown
# 10/10 - Clear, actionable, complete
### Step 1: Validate the Chart

Run the validation script:
```bash
./scripts/validate-chart.sh ./my-chart
```

Expected output:
```
✓ Linting passed
✓ Template rendering successful
```

If validation fails, check the error message and fix accordingly.

# 5/10 - Vague, incomplete
### Validation
You should validate your chart. There are several ways to do this.
Generally you want to make sure it works.
```

---

#### 3.2 Completeness (8 points)

| Criteria | Points | Check |
|----------|--------|-------|
| All referenced resources exist | 2 | [ ] |
| Edge cases documented | 2 | [ ] |
| Error handling described | 2 | [ ] |
| Prerequisites stated | 2 | [ ] |

**Checklist:**
- [ ] Every `scripts/name.py` mentioned in SKILL.md exists
- [ ] Every `references/name.md` mentioned exists
- [ ] Every `assets/name` mentioned exists
- [ ] "If this fails" scenarios covered
- [ ] Prerequisites/dependencies listed

---

#### 3.3 Accuracy (7 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Commands work as documented | 3 | [ ] |
| Code examples are syntactically correct | 2 | [ ] |
| Technical information is current | 2 | [ ] |

**Verification:**
- Run all documented commands
- Validate all code snippets
- Check API endpoints still exist
- Verify version compatibility claims

---

### 4. Resource Quality (15 points)

#### 4.1 Script Quality (6 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Scripts have docstrings/usage info | 2 | [ ] |
| Scripts validate inputs | 2 | [ ] |
| Scripts emit clear errors | 2 | [ ] |

**Good script:**
```python
#!/usr/bin/env python3
"""
Validate skill structure.

Usage:
    validate.py <skill-path>

Example:
    validate.py ./my-skill
"""

def validate(path):
    """Validate skill at given path."""
    if not path.exists():
        raise ValueError(f"Path does not exist: {path}")
```

**Bad script:**
```python
# No docstring, no validation
def go(p):
    do_stuff(p)
```

---

#### 4.2 Reference Quality (5 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Filenames are self-explanatory | 2 | [ ] |
| Content is well-organized | 2 | [ ] |
| References are actually referenced | 1 | [ ] |

**Good filenames:**
- `api_endpoints.md`
- `database_schema.md`
- `troubleshooting_guide.md`

**Bad filenames:**
- `reference.md`
- `docs.md`
- `info.md`

---

#### 4.3 Asset Quality (4 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Templates are immediately usable | 2 | [ ] |
| Examples match documentation | 2 | [ ] |

**Good template:**
```yaml
# assets/Chart.yaml.template
apiVersion: v2
name: {{ .Chart.Name }}       # User customizes
description: {{ .Description }}
version: 1.0.0
```

---

### 5. Safety & Reliability (20 points)

#### 5.1 Security (10 points)

| Criteria | Points | Check |
|----------|--------|-------|
| No hardcoded secrets | 3 | [ ] |
| No absolute user paths | 2 | [ ] |
| No personal/company information | 2 | [ ] |
| Environment variables for sensitive data | 3 | [ ] |

**Security scan checklist:**
- [ ] No API keys, passwords, tokens
- [ ] No `/home/username/` or `/Users/username/` paths
- [ ] No company names, product names
- [ ] Secrets use `os.environ.get()` pattern

---

#### 5.2 Safety Constraints (5 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Destructive operations have confirmations | 2 | [ ] |
| Safety warnings clearly documented | 2 | [ ] |
| Reversibility mentioned where applicable | 1 | [ ] |

**Good safety documentation:**
```markdown
## Safety & Constraints

**NEVER:**
- Run destructive commands without --dry-run first
- Delete production resources without explicit confirmation

**ALWAYS:**
- Use --dry-run mode for initial testing
- Confirm before irreversible actions
```

---

#### 5.3 Failure Handling (5 points)

| Criteria | Points | Check |
|----------|--------|-------|
| Failure modes documented | 2 | [ ] |
| Recovery procedures provided | 2 | [ ] |
| Partial success handling described | 1 | [ ] |

**Good failure handling:**
```markdown
## Troubleshooting

### Issue: Validation fails
**Cause:** Missing required field in Chart.yaml
**Fix:** Add required field, re-run validation

### Issue: Partial deployment
**Cause:** Network timeout during apply
**Recovery:**
1. Check which resources were created: `kubectl get all`
2. Re-run deployment: `helm upgrade --install`
```

---

## Quick Checklist (Pre-Release)

### Must Pass (Blocking)

- [ ] Name matches folder name
- [ ] Description describes WHAT and WHEN
- [ ] SKILL.md exists and is valid YAML frontmatter + markdown
- [ ] All referenced files exist
- [ ] No hardcoded secrets or absolute paths
- [ ] Instructions are actionable by an agent

### Should Pass (Quality)

- [ ] SKILL.md < 500 lines
- [ ] "When to Use" and "When NOT to Use" sections exist
- [ ] Related Skills section included
- [ ] Edge cases documented
- [ ] Scripts have docstrings and input validation

### Nice to Have (Polish)

- [ ] Examples for all operations
- [ ] Troubleshooting section
- [ ] Complete compatibility information
- [ ] License specified

---

## Automated Validation Commands

If scripts are available:

```bash
# Structure validation
python scripts/quick_validate.py <skill-path>

# Security scan
python scripts/security_scan.py <skill-path>

# Full validation (structure + security)
python scripts/package_skill.py <skill-path>
```

**Exit codes:**
- `0` - Passed
- `1` - High severity issues
- `2` - Critical issues (must fix)
- `3` - Tool missing
- `4` - Scan error

---

## Common Deductions

| Issue | Points Lost | Category |
|-------|-------------|----------|
| Name doesn't match folder | -5 | Metadata |
| Description under 50 chars | -4 | Metadata |
| No trigger phrases | -3 | Metadata |
| SKILL.md over 500 lines | -4 | Structure |
| Referenced file doesn't exist | -5 | Content |
| Vague instructions | -5 | Content |
| Hardcoded secrets | -10 | Safety |
| Absolute user paths | -5 | Safety |
| No error handling docs | -3 | Safety |
| Scripts without docstrings | -3 | Resources |

---

## Score Examples

### Example 1: Excellent Skill (95/100)

```
Metadata: 20/20
- Name perfect, description complete with triggers
- License and compatibility noted

Structure: 19/20
- Progressive disclosure perfect
- Missing "When NOT to Use" (-1)

Content: 24/25
- Highly actionable
- Minor edge case not covered (-1)

Resources: 15/15
- Scripts well-documented
- References properly named
- Templates immediately usable

Safety: 17/20
- Security clean
- Safety constraints documented
- Partial success handling missing (-3)

TOTAL: 95/100 - Production ready
```

### Example 2: Needs Work (62/100)

```
Metadata: 12/20
- Name correct
- Description too short, no triggers (-5)
- No compatibility info (-3)

Structure: 14/20
- All in SKILL.md, no references (-4)
- Related Skills missing (-2)

Content: 18/25
- Instructions vague in places (-4)
- Referenced script missing (-3)

Resources: 8/15
- Scripts lack docstrings (-3)
- Bad reference filenames (-2)
- No assets despite needing templates (-2)

Safety: 10/20
- Contains absolute path (-5)
- No safety constraints documented (-3)
- No failure handling (-2)

TOTAL: 62/100 - Needs polish before distribution
```

---

## Improvement Prioritization

When improving a low-scoring skill, address issues in this order:

1. **Critical (must fix):** Security issues, missing referenced files
2. **High (should fix):** Vague instructions, missing triggers in description
3. **Medium (improve):** Missing sections, poor structure
4. **Low (polish):** Formatting, additional examples

**Target score for release: 75+**

---

## Self-Review Template

```markdown
## Skill Self-Review: [skill-name]

**Date:** [date]
**Reviewer:** [agent/person]

### Metadata Quality: ___/20
- [ ] Name compliance (5)
- [ ] Description completeness (10)
- [ ] Optional metadata (5)

### Structure Quality: ___/20
- [ ] Progressive disclosure (8)
- [ ] Section organization (6)
- [ ] Directory structure (6)

### Content Quality: ___/25
- [ ] Actionability (10)
- [ ] Completeness (8)
- [ ] Accuracy (7)

### Resource Quality: ___/15
- [ ] Script quality (6)
- [ ] Reference quality (5)
- [ ] Asset quality (4)

### Safety & Reliability: ___/20
- [ ] Security (10)
- [ ] Safety constraints (5)
- [ ] Failure handling (5)

### TOTAL: ___/100

### Top 3 Issues to Address:
1. [Issue and fix]
2. [Issue and fix]
3. [Issue and fix]
```
