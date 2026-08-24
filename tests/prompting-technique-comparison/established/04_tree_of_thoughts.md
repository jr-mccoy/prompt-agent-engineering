# Established Technique #4: Tree of Thoughts + Adversarial Stress-Test

> **Techniques used:** RT-03 (Tree of Thoughts), QA-02 (Adversarial Stress-Test), RT-07 (Cascade Effect Analysis)
> 
> The repo's approach for design decisions: explore multiple approaches, stress-test each, analyze cascading effects, then implement the winner.

## Prompt (Single Turn)

```
# Distributed Task Scheduler — Design Exploration + Stress Test

## Phase 1: Generate 3 Architecture Approaches

For a distributed task scheduler with work-stealing in Python (threading, 
standard library only), design 3 distinct architectural approaches:

**Approach A — Centralized Queue Architecture:**
How would this work if the Scheduler owns a single centralized priority 
queue and workers pull from it?

**Approach B — Distributed Queue Architecture:**
How would this work if each Worker owns its own queue and the Scheduler 
distributes tasks across them?

**Approach C — Hybrid Architecture:**
How would this work with per-worker queues plus a shared overflow queue?

For each approach, describe:
1. Component ownership (who owns what state)
2. Lock topology (what locks exist, what they protect)
3. Work-stealing mechanism (how it works under this architecture)
4. Shutdown sequence (how graceful shutdown propagates)

## Phase 2: Adversarial Stress-Test Each Approach

Attack each architecture with these scenarios:
1. **Thundering herd**: 1000 tasks submitted simultaneously by 10 threads
2. **Poison task**: A task that takes 60 seconds (longer than shutdown timeout)
3. **Cascading failure**: Worker 1 dies while stealing from Worker 2's queue
4. **Starvation**: All tasks are LOW priority except one CRITICAL that arrives late
5. **Shutdown race**: `shutdown()` called while `submit()` is mid-execution

For each scenario × each approach, answer:
- What happens? (trace the execution)
- Does it deadlock, lose data, or corrupt state?
- How hard is it to handle correctly?

## Phase 3: Select Winner + Cascade Analysis

Pick the best approach. Explain:
- Why it wins on correctness under stress
- What its remaining weaknesses are
- What design mitigations address those weaknesses

Trace the cascade effects of your choice:
- How does this architecture choice affect work-stealing complexity?
- How does it affect shutdown ordering?
- How does it affect metrics collection?

## Phase 4: Implement the Winner

Full implementation with:
- Task (UUID, priority CRITICAL/HIGH/NORMAL/LOW, callable + args, timestamps, 
  TTL, max_retries, attempt_count, status enum)
- PriorityTaskQueue (thread-safe, priority+FIFO, timeout dequeue, peek)
- Worker (own thread, work-stealing from busiest/back, exception isolation)
- DeadLetterQueue (exhausted tasks, failure reasons, list/filter/drain)
- Scheduler (worker pool, distribution, retry with exponential backoff, 
  TTL expiration, metrics, graceful shutdown with report)

Edge cases: submit after shutdown (SchedulerShutdownError), task exceptions, 
worker death detection/restart, efficient idle wait, empty steal, concurrent 
submit, TTL=0, max_retries=0.

Single Python file. Type hints. `__main__` demo: 4 workers, 20 mixed tasks, 
mid-run metrics, shutdown.
```

## What This Tests

- Does exploring multiple architectures before implementing produce better design?
- Does adversarial stress-testing before implementation prevent bugs?
- Compare against: Experimental #5 (Adversarial Self-Split) which stress-tests AFTER implementation
