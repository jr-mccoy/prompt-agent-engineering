# Chain-of-Verification Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Self-Correction Prompts (Tier 1)

## Prompt

```
[YOUR ANALYSIS REQUEST]

After providing your initial analysis, complete these verification steps:

1. List three specific ways your analysis could be incomplete, misleading, or incorrect
2. For each potential issue, cite specific evidence from [DOCUMENT/DATA] that either confirms or refutes the concern
3. Provide a revised analysis that incorporates verified corrections

Do not skip the verification stage. I need to see your self-critique before the final answer.
```

## Usage Notes

The key is forcing enumeration of *specific* potential errors. Generic "check your work" gets ignored. Requiring evidence citation prevents the model from generating vacuous self-critique.
