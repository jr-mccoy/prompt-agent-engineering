# Established Technique #1: Standard Baseline

> **Techniques used:** ST-01 (Clear Objective), ST-02 (Structured Sequential Instructions), ST-03 (Output Format Specification), CM-01 (Explicit Context Framing), CM-02 (Constraint Specification)
> 
> This is the "bread and butter" combination — the repo's recommended foundation for any coding prompt.

## Prompt (Single Turn)

```
# Distributed Task Scheduler Implementation

**Objective:** Implement a production-grade distributed task scheduler with 
work-stealing, priority queues, dead letter handling, and graceful shutdown 
in Python using only the standard library.

**Context:**
- Language: Python 3.10+
- Concurrency model: threading (not async/await)
- Dependencies: standard library only (threading, queue, time, dataclasses, 
  enum, logging, uuid, typing)
- This is a single-process, multi-threaded system
- No persistence, network communication, or external services

**Constraints:**
- MUST: All shared mutable state protected by synchronization primitives
- MUST: Type hints on all function signatures
- MUST: Single file implementation (scheduler.py)
- MUST: No busy-spinning (use proper wait primitives)
- MUST NOT: Use async/await or external packages
- MUST NOT: Use global state; all state in class instances
- SHOULD: Prefer composition over inheritance
- SHOULD: Use dataclasses and enums for data modeling

**Instructions:**

1. Define the data model:
   - Task dataclass with UUID, priority (CRITICAL/HIGH/NORMAL/LOW enum), 
     callable payload + args, creation timestamp, TTL, max retry count, 
     attempt count, status (PENDING/RUNNING/COMPLETED/FAILED/EXPIRED/DEAD_LETTERED)
   - Custom exceptions: SchedulerShutdownError

2. Implement PriorityTaskQueue:
   - Thread-safe priority queue
   - Enqueue respecting priority; dequeue returns highest priority (CRITICAL first)
   - FIFO within same priority level
   - peek(), size(), is_empty() methods
   - Timeout support on dequeue

3. Implement Worker:
   - Runs in its own thread
   - Pulls tasks from assigned queue
   - Work-stealing: when idle, steal from busiest other worker's queue (from back)
   - Reports task completion/failure to scheduler
   - Exception isolation: one bad task never crashes the worker

4. Implement DeadLetterQueue:
   - Receives tasks exceeding max retries
   - Stores failure reason and all attempt timestamps
   - Supports: list all, filter by error type, drain back to main queue

5. Implement Scheduler:
   - Manages configurable worker pool
   - Distributes tasks (round-robin or least-loaded)
   - Retry with exponential backoff (1s, 2s, 4s...)
   - TTL expiration before execution
   - Metrics: submitted/completed/failed/expired/dead_lettered, avg latency, 
     queue depths per worker
   - Graceful shutdown: stop accepting → wait for in-flight (configurable 
     timeout) → collect unstarted → join threads → return report

6. Handle edge cases:
   - Submit after shutdown → SchedulerShutdownError
   - Task exception → catch, increment retry, re-queue or DLQ
   - Worker thread dies → scheduler detects and restarts
   - All idle, no tasks → efficient wait
   - Steal from empty → graceful no-op
   - Concurrent submit → thread-safe
   - TTL=0 → immediately expired
   - max_retries=0 → DLQ on first failure

7. Write `if __name__ == "__main__"` demo:
   - Create scheduler with 4 workers
   - Submit 20 mixed-priority tasks (some succeed, some fail, some expire)
   - Print metrics mid-run
   - Demonstrate graceful shutdown
   - Print shutdown report

**Expected Output:**
- A single, complete Python file
- All classes implemented with full functionality (no stubs, no TODOs)
- Type hints on all signatures
- Working demo block that can be executed directly
```

## What This Tests

- How far does the standard "clear objective + structured steps + constraints" approach get?
- This is the control group — the baseline all other techniques are measured against
- Uses the 5 most fundamental techniques from the repo
