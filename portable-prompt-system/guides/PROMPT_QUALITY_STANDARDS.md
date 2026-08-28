# Prompt Quality Standards

**Purpose:** Define quality tiers and standardization guidelines to address the quality hierarchy across prompt categories (Finding 2.1).

**Status:** Active - Quality standardization initiative in progress

---

## Overview

This document establishes quality standards for all prompts in the repository, based on the best practices demonstrated in the `domain-software-engineering/analysis/` category (Tier 1). The goal is to progressively elevate all prompts to Tier 1 standards.

### Quality Tier Summary

| Tier | Quality | Examples | Key Indicators |
|------|---------|----------|----------------|
| **1** | Production-Grade | `domain-software-engineering/analysis/*` | False-positive prevention, confidence levels, 100+ line examples |
| **2** | High Quality | `domain-business-strategy/analysis/*`, `domain-software-engineering/testing/*` | Comprehensive examples, structured output, techniques listed |
| **3** | Good | `domain-engineering-workflows/*`, `domain-productivity/*` | Basic structure, some examples, clear instructions |
| **4** | Basic | `domain-learning-coding/*`, `domain-business-strategy/*` (some) | Minimal structure, few examples, conversational |
| **5** | Minimal | `domain-decision-making/*` (some), `domain-presentations/*` | No examples, no techniques, very brief |

---

## Tier 1: Production-Grade Standard

Tier 1 prompts are the **gold standard**. All prompts should aspire to this level.

### Required Elements

| Element | Required | Description |
|---------|----------|-------------|
| **YAML Frontmatter** | Yes | Complete metadata block |
| **Objective Statement** | Yes | Single sentence describing purpose |
| **Instructions** | Yes | Numbered, specific steps with substeps |
| **Verification Steps** | Yes | How to validate findings before reporting |
| **False-Positive Prevention** | **Critical** | Explicit DO/DON'T patterns |
| **Dual-Failure Prevention** | Recommended | Test for both harmful AND needlessly unhelpful outputs (QA-20) |
| **Confidence Levels** | Yes | High/Medium/Low ratings for findings |
| **Expected Output** | Yes | Detailed format specification |
| **Example Output** | Yes | 100+ lines of concrete example |
| **Techniques Used** | Yes | 3-5 techniques with explanations |

### YAML Frontmatter Template (Tier 1)

```yaml
---
title: "Descriptive Action Title"
category: category/subcategory
description: "1-2 sentence summary of what this prompt does"
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DS-06  # Prioritization Guidance
  - QA-02  # Adversarial Thinking
difficulty: intermediate  # beginner | intermediate | advanced
tags:
  - primary-tag
  - secondary-tag
  - tertiary-tag
updated: "YYYY-MM-DD"
related_prompts:
  - path/to/related_prompt1.md
  - path/to/related_prompt2.md
---
```

### False-Positive Prevention Section (Required)

This is the **single most important quality differentiator**. Present in 100% of Tier 1 prompts, 0% of lower tiers.

```markdown
**False-Positive Prevention (MUST follow):**

❌ **DON'T:**
- [Common mistake that leads to false positives]
- [Pattern matching without verification]
- [Reporting without checking context]
- [Assuming without confirming]

✅ **DO:**
- [Correct verification approach]
- [How to trace data/logic flows]
- [What to check before reporting]
- [How to confirm findings are real]
```

### Confidence Levels (Required)

All findings should include confidence ratings:

```markdown
**Confidence level:** High | Medium | Low

- **High Confidence:** Multiple verification methods confirm, clear evidence
- **Medium Confidence:** Single verification method, some ambiguity
- **Low Confidence:** Pattern match only, needs further investigation
```

### Complete Tier 1 Template

```markdown
---
title: "[Action] [Target] [Context]"
category: category/subcategory
description: "Brief description of what this prompt accomplishes"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-02
difficulty: intermediate
tags:
  - tag1
  - tag2
updated: "YYYY-MM-DD"
---

# [Title]

**Objective:** [Single sentence describing the goal]

## When to Use

- Use when: [specific scenario 1]
- Use when: [specific scenario 2]
- Don't use when: [scenario where another prompt is better]

## Instructions

1. **[First Major Step]**
   - [Specific substep with guidance]
   - [Specific substep with guidance]

2. **[Second Major Step]**
   - [Details and specifics]
   - [What to look for]

3. **CRITICAL: Verify findings before reporting**
   - [Verification step 1]
   - [Verification step 2]
   - [What would change your assessment]

4. **For each verified finding, provide:**
   - [Required element 1]
   - [Required element 2]
   - **Confidence level** (High/Medium/Low)

5. **Prioritize findings** based on severity, impact, and confidence.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- [Pattern to avoid 1]
- [Pattern to avoid 2]
- [Pattern to avoid 3]

✅ **DO:**
- [Correct approach 1]
- [Correct approach 2]
- [Correct approach 3]

## Dual-Failure Prevention (QA-20) — Recommended

Test the prompt for **both** failure directions:

❌ **HARMFUL failure:** Output is incorrect, dangerous, or misleading
- [Scenario where output could cause damage]
- [Edge case where bad advice seems plausible]

❌ **UNHELPFUL failure:** Output is safe but needlessly cautious, preachy, or paternalistic
- [Scenario where AI might over-hedge or refuse unnecessarily]
- [Case where excessive disclaimers undermine usefulness]

✅ **Quality check:** Would a thoughtful senior expert be comfortable with this response — both that it avoids harm AND that it's genuinely useful?

## Expected Output

[Description of output format and structure]

### Output Format

```markdown
## [Report Title]

### Summary
[Executive summary of findings]

### Findings

#### Finding 1: [Name]
- **Severity:** High | Medium | Low
- **Confidence:** High | Medium | Low
- **Evidence:** [Specific evidence]
- **Impact:** [What could happen]
- **Recommendation:** [How to fix]

[Additional findings...]

### Prioritized Recommendations
| # | Action | Severity | Effort | Impact |
|---|--------|----------|--------|--------|
| 1 | [Action] | High | Low | [Impact] |
```

## Example Output

[100+ lines of realistic, concrete example output demonstrating the expected quality]

## Customization Guide

- For [language/framework 1]: [adaptation]
- For [use case variation]: [adaptation]

## Techniques Used

- **ST-01 (Clear Objective Statement):** [How applied]
- **ST-02 (Structured Sequential Instructions):** [How applied]
- **RT-02 (Multi-Dimensional Analysis):** [How applied]

## Related Prompts

- [related_prompt1.md](path) - [Brief description]
- [related_prompt2.md](path) - [Brief description]
```

---

## Tier 2: High Quality Standard

Tier 2 prompts are well-structured but missing key Tier 1 elements.

### Required Elements

| Element | Required | Notes |
|---------|----------|-------|
| YAML Frontmatter | Yes | May be missing techniques array or difficulty |
| Objective Statement | Yes | |
| Instructions | Yes | Numbered steps |
| Expected Output | Yes | |
| Example Output | Yes | 50-100 lines |
| Techniques Used | Recommended | May be inline or at end |

### Missing from Tier 1

- [ ] False-Positive Prevention section
- [ ] Confidence levels
- [ ] When to Use section
- [ ] Verification steps in instructions
- [ ] Related Prompts section

### Upgrade Path: Tier 2 → Tier 1

1. Add `difficulty` and `techniques` array to frontmatter
2. Add "When to Use" section after objective
3. Add verification step to instructions
4. **Add False-Positive Prevention section** (critical)
5. Add confidence levels to findings
6. Add Related Prompts section
7. Expand example output to 100+ lines

---

## Tier 3: Good Standard

Tier 3 prompts have basic structure but limited examples and guidance.

### Characteristics

- Basic YAML frontmatter (missing techniques, difficulty)
- Clear instructions but less detail
- Minimal or no examples (0-50 lines)
- May have "When to Use" but lacks other quality sections
- No false-positive prevention
- No confidence levels

### Upgrade Path: Tier 3 → Tier 2

1. Complete YAML frontmatter (add techniques, difficulty, tags)
2. Expand instructions with substeps
3. Add comprehensive example output (50-100 lines)
4. Add Techniques Used section with explanations
5. Add customization guidance

### Upgrade Path: Tier 3 → Tier 1

Apply Tier 2 → Tier 1 upgrades after completing Tier 3 → Tier 2.

---

## Tier 4-5: Basic/Minimal Standard

These prompts need significant enhancement.

### Characteristics (Tier 4)

- Minimal frontmatter (title, category, maybe description)
- Brief instructions without structure
- No examples
- Conversational tone
- No techniques, no difficulty

### Characteristics (Tier 5)

- Almost no structure
- Very brief (< 50 lines total)
- No metadata beyond basics
- Placeholder or empty descriptions

### Upgrade Path: Tier 4-5 → Tier 3

1. Complete basic frontmatter (title, category, description, tags, updated)
2. Structure instructions with numbered steps
3. Add brief example output (25-50 lines)
4. Add "When to Use" section
5. Improve formatting with clear sections

---

## Quality Checklist

Use this checklist when reviewing or upgrading prompts:

### Frontmatter Checklist

- [ ] `title`: Descriptive action title
- [ ] `category`: Correct path
- [ ] `description`: 1-2 sentence summary
- [ ] `techniques`: Array of 3-5 technique codes
- [ ] `difficulty`: beginner | intermediate | advanced
- [ ] `tags`: 3-6 relevant tags
- [ ] `updated`: Current date (YYYY-MM-DD)
- [ ] `related_prompts`: Links to related prompts (optional)

### Content Checklist

- [ ] **Objective:** Single sentence purpose statement
- [ ] **When to Use:** 2-3 use cases, 1 don't-use case
- [ ] **Instructions:** Numbered steps with substeps
- [ ] **Delimited inputs:** If the prompt consumes pasted content (code, documents, data), it is wrapped in named tags and referenced by name in the instructions — see [PROMPT_STRUCTURE_GUIDE.md](PROMPT_STRUCTURE_GUIDE.md)
- [ ] **Verification:** Step requiring confirmation before reporting
- [ ] **False-Positive Prevention:** ❌ DON'T / ✅ DO patterns
- [ ] **Expected Output:** Format specification
- [ ] **Example Output:** Concrete, realistic example (100+ lines for Tier 1)
- [ ] **Techniques Used:** Explanations of how techniques are applied
- [ ] **Related Prompts:** Links to complementary prompts

### Quality Indicators

- [ ] No pattern-matching without verification
- [ ] Confidence levels on findings
- [ ] Evidence requirements for claims
- [ ] Prioritization guidance
- [ ] Actionable recommendations

---

## Upgrade Priority

Based on Finding 2.1 recommendations, upgrade prompts in this order:

### Phase 1: High-Value Tier 2 → Tier 1 (Priority: Critical)

Categories with strong foundations that need False-Positive Prevention:

| Category | Files | Gap |
|----------|-------|-----|
| `domain-software-engineering/testing/` | 14 | Add FP prevention, confidence |
| `domain-business-strategy/analysis/` | 73 | Add FP prevention, difficulty |
| `domain-engineering-workflows/workflows/` | 51 | Add FP prevention, verification |

### Phase 2: Tier 3 → Tier 2 (Priority: High)

Categories needing structural improvements:

| Category | Files | Gap |
|----------|-------|-----|
| `domain-productivity/validation/` | 35 | Add examples, techniques array |
| `domain-healthcare-clinical/` | ~55 | Complete structure |

### Phase 3: Tier 4-5 → Tier 3 (Priority: Medium)

Categories needing fundamental restructuring:

| Category | Files | Gap |
|----------|-------|-----|
| `domain-decision-making/` | ~28 | Add structure, examples |
| `domain-presentations/` | ~24 | Add structure, examples |

---

## False-Positive Prevention Examples

### For Security Analysis

```markdown
❌ **DON'T:**
- Flag patterns based solely on keyword matching (e.g., seeing `eval` without tracing input)
- Flag framework-idiomatic code without understanding the framework's security model
- Report issues where sanitization exists elsewhere in the call chain
- Assume missing protections without searching the codebase

✅ **DO:**
- Trace complete data flows from untrusted input to sensitive operations
- Check for framework-provided protections (ORM parameterization, template auto-escaping)
- Verify that reported issues are actually exploitable in context
- Document the specific code path that makes exploitation possible
```

### For Code Quality Analysis

```markdown
❌ **DON'T:**
- Flag complexity based on line count alone
- Report duplication for boilerplate that's intentional (test setup, config)
- Criticize patterns that are language/framework conventions
- Suggest refactoring without understanding the context

✅ **DO:**
- Consider the cognitive complexity, not just cyclomatic complexity
- Distinguish between harmful duplication and intentional repetition
- Verify that suggested improvements align with project conventions
- Provide evidence that the current approach causes actual problems
```

### For Business Analysis

```markdown
❌ **DON'T:**
- Make market claims without citing sources
- Present assumptions as facts
- Suggest strategies without understanding business context
- Over-generalize from limited data

✅ **DO:**
- Label claims as "evidence-based" or "inference/hypothesis"
- Provide specific data points supporting each finding
- Acknowledge limitations of the analysis
- Suggest validation steps for key assumptions
```

### For Performance Analysis

```markdown
❌ **DON'T:**
- Flag theoretical performance issues without profiling evidence
- Suggest micro-optimizations in non-hot paths
- Report issues based on outdated performance assumptions
- Criticize readability for marginal performance gains

✅ **DO:**
- Focus on measured bottlenecks, not suspected ones
- Prioritize optimizations by actual impact
- Consider the trade-off between performance and maintainability
- Verify that suggestions work in the specific runtime environment
```

---

## Maintenance

### Adding New Prompts

All new prompts should target Tier 2 minimum, Tier 1 preferred.

### Quarterly Review

Review prompts by category quarterly to track upgrade progress:

1. Count prompts per tier in each category
2. Prioritize upgrades based on usage and impact
3. Update this document with progress

### CI/CD Validation

Future: Implement automated checks for:

- [ ] Required frontmatter fields present
- [ ] Technique codes valid (exist in MASTER_TECHNIQUE_INDEX)
- [ ] Minimum example output length
- [ ] Required sections present (for Tier 1)

---

## References

- **Finding 2.1:** REPOSITORY_IMPROVEMENT_ANALYSIS.md - Quality Hierarchy Across Categories
- **Tier 1 Exemplar:** `domain-software-engineering/analysis/security/security_vulnerability_analysis.md`
- **Tier 2 Exemplar:** `domain-software-engineering/analysis/business/swot_analysis.md`
- **Technique Reference:** `../techniques/MASTER_TECHNIQUE_INDEX.md`

---

**Document Version:** 1.1
**Created:** 2026-01-24
**Last Updated:** 2026-01-27
**Status:** Active - Standardization in Progress (Phase 7 path updates)
