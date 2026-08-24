# CREATION Skill Template

> **For artifact generation.** Use this template when the skill generates output artifacts like documents, code, configurations, diagrams, or other deliverables.

---

## When to Use This Template

**Use CREATION when:**
- The skill produces a tangible output artifact
- There's a clear input-to-output transformation
- Quality validation of the output is needed
- Templates or boilerplate are involved

**Examples:**
- Document generation (PDFs, reports, READMEs)
- Code generation (boilerplate, scaffolding)
- Configuration generation (YAML, JSON configs)
- Diagram creation (architecture, flowcharts)
- Template instantiation (project scaffolds)

---

## Directory Structure

```
{skill-name}/
├── SKILL.md                     # Required: generation instructions
├── scripts/                     # Generation automation
│   ├── generate.py             # Main generation script
│   ├── validate.py             # Output validation
│   └── convert.py              # Format conversion
├── references/                  # Format specifications
│   ├── format_spec.md          # Output format documentation
│   ├── schema.md               # Data schema reference
│   └── examples.md             # Example outputs
└── assets/                      # Templates and boilerplate
    ├── template.{ext}          # Main template file
    ├── partial_header.{ext}    # Reusable partials
    ├── partial_footer.{ext}    # Reusable partials
    └── sample_output.{ext}     # Example of complete output
```

---

## SKILL.md Template

Copy everything below the line and customize:

---

```yaml
---
name: {skill-name}
description: Generate {artifact type} from {input types}. Use this skill when creating {output description}, producing {artifact type}, converting {format A} to {format B}, or when users mention "create {artifact}", "generate {artifact}", "make {artifact}", or "{artifact type}".
---
```

```markdown
# {Artifact} Creator

{Brief 1-2 sentence overview of what artifacts this skill creates and why they're valuable.}

## Purpose

{Explain what outputs this skill generates and what problems it solves. 2-3 sentences maximum.}

## When to Use This Skill

Use this skill when you need to:
- {Use case 1 - create specific artifact}
- {Use case 2 - convert format}
- {Use case 3 - generate from template}
- {User says: "create...", "generate...", "make..."}

## When NOT to Use This Skill

Do NOT use this skill when:
- {Exclusion 1 - different artifact type needed}
- {Exclusion 2 - modification, not creation}
- {Exclusion 3 - redirect to appropriate skill}

---

## Inputs

### Required Inputs

| Input | Type | Description | Example |
|-------|------|-------------|---------|
| `{input1}` | {type} | {What this input provides} | `{example value}` |
| `{input2}` | {type} | {What this input provides} | `{example value}` |
| `{input3}` | {type} | {What this input provides} | `{example value}` |

### Optional Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `{input4}` | {type} | `{default}` | {What this input controls} |
| `{input5}` | {type} | `{default}` | {What this input controls} |
| `{input6}` | {type} | `{default}` | {What this input controls} |

### Input Validation

Before generation, verify:

```bash
# Validate required inputs
{validation command or check}
```

**Input requirements:**
- {Input 1}: {Validation rules - format, length, required values}
- {Input 2}: {Validation rules}
- {Input 3}: {Validation rules}

**Common input errors:**
| Error | Cause | Fix |
|-------|-------|-----|
| {Error 1} | {Why it happens} | {How to fix} |
| {Error 2} | {Why it happens} | {How to fix} |

---

## Generation Process

### Step 1: Validate & Prepare Inputs

**Purpose:** Ensure all inputs meet requirements before generation.

```bash
# Using validation script
python scripts/validate.py --input {input-file}

# Or manual validation
{manual validation commands}
```

**Validation checklist:**
- [ ] {Input 1} is present and valid
- [ ] {Input 2} meets format requirements
- [ ] {Input 3} contains required fields

### Step 2: Generate Output

**Option A: Using Generation Script**

```bash
python scripts/generate.py \
  --input {input-file} \
  --output {output-file} \
  --template assets/template.{ext} \
  {--optional-flags}
```

**Option B: Manual Generation**

1. Load template from `assets/template.{ext}`
2. Substitute placeholders:
   - `{{{placeholder1}}}` → {input1 value}
   - `{{{placeholder2}}}` → {input2 value}
   - `{{{placeholder3}}}` → {input3 value}
3. Apply transformations:
   - {Transformation 1}
   - {Transformation 2}
4. Write to output file

**Option C: Inline Generation**

For simple artifacts, generate directly:

```{language}
{Inline generation code template}
```

### Step 3: Post-Process (If Needed)

**Apply post-processing:**
- [ ] {Post-process step 1, e.g., format validation}
- [ ] {Post-process step 2, e.g., linting}
- [ ] {Post-process step 3, e.g., compression}

```bash
# Post-processing command
{post-process command}
```

### Step 4: Validate Output

**Purpose:** Ensure generated output meets quality standards.

```bash
# Validate output
python scripts/validate.py --output {output-file}
```

**Quality checks:**
- [ ] {Quality check 1}
- [ ] {Quality check 2}
- [ ] {Quality check 3}

---

## Output Format

### Structure

```
{output-filename}.{ext}
├── {Section 1}
│   ├── {Component A}
│   └── {Component B}
├── {Section 2}
│   └── {Component C}
└── {Section 3}
```

### Format Specification

**File format:** {Format type, e.g., JSON, YAML, Markdown, PDF}

**Encoding:** UTF-8

**Example output structure:**

```{format}
{Example showing the complete output structure}
```

### Placeholders Reference

| Placeholder | Source | Transformation |
|-------------|--------|----------------|
| `{{{placeholder1}}}` | {Input field} | {Any transformation applied} |
| `{{{placeholder2}}}` | {Input field} | {Any transformation applied} |
| `{{{placeholder3}}}` | {Computed/derived} | {How it's computed} |

---

## Templates

### Main Template

Location: `assets/template.{ext}`

```{format}
{Show the template structure with placeholders}
```

### Partial: {Partial Name 1}

Location: `assets/partial_{name}.{ext}`

```{format}
{Show partial template}
```

**Used when:** {Conditions for including this partial}

### Partial: {Partial Name 2}

Location: `assets/partial_{name}.{ext}`

```{format}
{Show partial template}
```

**Used when:** {Conditions for including this partial}

---

## Customization Options

### Output Variations

| Variation | Description | How to Enable |
|-----------|-------------|---------------|
| {Variation 1} | {What it changes} | `--{flag}` or {setting} |
| {Variation 2} | {What it changes} | `--{flag}` or {setting} |
| {Variation 3} | {What it changes} | `--{flag}` or {setting} |

### Styling/Formatting Options

| Option | Values | Default | Effect |
|--------|--------|---------|--------|
| `{option1}` | {valid values} | `{default}` | {What it controls} |
| `{option2}` | {valid values} | `{default}` | {What it controls} |

### Adding Custom Sections

To add custom sections to the output:

1. {Step 1 for customization}
2. {Step 2 for customization}
3. {Step 3 for customization}

---

## Quality Validation

### Automated Validation

```bash
# Run full validation suite
python scripts/validate.py --output {output-file} --strict

# Quick validation
python scripts/validate.py --output {output-file} --quick
```

### Manual Validation Checklist

**Structure validation:**
- [ ] All required sections present
- [ ] Correct nesting/hierarchy
- [ ] No orphaned references

**Content validation:**
- [ ] All placeholders replaced
- [ ] No empty required fields
- [ ] Data types correct

**Format validation:**
- [ ] Syntax valid (parseable)
- [ ] Encoding correct
- [ ] File size reasonable

### Common Output Issues

| Issue | Symptoms | Fix |
|-------|----------|-----|
| {Issue 1} | {How it manifests} | {Resolution steps} |
| {Issue 2} | {How it manifests} | {Resolution steps} |
| {Issue 3} | {How it manifests} | {Resolution steps} |

---

## Examples

### Example 1: {Simple Case}

**Inputs:**
```{format}
{Show input data}
```

**Generated Output:**
```{format}
{Show corresponding output}
```

### Example 2: {Complex Case}

**Inputs:**
```{format}
{Show more complex input data}
```

**Generated Output:**
```{format}
{Show corresponding output}
```

### Example 3: {Edge Case}

**Inputs:** {Description of edge case}

**Handling:** {How the skill handles this case}

**Output:** {What gets generated}

For more examples, see `references/examples.md` and `assets/sample_output.{ext}`.

---

## Conversion & Export

### To {Format A}

```bash
python scripts/convert.py --input {output-file} --format {formatA}
```

### To {Format B}

```bash
python scripts/convert.py --input {output-file} --format {formatB}
```

### Batch Generation

For multiple outputs:

```bash
# Generate from multiple inputs
for input in inputs/*.{ext}; do
  python scripts/generate.py --input "$input" --output "outputs/$(basename $input)"
done
```

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/generate.py` | Main generation script |
| `scripts/validate.py` | Input/output validation |
| `scripts/convert.py` | Format conversion |
| `references/format_spec.md` | Complete format specification |
| `references/schema.md` | Data schema reference |
| `references/examples.md` | Additional examples |
| `assets/template.{ext}` | Main template |
| `assets/sample_output.{ext}` | Example of complete output |

## Related Skills

- `{related-skill-1}` - {Skill for a different output format}
- `{related-skill-2}` - {Skill that uses this output}
- `{related-skill-3}` - {Skill for related artifact type}
```

---

## Key Patterns for CREATION Skills

| Pattern | Implementation | Example |
|---------|----------------|---------|
| **SP-05: Output Organization** | Inputs → Process → Output → Validation | Clear sections for each phase |
| **RP-03: Usable Templates** | Actual template files in assets/ | `assets/template.yaml` with placeholders |
| **RP-05: Input Validation** | Validate before generation | Input requirements table + validation script |
| **QP-01: Validation Pipeline** | Multi-stage validation | Input → Output → Format validation |
| **MG-02: Scaffolding Templates** | Complete starting point | Template with all sections pre-populated |
| **WP-02: Validation Checkpoints** | Check at each stage | Validation checklist after each step |

---

## Quality Checklist

Before releasing a CREATION skill:

- [ ] Required inputs are clearly documented with types
- [ ] Input validation rules are explicit
- [ ] Generation process has clear steps
- [ ] Templates are provided in assets/
- [ ] Output format is fully specified
- [ ] Validation scripts/checklists exist
- [ ] Multiple examples show input→output
- [ ] Conversion options are documented
- [ ] Common output issues have fixes

---

## Example Skills to Study

Production CREATION skills in the repository:
- `pdf-creator` - Generate PDFs from markdown
- `ppt-creator` - Create presentations from outlines
- `skill-creator` - Meta-skill for creating skills
- `helm-chart-scaffolding` - Generate Helm chart boilerplate

---

**Last Updated:** 2026-01-29
