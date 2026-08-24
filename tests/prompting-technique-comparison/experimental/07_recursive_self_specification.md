# Experimental Technique #7: Recursive Self-Specification

> **Hypothesis:** A model writing its own prompt produces better output than a human-written prompt, because the model knows its own failure modes.

## Prompt (Multi-Turn)

### Turn 1 — Self-Prompting

```
You are about to implement a complex concurrent system: a distributed task 
scheduler with work-stealing in Python (standard library only).

Before you implement anything, write the ideal prompt that would cause a 
coding AI to produce a FLAWLESS implementation. This prompt should:

1. Include every constraint the AI needs to avoid common mistakes
2. Call out specific pitfalls for concurrent Python code
3. Specify edge cases that AI models typically miss
4. Include quality gates that prevent lazy shortcuts
5. Define the exact output structure
6. Add whatever guardrails you think are necessary

The system needs: Task dataclass (UUID, priority levels, TTL, retries, status enum), 
PriorityTaskQueue (thread-safe, priority+FIFO ordering), Workers (own threads, 
work-stealing from busiest queue), DeadLetterQueue (failed tasks, inspection, drain), 
Scheduler (worker pool, retry with backoff, TTL expiration, metrics, graceful shutdown).

Write this prompt. Make it the most effective prompt you can design. Be specific 
about what goes wrong with AI-generated concurrent code and guard against it.
```

### Turn 2 — Execute Self-Prompt

```
Now execute the prompt you just wrote. Follow every instruction, constraint, 
and quality gate you specified. This is your own standard — meet it.
```

## What This Tests

- What pitfalls does the model identify that humans wouldn't think to constrain?
- Is the self-generated prompt more effective than the human-written established prompts?
- Does the model actually follow its own prompt more faithfully than an external one?
- Compare against: established technique stack CM-01 + CM-02 + DS-107 + ST-16 + QA-01
