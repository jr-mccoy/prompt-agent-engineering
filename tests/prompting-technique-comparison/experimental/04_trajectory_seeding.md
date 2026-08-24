# Experimental Technique #4: Trajectory Seeding

> **Hypothesis:** Providing a specific first reasoning step produces better output than generic "think step by step" instructions.

## Prompt (Single Turn)

```
Implement a distributed task scheduler with work-stealing in Python.

Think about this as follows: "The first thing I need to reason through is 
the concurrency model — what shared state exists, which threads access it, 
what the lock ordering should be, and where deadlocks could occur. Let me 
map out every piece of mutable shared state and its access pattern before 
I write a single line of implementation code."

Now, following that reasoning trajectory, implement the full system:

Requirements:
- Task dataclass: UUID, priority (CRITICAL/HIGH/NORMAL/LOW), callable + args, 
  creation timestamp, TTL, max retries, attempt count, status enum 
  (PENDING/RUNNING/COMPLETED/FAILED/EXPIRED/DEAD_LETTERED)
- PriorityTaskQueue: thread-safe, priority-ordered, FIFO within priority, 
  dequeue with timeout, peek, size, is_empty
- Worker: own thread, pulls from assigned queue, work-steals from busiest 
  queue when idle (steal from back), exception isolation, reports to scheduler
- DeadLetterQueue: stores exhausted tasks with failure reasons and timestamps, 
  list/filter/drain operations
- Scheduler: configurable worker pool, task distribution (round-robin or 
  least-loaded), retry with exponential backoff, TTL expiration, metrics 
  (submitted/completed/failed/expired/dead_lettered/avg_latency/queue_depths), 
  graceful shutdown (stop accepting → wait for in-flight → collect unstarted → 
  join threads → return report)

Edge cases: submit after shutdown (SchedulerShutdownError), task exceptions 
(catch → retry → DLQ), worker death (detect → restart), idle wait (no 
busy-spin), empty steal (no-op), concurrent submit (safe), TTL=0 (expired), 
max_retries=0 (DLQ on first failure).

Single Python file. Type hints. Standard library only (threading, queue, time, 
dataclasses, enum, logging, uuid, typing). Include __main__ demo with 4 workers, 
20 mixed tasks, mid-run metrics, graceful shutdown.
```

## What This Tests

- Does seeding the first thought toward "concurrency model analysis" improve thread safety?
- Compare against: established RT-01 (Chain-of-Thought) which says "think step by step"
- Specifically measure: quality of lock discipline, presence of deadlock prevention, 
  whether a shared-state analysis actually appears in the output
