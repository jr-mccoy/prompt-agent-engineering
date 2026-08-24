---
title: "Iteration and Refinement Prompt"
category: meta
description: ""
tags:
  - meta
updated: "2025-12-24"
---

# Iteration and Refinement Prompt

Use this when agent output isn't quite right. More effective than starting over or vague "try again" requests.

## Purpose

A meta-prompt for giving structured feedback to improve AI output. Prevents the common failure of vague revision requests.

## Techniques Used
- **OC-01**: Format Specification - KEEP/FIX/ADD/REMOVE structure
- **ST-03**: Constraint Specification - Preserve what works
- **NE-03**: Input Template Scaffolding - Clear feedback categories
- **ST-07**: Actionable Output Requirements - Specific improvements

## The Prompt

```
The output isn't quite right. Here's specific feedback:

**KEEP** (don't change these parts):
- [What worked well - be specific]
- [Structure or sections that are correct]
- [Tone, style, or approach that's right]

**FIX** (these specific problems):
- [Problem 1]: [What's wrong] → [What it should be instead]
- [Problem 2]: [What's wrong] → [What it should be instead]
- [Problem 3]: [What's wrong] → [What it should be instead]

**ADD** (these things are missing):
- [Missing element 1]: [Where it should go and what it should include]
- [Missing element 2]: [Where it should go and what it should include]

**REMOVE** (these things shouldn't be there):
- [Element to remove]: [Why it doesn't belong]

**EXAMPLE OF WHAT I WANT** (if helpful):
[Provide a short example of the style, format, or content you're looking for]

---

Regenerate with these specific adjustments. Preserve everything marked "KEEP."

Do not start from scratch—iterate on what you already produced.

If any of my feedback is unclear, ask before regenerating.
```

## When to Use

- Output is close but not quite right
- Want to refine rather than restart
- Need to preserve good parts while fixing issues
- Giving feedback on drafts

## Why This Works

1. **Preserves progress**: KEEP prevents losing good work
2. **Specific improvements**: FIX has clear before/after
3. **Additions are placed**: ADD says where things go
4. **Removals are reasoned**: REMOVE explains why

## Common Mistakes This Prevents

- "Try again" (vague, loses good parts)
- "Make it better" (unclear improvement direction)
- "I don't like it" (no actionable feedback)
- Restarting entirely (wastes good work)

## Key Instruction

"Do not start from scratch—iterate on what you already produced" prevents the common AI behavior of regenerating everything when only minor changes are needed.
