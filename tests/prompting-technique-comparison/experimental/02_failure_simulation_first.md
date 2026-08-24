# Experimental Technique #2: Failure Simulation First

> **Hypothesis:** Generating the bad version first primes quality-detection patterns, producing better final output than generating good code directly.

## Prompt (Single Turn)

```
I need you to implement a distributed task scheduler in Python. But we're going 
to do this in three phases — do NOT skip ahead.

## Phase 1: Write the BAD Version

Write the lazy, shortcut version of a task scheduler that a rushed junior developer 
would write on a Friday afternoon. It should technically "work" for the happy path 
but be riddled with real problems. Specifically:

- Use global state instead of proper encapsulation
- Skip thread safety on shared data structures  
- Use bare `except:` clauses that swallow errors
- Use time.sleep() loops instead of proper synchronization primitives
- Hardcode values that should be configurable
- Skip edge cases entirely
- No graceful shutdown (just kill threads)
- No work-stealing (just a single shared queue with no intelligence)

Write this bad version in full. Make it look like real bad code — not a caricature, 
but the kind of thing that actually ships under deadline pressure.

## Phase 2: Eviscerate It

Now write a detailed, line-by-line code review of that bad version. For every 
problem you find:
- Quote the specific bad code
- Explain exactly what will go wrong (race condition? data loss? deadlock?)
- Describe the production scenario where it fails
- State what the correct approach is

Be thorough. Find at least 15 distinct problems.

## Phase 3: Write the REAL Version

Now implement the actual production version. Here are the full requirements:

[Paste TASK_DEFINITION.md here]

This version must have NONE of the problems you identified in Phase 2. Every 
issue you called out in your review must be addressed in this implementation.

At the end, add a brief "Phase 2 → Phase 3 Traceability" section showing which 
Phase 2 finding maps to which Phase 3 code.
```

## What This Tests

- Does writing bad code first activate stronger quality-detection patterns?
- Is the Phase 3 code measurably better than a direct implementation?
- Does the traceability section show genuine connection between critique and code?
- Compare: established RT-01 (Chain-of-Thought) reasons through the problem linearly
