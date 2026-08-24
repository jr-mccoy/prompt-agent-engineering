# Adversarial Stress-Test Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Self-Correction Prompts (Tier 1)

## Prompt

```
[YOUR INITIAL REQUEST AND MODEL RESPONSE]

Now attack your previous answer:

1. Identify five specific ways it could be wrong, incomplete, or fail under adversarial conditions
2. For each vulnerability, rate severity (Critical/High/Medium/Low) and likelihood (Likely/Possible/Unlikely)
3. Propose specific revisions to address each issue
4. Provide the hardened version incorporating all improvements

Be aggressive in finding problems - I need stress-testing, not validation.
```

## Usage Notes

Deploy this for high-stakes decisions where you need the model to find problems even if it has to stretch. The severity/likelihood framework prevents the model from treating all critiques as equally important.
