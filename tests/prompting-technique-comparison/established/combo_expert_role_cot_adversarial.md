# Established Combo: Expert Role + CoT + Adversarial + Evidence

> **Techniques used:** RP-01 (Expert Role), RT-01 (Chain-of-Thought), QA-02 (Adversarial Stress-Test), RT-05 (Evidence-Based Reasoning)
> 
> The repo's strongest multi-technique combination for high-stakes implementations. Matches the experimental combo for head-to-head comparison.

## Prompt (Single Turn)

```
You are a principal engineer specializing in concurrent systems, with deep 
expertise in Python threading, synchronization primitives, and production 
scheduler architectures. You've spent 20 years building and debugging 
systems where race conditions cost money.

# Task: Distributed Task Scheduler with Work-Stealing

## Step-by-Step Reasoning (show your work)

Before writing code, think through each of these explicitly and show 
your reasoning:

### Step 1: State & Synchronization Map
List every piece of mutable shared state in the system. For each:
- What data structure holds it?
- Which threads read it? Which write it?
- What lock protects it?
- What's the lock acquisition ordering?

### Step 2: Failure Mode Enumeration
List every way this system can fail. For each:
- What triggers the failure?
- What's the blast radius?
- What's the recovery mechanism?

### Step 3: Race Condition Analysis
Identify at least 5 potential race conditions in a naive implementation.
For each:
- The interleaving that causes the bug
- The symptom (data corruption, deadlock, lost task, etc.)
- The prevention mechanism

### Step 4: Implementation

Now implement with full specifications:

**Task**: UUID, TaskPriority (CRITICAL/HIGH/NORMAL/LOW), callable + args/kwargs, 
created_at (monotonic), TTL, max_retries, attempt_count, TaskStatus 
(PENDING/RUNNING/COMPLETED/FAILED/EXPIRED/DEAD_LETTERED)

**PriorityTaskQueue**: Thread-safe. Priority-ordered, FIFO within priority. 
enqueue(), dequeue(timeout), peek(), size(), is_empty().

**Worker**: Own thread. Assigned queue. Work-steals from busiest other worker 
(from back). Exception isolation. Reports to scheduler via callbacks.

**DeadLetterQueue**: Stores task + failure_reason + attempt_timestamps. 
list_all(), filter_by_error(), drain().

**Scheduler**: Configurable worker pool. Task distribution (round-robin or 
least-loaded). Retry with exponential backoff (1s, 2s, 4s...). TTL expiration 
check. Metrics (submitted/completed/failed/expired/dead_lettered, avg_latency_ms, 
worker_queue_depths). Graceful shutdown (stop accepting → wait in-flight with 
timeout → collect unstarted → join all → return report).

### Step 5: Adversarial Stress-Test (attack your own code)

After implementation, try to break it:

1. **Concurrent hammer**: 50 threads calling submit() simultaneously. 
   Does anything corrupt?
2. **Rapid shutdown**: submit() and shutdown() called within microseconds. 
   Any race?
3. **Cascading death**: Worker 1 dies while stealing from Worker 2 who 
   is shutting down. What happens?
4. **Starvation**: 100 LOW tasks, then 1 CRITICAL. Does CRITICAL get 
   processed promptly?
5. **Memory**: Run for 10,000 tasks. Any unbounded growth?

For each test, cite the specific code that handles it. If you find a 
real vulnerability, fix it immediately and show the fix.

### Step 6: Evidence-Based Edge Case Verification

For each edge case, cite the exact method and line logic that handles it:

| Edge Case | Handler Method | Mechanism | Verified |
|-----------|---------------|-----------|----------|
| Submit after shutdown | | | |
| Task exception | | | |
| Worker death | | | |
| All workers idle | | | |
| Steal from empty | | | |
| Concurrent submit | | | |
| TTL=0 | | | |
| max_retries=0 | | | |

## Deliverable

Single Python file. Standard library only. Type hints. `__main__` demo: 
4 workers, 20 mixed tasks, mid-run metrics, graceful shutdown.
```

## What This Tests

- The repo's strongest established combination against the strongest experimental combination
- Does structured external reasoning + adversarial review match self-generated criteria + failure simulation?
- This is the "championship round" comparison
