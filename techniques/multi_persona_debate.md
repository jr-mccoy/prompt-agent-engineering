# Multi-Persona Debate Template

**Source:** ADVANCED_PROMPTING_TECHNIQUES.md
**Category:** Perspective Engineering (Tier 4)

## Prompt

```
Simulate a structured debate between three experts with different priorities:

**Persona 1: [ROLE]**
Priority: [SPECIFIC FOCUS - e.g., "minimize costs including operational burden"]
Must argue for: [THEIR PREFERENCE]

**Persona 2: [ROLE]**
Priority: [SPECIFIC FOCUS - e.g., "maximize security and compliance"]
Must argue for: [THEIR PREFERENCE]

**Persona 3: [ROLE]**
Priority: [SPECIFIC FOCUS - e.g., "optimize for team velocity and maintainability"]
Must argue for: [THEIR PREFERENCE]

Decision to debate: [YOUR QUESTION]

Format:
1. Each persona presents their position (3-4 paragraphs)
2. Each persona critiques the other two positions, identifying specific flaws in their reasoning
3. Synthesis: Reconcile all three perspectives with a recommendation that explicitly addresses each concern and explains which tradeoffs are acceptable and why

The synthesis should NOT be a compromise - it should be the strongest position that survives critique from all three perspectives.
```

## Usage Notes

Personas need genuinely conflicting priorities or you get artificial consensus. Specify what each cares about and why tensions exist. The critique phase is essential - it forces the model to generate substantive counterarguments rather than polite disagreement.
