# Temperature Simulation Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Perspective Engineering (Tier 4)

## Prompt

```
Provide three analyses of this decision:

**Analysis 1 - Cautious Junior Analyst**
You are uncertain and risk-aware. Explore what could go wrong, identify uncertainties, explain what we don't know and why that matters. Be verbose about concerns and edge cases.

**Analysis 2 - Confident Senior Expert**
You are decisive based on what's most likely. Provide clear recommendations with concise justification. Focus on the probable path forward, not every possible scenario.

**Analysis 3 - Synthesis**
Integrate both perspectives. Identify:
- Where confidence is justified and we should act decisively
- Where uncertainty is real and we need contingency planning
- What monitoring or staged rollout reduces risk without paralysis

Decision: [YOUR QUESTION]
```

## Usage Notes

This simulates the reasoning diversity you'd get from temperature adjustments without API access. The synthesis reconciles both modes - you get decisiveness where warranted and appropriate caution where uncertainty is genuine.
