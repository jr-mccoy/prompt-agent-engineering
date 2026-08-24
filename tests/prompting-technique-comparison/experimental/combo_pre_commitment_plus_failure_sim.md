# Experimental Combo: Pre-Commitment (#1) + Failure Simulation (#2)

> **Hypothesis:** Combining self-defined criteria with bad-version-first priming produces the strongest quality improvement of any technique combination.

## Prompt (Multi-Turn)

### Turn 1 — Pre-Commitment Extraction

```
You are about to implement a complex concurrent system in Python. Before I tell 
you what it is, I need you to commit to quality standards.

List exactly 10 characteristics that distinguish production-grade concurrent Python 
code from prototype-quality code. Be specific and measurable.

For each, provide:
1. The characteristic (specific, measurable)
2. A code-level indicator of its presence
3. A code-level indicator of its absence
```

### Turn 2 — Failure Simulation with Task Reveal

```
Good. Now here's the task:

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

But DON'T implement it yet. First, write the BAD version — the one that 
violates your 10 standards. Make it realistic bad code, not a caricature. 
Then critique it against each of your 10 standards, showing exactly how 
it fails each one.
```

### Turn 3 — Production Implementation

```
Now write the real production version. Requirements:
- Single Python file, standard library only
- Type hints throughout
- Must satisfy ALL 10 of your committed standards
- Must fix ALL problems identified in your critique of the bad version
- Include __main__ demo: 4 workers, 20 mixed tasks, mid-run metrics, 
  graceful shutdown

After implementation, provide:

## Traceability Matrix

| My Standard # | Bad Version Violation | Production Fix (file:line) |
|---------------|----------------------|---------------------------|

## Self-Score

| Standard | Score (1-5) | Evidence |
|----------|-------------|----------|
```

## What This Tests

- Does the combination outperform either technique alone?
- Does self-defined criteria + bad-first create compounding quality pressure?
- Is the traceability matrix more meaningful than either technique's verification alone?
- This is the experimental condition the model creator was "most excited to test"
