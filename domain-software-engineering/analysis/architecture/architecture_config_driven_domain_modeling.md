---
title: "Configuration-Driven Domain Modeling Review"
category: code-analysis/architecture
description: "Review the boundary between configuration and code in config-driven systems, assessing schema complexity, config debugging, and preventing configuration from becoming an undebuggable DSL"
tags:
  - architecture
  - configuration
  - domain-modeling
  - yaml
  - dsl
  - complexity
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-03  # Tree of Thoughts
  - RT-05  # Evidence-Based Reasoning
  - DS-01  # Framework Application
difficulty: intermediate
version: "1.0"
updated: 2026-03-04
related_prompts:
  - ../quality/quality_yaml_configuration_schema_validation.md
  - architecture_plugin_constraint_system.md
  - architecture_coupling_cohesion_analysis.md
---

# Configuration-Driven Domain Modeling Review

**Objective:** Evaluate the boundary between configuration and code in a config-driven system, identifying where configuration complexity is appropriate, where it has grown beyond what YAML can reasonably express, and whether users can understand, debug, and evolve their configurations without developer assistance.

**When to Use:** Use this prompt when a system's behavior is primarily controlled by configuration files (YAML, JSON, TOML) rather than code. Applicable to scheduling systems, workflow engines, rules-based systems, and any application where end users define behavior through structured configuration.

**Instructions:**

1. **Config vs Code Boundary Analysis**

   For every configurable behavior, classify:

   ```
   Classification Spectrum:
   ├── SHOULD be config (data that changes per deployment)
   │   ├── Worker names and roster
   │   ├── Date ranges
   │   ├── Role names and display labels
   │   ├── Simple numeric thresholds (min_gap: 2, max_per_week: 1)
   │   └── Feature toggles (enable_rebalancing: true)
   │
   ├── GRAY ZONE (could be either)
   │   ├── Constraint types and parameters
   │   ├── Rotation patterns (FSF/SFS)
   │   ├── Scoring weights
   │   └── Custom day type definitions
   │
   └── SHOULD be code (logic that requires testing/debugging)
       ├── Constraint evaluation logic
       ├── Backtracking algorithm parameters
       ├── Export format rendering
       └── Conditional rules with dependencies ("if X then Y unless Z")
   ```

   **Warning signs that config has crossed into code territory:**
   - Config files contain conditional logic (`if:`, `when:`, `unless:`)
   - Config references other config values dynamically
   - Users need to understand execution order to write correct config
   - Config errors only manifest at runtime, not at validation time
   - You find yourself building a "config debugger"

2. **Schema Complexity Assessment**

   Measure the complexity of the configuration schema:

   | Metric | Healthy | Warning | Critical |
   |--------|---------|---------|----------|
   | Nesting depth | ≤ 3 levels | 4 levels | 5+ levels |
   | Total keys | ≤ 30 | 31-60 | 60+ |
   | Cross-references | ≤ 5 | 6-10 | 10+ |
   | Conditional required | ≤ 3 | 4-6 | 6+ |
   | Config file lines | ≤ 100 | 101-200 | 200+ |

   **For each metric in the "Warning" or "Critical" zone:**
   - Is the complexity necessary, or can it be simplified?
   - Can defaults reduce what users need to specify?
   - Can complex sections be split into separate files?

3. **User Mental Model Test**

   **Can a non-developer user (nurse manager, store manager) answer these questions about their config?**

   - "What happens if I change `min_gap` from 2 to 3?" → Clear, predictable effect
   - "Why did Worker A get assigned to Saturday?" → Traceable through config rules
   - "How do I add a new constraint type?" → Documented, follows a pattern
   - "What does `rotation_rule: alternate` mean?" → Explained in comments or docs

   **If the answer to any question is "they'd need to read the source code" — the config has outgrown its documentation.**

4. **Default Value Strategy**

   ```yaml
   # GOOD: Sensible defaults with minimal required fields
   schedule:
     name: "My Schedule"           # Required
     # week_start: "monday"        # Default: monday
     # scoring_weights:            # Default: equal weights
     #   fairness: 0.25
     #   coverage: 0.25
     #   balance: 0.25
     #   gap: 0.25

   # BAD: Everything required, no defaults
   schedule:
     name: "My Schedule"
     week_start: "monday"         # Why do I have to specify this?
     scoring_weights:
       fairness: 0.25             # Why do I have to specify these?
       coverage: 0.25
       balance: 0.25
       gap: 0.25
   ```

   **Verify:**
   - Are defaults documented (in comments, template, or reference docs)?
   - Are defaults applied consistently (not sometimes in code, sometimes in config)?
   - Is there a command to dump the "effective config" (user values + defaults)?

5. **Config Composition and Inheritance**

   For systems with multiple config variants (healthcare vs retail vs emergency):

   ```yaml
   # Pattern 1: Template inheritance
   extends: "templates/healthcare_base.yaml"
   overrides:
     constraints:
       min_gap: 3  # Override base template's value of 2

   # Pattern 2: Config fragments
   includes:
     - "constraints/healthcare_standard.yaml"
     - "roles/pacu_roles.yaml"
     - "patterns/weekend_rotation.yaml"

   # Pattern 3: Flat, no composition (simplest)
   # Everything in one file per deployment
   ```

   **Evaluate:**
   - Is composition needed, or is copy-paste-customize sufficient?
   - If inheritance is used, can the user see the "effective config" after merging?
   - Are override rules clear? (Last-wins? Deepmerge? Explicit?)

6. **Config Debugging Tooling**

   What tools exist for users to understand their config?

   | Tool | Purpose | Exists? |
   |------|---------|---------|
   | `--validate-config` | Check for errors without running | ? |
   | `--dump-effective-config` | Show config after defaults and merges | ? |
   | `--dry-run` | Show what the schedule WOULD look like | ? |
   | `--explain-assignment` | Why was Worker A assigned to Monday? | ? |
   | Config diff | Compare two configs | ? |

   **Priority: `--validate-config` and `--dump-effective-config` should exist before any other tooling.**

7. **Industry Template Review**

   For each example configuration provided:

   | Template | Target User | Lines | Complexity | Documented? |
   |----------|-------------|-------|------------|-------------|
   | `pacu_call.yaml` | Nurse manager | ? | ? | Comments? |
   | `store_shifts.yaml` | Store manager | ? | ? | Comments? |
   | `fire_24_48.yaml` | Fire chief | ? | ? | Comments? |

   **For each template:**
   - Can the target user modify it without developer help?
   - Are all non-obvious fields commented?
   - Is there a "getting started" section that shows only the minimal changes needed?

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag all configuration complexity as "should be code" — the entire value proposition of config-driven systems is that behavior is configurable
- Insist on config inheritance if there are fewer than 3 distinct deployment configurations — copy-paste is simpler
- Recommend moving constraint definitions to code just because they're complex — the plugin system exists to make constraints configurable
- Flag deep nesting as always bad — some domains (scheduling patterns with nested rotations) genuinely need 3-4 levels

✅ **DO:**
- Identify specific config values that users cannot understand without reading source code
- Check whether the example templates can be modified by the stated target user
- Verify that config errors are caught at validation time, not at runtime
- Test the "minimal viable config" — what's the smallest config that produces a valid schedule?

## Expected Output

1. **Boundary Classification** — Table of every configurable behavior with config/code/gray classification
2. **Complexity Scorecard** — Schema metrics with health assessment
3. **User Mental Model Assessment** — Can target users answer the test questions?
4. **Default Strategy Report** — Coverage and documentation of defaults
5. **Tooling Inventory** — What debugging tools exist and what's missing
6. **Template Review** — Per-template usability assessment
7. **Recommendations** — Specific suggestions to simplify config or improve tooling

## Quality Checklist

- [ ] Every configurable behavior is classified (config / code / gray zone)
- [ ] Schema complexity metrics are measured
- [ ] At least one industry template is reviewed for user-friendliness
- [ ] Default values are inventoried
- [ ] Config debugging tooling is assessed

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on config vs code boundary analysis
- **ST-02** (Structured Sequential Instructions) — Systematic review from boundary to tooling
- **RT-02** (Multi-Dimensional Analysis) — Covers boundary, complexity, usability, defaults, tooling, templates
- **RT-03** (Tree of Thoughts) — Explores multiple valid positions on the config/code spectrum
- **RT-05** (Evidence-Based Reasoning) — Requires specific config examples and user scenarios
- **DS-01** (Framework Application) — Applies config-driven architecture patterns

## Related Prompts

- `quality_yaml_configuration_schema_validation.md` — Detailed validation of the config schema
- `architecture_plugin_constraint_system.md` — The plugin system that makes constraints configurable
- `architecture_coupling_cohesion_analysis.md` — Coupling between config and code modules
