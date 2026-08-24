# Gold Standard Skill: Annotated Example

> **Line-by-line explanation of a well-crafted skill.** Use this as a reference when building new skills.

---

## The Complete Example

Below is a complete, production-ready skill with inline annotations explaining each element.

---

## Directory Structure

```
config-validator/                    # ← Name matches frontmatter exactly
├── SKILL.md                        # ← Required, at root level
├── scripts/                        # ← Executable automation
│   ├── validate_config.py          # ← Self-documenting script
│   └── fix_common_issues.py        # ← Remediation helper
├── references/                     # ← Deep documentation
│   ├── schema_reference.md         # ← Self-explanatory filename
│   └── error_codes.md              # ← Organized error database
└── assets/                         # ← Output resources
    ├── config.example.yaml         # ← Working example
    └── config.schema.json          # ← Validation schema
```

---

## SKILL.md (Annotated)

```yaml
# ═══════════════════════════════════════════════════════════════════════════
# YAML FRONTMATTER - Machine-parsed metadata for discovery
# ═══════════════════════════════════════════════════════════════════════════

---
name: config-validator
# ↑ REQUIRED: 1-64 chars, lowercase, alphanumeric + hyphens
# ↑ MUST match directory name exactly
# ↑ No leading/trailing/consecutive hyphens

description: Validates YAML and JSON configuration files against schemas with detailed error reporting and automatic fix suggestions. Use this skill when checking configuration syntax, validating against schemas, debugging config errors, or when users mention "config validation", "schema check", "invalid config", or "fix my config file".
# ↑ REQUIRED: 1-1024 characters
# ↑ Pattern: [WHAT it does] + [WHEN to use] + [TRIGGER phrases]
# ↑ Third-person voice: "This skill should be used when..."
# ↑ Includes keywords: validation, schema, config, YAML, JSON
# ↑ Includes trigger phrases: "fix my config file"

license: MIT
# ↑ OPTIONAL: License for distribution

compatibility: Requires Python 3.8+, jsonschema package
# ↑ OPTIONAL: Environment constraints
---
```

```markdown
# ═══════════════════════════════════════════════════════════════════════════
# MARKDOWN BODY - Agent-executable instructions
# ═══════════════════════════════════════════════════════════════════════════

# Config Validator
# ↑ Title matches skill name (human-readable form)

Validates configuration files against schemas with detailed error reporting and automatic fix suggestions.
# ↑ Brief overview: 1-2 sentences restating purpose

## Purpose
# ↑ SP-04: Explains WHY this skill exists

This skill ensures configuration files are syntactically correct and conform to required schemas before deployment. It prevents deployment failures caused by misconfiguration.
# ↑ Problem being solved + benefit provided

## When to Use This Skill
# ↑ MP-03: Specific scope boundaries (POSITIVE)

Use this skill when you need to:
- Validate YAML or JSON configuration files
- Check configs against a JSON Schema
- Debug configuration errors with detailed messages
- Get automatic fix suggestions for common issues
- Ensure configs are deployment-ready
# ↑ Clear trigger conditions as bullet list

## When NOT to Use This Skill
# ↑ MP-03: Specific scope boundaries (NEGATIVE)

Do NOT use this skill when:
- Working with non-config file formats (use appropriate format skill)
- The file is code, not configuration (use linting skills)
- You need to generate configs from scratch (use config-generator skill)
# ↑ Prevents over-activation by excluding wrong use cases

## Prerequisites
# ↑ WP-02: State requirements upfront

- Python 3.8+
- `jsonschema` package: `pip install jsonschema`
- `pyyaml` package: `pip install pyyaml`

## Quick Start
# ↑ SP-02: Numbered workflow starts here

### Step 1: Validate Basic Syntax
# ↑ Each step has clear purpose

**Purpose:** Check that the file is valid YAML/JSON before schema validation.

**Skip if:** You've already verified syntax is correct.
# ↑ WP-01: Skip conditions documented

```bash
# For YAML
python scripts/validate_config.py config.yaml --syntax-only

# For JSON
python scripts/validate_config.py config.json --syntax-only
```
# ↑ Complete, runnable commands with context

**Expected output:**
```
✓ Syntax valid: config.yaml
```

**If this fails:**
# ↑ WP-03: Fallback procedures
1. Check error message for line number
2. Fix syntax at indicated line
3. Re-run validation

### Step 2: Validate Against Schema
# ↑ Next step in workflow

**Purpose:** Ensure configuration meets all schema requirements.

```bash
python scripts/validate_config.py config.yaml --schema assets/config.schema.json
```

**Output on success:**
```
✓ Schema validation passed
  - All required fields present
  - All types correct
  - 0 warnings
```

**Output on failure:**
```
✗ Schema validation failed: 3 errors

Error 1: Missing required field
  Path: $.database.host
  Expected: string
  Fix: Add 'host' field under 'database' section

Error 2: Invalid type
  Path: $.server.port
  Expected: integer
  Got: string "8080"
  Fix: Remove quotes around port number
```
# ↑ Real error examples help agent understand output

### Step 3: Apply Automatic Fixes (Optional)
# ↑ WP-05: Optional step clearly marked

**Purpose:** Automatically fix common configuration issues.

**Freedom level:** Medium
# ↑ WP-05: How much discretion agent has
- Script fixes known patterns safely
- User should review changes before applying

```bash
# Preview fixes without applying
python scripts/fix_common_issues.py config.yaml --dry-run

# Apply fixes
python scripts/fix_common_issues.py config.yaml --apply
```

**Validation:**
# ↑ WP-02: Validation checkpoint
- [ ] Review diff of proposed changes
- [ ] Confirm fixes match expected behavior
- [ ] Re-run Step 2 to verify fixes resolved issues

## Common Issues
# ↑ SP-06: Investigation-focused troubleshooting section

### Issue: "Failed to parse YAML"
# ↑ QP-05: Edge case documentation

**Quick Diagnosis:**
```bash
python scripts/validate_config.py config.yaml --verbose
```

**Root Causes:**
1. Incorrect indentation (most common)
2. Missing quotes around special characters
3. Tab characters instead of spaces

**Resolution:**
```bash
# Check for tabs
grep -P '\t' config.yaml

# Fix indentation (convert tabs to spaces)
sed -i 's/\t/  /g' config.yaml
```

### Issue: "Schema not found"

**Quick Diagnosis:**
```bash
ls -la assets/*.schema.json
```

**Resolution:**
1. Verify schema file path is correct
2. Check schema file exists in assets/
3. Use absolute path if relative path fails

## Deep Dive References
# ↑ SP-07: Cross-references to bundled resources

For detailed documentation:
- **Schema specification:** See `references/schema_reference.md`
- **Error code meanings:** See `references/error_codes.md`
- **Example configs:** See `assets/config.example.yaml`
# ↑ RP-04: Grep patterns for large references would go here if >10k words

## Safety & Constraints
# ↑ QP-06: Explicit safety documentation

**NEVER:**
- Modify original config without backup
- Apply fixes without --dry-run preview first
- Ignore validation warnings in production configs

**ALWAYS:**
- Create backup before applying fixes: `cp config.yaml config.yaml.bak`
- Review all proposed changes before applying
- Re-validate after any modifications

## Reference Files
# ↑ SP-07: Complete resource manifest

| Resource | Purpose |
|----------|---------|
| `scripts/validate_config.py` | Main validation script |
| `scripts/fix_common_issues.py` | Automatic fix application |
| `references/schema_reference.md` | Complete schema documentation |
| `references/error_codes.md` | Error code lookup table |
| `assets/config.schema.json` | JSON Schema for validation |
| `assets/config.example.yaml` | Working example configuration |

## Related Skills
# ↑ SP-08: Connections to other skills

- `config-generator` - Generate new configs from templates
- `yaml-tools` - Advanced YAML manipulation
- `json-schema-designer` - Create custom schemas
- `deployment-validator` - Full deployment readiness check
```

---

## Bundled Resources (Annotated)

### scripts/validate_config.py

```python
#!/usr/bin/env python3
# ↑ Shebang for direct execution

"""
Config Validator - Validate YAML/JSON against schemas

Usage:
    validate_config.py <config-file> [options]

Options:
    --syntax-only       Check syntax without schema validation
    --schema <path>     JSON Schema file for validation
    --verbose           Show detailed error information

Examples:
    validate_config.py config.yaml --syntax-only
    validate_config.py config.yaml --schema schema.json
    validate_config.py config.json --schema schema.json --verbose

"""
# ↑ RP-01: Complete docstring with usage, options, examples

import sys
import json
import argparse
from pathlib import Path

# ↑ Standard library imports only for portability

def validate_syntax(file_path: Path) -> tuple[bool, str]:
    """
    Validate file syntax (YAML or JSON).

    Args:
        file_path: Path to configuration file

    Returns:
        Tuple of (is_valid, message)
    """
    # ↑ RP-01: Function docstrings with Args/Returns

    if not file_path.exists():
        return False, f"File not found: {file_path}"
    # ↑ RP-05: Input validation with clear error

    # ... implementation ...


def main():
    """Main entry point with argument parsing."""

    parser = argparse.ArgumentParser(
        description="Validate configuration files against schemas"
    )
    parser.add_argument("config_file", help="Path to config file")
    parser.add_argument("--syntax-only", action="store_true",
                       help="Check syntax only")
    parser.add_argument("--schema", help="Path to JSON Schema")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Show detailed output")

    args = parser.parse_args()
    # ↑ QP-04: CLI supports verbose mode

    config_path = Path(args.config_file)
    if not config_path.exists():
        print(f"❌ Error: File not found: {config_path}")
        sys.exit(1)
    # ↑ RP-05: Early validation, clear errors

    # ... implementation ...

if __name__ == "__main__":
    main()
```

---

### references/error_codes.md

```markdown
# Error Codes Reference
# ↑ RP-02: Self-explanatory filename

## Error Categories

| Code Range | Category | Description |
|------------|----------|-------------|
| E001-E099 | Syntax | File parsing errors |
| E100-E199 | Schema | Schema validation errors |
| E200-E299 | Type | Type mismatch errors |

## Detailed Error Codes

### E001: Invalid YAML Syntax

**Message:** `Failed to parse YAML at line {n}`

**Causes:**
- Incorrect indentation
- Missing colons
- Invalid characters

**Resolution:**
1. Check line indicated in error
2. Verify indentation uses spaces (not tabs)
3. Ensure proper YAML syntax

### E101: Missing Required Field
# ↑ Organized by category, searchable

...
```
# ↑ Structure allows grep for specific codes

---

### assets/config.example.yaml

```yaml
# Example Configuration
# ↑ RP-03: Immediately usable template

# Copy this file and customize for your environment
# Required fields are marked with [REQUIRED]

server:
  host: localhost        # [REQUIRED] Server hostname
  port: 8080            # [REQUIRED] Port number (integer)
  timeout: 30           # Optional: Request timeout in seconds

database:
  host: db.example.com  # [REQUIRED] Database hostname
  port: 5432            # [REQUIRED] Database port
  name: myapp           # [REQUIRED] Database name
  # credentials:        # Use environment variables instead
  #   user: $DB_USER
  #   password: $DB_PASSWORD

logging:
  level: info           # Options: debug, info, warn, error
  format: json          # Options: json, text
```
# ↑ Comments explain each field, marks required vs optional
# ↑ Shows secure credential handling pattern

---

## Quality Score Breakdown

This example skill scores **96/100**:

| Category | Score | Notes |
|----------|-------|-------|
| Metadata Quality | 20/20 | Name, description, license, compatibility all present |
| Structure Quality | 20/20 | Progressive disclosure, all sections, proper directory |
| Content Quality | 24/25 | Minor: could add one more edge case (-1) |
| Resource Quality | 15/15 | Scripts documented, references named well, assets usable |
| Safety & Reliability | 17/20 | Missing: partial success handling (-3) |

---

## Key Patterns Demonstrated

| Pattern | Location | Example |
|---------|----------|---------|
| SP-01: Progressive Disclosure | Overall | Core in SKILL.md, details in references/ |
| SP-02: Numbered Steps | Quick Start | Step 1, Step 2, Step 3 |
| SP-06: Investigation Flow | Common Issues | Symptom → Diagnosis → Resolution |
| SP-07: Cross-References | Deep Dive | "See `references/...`" |
| SP-08: Related Skills | Bottom | Links to 4 related skills |
| MP-01: Trigger Phrases | Description | "fix my config file" |
| MP-03: Scope Boundaries | When to Use/NOT | Clear positive and negative |
| WP-01: Skip Conditions | Step 1 | "Skip if you've already verified..." |
| WP-02: Validation Checkpoints | Step 3 | Checklist before proceeding |
| WP-03: Fallback Procedures | Step 1 | "If this fails:" section |
| WP-05: Freedom Levels | Step 3 | "Freedom level: Medium" |
| RP-01: Script Documentation | validate_config.py | Full docstrings, examples |
| RP-02: Self-Describing Names | references/ | error_codes.md, not "codes.md" |
| RP-03: Usable Templates | assets/ | config.example.yaml |
| QP-05: Edge Cases | Common Issues | Two issues with full diagnosis |
| QP-06: Safety Constraints | Safety section | NEVER/ALWAYS lists |

---

## Using This Template

1. **Copy the structure** - Use directory layout as starting point
2. **Replace placeholders** - Swap `config-validator` for your skill name
3. **Adapt content** - Keep patterns, change domain content
4. **Validate** - Run through quality rubric
5. **Iterate** - Use with real tasks, refine based on failures

---

## Anti-Patterns to Avoid

| Bad Pattern | Problem | Fix |
|-------------|---------|-----|
| `description: Validates configs.` | Too short, no triggers | Add WHAT + WHEN + triggers |
| All content in SKILL.md | Context bloat | Push to references/ |
| `references/docs.md` | Vague filename | Use `error_codes.md` |
| No "When NOT to Use" | Over-activation | Add exclusion conditions |
| Vague: "generally you want to..." | Not actionable | Use imperative commands |
| No validation checkpoints | Failures cascade | Add after each major step |
| No related skills | Isolated | Link complementary skills |
