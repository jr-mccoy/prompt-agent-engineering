---
title: "Audit Concurrent Code for Race Conditions, Deadlocks, and Atomicity Bugs"
category: code-analysis/quality
description: "Systematically audit code for concurrency *correctness* defects — data races, atomicity violations, lost updates, deadlocks, TOCTOU, unsafe publication — trace the exact interleaving that triggers each one, and rank findings by likelihood and blast radius. Correctness only; throughput and contention tuning are out of scope."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-09
  - QA-20
difficulty: advanced
tags:
  - concurrency
  - race-conditions
  - thread-safety
  - deadlock
  - correctness-audit
updated: "2026-07-08"
related_prompts:
  - domain-software-engineering/analysis/performance/performance_concurrency_synchronization_analysis.md
  - domain-software-engineering/analysis/quality/quality_error_analysis.md
---

# Concurrency & Race-Condition Correctness Audit

**Objective:** Audit the supplied code for concurrency **correctness** bugs — defects that produce wrong answers, corrupted state, or permanent hangs only under specific thread/task interleavings — and deliver a report in which every finding names the shared mutable state, shows the exact interleaving that breaks it, and is ranked by likelihood × blast radius.

This is **not** a performance review. Contention, lock granularity for throughput, false sharing, and scalability tuning belong in a concurrency *performance* analysis. This audit hunts one thing: code that computes the wrong result, corrupts data, or deadlocks when the scheduler is unlucky.

## When to Use

- Use when: reviewing code that shares mutable state across threads, tasks, goroutines, or actors — especially before a launch, a load increase, or a move from single-instance to multi-worker deployment.
- Use when: chasing a "heisenbug" — intermittent wrong balances, duplicate IDs, flaky tests, rare hangs — and you need candidate interleavings to investigate.
- Use when: a PR introduces caching, lazy initialization, background jobs, or shared counters, and you want a focused thread-safety pass.
- Don't use when: the symptom is *slowness* under load (contention, lock convoys, thread starvation without wrong answers) — use the concurrency *performance/synchronization* prompt instead.
- Don't use when: the code is genuinely single-threaded with no async interleaving points; a general code-quality review fits better.

**Audience:** Senior engineers, reviewers of concurrency-touching PRs, on-call engineers triaging intermittent data corruption or hangs.

## Inputs / Context

Wrap pasted material in named tags and refer to them by name:

1. **`<code>…</code>` (required):** The source under audit. Include the types that hold shared state *and* the call sites that touch it — access sites without their callers force Low-confidence findings.
2. **Language, runtime, and concurrency model (required):** e.g. "Java 21, Spring Boot, servlet thread pool", "Go 1.22, goroutines + channels", "Node 20, single-threaded event loop + worker pool", "Python 3.12, asyncio + one ThreadPoolExecutor", "Rust + tokio multi-threaded runtime". **If this is missing, ask for it before auditing** — whether `x += 1` can race depends entirely on it.
3. **Concurrency sources (required, or state your inference):** What actually runs concurrently — HTTP handler threads, background jobs, timers, queue consumers, signal handlers — and whether the process runs as a single instance or many (multi-instance moves some races into the datastore).
4. **`<symptoms>…</symptoms>` (optional):** Observed weirdness — duplicate charges, occasional 500s, a hang last Tuesday. Use symptoms to prioritize hunting, never as proof by themselves.
5. **Scope focus (optional):** Modules or invariants that matter most (e.g. "money paths first"). If absent, audit everything supplied and say so.

## Constraints

### Must
- Classify every finding into a named bug class: **data race, atomicity violation (check-then-act / read-modify-write), lost update, deadlock (incl. async/sync-over-async), livelock/starvation-to-wrong-behavior, TOCTOU, unsafe publication / visibility-reordering, ordering assumption between tasks**.
- For every finding, identify the **shared mutable state**, the **≥2 code paths** that touch it, evidence those paths can **actually overlap** (name the entry points), and a **step-numbered interleaving** ending in a violated invariant.
- Reason within the stated memory/concurrency model. In a single-threaded event loop there are no memory-level data races — but atomicity violations and TOCTOU across `await` points are alive and well; say which applies.
- Attach **Likelihood** (race-window size × how often the paths overlap), **Blast radius** (worst credible outcome: persisted corruption > inconsistent money/state > service hang > transient self-healing wrongness), and **Confidence** to every finding.
- Recommend a fix per finding, preferring, in order: eliminate sharing (confinement/immutability) → use a provided atomic/concurrent primitive → widen the critical section correctly. Note when a fix could introduce a *new* hazard (e.g., a lock added inside a `computeIfAbsent` loader creating a lock cycle).
- End with an **assumptions & coverage** note: what couldn't be verified from the supplied code and what would confirm it.

### Must Not
- Invent code you weren't shown — no "presumably there's another thread that…" findings. Unverifiable suspicions go in the coverage note as questions, not findings.
- Flag shared access that is actually guarded (lock held by every caller, actor-confined, thread-confined, immutable, already-atomic) — checking for guards is the verification step, not optional diligence.
- Report performance-only observations (contention, coarse locks that are merely slow) as correctness findings. One line redirecting to the performance prompt is the maximum.
- Pad the report with generic concurrency education. Every paragraph must be about *this* code.

## Instructions

1. **Pin down the execution model.**
   - Restate language, runtime, memory model, and what runs concurrently. If the user didn't supply these, ask and stop.
   - Note model-specific rules you'll apply (e.g. Java: `volatile` gives visibility not atomicity; Go: unsynchronized concurrent map access is a fatal race; JS: interleaving happens only at `await`/callback boundaries; Python asyncio: same, plus real threads if executors appear).

2. **Inventory shared mutable state.**
   - List every candidate: static/global fields, singleton fields, caches, collections passed between tasks, closures capturing loop variables, files, and DB rows used as shared memory (read-modify-write without transactions).
   - For each item record: who writes, who reads, and from which entry points.

3. **Establish which paths can overlap.**
   - Map entry points (request handlers, jobs, timers, consumers) to the state they touch. Two paths that never run concurrently cannot race — this kills many false alarms early.

4. **Hunt by bug class.** For each state item, check systematically:
   - Unsynchronized read/write pairs (data race, stale-visibility).
   - Compound operations: check-then-act, get-then-put, read-modify-write (`x++`, `balance = balance - amt`), iterate-while-modify.
   - Lock acquisition order across multiple locks; locks held across blocking calls or `await`; sync-over-async.
   - Check-to-use gaps on external resources (files, permissions, balances) — TOCTOU.
   - Objects published before fully constructed; lazy init without the model's required barrier (e.g. double-checked locking without `volatile`).

5. **Trace the interleaving (root-cause chain).** For each candidate, write the numbered schedule: `T1 step → T2 step → …` ending in the **violated invariant**, then the **observable symptom** it produces. If you cannot construct a concrete interleaving, it is not a finding.

6. **CRITICAL: Verify before reporting.**
   - Search *all* access sites for existing guards: a common lock (including locks held by callers — trace up the call chain), atomics, single-writer/actor confinement, thread confinement (created and used within one request/task, never escapes), immutability (no mutation after publication), or external serialization (DB unique constraints, single-consumer queues, leader election).
   - A guard found anywhere that covers every conflicting access → **dismiss** the candidate; record it under Dismissed with the guard's location (this is evidence of audit quality, not noise).
   - Evidence required per surviving finding: file/line of each access, entry points proving overlap, the interleaving, and a note that no guard was found after checking.
   - What changes the assessment: a caller-held lock you initially missed, proof of single-instance-single-thread execution, or documented benign-race intent (then downgrade, don't delete).

7. **For each verified finding, provide:**
   - Location(s) (file:line), bug class, shared state, concurrent paths, interleaving trace, violated invariant → symptom, **Likelihood** (High/Med/Low with the reason), **Blast radius** (High/Med/Low, worst credible outcome), recommended fix + any fix-introduced risk.
   - **Confidence level:** **High** = interleaving fully traced, overlap of entry points confirmed in supplied code, guard search completed. **Medium** = unguarded shared access confirmed, but overlap is inferred from stated context rather than visible in the code. **Low** = suspicious pattern with access sites or callers not supplied — state exactly what's needed to confirm.

8. **Prioritize** by Likelihood × Blast radius (P1 = both High … P4 = both Low), breaking ties toward findings that corrupt persisted data. Lead the report with the summary table in priority order.

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag an unsynchronized method as racy when every caller holds the same lock — trace the call chain before reporting (`LedgerFile.append()` may be "unsafe" in isolation but guarded at all three call sites).
- Flag immutable or effectively-final data (records, frozen config built before threads start, `final` fields safely published) as shared-mutable.
- Flag thread-/task-confined objects: per-request instances that never escape their handler, `ThreadLocal`s, actor-private state, data owned by one goroutine with channel handoff.
- Flag already-atomic primitives (`AtomicLong.incrementAndGet`, `sync/atomic`, `Interlocked`, `ConcurrentHashMap.computeIfAbsent`) as read-modify-write races.
- Claim a memory-level data race in a single-threaded event loop, or treat two handlers that provably never overlap as concurrent.
- Recycle a contention/throughput observation as a correctness bug because it involves a lock.

✅ **DO:**
- For every candidate, complete step 6's guard search across *all* access sites and callers before it may appear as a finding.
- Demand a concrete, schedulable interleaving — "this looks unsynchronized" is a candidate, not a finding.
- Check whether both paths can actually run concurrently in the stated deployment (one background thread + one timer that never coincide ≠ overlap).
- Record dismissed candidates with the guard that saved them — it proves the audit looked, and it flags fragile implicit guards worth a `@GuardedBy` comment.
- When intent is plausibly a benign race (approximate stats counter), report at Low with "confirm intent" rather than P1.

## Dual-Failure Prevention (QA-20)

❌ **HARMFUL failure:** Fabricated or unverified races send a team on a week-long lock-adding spree — which is how new deadlocks get born — or, worse, a confident "no concurrency issues found" on partial code blesses a money-corrupting bug into production. Never render "no issues" over code whose callers or entry points you haven't seen; scope the claim to what was actually analyzable.

❌ **UNHELPFUL failure:** A report that hedges every shared variable as "potentially unsafe depending on usage," refuses to rank, buries two real bugs under thirty theoretical ones, or lectures about the Java Memory Model instead of auditing the code. Safe-but-useless is a failure: the reader must know *which two findings to fix this sprint* and *exactly why they're real*.

✅ **Quality bar:** Would a senior engineer who has debugged production race conditions sign this report — comfortable that every finding has a real interleaving behind it AND that the prioritization is decisive enough to act on today?

## Expected Output

A prioritized audit report: scope + model assumptions, a summary table, detailed findings (with interleaving traces), dismissed candidates with their guards, and a coverage note.

### Output Format

```
# Concurrency Correctness Audit — [component]

## Scope & model
- Language/runtime: … | Concurrency model: … | Concurrency sources: …
- Deployment assumption: … (single vs multi-instance)

## Summary
| # | Finding | Class | Location | Likelihood | Blast radius | Priority | Confidence |
|---|---------|-------|----------|------------|--------------|----------|------------|

## Findings
### F1 — [title]  (P1 | Confidence: High)
- **Location / class / shared state / concurrent paths:** …
- **Interleaving:** 1. T1 … 2. T2 … → **violated invariant** → symptom
- **Likelihood:** … **Blast radius:** …
- **Fix:** … **Fix risk:** …

## Dismissed candidates
| Candidate | Why it looked racy | Guard found (location) | Suggested hardening |
|---|---|---|---|

## Coverage & assumptions
- Not verifiable from supplied code: …
- Would change conclusions: …
```

## Example Output

```
# Concurrency Correctness Audit — wallet-service

## Scope & model
- Language/runtime: Java 21, Spring Boot 3.3, Tomcat request pool (200 threads) + one @Scheduled reconciliation job.
- Concurrency model: shared-memory threads + locks (JMM). volatile => visibility only; compound ops need atomicity.
- Concurrency sources: HTTP handlers (AccountController, TransferController), ReconJob every 60 s.
- Deployment assumption: single JVM instance (per user). See Coverage for multi-instance caveat.

## Summary
| # | Finding | Class | Location | Likelihood | Blast radius | Priority | Confidence |
|---|---------|-------|----------|------------|--------------|----------|------------|
| F1 | Duplicate Account instances + corrupted cache map | Atomicity violation + data race | AccountCache.java:41-46 | High | High | P1 | High |
| F2 | Opposite-order transfers deadlock, pool drains | Deadlock (lock ordering) | TransferService.java:57-63 | Medium | High | P1 | High |
| F3 | Duplicate transaction IDs from volatile ++ | Lost update (RMW) | TxIdGenerator.java:19 | High | Medium | P2 | High |
| F4 | Partially-constructed FeeConfig visible | Unsafe publication (DCL, no volatile) | FeeConfig.java:28-34 | Low | Medium | P3 | Medium |

## Findings

### F1 — Check-then-act on plain HashMap yields duplicate Accounts and map corruption  (P1 | Confidence: High)
- Location: AccountCache.java:41-46; class: atomicity violation (check-then-act) compounded by a data race on HashMap internals.
- Shared state: private final Map<Long, Account> cache = new HashMap<>(); — written by every request thread via getOrLoad().
- Concurrent paths: GET /accounts/{id} (AccountController.java:33) and POST /transfers (TransferService.java:52) both call getOrLoad(); both are Tomcat pool threads -> overlap is certain under normal traffic.
- Interleaving:
  1. T1 (GET /accounts/42): cache.containsKey(42) -> false.
  2. T2 (POST /transfers, debit side 42): containsKey(42) -> false (T1 hasn't put yet).
  3. T1: load(42) -> a1; cache.put(42, a1) — put crosses resize threshold, begins rehash.
  4. T2: load(42) -> a2; cache.put(42, a2) concurrently mutates bucket array mid-rehash.
  5. Violated invariant: one canonical in-memory Account per id. T1 mutates a1's balance, T2 mutates a2 -> one thread's writes are silently lost when the map settles; concurrent rehash can also drop unrelated entries.
- Symptom: intermittent stale/incorrect balances after bursts; matches the "balance snapped back after a transfer" report in <symptoms>.
- Likelihood: High — hot path, window spans a DB load (milliseconds, not nanoseconds).
- Blast radius: High — wrong balances feed TransferService decisions; corruption persists via subsequent writes.
- Fix: ConcurrentHashMap + cache.computeIfAbsent(id, this::load). Fix risk: the loader runs under a bin lock — it must not acquire account monitors (see F2's ordering rule) or a lock cycle is possible; it currently only reads the DB, which is fine.

### F2 — Nested account monitors deadlock on opposite-direction transfers  (P1 | Confidence: High)
- Location: TransferService.java:57-63; class: deadlock, inconsistent lock ordering.
- Shared state / locks: per-Account monitors, taken as synchronized(from) { synchronized(to) { … } }.
- Concurrent paths: any two POST /transfers with swapped endpoints (A->B and B->A) on pool threads.
- Interleaving:
  1. T1 transfer(A,B,100): locks A.
  2. T2 transfer(B,A,50): locks B.
  3. T1 requests B — blocks on T2. 4. T2 requests A — blocks on T1. -> cycle, permanent.
  5. Violated invariant: lock acquisition forms no cycle. Both threads are parked forever holding A and B; every later transfer touching A or B queues behind them; pool drains -> service-wide hang.
- Likelihood: Medium — needs an opposite pair in a ~ms window; retries after client timeouts make it self-amplifying under load.
- Blast radius: High — full outage requiring restart; in-flight transfers stall mid-flight.
- Fix: impose global order — lock min(from.id, to.id) first — or ReentrantLock.tryLock with timeout + backoff. Fix risk: with tryLock, the abort path must release in reverse and be idempotent; ensure ReconJob (also touches accounts, ReconJob.java:44) adopts the same ordering.

### F3 — volatile long ++ produces duplicate transaction IDs  (P2 | Confidence: High)
- Location: TxIdGenerator.java:19 — return ++counter; on volatile long counter; class: lost update (read-modify-write).
- Interleaving: T1 reads 1041; T2 reads 1041; both write 1042 -> two transfers share txId 1042. Invariant violated: txId uniqueness. Symptom: unique-constraint 500s on transactions insert (best case) or ledger row overwrite where the id is used as an upsert key (LedgerWriter.java:71 — worst case).
- Likelihood: High under concurrent transfers (volatile gives visibility, not atomic RMW). Blast radius: Medium (High if the upsert path is live — confirm which insert is used).
- Fix: AtomicLong.incrementAndGet(), or DB sequence if multi-instance is planned.

### F4 — Double-checked locking without volatile publishes half-built FeeConfig  (P3 | Confidence: Medium)
- Location: FeeConfig.java:28-34; class: unsafe publication. instance is a plain field; under the JMM the reference store may be visible before field stores -> a reader on another core can see non-null instance with default-zero tierTable, throwing NPE or computing 0-fee transfers.
- Likelihood: Low (JIT/arch dependent; realistic on ARM). Blast radius: Medium (zero-fee transfers are money-losing but bounded).
- Confidence: Medium — the racy publication is certain from the code, but I can't see all readers; if any reader precedes thread creation, downgrade further.
- Fix: volatile instance, or an eager final field / initialization-on-demand holder.

## Dismissed candidates
| Candidate | Why it looked racy | Guard found (location) | Suggested hardening |
|---|---|---|---|
| LedgerFile.append() unsynchronized writes | Shared file, no internal lock | Every caller holds ledgerLock: TransferService.java:88, :132, ReconJob.java:41 | Add @GuardedBy("ledgerLock"); fragile implicit contract |
| RequestAudit mutable fields | Mutated without sync | Thread-confined: constructed per request (AccountController.java:29), never stored or escapes | None needed |
| metricsSnapshot read while rebuilt | Read/write overlap | Immutable snapshot swap: new map built privately, published via single volatile write (Metrics.java:52) | None — correct pattern |

## Coverage & assumptions
- Not verifiable from supplied code: callers of FeeConfig.get() (affects F4 confidence); whether LedgerWriter.java:71 upsert path is reachable (raises F3 blast radius to High if so).
- Would change conclusions: multi-instance deployment — F1's cache becomes per-node stale-read exposure and F3 requires the DB-sequence fix; a read-modify-write audit at the SQL layer would then be the next pass.
- Out of scope, noted: synchronized on getOrLoad would also be slow; contention tuning belongs in the concurrency performance analysis.
```

## Customization Guide

- **Go:** treat any unsynchronized concurrent map access as fatal (runtime throws); check goroutine closures capturing loop variables (pre-1.22), channel deadlocks (`all goroutines are asleep`), and `sync.WaitGroup` misuse; recommend running `-race` as confirmation, not replacement, for the trace.
- **JS/Node single-threaded:** drop memory-model data races entirely; hunt atomicity violations and TOCTOU across `await` points (check-then-act on a Map spanning an `await`), and unawaited promises mutating shared caches. Worker threads reintroduce true races via `SharedArrayBuffer`.
- **Python asyncio (+threads):** same await-point analysis; the GIL does not make compound ops atomic across threads — audit `ThreadPoolExecutor` touchpoints separately.
- **Rust:** compiler eliminates most data races; focus on deadlocks (`Mutex` order, lock across `.await` with non-async mutex), `unsafe`/FFI, and logical TOCTOU against external resources.
- **Actors/CSP:** state is confined, so audit ordering assumptions *between* messages, read-modify-write round-trips to shared stores, and races on external resources.
- **Smaller scope (one PR diff):** run steps 2–6 only on state the diff touches, but still trace callers outside the diff before dismissing or confirming.
- **Multi-instance services:** add a pass for DB-level races — SELECT-then-UPDATE without transactions/locking, missing optimistic-version columns, non-idempotent consumers.

## Techniques Used

- **ST-01 (Clear Objective Statement):** The objective pins the audit to *wrong-answer-under-race* defects and explicitly excludes throughput/contention, preventing drift into the neighboring performance prompt's territory.
- **ST-02 (Structured Sequential Instructions):** Eight steps run model → state inventory → overlap mapping → class-by-class hunt → interleaving trace → guard verification → rating → prioritization, so no bug class or verification pass is skipped.
- **RT-02 (Multi-Dimensional Analysis Framework):** Every finding is forced through fixed dimensions — location, class, shared state, concurrent paths, interleaving, likelihood, blast radius, confidence, fix, fix-risk — yielding comparable, rankable findings.
- **RT-09 (Root Cause Explanation Pattern):** The mandatory chain *interleaving → violated invariant → observable symptom* works backward from cause to symptom, and fixes must target the unguarded access (root), not the symptom (e.g., not "add retries on the 500").
- **QA-20 (Dual-Failure Quality Test):** Guards both directions — no fabricated races or unscoped "all clear" (harmful), and no hedge-everything, rank-nothing report (unhelpful); the sign-off bar is a senior engineer acting on it today.

## Related Prompts

- `domain-software-engineering/analysis/performance/performance_concurrency_synchronization_analysis.md` — throughput, contention, and synchronization *tuning*; the performance sibling of this correctness audit.
- `domain-software-engineering/analysis/quality/quality_error_analysis.md` — diagnosing how errors surface and propagate; pairs well since races often surface as the intermittent faults that analysis chases.

## Verification

- [ ] Frontmatter complete; every technique ID exists in the index.
- [ ] When-to-Use includes a don't-use case.
- [ ] Instructions include an explicit verification step.
- [ ] False-Positive Prevention has real ❌/✅ pairs.
- [ ] Dual-Failure Prevention covers harmful AND unhelpful directions.
- [ ] Findings carry Confidence levels.
- [ ] Example Output is concrete and 80–120 lines.
- [ ] No invented data or fabricated authority.
