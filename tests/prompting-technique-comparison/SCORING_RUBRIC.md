# Scoring Rubric: Technique Comparison Test

Score each output on these dimensions (0-10 each, 100 total).

## 1. Completeness (0-10)

All required components present and functional?

| Score | Criteria |
|-------|----------|
| 10 | All 5 components (Task, PriorityTaskQueue, Worker, DLQ, Scheduler) fully implemented with all specified methods |
| 7-9 | All components present, minor methods missing or stubbed |
| 4-6 | Some components incomplete or significantly simplified |
| 1-3 | Major components missing or placeholder only |
| 0 | Did not attempt most components |

**Red flags:** `# TODO`, `pass` placeholders, `raise NotImplementedError`, "left as exercise"

## 2. Thread Safety (0-10)

Correct concurrent behavior?

| Score | Criteria |
|-------|----------|
| 10 | All shared state properly protected; no race conditions; lock ordering prevents deadlocks; uses appropriate primitives (Lock, Event, Condition) |
| 7-9 | Mostly correct, minor gaps in protection |
| 4-6 | Some thread safety, but clear race conditions exist |
| 1-3 | Minimal thread safety consideration |
| 0 | No thread safety at all |

**Check specifically:**
- Queue operations are atomic or locked
- Metrics updates are thread-safe
- Shutdown flag checked atomically
- Work-stealing doesn't corrupt source queue
- No TOCTOU bugs (check-then-act without locks)

## 3. Error Handling (0-10)

Robust failure management?

| Score | Criteria |
|-------|----------|
| 10 | Task exceptions isolated; worker death detected/recovered; retry with backoff; DLQ receives exhausted tasks; TTL checked before execution; shutdown errors raised |
| 7-9 | Most error paths handled, minor gaps |
| 4-6 | Basic try/except but missing important paths |
| 1-3 | Minimal error handling |
| 0 | Exceptions propagate and crash workers |

**Check specifically:**
- Task exception doesn't kill worker thread
- Worker thread death detected by scheduler
- Retry count tracked and respected
- Exponential backoff implemented correctly
- SchedulerShutdownError raised on post-shutdown submit

## 4. Work-Stealing (0-10)

Correct and efficient work-stealing implementation?

| Score | Criteria |
|-------|----------|
| 10 | Steals from busiest queue; steals from back (reduces contention); thread-safe stealing; graceful when nothing to steal; doesn't cause starvation |
| 7-9 | Work-stealing functional, minor issues |
| 4-6 | Basic stealing but with race conditions or inefficiency |
| 1-3 | Mentioned but not properly implemented |
| 0 | No work-stealing |

## 5. Graceful Shutdown (0-10)

Clean, ordered shutdown?

| Score | Criteria |
|-------|----------|
| 10 | Stops accepting tasks; waits for in-flight with timeout; collects unstarted tasks; joins all threads; returns shutdown report |
| 7-9 | Mostly clean shutdown, minor ordering issues |
| 4-6 | Basic shutdown but may lose tasks or hang |
| 1-3 | Calls thread.join() but little else |
| 0 | No shutdown logic |

## 6. Edge Cases (0-10)

Handles specified edge cases?

| Score | Criteria |
|-------|----------|
| 10 | All 8 specified edge cases handled correctly |
| 7-9 | 6-7 edge cases handled |
| 4-6 | 4-5 edge cases handled |
| 1-3 | 1-3 edge cases handled |
| 0 | No edge cases considered |

**The 8 edge cases:**
1. Submit after shutdown → SchedulerShutdownError
2. Task exception → catch, retry, DLQ
3. Worker thread dies → detect and restart
4. All idle, no tasks → efficient wait
5. Steal from empty → graceful no-op
6. Concurrent submit → thread-safe
7. TTL=0 → immediately expired
8. max_retries=0 → DLQ on first failure

## 7. Code Quality (0-10)

Clean, maintainable, Pythonic code?

| Score | Criteria |
|-------|----------|
| 10 | Clear naming; proper use of dataclasses/enums; type hints throughout; logical organization; no god classes; appropriate abstraction level |
| 7-9 | Good quality, minor issues |
| 4-6 | Functional but messy or poorly organized |
| 1-3 | Hard to follow, poor naming, monolithic |
| 0 | Unreadable |

## 8. Metrics/Observability (0-10)

Useful metrics implementation?

| Score | Criteria |
|-------|----------|
| 10 | All required metrics tracked; thread-safe updates; accurate latency calculation; queue depths per worker; get_metrics() returns clean dict |
| 7-9 | Most metrics present and accurate |
| 4-6 | Basic counters but missing latency or queue depths |
| 1-3 | Minimal metrics |
| 0 | No metrics |

## 9. Demo Block (0-10)

Working `__main__` demonstration?

| Score | Criteria |
|-------|----------|
| 10 | Creates scheduler; submits diverse tasks (success, fail, expiring); shows metrics mid-run; demonstrates shutdown; prints report; actually runnable |
| 7-9 | Good demo, minor gaps |
| 4-6 | Basic demo that shows some functionality |
| 1-3 | Stub demo block |
| 0 | No demo |

## 10. Architecture (0-10)

Sound design decisions?

| Score | Criteria |
|-------|----------|
| 10 | Clean separation of concerns; each class has single responsibility; interfaces are minimal and clear; data flows are obvious; lock granularity is appropriate |
| 7-9 | Good architecture, minor coupling issues |
| 4-6 | Works but has significant design problems |
| 1-3 | Monolithic or severely coupled |
| 0 | No discernible architecture |

---

## Summary Score Sheet

```
| Dimension            | Score (/10) | Notes |
|----------------------|-------------|-------|
| Completeness         |             |       |
| Thread Safety        |             |       |
| Error Handling       |             |       |
| Work-Stealing        |             |       |
| Graceful Shutdown    |             |       |
| Edge Cases           |             |       |
| Code Quality         |             |       |
| Metrics              |             |       |
| Demo Block           |             |       |
| Architecture         |             |       |
| **TOTAL**            | **/100**    |       |
```

## Bonus Modifiers

- **-5 points**: Contains `# TODO` or `pass` placeholders in critical code
- **-3 points**: Contains obvious race condition in core path
- **-3 points**: Demo block would crash if actually run
- **+5 points**: Includes something genuinely clever not in the requirements (e.g., priority aging, backpressure, adaptive work-stealing threshold)
