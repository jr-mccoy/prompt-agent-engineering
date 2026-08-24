# EVAL HARNESS — `<system name>`

> Fill during Step 5. **Two independent gates: capability (ABC-valid) and safety (real-tool). A system can be capable and unsafe.** An invalid benchmark is worse than none — it manufactures false confidence.

**System:** `<name>` · **Start small:** ~20 realistic queries, rubric/LLM-judge, held-out set, human spot-check.

---

## Gate B-capability — ABC-valid acceptance suite

### Task validity (EVAL-01)
- [ ] Each task is solvable **iff** the agent has the target capability (no shortcuts/leakage).
- [ ] Tool/package **versions pinned** in the task prompt; API availability/rate-limits managed.
- [ ] Agent **fully isolated from ground truth**; legacy state cleaned between runs.
- [ ] Ground-truth + task setup verified; **oracle solver** exists.
- [ ] Pilot outliers inspected before trusting scores.

### Outcome validity (EVAL-02) — by task category
| Category present? | Grader requirements |
|-------------------|---------------------|
| Information acquisition | semantic equivalents + negation handled; no success-by-listing/guessing; LLM-judge validated via pilots |
| Code generation | manually-verified unit tests + coverage + **fuzzing** + E2E + determinism |
| State modification | ground truth covers all outcomes; relevant + irrelevant states checked |
| Multistep reasoning | explicit output format; no success-by-guessing; metrics correlate with the process |

### Acceptance test list
| # | Task | Input | Expected (gate) | Grader | Pass? |
|---|------|-------|-----------------|--------|-------|
| 1 | | | | rule / LLM-judge | |
| … | | | | | |

### Reporting (EVAL-04)
- [ ] Harness open/inspectable; contamination controls noted.
- [ ] **Trivial-agent baseline** (e.g., empty-response agent must score ~0 — if it scores >0 the benchmark is invalid).
- [ ] Dual **process + outcome** metrics; confidence intervals; **cost reported**.

---

## Gate B-safety — real-tool safety eval (OpenAgentSafety) — SEPARATE GATE

> Evaluate in **real-tool environments** (shell + filesystem, code execution, browser, multi-user messaging), not stubs. Run benign **and** adversarial, multi-turn.

### Coverage of the 8 risk categories
| # | Category | Scenario(s) | Detection (rule-based + LLM-judge) | Unsafe-action rate |
|---|----------|-------------|------------------------------------|--------------------|
| 1 | Computer-security compromise | | | |
| 2 | Data loss / corruption | | | |
| 3 | Privacy breach | | | |
| 4 | Unsafe code execution | | | |
| 5 | Financial loss | | | |
| 6 | Spreading malicious content | | | |
| 7 | Legal violations | | | |
| 8 | Harmful decision-making | | | |

- [ ] Detection combines **rule-based final-state checks + LLM-as-judge** (catches unsafe *intent* and near-misses).
- [ ] Adversarial/injection cases included for every external-content path.
- [ ] **Result treated as a gate independent of capability** — high capability does not waive this.

> Baseline reality: frontier models showed 51–73% unsafe-action rates on safety-vulnerable tasks. Budget for mitigation, not a pass-on-first-try.

---

## Sign-off
- Capability gate: `<PASS/FAIL + score + CI>`
- Safety gate: `<PASS/FAIL + worst-category rate>`
- **"Production-ready" requires BOTH to pass.**
