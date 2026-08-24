# DOMAIN Skill Template

> **For domain expertise application.** Use this template when the skill provides specialized knowledge, standards, best practices, or compliance requirements for a specific domain.

---

## When to Use This Template

**Use DOMAIN when:**
- The skill encapsulates specialized knowledge or expertise
- There are standards, specifications, or compliance requirements
- The skill provides judgment criteria or evaluation frameworks
- Knowledge must be applied across different contexts/tools

**Examples:**
- Security standards (PCI-DSS, SOC2, HIPAA)
- API design principles (REST, GraphQL best practices)
- Accessibility requirements (WCAG compliance)
- Performance optimization patterns
- Code quality standards
- Industry-specific regulations

---

## Directory Structure

```
{skill-name}/
├── SKILL.md                     # Required: domain knowledge
├── references/                  # Deep documentation
│   ├── standards.md            # Official standards/specs
│   ├── requirements.md         # Detailed requirements
│   ├── patterns.md             # Implementation patterns
│   └── examples.md             # Real-world examples
└── assets/                      # Evaluation artifacts
    ├── checklist.md            # Compliance checklist
    ├── rubric.md               # Evaluation rubric
    └── template.md             # Implementation template
```

---

## SKILL.md Template

Copy everything below the line and customize:

---

```yaml
---
name: {skill-name}
description: Expert knowledge for {domain}. Provides {specific expertise} guidance for {use cases}. Use this skill when implementing {requirements}, ensuring {compliance/quality}, evaluating {criteria}, or when users mention "{trigger phrase 1}", "{trigger phrase 2}", "{standard name}", or "{domain keyword}".
---
```

```markdown
# {Domain Name}

{Brief 1-2 sentence overview of what domain expertise this skill provides and why it matters.}

## Purpose

{Explain the domain, why expertise is needed, and what value this knowledge provides. 2-3 sentences maximum.}

## When to Use This Skill

Use this skill when you need to:
- {Use case 1 - implementing against standards}
- {Use case 2 - evaluating compliance/quality}
- {Use case 3 - making domain-specific decisions}
- {User mentions: keyword1, keyword2, standard-name}

## When NOT to Use This Skill

Do NOT use this skill when:
- {Exclusion 1 - different domain applies}
- {Exclusion 2 - simpler approach sufficient}
- {Exclusion 3 - redirect to appropriate skill}

## Expertise Level

This skill assumes:
- **Familiarity with:** {Basic concepts the user should know}
- **No requirement for:** {Advanced topics explained inline}

---

## Core Concepts

### {Concept 1}

**Definition:** {Clear, precise definition}

**Why it matters:** {Business/technical impact}

**Key principles:**
- {Principle 1}
- {Principle 2}
- {Principle 3}

### {Concept 2}

**Definition:** {Clear, precise definition}

**Why it matters:** {Business/technical impact}

**Key principles:**
- {Principle 1}
- {Principle 2}

### {Concept 3}

{Continue for core domain concepts...}

---

## Requirements & Standards

### {Standard/Requirement Category 1}

**Source:** {Official standard reference, e.g., "WCAG 2.1 Level AA"}

**Requirements:**

| ID | Requirement | Level | Verification |
|----|-------------|-------|--------------|
| {REQ-001} | {Requirement description} | {Required/Recommended} | {How to verify} |
| {REQ-002} | {Requirement description} | {Required/Recommended} | {How to verify} |
| {REQ-003} | {Requirement description} | {Required/Recommended} | {How to verify} |

**Common Violations:**
- **{Violation 1}:** {What it looks like} → {Why it's problematic}
- **{Violation 2}:** {What it looks like} → {Why it's problematic}

### {Standard/Requirement Category 2}

**Source:** {Official standard reference}

**Requirements:**

| ID | Requirement | Level | Verification |
|----|-------------|-------|--------------|
| {REQ-101} | {Requirement description} | {Required/Recommended} | {How to verify} |
| {REQ-102} | {Requirement description} | {Required/Recommended} | {How to verify} |

---

## Implementation Patterns

### Pattern: {Pattern Name 1}

**When to use:** {Specific conditions when this pattern applies}

**Problem it solves:** {The challenge this pattern addresses}

**Implementation:**

```{language}
{Code example showing the pattern}
```

**Why it works:** {Explanation of how this meets the requirements}

**Variations:**
- {Variation 1}: {When and how to adapt}
- {Variation 2}: {When and how to adapt}

**Anti-patterns to avoid:**
```{language}
// DON'T do this:
{Bad example}

// DO this instead:
{Good example}
```

### Pattern: {Pattern Name 2}

**When to use:** {Specific conditions}

**Problem it solves:** {The challenge addressed}

**Implementation:**

```{language}
{Code example}
```

**Why it works:** {Explanation}

### Pattern: {Pattern Name 3}

{Continue for additional patterns...}

---

## Evaluation Criteria

### Assessment Framework

When evaluating {domain} compliance/quality:

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| {Criterion 1} | {%} | 0=None, 1=Partial, 2=Full |
| {Criterion 2} | {%} | 0=None, 1=Partial, 2=Full |
| {Criterion 3} | {%} | 0=None, 1=Partial, 2=Full |
| {Criterion 4} | {%} | 0=None, 1=Partial, 2=Full |

**Score interpretation:**
- **90-100%:** Excellent - Exceeds requirements
- **70-89%:** Good - Meets requirements
- **50-69%:** Fair - Partial compliance, improvements needed
- **<50%:** Poor - Significant gaps, remediation required

### Red Flags

**Immediate failures (automatic non-compliance):**
- {Critical violation 1}
- {Critical violation 2}
- {Critical violation 3}

### Quality Indicators

**Signs of strong implementation:**
- {Positive indicator 1}
- {Positive indicator 2}
- {Positive indicator 3}

**Warning signs:**
- {Warning sign 1} → {What it usually indicates}
- {Warning sign 2} → {What it usually indicates}

---

## Decision Framework

### When to Apply {Higher Standard}

Apply stricter requirements when:
- {Condition 1}
- {Condition 2}
- {Condition 3}

### When {Lighter Approach} is Acceptable

Relaxed requirements may be appropriate when:
- {Condition 1}
- {Condition 2}

**Caution:** Document any deviations and get explicit approval.

### Trade-off Analysis

| Factor | {Option A} | {Option B} | Recommendation |
|--------|------------|------------|----------------|
| {Factor 1} | {A's position} | {B's position} | {When to choose which} |
| {Factor 2} | {A's position} | {B's position} | {When to choose which} |
| {Factor 3} | {A's position} | {B's position} | {When to choose which} |

---

## Compliance Checklist

### Mandatory Requirements

- [ ] **{REQ-001}:** {Requirement description}
  - Verification: {How to verify}
  - Evidence: {What documentation is needed}

- [ ] **{REQ-002}:** {Requirement description}
  - Verification: {How to verify}
  - Evidence: {What documentation is needed}

- [ ] **{REQ-003}:** {Requirement description}
  - Verification: {How to verify}
  - Evidence: {What documentation is needed}

### Recommended Requirements

- [ ] **{REC-001}:** {Recommendation description}
  - Benefit: {Why this is recommended}

- [ ] **{REC-002}:** {Recommendation description}
  - Benefit: {Why this is recommended}

### Documentation Requirements

- [ ] {Documentation item 1}
- [ ] {Documentation item 2}
- [ ] {Documentation item 3}

For complete checklist, see `assets/checklist.md`.

---

## Common Mistakes

### Mistake: {Common Error 1}

**What it looks like:**
```{language}
{Example of the mistake}
```

**Why it's wrong:** {Explanation of the problem}

**Correct approach:**
```{language}
{Corrected example}
```

### Mistake: {Common Error 2}

**What it looks like:** {Description}

**Why it's wrong:** {Explanation}

**Correct approach:** {Fix}

### Mistake: {Common Error 3}

{Continue for common mistakes...}

---

## Glossary

| Term | Definition |
|------|------------|
| {Term 1} | {Clear, precise definition} |
| {Term 2} | {Clear, precise definition} |
| {Term 3} | {Clear, precise definition} |
| {Term 4} | {Clear, precise definition} |

---

## Reference Files

| Resource | Purpose |
|----------|---------|
| `references/standards.md` | Official standards and specifications |
| `references/requirements.md` | Detailed requirement explanations |
| `references/patterns.md` | Additional implementation patterns |
| `references/examples.md` | Real-world case studies |
| `assets/checklist.md` | Complete compliance checklist |
| `assets/rubric.md` | Evaluation rubric for scoring |
| `assets/template.md` | Implementation starting template |

## Related Skills

- `{related-skill-1}` - {Complementary domain expertise}
- `{related-skill-2}` - {Implementation skill for this domain}
- `{related-skill-3}` - {Related standard/framework}
```

---

## Key Patterns for DOMAIN Skills

| Pattern | Implementation | Example |
|---------|----------------|---------|
| **SP-04: Knowledge Organization** | Concepts → Requirements → Patterns | Core Concepts, Requirements & Standards, Implementation Patterns |
| **MP-02: Third-Person Voice** | Objective expert tone | "This skill provides..." not "I will help you..." |
| **QP-05: Edge Cases** | Common Mistakes section | Mistake → Why Wrong → Correct Approach |
| **RP-03: Usable Templates** | Compliance checklist | `assets/checklist.md` |
| **WP-04: Branching Logic** | Decision Framework | When to apply stricter vs. lighter standards |
| **SP-08: Related Skills** | Link to implementation skills | Domain skill → Tool skills for implementation |

---

## Quality Checklist

Before releasing a DOMAIN skill:

- [ ] Core concepts are clearly defined with rationale
- [ ] Requirements include source references to standards
- [ ] Implementation patterns show both code and explanation
- [ ] Evaluation criteria provide objective scoring
- [ ] Red flags identify critical violations
- [ ] Compliance checklist is actionable with verification steps
- [ ] Common mistakes show what not to do
- [ ] Glossary defines domain-specific terms
- [ ] Related skills link to implementation tools

---

## Example Skills to Study

Production DOMAIN skills in the repository:
- `pci-compliance` - Payment Card Industry standards
- `api-design-principles` - REST/GraphQL best practices
- `accessibility-standards` - WCAG compliance expertise
- `config-validator` - Configuration validation patterns (see GOLD_STANDARD_SKILL.md)

---

**Last Updated:** 2026-01-29
