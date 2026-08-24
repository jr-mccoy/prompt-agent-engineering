# Reverse Prompting Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Meta-Prompting (Tier 2)

## Prompt

```
You are an expert prompt engineer. Your task is to write the single most effective prompt that would make an LLM solve this problem with maximum accuracy:

[DESCRIBE YOUR TASK AND OBJECTIVES]

Consider:
- What specific details and constraints matter for quality output
- What reasoning steps are essential to avoid common failure modes
- What output format would be most actionable for the end user
- What examples or edge cases would improve reliability

First, write the optimal prompt. Then execute that prompt.
```

## Usage Notes

This works best for unfamiliar domains where you don't know what good looks like. The model's training data includes thousands of examples of effective prompts - leverage that knowledge instead of guessing.
