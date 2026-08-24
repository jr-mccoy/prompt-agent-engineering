# Troubleshooting Guide

This guide helps diagnose and resolve common issues when creating, using, or maintaining resources in the Prompting-guides repository.

---

## Quick Diagnostics

### Issue Categories

| Symptom | Likely Cause | Go To Section |
|---------|--------------|---------------|
| Prompt produces wrong output | Missing context, unclear instructions | [Prompt Issues](#prompt-issues) |
| Skill not loading properly | Metadata errors, file structure | [Skill Issues](#skill-issues) |
| Agent behaves unexpectedly | Decision logic, guardrails | [Agent Issues](#agent-issues) |
| Command pipeline fails | Orchestration, dependencies | [Command Issues](#command-issues) |
| Quality check fails | Missing sections, format | [Quality Issues](#quality-issues) |
| Resource not discoverable | Metadata, indexing | [Discovery Issues](#discovery-issues) |

---

## Prompt Issues

### Problem: Prompt produces inconsistent output

**Symptoms:**
- Same prompt gives different results
- Output format varies unexpectedly
- Missing expected sections

**Diagnosis:**
```markdown
Check for:
1. Ambiguous instructions - multiple interpretations possible
2. Missing output format specification
3. Lack of examples showing expected output
4. Undefined terms or concepts
```

**Solutions:**

1. **Add explicit output format:**
   ```markdown
   ## Expected Output Format

   Return a JSON object with the following structure:
   {
     "summary": "string - one sentence summary",
     "findings": ["array of finding objects"],
     "severity": "low | medium | high | critical"
   }
   ```

2. **Add concrete examples:**
   ```markdown
   ## Example Output

   Given input: [specific example]
   Expected output:
   [exact expected output]
   ```

3. **Clarify ambiguous terms:**
   ```markdown
   ## Definitions

   - "Critical issue": Any issue that would cause data loss or security breach
   - "High priority": Issues affecting >50% of users
   ```

---

### Problem: Prompt works for simple cases but fails on complex ones

**Symptoms:**
- Works on test examples, fails on real data
- Misses edge cases
- Partial or incomplete analysis

**Diagnosis:**
```markdown
Check for:
1. Instructions assume simple input
2. Missing handling for edge cases
3. No progressive complexity
4. Output constraints too rigid
```

**Solutions:**

1. **Add edge case handling:**
   ```markdown
   ## Edge Cases

   If the input contains:
   - Empty values: Report as "No data provided for X"
   - Multiple conflicting sources: List all with confidence levels
   - Incomplete data: Proceed with available data, note gaps
   ```

2. **Add progressive analysis:**
   ```markdown
   ## Analysis Depth

   Adjust analysis based on input complexity:
   - Simple (< 100 lines): Full detailed analysis
   - Medium (100-1000 lines): Focus on high-risk areas
   - Large (> 1000 lines): Prioritize critical paths, sample others
   ```

---

### Problem: Prompt generates false positives

**Symptoms:**
- Flags non-issues as problems
- Over-reports low-priority items
- Recommendations don't apply

**Diagnosis:**
```markdown
Check for:
1. Missing False-Positive Prevention section
2. No context-awareness
3. Overly broad matching criteria
4. Missing "When NOT to flag" guidance
```

**Solutions:**

1. **Add False-Positive Prevention:**
   ```markdown
   ## False-Positive Prevention

   Do NOT flag as issues:
   - Intentional design decisions documented in comments
   - Framework-specific patterns that appear unusual
   - Test code following different standards than production
   - Deprecated code marked for removal
   ```

2. **Add confidence levels:**
   ```markdown
   Report confidence for each finding:
   - HIGH: Clear violation, verifiable
   - MEDIUM: Likely issue, context-dependent
   - LOW: Possible concern, requires human review
   ```

---

## Skill Issues

### Problem: Skill metadata not recognized

**Symptoms:**
- Skill doesn't appear in listings
- Trigger phrases don't activate skill
- Description not showing

**Diagnosis:**
```bash
# Check SKILL.md frontmatter
head -10 skill-directory/SKILL.md

# Expected format:
---
name: skill-name
description: Description text...
---
```

**Solutions:**

1. **Fix YAML frontmatter:**
   ```yaml
   ---
   name: security-audit
   description: Comprehensive security audit for web applications. Use when users mention "security review", "vulnerability scan", "OWASP", or "penetration test".
   ---
   ```

2. **Ensure description includes trigger phrases:**
   ```yaml
   description: ... Use this skill when users mention "keyword1", "keyword2", or ask about "topic".
   ```

---

### Problem: Skill scripts don't execute

**Symptoms:**
- Scripts referenced but not running
- Permission errors
- Path not found errors

**Diagnosis:**
```bash
# Check script exists and is executable
ls -la skill-directory/scripts/

# Check shebang line
head -1 skill-directory/scripts/script.sh
# Should be: #!/bin/bash or #!/usr/bin/env python3
```

**Solutions:**

1. **Add proper shebang:**
   ```bash
   #!/usr/bin/env bash
   # or
   #!/usr/bin/env python3
   ```

2. **Make executable:**
   ```bash
   chmod +x scripts/*.sh scripts/*.py
   ```

3. **Use relative paths correctly:**
   ```markdown
   ## Reference Files

   Run the validation script:
   ```bash
   ./scripts/validate.sh
   ```
   ```

---

### Problem: Skill references not found

**Symptoms:**
- "File not found" when loading references
- Broken links in skill documentation
- Missing context for instructions

**Diagnosis:**
```bash
# List skill directory structure
find skill-directory -type f -name "*.md"

# Check references in SKILL.md match actual files
grep -E "references/|assets/|scripts/" skill-directory/SKILL.md
```

**Solutions:**

1. **Verify file paths:**
   ```markdown
   ## Reference Files

   | Resource | Purpose |
   |----------|---------|
   | `references/patterns.md` | Common patterns (verify file exists) |
   | `assets/template.yaml` | Configuration template |
   ```

2. **Use consistent naming:**
   - `references/` for documentation
   - `assets/` for templates and examples
   - `scripts/` for executable code

---

## Agent Issues

### Problem: Agent enters infinite loop

**Symptoms:**
- Agent keeps repeating same action
- Never reaches conclusion
- Resource exhaustion

**Diagnosis:**
```markdown
Check for:
1. Missing termination conditions
2. No maximum iteration limit
3. Circular decision logic
4. Lack of progress tracking
```

**Solutions:**

1. **Add termination conditions:**
   ```markdown
   ## Termination Conditions

   Stop processing when:
   - Root cause identified with confidence > 80%
   - Maximum 10 investigation cycles reached
   - No new information gained in 2 consecutive cycles
   - User requests stop
   ```

2. **Add progress tracking:**
   ```markdown
   ## Progress Tracking

   After each cycle, evaluate:
   - What new information was gained?
   - Is confidence increasing?
   - Are hypotheses being eliminated?

   If no progress in 2 cycles, escalate to human.
   ```

---

### Problem: Agent takes unexpected actions

**Symptoms:**
- Performs operations not requested
- Makes changes without confirmation
- Ignores guardrails

**Diagnosis:**
```markdown
Check for:
1. Ambiguous action boundaries
2. Missing confirmation requirements
3. Unclear scope limits
4. No destructive action guards
```

**Solutions:**

1. **Add explicit guardrails:**
   ```markdown
   ## Guardrails

   NEVER without explicit user confirmation:
   - Delete any file or resource
   - Modify production data
   - Execute commands with side effects
   - Make external API calls that change state

   ALWAYS before taking action:
   - State what action will be taken
   - Explain why it's necessary
   - Wait for user approval
   ```

2. **Define scope clearly:**
   ```markdown
   ## Scope

   This agent operates ONLY on:
   - Files in the current repository
   - Read-only external APIs
   - Local development environments

   This agent does NOT:
   - Access production systems
   - Modify infrastructure
   - Send communications
   ```

---

## Command Issues

### Problem: Pipeline stages fail silently

**Symptoms:**
- Some agents don't run
- Missing outputs from stages
- Incomplete results

**Diagnosis:**
```markdown
Check for:
1. Missing error handling
2. Incorrect input/output mapping
3. Timeout too short
4. Dependency errors
```

**Solutions:**

1. **Add explicit error handling:**
   ```yaml
   pipeline:
     - stage: analysis
       agents: [security-review]
       on_error: continue  # or: fail, retry
       max_retries: 2
       timeout: 300s
   ```

2. **Add stage validation:**
   ```markdown
   ## Stage Validation

   After each stage, verify:
   - [ ] Expected outputs exist
   - [ ] Output format is valid
   - [ ] No error indicators in output
   ```

---

### Problem: Command outputs are inconsistent

**Symptoms:**
- Different runs produce different structures
- Missing sections in output
- Formatting varies

**Solutions:**

1. **Define output schema:**
   ```markdown
   ## Output Schema

   Final output MUST include:
   ```json
   {
     "summary": "required",
     "stages": {
       "stage_name": {
         "status": "success | error | skipped",
         "output": "...",
         "errors": []
       }
     },
     "recommendations": []
   }
   ```

2. **Add output validation:**
   ```markdown
   ## Output Validation

   Before returning output:
   1. Validate against schema
   2. Fill missing sections with "Not available"
   3. Include execution metadata
   ```

---

## Quality Issues

### Problem: Resource fails quality rubric

**Symptoms:**
- Low scores on quality check
- Missing required sections
- Inconsistent formatting

**Common missing sections and fixes:**

| Missing Section | How to Fix |
|-----------------|------------|
| False-Positive Prevention | Add section with DO NOT flag guidance |
| When to Use / NOT Use | Add clear inclusion/exclusion criteria |
| Examples | Add 3-5 worked examples with input/output |
| Confidence Levels | Add framework for output certainty |
| Quality Indicators | Add measurable success criteria |

**Quality checklist:**
```markdown
## Self-Review Checklist

- [ ] Clear intent statement
- [ ] Specified audience
- [ ] Context requirements
- [ ] Output format specification
- [ ] 3-5 worked examples
- [ ] False-positive prevention
- [ ] When to use / not use
- [ ] Confidence framework
- [ ] Quality indicators
- [ ] No ambiguous terms
```

---

## Discovery Issues

### Problem: Resource not appearing in searches

**Symptoms:**
- Can't find resource by name
- Trigger phrases don't work
- Not in category listings

**Diagnosis:**
```markdown
Check:
1. File location matches expected category
2. Frontmatter/metadata present and valid
3. README.md updated with new resource
4. CLAUDE.md mappings updated
```

**Solutions:**

1. **Verify file location:**
   ```
   Expected: domain-{category}/{subcategory}/{resource}.md
   Or: domain-agentic-resources/skills/{category}/{skill-name}/SKILL.md
   ```

2. **Update category README:**
   ```markdown
   ## Resources

   | Resource | Description |
   |----------|-------------|
   | new-resource | Description |
   ```

3. **Update CLAUDE.md mappings:**
   ```markdown
   | "keyword" | `domain-category/path/` |
   ```

---

## General Troubleshooting Process

### Step 1: Isolate the Issue

```markdown
1. What is the expected behavior?
2. What is the actual behavior?
3. When did it start failing?
4. What changed recently?
```

### Step 2: Check Common Causes

```markdown
1. Syntax errors in frontmatter/metadata
2. Missing required sections
3. Broken file paths or references
4. Inconsistent naming
5. Missing permissions (scripts)
```

### Step 3: Test Incrementally

```markdown
1. Test with minimal input
2. Add complexity gradually
3. Identify breaking point
4. Fix specific issue
```

### Step 4: Validate Fix

```markdown
1. Verify original issue resolved
2. Test edge cases
3. Run quality checks
4. Update documentation if needed
```

---

## Getting Help

If this guide doesn't resolve your issue:

1. **Check existing resources:**
   - `authoring/skill-patterns/SKILL_PATTERN_INDEX.md`
   - `AI_AGENT_QUICK_START.md`
   - `PROMPT_QUALITY_STANDARDS.md`

2. **Review similar resources:**
   - Find a working resource of the same type
   - Compare structure and content

3. **Open an issue:**
   - Describe expected vs. actual behavior
   - Include resource path
   - Provide minimal reproduction steps

---

**Last Updated:** 2026-01-29
