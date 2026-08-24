# New Prompt Template

**Purpose:** Copy-paste template for creating consistent, high-quality prompts. Works with any AI model.

> **Technique IDs:** All IDs referenced here (ST-01, RT-02, etc.) are from the canonical [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md). Do not invent new IDs.

---

## Quick Start: Copy This Template

> **Saving into this repository?** Keep the YAML frontmatter block — it feeds `PROMPT_INDEX.json` and discovery tooling. Using the prompt ad hoc? You can drop the frontmatter.

```markdown
---
title: "[Descriptive Action Title]"
category: [domain/subcategory]
description: "[One-line statement of what this prompt accomplishes]"
techniques:
  - [ST-01]
  - [CM-02]
difficulty: [beginner | intermediate | advanced]
tags:
  - [keyword1]
  - [keyword2]
updated: "[YYYY-MM-DD]"
related_prompts:
  - [path/to/related_prompt.md]
---

# [Prompt Name]

**Objective:** [One clear sentence describing what this prompt accomplishes — ST-01]

---

## Inputs / Context

**Required:**
- [Input 1]: [Description of what to provide]
- [Input 2]: [Description of what to provide]

**Optional:**
- [Input 3]: [Description, with default if omitted]

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- [Constraint 1 — what MUST happen]
- [Constraint 2 — what MUST happen]

**Must Not:**
- [Constraint 1 — what MUST NOT happen]
- [Constraint 2 — what MUST NOT happen]

---

## Steps

1. [First action — typically gather/understand context]
2. [Second action — core analysis or creation work]
3. [Third action — synthesize or refine]
4. [Fourth action — produce final output]

---

## Output Format

**Produce output in this exact structure:**

### [Section 1 Name]
[Description of what goes here]

### [Section 2 Name]
[Description of what goes here]

### [Section 3 Name]
[Description of what goes here]

---

## Verification

**Quick self-check (always do):**
- [ ] Output addresses the stated objective
- [ ] All required inputs were used
- [ ] No constraints were violated
- [ ] Format matches specification

**High-stakes option (for critical work):**
After completing output, explicitly answer:
1. What could be wrong or missing?
2. What assumptions did I make?
3. What evidence supports my conclusions?
```

---

## Frontmatter Fields (repository prompts)

| Field | Required | Notes |
|-------|----------|-------|
| `title` | Yes | Descriptive action title, quoted |
| `category` | Yes | `domain/subcategory` matching the file's directory |
| `description` | Yes | One line; shown in PROMPT_INDEX |
| `techniques` | Yes | 3–5 canonical IDs from the [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md) — never invented |
| `difficulty` | Yes | `beginner`, `intermediate`, or `advanced` |
| `tags` | Yes | Lowercase keywords for search |
| `updated` | Yes | `"YYYY-MM-DD"`, quoted |
| `related_prompts` | Recommended | Repo-relative paths to complementary prompts |

See [PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) for the canonical frontmatter specification.

### Optional domain-specific frontmatter

Some domains add an extra machine-readable block on top of the standard fields. Most notably, prompts in [`domain-reasoning-craft/`](../domain-reasoning-craft/) carry a `reasoning:` block that is indexed for discovery:

```yaml
reasoning:
  styles: [bayesian, probabilistic]   # reasoning styles the prompt exercises
  stakes: variable                    # low | medium | high | variable
  horizon: variable                   # short | medium | long | variable
  uncertainty: risk                   # risk | ambiguity | deep_uncertainty
  evidence_quality: variable
  domain_complexity: single_domain    # single_domain | cross_domain
  collaboration: solo                 # solo | group
  output_format: structured_table
  user_role: [analyst, researcher, forecaster, strategist]
  mode: [audit, synthesize]           # audit | generate | synthesize | ...
```

**If you contribute to a domain that uses an extended block, copy it from an existing sibling prompt** in that directory and adjust the values — don't omit it, or your prompt's metadata will be inconsistent with the rest of the domain. These fields are optional repo-wide (the validator won't flag their absence), so consistency is on the author. After editing, re-run `python3 ../scripts/generate_prompt_index.py`.

---

## Template Fields Explained

| Field | Purpose | Technique |
|-------|---------|-----------|
| **Objective** | Single sentence defining success | ST-01: Clear Objective Statement |
| **Inputs/Context** | What the AI needs to work with — if the prompt consumes pasted content, tell the model it arrives in named tags (see below) | CM-01: Explicit Context Framing |
| **Constraints** | Must/Must-Not guardrails | CM-02: Constraint Specification |
| **Steps** | Numbered workflow | ST-02: Structured Sequential Instructions |
| **Output Format** | Explicit structure | ST-03: Output Format Specification |
| **Verification** | Self-check + high-stakes option | QA-01: Chain-of-Verification |

---

## "If Missing Info" Rule

**Always include this behavior:**

> **If any required input is missing:** Ask clarifying questions before proceeding.

This prevents the AI from guessing or producing generic output. Applies to all prompts.

---

## Constraints Best Practice

**Always include at least 2 "Must Not" constraints when relevant.** These prevent common failure modes:

| Common "Must Not" Constraints |
|------------------------------|
| Must not invent information not in the provided context |
| Must not skip steps or combine steps |
| Must not produce output without citing evidence |
| Must not make assumptions about missing data |
| Must not use placeholder text in final output |
| Must not exceed specified length/scope |

---

## Delimiting Injected Content

**When a prompt has the model consume pasted content** — code, a document, a transcript, a dataset, a draft to improve, few-shot examples — wrap each piece in a named XML-style tag and reference that tag by name in the Steps. This tells the model exactly where the material ends and your instructions begin; a markdown header inside a pasted file is otherwise indistinguishable from one you wrote.

**Conventions:** lowercase `snake_case`, descriptive, short (`<codebase>`, `<student_draft>`, `<q3_financials>`). Open and close tags on their own lines. Reference them by name: "Review the code in `<codebase>`," not "Review the code above."

**Before** — instruction and data run together:

```
Summarize this for the board:
Q3 Revenue: $4.2M (down 11% YoY)
Focus on overhead risk and keep it to three bullets.
```

**After** — unambiguous:

```
Summarize the figures in <q3_financials> for the board.
Focus on overhead risk. Output: exactly three bullets, one sentence each.

<q3_financials>
Q3 Revenue: $4.2M (down 11% YoY)
</q3_financials>
```

Skip tags when there is no injected content (e.g. "convert this CSV to JSON" with nothing else present). Full rationale, cross-vendor notes, and diagnostics: [PROMPT_STRUCTURE_GUIDE.md](PROMPT_STRUCTURE_GUIDE.md).

---

## Verification Levels

Choose based on stakes:

| Level | When to Use | What to Add |
|-------|-------------|-------------|
| **Quick** | Standard work | Self-check checklist (always include) |
| **Medium** | Important decisions | + Assumptions stated + Evidence cited |
| **High** | Critical/production | + Adversarial stress-test (QA-02): "List 3 ways this could be wrong" |

---

## Minimal Example

```markdown
# Code Security Review

**Objective:** Identify security vulnerabilities in the provided codebase.

---

## Inputs / Context

**Required:**
- Codebase or file paths to review
- Tech stack (language, framework)

**If any required input is missing:** Ask clarifying questions before proceeding.

---

## Constraints

**Must:**
- Cite file path and line number for each finding
- Prioritize by severity (Critical/High/Medium/Low)

**Must Not:**
- Invent vulnerabilities not evidenced in code
- Skip OWASP Top 10 categories

---

## Steps

1. Scan codebase for security anti-patterns
2. For each finding, document: location, issue, impact, fix
3. Prioritize findings by severity
4. Summarize patterns and recommend next actions

---

## Output Format

### Executive Summary
[1-2 sentence overview]

### Findings
| Severity | File:Line | Issue | Recommendation |
|----------|-----------|-------|----------------|
| ... | ... | ... | ... |

### Patterns Observed
[Recurring issues or systemic problems]

---

## Verification

**Quick self-check:**
- [ ] All OWASP Top 10 categories considered
- [ ] Every finding has file:line citation
- [ ] Severity is justified
```

---

## Copy or Mark — Never Infer (anti-fabrication rule)

Every **ID, category, family name, path, and cross-reference** must be **copied verbatim** from a real source (an existing file, the technique index, or the idea you were given), or written as `[UNVERIFIED — assign at ingestion]`. Do **not** fill an unknown with the most plausible value. If a convention isn't stated where you're working, that absence *is the finding* — flag it; don't invent.

This one rule eliminates the most common authoring errors: a `category:` derived from the folder path instead of the convention, a `related_prompts:` link to a file that doesn't exist, and a technique ID cited from memory that collides with a different live technique.

- **`category:`** — copy the convention, don't mirror the directory path. Software-engineering prompts use `code-analysis/<sub>`, not `software-engineering/analysis/<sub>`; decision prompts use `decision-making/<sub>`.
- **`related_prompts:`** — cite only paths you have confirmed exist. If you can't confirm, omit the link or mark it `[UNVERIFIED]`.
- **`techniques:`** — every ID must exist in the [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md). Reference integrity is enforced by [`audit_technique_index.py`](../techniques/audit_technique_index.py).

## Example Output must be fenced

Wrap the entire Example Output body in **one fenced code block**. Its internal `#`/`##` headings must not enter the document's own outline. Make it *one internally-consistent scenario* whose findings reference each other — not disconnected fragments.

## Decision-forcing prompts: state the verdict rule (analysis / evaluation / decision only)

If the prompt's job is to judge, end it with a **mechanical verdict rule** that includes an insufficiency branch, so a forced verdict never fabricates a finding to fire:

```
- VERDICT-A iff [condition]            (e.g. REQUEST CHANGES iff ≥1 Blocking)
- VERDICT-B iff [condition]
- INSUFFICIENT EVIDENCE iff [condition], plus the single cheapest datum that unblocks the verdict.
No verdict outside this list may be emitted; "it depends" is banned.
```

See [PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) → *Tier 1+ House-Style Patterns* for the full set (two-axis output, evidence-or-drop, negative-space accounting, mirror-image QA-20, decision-forcing output, loop-closure, and the proportionality/anti-moralizing tightenings).

---

## Related Resources

- **Technique reference:** [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md)
- **Pattern by use case:** [Use Case Lookup](../techniques/USE_CASE_LOOKUP.md)
- **Checklist for adding:** [NEW_RESOURCE_CHECKLIST.md](NEW_RESOURCE_CHECKLIST.md)
- **Fast technique picker:** [TECHNIQUE_PICKER_FAST.md](TECHNIQUE_PICKER_FAST.md)
- **Structuring prompts & delimiting content:** [PROMPT_STRUCTURE_GUIDE.md](PROMPT_STRUCTURE_GUIDE.md)

---

**Last Updated:** 2026-06-11
