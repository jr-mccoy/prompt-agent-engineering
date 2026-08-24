# Experimental Technique #5: Adversarial Self-Split

> **Hypothesis:** A motivated adversarial review frame ("bonus for every bug") produces more thorough self-correction than neutral self-review.

## Prompt (Multi-Turn)

### Turn 1 — Generate Implementation

```
Implement a distributed task scheduler with work-stealing in Python.

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

Single Python file. Type hints. Standard library only. Include __main__ demo 
with 4 workers, 20 mixed tasks, mid-run metrics, graceful shutdown.
```

### Turn 2 — Adversarial Review

```
Now switch roles completely. You are a senior concurrency engineer conducting a 
hostile code review. You get paid $1,000 for every real bug, race condition, 
deadlock risk, or correctness issue you find. You get $500 for every design 
flaw. You get NOTHING for compliments.

Review the code you just wrote with the intensity of someone whose mortgage 
payment depends on finding problems.

For each issue found:
1. **Bug ID**: B-001, B-002, etc.
2. **Severity**: CRITICAL / HIGH / MEDIUM / LOW
3. **Location**: exact function/method and what's wrong
4. **Reproduction scenario**: specific sequence of events that triggers the bug
5. **Fix**: exact code change needed

After your review, produce a FIXED version of the complete file that addresses 
every issue rated HIGH or CRITICAL. Show the diff for each fix.
```

## What This Tests

- Does the "paid per bug" frame find more issues than neutral "review your work"?
- How many of the issues found are genuine vs. false positives?
- Compare against: established QA-02 (Adversarial Stress-Test) which is framed neutrally
