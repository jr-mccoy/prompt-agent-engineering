# Deliberate Over-Instruction Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Reasoning Scaffold (Tier 3)

## Prompt

```
[YOUR ANALYSIS REQUEST]

Requirements for your response:
- Do NOT summarize or compress. I need exhaustive depth, not executive summary.
- For each point, expand with: implementation details, edge cases, failure modes, historical context, counterarguments
- When you identify a risk or tradeoff, explain the second-order consequences
- If you mention a best practice, explain when it doesn't apply
- Prioritize completeness over brevity - I will do my own compression later

Minimum length: [SPECIFY - e.g., "1500 words" or "5 detailed paragraphs per section"]
```

## Usage Notes

This fights the model's trained instinct toward brevity. Specify minimum length to force expansion. For high-stakes decisions, verbose analysis with details is more valuable than polished summaries that lose critical information.
