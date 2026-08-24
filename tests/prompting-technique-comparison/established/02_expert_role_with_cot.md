# Established Technique #2: Expert Role + Chain-of-Thought

> **Techniques used:** RP-01 (Expert Role Assignment), RT-01 (Chain-of-Thought), RT-05 (Evidence-Based Reasoning), QA-01 (Chain-of-Verification)
> 
> The repo's recommended approach for complex implementation tasks: assign expertise, require explicit reasoning, demand evidence, then verify.

## Prompt (Single Turn)

```
You are a senior distributed systems engineer with 15 years of experience 
building concurrent Python systems. You have deep expertise in threading 
primitives, lock-free data structures, and production scheduler architectures. 
You've debugged countless race conditions and deadlocks in production.

## Task

Implement a distributed task scheduler with work-stealing in Python.

## Think Through This Step-by-Step

Before writing any code, reason through the following explicitly:

1. **Concurrency analysis**: What shared state exists? Which threads access 
   which state? What are the potential race conditions? What's the lock 
   acquisition order to prevent deadlocks?

2. **Architecture decisions**: How should workers discover each other for 
   work-stealing? Should the scheduler own all queues, or should workers? 
   What's the right granularity for locks?

3. **Failure mode analysis**: What happens when a task throws? When a worker 
   dies? When shutdown races with task submission? When work-stealing races 
   with normal dequeue?

4. **Implementation plan**: In what order should components be built? What 
   are the dependencies between them?

Show your reasoning for each point, then implement.

## Requirements

- **Task**: UUID, priority (CRITICAL/HIGH/NORMAL/LOW), callable + args, 
  creation timestamp, TTL, max retries, attempt count, status 
  (PENDING/RUNNING/COMPLETED/FAILED/EXPIRED/DEAD_LETTERED)
- **PriorityTaskQueue**: thread-safe, priority+FIFO ordered, dequeue with 
  timeout, peek, size, is_empty
- **Worker**: own thread, assigned queue, work-steals from busiest queue 
  (from back), exception isolation, reports to scheduler
- **DeadLetterQueue**: exhausted tasks + failure reasons + timestamps, 
  list/filter/drain
- **Scheduler**: configurable worker pool, task distribution, retry with 
  exponential backoff (1s, 2s, 4s...), TTL expiration, metrics 
  (submitted/completed/failed/expired/dead_lettered, avg_latency, queue_depths), 
  graceful shutdown (stop accepting → wait in-flight → collect unstarted → 
  join → report)

## Edge Cases (require explicit handling)

For each, cite the exact code location that handles it:
- Submit after shutdown → SchedulerShutdownError
- Task exception → catch, retry, DLQ
- Worker thread dies → detect and restart
- All idle → efficient wait (no busy-spin)
- Steal from empty → no-op
- Concurrent submit → thread-safe
- TTL=0 → immediately expired
- max_retries=0 → DLQ on first failure

## Verification

After implementation, verify your own work:
- Walk through a task's complete lifecycle (submit → queue → dequeue → execute → complete)
- Walk through a failing task's lifecycle (submit → fail → retry → retry → DLQ)
- Walk through shutdown during active processing
- Identify any remaining thread-safety gaps

## Deliverable

Single Python file. Standard library only. Type hints throughout. Include 
`__main__` demo with 4 workers, 20 mixed tasks, mid-run metrics, shutdown.
```

## What This Tests

- Does expert persona + explicit reasoning chain + evidence requirement + self-verification improve output?
- This combines 4 of the repo's most impactful techniques
- Direct comparison to Experimental #4 (Trajectory Seeding) and #5 (Adversarial Self-Split)
