# Recursive Optimization Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Meta-Prompting (Tier 2)

## Prompt

```
You are a recursive prompt optimizer.

Current prompt: "[YOUR EXISTING PROMPT]"

Task goal: [SPECIFIC OBJECTIVE AND SUCCESS CRITERIA]

Improve this prompt through three iterations:
- Version 1: Add missing constraints, specifications, and edge case handling
- Version 2: Resolve ambiguities, clarify expectations, improve structure
- Version 3: Enhance reasoning depth and output quality while maintaining clarity

Provide only the final Version 3 prompt, ready for production deployment.
```

## Usage Notes

Use this to harden prompts before scaling them. The three-iteration structure prevents over-optimization - you get systematic improvement without the prompt becoming unwieldy.
