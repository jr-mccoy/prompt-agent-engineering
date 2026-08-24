# New Prompt Template

**Purpose:** Copy-paste template for creating consistent, high-quality prompts. Works with any AI model.

> **Technique IDs:** All IDs referenced here (ST-01, RT-02, etc.) are from the canonical [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md). Do not invent new IDs.

---

## Quick Start: Copy This Template

```markdown
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

## Related Resources

- **Technique reference:** [Master Technique Index](../techniques/MASTER_TECHNIQUE_INDEX.md)
- **Pattern by use case:** [Use Case Lookup](../techniques/USE_CASE_LOOKUP.md)
- **Checklist for adding:** [NEW_RESOURCE_CHECKLIST.md](NEW_RESOURCE_CHECKLIST.md)
- **Fast technique picker:** [TECHNIQUE_PICKER_FAST.md](TECHNIQUE_PICKER_FAST.md)
- **Structuring prompts & delimiting content:** [PROMPT_STRUCTURE_GUIDE.md](PROMPT_STRUCTURE_GUIDE.md)

---

**Last Updated:** 2026-01-31
