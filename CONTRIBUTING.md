# Contributing to Prompt & Agent Engineering

Thank you for your interest in contributing! This guide covers the rules and mechanics of contributing.

> **First time here?** Start with the [`EXTERNAL_CONTRIBUTOR_GUIDE.md`](EXTERNAL_CONTRIBUTOR_GUIDE.md) — a friendly, end-to-end walkthrough (including a "for researchers" path). This file is the detailed reference.
>
> **Contributing a new technique** (not just a prompt)? See [`authoring/TECHNIQUE_CONTRIBUTION_GUIDE.md`](authoring/TECHNIQUE_CONTRIBUTION_GUIDE.md).
>
> All participation is governed by our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Table of Contents

- [How to Contribute](#how-to-contribute)
- [File Naming Conventions](#file-naming-conventions)
- [Prompt Quality Standards](#prompt-quality-standards)
- [Prompt Template](#prompt-template)
- [Adding New Prompts](#adding-new-prompts)
- [Improving Existing Prompts](#improving-existing-prompts)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## How to Contribute

We welcome contributions in several forms:

1. **New Prompts**: Add prompts for missing use cases or domains
2. **Prompt Improvements**: Enhance existing prompts with examples, clarity, or techniques
3. **Documentation**: Improve guides, add examples, or fix typos
4. **Bug Reports**: Report broken prompts or incorrect instructions
5. **Feature Requests**: Suggest new categories or improvements

## File Naming Conventions

Consistent naming is critical for discoverability and programmatic access.

### Root Level Files
Use `UPPERCASE_WITH_UNDERSCORES.md` for main entry points:
- ✅ `README.md`
- ✅ `CONTRIBUTING.md`
- ✅ `MASTER_TECHNIQUE_INDEX.md`

### Category Files
Use `lowercase_with_underscores.md` for all prompts in subdirectories:
- ✅ `architecture_design_pattern_identification.md`
- ✅ `performance_bottleneck_identification.md`
- ✅ `engineering_prompt_improver.md` (correct format)
- ✅ `advanced_prompting_techniques.md` (correct format)

### Rules
- Use only lowercase letters, numbers, and underscores
- No hyphens, spaces, or special characters
- Be descriptive but concise (3-6 words)
- Start with category context when helpful

## Prompt Quality Standards

All prompts should meet these quality criteria:

### Structure (Required)
- Clear markdown hierarchy with headers
- Logical flow from objective → instructions → output
- Numbered or bulleted steps for clarity

### Clarity (Required)
- Single, unambiguous objective stated upfront
- Clear scope and boundaries
- Specific, actionable language

### Instructions (Required)
- Detailed, sequential steps
- Sub-steps for complex operations
- Explicit rather than implicit guidance

### Examples (Highly Recommended)
- Sample input/code snippets
- Expected output format
- Before/after comparisons for improvement prompts

### Techniques (Recommended)
- Reference technique codes from MASTER_TECHNIQUE_INDEX.md
- Apply appropriate prompt engineering patterns
- Document which techniques are used

### Documentation (Required)
- "When to Use" section describing ideal scenarios
- Clear output format specification
- Customization guidance where applicable

## Prompt Template

Every prompt saved to this repository starts with a **YAML frontmatter block** (it feeds `PROMPT_INDEX.json` and discovery tooling), followed by a structured markdown body. The canonical, copy-paste template — with field explanations, a minimal example, and content-delimiting guidance — lives in [`authoring/NEW_PROMPT_TEMPLATE.md`](authoring/NEW_PROMPT_TEMPLATE.md). Use it.

The required shape:

```markdown
---
title: "Descriptive Action Title"
category: domain/subcategory
description: "One-line statement of what this prompt accomplishes"
techniques:
  - ST-01
  - CM-02
difficulty: beginner | intermediate | advanced
tags:
  - keyword1
  - keyword2
updated: "YYYY-MM-DD"
related_prompts:
  - path/to/related_prompt.md
---

# Prompt Name

**Objective:** [One clear sentence — ST-01]

## Inputs / Context
**Required:** [...]
**If any required input is missing:** Ask clarifying questions before proceeding.

## Constraints
**Must:** [...]
**Must Not:** [at least 2 guardrails against common failure modes]

## Steps
1. [...]

## Output Format
[Explicit structure — ST-03]

## Verification
- [ ] Output addresses the objective
- [ ] No constraints violated
- [ ] Format matches specification
```

### Frontmatter fields

| Field | Required | Notes |
|-------|----------|-------|
| `title` | Yes | Descriptive action title, quoted |
| `category` | Yes | `domain/subcategory` matching the file's directory |
| `description` | Yes | One line; shown in `PROMPT_INDEX` |
| `techniques` | Yes | 3–5 **canonical** IDs from [`MASTER_TECHNIQUE_INDEX.md`](techniques/MASTER_TECHNIQUE_INDEX.md) — never invented |
| `difficulty` | Yes | `beginner`, `intermediate`, or `advanced` |
| `tags` | Yes | Lowercase keywords for search |
| `updated` | Yes | `"YYYY-MM-DD"`, quoted |
| `related_prompts` | Recommended | Repo-relative paths to complementary prompts |

> **Domain-specific fields:** some domains add an optional machine-readable block — e.g. prompts in `domain-reasoning-craft/` carry a `reasoning:` block (styles, stakes, horizon, uncertainty, mode). If you contribute to such a domain, copy the block from an existing sibling prompt so metadata stays consistent. See [`authoring/NEW_PROMPT_TEMPLATE.md`](authoring/NEW_PROMPT_TEMPLATE.md) and [`PROMPT_QUALITY_STANDARDS.md`](PROMPT_QUALITY_STANDARDS.md).

## Adding New Prompts

### Step 1: Identify the Right Domain

Prompts live in **`domain-*/` directories** (42 of them) plus a few self-contained toolkits. Pick the domain that matches your content:

- Browse the full **Repository Structure** table in [`README.md`](README.md#repository-structure), or
- Use the detailed **Category Mapping** routing in [`CLAUDE.md`](CLAUDE.md) (the most complete "what goes where" reference), or
- Search [`PROMPT_INDEX.md`](PROMPT_INDEX.md) for similar existing prompts and place yours alongside them.

**Choosing the resource type first:**

| If your contribution is… | It's a… | Place it in / start with |
|--------------------------|---------|--------------------------|
| A single reusable instruction set | **Prompt** | the matching `domain-*/` directory |
| A reusable, multi-step capability with bundled scripts/assets | **Skill** | [`domain-agentic-resources/skills/`](domain-agentic-resources/skills/) ([authoring guide](authoring/skill-patterns/README.md)) |
| A task-specific agent definition | **Agent** | [`domain-agentic-resources/agents/`](domain-agentic-resources/agents/) ([authoring guide](authoring/agent-patterns/AGENT_QUICK_START.md)) |
| A slash-command workflow | **Command** | [`domain-agentic-resources/commands/`](domain-agentic-resources/commands/) ([authoring guide](authoring/command-patterns/COMMAND_QUICK_START.md)) |
| A new prompt-engineering technique | **Technique** | follow [`authoring/TECHNIQUE_CONTRIBUTION_GUIDE.md`](authoring/TECHNIQUE_CONTRIBUTION_GUIDE.md) |

If no domain fits, propose a new one in your PR (briefly justify why existing domains don't work).

### Step 2: Create the Prompt File

1. Use the naming convention: `category_descriptive_name.md`
2. Follow the prompt template above
3. Include concrete examples
4. Reference relevant techniques

### Step 3: Test and Validate

Before submitting:
1. Test the prompt with an AI agent (Claude Code, Cursor, ChatGPT, etc.) and verify it produces the expected output.
2. Check for clarity, completeness, and accurate examples.
3. Run the local validation tooling:

   ```bash
   # frontmatter (required fields, technique-ID format, date format)
   python3 scripts/generate_prompt_index.py            # regenerate the prompt index
   python3 scripts/validate_naming_conventions.py --ci  # naming conventions
   python3 scripts/check_relative_links.py              # relative Markdown links

   # file naming (lowercase, underscores, no articles, ≤55 chars)
   python3 scripts/validate_naming_conventions.py

   # technique IDs reference real entries in MASTER_TECHNIQUE_INDEX.md
   python3 scripts/validate_technique_catalog.py

   # regenerate the index so your prompt is discoverable
   python3 scripts/generate_prompt_index.py
   ```

4. If you use [`pre-commit`](https://pre-commit.com/), `pre-commit run --all-files` runs the same checks (see [`.pre-commit-config.yaml`](.pre-commit-config.yaml)).

> CI enforces these on every PR (structure compliance, metadata validation, inventory counts), so running them locally first avoids round-trips.

### Step 4: Update Documentation

If adding a new category or significant prompts:
1. Update README.md with the new prompt listing
2. Add cross-references to related prompts
3. Update USE_CASE_LOOKUP.md if relevant

## Improving Existing Prompts

When improving existing prompts, focus on:

### Priority Improvements
1. **Add Examples**: Most valuable addition for users
2. **Enhance Instructions**: Add sub-steps and details
3. **Add Customization Guide**: Help users adapt prompts
4. **Add Technique References**: Link to MASTER_TECHNIQUE_INDEX
5. **Add Cross-References**: Link related prompts

### Quality Enhancements
- Clarify ambiguous language
- Add missing output specifications
- Include edge cases and special scenarios
- Improve formatting and structure
- Fix typos and grammatical errors

## Commit Guidelines

### Commit Message Format

```
<type>: <short description>

<optional detailed description>
```

### Types
- `feat`: New prompt or major feature
- `improve`: Enhancement to existing prompt
- `fix`: Fix broken prompt or error
- `docs`: Documentation updates
- `style`: Formatting, naming (no content change)
- `refactor`: Restructure without changing functionality
- `test`: Add tests or validation

### Examples

```
feat: add OWASP Top 10 security analysis prompt

Comprehensive prompt for analyzing codebases against all OWASP Top 10
vulnerabilities with specific detection patterns for each category.
```

```
improve: add examples to performance bottleneck prompt

Added concrete code examples and sample output to demonstrate
expected analysis format.
```

```
fix: correct technique reference in prompt improver

Fixed incorrect technique code ST-03 → ST-05 in engineering/prompt_improver.md
```

## Pull Request Process

### Before Submitting

1. ✅ Follow file naming conventions
2. ✅ Use the prompt template
3. ✅ Test your prompt with an AI agent
4. ✅ Add examples where possible
5. ✅ Update README.md if needed
6. ✅ Ensure markdown is properly formatted
7. ✅ Check for typos and grammar

### PR Description Template

```markdown
## Description
[Brief description of what this PR adds or changes]

## Type of Change
- [ ] New prompt
- [ ] Prompt improvement
- [ ] Documentation update
- [ ] Bug fix
- [ ] Other (specify)

## Category
[Which category/directory does this affect?]

## Testing
[Describe how you tested this prompt]

## Checklist
- [ ] Follows file naming conventions
- [ ] Uses prompt template structure
- [ ] Includes examples
- [ ] References techniques from MASTER_TECHNIQUE_INDEX
- [ ] Updates README.md (if applicable)
- [ ] Markdown is properly formatted
```

### Review Process

1. Submit your PR with a clear description
2. Maintainers will review for quality and consistency
3. Address any requested changes
4. Once approved, your PR will be merged

### What We Look For

- **Quality**: Does it meet our quality standards?
- **Clarity**: Is it clear and easy to understand?
- **Completeness**: Does it include examples and documentation?
- **Consistency**: Does it follow our conventions?
- **Value**: Does it add meaningful value to the repository?

## Questions or Need Help?

- Open an issue for questions or discussions
- Tag issues with appropriate labels
- Be specific about what you need help with

## Recognition

All contributors will be recognized in the repository. Thank you for helping make this resource better!

---

**License**: By contributing, you agree that your contributions will be licensed under the MIT License.
