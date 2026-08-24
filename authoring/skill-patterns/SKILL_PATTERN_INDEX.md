# Skill Pattern Index

> **Master reference for Agent Skill patterns and techniques.** Use this index to find specific patterns, understand their implementations, and apply them to new skills.

---

## Pattern Categories

| Category | Code | Description | Pattern Count |
|----------|------|-------------|---------------|
| [Structure Patterns](#structure-patterns-sp) | SP | How to organize skill content | 8 |
| [Metadata Patterns](#metadata-patterns-mp) | MP | Description and discovery optimization | 5 |
| [Resource Patterns](#resource-patterns-rp) | RP | Bundled resource organization | 7 |
| [Workflow Patterns](#workflow-patterns-wp) | WP | Sequential process guidance | 6 |
| [Quality Patterns](#quality-patterns-qp) | QP | Validation and error handling | 6 |
| [Integration Patterns](#integration-patterns-ip) | IP | External tool/API connections | 5 |
| [Meta Patterns](#meta-patterns-mg) | MG | Self-referential and generative skills | 4 |

---

## Structure Patterns (SP)

### SP-01: Progressive Disclosure Architecture

**Description:** Three-tier loading system that defers detail until needed.

**Implementation:**
```
Tier 1: Metadata (always loaded) ─── ~100 words
Tier 2: SKILL.md body (on trigger) ─ <5k words
Tier 3: Bundled resources (on demand) ─ Unlimited
```

**When to use:** Every skill should follow this pattern.

**Example from `helm-chart-scaffolding`:**
- Tier 1: `description: Design, organize, and manage Helm charts...`
- Tier 2: Core workflow in SKILL.md (~500 lines)
- Tier 3: `assets/Chart.yaml.template`, `scripts/validate-chart.sh`

**Anti-pattern:** Loading all content into SKILL.md body.

---

### SP-02: Numbered Step Workflow

**Description:** Sequential numbered steps with clear entry/exit conditions.

**Implementation:**
```markdown
### Step 1: [Phase Name]

**Purpose:** [What this accomplishes]

**Procedure:**
1. [Action]
2. [Action]

**Validation:**
- [ ] [Verification check]

### Step 2: [Next Phase]
...
```

**When to use:** WORKFLOW-type skills, multi-stage processes.

**Example from `skill-creator`:**
```markdown
### Step 1: Understanding the Skill with Concrete Examples
Skip this step only when the skill's usage patterns are already clearly understood.

### Step 2: Planning the Reusable Skill Contents
To turn concrete examples into an effective skill, analyze each example by:
1. Considering how to execute on the example from scratch
2. Determining the appropriate level of freedom for Claude
```

**Key elements:**
- Skip conditions ("Skip this step only when...")
- Clear purpose statements
- Validation checkpoints

---

### SP-03: Task-Based Organization

**Description:** Sections organized by operation type rather than sequence.

**Implementation:**
```markdown
## Common Operations

### Operation: [Name]
**Command:** `...`
**Parameters:** ...
**Example:** ...

### Operation: [Name]
...

## Configuration Reference
...

## Troubleshooting
...
```

**When to use:** TOOL-type skills, reference-heavy content.

**Example from `github-ops`:**
- PR Operations section
- Issue Operations section
- Workflow Operations section
- Each operation documented independently

---

### SP-04: Hierarchical Knowledge Organization

**Description:** Domain knowledge organized from concepts to implementation.

**Implementation:**
```markdown
## Core Concepts
[Foundational understanding]

## Requirements/Standards
[What must be satisfied]

## Implementation Patterns
[How to satisfy requirements]

## Compliance Checklist
[Verification of completeness]
```

**When to use:** DOMAIN-type skills, compliance-focused content.

---

### SP-05: Input-Process-Output Flow

**Description:** Creation skills structured around transformation pipeline.

**Implementation:**
```markdown
## Inputs
**Required:** [What must be provided]
**Optional:** [What can be customized]

## Process
[Step-by-step transformation]

## Output
**Format:** [What is produced]
**Validation:** [How to verify]
```

**When to use:** CREATION-type skills, generation workflows.

**Example from `pdf-creator`:**
- Input: Markdown file
- Process: weasyprint conversion with Chinese font support
- Output: PDF document

---

### SP-06: Investigation-Resolution Flow

**Description:** Analysis skills structured for systematic troubleshooting.

**Implementation:**
```markdown
## Investigation Approach
[Philosophy and methodology]

## Diagnostic Tools
[What to use]

## Common Issues
### Issue: [Symptom]
**Quick Diagnosis:** [Command]
**Root Causes:** [Possibilities]
**Resolution:** [Fixes]

## Deep Dive References
[Where to go for complex cases]
```

**When to use:** ANALYSIS-type skills, debugging workflows.

**Example from `cloudflare-troubleshooting`:**
- Investigation via API evidence gathering
- Common issues with diagnostic scripts
- Resolution procedures per issue type

---

### SP-07: Section Cross-Referencing

**Description:** Explicit links between SKILL.md sections and bundled resources.

**Implementation:**
```markdown
**Reference:** See `references/detailed_spec.md` for complete documentation

For implementation scripts, use `scripts/generate.py`:
```bash
python scripts/generate.py --input file.txt
```
```

**When to use:** When bundled resources extend SKILL.md content.

**Example from `helm-chart-scaffolding`:**
```markdown
**Reference:** See `assets/Chart.yaml.template` for complete example
```

---

### SP-08: Related Skills Linking

**Description:** Explicit connections to complementary skills.

**Implementation:**
```markdown
## Related Skills

- `[skill-name]` - [Relationship/use case]
- `[skill-name]` - [Relationship/use case]
```

**When to use:** Every skill should link related skills.

**Example from `helm-chart-scaffolding`:**
```markdown
## Related Skills

- `k8s-manifest-generator` - For creating base Kubernetes manifests
- `gitops-workflow` - For automated Helm chart deployments
```

---

## Metadata Patterns (MP)

### MP-01: Trigger Phrase Inclusion

**Description:** Include phrases that would activate the skill in description.

**Implementation:**
```yaml
description: [What it does]. Use when [triggers]. Activates on [keywords].
```

**When to use:** Every skill description.

**Good example from `youtube-downloader`:**
```yaml
description: Download YouTube videos and HLS streams (m3u8) from platforms like Mux, Vimeo, etc. using yt-dlp and ffmpeg. Use this skill when users request downloading videos, extracting audio, handling protected streams with authentication headers, or troubleshooting download issues like nsig extraction failures, 403 errors, or cookie extraction problems.
```

**Key elements:**
- Action verbs ("Download", "Extract", "Troubleshoot")
- Platform/tool names
- Common error conditions
- User request patterns

---

### MP-02: Third-Person Skill Voice

**Description:** Use third-person to describe when skill applies.

**Implementation:**
```yaml
# Good
description: This skill should be used when...

# Bad
description: Use this skill when...
description: You should use this when...
```

**When to use:** All skill descriptions.

**Rationale:** Third-person enables the skill description to be quoted or referenced by the agent system without voice conflicts.

---

### MP-03: Specific Scope Boundaries

**Description:** Define what the skill does AND does not do.

**Implementation:**
```markdown
## When to Use This Skill

Use this skill when you need to:
- [Positive condition 1]
- [Positive condition 2]

## When NOT to Use This Skill

Do NOT use this skill when:
- [Exclusion 1]
- [Exclusion 2]
```

**When to use:** Skills that could be over-activated.

**Example from `cloudflare-troubleshooting`:**
- Use for: ERR_TOO_MANY_REDIRECTS, SSL errors, DNS issues
- Not for: General networking issues unrelated to Cloudflare

---

### MP-04: Keyword Density Optimization

**Description:** Include relevant keywords naturally in description.

**Implementation:**
- Include tool/technology names
- Include file formats/extensions
- Include common error messages
- Include user intent phrases

**Example from `mermaid-tools`:**
```yaml
description: Extracts Mermaid diagrams from markdown files and generates high-quality PNG images using bundled scripts. Activates when working with Mermaid diagrams, converting diagrams to PNG, extracting diagrams from markdown, or processing markdown files with embedded Mermaid code.
```

**Keywords included:** Mermaid, diagrams, markdown, PNG, extracting, converting

---

### MP-05: Action-Outcome Description

**Description:** Description states action (what it does) and outcome (what user gets).

**Implementation:**
```yaml
description: [ACTION] to [OUTCOME]. Use when [CONTEXT].
```

**Example:**
```yaml
# Action: Extracts structured text and tables
# Outcome: for downstream analysis or transformation
description: Extracts structured text and tables from PDF files for downstream analysis or transformation.
```

---

## Resource Patterns (RP)

### RP-01: Script Executable Documentation

**Description:** Scripts that serve as both tools and documentation.

**Implementation:**
```python
#!/usr/bin/env python3
"""
Script Name - Brief description

Usage:
    script.py <arg1> --option value

Examples:
    script.py input.txt --format json

"""

def main(arg1: str, option: str = "default"):
    """
    Function docstring explains behavior.

    Args:
        arg1: Description of first argument
        option: What this controls (default: "default")
    """
```

**Requirements:**
- Comprehensive docstring with usage
- Type hints for parameters
- Default values documented
- Example invocations

**Example from `skill-creator/scripts/init_skill.py`:**
- Module docstring with usage
- Function docstrings with parameters
- Real example commands

---

### RP-02: Reference File Self-Description

**Description:** Reference filenames explain content without reading.

**Implementation:**
```
references/
├── api_endpoints.md        # ✓ Clear
├── database_schema.md      # ✓ Clear
├── script_parameters.md    # ✓ Clear
├── commands.md             # ✗ Vague
├── reference.md            # ✗ Vague
```

**Naming pattern:** `<content-type>_<specificity>.md`

**Test:** Can someone understand the file's contents from the name alone?

---

### RP-03: Template Asset Organization

**Description:** Assets organized for copy-and-customize workflow.

**Implementation:**
```
assets/
├── [artifact-type]-template.[ext]  # Primary template
├── [artifact-type].example.[ext]   # Filled example
└── [supporting-files]/              # Related resources
```

**Example from `helm-chart-scaffolding`:**
```
assets/
├── Chart.yaml.template
└── values.yaml.template
```

**Usage in SKILL.md:**
```markdown
Copy `assets/Chart.yaml.template` and customize the following fields:
- `name`: Your chart name
- `version`: Initial version (1.0.0)
```

---

### RP-04: Grep-Friendly Large References

**Description:** For large references, provide grep patterns in SKILL.md.

**Implementation:**
```markdown
## API Reference

For complete API documentation, see `references/api_docs.md`.

**Quick lookups:**
- Authentication: Search for `## Authentication`
- Rate limits: Search for `## Rate Limiting`
- Error codes: Search for `## Error Codes`
```

**When to use:** References exceeding ~10k words.

---

### RP-05: Script Input Validation

**Description:** Scripts validate inputs before processing.

**Implementation:**
```python
def validate_inputs(skill_path: Path) -> tuple[bool, str]:
    """Validate skill directory structure."""
    if not skill_path.exists():
        return False, f"Path does not exist: {skill_path}"

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, f"SKILL.md not found in {skill_path}"

    return True, "Valid"
```

**Requirements:**
- Check existence of required inputs
- Return clear error messages
- Fail early, fail loudly

---

### RP-06: Relative Path References

**Description:** All path references are relative to skill directory.

**Implementation:**
```markdown
# Good
See `scripts/validate.py` for validation logic.
Use the template from `assets/template.yaml`.

# Bad
See `/home/user/.claude/skills/my-skill/scripts/validate.py`
See `~/.claude/skills/my-skill/assets/template.yaml`
```

**Forbidden patterns:**
- `/home/username/`
- `/Users/username/`
- `~/.claude/`
- Any absolute paths

---

### RP-07: Security-Sensitive Content Isolation

**Description:** Separate sensitive content patterns from core skill.

**Implementation:**
```
skill-name/
├── SKILL.md                    # No secrets
├── references/
│   └── auth_setup.md           # Documents env var usage
└── scripts/
    └── auth_helper.py          # Uses os.environ.get()
```

**Requirements:**
- Never hardcode secrets
- Document environment variable usage
- Reference `.env` or secrets manager patterns

---

## Workflow Patterns (WP)

### WP-01: Skip Condition Documentation

**Description:** Explicit conditions when steps can be skipped.

**Implementation:**
```markdown
### Step 1: [Step Name]

**Skip this step if:** [Condition when skip is valid]

[Step content...]
```

**Example from `skill-creator`:**
```markdown
### Step 1: Understanding the Skill with Concrete Examples

Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when working with an existing skill.
```

---

### WP-02: Validation Checkpoints

**Description:** Each major step ends with verification criteria.

**Implementation:**
```markdown
### Step N: [Step Name]

[Instructions...]

**Validation:**
- [ ] [Verification 1]
- [ ] [Verification 2]

**Proceed when:** All validation checks pass.
```

---

### WP-03: Fallback Procedures

**Description:** Document what to do when primary path fails.

**Implementation:**
```markdown
### Step N: [Step Name]

**Primary approach:**
[Main instructions]

**If this fails:**
1. [Fallback step 1]
2. [Fallback step 2]

**Still failing?** See `references/troubleshooting.md`
```

---

### WP-04: Decision Branch Documentation

**Description:** Explicit branching for conditional workflows.

**Implementation:**
```markdown
### Step N: Choose Approach

**Evaluate your situation:**

**If [Condition A]:**
→ Proceed to Step N+1a

**If [Condition B]:**
→ Proceed to Step N+1b

**If [Condition C]:**
→ Skip to Step N+2
```

---

### WP-05: Freedom Level Specification

**Description:** Indicate how much discretion the agent has.

**Implementation:**
```markdown
### [Operation Name]

**Freedom level:** [High/Medium/Low]

**High freedom:**
- Multiple valid approaches exist
- Agent should choose based on context

**Medium freedom:**
- Preferred patterns exist
- Acceptable variation within bounds

**Low freedom:**
- Exact steps required
- Use provided scripts
```

**Example from `skill-creator`:**
```markdown
**Match specificity to task risk:**
- **High freedom (text instructions)**: Multiple valid approaches exist
- **Medium freedom (pseudocode with parameters)**: Preferred patterns exist
- **Low freedom (exact scripts)**: Operations are fragile, consistency critical
```

---

### WP-06: Iteration Loop Documentation

**Description:** Document the refinement cycle for iterative work.

**Implementation:**
```markdown
### Step N: Iterate

**Iteration workflow:**
1. Use the [artifact] on real tasks
2. Notice struggles or inefficiencies
3. Identify what should be updated
4. Implement changes
5. Return to step 1

**Refinement filter:** Only add what solves observed problems.
```

---

## Quality Patterns (QP)

### QP-01: Multi-Stage Validation Pipeline

**Description:** Sequential validation gates with fail-fast behavior.

**Implementation:**
```python
# Stage 1: Structure validation
if not validate_structure(skill_path):
    return False, "Structure validation failed"

# Stage 2: Security validation
if not validate_security(skill_path):
    return False, "Security validation failed"

# Stage 3: Continue only if all pass
return True, "All validations passed"
```

**Stages in skill-creator:**
1. Quick validation (structure, naming, paths)
2. Security scan (secrets, dangerous patterns)
3. Packaging (only if all pass)

---

### QP-02: Content Hash Integrity

**Description:** Hash-based change detection for stale validation.

**Implementation:**
```python
def calculate_skill_hash(skill_path: Path) -> str:
    """Calculate deterministic hash of all security-relevant files."""
    hasher = hashlib.sha256()

    for file_path in sorted(files_to_hash):
        hasher.update(str(relative_path).encode('utf-8'))
        hasher.update(content)

    return hasher.hexdigest()
```

**Use case:** Invalidate security approval when content changes.

---

### QP-03: Error Exit Codes

**Description:** Distinct exit codes for different failure types.

**Implementation:**
```python
EXIT_SUCCESS = 0        # Clean
EXIT_HIGH_SEVERITY = 1  # Issues found
EXIT_CRITICAL = 2       # Must fix before distribution
EXIT_TOOL_MISSING = 3   # Required tool not installed
EXIT_ERROR = 4          # Script error
```

---

### QP-04: Dual-Mode Reporting

**Description:** Same validation with different verbosity for different contexts.

**Implementation:**
```python
if args.verbose:
    # Educational mode: detailed explanations
    print_verbose_report(findings)
else:
    # Gate mode: pass/fail with minimal output
    print_simple_report(findings)
```

**Use cases:**
- Simple mode: CI/CD gates
- Verbose mode: Developer education

---

### QP-05: Edge Case Documentation

**Description:** Explicit handling of non-happy-path scenarios.

**Implementation:**
```markdown
## Edge Cases & Failure Modes

### Missing Data
**Symptom:** [What happens]
**Handling:** [What skill should do]

### Ambiguous Input
**Symptom:** [What happens]
**Handling:** [Ask for clarification / Apply default]

### Partial Success
**Symptom:** [What happens]
**Handling:** [Report what succeeded, what failed]
```

---

### QP-06: Safety Constraints

**Description:** Explicit restrictions on dangerous operations.

**Implementation:**
```markdown
## Safety & Constraints

**NEVER:**
- Execute destructive commands without confirmation
- Modify production resources without explicit permission
- Store secrets in skill files

**ALWAYS:**
- Validate inputs before processing
- Use dry-run mode when available
- Confirm before irreversible actions
```

---

## Integration Patterns (IP)

### IP-01: API-First Documentation

**Description:** Document API usage patterns prominently.

**Implementation:**
```markdown
## API Operations

### Authentication
```bash
export API_KEY="your-key-here"
```

### Core Endpoints

**GET /resource**
```bash
curl -H "Authorization: Bearer $API_KEY" \
  https://api.example.com/resource
```

**Response:**
```json
{"id": 123, "name": "example"}
```
```

---

### IP-02: CLI Command Patterns

**Description:** Document CLI usage with real examples.

**Implementation:**
```markdown
### Command: [name]

**Syntax:**
```bash
command [options] <required-arg> [optional-arg]
```

**Options:**
| Flag | Description | Default |
|------|-------------|---------|
| `-v` | Verbose output | false |

**Examples:**
```bash
# Basic usage
command input.txt

# With options
command -v --format json input.txt
```
```

---

### IP-03: Error Response Handling

**Description:** Document common errors and resolution.

**Implementation:**
```markdown
## Error Handling

### Error: [Error Name/Code]
**HTTP Status:** 401
**Meaning:** Authentication failed
**Resolution:**
1. Verify API key is set
2. Check key hasn't expired
3. Regenerate key if needed

### Error: [Error Name/Code]
...
```

---

### IP-04: Rate Limit Documentation

**Description:** Document rate limits and best practices.

**Implementation:**
```markdown
## Rate Limits

| Endpoint | Limit | Window |
|----------|-------|--------|
| /api/v1/* | 100 | 1 minute |
| /search | 10 | 1 minute |

**Best practices:**
- Implement exponential backoff
- Cache responses when possible
- Batch requests where supported
```

---

### IP-05: Authentication Pattern Library

**Description:** Document common auth patterns.

**Implementation:**
```markdown
## Authentication Methods

### API Key (Header)
```bash
curl -H "X-API-Key: $API_KEY" https://api.example.com
```

### Bearer Token
```bash
curl -H "Authorization: Bearer $TOKEN" https://api.example.com
```

### OAuth 2.0
See `references/oauth_flow.md` for complete flow.
```

---

## Meta Patterns (MG)

### MG-01: Self-Exemplifying Architecture

**Description:** Skill structure demonstrates the patterns it teaches.

**Implementation:**
- Skill teaches skill creation by being a well-structured skill
- Every bundled resource demonstrates the pattern it documents
- The skill is its own reference implementation

**Example from `skill-creator`:**
- SKILL.md teaches SKILL.md structure
- `scripts/init_skill.py` creates the structure it documents
- `scripts/package_skill.py` validates the rules it defines

---

### MG-02: Template-Based Generation

**Description:** Provide templates with TODO markers for completion.

**Implementation:**
```markdown
# Template with educational scaffolding

---
name: [TODO: skill-name]
description: [TODO: Clear description of what this skill does and when to use it]
---

# [TODO: Skill Title]

## Purpose
[TODO: One paragraph describing the skill's purpose]

## When to Use This Skill
[TODO: Bullet list of trigger conditions]
```

**Key elements:**
- Clear `[TODO: ...]` markers
- Inline guidance on what to write
- Deletable scaffolding sections

---

### MG-03: Skill Composition

**Description:** Skills that orchestrate or compose other skills.

**Implementation:**
```markdown
## Workflow

This skill coordinates multiple specialized skills:

1. **Input Processing** → Use `input-parser` skill
2. **Transformation** → Use `transformer` skill
3. **Output Generation** → Use `output-generator` skill

For each stage, invoke the appropriate skill.
```

**Use case:** Complex workflows that span multiple domains.

---

### MG-04: Self-Updating Documentation

**Description:** Documentation that references executable source of truth.

**Implementation:**
```markdown
## Validation Rules

For current validation rules, see `scripts/validate.py`.

The validator checks:
- [High-level description]

For exact patterns, reference the script source.
```

**Rationale:** Scripts are authoritative; documentation can become stale.

---

## Pattern Application Guide

### For New Skill Creation

**Always apply:**
- SP-01: Progressive Disclosure Architecture
- SP-08: Related Skills Linking
- MP-01: Trigger Phrase Inclusion
- MP-02: Third-Person Skill Voice
- RP-06: Relative Path References

**Apply based on type:**
| Skill Type | Primary Patterns |
|------------|-----------------|
| WORKFLOW | SP-02, WP-01, WP-02, WP-03 |
| TOOL | SP-03, IP-01, IP-02, IP-03 |
| DOMAIN | SP-04, QP-05, QP-06 |
| CREATION | SP-05, RP-03, QP-01 |
| ANALYSIS | SP-06, WP-04, QP-05 |
| INTEGRATION | IP-01 through IP-05 |

### For Skill Review

**Check against:**
1. Does description enable task matching? (MP-01, MP-04)
2. Is content appropriately tiered? (SP-01)
3. Are resources properly organized? (RP-02, RP-03)
4. Are edge cases handled? (QP-05, QP-06)
5. Are related skills linked? (SP-08)

---

## Quick Reference Tables

### Pattern by Problem

| Problem | Pattern |
|---------|---------|
| Skill not activating | MP-01, MP-04 |
| Too much in SKILL.md | SP-01, RP-04 |
| Users confused about steps | SP-02, WP-01, WP-02 |
| Scripts not documented | RP-01 |
| Edge cases causing failures | QP-05, WP-03 |
| Security concerns | QP-01, RP-07 |
| Users don't know related skills | SP-08 |

### Pattern by Complexity

| Complexity | Recommended Patterns |
|------------|---------------------|
| Simple (single operation) | SP-03, MP-01, QP-05 |
| Medium (multi-step) | SP-02, WP-01, WP-02, RP-01 |
| Complex (multi-resource) | SP-01, SP-07, RP-03, QP-01 |
| Meta (creates other skills) | MG-01, MG-02, QP-01 |

---

**Total Patterns: 41**
- Structure: 8
- Metadata: 5
- Resource: 7
- Workflow: 6
- Quality: 6
- Integration: 5
- Meta: 4
