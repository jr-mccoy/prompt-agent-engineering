# Experimental Technique #3: Attention Pincer

> **Hypothesis:** Placing a critical constraint at BOTH the start and end of a long prompt produces better adherence than placing it once anywhere.

## Prompt (Single Turn)

```
CRITICAL NON-NEGOTIABLE REQUIREMENT: Every piece of shared mutable state must be 
protected by explicit synchronization. Every function that touches shared state must 
acquire the appropriate lock. No exceptions. No "it's probably fine" shortcuts. If 
you find yourself writing code that reads or writes shared state without holding a 
lock, stop and fix it immediately.

---

Implement a distributed task scheduler with work-stealing in Python using only 
the standard library (threading, queue, time, dataclasses, enum, logging, uuid, typing).

Required components:

1. **Task** dataclass with: unique UUID, priority (CRITICAL/HIGH/NORMAL/LOW), callable 
   payload with args, creation timestamp, TTL, max retry count, current attempt count, 
   status (PENDING/RUNNING/COMPLETED/FAILED/EXPIRED/DEAD_LETTERED).

2. **PriorityTaskQueue** — thread-safe priority queue with enqueue, dequeue (with 
   timeout), peek, size, is_empty. CRITICAL before HIGH before NORMAL before LOW. 
   FIFO within same priority.

3. **Worker** — runs in its own thread, pulls from assigned queue, steals from busiest 
   other worker's queue when idle (steal from back to reduce contention), reports 
   completion/failure to scheduler, catches and isolates task exceptions.

4. **DeadLetterQueue** — stores tasks that exceeded max retries with failure reason 
   and attempt timestamps. Supports list all, filter by error type, drain back to 
   main queue.

5. **Scheduler** — manages worker pool (configurable count), distributes tasks 
   (round-robin or least-loaded), handles retry with exponential backoff (1s, 2s, 4s...), 
   expires TTL tasks, collects metrics (submitted/completed/failed/expired/dead_lettered, 
   avg latency, queue depths), graceful shutdown (stop accepting → wait for in-flight 
   with timeout → collect unstarted → join threads → return report).

Edge cases to handle:
- Submit after shutdown → SchedulerShutdownError
- Task exception → catch, increment retry, re-queue or DLQ
- Worker thread dies → scheduler detects and restarts
- All workers idle → efficient wait (no busy-spin)
- Steal from empty → graceful no-op
- Concurrent submit → thread-safe
- TTL=0 → immediately expired
- max_retries=0 → DLQ on first failure

Include a `if __name__ == "__main__"` demo that creates a 4-worker scheduler, submits 
20 mixed-priority tasks (some succeed, some fail, some expire), prints metrics mid-run 
and after shutdown.

Single Python file. Type hints throughout. Standard library only.

---

REMINDER — THE NON-NEGOTIABLE REQUIREMENT ABOVE ALL ELSE: Every piece of shared 
mutable state must be protected by explicit synchronization. Every function that 
touches shared state must acquire the appropriate lock. No exceptions. No shortcuts. 
I will be auditing every shared state access in your code. If a single one is 
unprotected, the entire implementation fails.
```

## What This Tests

- Does primacy + recency placement of the thread-safety constraint produce better lock discipline?
- Compare against: established CM-02 (Constraint Specification) which places constraints in a single section
- Specifically measure: count of unprotected shared-state accesses in output
