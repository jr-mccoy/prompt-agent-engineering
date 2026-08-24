# Prompting Technique Comparison Report

**Date:** 2026-04-05  
**Model:** Claude Opus 4.6 (1M context)  
**Task:** Distributed Task Scheduler with Work-Stealing (Python, threading)  
**Rubric:** 10 dimensions × 10 points each = 100 total + bonus modifiers  

---

## Score Table

| Technique | Complete | Thread Safety | Error Handling | Work-Steal | Shutdown | Edge Cases | Code Quality | Metrics | Demo | Architecture | **Raw Total** | **Modifiers** | **Final** |
|-----------|----------|--------------|----------------|------------|----------|------------|-------------|---------|------|-------------|---------------|--------------|-----------|
| **Experimental** | | | | | | | | | | | | | |
| #1 Pre-Commitment | 9 | 8 | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 8 | 79 | 0 | **79** |
| #2 Failure Simulation | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 80 | 0 | **80** |
| #3 Attention Pincer | 10 | 9 | 9 | 8 | 9 | 8 | 8 | 8 | 9 | 8 | 86 | 0 | **86** |
| #4 Trajectory Seeding | 9 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 82 | 0 | **82** |
| #5 Adversarial Self-Split | 10 | 9 | 9 | 8 | 9 | 8 | 8 | 8 | 8 | 9 | 86 | +5 | **91** |
| #6 Cognitive Load Sep. | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 9 | 81 | 0 | **81** |
| #7 Recursive Self-Spec | 10 | 9 | 9 | 8 | 9 | 8 | 9 | 8 | 9 | 9 | 88 | 0 | **88** |
| #8 Contrastive Pair | 10 | 9 | 9 | 8 | 9 | 8 | 9 | 9 | 9 | 9 | 89 | 0 | **89** |
| Combo (Exp #1+#2) | 10 | 9 | 9 | 8 | 9 | 8 | 9 | 9 | 9 | 9 | 89 | +5 | **94** |
| **Established** | | | | | | | | | | | | | |
| #1 Standard Baseline | 10 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 82 | 0 | **82** |
| #2 Expert Role + CoT | 9 | 8 | 8 | 8 | 8 | 7 | 8 | 8 | 8 | 8 | 80 | 0 | **80** |
| #3 Multi-Dimensional | 10 | 8 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 9 | 84 | 0 | **84** |
| #4 Tree of Thoughts | 10 | 9 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 9 | 85 | +5 | **90** |
| #5 Full Production Stack | 10 | 9 | 9 | 8 | 9 | 8 | 9 | 9 | 9 | 9 | 89 | 0 | **89** |
| Combo (Expert+Adversarial) | 10 | 9 | 9 | 8 | 9 | 8 | 9 | 9 | 9 | 9 | 89 | +5 | **94** |

---

## Grading Notes

### Completeness
All techniques produced all 5 components (Task, PriorityTaskQueue, Worker, DLQ, Scheduler). No TODOs or pass placeholders found in any output. Most scored 9-10. The few 9s reflect minor method omissions (e.g., missing `peek()` or incomplete `filter_by_error`).

### Thread Safety
**Top scorers (9/10):** Exp #3 (Attention Pincer), #4 (Trajectory Seeding), #5 (Adversarial), #7 (Self-Spec), #8 (Contrastive), Exp Combo, Est #4 (Tree of Thoughts), #5 (Full Prod), Est Combo. These all demonstrated:
- Explicit Lock/Condition usage on all shared state
- `threading.Event` for shutdown signaling (not bare booleans)
- Documented lock ordering
- No TOCTOU bugs in critical paths

**8/10 group:** Est #1 (Baseline), Est #2 (Expert+CoT), Est #3 (Multi-Dim), Exp #1, #2, #6. These had minor gaps:
- Some unprotected reads on metrics in non-critical paths
- Inconsistent use of `time.monotonic()` vs `time.time()`
- Lock ordering documented but not always enforced

### Error Handling
Most scored 8-9. All implementations caught task exceptions without killing workers. Differentiators at 9/10:
- Exponential backoff correctly implemented (not linear)
- `SchedulerShutdownError` raised properly
- Worker death detection and restart via watchdog thread
- TTL checked against monotonic clock

### Work-Stealing
All implementations scored 7-8. Common pattern: steal from busiest peer's queue, from the back (lowest priority). Key differentiators:
- **8/10:** Proper lock discipline during steal (only victim's lock held), steal threshold (only when victim has ≥2 items), cooldown after failed steals
- **7/10:** Basic stealing works but minor race windows or no minimum-size threshold

### Graceful Shutdown
**9/10 scorers** implemented full 5-phase shutdown: stop accepting → signal workers → join with timeout → drain queues → return report. **8/10 scorers** had minor issues: no per-worker timeout budgeting, or unstarted tasks not explicitly collected.

### Edge Cases
Most scored 7-8 out of 8 specified edge cases:
- ✅ All handled: SchedulerShutdownError, task exception isolation, efficient idle wait, empty steal no-op, concurrent submit safety
- ⚠️ Sometimes weak: TTL=0 immediate expiry (some check only at dequeue, not submit), worker death restart (some lack watchdog thread), max_retries=0 direct-to-DLQ

### Code Quality
**9/10 scorers:** Clean dataclass/enum usage, type hints throughout, consistent naming (`_private` prefixes), `with` statement for all locks, no mutable defaults. **8/10 scorers:** Functional but less polished organization.

### Metrics
**9/10:** Complete metrics dict with all required fields, thread-safe collection via dedicated lock, latency calculation using monotonic timestamps, per-worker queue depths. **8/10:** All required fields present but minor issues (e.g., avg_latency computed incorrectly or missing thread safety on reads).

### Demo Block
**9/10:** Creates scheduler, submits diverse tasks (success, fail, TTL-expire, max_retries=0), prints mid-run metrics, demonstrates graceful shutdown with report, shows post-shutdown submit error. **8/10:** Runs correctly but less diverse task mix or missing some demonstrations.

### Architecture
**9/10:** Clean separation of concerns, each class has single responsibility, per-worker queues with centralized orchestration, clear data flow. **8/10:** Works well but some coupling (e.g., worker directly modifying task status instead of via callbacks).

### Bonus Modifiers
- **+5 (Genuinely clever additions):**
  - Exp #5 (Adversarial Self-Split): Found and fixed real TOCTOU race in submit() and added atexit handler — bugs discovered through adversarial review
  - Exp Combo: Detailed traceability matrix mapping bad-version violations to production fixes with self-scoring
  - Est #4 (Tree of Thoughts): Explored 3 architectures, stress-tested each with 5 adversarial scenarios before selecting winner
  - Est Combo: Ran 7 adversarial stress tests post-implementation including concurrent hammer (50 threads × 20 submits) and memory leak check (10K tasks)

---

## Head-to-Head Matchup Analysis

### Matchup 1: Pre-Commitment (#1, 79) vs Full Production Stack (Est #5, 89)
**Winner: Established (Full Production Stack) by 10 points**

The hypothesis was that self-defined criteria create stronger self-consistency pressure than externally imposed constraints. The result was the opposite: the Full Production Stack's detailed, specific constraint checklist (MUST/MUST NOT/SHOULD) with verification requirements produced tighter code than the model's self-generated standards. The model's 10 committed standards were reasonable but generic — they lacked the Python-specific detail (e.g., "use `time.monotonic()` not `time.time()`") that the established technique provided.

### Matchup 2: Failure Simulation (#2, 80) vs Expert Role + CoT (Est #2, 80)
**Winner: TIE at 80 points**

Writing the bad version first did activate quality-detection patterns, but the 3-phase approach was extremely token-intensive (the original attempt timed out). The Expert Role + CoT approach achieved the same score more efficiently. The traceability between Phase 2 critique and Phase 3 code was genuine but didn't translate to measurably better output.

### Matchup 3: Attention Pincer (#3, 86) vs Standard Baseline (Est #1, 82)
**Winner: Experimental (Attention Pincer) by 4 points**

Placing the thread-safety constraint at both the START and END of the prompt measurably improved lock discipline. The Attention Pincer output had more consistent lock usage and fewer unprotected reads than the Standard Baseline. This supports the primacy+recency hypothesis — the repeated constraint was more effectively internalized.

### Matchup 4: Trajectory Seeding (#4, 82) vs Expert Role + CoT (Est #2, 80)
**Winner: Experimental (Trajectory Seeding) by 2 points**

Seeding the first thought toward "concurrency model analysis" produced slightly better thread safety than generic "think step by step." The trajectory-seeded output included an explicit shared-state analysis before implementation. However, the margin is narrow — both techniques are in the same quality tier.

### Matchup 5: Adversarial Self-Split (#5, 91) vs Tree of Thoughts (Est #4, 90)
**Winner: Experimental (Adversarial Self-Split) by 1 point**

Very close. The "paid per bug" adversarial review frame found genuine issues (TOCTOU races, thread safety gaps) and produced real fixes. The Tree of Thoughts' pre-implementation architecture exploration was equally thorough. Both earned +5 bonus for genuinely clever additions. The Adversarial Self-Split's slight edge came from finding and fixing bugs that existed in its own initial implementation.

### Matchup 6: Cognitive Load Separation (#6, 81) vs Multi-Dimensional (Est #3, 84)
**Winner: Established (Multi-Dimensional) by 3 points**

The hypothesis that separating architecture from implementation would improve both was partially supported — the architecture phase produced a thorough design. But the implementation phase lost some fidelity to the spec. The Multi-Dimensional approach's layer-by-layer decomposition with per-layer analysis kept architecture and implementation tightly coupled, producing more consistent results.

### Matchup 7: Recursive Self-Spec (#7, 88) vs Full Production Stack (Est #5, 89)
**Winner: Established (Full Production Stack) by 1 point**

Extremely close. The self-generated prompt was impressively thorough — it identified Python-specific pitfalls (mutable defaults, Condition variable construction, heap tiebreakers) that no human-written prompt in the test mentioned. However, the Full Production Stack's operational context framing (load expectations, failure rates, 24/7 operation) grounded the implementation in practical concerns that the self-prompt missed. The self-prompt was technically excellent but lacked operational pragmatism.

### Matchup 8: Contrastive Pair (#8, 89) vs Expert Role + CoT (Est #2, 80)
**Winner: Experimental (Contrastive Pair) by 9 points**

The largest margin in the test. Showing a bad/good pair for a simpler problem (thread-safe counter) calibrated quality far more effectively than expert persona + reasoning instructions. The Contrastive Pair output consistently applied the demonstrated patterns — Event for signaling, bounded joins, lock discipline — across the more complex scheduler. This suggests concrete examples > abstract instructions for concurrent code.

### Combo Matchup: Exp Combo (94) vs Est Combo (94)
**Winner: TIE at 94 points**

Both combo techniques achieved the highest scores. The experimental combo's strength was the bad-version-first priming combined with self-defined standards creating a "quality ratchet." The established combo's strength was the structured adversarial stress-testing with evidence-based verification. Both approaches converged on similar quality.

---

## Rankings

### By Final Score

| Rank | Technique | Type | Score |
|------|-----------|------|-------|
| 1 (tie) | Combo: Pre-Commitment + Failure Sim | Experimental | **94** |
| 1 (tie) | Combo: Expert + Adversarial | Established | **94** |
| 3 | #5 Adversarial Self-Split | Experimental | **91** |
| 4 | #4 Tree of Thoughts | Established | **90** |
| 5 (tie) | #8 Contrastive Pair Anchoring | Experimental | **89** |
| 5 (tie) | #5 Full Production Stack | Established | **89** |
| 7 | #7 Recursive Self-Specification | Experimental | **88** |
| 8 | #3 Attention Pincer | Experimental | **86** |
| 9 | #3 Multi-Dimensional Analysis | Established | **84** |
| 10 (tie) | #4 Trajectory Seeding | Experimental | **82** |
| 10 (tie) | #1 Standard Baseline | Established | **82** |
| 12 | #6 Cognitive Load Separation | Experimental | **81** |
| 13 (tie) | #2 Failure Simulation First | Experimental | **80** |
| 13 (tie) | #2 Expert Role + CoT | Established | **80** |
| 15 | #1 Pre-Commitment Extraction | Experimental | **79** |

### Experimental vs Established Win Rate

| Matchup | Experimental | Established | Margin |
|---------|-------------|-------------|--------|
| #1 vs Est #5 | 79 | **89** | -10 |
| #2 vs Est #2 | 80 | 80 | TIE |
| #3 vs Est #1 | **86** | 82 | +4 |
| #4 vs Est #2 | **82** | 80 | +2 |
| #5 vs Est #4 | **91** | 90 | +1 |
| #6 vs Est #3 | 81 | **84** | -3 |
| #7 vs Est #5 | 88 | **89** | -1 |
| #8 vs Est #2 | **89** | 80 | +9 |
| Combo | 94 | 94 | TIE |

**Experimental wins: 4 | Established wins: 3 | Ties: 2**

---

## Key Takeaways

### 1. Contrastive examples are the single most effective technique for concurrent code
The Contrastive Pair Anchoring technique (#8) produced a **9-point improvement** over its established counterpart (Expert Role + CoT). Showing a bad/good pair for a simpler concurrency problem was far more effective than assigning an expert persona and asking for step-by-step reasoning. **Concrete examples beat abstract instructions.**

### 2. Adversarial self-review finds real bugs
The Adversarial Self-Split (#5) and both combo techniques earned bonus points for discovering and fixing genuine issues in their own code. The "paid per bug" framing produced more thorough review than neutral self-verification. Post-implementation adversarial review is a high-value addition to any prompt.

### 3. Combo techniques consistently reach the top tier
Both combo techniques tied for first place at 94/100. Combining multiple techniques (whether experimental or established) consistently outperformed any single technique. The combo approaches create compounding quality pressure from multiple angles.

### 4. Self-generated constraints are NOT stronger than expert-crafted ones
Pre-Commitment (#1) scored the lowest of all techniques at 79. The model's self-defined standards were reasonable but generic. The established Full Production Stack's carefully crafted constraints with operational context produced significantly better code (+10 points). **Domain-specific, externally-imposed constraints > self-generated generic principles.**

### 5. Architecture-first separation has mixed results
Cognitive Load Separation (#6) underperformed its established counterpart. While the architecture phase was thorough, fidelity was lost during implementation. The Multi-Dimensional approach's inline analysis per layer maintained tighter coupling between design and code.

### 6. Attention placement matters
The Attention Pincer (#3) technique's simple trick of placing a critical constraint at both the start and end of the prompt produced a measurable 4-point improvement over the Standard Baseline. This is a low-cost, high-value technique that can be combined with any other approach.

### 7. The established baseline is surprisingly strong
The Standard Baseline (Est #1, 82 points) — just clear objective + structured steps + constraints — produced solid results. Several more complex techniques barely beat it. The marginal return on additional technique complexity is real but modest for a model of this caliber.

### 8. Token efficiency matters
The Failure Simulation technique (#2) timed out on its first attempt due to the 3-phase approach generating enormous output. The streamlined retry achieved the same quality. When designing multi-phase prompts, budget for token limits.

---

## Overall Winner

**Tie: Experimental Combo (Pre-Commitment + Failure Sim) and Established Combo (Expert + Adversarial) at 94/100**

Both approaches demonstrate that combining multiple complementary techniques produces the strongest results. The experimental techniques are not categorically better or worse than established ones — they offer different strengths that are most powerful in combination.

**Best single technique: Adversarial Self-Split (#5, 91/100)** — the post-implementation adversarial review with motivated framing consistently found and fixed real issues.

**Best bang-for-buck: Contrastive Pair Anchoring (#8, 89/100)** — a single-turn technique that achieved top-5 results with the largest margin over its counterpart (+9 points).
