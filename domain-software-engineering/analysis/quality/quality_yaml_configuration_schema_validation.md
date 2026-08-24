---
title: "YAML Configuration Schema Validation & Error Reporting"
category: code-analysis/quality
description: "Audit and improve YAML configuration schema validation including cross-field validation, error message quality, and migration strategies for config-driven systems"
tags:
  - quality
  - configuration
  - yaml
  - schema-validation
  - error-handling
  - config-driven
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-03  # Tool and Methodology Suggestions
  - QA-01  # Chain-of-Verification
  - QA-02  # Adversarial Stress-Test
  - OC-04  # Conditional Output Logic
difficulty: intermediate
version: "1.0"
updated: 2026-03-04
related_prompts:
  - ../architecture/architecture_config_driven_domain_modeling.md
  - quality_code_complexity_analysis.md
---

# YAML Configuration Schema Validation & Error Reporting

**Objective:** Audit a config-driven system's YAML schema validation for completeness, evaluating syntactic validation, semantic cross-field validation, error message quality, and config migration strategy — identifying configurations that pass validation but cause runtime failures.

**When to Use:** Use this prompt when a system is driven by YAML (or JSON) configuration files with complex schemas involving cross-references between sections, conditional required fields, and domain-specific value constraints. Particularly important when end users (not developers) write configuration files.

**Instructions:**

1. **Schema Inventory**

   Map every top-level configuration key:

   | Key | Type | Required | Default | Valid Values | Cross-References |
   |-----|------|----------|---------|--------------|-----------------|
   | `schedule.name` | string | yes | — | any | — |
   | `roles[].name` | string | yes | — | unique identifiers | Referenced by `constraints`, `patterns` |
   | `constraints.spacing.days` | int | yes | — | ≥ 1 | Must be < schedule horizon length |
   | `patterns.*.assignments` | map | yes | — | keys must be valid day names | Role values must exist in `roles` |

   **Find:**
   - Undocumented keys that the code silently accepts
   - Keys that are only validated at runtime (not at config load time)
   - Keys with ambiguous types (is `max_per_week: "2"` a string or int?)

2. **Validation Layer Architecture**

   ```
   Config Loading Pipeline (should be):
   ├── Layer 1: YAML Parsing
   │   └── Syntax errors → line number + column
   │
   ├── Layer 2: Schema Validation
   │   └── Type checking, required fields, enum values
   │   └── Tool: JSON Schema, Pydantic, Cerberus, or custom
   │
   ├── Layer 3: Semantic Validation
   │   └── Cross-field rules, value range checks
   │   └── Example: "spacing.days must be < (end_date - start_date)"
   │
   ├── Layer 4: Cross-Reference Validation
   │   └── All role names referenced in constraints exist in roles list
   │   └── All day names in patterns are valid for the configured week
   │
   └── Layer 5: Domain Validation
       └── Business rules specific to the industry
       └── Example: "healthcare requires at least one 'main' role"
   ```

   **Verify:**
   - Is YAML parsing separated from semantic validation?
   - Are parse errors reported with line numbers?
   - Is all validation performed before any scheduling logic runs?
   - Can the user get ALL validation errors at once (not fail on the first one)?

3. **Cross-Reference Validation**

   The most common source of config bugs in scheduling systems:

   ```yaml
   # This config is syntactically valid but semantically broken:
   roles:
     - name: "main"
     - name: "backup"

   constraints:
     weekly_limits:
       - role: "primary"      # ERROR: "primary" doesn't match any role name
         max_per_week: 1

   patterns:
     weekend_rotation:
       assignments:
         friday: "lead"       # ERROR: "lead" doesn't match any role name
   ```

   **Build a cross-reference map:**
   - Role names: defined in `roles[]`, referenced in `constraints`, `patterns`
   - Day names: defined by week configuration, referenced in `patterns`
   - Worker names: defined in database/roster, referenced in `unavailable_dates`
   - Plugin names: defined by available plugins, referenced in `constraints`

4. **Conditional Required Fields**

   Identify all "if A then B is required" relationships:

   ```yaml
   # If rotation pattern type is "rotating", then "rotation_rule" is required
   patterns:
     weekend_rotation:
       type: "rotating"
       rotation_rule: "alternate"  # Required when type=rotating

   # If role has "qualification" constraint, then workers must have
   # a "qualifications" field in their roster entry
   ```

   **For each conditional requirement:**
   - Is it enforced by the validator?
   - What error message appears when B is missing and A is set?
   - Is the condition documented in the config template comments?

5. **Error Message Quality Audit**

   Grade each validation error on 5 criteria:

   | Criterion | Good Example | Bad Example |
   |-----------|-------------|-------------|
   | **Field path** | `constraints.weekly_limits[0].role` | `invalid role` |
   | **Actual value** | `got "primary"` | (omitted) |
   | **Expected constraint** | `must be one of: "main", "backup"` | `invalid value` |
   | **Line number** | `line 15, column 9` | (omitted) |
   | **Fix suggestion** | `Did you mean "main"?` | (omitted) |

   **For each validation error in the system:**
   - Does it include all 5 criteria?
   - Is fuzzy matching used for likely typos? (`"primay"` → `Did you mean "primary"?`)
   - Are errors grouped by severity (error vs warning)?

6. **Adversarial Config Construction**

   Create 8 malformed configs that each test a different validation gap:

   | # | Deficiency | Malformed Config Snippet |
   |---|-----------|------------------------|
   | 1 | Missing cross-reference | Role referenced in constraint doesn't exist |
   | 2 | Type coercion | `max_per_week: "two"` (string instead of int) |
   | 3 | Out-of-range value | `min_gap_days: 0` (must be ≥ 1) |
   | 4 | Duplicate key | Two roles with same `name` |
   | 5 | Empty required section | `roles: []` |
   | 6 | Conditional missing | `type: rotating` without `rotation_rule` |
   | 7 | Circular reference | Pattern references itself |
   | 8 | Mutually exclusive | Both `fixed` and `rotating` type set |

   **For each: does the validator catch it? Is the error message actionable?**

7. **Config Migration Strategy**

   When the schema changes between versions:
   - Is there a schema version field in the config?
   - Can old configs be detected and auto-upgraded?
   - Are deprecated fields warned about before removal?
   - Is there a migration script or `--upgrade-config` CLI command?

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag the absence of JSON Schema as a deficiency if the system uses Pydantic or another validator — the tool choice is less important than the coverage
- Report "YAML allows duplicate keys" as a system bug — this is a YAML spec limitation, not the application's fault (but the application should detect it)
- Flag every undocumented key as a bug if it's an internal/advanced option with a sensible default
- Recommend schema validation libraries without checking Python version compatibility

✅ **DO:**
- Focus on configs that pass validation but cause runtime errors — these are the highest-priority gaps
- Check that the example/template configs included with the project actually pass validation
- Verify that error messages help users who are NOT developers (no stack traces in user-facing errors)
- Test with both minimal configs (only required fields) and maximal configs (every option set)

## Expected Output

1. **Schema Map** — Complete inventory of config keys with types, requirements, and cross-references
2. **Validation Layer Assessment** — Which layers exist, which are missing
3. **Cross-Reference Gaps** — References that aren't validated at config load time
4. **Error Message Report Card** — Grade each validation error on the 5-criteria scale
5. **Adversarial Test Results** — Pass/fail for each of the 8 malformed configs
6. **Migration Assessment** — Version handling and upgrade path status
7. **Recommendations** — Prioritized list of validation improvements

## Quality Checklist

- [ ] All config keys are inventoried with their validation rules
- [ ] Cross-references between config sections are mapped
- [ ] At least 5 adversarial configs are tested
- [ ] Error messages are graded on the 5-criteria scale
- [ ] Example/template configs pass validation

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on config validation completeness
- **ST-02** (Structured Sequential Instructions) — Layered validation audit from syntax to domain rules
- **RT-02** (Multi-Dimensional Analysis) — Covers syntax, semantics, cross-references, error quality, migration
- **DS-03** (Tool and Methodology Suggestions) — Recommends validation libraries and approaches
- **QA-01** (Chain-of-Verification) — Self-check: "Does this config actually pass validation?"
- **QA-02** (Adversarial Stress-Test) — Constructs malformed configs to expose validation gaps
- **OC-04** (Conditional Output Logic) — Handles case where validation is already comprehensive

## Related Prompts

- `architecture_config_driven_domain_modeling.md` — Higher-level review of config vs code boundary
- `quality_code_complexity_analysis.md` — Complexity analysis of the validation code itself
- `algorithms_temporal_logic_scheduling.md` — Temporal aspects of config (date formats, week definitions)
