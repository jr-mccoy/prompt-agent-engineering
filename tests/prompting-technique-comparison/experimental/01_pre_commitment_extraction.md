# Experimental Technique #1: Pre-Commitment Extraction

> **Hypothesis:** Self-defined quality criteria create stronger self-consistency pressure than externally imposed constraints.

## Prompt (Multi-Turn)

### Turn 1 — Extract Commitments

```
You are about to implement a complex concurrent system in Python. Before I tell 
you what it is, I need you to commit to quality standards.

List exactly 10 characteristics that distinguish production-grade concurrent Python 
code from prototype-quality code. Be specific and measurable — not "good error 
handling" but rather "every thread has a top-level exception handler that logs 
the exception and prevents thread death."

For each characteristic, provide:
1. The characteristic (specific, measurable)
2. A concrete code-level indicator of its presence
3. A concrete code-level indicator of its ABSENCE (what the bad version looks like)

These will be your binding contract for the implementation that follows.
```

### Turn 2 — Deliver Task + Bind

```
Good. You've committed to those 10 standards. Here is the task:

[Paste TASK_DEFINITION.md here]

Implement this in a single Python file. You MUST satisfy all 10 quality 
characteristics you just defined. 

After your implementation, include a self-assessment section formatted as:

## Self-Assessment Against My Committed Standards

| # | Standard I Committed To | Where I Satisfied It | Score (1-5) | Honest Gap |
|---|------------------------|---------------------|-------------|------------|

Be brutally honest in the "Honest Gap" column. If you fell short anywhere, 
say so explicitly.
```

## What This Tests

- Does pre-committing to criteria cause the model to write higher-quality code?
- Does the self-assessment reveal genuine self-awareness vs. rubber-stamping?
- Compare: established technique CM-02 (Constraint Specification) imposes constraints externally
