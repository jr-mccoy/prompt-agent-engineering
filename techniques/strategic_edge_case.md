# Strategic Edge Case Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Self-Correction Prompts (Tier 1)

## Prompt

```
I need you to [TASK]. Here are three calibration examples:

**BASELINE EXAMPLE**
Input: [Simple case where correct approach is obvious]
Correct Output: [What good analysis looks like]
Why this is correct: [Brief reasoning]

**FAILURE MODE EXAMPLE**
Input: [Case where naive approach produces false positive/negative]
Incorrect Output: [What the wrong answer looks like]
Correct Output: [Actual right answer]
Why naive approach fails: [Specific reason the obvious method breaks]

**EDGE CASE EXAMPLE**
Input: [Complex case similar to your actual problem]
Correct Output: [Known good answer]
Why this is tricky: [What makes this boundary case difficult]

Now apply this same reasoning to: [YOUR ACTUAL PROBLEM]
```

## Usage Notes

This is the most labor-intensive template because you need to construct good edge cases. The ROI comes from reusing it across similar problems - build once per problem class, deploy hundreds of times.
