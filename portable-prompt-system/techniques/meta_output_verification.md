---
title: "Output Verification Request"
category: meta
description: ""
tags:
  - meta
updated: "2025-12-24"
---

# Output Verification Request

Use this after you receive output from an agent to verify it meets your standards before using it.

## Purpose

A meta-prompt for validating AI output. Checks sources, confidence, assumptions, and limitations.

## Techniques Used
- **DS-02**: Evidence-Based Decision Making - Source verification
- **RT-02**: Explicit Uncertainty Quantification - Confidence flags
- **QA-01**: Self-Critique Triggers - Assumptions and contradictions
- **ST-07**: Actionable Output Requirements - Next action options
- **QA-02**: Adversarial Thinking Prompts - Surprises and "too good to be true"

## The Prompt

```
Before I use this output, show me your work.

PROVIDE:

1. **Sources used**
   - List every source with clickable URLs
   - Note which claims came from which source
   - Highlight any claim that has only a single source

2. **Confidence assessment**
   - Flag any data points you're less than 90% confident about
   - Explain what made verification difficult
   - Note what would increase your confidence

3. **Assumptions made**
   - List every assumption you made that I didn't explicitly specify
   - For each, explain why you chose that interpretation
   - Highlight assumptions that, if wrong, would significantly change the output

4. **Contradictions or surprises**
   - Note anywhere your sources conflicted
   - Highlight anything that surprised you or contradicted expectations
   - Flag information that seems too good to be true

5. **Gaps or limitations**
   - What did you look for but couldn't find?
   - What would have improved this output that was outside your capability?
   - What follow-up would you recommend?

---

Based on this review, I'll decide whether to:
- Use the output as-is
- Request specific corrections
- Verify specific claims myself
- Request additional research

If you cannot provide sources for a claim, remove that claim from the output rather than leaving it unverified.
```

## When to Use

- After receiving research output
- Before sharing AI-generated content externally
- When stakes are high (financial, legal, reputational)
- To build trust in AI output quality

## Why This Works

Creates transparency about:
1. **Provenance**: Where information came from
2. **Reliability**: How confident to be
3. **Interpretation**: What was assumed
4. **Conflicts**: Where sources disagreed
5. **Incompleteness**: What's missing

## Key Principle

The final instruction—"If you cannot provide sources for a claim, remove that claim"—ensures unsourced claims don't slip through.
