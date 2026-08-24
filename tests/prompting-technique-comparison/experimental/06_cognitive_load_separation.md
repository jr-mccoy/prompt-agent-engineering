# Experimental Technique #6: Cognitive Load Separation

> **Hypothesis:** Splitting architecture decisions and implementation into separate passes produces better results than a single combined generation.

## Prompt (Multi-Turn)

### Turn 1 — Architecture Only

```
Design the architecture for a distributed task scheduler with work-stealing in Python.

Output ONLY the following — do NOT write any implementation code:

1. **File structure and class diagram** (text-based)
   - Every class with its responsibilities
   - Inheritance/composition relationships

2. **Complete type definitions**
   - Every enum, dataclass, and custom exception
   - Full type signatures, no implementation

3. **Every method signature with types**
   - Full function signatures for every public and private method
   - Include parameter types and return types
   - One-line docstring per method describing what it does

4. **Shared state map**
   - Every piece of mutable shared state
   - Which threads access it
   - What lock protects it
   - Lock acquisition ordering to prevent deadlocks

5. **Data flow diagram** (text-based)
   - How a task flows from submission to completion
   - How a task flows from failure to retry to DLQ
   - How work-stealing triggers and executes
   - How graceful shutdown propagates

6. **Edge case catalog**
   - Every edge case from requirements
   - Which component handles it
   - What the expected behavior is

Requirements for the system:
- Task with UUID, priority (CRITICAL/HIGH/NORMAL/LOW), callable + args, timestamps, 
  TTL, max retries, attempt count, status enum
- PriorityTaskQueue: thread-safe, priority+FIFO ordered, dequeue timeout, peek
- Worker: own thread, pulls from queue, steals from busiest when idle (from back), 
  exception isolation
- DeadLetterQueue: exhausted tasks + failure reasons, list/filter/drain
- Scheduler: worker pool, task distribution, retry with exponential backoff, TTL 
  expiration, metrics, graceful shutdown with report
- Standard library only (threading, queue, time, dataclasses, enum, logging, uuid, typing)

IMPORTANT: Architecture and signatures ONLY. Zero implementation code.
```

### Turn 2 — Implementation Only

```
Here is the architecture spec you designed. Implement it exactly.

[Paste Turn 1 output here]

Rules for this phase:
- Every class, method, and type from the spec above must be implemented
- Every edge case from the catalog must be handled
- Every lock from the shared state map must be used exactly as specified
- Do not deviate from the architecture — the design decisions are made
- Focus 100% of your effort on implementation quality: correct logic, clean code, 
  proper error handling
- Include a `if __name__ == "__main__"` demo: 4 workers, 20 mixed-priority tasks 
  (some succeed, some fail, some expire), metrics mid-run, graceful shutdown

Single Python file. Type hints throughout.
```

## What This Tests

- Does separating architecture from implementation improve both?
- Is the architecture more thorough when not competing with implementation?
- Is the implementation more correct when architecture is pre-decided?
- Compare against: established DT-01 (Hierarchical Task Breakdown) which decomposes but in a single pass
